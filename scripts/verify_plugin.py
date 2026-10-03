from pathlib import Path, PurePosixPath
from io import BytesIO
import argparse
import datetime
import hashlib
import json
import posixpath
import re
import stat
import unicodedata
import urllib.parse
import zipfile
import xml.etree.ElementTree as ET

from PIL import Image
import yaml

POINTER_PREFIX = b"version https://git-lfs.github.com/spec/v1"
DEFAULT_ZIP_TIMESTAMP = (2026, 10, 2, 0, 0, 0)
PUBLIC_FILES = {
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
}
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
RASTER_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tif", ".tiff", ".avif"}
HEX64 = re.compile(r"\A[0-9a-f]{64}\Z")
HEX40 = re.compile(r"\A[0-9a-f]{40}\Z")
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\s*\r?\n|\Z)", re.S)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def safe_relative_path(name):
    require(isinstance(name, str) and bool(name), "Inventory path must be a non-empty string")
    parts = name.split("/")
    require(name == name.strip(), "Archive path has outer whitespace: " + name)
    require("\\" not in name and not name.startswith("/"), "Archive path is not a relative slash path: " + name)
    require(not (len(parts[0]) >= 2 and parts[0][1] == ":"), "Archive path contains a drive prefix: " + name)
    require(all(part not in ("", ".", "..") for part in parts), "Archive path has an empty/current/parent segment: " + name)
    require(len(parts) <= 20, "Archive path exceeds 20 segments: " + name)
    return PurePosixPath(name)


def zip_timestamp(manifest, schema_version):
    value = manifest.get("zipTimestamp")
    if value is None and schema_version == 1:
        return DEFAULT_ZIP_TIMESTAMP
    require(
        isinstance(value, list)
        and len(value) == 6
        and all(isinstance(part, int) and not isinstance(part, bool) for part in value),
        "Manifest zipTimestamp must contain six integers",
    )
    timestamp = tuple(value)
    require(timestamp[0] >= 1980 and timestamp[0] <= 2107, "Manifest zipTimestamp is outside ZIP limits")
    require(timestamp[5] % 2 == 0, "Manifest zipTimestamp seconds must be even")
    try:
        datetime.datetime(*timestamp)
    except ValueError:
        raise AssertionError("Manifest zipTimestamp is invalid")
    return timestamp


def parse_frontmatter(data, name):
    text = data.decode("utf-8")
    match = FRONTMATTER.match(text)
    require(match is not None, "Skill frontmatter is missing: " + name)
    frontmatter = yaml.safe_load(match.group(1))
    require(
        isinstance(frontmatter, dict)
        and isinstance(frontmatter.get("name"), str)
        and bool(frontmatter.get("name"))
        and isinstance(frontmatter.get("description"), str)
        and bool(frontmatter.get("description")),
        "Skill name/description is missing: " + name,
    )
    return frontmatter


def verify_v2_public_inventory(names):
    require(PUBLIC_FILES.issubset(set(names)), "Schema 2 archive is missing required public package files")
    for name in names:
        if name == "SOURCE-MANIFEST.json":
            continue
        if name.startswith("skills/"):
            safe_relative_path(name)
            parts = PurePosixPath(name).parts
            require(not any(part.casefold() in CACHE_DIRS for part in parts), "Cache file is not public package content: " + name)
            require(not any(name.startswith(prefix) for prefix in PRIVATE_SKILL_PREFIXES), "Known private skill asset is packaged: " + name)
            require(name not in PRIVATE_SKILL_FILES, "Known private skill asset is packaged: " + name)
            continue
        require(name in PUBLIC_FILES, "Path is outside the curated public package inventory: " + name)


def verify_v2_snapshot(manifest, inventory, skill_paths):
    snapshot = manifest.get("sourceSnapshot")
    require(isinstance(snapshot, dict), "Schema 2 sourceSnapshot is missing")
    commit = snapshot.get("baseCommit")
    require(isinstance(commit, str) and HEX40.fullmatch(commit), "Source baseCommit must be a full Git SHA-1")
    require(isinstance(snapshot.get("workingTreeDirty"), bool), "Source workingTreeDirty must be a boolean")
    content_hash = snapshot.get("workingTreeContentSha256")
    require(isinstance(content_hash, str) and HEX64.fullmatch(content_hash), "Source workingTreeContentSha256 is invalid")
    skill_records = snapshot.get("skillFiles")
    require(isinstance(skill_records, list), "Source skillFiles must be a list")
    require(
        [record.get("path") for record in skill_records if isinstance(record, dict)]
        == sorted(record.get("path") for record in skill_records if isinstance(record, dict)),
        "Source skillFiles paths are not sorted",
    )
    require(snapshot.get("dirtyStatusScope") == "repository excluding generated SOURCE-MANIFEST.json", "Source dirty status scope is missing or unsupported")
    skill_by_path = {}
    skill_paths_from_inventory = sorted(name for name in inventory if name.startswith("skills/"))
    skill_entries_from_inventory = sorted(skill_paths)
    require(len(skill_records) == len(skill_paths_from_inventory), "Source skillFiles count differs from package inventory")
    for record in skill_records:
        require(isinstance(record, dict), "Malformed source skill file record")
        name = record.get("path")
        safe_relative_path(name)
        require(name not in skill_by_path, "Duplicate source skill file path: " + str(name))
        digest = record.get("sha256")
        size = record.get("bytes")
        require(isinstance(digest, str) and HEX64.fullmatch(digest), "Invalid source skill file SHA-256: " + str(name))
        require(isinstance(size, int) and not isinstance(size, bool) and size >= 0, "Invalid source skill file size: " + str(name))
        skill_by_path[name] = record
    require(set(skill_by_path) == set(skill_paths_from_inventory), "Source skill file paths differ from package inventory")
    lfs_records = snapshot.get("lfsPayloadResolutions")
    require(isinstance(lfs_records, list), "Source lfsPayloadResolutions must be a list")
    lfs_by_path = {}
    for record in lfs_records:
        require(isinstance(record, dict), "Malformed source LFS resolution")
        name = record.get("path")
        safe_relative_path(name)
        require(name not in lfs_by_path, "Duplicate source LFS resolution: " + str(name))
        oid = record.get("oid")
        payload_digest = record.get("sha256")
        pointer_digest = record.get("pointerSha256")
        payload_size = record.get("bytes")
        pointer_size = record.get("pointerBytes")
        require(isinstance(oid, str) and HEX64.fullmatch(oid), "Invalid LFS OID: " + str(name))
        require(isinstance(payload_digest, str) and HEX64.fullmatch(payload_digest), "Invalid LFS payload SHA-256: " + str(name))
        require(isinstance(pointer_digest, str) and HEX64.fullmatch(pointer_digest), "Invalid LFS pointer SHA-256: " + str(name))
        require(isinstance(payload_size, int) and not isinstance(payload_size, bool) and payload_size >= 0, "Invalid LFS payload size: " + str(name))
        require(isinstance(pointer_size, int) and not isinstance(pointer_size, bool) and pointer_size > 0, "Invalid LFS pointer size: " + str(name))
        source = record.get("source")
        require(source in ("git-lfs-object-store", "verified-archive-entry"), "Unknown LFS hydration provenance: " + str(name))
        if source == "verified-archive-entry":
            archive_name = record.get("archiveName")
            require(isinstance(archive_name, str) and archive_name and Path(archive_name).name == archive_name, "Invalid LFS hydration archive name: " + str(name))
            archive_hash = record.get("archiveSha256")
            require(isinstance(archive_hash, str) and HEX64.fullmatch(archive_hash), "Invalid LFS hydration archive hash: " + str(name))
        lfs_by_path[name] = record
    require(set(lfs_by_path).issubset(set(inventory)), "LFS resolution path is not a packaged payload")
    raw_content_records = []
    for name in sorted(inventory):
        package_record = inventory[name]
        resolution = lfs_by_path.get(name)
        if resolution:
            require(
                package_record["sha256"] == resolution["oid"] == resolution["sha256"]
                and package_record["bytes"] == resolution["bytes"],
                "LFS payload does not match package inventory: " + name,
            )
            raw_digest = resolution["pointerSha256"]
            raw_size = resolution["pointerBytes"]
        else:
            raw_digest = package_record["sha256"]
            raw_size = package_record["bytes"]
        raw_content_records.append({"path": name, "sha256": raw_digest, "bytes": raw_size})
        if name in skill_by_path:
            skill_record = skill_by_path[name]
            require(
                skill_record["sha256"] == raw_digest and skill_record["bytes"] == raw_size,
                "Source skill file hash differs from working-tree snapshot: " + name,
            )
    canonical = json.dumps(raw_content_records, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    require(hashlib.sha256(canonical).hexdigest() == content_hash, "Working-tree content hash does not reconcile")
    require(set(skill_paths_from_inventory) == set(skill_by_path), "Source skill inventory is incomplete")
    require(skill_entries_from_inventory == sorted(skill_paths), "Internal skill-entry inventory mismatch")
    return len(lfs_by_path)


def verify(args):
    archive_path = Path(args.archive).expanduser().resolve()
    checksums_path = Path(args.checksums).expanduser().resolve() if args.checksums else archive_path.parent / "SHA256SUMS.txt"
    require(archive_path.is_file(), "ZIP archive does not exist")
    require(checksums_path.is_file(), "SHA256SUMS.txt does not exist")
    zip_size = archive_path.stat().st_size
    directory_size_ok = zip_size <= 100_000_000
    if args.target == "plugin-directory":
        require(directory_size_ok, "ZIP exceeds the plugin directory's 100 MB compressed limit")
    else:
        require(zip_size < 2 * 1024**3, "ZIP exceeds GitHub Releases' per-asset 2 GiB limit")
    with zipfile.ZipFile(archive_path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        require(names == sorted(names), "Archive entries are not sorted")
        require(len(names) == len(set(names)), "Archive contains duplicate paths")
        require(len(names) <= 5000, "Archive exceeds the official 5,000-entry limit")
        require("SOURCE-MANIFEST.json" in names, "SOURCE-MANIFEST.json is missing")
        normalized = set()
        max_depth = 0
        max_path_chars = 0
        max_member_bytes = 0
        uncompressed_bytes = 0
        fileset = set(names)
        for info in infos:
            name = info.filename
            parts = safe_relative_path(name).parts
            key = unicodedata.normalize("NFC", name).casefold()
            require(key not in normalized, "Archive path normalization collision: " + name)
            normalized.add(key)
            mode = info.external_attr >> 16
            require(stat.S_IFMT(mode) in (0, stat.S_IFREG), "Archive entry is not a regular file: " + name)
            require(not (info.flag_bits & 0x1), "Encrypted archive entry: " + name)
            require(info.compress_type == zipfile.ZIP_DEFLATED, "Unsupported archive compression: " + name)
            max_depth = max(max_depth, len(parts))
            max_path_chars = max(max_path_chars, len(name))
            max_member_bytes = max(max_member_bytes, info.file_size)
            uncompressed_bytes += info.file_size
        for name in names:
            parts = name.split("/")
            for index in range(1, len(parts)):
                require("/".join(parts[:index]) not in fileset, "Archive file/directory path conflict: " + name)
        require(max_member_bytes <= 104_857_600, "Archive entry exceeds the official 100 MiB limit")
        require(uncompressed_bytes <= 536_870_912, "Archive exceeds the official 512 MiB extracted limit")
        manifest_bytes = archive.read("SOURCE-MANIFEST.json")
        require(not manifest_bytes.startswith(POINTER_PREFIX), "SOURCE-MANIFEST.json is an LFS pointer")
        manifest = json.loads(manifest_bytes.decode("utf-8"))
        package = manifest.get("package")
        require(isinstance(package, dict) and package.get("name") == "oneirloom", "Package identity mismatch")
        version = package.get("version")
        require(isinstance(version, str) and bool(version), "Package version is missing")
        schema_version = manifest.get("schemaVersion", 1)
        if schema_version is None:
            schema_version = 1
        require(schema_version in (1, 2), "Unsupported source manifest schema version")
        timestamp = zip_timestamp(manifest, schema_version)
        for info in infos:
            require(info.date_time == timestamp, "Archive entry timestamp differs from manifest: " + info.filename)
        records = manifest.get("packagedFilesExceptThisManifest")
        require(isinstance(records, list) and bool(records), "Manifest package inventory is missing")
        inventory = {}
        inventory_names = []
        for record in records:
            require(isinstance(record, dict), "Malformed manifest inventory record")
            name = record.get("path")
            safe_relative_path(name)
            require(name != "SOURCE-MANIFEST.json", "Manifest inventory must not hash itself")
            require(name not in inventory, "Manifest inventory contains a duplicate path: " + name)
            digest = record.get("sha256")
            size = record.get("bytes")
            require(isinstance(digest, str) and HEX64.fullmatch(digest), "Manifest SHA-256 is invalid: " + name)
            require(isinstance(size, int) and not isinstance(size, bool) and size >= 0, "Manifest byte count is invalid: " + name)
            inventory[name] = record
            inventory_names.append(name)
        require(inventory_names == sorted(inventory_names), "Manifest inventory paths are not sorted")
        require(set(names) == set(inventory) | {"SOURCE-MANIFEST.json"}, "Archive names do not exactly match the curated inventory")
        payloads = {}
        pointer_paths = []
        for name in names:
            data = archive.read(name)
            require(not data.startswith(POINTER_PREFIX), "Git LFS pointer prefix found in package entry: " + name)
            payloads[name] = data
            if name != "SOURCE-MANIFEST.json":
                record = inventory[name]
                require(len(data) == record["bytes"], "Manifest byte count mismatch: " + name)
                require(hashlib.sha256(data).hexdigest() == record["sha256"], "Manifest SHA-256 mismatch: " + name)
            if name.lower().endswith(tuple(RASTER_SUFFIXES)):
                with Image.open(BytesIO(data)) as image:
                    image.verify()
            if name.lower().endswith(".svg"):
                element = ET.fromstring(data)
                require(element.tag.rsplit("}", 1)[-1] == "svg", "SVG root element is invalid: " + name)
        require(not pointer_paths, "LFS pointer entries found")
        if schema_version == 2:
            require(manifest.get("collectionVersion") == version, "collectionVersion does not match package version")
            declared_skill_ids = manifest.get("skillIds")
            require(isinstance(declared_skill_ids, list) and declared_skill_ids, "Schema 2 skillIds are missing")
            verify_v2_public_inventory(names)
        package_manifest = json.loads(payloads["plugin.json"].decode("utf-8"))
        codex_manifest = json.loads(payloads[".codex-plugin/plugin.json"].decode("utf-8"))
        require(package_manifest.get("name") == codex_manifest.get("name") == "oneirloom", "Plugin manifest name mismatch")
        require(package_manifest.get("version") == codex_manifest.get("version") == version, "Plugin manifest version mismatch")
        author = package_manifest.get("author", {})
        codex_author = codex_manifest.get("author", {})
        require(isinstance(author, dict) and isinstance(codex_author, dict), "Plugin author fields must be objects")
        require(bool(author.get("name")) and author.get("name") == codex_author.get("name"), "Plugin author name mismatch")
        require(package_manifest.get("extensions", {}).get("com.openai") is not None, "OpenAI plugin interface is missing")
        extension = package_manifest["extensions"]["com.openai"]
        require(set(extension) == {"interface", "publication"}, "OpenAI extension fields mismatch")
        interface = codex_manifest.get("interface")
        require(isinstance(interface, dict) and interface == extension["interface"], "Portable and Codex interfaces differ")
        require(interface.get("developerName") == author["name"], "Interface developer name does not match author")
        require(len(interface.get("displayName", "")) <= 30, "Display name exceeds the final listing limit")
        require(len(interface.get("shortDescription", "")) <= 30, "Short description exceeds the final listing limit")
        for field in ("logo", "composerIcon"):
            icon = interface.get(field, "")
            require(isinstance(icon, str) and icon.startswith("./"), "Icon path must be package-relative: " + field)
            icon_path = icon[2:]
            safe_relative_path(icon_path)
            require(icon_path in names, "Icon file is missing: " + field)
        icon_root = ET.fromstring(payloads[interface["logo"][2:]])
        require(icon_root.tag.rsplit("}", 1)[-1] == "svg", "Plugin icon is not an SVG")
        skill_paths = sorted(name for name in names if re.fullmatch(r"skills/[^/]+/SKILL\.md", name))
        require(bool(skill_paths), "No skill entrypoints were packaged")
        actual_skill_ids = [parse_frontmatter(payloads[name], name)["name"] for name in skill_paths]
        require(len(set(actual_skill_ids)) == len(actual_skill_ids), "Skill frontmatter names are not unique")
        if schema_version == 2:
            require(
                all(isinstance(skill_id, str) and bool(skill_id) for skill_id in declared_skill_ids),
                "Schema 2 skillIds must be non-empty strings",
            )
            require(len(set(declared_skill_ids)) == len(declared_skill_ids), "Manifest skillIds are not unique")
            require(declared_skill_ids == actual_skill_ids, "Manifest skillIds differ from archived skill frontmatter")
            lfs_matches = verify_v2_snapshot(manifest, inventory, skill_paths)
        else:
            lfs_matches = 0
        if schema_version == 2:
            markdown_paths = [
                name for name in names
                if name.startswith(("skills/", "docs/")) and name.endswith(".md")
            ]
        else:
            markdown_paths = [name for name in names if name.startswith("skills/") and name.endswith(".md")]
            if "docs/model-evidence.md" in names:
                markdown_paths.append("docs/model-evidence.md")
        for name in markdown_paths:
            text = payloads[name].decode("utf-8")
            for raw_link in re.findall(r"\]\(([^)]+)\)", text):
                link = raw_link.strip()
                if not link or "<" in link or "://" in link or link.startswith(("mailto:", "data:", "//")):
                    continue
                destination = link.split("#", 1)[0].split("?", 1)[0]
                if not destination:
                    continue
                destination = urllib.parse.unquote(destination)
                target = posixpath.normpath(posixpath.join(posixpath.dirname(name), destination))
                require(target != ".." and not target.startswith("../") and not target.startswith("/"), "Local Markdown link escapes package: " + name + " -> " + link)
                if name.startswith("skills/"):
                    require(target.startswith("skills/"), "Skill link escapes skills tree: " + name + " -> " + link)
                exists = target in names or any(entry.startswith(target.rstrip("/") + "/") for entry in names)
                require(exists, "Broken local Markdown link: " + name + " -> " + link)
        zip_sha = hashlib.sha256(archive_path.read_bytes()).hexdigest()
        expected_sums = {name: hashlib.sha256(payloads[name]).hexdigest() for name in names}
        expected_sums[archive_path.name] = zip_sha
        sums = {}
        for line in checksums_path.read_text(encoding="utf-8").splitlines():
            if not line:
                continue
            require("  " in line, "Malformed SHA256SUMS line")
            digest, name = line.split("  ", 1)
            require(name not in sums, "Duplicate checksum path: " + name)
            require(bool(HEX64.fullmatch(digest)), "Invalid checksum digest: " + name)
            sums[name] = digest
        require(sums == expected_sums, "External SHA256SUMS.txt does not match the package and ZIP")
    image_count = sum(1 for name in names if name.lower().endswith(tuple(RASTER_SUFFIXES)))
    svg_count = sum(1 for name in names if name.lower().endswith(".svg"))
    report = {
        "passed": True,
        "target": args.target,
        "directorySubmissionEligible": False if not directory_size_ok else (True if args.target == "plugin-directory" else None),
        "directoryCompressedSizeLimitMet": directory_size_ok,
        "githubReleaseAssetSizeLimitMet": zip_size < 2 * 1024**3,
        "githubReleaseAssetSizeLimitSource": "https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases",
        "manifestSchemaVersion": schema_version,
        "zip": str(archive_path),
        "zipSha256": zip_sha,
        "zipBytes": archive_path.stat().st_size,
        "packageVersion": version,
        "entries": len(names),
        "inventoryRecords": len(inventory),
        "uncompressedBytes": uncompressed_bytes,
        "maximumEntryBytes": max_member_bytes,
        "maximumPathCharacters": max_path_chars,
        "maximumPathSegments": max_depth,
        "zeroLfsPointers": len(pointer_paths) == 0,
        "lfsPayloadsMatched": lfs_matches,
        "skillEntrypoints": len(skill_paths),
        "skillIds": actual_skill_ids,
        "workingTreeDirty": manifest.get("sourceSnapshot", {}).get("workingTreeDirty") if schema_version == 2 else None,
        "deliveryOnlyNoticeDeclared": "skills/oneirloom-model-qwen-image-2-1/references/official/Notice" in names,
        "marketplaceIncludedAsCuratedFile": ".agents/plugins/marketplace.json" in names,
        "legacyMarketplaceExcluded": schema_version == 1 and ".agents/plugins/marketplace.json" not in names,
        "imageDecodeCount": image_count,
        "svgXmlCount": svg_count,
        "checks": [
            "exact manifest/archive inventory and SHA-256 sizes",
            "package version and plugin metadata coherence",
            "public package boundary and known private branding exclusions" if schema_version == 2 else "legacy package inventory and version coherence",
            "skill frontmatter, unique IDs, and schema skill ID coherence" if schema_version == 2 else "skill frontmatter and unique IDs",
            "local Markdown links",
            "raster image decode and SVG XML",
            "source working-tree snapshot and LFS OID/size provenance" if schema_version == 2 else "legacy schema accepted without Git/source checkout",
            "fixed timestamp, deflate compression, path safety, and regular-file modes",
            "target ZIP size, entry-count, and extracted-size limits",
            "external SHA-256 checksums",
        ],
        "officialPathLengthLimit": "The cited official reference names a supported path-length limit but does not publish a numeric value; measured maximum is reported above.",
    }
    return report


def main():
    parser = argparse.ArgumentParser(description="Verify a Oneirloom plugin ZIP using only the archive and external checksums.")
    parser.add_argument("archive")
    parser.add_argument("--checksums")
    parser.add_argument("--target", choices=("github-release", "plugin-directory"), default="plugin-directory")
    args = parser.parse_args()
    try:
        report = verify(args)
    except (AssertionError, OSError, ValueError, KeyError, zipfile.BadZipFile, UnicodeDecodeError, json.JSONDecodeError, yaml.YAMLError, ET.ParseError) as error:
        parser.error("verification failed: " + str(error))
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
