from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import stat
import zipfile

ROOT = Path(__file__).resolve().parents[1]
POINTER_PREFIX = b"version https://git-lfs.github.com/spec/v1\n"
parser = argparse.ArgumentParser()
parser.add_argument("--output", default="dist-plugin")
args = parser.parse_args()
out = Path(args.output).resolve()
out.mkdir(parents=True, exist_ok=True)
manifest_path = ROOT / "SOURCE-MANIFEST.json"
manifest_bytes = manifest_path.read_bytes()
manifest = json.loads(manifest_bytes.decode("utf-8"))
version = manifest.get("package", {}).get("version")
if version != "0.1.1" or manifest.get("package", {}).get("name") != "oneirloom":
    raise SystemExit("SOURCE-MANIFEST.json package identity/version mismatch")
if manifest.get("sourceSnapshot", {}).get("commit") != "8d195d4fc9404d5da71733c861fd947aa109d4f1":
    raise SystemExit("SOURCE-MANIFEST.json is not pinned to the selected skill snapshot")
records = manifest.get("packagedFilesExceptThisManifest")
if not isinstance(records, list) or len(records) != 116:
    raise SystemExit("SOURCE-MANIFEST.json must inventory the curated 116 non-manifest files")
paths = [record.get("path") for record in records]
if len(set(paths)) != len(paths) or "SOURCE-MANIFEST.json" in paths:
    raise SystemExit("SOURCE-MANIFEST.json inventory contains duplicates or itself")
entries = {}
for record in records:
    name = record["path"]
    parts = name.split("/")
    if not name or "\\" in name or name.startswith("/") or name != name.strip() or any(part in ("", ".", "..") for part in parts):
        raise SystemExit("Unsafe inventory path: " + repr(name))
    if len(parts) > 20:
        raise SystemExit("Inventory path exceeds the 20-segment limit: " + name)
    path = ROOT.joinpath(*PurePosixPath(name).parts)
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if len(data) != record.get("bytes") or digest != record.get("sha256"):
        raise SystemExit("Source file does not match manifest inventory: " + name)
    if data.startswith(POINTER_PREFIX):
        raise SystemExit("Git LFS pointer is not a package payload: " + name)
    entries[name] = data
if manifest_bytes.startswith(POINTER_PREFIX):
    raise SystemExit("SOURCE-MANIFEST.json unexpectedly contains an LFS pointer")
entries["SOURCE-MANIFEST.json"] = manifest_bytes
target = out / f"oneirloom-{version}.zip"
with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for name, data in sorted(entries.items()):
        info = zipfile.ZipInfo(name, (2026, 10, 2, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.create_system = 3
        info.external_attr = (stat.S_IFREG | 0o644) << 16
        archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
zip_bytes = target.read_bytes()
zip_sha = hashlib.sha256(zip_bytes).hexdigest()
checksums = [f"{hashlib.sha256(data).hexdigest()}  {name}" for name, data in sorted(entries.items())]
checksums.append(f"{zip_sha}  {target.name}")
with (out / "SHA256SUMS.txt").open("w", encoding="utf-8", newline="\n") as stream:
    stream.write("\n".join(checksums) + "\n")
print(json.dumps({"zip": str(target), "sha256": zip_sha, "sizeBytes": len(zip_bytes), "entries": len(entries), "lfsPointers": 0}, sort_keys=True))
