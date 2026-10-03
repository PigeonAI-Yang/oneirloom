from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "SOURCE-MANIFEST.json"
POINTER_PREFIX = b"version https://git-lfs.github.com/spec/v1"
DEFAULT_ZIP_TIMESTAMP = (2026, 10, 2, 0, 0, 0)
PUBLIC_FILES = (
    ".agents/plugins/marketplace.json",
    ".codex-plugin/plugin.json",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
    "assets/icon.svg",
    "docs/COMPATIBILITY.md",
    "docs/INSTALL.md",
    "docs/SAFETY.md",
    "docs/model-evidence.md",
    "docs/releases/0.2.0-preview.1.md",
    "plugin.json",
    "scripts/build_plugin.py",
    "scripts/verify_plugin.py",
)
CACHE_DIRS = {
    "__pycache__", ".cache", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    ".tox", ".venv", "node_modules",
}
PRIVATE_SKILL_PREFIXES = (
    "skills/oneirloom-expression-stickers/assets/",
    "skills/oneirloom-prompt-card/assets/oneirloom-signature",
    "skills/oneirloom-prompt-card/assets/oneirloom-woven-signature",
)
PRIVATE_SKILL_FILES = {
    "skills/oneirloom-expression-stickers/templates/eight-slot-workspace/workspace.svg",
    "skills/oneirloom-expression-stickers/templates/eight-slot-workspace/workspace-preview.png",
}
HEX64 = re.compile(r"\A[0-9a-f]{64}\Z")
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\s*\r?\n|\Z)", re.S)


def fail(message):
    raise SystemExit(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def run_git(*arguments, input_bytes=None):
    result = subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode not in (0, 1):
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        fail("Git command failed: " + " ".join(arguments) + (": " + detail if detail else ""))
    return result


def safe_relative_path(name):
    if (
        not isinstance(name, str)
        or not name
        or "\\" in name
        or name.startswith("/")
        or name != name.strip()
        or any(part in ("", ".", "..") for part in name.split("/"))
        or len(name.split("/")) > 20
    ):
        fail("Unsafe inventory path: " + repr(name))
    return PurePosixPath(name)


def git_status_without_manifest():
    return run_git(
        "status", "--porcelain=v1", "--untracked-files=all",
        "--", ".", ":(exclude)SOURCE-MANIFEST.json",
    ).stdout


def git_ignored_paths(paths):
    if not paths:
        return set()
    payload = b"\0".join(os.fsencode(path) for path in paths) + b"\0"
    result = run_git("check-ignore", "--no-index", "-z", "--stdin", input_bytes=payload)
    if result.returncode == 1:
        return set()
    if result.returncode != 0:
        fail("git check-ignore failed")
    return {item.decode("utf-8") for item in result.stdout.split(b"\0") if item}


def discover_package_paths():
    skill_root = ROOT / "skills"
    if not skill_root.is_dir():
        fail("skills/ is missing")
    candidates = []
    for path in skill_root.rglob("*"):
        relative = path.relative_to(ROOT).as_posix()
        if any(part.casefold() in CACHE_DIRS for part in PurePosixPath(relative).parts):
            continue
        if path.is_symlink() or not path.is_file():
            continue
        candidates.append(relative)
    ignored = git_ignored_paths(candidates)
    paths = set(PUBLIC_FILES)
    paths.update(
        path for path in candidates
        if path not in ignored and not path.startswith(PRIVATE_SKILL_PREFIXES)
        and path not in PRIVATE_SKILL_FILES
    )
    for name in sorted(paths):
        relative = safe_relative_path(name)
        path = ROOT.joinpath(*relative.parts)
        if path.is_symlink() or not path.is_file():
            fail("Required public package file is missing or not a regular file: " + name)
    for name in paths:
        if name == "SOURCE-MANIFEST.json":
            fail("SOURCE-MANIFEST.json must not inventory itself")
    if "SOURCE-MANIFEST.json" in paths:
        fail("SOURCE-MANIFEST.json must not inventory itself")
    entrypoints = sorted(
        name for name in paths
        if re.fullmatch(r"skills/[^/]+/SKILL\.md", name)
    )
    if not entrypoints:
        fail("No public skill entrypoints were discovered")
    all_skill_dirs = {
        PurePosixPath(name).parts[1]
        for name in paths
        if name.startswith("skills/") and len(PurePosixPath(name).parts) > 1
    }
    if {PurePosixPath(name).parts[1] for name in entrypoints} != all_skill_dirs:
        fail("Every public skill directory must contain a top-level SKILL.md")
    return sorted(paths), entrypoints


def skill_ids_from_paths(entrypoints):
    import yaml

    skill_ids = []
    for name in entrypoints:
        data = ROOT.joinpath(*PurePosixPath(name).parts).read_bytes()
        match = FRONTMATTER.match(data.decode("utf-8"))
        if not match:
            fail("Skill frontmatter is missing: " + name)
        frontmatter = yaml.safe_load(match.group(1))
        if not isinstance(frontmatter, dict) or not frontmatter.get("name") or not frontmatter.get("description"):
            fail("Skill name/description is missing: " + name)
        skill_ids.append(frontmatter["name"])
    if len(set(skill_ids)) != len(skill_ids):
        fail("Skill frontmatter names are not unique")
    return skill_ids


def pointer_info(data, name):
    try:
        lines = data.decode("ascii").splitlines()
    except UnicodeDecodeError:
        fail("Malformed Git LFS pointer: " + name)
    if (
        len(lines) < 3
        or lines[0] != "version https://git-lfs.github.com/spec/v1"
        or not lines[1].startswith("oid sha256:")
        or not lines[2].startswith("size ")
    ):
        fail("Malformed Git LFS pointer: " + name)
    oid = lines[1][len("oid sha256:"):]
    size_text = lines[2][len("size "):]
    if not HEX64.fullmatch(oid) or not size_text.isdecimal():
        fail("Malformed Git LFS pointer fields: " + name)
    return oid, int(size_text)


def lfs_objects_root():
    result = run_git("rev-parse", "--git-path", "lfs/objects")
    value = result.stdout.decode("utf-8").strip()
    if not value:
        return None
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    return path.resolve()


def archive_digest(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_lfs_payload(name, oid, size, lfs_archive, lfs_archive_sha):
    objects = lfs_objects_root()
    if objects is not None:
        object_path = objects / oid[:2] / oid[2:4] / oid
        if object_path.is_file():
            data = object_path.read_bytes()
            if len(data) != size or sha256(data) != oid:
                fail("Local Git LFS object does not match its OID/size: " + name)
            return data, {"source": "git-lfs-object-store"}
    if lfs_archive is not None:
        try:
            with zipfile.ZipFile(lfs_archive) as archive:
                matches = [info for info in archive.infolist() if info.filename == name]
                if len(matches) != 1:
                    fail("LFS hydration archive must contain exactly one matching path: " + name)
                data = archive.read(matches[0])
        except (OSError, zipfile.BadZipFile) as error:
            fail("Cannot read LFS hydration archive: " + str(error))
        if len(data) != size or sha256(data) != oid:
            fail("Hydration archive payload does not match the public pointer OID/size: " + name)
        return data, {
            "source": "verified-archive-entry",
            "archiveName": lfs_archive.name,
            "archiveSha256": lfs_archive_sha,
        }
    fail("Git LFS payload is unavailable for " + name + "; use --lfs-archive PATH")


def canonical_content_hash(records):
    content = json.dumps(records, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256(content)


def normalize_created_at(value):
    if value is None:
        return datetime.now(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        moment = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        fail("--created-at must be an ISO-8601 UTC timestamp")
    if moment.tzinfo is None or moment.utcoffset().total_seconds() != 0:
        fail("--created-at must include a UTC timezone")
    return moment.astimezone(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")


def prepare_manifest(args):
    for required in ("plugin.json", ".codex-plugin/plugin.json"):
        path = ROOT / required
        if not path.is_file():
            fail("Plugin metadata is missing: " + required)
    package_meta = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    codex_meta = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    version = package_meta.get("version")
    if package_meta.get("name") != "oneirloom" or codex_meta.get("name") != "oneirloom":
        fail("Plugin package identity mismatch")
    if not isinstance(version, str) or not version or codex_meta.get("version") != version:
        fail("Plugin metadata versions do not match")
    paths, entrypoints = discover_package_paths()
    skill_ids = skill_ids_from_paths(entrypoints)
    commit = run_git("rev-parse", "HEAD").stdout.decode("ascii").strip()
    dirty_status = git_status_without_manifest()
    dirty = bool(dirty_status)
    lfs_archive = Path(args.lfs_archive).expanduser().resolve() if args.lfs_archive else None
    if lfs_archive is not None and not lfs_archive.is_file():
        fail("LFS hydration archive does not exist: " + str(lfs_archive))
    lfs_archive_sha = archive_digest(lfs_archive) if lfs_archive else None
    records = []
    source_file_records = []
    lfs_resolutions = []
    for name in paths:
        raw = ROOT.joinpath(*PurePosixPath(name).parts).read_bytes()
        raw_digest = sha256(raw)
        source_file_records.append({"path": name, "sha256": raw_digest, "bytes": len(raw)})
        if raw.startswith(POINTER_PREFIX):
            oid, size = pointer_info(raw, name)
            data, provenance = resolve_lfs_payload(name, oid, size, lfs_archive, lfs_archive_sha)
            record = {
                "path": name,
                "sha256": sha256(data),
                "bytes": len(data),
            }
            lfs_resolutions.append({
                "path": name,
                "oid": oid,
                "bytes": size,
                "sha256": sha256(data),
                "pointerSha256": raw_digest,
                "pointerBytes": len(raw),
                **provenance,
            })
        else:
            record = {"path": name, "sha256": raw_digest, "bytes": len(raw)}
        records.append(record)
    skill_file_records = [record for record in source_file_records if record["path"].startswith("skills/")]
    git_status = git_status_without_manifest()
    if bool(git_status) != dirty:
        fail("Git dirty state changed while preparing the source manifest")
    manifest = {
        "schemaVersion": 2,
        "generatedAt": normalize_created_at(args.created_at),
        "package": {"name": "oneirloom", "version": version},
        "collectionVersion": version,
        "skillIds": skill_ids,
        "zipTimestamp": list(DEFAULT_ZIP_TIMESTAMP),
        "sourceSnapshot": {
            "baseCommit": commit,
            "workingTreeDirty": dirty,
            "dirtyStatusScope": "repository excluding generated SOURCE-MANIFEST.json",
            "workingTreeContentSha256": canonical_content_hash(source_file_records),
            "skillFiles": skill_file_records,
            "lfsPayloadResolutions": lfs_resolutions,
        },
        "packagedFilesExceptThisManifest": records,
    }
    payload = json.dumps(manifest, ensure_ascii=False, indent=2).encode("utf-8") + b"\n"
    MANIFEST_PATH.write_bytes(payload)
    print(json.dumps({
        "prepared": str(MANIFEST_PATH),
        "version": version,
        "skillEntrypoints": len(skill_ids),
        "inventoryFiles": len(records),
        "workingTreeDirty": dirty,
        "baseCommit": commit,
        "lfsPayloadsResolved": len(lfs_resolutions),
    }, ensure_ascii=False, sort_keys=True))


def manifest_zip_timestamp(manifest):
    value = manifest.get("zipTimestamp")
    if value is None:
        return DEFAULT_ZIP_TIMESTAMP
    if (
        not isinstance(value, list)
        or len(value) != 6
        or any(not isinstance(part, int) or isinstance(part, bool) for part in value)
    ):
        fail("SOURCE-MANIFEST.json zipTimestamp must be six integers")
    timestamp = tuple(value)
    try:
        if timestamp[5] % 2:
            fail("SOURCE-MANIFEST.json zipTimestamp seconds must be even")
        import datetime as datetime_module
        datetime_module.datetime(*timestamp)
    except ValueError:
        fail("SOURCE-MANIFEST.json zipTimestamp is invalid")
    if timestamp[0] < 1980 or timestamp[0] > 2107:
        fail("SOURCE-MANIFEST.json zipTimestamp is outside ZIP limits")
    return timestamp


def build_archive(args):
    if not MANIFEST_PATH.is_file():
        fail("SOURCE-MANIFEST.json is missing; run with --prepare after source files are final")
    manifest_bytes = MANIFEST_PATH.read_bytes()
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    package = manifest.get("package")
    if not isinstance(package, dict) or package.get("name") != "oneirloom":
        fail("SOURCE-MANIFEST.json package identity mismatch")
    version = package.get("version")
    if not isinstance(version, str) or not version:
        fail("SOURCE-MANIFEST.json package version is missing")
    if manifest.get("schemaVersion") == 2 and manifest.get("collectionVersion") != version:
        fail("SOURCE-MANIFEST.json collectionVersion does not match package version")
    records = manifest.get("packagedFilesExceptThisManifest")
    if not isinstance(records, list) or not records:
        fail("SOURCE-MANIFEST.json package inventory is missing")
    paths = []
    for record in records:
        if not isinstance(record, dict) or not isinstance(record.get("path"), str):
            fail("SOURCE-MANIFEST.json contains a malformed inventory record")
        paths.append(record["path"])
    if len(set(paths)) != len(paths) or "SOURCE-MANIFEST.json" in paths:
        fail("SOURCE-MANIFEST.json inventory contains duplicates or itself")
    if paths != sorted(paths):
        fail("SOURCE-MANIFEST.json inventory paths are not sorted")
    if not args.repack_extracted:
        discovered_paths, entrypoints = discover_package_paths()
        if paths != discovered_paths:
            fail("Public source file set changed after SOURCE-MANIFEST.json preparation")
        if manifest.get("schemaVersion") == 2 and manifest.get("skillIds") != skill_ids_from_paths(entrypoints):
            fail("Public skill IDs changed after SOURCE-MANIFEST.json preparation")
    source_snapshot = manifest.get("sourceSnapshot", {})
    lfs_records = source_snapshot.get("lfsPayloadResolutions", [])
    if not isinstance(lfs_records, list):
        fail("SOURCE-MANIFEST.json LFS resolutions must be a list")
    lfs_by_path = {record.get("path"): record for record in lfs_records if isinstance(record, dict)}
    if len(lfs_by_path) != len(lfs_records):
        fail("SOURCE-MANIFEST.json contains duplicate or malformed LFS resolutions")
    lfs_archive = Path(args.lfs_archive).expanduser().resolve() if args.lfs_archive else None
    if lfs_archive is not None and not lfs_archive.is_file():
        fail("LFS hydration archive does not exist: " + str(lfs_archive))
    lfs_archive_sha = archive_digest(lfs_archive) if lfs_archive else None
    entries = {}
    raw_content_records = []
    skill_source_records = []
    for record in records:
        name = record.get("path")
        relative = safe_relative_path(name)
        if name in entries:
            fail("Duplicate inventory path: " + name)
        path = ROOT.joinpath(*relative.parts)
        if path.is_symlink() or not path.is_file():
            fail("Source file is missing or not a regular file: " + name)
        raw = path.read_bytes()
        resolution = lfs_by_path.get(name)
        raw_record = {"path": name, "sha256": sha256(raw), "bytes": len(raw)}
        raw_content_records.append(raw_record)
        if name.startswith("skills/"):
            skill_source_records.append(raw_record)
        if raw.startswith(POINTER_PREFIX):
            if not isinstance(resolution, dict):
                fail("Manifest has no LFS payload resolution for " + name)
            oid, size = pointer_info(raw, name)
            if resolution.get("oid") != oid or resolution.get("bytes") != size:
                fail("LFS resolution does not match source pointer: " + name)
            data, _ = resolve_lfs_payload(name, oid, size, lfs_archive, lfs_archive_sha)
        else:
            if resolution is not None and not args.repack_extracted:
                fail("Manifest records an LFS resolution for a non-pointer file: " + name)
            data = raw
        if len(data) != record.get("bytes") or sha256(data) != record.get("sha256"):
            fail("Source payload does not match manifest inventory: " + name)
        if data.startswith(POINTER_PREFIX):
            fail("Git LFS pointer is not a package payload: " + name)
        entries[name] = data
    if manifest.get("schemaVersion") == 2 and not args.repack_extracted:
        snapshot = source_snapshot
        if snapshot.get("baseCommit") != run_git("rev-parse", "HEAD").stdout.decode("ascii").strip():
            fail("Source baseCommit changed after SOURCE-MANIFEST.json preparation")
        if snapshot.get("dirtyStatusScope") != "repository excluding generated SOURCE-MANIFEST.json":
            fail("SOURCE-MANIFEST.json dirty status scope is missing or unsupported")
        if snapshot.get("workingTreeDirty") is not bool(git_status_without_manifest()):
            fail("Source dirty status changed after SOURCE-MANIFEST.json preparation")
        if snapshot.get("workingTreeContentSha256") != canonical_content_hash(raw_content_records):
            fail("Working-tree content differs from SOURCE-MANIFEST.json snapshot")
        if snapshot.get("skillFiles") != skill_source_records:
            fail("Working-tree skill file hashes differ from SOURCE-MANIFEST.json snapshot")
    if not args.repack_extracted and set(lfs_by_path) != {
        name for name in paths
        if isinstance(name, str)
        and (ROOT.joinpath(*safe_relative_path(name).parts).read_bytes().startswith(POINTER_PREFIX))
    }:
        fail("Manifest LFS resolutions do not exactly match source pointers")
    if manifest_bytes.startswith(POINTER_PREFIX):
        fail("SOURCE-MANIFEST.json unexpectedly contains an LFS pointer")
    entries["SOURCE-MANIFEST.json"] = manifest_bytes
    timestamp = manifest_zip_timestamp(manifest)
    output_dir = Path(args.output).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / f"oneirloom-{version}.zip"
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(name, timestamp)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    zip_bytes = target.read_bytes()
    zip_sha = sha256(zip_bytes)
    checksums = {
        name: sha256(data) for name, data in entries.items()
    }
    checksums[target.name] = zip_sha
    with (output_dir / "SHA256SUMS.txt").open("w", encoding="utf-8", newline="\n") as stream:
        stream.write("".join(f"{digest}  {name}\n" for name, digest in sorted(checksums.items())))
    print(json.dumps({
        "mode": "repack-extracted" if args.repack_extracted else "source",
        "zip": str(target),
        "sha256": zip_sha,
        "sizeBytes": len(zip_bytes),
        "entries": len(entries),
        "lfsPointers": 0,
        "version": version,
    }, sort_keys=True))


def main():
    parser = argparse.ArgumentParser(description="Prepare a curated Oneirloom plugin manifest or build its deterministic ZIP.")
    parser.add_argument("--prepare", action="store_true", help="regenerate SOURCE-MANIFEST.json only; does not build a ZIP")
    parser.add_argument("--output", default="dist-plugin", help="output directory for the ZIP and SHA256SUMS.txt")
    parser.add_argument("--lfs-archive", help="optional verified ZIP used only to hydrate matching Git LFS paths by OID and size")
    parser.add_argument("--created-at", help="ISO-8601 UTC timestamp for manifest generation; defaults to current UTC time")
    parser.add_argument("--repack-extracted", action="store_true", help="rebuild from an extracted verified package without Git or LFS")
    args = parser.parse_args()
    if args.prepare:
        if args.repack_extracted:
            parser.error("--prepare and --repack-extracted cannot be used together")
        prepare_manifest(args)
    else:
        build_archive(args)


if __name__ == "__main__":
    main()
