#!/usr/bin/env python3
"""Check or update deterministic Oneirloom source and package metadata."""

from __future__ import annotations

import argparse
import copy
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/PigeonAI-Yang/oneirloom"
GITHUB_REPOSITORY = "PigeonAI-Yang/oneirloom"
CATALOG_ORDER = [
    "oneirloom",
    "oneirloom-dream-weaving",
    "oneirloom-visual-analysis",
    "oneirloom-product-art-direction",
    "oneirloom-camera-composition",
    "oneirloom-color-light",
    "oneirloom-character-sheet",
    "oneirloom-expression-stickers",
    "oneirloom-icon-design",
    "oneirloom-brand-identity",
    "oneirloom-figure-art",
    "oneirloom-style-photography",
    "oneirloom-style-illustration",
    "oneirloom-style-design",
    "oneirloom-craft-construction",
    "oneirloom-digital-form",
    "oneirloom-space-conception",
    "oneirloom-model-krea-2",
    "oneirloom-model-qwen-image-2-1",
    "oneirloom-result-diagnosis",
    "oneirloom-image-tutorial",
    "oneirloom-prompt-card",
]
COPY_FIELDS = {"zh", "en", "zhDescription", "enDescription"}
VERSION_PATTERN = re.compile(
    r"[0-9]+(?:\.[0-9]+){2}(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?\Z"
)
SKILL_ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


class MetadataError(Exception):
    pass


def relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_bytes().decode("utf-8-sig"))
    except FileNotFoundError as exc:
        raise MetadataError(f"Required input is missing: {relative(path)}") from exc
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise MetadataError(f"Cannot read JSON input {relative(path)}: {exc}") from exc


def require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise MetadataError(f"{label} must be a JSON object.")
    return value


def require_version(value: Any, label: str) -> str:
    if not isinstance(value, str) or not VERSION_PATTERN.fullmatch(value):
        raise MetadataError(f"{label} must be a three-part version with an optional prerelease or build suffix.")
    return value


def validate_skill_id(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SKILL_ID_PATTERN.fullmatch(value):
        raise MetadataError(f"{label} contains an invalid skill ID: {value!r}")
    return value


def discover_skill_ids() -> list[str]:
    skills_root = ROOT / "skills"
    if not skills_root.is_dir():
        raise MetadataError("Required source directory is missing: skills/")
    try:
        ids = sorted(
            path.name
            for path in skills_root.iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        )
    except OSError as exc:
        raise MetadataError(f"Cannot read the skills/ directory: {exc}") from exc
    if not ids:
        raise MetadataError("No skills/*/SKILL.md entries were found.")
    for skill_id in ids:
        validate_skill_id(skill_id, "skills/")
    return ids


def ordered_skill_ids(skill_ids: list[str]) -> list[str]:
    present = set(skill_ids)
    known = [skill_id for skill_id in CATALOG_ORDER if skill_id in present]
    extras = sorted(present.difference(CATALOG_ORDER))
    return known + extras


def validate_copy_labels(value: Any, skill_ids: list[str]) -> dict[str, dict[str, str]]:
    labels = require_object(value, "docs/project-copy.json")
    current_ids = set(skill_ids)
    missing = sorted(current_ids.difference(labels))
    extra = sorted(set(labels).difference(current_ids))
    if missing or extra:
        details = []
        if missing:
            details.append(
                "missing bilingual labels for current skill IDs: "
                + ", ".join(missing)
                + ". Add zh, en, zhDescription, and enDescription for each ID"
            )
        if extra:
            details.append("labels do not match current skill IDs: " + ", ".join(extra))
        raise MetadataError("docs/project-copy.json " + "; ".join(details) + ".")

    result: dict[str, dict[str, str]] = {}
    for skill_id in ordered_skill_ids(skill_ids):
        entry = require_object(labels[skill_id], f"docs/project-copy.json[{skill_id!r}]")
        if set(entry) != COPY_FIELDS:
            raise MetadataError(
                f"docs/project-copy.json[{skill_id!r}] must contain only "
                "zh, en, zhDescription, and enDescription."
            )
        clean: dict[str, str] = {}
        for field in ("zh", "en", "zhDescription", "enDescription"):
            text = entry[field]
            if not isinstance(text, str) or not text.strip():
                raise MetadataError(f"docs/project-copy.json[{skill_id!r}].{field} must be a non-empty string.")
            if "\n" in text or "\r" in text:
                raise MetadataError(f"docs/project-copy.json[{skill_id!r}].{field} must be one line.")
            clean[field] = text.strip()
        result[skill_id] = clean
    return result


def read_inputs() -> dict[str, Any]:
    source_plugin = require_object(load_json(ROOT / ".codex-plugin" / "plugin.json"), ".codex-plugin/plugin.json")
    if source_plugin.get("name") != "oneirloom":
        raise MetadataError(".codex-plugin/plugin.json must name the plugin oneirloom.")
    source_version = require_version(source_plugin.get("version"), ".codex-plugin/plugin.json.version")

    package_manifest = require_object(load_json(ROOT / "SOURCE-MANIFEST.json"), "SOURCE-MANIFEST.json")
    package = require_object(package_manifest.get("package"), "SOURCE-MANIFEST.json.package")
    if package.get("name") != "oneirloom":
        raise MetadataError("SOURCE-MANIFEST.json.package.name must be oneirloom.")
    package_version = require_version(package.get("version"), "SOURCE-MANIFEST.json.package.version")
    package_skill_ids = package_manifest.get("skillIds")
    if not isinstance(package_skill_ids, list) or not package_skill_ids:
        raise MetadataError("SOURCE-MANIFEST.json.skillIds must be a non-empty array.")
    for skill_id in package_skill_ids:
        validate_skill_id(skill_id, "SOURCE-MANIFEST.json.skillIds")
    if len(package_skill_ids) != len(set(package_skill_ids)):
        raise MetadataError("SOURCE-MANIFEST.json.skillIds contains duplicate IDs.")

    source_skill_ids = discover_skill_ids()
    copies = validate_copy_labels(load_json(ROOT / "docs" / "project-copy.json"), source_skill_ids)
    source_interface = require_object(source_plugin.get("interface"), ".codex-plugin/plugin.json.interface")
    if not isinstance(source_interface.get("longDescription"), str):
        raise MetadataError(".codex-plugin/plugin.json.interface.longDescription must be a string.")

    return {
        "sourcePlugin": source_plugin,
        "sourceInterface": source_interface,
        "sourceVersion": source_version,
        "sourceSkillIds": ordered_skill_ids(source_skill_ids),
        "copies": copies,
        "packageVersion": package_version,
        "packageSkillIds": package_skill_ids,
    }


def make_artifact(inputs: dict[str, Any]) -> dict[str, Any]:
    source_version = inputs["sourceVersion"]
    package_version = inputs["packageVersion"]
    source_count = len(inputs["sourceSkillIds"])
    package_count = len(inputs["packageSkillIds"])
    package_tag = "v" + package_version
    skills = []
    for skill_id in inputs["sourceSkillIds"]:
        copy = inputs["copies"][skill_id]
        skills.append(
            {
                "id": skill_id,
                "zh": copy["zh"],
                "en": copy["en"],
                "zhDescription": copy["zhDescription"],
                "enDescription": copy["enDescription"],
            }
        )
    return {
        "schemaVersion": 1,
        "repository": REPOSITORY,
        "source": {
            "version": source_version,
            "skillCount": source_count,
            "skillIds": inputs["sourceSkillIds"],
            "status": "development-preview",
            "notesUrl": f"{REPOSITORY}/blob/main/docs/releases/{source_version}.md",
        },
        "package": {
            "version": package_version,
            "skillCount": package_count,
            "tag": package_tag,
            "downloadUrl": f"{REPOSITORY}/releases/download/{package_tag}/oneirloom-{package_version}.zip",
            "checksumUrl": f"{REPOSITORY}/releases/download/{package_tag}/SHA256SUMS.txt",
            "releaseUrl": f"{REPOSITORY}/releases/tag/{package_tag}",
        },
        "skills": skills,
        "copy": {
            "zh": {
                "summary": "围绕视觉提示词、参考图分析、创作方法与结果诊断提供 Agent Skills。",
                "sourceStatus": f"{source_version} 是开发源码预览，包含 {source_count} 个 Skill。",
                "packageStatus": f"已发布的冻结包 {package_version} 包含 {package_count} 个 Skill。",
            },
            "en": {
                "summary": "Agent Skills for visual prompts, reference analysis, creation methods, and result diagnosis.",
                "sourceStatus": f"{source_version} is a development source preview with {source_count} skills.",
                "packageStatus": f"The published frozen package {package_version} contains {package_count} skills.",
            },
        },
        "github": {
            "description": (
                f"Oneirloom / 织梦师: {source_count} visual creation Agent Skills in "
                f"{source_version} source; frozen {package_version} package has {package_count}. "
                "Prompts, reference analysis, craft, digital form, and spatial concepts."
            )
        },
    }


def json_text(value: Any, newline: str = "\n", bom: bool = False) -> bytes:
    rendered = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    text = rendered.replace("\n", newline)
    prefix = "\ufeff" if bom else ""
    return (prefix + text).encode("utf-8")


def preserved_json_bytes(path: Path, value: Any) -> bytes:
    current = path.read_bytes()
    newline = "\r\n" if b"\r\n" in current else "\n"
    bom = current.startswith(b"\xef\xbb\xbf")
    return json_text(value, newline, bom)


def marker_tokens(name: str) -> tuple[str, str]:
    return (f"<!-- project-metadata:{name}:start -->", f"<!-- project-metadata:{name}:end -->")


def replace_region_text(original: str, path_label: str, name: str, replacement: str, inline: bool = False) -> str:
    start_token, end_token = marker_tokens(name)
    if original.count(start_token) != 1 or original.count(end_token) != 1:
        raise MetadataError(
            f"{path_label} must contain exactly one {start_token} and one {end_token} marker."
        )
    start = original.index(start_token) + len(start_token)
    end = original.index(end_token, start)
    if end < start:
        raise MetadataError(f"{path_label} has reversed {name} markers.")
    if inline:
        updated = original[:start] + replacement + original[end:]
    else:
        newline = "\r\n" if "\r\n" in original else "\n"
        content = replacement.replace("\n", newline)
        updated = original[:start] + newline + content + newline + original[end:]
    return updated


def replace_region(path: Path, name: str, replacement: str, inline: bool = False) -> bytes:
    try:
        original = path.read_bytes().decode("utf-8")
    except FileNotFoundError as exc:
        raise MetadataError(f"Required generated target is missing: {relative(path)}") from exc
    except (OSError, UnicodeError) as exc:
        raise MetadataError(f"Cannot read generated target {relative(path)}: {exc}") from exc
    return replace_region_text(original, relative(path), name, replacement, inline).encode("utf-8")


def source_intro(artifact: dict[str, Any], language: str) -> str:
    source = artifact["source"]
    package = artifact["package"]
    if language == "zh":
        return (
            f'<p>当前源码包含 {source["skillCount"]} 个视觉创作 Skill。'
            f'{source["version"]} 是开发源码预览，尚无对应发布包；已发布的冻结包为 '
            f'{package["version"]}，包含 {package["skillCount"]} 项。'
            f'<a href="docs/releases/{source["version"]}.md">查看源码记录</a></p>'
        )
    return (
        f'<p>The current source contains {source["skillCount"]} visual-creation Agent Skills. '
        f'{source["version"]} is a development source preview with no matching package. '
        f'The published frozen package is {package["version"]} with {package["skillCount"]} skills. '
        f'<a href="docs/releases/{source["version"]}.md">Read the source record</a>.</p>'
    )


def table_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def skill_table(artifact: dict[str, Any], language: str) -> str:
    if language == "zh":
        headers = "| 技能 | 用途 |"
        separators = "| --- | --- |"
    else:
        headers = "| Skill | Purpose |"
        separators = "| --- | --- |"
    rows = [headers, separators]
    for skill in artifact["skills"]:
        link = f'[{skill["id"]}](skills/{skill["id"]}/SKILL.md)'
        if language == "zh":
            cells = [link, skill["zhDescription"]]
        else:
            cells = [link, skill["enDescription"]]
        rows.append("| " + " | ".join(table_cell(cell) for cell in cells) + " |")
    return "\n".join(rows)


def package_badge(artifact: dict[str, Any], language: str) -> str:
    package = artifact["package"]
    if language == "zh":
        return (
            f'<p align="center"><a href="{package["releaseUrl"]}">已发布的冻结版本：'
            f'{package["version"]}（{package["skillCount"]} 项）</a> · '
            f'<a href="{package["downloadUrl"]}">下载冻结安装包（{package["skillCount"]} 项）</a></p>'
        )
    return (
        f'<p align="center"><a href="{package["releaseUrl"]}">Frozen released version: '
        f'{package["version"]} ({package["skillCount"]} skills)</a> · '
        f'<a href="{package["downloadUrl"]}">Download the frozen package '
        f'({package["skillCount"]} skills)</a></p>'
    )


def guidance_heading(artifact: dict[str, Any], language: str) -> str:
    version = artifact["package"]["version"]
    if language == "zh":
        return f"## 冻结的 {version} 版本包含的工作指导"
    return f"## Guidance in the frozen {version} package"


def readme_current_status(artifact: dict[str, Any], language: str) -> str:
    source = artifact["source"]
    package = artifact["package"]
    publication_url = f"docs/releases/{package['version']}-publication.md"
    if language == "zh":
        return (
            f'这些指导属于冻结的 {package["version"]} 包。{source["version"]} 源码仍是开发预览，'
            f'尚无对应发布包；其新对话行为和生成图像质量尚未验证。{package["version"]} 的日期化发布记录'
            f'见[发布状态]({publication_url})。'
        )
    return (
        f'These instructions belong to the frozen {package["version"]} package. The {source["version"]} '
        f'source remains a development preview with no corresponding package; its new-session behavior and '
        f'generated image quality have not been verified. See the dated [{package["version"]} publication '
        f'record]({publication_url}) for its account checks.'
    )


def install_heading(artifact: dict[str, Any]) -> str:
    return f'### 安装冻结的 {artifact["package"]["version"]} 技能包'


def readme_install_intro(artifact: dict[str, Any], language: str) -> str:
    source = artifact["source"]
    package = artifact["package"]
    publication_url = f"docs/releases/{package['version']}-publication.md"
    if language == "zh":
        return (
            f'以下安装步骤只适用于冻结的 `{package["version"]}` 发布包，包含 '
            f'**{package["skillCount"]} 个免费技能**，不含 {source["version"]} 源码改动。'
            f'请从[固定安装包地址]({package["downloadUrl"]})下载发布者提供的 ZIP，并使用'
            f'[同页校验文件 SHA256SUMS.txt]({package["checksumUrl"]})核对；不要把 GitHub 自动生成的源码 ZIP '
            f'当作已检查安装包。'
        )
    return (
        f'The frozen `{package["version"]}` package has **{package["skillCount"]} free skills** and does not '
        f'contain the {source["version"]} source changes. Download the publisher-built ZIP from the '
        f'[fixed package URL]({package["downloadUrl"]}) and verify it with '
        f'[SHA256SUMS.txt]({package["checksumUrl"]}). Do not use GitHub\'s generated source archive as the '
        f'inspected installation package. See [installation and rollback](docs/INSTALL.md), '
        f'[frozen-package publication status]({publication_url}), and '
        f'[prepublication compatibility and verification records](docs/COMPATIBILITY.md).'
    )


def readme_install_copy(artifact: dict[str, Any], language: str) -> str:
    package = artifact["package"]
    publication_url = f"docs/releases/{package['version']}-publication.md"
    if language == "zh":
        return (
            f'按[安装与升级回退说明](docs/INSTALL.md)，将包内 `skills/` 的 {package["skillCount"]} 个目录完整复制到'
            f'新项目的 `.agents/skills/`，保持同级关系。公开包默认不含私有品牌水印，提示词卡可直接制作无水印版本。'
            f'已有安装先保留准确备份与包哈希。请以[冻结包发布状态]({publication_url})为准；'
            f'[发布前候选验证记录](docs/COMPATIBILITY.md)保留的是发布前准备阶段的待验状态。'
        )
    return (
        f'1. Follow the installation guide to copy all {package["skillCount"]} directories in the frozen package under '
        f'`skills/` as siblings into a new project\'s `.agents/skills/`. Preserve the exact prior installation and '
        f'package hash before an upgrade.'
    )


def methods_summary_row(artifact: dict[str, Any]) -> str:
    methods = [skill["en"] for skill in artifact["skills"] if skill["id"] != "oneirloom"]
    return "| Methods | " + "; ".join(table_cell(method) for method in methods) + " |"


def architecture_status(artifact: dict[str, Any]) -> str:
    source = artifact["source"]
    package = artifact["package"]
    return (
        f'The {source["version"]} source contains {source["skillCount"]} sibling '
        "`skills/*/SKILL.md` entries. It is a development source preview with no corresponding package or installation. "
        "The new method guidance is text only. No new render or native-model result validates it, and image generation "
        "and image quality remain unverified. The frozen `"
        f'{package["tag"]}` package remains at {package["skillCount"]} skills. A host discovers metadata and explicitly '
        "reads the chosen entry. The coordinator is optional for direct capability use. This is a document-reading "
        "design, not a runtime loader or a required layer count."
    )


def install_intro(artifact: dict[str, Any]) -> str:
    source = artifact["source"]
    package = artifact["package"]
    publication_url = f'{REPOSITORY}/blob/main/docs/releases/{package["version"]}-publication.md'
    return "\n".join(
        [
            f'This guide installs the published frozen package `{package["version"]}`, which contains {package["skillCount"]} sibling skills.',
            f'The current `{source["version"]}` source contains {source["skillCount"]} skills and remains a development preview with no matching package.',
            f'See the [source record]({source["notesUrl"]}) and the [frozen-package publication record]({publication_url}).',
        ]
    )


def manifest_count_instruction(artifact: dict[str, Any]) -> str:
    package = artifact["package"]
    return (
        f'3. Check that the manifest records package version `{package["version"]}` and the '
        f'{package["skillCount"]} skill IDs listed below. Keep the ZIP, `SHA256SUMS.txt`, and manifest together '
        f'with your installation record.'
    )


def package_hash_instruction(artifact: dict[str, Any]) -> str:
    filename = f'oneirloom-{artifact["package"]["version"]}.zip'
    return (
        f'1. Compare the ZIP\'s SHA-256 with the exact filename in `SHA256SUMS.txt`. In PowerShell, run '
        f'`Get-FileHash -Algorithm SHA256 -LiteralPath \'./{filename}\'` in the download directory.'
    )


def install_copy_instruction(artifact: dict[str, Any]) -> str:
    return (
        f'Start with an empty project so existing skills do not need to be overwritten. Copy all '
        f'{artifact["package"]["skillCount"]} directories inside the package\'s `skills/` into the project\'s '
        f'`.agents/skills/`, retaining every directory name and its internal files. Do not put the collection inside '
        f'one extra `oneirloom/` directory.'
    )


def install_obtain(artifact: dict[str, Any]) -> str:
    package = artifact["package"]
    filename = f'oneirloom-{package["version"]}.zip'
    return "\n".join(
        [
            "## Obtain and check the frozen package",
            "",
            f'Download the publisher-built [{filename}]({package["downloadUrl"]}) and its [SHA256SUMS.txt]({package["checksumUrl"]}).',
            "Compare the downloaded ZIP with its exact filename in the checksum file before extraction.",
        ]
    )


def compatibility_status(artifact: dict[str, Any]) -> str:
    source = artifact["source"]
    package = artifact["package"]
    publication_url = f'{REPOSITORY}/blob/main/docs/releases/{package["version"]}-publication.md'
    return "\n".join(
        [
            "## Current source and package status",
            "",
            f'The current `{source["version"]}` source contains {source["skillCount"]} skills and remains a development preview without a matching package.',
            f'The published frozen `{package["version"]}` package contains {package["skillCount"]} skills. See the [source record]({source["notesUrl"]}) and [publication record]({publication_url}).',
            "The candidate table below preserves prepublication checks. Its pending items describe that earlier review, not current package availability.",
        ]
    )


def project_files_source_row(artifact: dict[str, Any]) -> str:
    source = artifact["source"]
    package = artifact["package"]
    return (
        f' Current {source["version"]} source | {source["skillCount"]} source skills; development preview with no corresponding package. '
        f'The published frozen `{package["version"]}` package contains {package["skillCount"]} skills. '
        f'See the [source record](docs/releases/{source["version"]}.md) and [frozen-package publication record]'
        f'(docs/releases/{package["version"]}-publication.md).'
    )


def source_description(source_count: int) -> str:
    return (
        "Visual prompting, reference analysis, craft construction, digital form, spatial concepts, "
        f"and result diagnosis with {source_count} source skills."
    )


def long_description(artifact: dict[str, Any]) -> str:
    source = artifact["source"]
    package = artifact["package"]
    return (
        f'The {source["version"]} source tree contains {source["skillCount"]} skills for visual prompts, reference analysis, '
        "craft construction, digital form, space conception, composition and light, model adaptation, and result diagnosis. "
        f'This is a development source preview with no corresponding package; the published frozen {package["version"]} '
        f'package remains at {package["skillCount"]} skills. A host with image input is needed for visual analysis. Prompts do not '
        "generate images; generation requires a separately available model or tool and is not guaranteed. The optional prompt-card "
        "renderer requires local Python, Pillow, Playwright, a browser, and file access. No MCP server, account connection, "
        "background service, or automatic upload is bundled. Package and text checks do not establish image-generation quality."
    )


def release_note(artifact: dict[str, Any]) -> str:
    source = artifact["source"]
    package = artifact["package"]
    return (
        f'{source["version"]} is a development source preview with {source["skillCount"]} skills and no corresponding package. '
        f'The published frozen {package["version"]} package contains {package["skillCount"]} skills. '
        "Package and text checks do not establish image-generation quality."
    )


def marketplace_name(version: str) -> str:
    return "oneirloom-" + re.sub(r"[^a-z0-9]+", "-", version.lower()).strip("-")


def marketplace_display_name(version: str) -> str:
    return "Oneirloom " + version.replace("-", " ").replace("+", " ").title()


def generated_targets(inputs: dict[str, Any], artifact: dict[str, Any]) -> dict[str, bytes]:
    output: dict[str, bytes] = {}
    source_count = artifact["source"]["skillCount"]
    description = source_description(source_count)
    long_desc = long_description(artifact)

    source_plugin_path = ROOT / ".codex-plugin" / "plugin.json"
    source_plugin = copy.deepcopy(inputs["sourcePlugin"])
    source_plugin["description"] = description
    source_plugin["interface"]["longDescription"] = long_desc
    output[relative(source_plugin_path)] = preserved_json_bytes(source_plugin_path, source_plugin)

    root_plugin_path = ROOT / "plugin.json"
    root_plugin = require_object(load_json(root_plugin_path), "plugin.json")
    extensions = require_object(root_plugin.get("extensions"), "plugin.json.extensions")
    openai = require_object(extensions.get("com.openai"), "plugin.json.extensions.com.openai")
    openai_interface = require_object(openai.get("interface"), "plugin.json.extensions.com.openai.interface")
    publication = require_object(openai.get("publication"), "plugin.json.extensions.com.openai.publication")
    root_plugin["version"] = artifact["source"]["version"]
    root_plugin["description"] = description
    openai_interface["longDescription"] = long_desc
    publication["release_notes"] = release_note(artifact)
    output[relative(root_plugin_path)] = preserved_json_bytes(root_plugin_path, root_plugin)

    marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"
    marketplace = require_object(load_json(marketplace_path), ".agents/plugins/marketplace.json")
    marketplace_interface = require_object(marketplace.get("interface"), ".agents/plugins/marketplace.json.interface")
    marketplace["name"] = marketplace_name(artifact["source"]["version"])
    marketplace_interface["displayName"] = marketplace_display_name(artifact["source"]["version"])
    output[relative(marketplace_path)] = preserved_json_bytes(marketplace_path, marketplace)

    readme_zh_path = ROOT / "README.md"
    readme_zh = replace_region(
        readme_zh_path,
        "source-summary",
        source_intro(artifact, "zh"),
    ).decode("utf-8")
    for region, replacement in [
        ("package-badge", package_badge(artifact, "zh")),
        ("guidance-heading", guidance_heading(artifact, "zh")),
        ("guidance-current-status", readme_current_status(artifact, "zh")),
        ("install-heading", install_heading(artifact)),
        ("install-intro", readme_install_intro(artifact, "zh")),
        ("install-copy", readme_install_copy(artifact, "zh")),
    ]:
        readme_zh = replace_region_text(readme_zh, relative(readme_zh_path), region, replacement)
    zh_directory = "\n".join(
        [
            "主技能负责理解任务与整合交付，方法技能负责各自的判断。具体画面配方放在所属方法的模板目录中。",
            f'以下目录列出 `{artifact["source"]["version"]}` 源码中的 {source_count} 个 Skill。',
            "",
            "<details>",
            "<summary>展开全部技能</summary>",
            "",
            skill_table(artifact, "zh"),
            "",
            "</details>",
        ]
    )
    output["README.md"] = replace_region_text(
        readme_zh,
        relative(readme_zh_path),
        "skill-directory",
        zh_directory,
    ).encode("utf-8")

    readme_en_path = ROOT / "README.en.md"
    readme_en = replace_region(
        readme_en_path,
        "source-summary",
        source_intro(artifact, "en"),
    ).decode("utf-8")
    for region, replacement in [
        ("package-badge", package_badge(artifact, "en")),
        ("guidance-heading", guidance_heading(artifact, "en")),
        ("guidance-current-status", readme_current_status(artifact, "en")),
        ("install-intro", readme_install_intro(artifact, "en")),
        ("install-copy", readme_install_copy(artifact, "en")),
        ("methods-summary", methods_summary_row(artifact)),
    ]:
        readme_en = replace_region_text(readme_en, relative(readme_en_path), region, replacement)
    en_directory = "\n".join(
        [
            "## Skill directory",
            "",
            f'This table lists all {source_count} skills in the `{artifact["source"]["version"]}` source tree.',
            "",
            skill_table(artifact, "en"),
        ]
    )
    output["README.en.md"] = replace_region_text(
        readme_en,
        relative(readme_en_path),
        "skill-directory",
        en_directory,
    ).encode("utf-8")

    output["docs/architecture.md"] = replace_region(
        ROOT / "docs" / "architecture.md",
        "source-status",
        architecture_status(artifact),
    )
    install_path = ROOT / "docs" / "INSTALL.md"
    install_content = replace_region(
        install_path,
        "current-package-status",
        install_intro(artifact),
    ).decode("utf-8")
    install_text = replace_region_text(
        install_content,
        relative(install_path),
        "package-obtain",
        install_obtain(artifact),
    )
    for region, replacement in [
        ("package-title", f'# Install Oneirloom {artifact["package"]["version"]}'),
        ("package-hash-command", package_hash_instruction(artifact)),
        ("manifest-count", manifest_count_instruction(artifact)),
        ("install-copy", install_copy_instruction(artifact)),
    ]:
        install_text = replace_region_text(install_text, relative(install_path), region, replacement)
    output["docs/INSTALL.md"] = install_text.encode("utf-8")
    output["docs/COMPATIBILITY.md"] = replace_region(
        ROOT / "docs" / "COMPATIBILITY.md",
        "current-status",
        compatibility_status(artifact),
    )
    output["PROJECT-FILES.md"] = replace_region(
        ROOT / "PROJECT-FILES.md",
        "local-source-row",
        project_files_source_row(artifact),
        inline=True,
    )

    status_path = ROOT / "docs" / "project-status.json"
    output[relative(status_path)] = json_text(artifact)
    return output


def contained_path(root: Path, path: Path, label: str, must_exist: bool) -> Path:
    try:
        resolved = path.resolve(strict=must_exist)
    except OSError as exc:
        raise MetadataError(f"Invalid site-root {label}: {exc}") from exc
    if resolved != root and root not in resolved.parents:
        raise MetadataError(f"Site-root {label} must stay inside the supplied root.")
    return resolved


def validate_site_root(site_root_value: Path) -> tuple[Path, Path]:
    try:
        site_root = site_root_value.resolve(strict=True)
    except OSError as exc:
        raise MetadataError(f"The supplied site root does not exist: {exc}") from exc
    if not site_root.is_dir():
        raise MetadataError("The supplied site root must be an existing directory.")

    package_path = contained_path(site_root, site_root / "package.json", "package.json", True)
    script_path = contained_path(site_root, site_root / "scripts" / "skill-pages.mjs", "scripts/skill-pages.mjs", True)
    content_dir = contained_path(site_root, site_root / "content", "content/", True)
    if not package_path.is_file():
        raise MetadataError("Site root package.json must be a file.")
    if not script_path.is_file():
        raise MetadataError("Site root scripts/skill-pages.mjs must be a file.")
    if not content_dir.is_dir():
        raise MetadataError("Site root content/ must be an existing directory.")
    package_json = require_object(load_json(package_path), "site-root/package.json")
    if package_json.get("name") != "oneirloom":
        raise MetadataError("Site root package.json must name the package oneirloom.")

    target = site_root / "content" / "oneirloom-project.json"
    if target.is_symlink():
        raise MetadataError("Site target content/oneirloom-project.json must not be a symbolic link.")
    contained_path(site_root, target, "content/oneirloom-project.json", target.exists())
    return site_root, target


def atomic_write(path: Path, content: bytes) -> None:
    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as temp_file:
            temp_file.write(content)
            temp_file.flush()
            os.fsync(temp_file.fileno())
            temp_path = Path(temp_file.name)
        os.replace(temp_path, path)
    except OSError as exc:
        if temp_path is not None:
            try:
                temp_path.unlink(missing_ok=True)
            except OSError:
                pass
        raise MetadataError(f"Cannot update {path}: {exc}") from exc


def check_file_targets(outputs: dict[str, bytes]) -> list[str]:
    drift: list[str] = []
    for target, expected in outputs.items():
        path = ROOT / Path(target)
        try:
            current = path.read_bytes()
        except FileNotFoundError:
            current = None
        except OSError as exc:
            raise MetadataError(f"Cannot read generated target {target}: {exc}") from exc
        if current != expected:
            drift.append(target)
    return drift


def write_file_targets(
    outputs: dict[str, bytes],
    drift: list[str],
    changed: list[str],
    remaining_drift: list[str],
) -> None:
    for target in drift:
        path = ROOT / Path(target)
        atomic_write(path, outputs[target])
        changed.append(target)
        if target in remaining_drift:
            remaining_drift.remove(target)


def gh_call(arguments: list[str], operation: str) -> str:
    try:
        result = subprocess.run(
            ["gh", *arguments],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
            check=False,
        )
    except FileNotFoundError as exc:
        raise MetadataError("GitHub CLI `gh` is not available on PATH.") from exc
    except subprocess.TimeoutExpired as exc:
        raise MetadataError(f"GitHub {operation} timed out; no retry was attempted.") from exc
    except OSError as exc:
        raise MetadataError(f"GitHub {operation} could not start: {exc}") from exc
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip().splitlines()
        suffix = f" Output: {detail[0][:400]}" if detail else ""
        raise MetadataError(
            f"GitHub {operation} failed with exit code {result.returncode}.{suffix} No retry was attempted."
        )
    return result.stdout.strip()


def github_view() -> str:
    raw = gh_call(
        ["repo", "view", GITHUB_REPOSITORY, "--json", "description", "--jq", ".description"],
        "description read",
    )
    return raw


def github_sync(description: str) -> str:
    gh_call(
        ["repo", "edit", GITHUB_REPOSITORY, "--description", description],
        "description update",
    )
    return github_view()


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check or update Oneirloom metadata from the source plugin version, "
            "skills/*/SKILL.md, frozen package manifest, and docs/project-copy.json."
        )
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", dest="write", action="store_false", help="Check generated files without writing. This is the default.")
    mode.add_argument("--write", dest="write", action="store_true", help="Write generated repository files.")
    parser.set_defaults(write=False)
    parser.add_argument(
        "--site-root",
        type=Path,
        help="Check or copy only content/oneirloom-project.json under a validated existing Oneirloom site root.",
    )
    github = parser.add_mutually_exclusive_group()
    github.add_argument("--github-check", action="store_true", help="Read the GitHub repository description and compare it.")
    github.add_argument("--github-sync", action="store_true", help="Set only the GitHub repository description and read it back. Requires --write.")
    parser.add_argument("--json", action="store_true", help="Print a JSON report with counts, drift, changes, and checks.")
    return parser.parse_args(argv)


def base_report(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "mode": "write" if args.write else "check",
        "changedFiles": [],
        "driftFiles": [],
        "sourceSkillCount": None,
        "packageSkillCount": None,
        "currentGitHubDescription": None,
        "expectedGitHubDescription": None,
        "checks": [],
        "errors": [],
    }


def print_report(report: dict[str, Any], json_mode: bool, exit_code: int) -> int:
    if json_mode:
        sys.stdout.write(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    else:
        status = "error" if exit_code == 2 else "drift" if exit_code == 1 else "ok"
        print(f"Project metadata {status}.")
        if report.get("sourceSkillCount") is not None:
            print(
                f'Source skills: {report["sourceSkillCount"]}. '
                f'Frozen package skills: {report["packageSkillCount"]}.'
            )
        for field in ("changedFiles", "driftFiles", "errors"):
            for item in report[field]:
                print(f"{field}: {item}")
    return exit_code


def main(argv: list[str] | None = None) -> int:
    try:
        args = parse_args(argv)
    except SystemExit as exc:
        return int(exc.code)
    report = base_report(args)
    exit_code = 0
    try:
        if args.github_sync and not args.write:
            raise MetadataError("--github-sync requires --write; default checks never update GitHub.")

        inputs = read_inputs()
        artifact = make_artifact(inputs)
        outputs = generated_targets(inputs, artifact)
        expected_description = artifact["github"]["description"]
        report["sourceSkillCount"] = artifact["source"]["skillCount"]
        report["packageSkillCount"] = artifact["package"]["skillCount"]
        report["sourceVersion"] = artifact["source"]["version"]
        report["packageVersion"] = artifact["package"]["version"]
        report["expectedGitHubDescription"] = expected_description
        report["checks"].extend(
            [
                {"name": "source-inventory", "status": "pass", "skillCount": report["sourceSkillCount"]},
                {"name": "frozen-package-manifest", "status": "pass", "skillCount": report["packageSkillCount"]},
                {"name": "bilingual-copy-labels", "status": "pass", "skillCount": report["sourceSkillCount"]},
            ]
        )

        site_root: Path | None = None
        site_target: Path | None = None
        if args.site_root is not None:
            site_root, site_target = validate_site_root(args.site_root)
            report["siteRoot"] = str(site_root)

        initial_drift = check_file_targets(outputs)
        site_target_rel = "site-root/content/oneirloom-project.json"
        if site_target is not None:
            expected_site_bytes = outputs["docs/project-status.json"]
            try:
                current_site_bytes = site_target.read_bytes()
            except FileNotFoundError:
                current_site_bytes = None
            except OSError as exc:
                raise MetadataError(f"Cannot read {site_target_rel}: {exc}") from exc
            if current_site_bytes != expected_site_bytes:
                initial_drift.append(site_target_rel)

        report["driftFiles"] = list(initial_drift)
        if args.write:
            repository_drift = [target for target in initial_drift if target != site_target_rel]
            write_file_targets(outputs, repository_drift, report["changedFiles"], report["driftFiles"])
            if site_target is not None and site_target_rel in initial_drift:
                atomic_write(site_target, outputs["docs/project-status.json"])
                report["changedFiles"].append(site_target_rel)
                report["driftFiles"].remove(site_target_rel)
            report["checks"].append({"name": "generated-files", "status": "written"})
        else:
            report["checks"].append(
                {"name": "generated-files", "status": "drift" if report["driftFiles"] else "pass"}
            )

        if args.github_check:
            current_description = github_view()
            report["currentGitHubDescription"] = current_description
            matches = current_description == expected_description
            report["checks"].append(
                {"name": "github-description", "status": "pass" if matches else "drift"}
            )
            if not matches:
                report["driftFiles"].append("github.description")
        elif args.github_sync:
            current_description = github_sync(expected_description)
            report["currentGitHubDescription"] = current_description
            matches = current_description == expected_description
            report["checks"].append(
                {"name": "github-description-readback", "status": "pass" if matches else "drift"}
            )
            if not matches:
                report["driftFiles"].append("github.description")

        exit_code = 1 if report["driftFiles"] else 0
    except MetadataError as exc:
        message = str(exc)
        report["errors"].append(message)
        report["checks"].append({"name": "project-metadata", "status": "error", "message": message})
        exit_code = 2
    except OSError as exc:
        message = f"Project metadata operation failed: {exc}"
        report["errors"].append(message)
        report["checks"].append({"name": "project-metadata", "status": "error", "message": message})
        exit_code = 2
    return print_report(report, args.json, exit_code)


if __name__ == "__main__":
    raise SystemExit(main())
