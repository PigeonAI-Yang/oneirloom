from __future__ import annotations

import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills" / "oneirloom-expression-stickers"
GENERATED = SKILL / "assets" / "generated"
CATALOG_PATH = GENERATED / "catalog.json"

EXPECTED_COUNTS = {
    "identity-acting-system": 4,
    "daily-sixteen": 16,
    "chat-coverage": 12,
    "pose-decomposition": 3,
    "emotion-five": 5,
    "eight-slot-workspace": 8,
    "source-export-workspace": 1,
    "custom-caption-layout": 6,
    "ten-reactions": 10,
    "extended-reaction-library": 24,
    "soft-six": 6,
    "nine-reaction-sheet": 9,
    "seven-poses": 7,
    "treatment-expression-family": 45,
}

BASE_NOTE = (
    "原生输出记录为1254×1254 RGBA；人工受众理解及平台导入、审核或接受未经验证。第三方来源中未核验或暂定的部分仍按原记录标注。"
)
IDENTITY_INTENTS = {
    "I01": "准备好了",
    "I02": "感谢",
    "I03": "完成",
    "I04": "休息",
}
CUSTOM_INTENTS = {
    "top-greeting": "上方问候留白",
    "left-reply": "左侧回复留白",
    "bottom-reassurance": "下方安慰留白",
}
FAMILY_KIND_LABELS = {
    "Flat illustration": "平涂",
    "Doodle": "涂鸦",
    "Plush": "毛绒",
    "Clay": "黏土",
    "Monochrome": "灰度",
}
REVIEW_FIELDS = (
    "limitations",
    "misses",
    "not_verified",
    "gaps",
    "remaining_limits",
    "edge_review",
    "small_size",
    "alpha",
    "layout",
    "deviations",
    "status",
)
NOTE_FIELDS = ("limitations", "not_verified", "gaps", "remaining_limits")


def _object(value: object, label: str) -> dict:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    return value


def _list(record: dict, key: str, label: str) -> list:
    if key not in record or not isinstance(record[key], list):
        raise ValueError(f"{label}.{key} must be a list")
    return record[key]


def _text(value: object, label: str, allow_none: bool = False) -> str:
    if value is None and allow_none:
        return ""
    if not isinstance(value, str):
        raise ValueError(f"{label} must be a string")
    return value


def _field(record: dict, key: str, label: str, allow_none: bool = False) -> str:
    if key not in record:
        raise ValueError(f"{label}.{key} is missing")
    return _text(record[key], f"{label}.{key}", allow_none)


def _required(record: dict, key: str, label: str) -> object:
    if key not in record:
        raise ValueError(f"{label}.{key} is missing")
    return record[key]


def _flatten_strings(value: object, label: str) -> list[str]:
    if isinstance(value, str):
        return [value.strip()] if value.strip() else []
    if isinstance(value, list):
        flattened = []
        for item in value:
            flattened.extend(_flatten_strings(item, label))
        return flattened
    if isinstance(value, dict):
        flattened = []
        for item in value.values():
            flattened.extend(_flatten_strings(item, label))
        return flattened
    if isinstance(value, bool):
        return [str(value).lower()]
    if value is None:
        return []
    raise ValueError(f"{label} contains an unsupported value")


def _review_text(value: object, label: str) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        parts = _flatten_strings(value, label)
    elif isinstance(value, dict):
        selected = [key for key in REVIEW_FIELDS if key in value]
        if not selected:
            raise ValueError(f"{label} has no supported limitation fields")
        parts = []
        for key in selected:
            parts.extend(_flatten_strings(value[key], f"{label}.{key}"))
    else:
        raise ValueError(f"{label} must be a string, list, or object")
    unique = list(dict.fromkeys(part for part in parts if part))
    return "；".join(unique)


def _same_filename(left: object, right: object, label: str) -> bool:
    left_text = _text(left, label).replace("\\", "/")
    right_text = _text(right, label).replace("\\", "/")
    return PurePosixPath(left_text).name == PurePosixPath(right_text).name


def _source_record(
    record_id: object,
    caption: object,
    intent: object,
    file_value: object,
    review: object,
    label: str,
    kind: object = None,
) -> dict:
    caption_text = _text(caption, f"{label}.caption", allow_none=True)
    intent_text = _text(intent, f"{label}.intent", allow_none=True)
    result = {
        "id": _text(record_id, f"{label}.id"),
        "caption": caption_text,
        "intent": intent_text if intent_text.strip() else caption_text,
        "file": file_value,
        "review": _review_text(review, f"{label}.review"),
    }
    if kind is not None:
        result["kind"] = _text(kind, f"{label}.kind")
    return result


def _canonical_outputs(data: dict, slug: str) -> list[dict]:
    rows = _list(data, "outputs", slug)
    records = []
    for index, raw in enumerate(rows):
        label = f"{slug}.outputs[{index}]"
        row = _object(raw, label)
        records.append(
            _source_record(
                _field(row, "id", label),
                _field(row, "caption", label, allow_none=True),
                _field(row, "intent", label),
                _field(row, "file", label),
                _required(row, "review", label),
                label,
            )
        )
    return records


def _selected_records(slug: str, data: dict) -> list[dict]:
    if slug in {"eight-slot-workspace", "source-export-workspace"}:
        return _canonical_outputs(data, slug)

    if slug == "identity-acting-system":
        selected = _list(data, "selected", slug)
        jobs = [_object(row, f"{slug}.jobs[{index}]") for index, row in enumerate(_list(data, "jobs", slug))]
        records = []
        for index, filename in enumerate(selected):
            name = _text(filename, f"{slug}.selected[{index}]")
            matches = [
                job
                for job in jobs
                if _same_filename(_field(job, "output", f"{slug}.jobs"), name, f"{slug}.jobs.output")
            ]
            if not matches:
                raise ValueError(f"{slug} has no job matching selected file {name}")
            job = matches[-1]
            job_id = _field(job, "id", f"{slug}.jobs")
            intent = next(
                (value for prefix, value in IDENTITY_INTENTS.items() if job_id.startswith(prefix)),
                "",
            )
            records.append(
                _source_record(
                    job_id,
                    "",
                    intent,
                    name,
                    _required(job, "review", f"{slug}.jobs"),
                    f"{slug}.selected[{index}]",
                )
            )
        return records

    if slug == "daily-sixteen":
        records = []
        for index, raw in enumerate(_list(data, "items", slug)):
            row = _object(raw, f"{slug}.items[{index}]")
            label = f"{slug}.items[{index}]"
            inspection = _object(row.get("finalInspection"), f"{slug}.items[{index}].finalInspection")
            caption = _field(row, "caption", label, allow_none=True)
            records.append(
                _source_record(
                    _field(row, "id", label),
                    caption,
                    caption,
                    _field(row, "file", label),
                    _required(inspection, "visual_review", f"{label}.finalInspection"),
                    label,
                )
            )
        return records

    if slug == "chat-coverage":
        records = []
        for bucket in ("outputs", "reused"):
            for index, raw in enumerate(_list(data, bucket, slug)):
                row = _object(raw, f"{slug}.{bucket}[{index}]")
                records.append(
                    _source_record(
                        _field(row, "id", f"{slug}.{bucket}[{index}]"),
                        _field(row, "caption", f"{slug}.{bucket}[{index}]", allow_none=True),
                        _field(row, "intent", f"{slug}.{bucket}[{index}]"),
                        _field(row, "file", f"{slug}.{bucket}[{index}]"),
                        _required(row, "review", f"{slug}.{bucket}[{index}]"),
                        f"{slug}.{bucket}[{index}]",
                    )
                )
        return records

    if slug == "pose-decomposition":
        rows = _list(data, "outputs", slug)
        return [
            _source_record(
                _field(row, "id", f"{slug}.outputs[{index}]"),
                _field(row, "caption", f"{slug}.outputs[{index}]", allow_none=True),
                _field(row, "intent", f"{slug}.outputs[{index}]"),
                _field(row, "file", f"{slug}.outputs[{index}]"),
                _required(row, "review", f"{slug}.outputs[{index}]"),
                f"{slug}.outputs[{index}]",
            )
            for index, raw in enumerate(rows)
            for row in [_object(raw, f"{slug}.outputs[{index}]")]
        ]

    if slug == "emotion-five":
        rows = _list(data, "records", slug)
        return [
            _source_record(
                _field(row, "id", f"{slug}.records[{index}]"),
                _field(row, "caption", f"{slug}.records[{index}]", allow_none=True),
                _field(row, "emotion", f"{slug}.records[{index}]"),
                _field(row, "selected_file", f"{slug}.records[{index}]"),
                _required(row, "review", f"{slug}.records[{index}]"),
                f"{slug}.records[{index}]",
            )
            for index, raw in enumerate(rows)
            for row in [_object(raw, f"{slug}.records[{index}]")]
        ]

    if slug == "custom-caption-layout":
        rows = _list(data, "items", slug)
        records = []
        for index, raw in enumerate(rows):
            row = _object(raw, f"{slug}.items[{index}]")
            name = _field(row, "name", f"{slug}.items[{index}]")
            intent = next(
                (value for prefix, value in CUSTOM_INTENTS.items() if name.startswith(prefix)),
                "",
            )
            records.append(
                _source_record(
                    _field(row, "key", f"{slug}.items[{index}]"),
                    _field(row, "caption", f"{slug}.items[{index}]", allow_none=True),
                    intent,
                    _field(row, "output", f"{slug}.items[{index}]"),
                    _required(row, "visual_review", f"{slug}.items[{index}]"),
                    f"{slug}.items[{index}]",
                    "无字底图" if name.endswith("-base") else "带字表情",
                )
            )
        return records

    if slug == "ten-reactions":
        entries = [_object(row, f"{slug}.entries[{index}]") for index, row in enumerate(_list(data, "entries", slug))]
        records = []
        for index, raw in enumerate(_list(data, "numeric_inspection", slug)):
            inspection = _object(raw, f"{slug}.numeric_inspection[{index}]")
            filename = _field(inspection, "file", f"{slug}.numeric_inspection[{index}]")
            matches = [
                row
                for row in entries
                if _same_filename(_field(row, "output", f"{slug}.entries"), filename, f"{slug}.entries.output")
            ]
            if not matches:
                raise ValueError(f"{slug} has no entry matching selected file {filename}")
            row = matches[-1]
            records.append(
                _source_record(
                    _field(row, "id", f"{slug}.entries"),
                    _field(row, "caption", f"{slug}.entries", allow_none=True),
                    "",
                    filename,
                    _required(row, "review", f"{slug}.entries"),
                    f"{slug}.numeric_inspection[{index}]",
                )
            )
        return records

    if slug == "extended-reaction-library":
        rows = _list(data, "items", slug)
        records = []
        for index, raw in enumerate(rows):
            row = _object(raw, f"{slug}.items[{index}]")
            output = _object(row.get("output"), f"{slug}.items[{index}].output")
            records.append(
                _source_record(
                    _field(row, "id", f"{slug}.items[{index}]"),
                    _field(row, "caption", f"{slug}.items[{index}]", allow_none=True),
                    _field(row, "purpose", f"{slug}.items[{index}]"),
                    _field(output, "path", f"{slug}.items[{index}].output"),
                    _required(row, "review", f"{slug}.items[{index}]"),
                    f"{slug}.items[{index}]",
                )
            )
        return records

    if slug == "soft-six":
        rows = _list(data, "records", slug)
        records = []
        for index, raw in enumerate(rows):
            row = _object(raw, f"{slug}.records[{index}]")
            inspection = _object(row.get("file_inspection"), f"{slug}.records[{index}].file_inspection")
            records.append(
                _source_record(
                    _field(row, "id", f"{slug}.records[{index}]"),
                    _field(row, "caption", f"{slug}.records[{index}]", allow_none=True),
                    "",
                    _field(inspection, "file", f"{slug}.records[{index}].file_inspection"),
                    _required(row, "visual_review", f"{slug}.records[{index}]"),
                    f"{slug}.records[{index}]",
                )
            )
        return records

    if slug == "nine-reaction-sheet":
        rows = _list(data, "outputs", slug)
        return [
            _source_record(
                _field(row, "id", f"{slug}.outputs[{index}]"),
                _field(row, "caption", f"{slug}.outputs[{index}]", allow_none=True),
                _field(row, "intent", f"{slug}.outputs[{index}]"),
                _field(row, "file", f"{slug}.outputs[{index}]"),
                _required(row, "review", f"{slug}.outputs[{index}]"),
                f"{slug}.outputs[{index}]",
            )
            for index, raw in enumerate(rows)
            for row in [_object(raw, f"{slug}.outputs[{index}]")]
        ]

    if slug == "seven-poses":
        rows = _list(data, "artifacts", slug)
        return [
            _source_record(
                _field(row, "id", f"{slug}.artifacts[{index}]"),
                _field(row, "caption", f"{slug}.artifacts[{index}]", allow_none=True),
                _field(row, "name", f"{slug}.artifacts[{index}]"),
                _field(row, "file", f"{slug}.artifacts[{index}]"),
                _required(row, "review", f"{slug}.artifacts[{index}]"),
                f"{slug}.artifacts[{index}]",
            )
            for index, raw in enumerate(rows)
            for row in [_object(raw, f"{slug}.artifacts[{index}]")]
        ]

    if slug == "treatment-expression-family":
        rows = _list(data, "assets", slug)
        records = []
        for index, raw in enumerate(rows):
            row = _object(raw, f"{slug}.assets[{index}]")
            treatment = _field(row, "treatment", f"{slug}.assets[{index}]")
            records.append(
                _source_record(
                    _field(row, "id", f"{slug}.assets[{index}]"),
                    row.get("caption"),
                    _field(row, "intent", f"{slug}.assets[{index}]"),
                    _field(row, "path", f"{slug}.assets[{index}]"),
                    _required(row, "review", f"{slug}.assets[{index}]"),
                    f"{slug}.assets[{index}]",
                    FAMILY_KIND_LABELS.get(treatment, treatment),
                )
            )
        return records

    raise ValueError(f"Unsupported generated template id: {slug}")


def _asset_path(value: object, slug: str) -> tuple[str, Path]:
    raw = _text(value, "generated asset path")
    if not raw.strip():
        raise ValueError("Generated asset paths must not be empty")
    path = Path(raw)
    if path.is_absolute():
        try:
            relative = PurePosixPath(path.resolve().relative_to(SKILL.resolve()).as_posix())
        except ValueError as exc:
            raise ValueError(f"Generated asset path escapes the skill directory: {raw}") from exc
    else:
        normalized = raw.replace("\\", "/")
        relative_input = PurePosixPath(normalized)
        if relative_input.is_absolute() or any(part in {"", ".", ".."} for part in relative_input.parts):
            raise ValueError(f"Invalid generated asset path: {raw}")
        if relative_input.parts[:2] == ("assets", "generated"):
            relative = relative_input
        else:
            relative = PurePosixPath("assets", "generated", slug, *relative_input.parts)
    if len(relative.parts) < 3 or relative.parts[:2] != ("assets", "generated"):
        raise ValueError(f"Generated asset path must stay under assets/generated: {raw}")
    target = (SKILL / Path(*relative.parts)).resolve()
    try:
        target.relative_to(SKILL.resolve())
    except ValueError as exc:
        raise ValueError(f"Generated asset path escapes the skill directory: {raw}") from exc
    return relative.as_posix(), target


def _existing_asset(value: object, slug: str) -> str | None:
    relative, target = _asset_path(value, slug)
    return relative if target.is_file() else None


def _preview(slug: str) -> str | None:
    candidates = ["preview.png"]
    if slug == "custom-caption-layout":
        candidates.append("review-light-dark-128-384.png")
    if slug == "treatment-expression-family":
        candidates.append("preview-F.png")
    for name in candidates:
        found = _existing_asset(name, slug)
        if found:
            return found
    return None


def _source_notes(data: dict, slug: str) -> list[str]:
    notes = []
    for key in NOTE_FIELDS:
        if key not in data:
            continue
        value = data[key]
        if isinstance(value, str):
            parts = [value.strip()] if value.strip() else []
        elif isinstance(value, (list, dict)):
            parts = _flatten_strings(value, f"{slug}.{key}")
        else:
            raise ValueError(f"{slug}.{key} has an unsupported shape")
        notes.extend(parts)
    return list(dict.fromkeys(notes))


def _blocker_notes(data: dict, slug: str, linked_ids: set[str]) -> list[str]:
    if "generation_blockers" not in data:
        return []
    blockers = _list(data, "generation_blockers", slug)
    notes = []
    for index, raw in enumerate(blockers):
        row = _object(raw, f"{slug}.generation_blockers[{index}]")
        blocker_id = _field(row, "id", f"{slug}.generation_blockers[{index}]")
        status = _field(row, "status", f"{slug}.generation_blockers[{index}]")
        if blocker_id not in linked_ids:
            notes.append(f"生成阻塞项 {blocker_id}：{status}")
    return notes


def _collect_template(slug: str, expected: int) -> tuple[dict, str]:
    folder = GENERATED / slug
    source = folder / "production.json"
    data = None
    if folder.is_dir() and source.is_file():
        data = _object(json.loads(source.read_text(encoding="utf-8")), f"{slug}.production.json")

    raw_records = _selected_records(slug, data) if data is not None else []
    images = []
    seen_ids = set()
    duplicates = []
    missing_files = []
    for index, raw in enumerate(raw_records):
        image_id = _text(raw.get("id"), f"{slug}.images[{index}].id")
        if not image_id.strip():
            raise ValueError(f"{slug}.images[{index}].id must not be empty")
        relative, target = _asset_path(raw.get("file"), slug)
        if not target.is_file():
            missing_files.append(relative)
            continue
        if image_id in seen_ids:
            duplicates.append(image_id)
            continue
        seen_ids.add(image_id)
        image = {
            "id": image_id,
            "caption": _text(raw.get("caption"), f"{slug}.{image_id}.caption", allow_none=True),
            "intent": _text(raw.get("intent"), f"{slug}.{image_id}.intent", allow_none=True),
            "file": relative,
        }
        if raw.get("kind") is not None:
            image["kind"] = _text(raw["kind"], f"{slug}.{image_id}.kind")
        image["review"] = _text(raw.get("review"), f"{slug}.{image_id}.review")
        images.append(image)

    notes = [BASE_NOTE]
    if data is None:
        notes.append(f"生产记录尚未落盘；当前已链接 0/{expected} 项，素材清单待补充。")
    elif len(images) < expected:
        notes.append(f"当前已链接 {len(images)}/{expected} 项；缺项保留为空，未创建占位素材。")
    elif len(images) > expected:
        notes.append(f"当前已链接 {len(images)} 项，高于参考数量 {expected}；保留生产记录中的实际选择。")
    if missing_files:
        notes.append("生产记录引用但当前不存在的文件已跳过：" + "、".join(dict.fromkeys(missing_files)))
    if duplicates:
        notes.append("重复素材 ID 已去重：" + "、".join(dict.fromkeys(duplicates)))
    if data is not None:
        notes.extend(_source_notes(data, slug))
        notes.extend(_blocker_notes(data, slug, seen_ids))

    record = {
        "id": slug,
        "count": len(images),
        "preview": _preview(slug),
        "images": images,
        "notes": "；".join(dict.fromkeys(note for note in notes if note)),
    }
    production_date = ""
    if data is not None:
        for key in ("production_date", "date", "created"):
            value = data.get(key)
            if isinstance(value, str) and value.strip():
                production_date = value.strip()
                break
    return record, production_date


def build_catalog() -> dict:
    templates = []
    dates = []
    for slug, expected in EXPECTED_COUNTS.items():
        record, production_date = _collect_template(slug, expected)
        templates.append(record)
        if production_date:
            dates.append(production_date)
    archive = _existing_asset("assets/generated/oneirloom-stickers-20261003.zip", "")
    image_count = sum(len(record["images"]) for record in templates)
    return {
        "date": max(dates) if dates else "",
        "image_count": image_count,
        "templates": templates,
        **({"archive": archive} if archive else {}),
    }


def build() -> Path:
    catalog = build_catalog()
    CATALOG_PATH.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return CATALOG_PATH


if __name__ == "__main__":
    print(build().relative_to(ROOT).as_posix())
