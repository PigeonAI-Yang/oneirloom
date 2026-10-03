from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
from pathlib import Path, PurePosixPath
from urllib.parse import quote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills" / "oneirloom-expression-stickers"
TEMPLATE_DIR = SKILL / "templates"
BROWSER_PATH = TEMPLATE_DIR / "browse.html"
GENERATED_CATALOG = SKILL / "assets" / "generated" / "catalog.json"

TEMPLATES = [
    {
        "id": "identity-acting-system",
        "title": "身份与动作库",
        "category": "身份与动作",
        "summary": "区分已认可的正面身份与不同动作记录。",
    },
    {
        "id": "daily-sixteen",
        "title": "日常十六式",
        "category": "聊天回应",
        "summary": "规划十六种日常对话回应，数量属于此模板的选择。",
    },
    {
        "id": "chat-coverage",
        "title": "聊天回复覆盖",
        "category": "聊天回应",
        "summary": "按短语、情绪和情境组织可选回复。",
    },
    {
        "id": "pose-decomposition",
        "title": "动作姿势拆解",
        "category": "姿势设计",
        "summary": "将意图落实到身体、触角、手臂、月网和文字关系。",
    },
    {
        "id": "emotion-five",
        "title": "五种情绪练习",
        "category": "情绪设计",
        "summary": "用完整正面姿态表现五种情绪组合。",
    },
    {
        "id": "eight-slot-workspace",
        "title": "八格空白工作表",
        "category": "绘制工作区",
        "summary": "空白绘制工作表；8 个动作待绘制。",
    },
    {
        "id": "source-export-workspace",
        "title": "源稿与导出工作区",
        "category": "制作流程",
        "summary": "整理可编辑源稿及按选定平台导出的工作流程。",
    },
    {
        "id": "custom-caption-layout",
        "title": "自定义文字留白",
        "category": "文字布局",
        "summary": "为固定文字或可编辑文字规划画面留白。",
    },
    {
        "id": "ten-reactions",
        "title": "十种日常回应",
        "category": "回应清单",
        "summary": "以十种常见意图整理动作与文字候选。",
    },
    {
        "id": "extended-reaction-library",
        "title": "扩展回应资料库",
        "category": "回应清单",
        "summary": "从沟通、情绪与织梦动作中选择回应。",
    },
    {
        "id": "soft-six",
        "title": "温柔情绪六款",
        "category": "情绪设计",
        "summary": "比较六种柔和情绪组合的姿态方案。",
    },
    {
        "id": "nine-reaction-sheet",
        "title": "九宫格动作预览",
        "category": "概念预览",
        "summary": "用九格概念预览比较不同意图，不代表九张成品。",
    },
    {
        "id": "seven-poses",
        "title": "七种原创姿势",
        "category": "姿势设计",
        "summary": "从中性基准开始规划六种额外姿势。",
    },
    {
        "id": "treatment-expression-family",
        "title": "表情与画风对照",
        "category": "画风比较",
        "summary": "固定身份和动作，对照五种绘制处理。",
    },
]

PROFILE_TITLES = {
    "LINE static stickers": ("line-static", "LINE 静态贴图"),
    "Telegram static stickers": ("telegram-static", "Telegram 静态贴图"),
    "WhatsApp Android static stickers": ("whatsapp-android-static", "WhatsApp 安卓静态贴图"),
    "Discord server static stickers": ("discord-server-static", "Discord 服务器静态贴图"),
    "WeChat static stickers, pending official requirements": ("wechat-static", "微信静态贴图（规范待核实）"),
}

REFERENCES = {
    "brand": SKILL / "references" / "oneirloom-brand.md",
    "platform": SKILL / "references" / "platform-profiles.md",
    "coverage": SKILL / "references" / "research-coverage.md",
}


def _safe_json(value: object) -> str:
    encoded = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    return (
        encoded.replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def _source_dir_from_browser(source_dir: Path) -> str:
    relative = source_dir.relative_to(SKILL).as_posix()
    return posixpath.relpath(relative, "templates")


def _rewrite_url(destination: str, source_dir: Path) -> str:
    parts = urlsplit(destination)
    if parts.scheme or parts.netloc or not parts.path:
        return destination
    if parts.path.startswith("/"):
        return destination
    relative_base = _source_dir_from_browser(source_dir)
    rebased = posixpath.normpath(posixpath.join(relative_base, parts.path.replace("\\", "/")))
    rebased = quote(rebased, safe="/:@-._~!$&'()*+,;=%")
    return urlunsplit(("", "", rebased, parts.query, parts.fragment))


def _markdown_engine():
    try:
        from markdown_it import MarkdownIt
    except ImportError:
        return None
    return MarkdownIt("default", {"html": False, "linkify": False}).enable("table")


def _fallback_inline(text: str, source_dir: Path) -> str:
    code_char = chr(96)
    token_pattern = re.compile(
        r"(!?\[[^\]]*\]\([^)]*\)|" + re.escape(code_char) + r"[^" + re.escape(code_char) + r"]+" + re.escape(code_char) + r"|\*\*.+?\*\*|__.+?__|~~.+?~~|\*[^*]+\*)"
    )
    output = []
    position = 0
    for match in token_pattern.finditer(text):
        output.append(html.escape(text[position:match.start()]))
        token = match.group(0)
        if token.startswith("![") or token.startswith("["):
            image_match = re.fullmatch(r"(!?)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)", token)
            if image_match:
                is_image, label, destination, title = image_match.groups()
                destination = _rewrite_url(destination, source_dir)
                safe_destination = html.escape(destination, quote=True)
                safe_title = f' title="{html.escape(title, quote=True)}"' if title else ""
                if is_image:
                    output.append(f'<img src="{safe_destination}" alt="{html.escape(label, quote=True)}"{safe_title}>')
                else:
                    output.append(f'<a href="{safe_destination}"{safe_title}>{html.escape(label)}</a>')
            else:
                output.append(html.escape(token))
        elif token.startswith(code_char):
            output.append(f"<code>{html.escape(token[1:-1])}</code>")
        elif token.startswith("**") or token.startswith("__"):
            output.append(f"<strong>{html.escape(token[2:-2])}</strong>")
        elif token.startswith("~~"):
            output.append(f"<del>{html.escape(token[2:-2])}</del>")
        else:
            output.append(f"<em>{html.escape(token[1:-1])}</em>")
        position = match.end()
    output.append(html.escape(text[position:]))
    return "".join(output)


def _fallback_render(markdown_text: str, source_dir: Path) -> str:
    lines = markdown_text.replace("\r\n", "\n").split("\n")
    rendered = []
    index = 0
    fence = chr(96) * 3

    def is_table_start(position: int) -> bool:
        if position + 1 >= len(lines) or "|" not in lines[position]:
            return False
        return bool(re.fullmatch(r"\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*", lines[position + 1]))

    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith(fence):
            language = line[len(fence):].strip().split(maxsplit=1)[0] if line[len(fence):].strip() else ""
            index += 1
            code = []
            while index < len(lines) and not lines[index].startswith(fence):
                code.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            language_class = f' class="language-{html.escape(language, quote=True)}"' if language else ""
            rendered.append(f"<pre><code{language_class}>{html.escape(chr(10).join(code))}</code></pre>")
            continue
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if heading:
            level = len(heading.group(1))
            rendered.append(f"<h{level}>{_fallback_inline(heading.group(2), source_dir)}</h{level}>")
            index += 1
            continue
        if is_table_start(index):
            headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
            index += 2
            rows = []
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")])
                index += 1
            head_html = "".join(f"<th>{_fallback_inline(cell, source_dir)}</th>" for cell in headers)
            body_html = "".join(
                "<tr>" + "".join(f"<td>{_fallback_inline(cell, source_dir)}</td>" for cell in row) + "</tr>"
                for row in rows
            )
            rendered.append(f"<table><thead><tr>{head_html}</tr></thead><tbody>{body_html}</tbody></table>")
            continue
        if re.match(r"^\s*(?:[-+*]|\d+\.)\s+", line):
            ordered = bool(re.match(r"^\s*\d+\.\s+", line))
            tag = "ol" if ordered else "ul"
            items = []
            while index < len(lines) and re.match(r"^\s*(?:[-+*]|\d+\.)\s+", lines[index]):
                item = re.sub(r"^\s*(?:[-+*]|\d+\.)\s+", "", lines[index]).strip()
                items.append(f"<li>{_fallback_inline(item, source_dir)}</li>")
                index += 1
            rendered.append(f"<{tag}>{''.join(items)}</{tag}>")
            continue
        if line.startswith(">"):
            quote_lines = []
            while index < len(lines) and lines[index].startswith(">"):
                quote_lines.append(re.sub(r"^>\s?", "", lines[index]))
                index += 1
            rendered.append(f"<blockquote><p>{_fallback_inline(' '.join(quote_lines), source_dir)}</p></blockquote>")
            continue
        paragraph = [line.strip()]
        index += 1
        while index < len(lines) and lines[index].strip() and not lines[index].startswith(fence):
            if re.match(r"^(#{1,6})\s+", lines[index]) or is_table_start(index) or re.match(r"^\s*(?:[-+*]|\d+\.)\s+", lines[index]):
                break
            paragraph.append(lines[index].strip())
            index += 1
        rendered.append(f"<p>{_fallback_inline(' '.join(paragraph), source_dir)}</p>")
    return "\n".join(rendered)


def render_markdown(markdown_text: str, source_dir: Path, engine) -> str:
    if engine is None:
        return _fallback_render(markdown_text, source_dir)
    tokens = engine.parse(markdown_text)
    for token in tokens:
        for candidate in (token, *(token.children or [])):
            if candidate.type == "link_open" and candidate.attrGet("href"):
                candidate.attrSet("href", _rewrite_url(candidate.attrGet("href"), source_dir))
            elif candidate.type == "image" and candidate.attrGet("src"):
                candidate.attrSet("src", _rewrite_url(candidate.attrGet("src"), source_dir))
    return engine.renderer.render(tokens, engine.options, {})


def extract_source_links(markdown_text: str) -> list[dict[str, str]]:
    seen = set()
    links = []
    pattern = re.compile(r"(?<!!)\[([^\]]+)\]\((https?://[^)\s]+)(?:\s+\"[^\"]*\")?\)")
    for label, destination in pattern.findall(markdown_text):
        if destination not in seen:
            seen.add(destination)
            links.append({"label": label, "url": destination})
    return links


def extract_first_prompt(markdown_text: str) -> str:
    fence = chr(96) * 3
    pattern = re.compile(r"(?ms)^" + re.escape(fence) + r"text[ \t]*\n(.*?)^" + re.escape(fence) + r"[ \t]*$")
    match = pattern.search(markdown_text)
    if not match:
        raise ValueError("Template is missing its first English text prompt")
    return match.group(1)


def split_platform_profiles(markdown_text: str) -> tuple[str, list[dict[str, str]]]:
    matches = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", markdown_text))
    if len(matches) != 5:
        raise ValueError(f"Expected five platform profile headings, found {len(matches)}")
    intro = markdown_text[:matches[0].start()]
    profiles = []
    for index, match in enumerate(matches):
        heading = match.group(1)
        if heading not in PROFILE_TITLES:
            raise ValueError(f"Unknown platform profile heading: {heading}")
        key, display_title = PROFILE_TITLES[heading]
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown_text)
        profiles.append(
            {
                "id": key,
                "title": display_title,
                "sourceTitle": heading,
                "markdown": markdown_text[match.start():end].strip(),
            }
        )
    return intro, profiles


def read_source(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"Required source is missing: {path}")
    return path.read_text(encoding="utf-8")


def _generated_asset_url(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Generated asset paths must be non-empty strings")
    normalized = value.strip().replace("\\", "/")
    parts = normalized.split("/")
    parsed = urlsplit(normalized)
    if (
        parsed.scheme
        or parsed.netloc
        or parsed.query
        or parsed.fragment
        or normalized.startswith("/")
        or len(parts) < 3
        or parts[:2] != ["assets", "generated"]
        or any(part in {"", ".", ".."} for part in parts)
    ):
        raise ValueError(f"Generated asset path must stay under assets/generated: {value}")
    source = (SKILL / PurePosixPath(normalized)).resolve()
    try:
        source.relative_to(SKILL.resolve())
    except ValueError as exc:
        raise ValueError(f"Generated asset path escapes the skill directory: {value}") from exc
    if not source.is_file():
        raise FileNotFoundError(f"Generated asset is missing: {source}")
    browser_path = posixpath.relpath(PurePosixPath(normalized).as_posix(), "templates")
    return quote(browser_path, safe="/-._~")


def _prepare_generated_catalog(catalog: object) -> tuple[dict | None, dict[str, dict]]:
    if catalog is None:
        if not GENERATED_CATALOG.is_file():
            return None, {}
        catalog = json.loads(GENERATED_CATALOG.read_text(encoding="utf-8"))
    if not isinstance(catalog, dict):
        raise ValueError("Generated catalog must be a JSON object")
    raw_templates = catalog.get("templates", [])
    if not isinstance(raw_templates, list):
        raise ValueError("Generated catalog templates must be a list")

    known_ids = {item["id"] for item in TEMPLATES}
    prepared_templates: dict[str, dict] = {}
    image_total = 0
    for record in raw_templates:
        if not isinstance(record, dict):
            raise ValueError("Generated catalog template records must be objects")
        template_id = record.get("id")
        if template_id not in known_ids:
            raise ValueError(f"Generated catalog has an unknown template id: {template_id}")
        if template_id in prepared_templates:
            raise ValueError(f"Generated catalog repeats template id: {template_id}")
        raw_images = record.get("images", [])
        if not isinstance(raw_images, list):
            raise ValueError(f"Generated images must be a list for {template_id}")
        images = []
        image_ids = set()
        for raw_image in raw_images:
            if not isinstance(raw_image, dict):
                raise ValueError(f"Generated image records must be objects for {template_id}")
            image_id = raw_image.get("id")
            if not isinstance(image_id, str) or not image_id.strip():
                raise ValueError(f"Generated images need a non-empty id for {template_id}")
            if image_id in image_ids:
                raise ValueError(f"Generated images repeat id {image_id} for {template_id}")
            image_ids.add(image_id)
            caption = raw_image.get("caption", "")
            intent = raw_image.get("intent", "")
            if not isinstance(caption, str) or not isinstance(intent, str):
                raise ValueError(f"Generated captions and intents must be strings for {template_id}/{image_id}")
            image = {
                "id": image_id,
                "caption": caption,
                "intent": intent,
                "file": _generated_asset_url(raw_image.get("file")),
            }
            kind = raw_image.get("kind")
            review = raw_image.get("review")
            if kind is not None:
                if not isinstance(kind, str):
                    raise ValueError(f"Generated image kind must be a string for {template_id}/{image_id}")
                image["kind"] = kind
            if review is not None:
                if not isinstance(review, str):
                    raise ValueError(f"Generated image review must be a string for {template_id}/{image_id}")
                image["review"] = review
            images.append(image)
        image_total += len(images)

        preview = record.get("preview")
        notes = record.get("notes")
        count = record.get("count")
        if count is not None and (not isinstance(count, int) or isinstance(count, bool) or count < 0):
            raise ValueError(f"Generated image count must be a non-negative integer for {template_id}")
        if notes is not None and not isinstance(notes, str):
            raise ValueError(f"Generated notes must be a string for {template_id}")
        prepared = {
            "id": template_id,
            "count": count if count is not None else len(images),
            "images": images,
            "preview": _generated_asset_url(preview) if preview else None,
            "notes": notes or "",
        }
        prepared_templates[template_id] = prepared

    date = catalog.get("date", "")
    declared_count = catalog.get("image_count")
    if date is not None and not isinstance(date, str):
        raise ValueError("Generated catalog date must be a string")
    if declared_count is not None and (
        not isinstance(declared_count, int) or isinstance(declared_count, bool) or declared_count < 0
    ):
        raise ValueError("Generated catalog image_count must be a non-negative integer")
    archive = catalog.get("archive")
    metadata = {
        "date": date or "",
        "image_count": declared_count if declared_count is not None else image_total,
        "archive": _generated_asset_url(archive) if archive else None,
    }
    return metadata, prepared_templates


def build_data(engine, generated_catalog=None) -> dict:
    generated_metadata, generated_templates = _prepare_generated_catalog(generated_catalog)
    templates = []
    for metadata in TEMPLATES:
        source_path = TEMPLATE_DIR / metadata["id"] / "template.md"
        markdown_text = read_source(source_path)
        source_dir = source_path.parent
        templates.append(
            {
                **metadata,
                "markdown": markdown_text,
                "html": render_markdown(markdown_text, source_dir, engine),
                "sourceFile": f'{metadata["id"]}/template.md',
                "sources": extract_source_links(markdown_text),
                "copyText": extract_first_prompt(markdown_text),
                "generated": generated_templates.get(metadata["id"]),
            }
        )

    reference_data = {}
    for key, path in REFERENCES.items():
        markdown_text = read_source(path)
        reference_data[key] = {
            "markdown": markdown_text,
            "html": render_markdown(markdown_text, path.parent, engine),
            "sourceFile": "../references/" + path.name,
        }

    platform_markdown = reference_data["platform"]["markdown"]
    platform_intro, raw_profiles = split_platform_profiles(platform_markdown)
    profiles = []
    for profile in raw_profiles:
        profiles.append(
            {
                **profile,
                "html": render_markdown(profile["markdown"], REFERENCES["platform"].parent, engine),
            }
        )
    reference_data["platform"]["introHtml"] = render_markdown(
        platform_intro, REFERENCES["platform"].parent, engine
    )
    reference_data["platform"]["profiles"] = profiles
    return {
        "templates": templates,
        "references": reference_data,
        "generatedCatalog": generated_metadata,
        "markdownEngine": "markdown-it-py" if engine else "stdlib fallback",
    }


HTML_TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>__PAGE_TITLE__</title>
  <style>
    :root {
      color-scheme: light;
      --paper: #f7f5f0;
      --paper-raised: #fffefa;
      --ink: #25244c;
      --muted: #616176;
      --periwinkle: #9994e8;
      --gold: #ffd873;
      --sky: #71b9e8;
      --line: #d9d5ca;
      --soft-blue: #edf4f9;
      --shadow: 0 12px 34px rgba(37, 36, 76, .08);
    }
    * { box-sizing: border-box; }
    html { background: var(--paper); }
    body { margin: 0; min-width: 320px; color: var(--ink); background: var(--paper); font: 16px/1.58 "Segoe UI", "Microsoft YaHei UI", "PingFang SC", sans-serif; }
    button, select { color: inherit; font: inherit; }
    button { min-height: 42px; border: 1px solid var(--line); border-radius: 999px; padding: 0 15px; background: var(--paper-raised); cursor: pointer; }
    button:hover, select:hover { border-color: var(--periwinkle); }
    button:focus-visible, select:focus-visible, a:focus-visible { outline: 3px solid rgba(113, 185, 232, .72); outline-offset: 2px; }
    a { color: #3c64a0; overflow-wrap: anywhere; }
    .shell { width: min(1160px, calc(100% - 40px)); margin: 0 auto; }
    .masthead { padding: 27px 0 21px; border-bottom: 1px solid var(--line); }
    .brand-row { display: flex; justify-content: space-between; align-items: center; gap: 24px; }
    .brand-lockup { display: block; width: min(295px, 55vw); height: auto; }
    .brand-copy { margin: 15px 0 0; color: var(--muted); }
    .identity-reference { display: grid; grid-template-columns: 74px minmax(0, 1fr); align-items: center; gap: 12px; max-width: 330px; margin: 0; padding: 9px 13px 9px 9px; border: 1px solid var(--line); border-radius: 14px; background: var(--paper-raised); }
    .identity-reference img { width: 74px; height: 74px; object-fit: contain; border-radius: 9px; background: white; }
    .identity-reference strong { display: block; font-size: 13px; line-height: 1.4; }
    .identity-reference span { display: block; margin-top: 3px; color: var(--muted); font-size: 12px; line-height: 1.4; }
    .eyebrow { color: #605bc0; font-size: 11px; font-weight: 750; letter-spacing: .13em; text-transform: uppercase; }
    h1 { margin: 5px 0 0; font-size: clamp(25px, 4vw, 38px); line-height: 1.18; letter-spacing: -.035em; }
    .topbar { position: sticky; z-index: 3; top: 0; padding: 10px 0; border-bottom: 1px solid rgba(217, 213, 202, .9); background: rgba(247, 245, 240, .95); backdrop-filter: blur(12px); }
    .nav-tabs { display: flex; gap: 8px; overflow-x: auto; padding: 1px 2px 3px; scrollbar-width: thin; }
    .nav-tabs button { flex: 0 0 auto; min-height: 38px; padding: 0 15px; font-size: 14px; }
    .nav-tabs button[aria-pressed="true"] { border-color: var(--ink); color: white; background: var(--ink); }
    main { padding: 25px 0 64px; }
    .view[hidden] { display: none; }
    .view-heading { display: flex; flex-wrap: wrap; align-items: end; justify-content: space-between; gap: 10px 22px; margin-bottom: 18px; }
    .view-heading h2 { margin: 0; font-size: 25px; line-height: 1.25; }
    .view-heading p { max-width: 680px; margin: 5px 0 0; color: var(--muted); }
    .chip { display: inline-flex; align-items: center; min-height: 28px; border: 1px solid rgba(153, 148, 232, .55); border-radius: 999px; padding: 2px 10px; color: #4d499b; background: rgba(153, 148, 232, .13); font-size: 12px; font-weight: 700; }
    .picker { display: grid; grid-template-columns: minmax(210px, 1fr) auto auto auto; align-items: end; gap: 10px; margin: 17px 0; padding: 14px; border: 1px solid var(--line); border-radius: 15px; background: var(--paper-raised); box-shadow: var(--shadow); }
    .field label { display: block; margin: 0 0 5px; color: var(--muted); font-size: 12px; font-weight: 700; }
    select { width: 100%; min-width: 0; min-height: 42px; border: 1px solid var(--line); border-radius: 9px; padding: 0 35px 0 11px; background: white; }
    .position { min-width: 58px; padding-bottom: 10px; text-align: center; color: var(--muted); font-size: 12px; font-variant-numeric: tabular-nums; }
    .next-button { border-color: var(--ink); color: white; background: var(--ink); }
    .record-card { overflow: hidden; border: 1px solid var(--line); border-radius: 18px; background: var(--paper-raised); box-shadow: var(--shadow); }
    .record-header { padding: 21px 24px 18px; border-bottom: 1px solid var(--line); background: linear-gradient(115deg, rgba(153,148,232,.13), rgba(113,185,232,.12) 65%, rgba(255,216,115,.13)); }
    .record-topline { display: flex; flex-wrap: wrap; align-items: center; gap: 9px; }
    .record-header h3 { margin: 6px 0 2px; font-size: clamp(22px, 3vw, 30px); line-height: 1.25; }
    .record-header .english-title { margin: 0; color: var(--muted); font-size: 13px; }
    .record-summary { margin: 10px 0 0; max-width: 760px; }
    .source-row { display: flex; flex-wrap: wrap; align-items: center; gap: 9px 15px; margin-top: 12px; font-size: 13px; }
    .source-row a { text-decoration-thickness: 1px; text-underline-offset: 3px; }
    .source-links { display: flex; flex-wrap: wrap; gap: 6px 13px; }
    .copy-row { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 12px; margin-top: 13px; }
    .copy-row button { min-height: 38px; border-color: var(--ink); color: white; background: var(--ink); font-size: 13px; font-weight: 700; }
    .copy-status { color: var(--muted); font-size: 12px; }
    .preview-panel { display: none; padding: 17px 24px; border-bottom: 1px solid var(--line); background: var(--soft-blue); }
    .preview-panel[data-visible="true"] { display: grid; grid-template-columns: minmax(0, 400px) minmax(0, 1fr); align-items: center; gap: 17px 22px; }
    .preview-panel img { display: block; width: 100%; height: auto; border: 1px solid var(--line); background: white; }
    .preview-panel p { margin: 0 0 10px; }
    .download-link { display: inline-flex; align-items: center; min-height: 40px; border-radius: 999px; padding: 0 15px; color: var(--ink); background: var(--gold); font-size: 13px; font-weight: 750; text-decoration: none; }
    .generated-panel { padding: 18px 24px 21px; border-bottom: 1px solid var(--line); background: #f4f2fc; }
    .generated-heading { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 12px; }
    .generated-heading h4 { margin: 0; font-size: 18px; }
    .generated-intro, .generated-catalog-summary { margin: 4px 0 0; color: var(--muted); font-size: 13px; }
    .generated-archive-row { margin: 11px 0 0; }
    .generated-toolbar { display: grid; grid-template-columns: minmax(190px, 1fr) auto auto auto; align-items: end; gap: 9px; margin: 15px 0 12px; }
    .generated-toolbar .position { padding-bottom: 10px; }
    .generated-toolbar button { min-height: 40px; padding: 0 13px; font-size: 13px; }
    .generated-toolbar .next-button { border-color: var(--ink); color: white; background: var(--ink); }
    .generated-content[hidden], .generated-empty[hidden], .generated-catalog-summary[hidden], .generated-archive-row[hidden], .generated-kind-row[hidden], .generated-review-row[hidden], .generated-notes[hidden], .generated-contact-sheet[hidden] { display: none !important; }
    .generated-empty { margin: 15px 0 2px; border: 1px dashed #c5c1d8; border-radius: 12px; padding: 13px 15px; color: var(--muted); background: rgba(255,255,255,.65); }
    .generated-stage { display: grid; grid-template-columns: minmax(0, 1.08fr) minmax(0, .92fr); gap: 18px; align-items: stretch; }
    .generated-image-frame { display: grid; min-width: 0; min-height: 260px; place-items: center; overflow: hidden; border: 1px solid var(--line); border-radius: 12px; padding: 14px; background: #fffefa; transition: background-color .16s ease; }
    .generated-stage[data-background="dark"] .generated-image-frame { background: #292844; }
    .generated-image-frame img { display: block; width: 100%; max-height: 560px; object-fit: contain; }
    .generated-image-figure { min-width: 0; margin: 0; }
    .generated-image-figure figcaption { margin-top: 8px; color: var(--ink); font-weight: 750; overflow-wrap: anywhere; }
    .generated-details { min-width: 0; border: 1px solid var(--line); border-radius: 12px; padding: 16px; background: var(--paper-raised); }
    .generated-details p { margin: 0 0 12px; overflow-wrap: anywhere; }
    .generated-details p:last-child { margin-bottom: 0; }
    .generated-label { display: block; margin-bottom: 2px; color: var(--muted); font-size: 12px; font-weight: 700; }
    .generated-kind { margin-top: 2px; }
    .generated-review-row { border-top: 1px solid var(--line); padding-top: 10px; }
    .generated-notes { color: var(--muted); font-size: 13px; }
    .generated-background-control { display: flex; flex-wrap: wrap; align-items: center; gap: 7px; margin: 0 0 10px; }
    .generated-background-control span { color: var(--muted); font-size: 12px; font-weight: 700; }
    .generated-background-control button { min-height: 34px; padding: 0 11px; font-size: 12px; }
    .generated-background-control button[aria-pressed="true"] { border-color: var(--ink); color: white; background: var(--ink); }
    .generated-links { display: flex; flex-wrap: wrap; align-items: center; gap: 9px 14px; margin-top: 14px; font-size: 13px; }
    .generated-links a { overflow-wrap: anywhere; }
    .markdown-body { padding: 22px clamp(17px, 3.4vw, 36px) 34px; overflow-wrap: anywhere; }
    .markdown-body > :first-child { margin-top: 0; }
    .markdown-body h1 { margin: 1.35em 0 .42em; font-size: 1.8em; }
    .markdown-body h2 { margin: 1.55em 0 .45em; padding-bottom: .32em; border-bottom: 1px solid var(--line); font-size: 1.42em; }
    .markdown-body h3 { margin: 1.35em 0 .4em; font-size: 1.18em; }
    .markdown-body h4, .markdown-body h5, .markdown-body h6 { margin: 1.25em 0 .35em; }
    .markdown-body p { margin: .7em 0; }
    .markdown-body ul, .markdown-body ol { padding-left: 1.55em; }
    .markdown-body li + li { margin-top: .24em; }
    .markdown-body blockquote { margin: 1em 0; border-left: 3px solid var(--sky); padding: .2em 0 .2em 1em; color: var(--muted); }
    .markdown-body table { display: block; width: 100%; max-width: 100%; margin: 1em 0 1.3em; overflow-x: auto; border-collapse: collapse; font-size: .92em; }
    .markdown-body th, .markdown-body td { min-width: 120px; border: 1px solid var(--line); padding: 9px 11px; text-align: left; vertical-align: top; }
    .markdown-body th { background: rgba(153,148,232,.11); color: var(--ink); font-weight: 750; }
    .markdown-body tr:nth-child(even) td { background: rgba(237,244,249,.55); }
    .markdown-body pre { max-width: 100%; margin: 1em 0; overflow: auto; border: 1px solid #dcd9e6; border-radius: 10px; padding: 15px; color: #f5f4ff; background: #292844; white-space: pre; }
    .markdown-body pre code { color: inherit; background: transparent; }
    .markdown-body code { border-radius: 4px; padding: .1em .28em; color: #36336d; background: rgba(153,148,232,.14); font: .92em/1.5 Consolas, "Cascadia Code", monospace; overflow-wrap: anywhere; }
    .markdown-body img { display: block; max-width: min(100%, 700px); height: auto; margin: 1em auto; }
    .markdown-body hr { height: 1px; border: 0; background: var(--line); }
    .reference-toolbar { display: grid; grid-template-columns: minmax(220px, 1fr) auto; align-items: end; gap: 10px; margin: 16px 0; }
    .reference-intro { margin: 16px 0; border: 1px solid var(--line); border-radius: 14px; background: var(--paper-raised); }
    .reference-intro .markdown-body { padding-top: 17px; padding-bottom: 17px; }
    .profile-card { border: 1px solid var(--line); border-radius: 18px; background: var(--paper-raised); box-shadow: var(--shadow); }
    .profile-header { padding: 18px 22px; border-bottom: 1px solid var(--line); background: linear-gradient(115deg, rgba(153,148,232,.12), rgba(113,185,232,.12)); }
    .profile-header h3 { display: inline-block; margin: 0 10px 0 0; font-size: 22px; }
    .status-gap { border-color: #d3a332; color: #75530a; background: #fff2c9; }
    .status-row { margin-top: 9px; }
    .profile-body { padding: 3px 22px 20px; }
    .single-reference { border: 1px solid var(--line); border-radius: 18px; background: var(--paper-raised); box-shadow: var(--shadow); }
    .single-reference .markdown-body { padding-top: 21px; }
    .notice { margin: 14px 0 0; padding: 11px 14px; border-left: 3px solid var(--gold); border-radius: 8px; background: #fff8e3; font-size: 13px; }
    .footer { margin-top: 24px; color: var(--muted); font-size: 12px; text-align: center; }
    @media (max-width: 720px) {
      .shell { width: min(100% - 24px, 680px); }
      .masthead { padding-top: 17px; }
      .brand-row { align-items: flex-start; }
      .identity-reference { grid-template-columns: 58px minmax(0, 1fr); gap: 8px; max-width: 216px; padding: 7px; }
      .identity-reference img { width: 58px; height: 58px; }
      .identity-reference strong { font-size: 11px; }
      .identity-reference span { font-size: 10px; }
      .brand-copy { max-width: 600px; margin-top: 12px; font-size: 14px; }
      .picker { grid-template-columns: minmax(0, 1fr) auto auto; padding: 11px; gap: 8px; }
      .picker .field { grid-column: 1 / -1; }
      .picker .position { padding-bottom: 11px; }
      .picker button { padding: 0 12px; font-size: 13px; }
      .record-header { padding: 18px 17px 15px; }
      .preview-panel { padding: 14px 16px; }
      .preview-panel[data-visible="true"] { grid-template-columns: minmax(0, 1fr); }
      .preview-panel img { max-height: 300px; object-fit: contain; }
      .generated-panel { padding: 15px 16px 17px; }
      .generated-toolbar { grid-template-columns: minmax(0, 1fr) auto auto; }
      .generated-toolbar .field { grid-column: 1 / -1; }
      .generated-toolbar .position { padding-bottom: 10px; }
      .generated-toolbar button { padding: 0 10px; }
      .generated-stage { grid-template-columns: minmax(0, 1fr); }
      .generated-image-frame { min-height: 220px; }
      .reference-toolbar { grid-template-columns: minmax(0, 1fr) auto; }
      .record-card, .profile-card, .single-reference { border-radius: 14px; }
      .profile-header { padding: 16px; }
      .profile-body { padding: 2px 13px 14px; }
      .markdown-body { padding: 18px 15px 25px; font-size: 15px; }
      .markdown-body th, .markdown-body td { min-width: 112px; padding: 8px; }
    }
    @media (max-width: 390px) {
      .brand-row { flex-direction: column; align-items: flex-start; gap: 11px; }
      .brand-lockup { width: min(205px, 54vw); }
      .identity-reference { grid-template-columns: 52px minmax(0, 1fr); width: max-content; max-width: 100%; }
      .identity-reference img { width: 52px; height: 52px; }
      .view-heading h2 { font-size: 22px; }
      .reference-toolbar { grid-template-columns: minmax(0, 1fr); }
      .reference-toolbar .position { padding: 0; text-align: left; }
    }
  </style>
</head>
<body>
  <header class="masthead">
    <div class="shell">
      <div class="brand-row">
        <div>
__BRAND_LOCKUP__
          <div class="brand-copy">
            <span class="eyebrow">__HEADER_EYEBROW__</span>
            <h1>表情贴图模板库</h1>
            <p>__HEADER_SUMMARY__</p>
          </div>
        </div>
        __IDENTITY_REFERENCE__
      </div>
    </div>
  </header>
  <div class="topbar">
    <nav class="shell nav-tabs" aria-label="资料视图">
      <button type="button" data-view-button="templates" aria-pressed="true">模板库</button>
      <button type="button" data-view-button="platform" aria-pressed="false">平台规范</button>
      <button type="button" data-view-button="coverage" aria-pressed="false">来源覆盖</button>
      <button type="button" data-view-button="brand" aria-pressed="false">品牌指南</button>
    </nav>
  </div>
  <main class="shell">
    <section class="view" id="view-templates">
      <div class="view-heading">
        <div>
          <h2>一次浏览一款模板</h2>
          <p>选择模板查看完整原文；提示词仍保留英文，链接指向本地原稿与记录的来源。</p>
        </div>
      </div>
      <div class="picker" aria-label="模板选择器">
        <div class="field">
          <label for="template-select">选择模板</label>
          <select id="template-select"></select>
        </div>
        <div class="position" id="template-position" aria-live="polite"></div>
        <button type="button" id="template-previous">上一款</button>
        <button type="button" class="next-button" id="template-next">下一款</button>
      </div>
      <article class="record-card">
        <header class="record-header">
          <div class="record-topline">
            <span class="chip" id="template-category"></span>
            <span class="eyebrow" id="template-id"></span>
          </div>
          <h3 id="template-title"></h3>
          <p class="english-title" id="template-source-title"></p>
          <p class="record-summary" id="template-summary"></p>
          <div class="source-row">
            <a id="template-source-file" href="#">打开原始 Markdown</a>
            <span>原始来源链接：</span>
            <span class="source-links" id="template-source-links"></span>
          </div>
          <div class="copy-row">
            <button type="button" id="copy-prompt">复制首段英文提示词</button>
            <span class="copy-status" id="copy-status" aria-live="polite"></span>
          </div>
        </header>
        __WORKSHEET_PANEL__
        <section class="generated-panel" id="generated-viewer" aria-labelledby="generated-viewer-title">
          <header>
            <div class="generated-heading">
              <h4 id="generated-viewer-title">生成图像预览</h4>
              <span class="chip" id="generated-count">暂无生成图像</span>
            </div>
            <p class="generated-intro">__GENERATED_INTRO__</p>
            <p class="generated-catalog-summary" id="generated-catalog-summary" hidden>
              生成记录：<span id="generated-date"></span> · 清单共 <span id="generated-catalog-count"></span> 张图像
            </p>
__GENERATED_ARCHIVE_ROW__
          </header>
          <p class="generated-empty" id="generated-empty" aria-live="polite">__GENERATED_EMPTY__</p>
          <div class="generated-content" id="generated-content" hidden>
            <div class="generated-toolbar" aria-label="生成图像选择器">
              <div class="field">
                <label for="generated-asset-select">选择生成图像</label>
                <select id="generated-asset-select"></select>
              </div>
              <div class="position" id="generated-asset-position" aria-live="polite"></div>
              <button type="button" id="generated-asset-previous">上一张</button>
              <button type="button" class="next-button" id="generated-asset-next">下一张</button>
            </div>
            <div class="generated-background-control" role="group" aria-label="图像预览底色">
              <span>预览底色</span>
              <button type="button" data-generated-background="light" aria-pressed="true">浅色</button>
              <button type="button" data-generated-background="dark" aria-pressed="false">深色</button>
            </div>
            <div class="generated-stage" id="generated-stage" data-background="light">
              <figure class="generated-image-figure">
                <div class="generated-image-frame">
                  <img id="generated-asset-image" alt="">
                </div>
                <figcaption id="generated-asset-caption"></figcaption>
              </figure>
              <div class="generated-details">
                <p><span class="generated-label">表达意图</span><span id="generated-asset-intent"></span></p>
                <p class="generated-kind-row" id="generated-kind-row" hidden><span class="generated-label">素材类型</span><span class="chip generated-kind" id="generated-kind"></span></p>
                <p class="generated-review-row" id="generated-review-row" hidden><span class="generated-label">复核记录</span><span id="generated-asset-review"></span></p>
                <p class="generated-notes" id="generated-notes" hidden></p>
                <div class="generated-links">
                  <a id="generated-download" href="#" download>下载原始 PNG</a>
                  <a class="generated-contact-sheet" id="generated-contact-sheet" href="#" target="_blank" rel="noopener noreferrer" hidden>查看联系表预览</a>
                </div>
              </div>
            </div>
          </div>
        </section>
        <div class="markdown-body" id="template-body"></div>
      </article>
      <div class="footer">本地静态页面 · 内容嵌入此文件 · 不需要联网</div>
    </section>
    <section class="view" id="view-platform" hidden>
      <div class="view-heading">
        <div>
          <h2>平台静态贴图档案</h2>
          <p>五个档案各自显示平台来源文档中的完整对应章节；来源核验不代表上传或平台接收。</p>
        </div>
      </div>
      <div class="reference-intro"><div class="markdown-body" id="platform-intro"></div></div>
      <div class="reference-toolbar">
        <div class="field">
          <label for="profile-select">选择平台档案</label>
          <select id="profile-select"></select>
        </div>
        <div class="position" id="profile-position" aria-live="polite"></div>
        <button type="button" id="profile-previous">上一项</button>
        <button type="button" class="next-button" id="profile-next">下一项</button>
      </div>
      <article class="profile-card">
        <header class="profile-header">
          <h3 id="profile-title"></h3>
          <span class="chip" id="profile-category">平台规范</span>
          <div class="status-row" id="profile-status"></div>
          <p class="source-row"><a id="profile-source-file" href="../references/platform-profiles.md">打开完整平台规范 Markdown</a></p>
        </header>
        <div class="profile-body markdown-body" id="profile-body"></div>
      </article>
      <div class="footer">微信条目保留原文中的来源缺口状态。</div>
    </section>
    <section class="view" id="view-coverage" hidden>
      <div class="view-heading">
        <div>
          <h2>研究来源与覆盖范围</h2>
          <p>显示研究覆盖原文，保留已读内容、未访问内容与来源缺口的区分。</p>
        </div>
        <a id="coverage-source-file" href="../references/research-coverage.md">打开来源覆盖 Markdown</a>
      </div>
      <article class="single-reference"><div class="markdown-body" id="coverage-body"></div></article>
    </section>
    <section class="view" id="view-brand" hidden>
      <div class="view-heading">
        <div>
          <h2>DreamWeaver 品牌指南</h2>
          <p>显示品牌身份、四臂动作关系、配色与品牌署名原文。</p>
        </div>
        <a id="brand-source-file" href="../references/oneirloom-brand.md">打开品牌指南 Markdown</a>
      </div>
      <article class="single-reference"><div class="markdown-body" id="brand-body"></div></article>
    </section>
  </main>
  <script type="application/json" id="browser-data">__BROWSER_DATA__</script>
  <script>
    (() => {
      const data = JSON.parse(document.getElementById("browser-data").textContent);
      const templateSelect = document.getElementById("template-select");
      const profileSelect = document.getElementById("profile-select");
      const generatedAssetSelect = document.getElementById("generated-asset-select");
      let templateIndex = 0;
      let profileIndex = 0;
      let generatedAssetIndex = 0;

      function fillSelect(select, rows, valueKey, labelFor) {
        select.replaceChildren(...rows.map((row) => {
          const option = document.createElement("option");
          option.value = row[valueKey];
          option.textContent = labelFor(row);
          return option;
        }));
      }

      function setSourceLinks(container, links) {
        container.replaceChildren();
        for (const item of links) {
          const anchor = document.createElement("a");
          anchor.href = item.url;
          anchor.textContent = item.label;
          anchor.target = "_blank";
          anchor.rel = "noopener noreferrer";
          container.append(anchor);
        }
        if (!links.length) container.textContent = "原文未列外部来源链接";
      }

      function renderGenerated(item) {
        const generated = item.generated;
        const images = generated ? generated.images : [];
        const hasImages = images.length > 0;
        const empty = document.getElementById("generated-empty");
        const content = document.getElementById("generated-content");
        empty.hidden = hasImages;
        content.hidden = !hasImages;
        document.getElementById("generated-count").textContent = hasImages
          ? images.length + " 张生成图像"
          : "暂无生成图像";

        const catalog = data.generatedCatalog;
        const catalogSummary = document.getElementById("generated-catalog-summary");
        catalogSummary.hidden = !catalog;
        if (catalog) {
          document.getElementById("generated-date").textContent = catalog.date || "未记录日期";
          document.getElementById("generated-catalog-count").textContent = String(catalog.image_count);
        }
        const archiveRow = document.getElementById("generated-archive-row");
        if (archiveRow) {
          archiveRow.hidden = !(catalog && catalog.archive);
          if (catalog && catalog.archive) document.getElementById("generated-archive").href = catalog.archive;
        }

        if (!hasImages) return;
        if (generatedAssetIndex >= images.length) generatedAssetIndex = 0;
        fillSelect(generatedAssetSelect, images, "id", (asset) => asset.caption ? asset.id + " · " + asset.caption : asset.id);
        const asset = images[generatedAssetIndex];
        generatedAssetSelect.value = asset.id;
        document.getElementById("generated-asset-position").textContent =
          String(generatedAssetIndex + 1).padStart(2, "0") + " / " + String(images.length).padStart(2, "0");
        const image = document.getElementById("generated-asset-image");
        image.src = asset.file;
        image.alt = asset.caption ? "生成图像：" + asset.caption : "生成图像 " + asset.id;
        document.getElementById("generated-asset-caption").textContent = asset.caption;
        document.getElementById("generated-asset-intent").textContent = asset.intent;
        document.getElementById("generated-download").href = asset.file;
        const kindRow = document.getElementById("generated-kind-row");
        kindRow.hidden = !asset.kind;
        document.getElementById("generated-kind").textContent = asset.kind || "";
        const reviewRow = document.getElementById("generated-review-row");
        reviewRow.hidden = !asset.review;
        document.getElementById("generated-asset-review").textContent = asset.review || "";
        const notes = document.getElementById("generated-notes");
        notes.hidden = !generated.notes;
        notes.textContent = generated.notes ? "模板备注：" + generated.notes : "";
        const previewLink = document.getElementById("generated-contact-sheet");
        previewLink.hidden = !generated.preview;
        if (generated.preview) previewLink.href = generated.preview;
      }

      function renderTemplate() {
        const item = data.templates[templateIndex];
        templateSelect.value = item.id;
        document.getElementById("template-position").textContent =
          String(templateIndex + 1).padStart(2, "0") + " / " + data.templates.length;
        document.getElementById("template-category").textContent = item.category;
        document.getElementById("template-id").textContent = item.id;
        document.getElementById("template-title").textContent = item.title;
        const heading = item.markdown.match(/^#\s+(.+)$/m);
        document.getElementById("template-source-title").textContent = heading ? heading[1] : "";
        document.getElementById("template-summary").textContent = item.summary;
        document.getElementById("template-source-file").href = item.sourceFile;
        setSourceLinks(document.getElementById("template-source-links"), item.sources);
        document.getElementById("template-body").innerHTML = item.html;
        document.getElementById("workspace-preview").dataset.visible =
          String(item.id === "eight-slot-workspace");
        document.getElementById("copy-status").textContent = "";
        generatedAssetIndex = 0;
        renderGenerated(item);
        document.title = item.title + " · Oneirloom 表情贴图模板库";
      }

      function renderProfile() {
        const item = data.references.platform.profiles[profileIndex];
        profileSelect.value = item.id;
        document.getElementById("profile-position").textContent =
          String(profileIndex + 1).padStart(2, "0") + " / " + data.references.platform.profiles.length;
        document.getElementById("profile-title").textContent = item.title;
        document.getElementById("profile-status").replaceChildren();
        if (item.id === "wechat-static") {
          const status = document.createElement("span");
          status.className = "chip status-gap";
          status.textContent = "SOURCE GAP · 官方要求待核实";
          document.getElementById("profile-status").append(status);
        }
        document.getElementById("profile-body").innerHTML = item.html;
      }

      function setView(name) {
        for (const section of document.querySelectorAll(".view")) {
          section.hidden = section.id !== "view-" + name;
        }
        for (const button of document.querySelectorAll("[data-view-button]")) {
          button.setAttribute("aria-pressed", String(button.dataset.viewButton === name));
        }
      }

      fillSelect(
        templateSelect,
        data.templates,
        "id",
        (item) => item.title + " · " + item.category
      );
      fillSelect(
        profileSelect,
        data.references.platform.profiles,
        "id",
        (item) => item.title
      );
      document.getElementById("platform-intro").innerHTML = data.references.platform.introHtml;
      document.getElementById("coverage-body").innerHTML = data.references.coverage.html;
      document.getElementById("brand-body").innerHTML = data.references.brand.html;
      renderTemplate();
      renderProfile();

      templateSelect.addEventListener("change", () => {
        templateIndex = data.templates.findIndex((item) => item.id === templateSelect.value);
        renderTemplate();
      });
      generatedAssetSelect.addEventListener("change", () => {
        const item = data.templates[templateIndex];
        generatedAssetIndex = item.generated.images.findIndex((asset) => asset.id === generatedAssetSelect.value);
        renderGenerated(item);
      });
      document.getElementById("generated-asset-previous").addEventListener("click", () => {
        const images = data.templates[templateIndex].generated.images;
        generatedAssetIndex = (generatedAssetIndex + images.length - 1) % images.length;
        renderGenerated(data.templates[templateIndex]);
      });
      document.getElementById("generated-asset-next").addEventListener("click", () => {
        const images = data.templates[templateIndex].generated.images;
        generatedAssetIndex = (generatedAssetIndex + 1) % images.length;
        renderGenerated(data.templates[templateIndex]);
      });
      for (const button of document.querySelectorAll("[data-generated-background]")) {
        button.addEventListener("click", () => {
          const background = button.dataset.generatedBackground;
          document.getElementById("generated-stage").dataset.background = background;
          for (const option of document.querySelectorAll("[data-generated-background]")) {
            option.setAttribute("aria-pressed", String(option === button));
          }
        });
      }
      document.getElementById("template-previous").addEventListener("click", () => {
        templateIndex = (templateIndex + data.templates.length - 1) % data.templates.length;
        renderTemplate();
      });
      document.getElementById("template-next").addEventListener("click", () => {
        templateIndex = (templateIndex + 1) % data.templates.length;
        renderTemplate();
      });
      profileSelect.addEventListener("change", () => {
        profileIndex = data.references.platform.profiles.findIndex((item) => item.id === profileSelect.value);
        renderProfile();
      });
      document.getElementById("profile-previous").addEventListener("click", () => {
        profileIndex = (profileIndex + data.references.platform.profiles.length - 1) % data.references.platform.profiles.length;
        renderProfile();
      });
      document.getElementById("profile-next").addEventListener("click", () => {
        profileIndex = (profileIndex + 1) % data.references.platform.profiles.length;
        renderProfile();
      });
      for (const button of document.querySelectorAll("[data-view-button]")) {
        button.addEventListener("click", () => setView(button.dataset.viewButton));
      }
      document.getElementById("copy-prompt").addEventListener("click", async () => {
        const item = data.templates[templateIndex];
        const status = document.getElementById("copy-status");
        try {
          if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error("Clipboard unavailable");
          await navigator.clipboard.writeText(item.copyText);
          status.textContent = "已复制首段英文提示词。";
        } catch {
          const code = document.querySelector("#template-body pre code");
          if (code) {
            const range = document.createRange();
            range.selectNodeContents(code);
            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);
            status.textContent = "自动复制不可用，提示词已选中，可使用系统复制。";
          } else {
            status.textContent = "自动复制不可用，正文没有可选择的提示词。";
          }
        }
      });
    })();
  </script>
</body>
</html>
"""


def _render_browser(data: dict, public: bool) -> str:
    if public:
        substitutions = {
            "__PAGE_TITLE__": "表情贴图模板库 | 离线参考",
            "__BRAND_LOCKUP__": "",
            "__HEADER_EYEBROW__": "OFFLINE REFERENCE",
            "__HEADER_SUMMARY__": "十四款方法模板、五份平台档案、来源覆盖与品牌素材说明",
            "__IDENTITY_REFERENCE__": (
                '<p class="brand-copy">角色身份请由用户提供的角色参考确定；此公共包不含预置品牌图像。</p>'
            ),
            "__WORKSHEET_PANEL__": (
                '<aside class="preview-panel" id="workspace-preview" aria-label="工作表素材说明">'
                '<p>工作表图像属于本地品牌素材，公共包提供八格规划方法；使用用户自己的角色参考</p>'
                '</aside>'
            ),
            "__GENERATED_INTRO__": (
                "本地品牌示例图像属于私人素材，公共包不包含这些文件；此浏览器不包含其图像地址或归档。"
            ),
            "__GENERATED_ARCHIVE_ROW__": "",
            "__GENERATED_EMPTY__": (
                "公共包不含私人本地生成示例、图像地址或归档。请用自己的角色参考按模板方法制作并在本地查看图像。"
            ),
        }
    else:
        substitutions = {
            "__PAGE_TITLE__": "Oneirloom 表情贴图模板库",
            "__BRAND_LOCKUP__": '<img class="brand-lockup" src="../assets/brand-lockup.svg" alt="Oneirloom 织梦师">',
            "__HEADER_EYEBROW__": "ONEIRLOOM · OFFLINE REFERENCE",
            "__HEADER_SUMMARY__": "十四款品牌模板、五份平台档案、来源覆盖与品牌指南",
            "__IDENTITY_REFERENCE__": (
                '<figure class="identity-reference">'
                '<img src="../assets/mascot-reference.png" alt="DreamWeaver 获认可的正面身份参考图">'
                '<figcaption><strong>身份参考，非动作成品</strong><span>正面角色示例</span></figcaption>'
                '</figure>'
            ),
            "__WORKSHEET_PANEL__": (
                '<aside class="preview-panel" id="workspace-preview" aria-label="八格工作表预览">'
                '<img src="eight-slot-workspace/workspace-preview.png" alt="空白绘制工作表，8个动作待绘制">'
                '<div><p><strong>空白绘制工作表，8个动作待绘制</strong></p>'
                '<p>预览格是绘制位置，不是已完成的表情动作。</p>'
                '<a class="download-link" href="eight-slot-workspace/workspace.svg" download>下载空白绘制工作表 SVG</a>'
                '</div></aside>'
            ),
            "__GENERATED_INTRO__": "此处展示实际生成的单张图像，身份参考继续单独显示。",
            "__GENERATED_ARCHIVE_ROW__": (
                '<p class="generated-archive-row" id="generated-archive-row" hidden>'
                '<a class="download-link" id="generated-archive" href="#" download>下载生成图像归档</a>'
                '</p>'
            ),
            "__GENERATED_EMPTY__": "暂无生成图像。登记本地生成素材后，会在这里显示。",
        }

    rendered_html = HTML_TEMPLATE
    for placeholder, value in substitutions.items():
        rendered_html = rendered_html.replace(placeholder, value)
    return rendered_html.replace("__BROWSER_DATA__", _safe_json(data))


def build(public: bool = False) -> Path:
    engine = _markdown_engine()
    if public:
        data = build_data(engine, generated_catalog={})
        data["generatedCatalog"] = None
    else:
        data = build_data(engine)
    rendered_html = _render_browser(data, public)
    BROWSER_PATH.write_text(rendered_html, encoding="utf-8", newline="\n")
    return BROWSER_PATH


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the offline expression-sticker template browser.")
    parser.add_argument("--public", action="store_true", help="omit private local brand and generated assets")
    args = parser.parse_args()
    print(build(public=args.public).relative_to(ROOT).as_posix())
