from pathlib import Path, PurePosixPath
from io import BytesIO
import argparse
import hashlib
import json
import posixpath
import re
import stat
import subprocess
import unicodedata
import urllib.parse
import zipfile
import xml.etree.ElementTree as ET

from PIL import Image
import yaml

ROOT = Path(__file__).resolve().parents[1]
PINNED = "8d195d4fc9404d5da71733c861fd947aa109d4f1"
POINTER_PREFIX = b"version https://git-lfs.github.com/spec/v1\n"
RASTER_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tif", ".tiff", ".avif"}
parser = argparse.ArgumentParser()
parser.add_argument("archive")
parser.add_argument("--checksums")
args = parser.parse_args()
archive_path = Path(args.archive).resolve()
checksums_path = Path(args.checksums).resolve() if args.checksums else archive_path.parent / "SHA256SUMS.txt"

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def git_bytes(*arguments):
    return subprocess.check_output(["git", "-c", f"safe.directory={ROOT.as_posix()}", *arguments], cwd=ROOT)

def pointer_info(data):
    lines = data.decode("ascii").splitlines()
    require(len(lines) >= 3 and lines[0] == "version https://git-lfs.github.com/spec/v1", "Malformed pinned LFS pointer")
    require(lines[1].startswith("oid sha256:") and lines[2].startswith("size "), "Malformed pinned LFS pointer fields")
    return lines[1].removeprefix("oid sha256:"), int(lines[2].removeprefix("size "))

with zipfile.ZipFile(archive_path) as archive:
    infos = archive.infolist()
    names = [info.filename for info in infos]
    require(names == sorted(names), "Archive entries are not sorted")
    require(len(names) == len(set(names)), "Archive contains duplicate paths")
    require(len(names) == 117, f"Expected 117 entries, got {len(names)}")
    require("plugin.json" in names and ".codex-plugin/plugin.json" in names, "Required plugin manifests are missing")
    require("SOURCE-MANIFEST.json" in names, "SOURCE-MANIFEST.json is missing")
    normalized = set()
    max_depth = 0
    max_path_chars = 0
    max_member_bytes = 0
    uncompressed_bytes = 0
    fileset = set(names)
    for info in infos:
        name = info.filename
        parts = name.split("/")
        require(bool(name) and name == name.strip(), "Archive path is empty or has outer whitespace")
        require("\\" not in name and not name.startswith("/"), "Archive path is not a relative slash path")
        require(not (len(parts[0]) >= 2 and parts[0][1] == ":"), "Archive path contains a drive prefix")
        require(all(part not in ("", ".", "..") for part in parts), "Archive path has an empty/current/parent segment")
        require(len(parts) <= 20, "Archive path exceeds 20 segments: " + name)
        key = unicodedata.normalize("NFC", name).casefold()
        require(key not in normalized, "Archive path normalization collision: " + name)
        normalized.add(key)
        mode = info.external_attr >> 16
        require(stat.S_IFMT(mode) in (0, stat.S_IFREG), "Archive entry is not a regular file: " + name)
        require(not (info.flag_bits & 0x1), "Encrypted archive entry: " + name)
        require(info.compress_type == zipfile.ZIP_DEFLATED, "Unsupported archive compression: " + name)
        require(info.date_time == (2026, 10, 2, 0, 0, 0), "Archive entry timestamp is not fixed: " + name)
        max_depth = max(max_depth, len(parts))
        max_path_chars = max(max_path_chars, len(name))
        max_member_bytes = max(max_member_bytes, info.file_size)
        uncompressed_bytes += info.file_size
    for name in names:
        parts = name.split("/")
        for index in range(1, len(parts)):
            require("/".join(parts[:index]) not in fileset, "Archive file/directory path conflict: " + name)
    require(archive_path.stat().st_size <= 100_000_000, "ZIP exceeds the official 100 MB compressed limit")
    require(max_member_bytes <= 104_857_600, "Archive entry exceeds the official 100 MiB limit")
    require(len(names) <= 5000, "Archive exceeds the official 5,000-entry limit")
    require(uncompressed_bytes <= 536_870_912, "Archive exceeds the official 512 MiB extracted limit")
    manifest_bytes = archive.read("SOURCE-MANIFEST.json")
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    require(manifest.get("package") == {"name": "oneirloom", "version": "0.1.1"}, "Package identity/version mismatch")
    snapshot = manifest.get("sourceSnapshot", {})
    require(snapshot.get("commit") == PINNED, "Source snapshot commit mismatch")
    records = manifest.get("packagedFilesExceptThisManifest")
    require(isinstance(records, list) and len(records) == 116, "Manifest must inventory exactly 116 other entries")
    inventory = {record.get("path"): record for record in records}
    require(None not in inventory and len(inventory) == len(records), "Manifest inventory has duplicate or invalid paths")
    require(set(names) == set(inventory) | {"SOURCE-MANIFEST.json"}, "Archive names do not exactly match the curated inventory")
    pointer_paths = []
    for name in names:
        data = archive.read(name)
        require(not data.startswith(POINTER_PREFIX), "Git LFS pointer prefix found in package entry: " + name)
        if name != "SOURCE-MANIFEST.json":
            record = inventory[name]
            require(len(data) == record.get("bytes"), "Manifest byte count mismatch: " + name)
            require(hashlib.sha256(data).hexdigest() == record.get("sha256"), "Manifest SHA-256 mismatch: " + name)
            source = ROOT.joinpath(*PurePosixPath(name).parts).read_bytes()
            require(data == source, "Packaged source differs: " + name)
        if name.lower().endswith(tuple(RASTER_SUFFIXES)):
            with Image.open(BytesIO(data)) as image:
                image.verify()
        if name.lower().endswith(".svg"):
            element = ET.fromstring(data)
            require(element.tag.rsplit("}", 1)[-1] == "svg", "SVG root element is invalid: " + name)
        if data.startswith(POINTER_PREFIX):
            pointer_paths.append(name)
    require(not pointer_paths, "LFS pointer entries found")
    require(manifest_bytes == (ROOT / "SOURCE-MANIFEST.json").read_bytes(), "Packaged source manifest differs from checkout")

    package_manifest = json.loads(archive.read("plugin.json").decode("utf-8"))
    codex_manifest = json.loads(archive.read(".codex-plugin/plugin.json").decode("utf-8"))
    require(package_manifest.get("name") == codex_manifest.get("name") == "oneirloom", "Plugin manifest name mismatch")
    require(package_manifest.get("version") == codex_manifest.get("version") == manifest["package"]["version"], "Plugin manifest version mismatch")
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
        require(icon.startswith("./"), "Icon path must be package-relative: " + field)
        require(icon[2:] in names, "Icon file is missing: " + field)
    icon_root = ET.fromstring(archive.read(interface["logo"][2:]))
    require(icon_root.tag.rsplit("}", 1)[-1] == "svg", "Plugin icon is not an SVG")

    skill_paths = [name for name in names if re.fullmatch(r"skills/[^/]+/SKILL\.md", name)]
    require(len(skill_paths) == 15, f"Expected 15 skill entrypoints, found {len(skill_paths)}")
    skill_ids = []
    for name in skill_paths:
        text = archive.read(name).decode("utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\s*\r?\n|\Z)", text, re.S)
        require(match is not None, "Skill frontmatter is missing: " + name)
        front = yaml.safe_load(match.group(1))
        require(isinstance(front, dict) and bool(front.get("name")) and bool(front.get("description")), "Skill name/description is missing: " + name)
        skill_ids.append(front["name"])
    require(len(set(skill_ids)) == 15, "Skill frontmatter names are not unique")

    markdown_paths = [name for name in names if name.startswith("skills/") and name.endswith(".md")]
    markdown_paths.append("docs/model-evidence.md")
    for name in markdown_paths:
        text = archive.read(name).decode("utf-8")
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

    skill_records = snapshot.get("originalSkillFiles")
    require(isinstance(skill_records, list) and len(skill_records) == 104, "Pinned original skill inventory must contain 104 files")
    expected_paths = git_bytes("ls-tree", "-r", "--name-only", PINNED, "--", "skills").decode("utf-8").splitlines()
    by_path = {record.get("path"): record for record in skill_records}
    require(len(by_path) == len(skill_records) and set(by_path) == set(expected_paths), "Pinned original skill paths differ from Git tree")
    lfs_records = snapshot.get("lfsPayloadResolutions", [])
    lfs_by_path = {record.get("path"): record for record in lfs_records}
    require(len(lfs_by_path) == 8, "Manifest must record eight LFS payload resolutions")
    crlf_matches = raw_matches = lfs_matches = 0
    skill_bytes = 0
    for name in expected_paths:
        record = by_path[name]
        data = archive.read(name)
        require(len(data) == record.get("bytes"), "Original-skill byte count mismatch: " + name)
        require(hashlib.sha256(data).hexdigest() == record.get("sha256"), "Original-skill hash mismatch: " + name)
        original = git_bytes("show", f"{PINNED}:{name}")
        if original.startswith(POINTER_PREFIX):
            oid, expected_bytes = pointer_info(original)
            resolution = lfs_by_path.get(name)
            require(resolution is not None and resolution.get("oid") == oid and resolution.get("bytes") == expected_bytes, "LFS resolution record differs from pinned pointer: " + name)
            require(hashlib.sha256(data).hexdigest() == oid and len(data) == expected_bytes, "Resolved LFS payload differs from pinned pointer: " + name)
            lfs_matches += 1
        elif data == original:
            raw_matches += 1
        elif b"\r\n" in data and data.replace(b"\r\n", b"\n") == original:
            crlf_matches += 1
        else:
            raise AssertionError("Pinned source differs outside CRLF normalization or LFS resolution: " + name)
        skill_bytes += len(data)
    require(set(lfs_by_path) == {name for name in expected_paths if git_bytes("show", f"{PINNED}:{name}").startswith(POINTER_PREFIX)}, "LFS resolution paths differ from pinned pointers")
    require(crlf_matches + raw_matches + lfs_matches == 104 and lfs_matches == 8, "Pinned source comparison counts do not reconcile")
    require(snapshot.get("originalSkillFileCount") == 104 and snapshot.get("originalSkillBytes") == skill_bytes, "Pinned source totals mismatch")

    delivery_only = manifest.get("deliveryOnlyFiles", [])
    if isinstance(delivery_only, dict):
        delivery_only = [delivery_only]
    delivery_by_path = {record.get("path"): record for record in delivery_only}
    require(len(delivery_by_path) == len(delivery_only), "Delivery-only manifest paths are duplicated")
    notice_path = "skills/oneirloom-model-qwen-image-2-1/references/official/Notice"
    marketplace_path = ".agents/plugins/marketplace.json"
    require(notice_path in delivery_by_path and notice_path in names and delivery_by_path[notice_path].get("includedInZip") is True, "Required Qwen Notice is not declared and packaged")
    require(marketplace_path in delivery_by_path and marketplace_path not in names and delivery_by_path[marketplace_path].get("includedInZip") is False, "Local marketplace file is not correctly excluded")
    for name, record in delivery_by_path.items():
        data = ROOT.joinpath(*PurePosixPath(name).parts).read_bytes()
        require(hashlib.sha256(data).hexdigest() == record.get("sha256"), "Delivery-only file hash mismatch: " + name)
        if "bytes" in record:
            require(len(data) == record["bytes"], "Delivery-only file byte count mismatch: " + name)

    zip_sha = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    sums = {}
    for line in checksums_path.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        digest, name = line.split("  ", 1)
        require(name not in sums, "Duplicate checksum path: " + name)
        sums[name] = digest
    expected_sums = {name: hashlib.sha256(archive.read(name)).hexdigest() for name in names}
    expected_sums[archive_path.name] = zip_sha
    require(sums == expected_sums, "External SHA256SUMS.txt does not match the package and ZIP")

image_count = sum(1 for name in names if name.lower().endswith(tuple(RASTER_SUFFIXES)))
svg_count = sum(1 for name in names if name.lower().endswith(".svg"))
report = {
    "passed": True,
    "zip": str(archive_path),
    "zipSha256": zip_sha,
    "zipBytes": archive_path.stat().st_size,
    "entries": len(names),
    "inventoryRecords": len(inventory),
    "uncompressedBytes": uncompressed_bytes,
    "maximumEntryBytes": max_member_bytes,
    "maximumPathCharacters": max_path_chars,
    "maximumPathSegments": max_depth,
    "zeroLfsPointers": len(pointer_paths) == 0,
    "lfsPayloadsMatched": lfs_matches,
    "skillEntrypoints": len(skill_paths),
    "deliveryOnlyNoticeDeclared": True,
    "excludedMarketplaceNotPackaged": True,
    "imageDecodeCount": image_count,
    "svgXmlCount": svg_count,
    "pinnedSkillFileComparisons": {"crlfNormalized": crlf_matches, "byteForByte": raw_matches, "lfsOidAndSize": lfs_matches},
    "checks": ["exact curated archive inventory", "source manifest hashes and sizes", "plugin author and interface", "15 skill frontmatters", "local skill and model-evidence links", "raster image decode and SVG XML", "Git snapshot and LFS OID/size comparisons", "delivery-only Notice classification", "deterministic timestamp and deflate compression", "official ZIP size, entry-count, and path-depth limits", "external SHA-256 checksums"],
    "officialPathLengthLimit": "The cited official reference names a supported path-length limit but does not publish a numeric value; measured maximum is reported above."
}
print(json.dumps(report, ensure_ascii=False, sort_keys=True))
