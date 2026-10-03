from __future__ import annotations

import importlib.util
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
BUILDER_PATH = ROOT / "skills" / "oneirloom-expression-stickers" / "scripts" / "build_template_browser.py"
EDGE = Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
EVIDENCE = ROOT / "work" / "sticker-pack-templates-20261002"
CHECK_PATH = EVIDENCE / "complete-browser-checks.json"

spec = importlib.util.spec_from_file_location("complete_sticker_browser_builder", BUILDER_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Cannot load browser builder: {BUILDER_PATH}")
builder = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = builder
spec.loader.exec_module(builder)


def file_url_path(value: str) -> Path:
    parts = urlsplit(value)
    if parts.scheme.lower() != "file" or parts.netloc not in ("", "localhost"):
        raise AssertionError(f"Expected a local file URL, received {value}")
    path = unquote(parts.path)
    if re.match(r"^/[A-Za-z]:/", path):
        path = path[1:]
    if os.name == "nt":
        path = path.replace("/", "\\")
    return Path(path)


def assert_file_href(page, selector: str, expected: Path, label: str) -> str:
    href = page.locator(selector).evaluate("element => element.href")
    actual = file_url_path(href)
    if actual.resolve() != expected.resolve():
        raise AssertionError(f"{label} points to {actual}, expected {expected}")
    if not actual.is_file():
        raise AssertionError(f"{label} target does not exist: {actual}")
    return href


def check_rendered_file_targets(page, selector: str, label: str, checked: list[dict]) -> None:
    targets = page.locator(selector).evaluate_all(
        "elements => elements.flatMap(element => [element.href, element.src])"
    )
    for href in targets:
        if not href:
            continue
        parts = urlsplit(href)
        if parts.scheme.lower() != "file":
            continue
        target = file_url_path(href)
        if not target.is_file():
            raise AssertionError(f"{label} has a missing local file target: {href}")
        checked.append({"owner": label, "href": href, "path": str(target)})


catalog = json.loads(builder.GENERATED_CATALOG.read_text(encoding="utf-8"))
catalog_templates = catalog["templates"]
catalog_by_id = {item["id"]: item for item in catalog_templates}
browser_html = builder.BROWSER_PATH.read_text(encoding="utf-8")
embedded_match = re.search(
    r'<script type="application/json" id="browser-data">(.*?)</script>',
    browser_html,
    re.S,
)
if embedded_match is None:
    raise AssertionError("The rebuilt browser-data script was not found")
embedded = json.loads(embedded_match.group(1))
browser_templates = embedded["templates"]
browser_by_id = {item["id"]: item for item in browser_templates}

assert embedded["generatedCatalog"] is not None
assert embedded["generatedCatalog"]["date"] == catalog["date"]
assert embedded["generatedCatalog"]["image_count"] == catalog["image_count"] == 156
assert len(catalog_templates) == len(browser_templates) == 14
assert set(catalog_by_id) == set(browser_by_id)
assert sum(len(item["images"]) for item in catalog_templates) == 156

for template_id, record in catalog_by_id.items():
    image_rows = record["images"]
    assert record["count"] == len(image_rows), template_id
    browser_record = browser_by_id[template_id]
    assert len(browser_record["generated"]["images"]) == len(image_rows), template_id
    assert [image["id"] for image in browser_record["generated"]["images"]] == [
        image["id"] for image in image_rows
    ], template_id
    assert (builder.SKILL / record["preview"]).is_file(), record["preview"]
    for image in image_rows:
        assert image["id"]
        assert isinstance(image.get("caption", ""), str)
        assert isinstance(image.get("intent", ""), str)
        assert (builder.SKILL / image["file"]).is_file(), image["file"]

archive_path = builder.SKILL / catalog["archive"]
assert archive_path.is_file(), catalog["archive"]

checks: dict[str, object] = {
    "result": "RUNNING",
    "browser": "Microsoft Edge",
    "browser_path": str(EDGE),
    "page": builder.BROWSER_PATH.as_uri(),
    "catalog": {
        "path": str(builder.GENERATED_CATALOG),
        "date": catalog["date"],
        "template_count": len(catalog_templates),
        "image_count": catalog["image_count"],
        "archive": catalog["archive"],
        "archive_file_exists": archive_path.is_file(),
        "template_ids": [item["id"] for item in catalog_templates],
    },
    "templates": [],
    "assets": [],
    "local_file_links": [],
    "interactions": {},
    "screenshots": {},
}
page_errors: list[str] = []
console_errors: list[str] = []
external_requests: list[str] = []
failed_requests: list[dict[str, str]] = []
browser = None

try:
    if not EDGE.is_file():
        raise FileNotFoundError(f"Edge executable is missing: {EDGE}")
    if not builder.BROWSER_PATH.is_file():
        raise FileNotFoundError(f"Built browser is missing: {builder.BROWSER_PATH}")

    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=str(EDGE), headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=1)
        page.on("pageerror", lambda error: page_errors.append(str(error)))
        page.on("console", lambda message: console_errors.append(message.text) if message.type == "error" else None)
        page.on(
            "request",
            lambda request: external_requests.append(request.url)
            if urlsplit(request.url).scheme.lower() not in ("file", "data")
            else None,
        )
        page.on(
            "requestfailed",
            lambda request: failed_requests.append(
                {"url": request.url, "failure": request.failure or "unknown"}
            ),
        )
        page.goto(builder.BROWSER_PATH.as_uri(), wait_until="load")

        page_data = page.locator("#browser-data").evaluate("element => JSON.parse(element.textContent)")
        assert page_data["generatedCatalog"] == embedded["generatedCatalog"]
        assert page.locator("#template-select option").count() == 14
        assert page.locator("#profile-select option").count() == 5
        assert page.locator("#generated-catalog-summary").is_visible()
        assert page.locator("#generated-date").inner_text() == catalog["date"]
        assert page.locator("#generated-catalog-count").inner_text() == "156"
        assert "身份参考" in page.locator(".identity-reference").inner_text()
        check_rendered_file_targets(page, "img", "initial page images", checks["local_file_links"])

        ui_template_rows = []
        asset_rows = []
        local_links = checks["local_file_links"]
        selected_multientry = max(catalog_templates, key=lambda item: len(item["images"]))

        for template in catalog_templates:
            template_id = template["id"]
            markdown_path = builder.TEMPLATE_DIR / template_id / "template.md"
            source_file = browser_by_id[template_id]["sourceFile"]
            assert markdown_path.is_file(), markdown_path
            assert Path(source_file).as_posix() == f"{template_id}/template.md"

            page.locator("#template-select").select_option(template_id)
            assert page.locator("#template-id").text_content() == template_id
            assert page.locator("#template-select").input_value() == template_id
            assert page.locator("#template-position").inner_text().endswith("/ 14")
            assert page.locator("#template-body").inner_text().strip()
            source_href = assert_file_href(
                page,
                "#template-source-file",
                markdown_path,
                f"{template_id} Markdown source",
            )
            check_rendered_file_targets(
                page, "#template-body a, #template-body img", f"{template_id} Markdown body", local_links
            )
            generated_count = len(template["images"])
            assert page.locator("#generated-count").inner_text() == f"{generated_count} 张生成图像"
            assert page.locator("#generated-asset-select option").count() == generated_count
            assert page.locator("#generated-archive-row").is_visible()
            archive_href = assert_file_href(page, "#generated-archive", archive_path, "generated ZIP archive")

            preview_href = None
            preview_path = builder.SKILL / template["preview"]
            preview_href = assert_file_href(
                page,
                "#generated-contact-sheet",
                preview_path,
                f"{template_id} contact sheet",
            )

            ui_ids = page.locator("#generated-asset-select option").evaluate_all(
                "elements => elements.map(element => element.value)"
            )
            assert ui_ids == [image["id"] for image in template["images"]], template_id

            for index, asset in enumerate(template["images"], start=1):
                asset_path = builder.SKILL / asset["file"]
                expected_href = asset_path.resolve().as_uri()
                page.locator("#generated-asset-select").select_option(asset["id"])
                page.wait_for_function(
                    "expected => { const image = document.getElementById('generated-asset-image'); "
                    "return image.complete && image.naturalWidth === 1254 && image.src === expected; }",
                    arg=expected_href,
                    timeout=20000,
                )
                assert page.locator("#generated-asset-select").input_value() == asset["id"]
                assert page.locator("#generated-asset-position").inner_text() == (
                    f"{index:02d} / {generated_count:02d}"
                )
                assert page.locator("#generated-asset-caption").inner_text() == asset.get("caption", "")
                assert page.locator("#generated-asset-intent").inner_text() == asset.get("intent", "")
                actual_href = assert_file_href(
                    page,
                    "#generated-download",
                    asset_path,
                    f"{template_id}/{asset['id']} PNG download",
                )
                image_state = page.locator("#generated-asset-image").evaluate(
                    "image => ({src: image.src, naturalWidth: image.naturalWidth, "
                    "complete: image.complete, alt: image.alt})"
                )
                assert image_state["src"] == expected_href
                assert image_state["naturalWidth"] == 1254
                assert image_state["complete"] is True
                assert image_state["alt"] == (
                    "生成图像：" + asset["caption"] if asset.get("caption") else "生成图像 " + asset["id"]
                )
                asset_rows.append(
                    {
                        "template_id": template_id,
                        "id": asset["id"],
                        "caption": asset.get("caption", ""),
                        "intent": asset.get("intent", ""),
                        "file": asset["file"],
                        "download_href": actual_href,
                        "image_href": image_state["src"],
                        "natural_width": image_state["naturalWidth"],
                    }
                )

            ui_template_rows.append(
                {
                    "id": template_id,
                    "ui_count": generated_count,
                    "asset_ids": ui_ids,
                    "source_markdown": source_file,
                    "source_href": source_href,
                    "contact_sheet_href": preview_href,
                    "archive_href": archive_href,
                    "guidance_visible": bool(page.locator("#template-body").inner_text().strip()),
                }
            )

        assert len(asset_rows) == catalog["image_count"] == 156
        checks["templates"] = ui_template_rows
        checks["assets"] = asset_rows

        chosen_template_id = selected_multientry["id"]
        chosen_images = selected_multientry["images"]
        page.locator("#template-select").select_option(chosen_template_id)
        page.locator("#generated-asset-select").select_option(chosen_images[0]["id"])
        page.wait_for_function(
            "() => { const image = document.getElementById('generated-asset-image'); "
            "return image.complete && image.naturalWidth === 1254; }",
            timeout=20000,
        )
        page.locator('[data-generated-background="dark"]').click()
        assert page.locator("#generated-stage").get_attribute("data-background") == "dark"
        assert page.locator('[data-generated-background="dark"]').get_attribute("aria-pressed") == "true"
        page.locator('[data-generated-background="light"]').click()
        assert page.locator("#generated-stage").get_attribute("data-background") == "light"
        assert page.locator('[data-generated-background="light"]').get_attribute("aria-pressed") == "true"
        page.locator("#generated-asset-previous").click()
        assert page.locator("#generated-asset-select").input_value() == chosen_images[-1]["id"]
        page.wait_for_function(
            "() => { const image = document.getElementById('generated-asset-image'); "
            "return image.complete && image.naturalWidth === 1254; }",
            timeout=20000,
        )
        page.locator("#generated-asset-next").click()
        assert page.locator("#generated-asset-select").input_value() == chosen_images[0]["id"]
        page.wait_for_function(
            "() => { const image = document.getElementById('generated-asset-image'); "
            "return image.complete && image.naturalWidth === 1254; }",
            timeout=20000,
        )

        ordered_ids = [item["id"] for item in browser_templates]
        page.locator("#template-select").select_option(ordered_ids[-1])
        page.locator("#template-next").click()
        assert page.locator("#template-select").input_value() == ordered_ids[0]
        page.locator("#template-previous").click()
        assert page.locator("#template-select").input_value() == ordered_ids[-1]
        page.locator("#template-select").select_option(chosen_template_id)
        page.locator("#copy-prompt").click()
        page.wait_for_function(
            "() => ['已复制首段英文提示词。', "
            "'自动复制不可用，提示词已选中，可使用系统复制。'].includes(" 
            "document.getElementById('copy-status').textContent)",
            timeout=5000,
        )
        assert page.locator("#copy-status").inner_text() in (
            "已复制首段英文提示词。",
            "自动复制不可用，提示词已选中，可使用系统复制。",
        )

        page.locator('[data-view-button="platform"]').click()
        assert len(page.locator("#platform-intro").inner_text().strip()) > 100
        assert_file_href(
            page,
            "#profile-source-file",
            builder.REFERENCES["platform"],
            "platform Markdown source",
        )
        check_rendered_file_targets(page, "#platform-intro a, #platform-intro img", "platform intro", local_links)
        profile_rows = page.locator("#profile-select option").evaluate_all(
            "elements => elements.map(element => element.value)"
        )
        assert len(profile_rows) == 5
        for profile in embedded["references"]["platform"]["profiles"]:
            page.locator("#profile-select").select_option(profile["id"])
            assert page.locator("#profile-title").inner_text() == profile["title"]
            assert len(page.locator("#profile-body").inner_text().strip()) > 100
            check_rendered_file_targets(
                page, "#profile-body a, #profile-body img", f"{profile['id']} profile", local_links
            )
            if profile["id"] == "wechat-static":
                assert "SOURCE GAP" in page.locator("#profile-status").inner_text()
        page.locator("#profile-select").select_option(profile_rows[0])
        page.locator("#profile-previous").click()
        assert page.locator("#profile-select").input_value() == profile_rows[-1]
        page.locator("#profile-next").click()
        assert page.locator("#profile-select").input_value() == profile_rows[0]

        page.locator('[data-view-button="coverage"]').click()
        assert len(page.locator("#coverage-body").inner_text().strip()) > 500
        assert_file_href(
            page,
            "#coverage-source-file",
            builder.REFERENCES["coverage"],
            "coverage Markdown source",
        )
        check_rendered_file_targets(page, "#coverage-body a, #coverage-body img", "coverage guide", local_links)

        page.locator('[data-view-button="brand"]').click()
        assert len(page.locator("#brand-body").inner_text().strip()) > 500
        assert_file_href(
            page,
            "#brand-source-file",
            builder.REFERENCES["brand"],
            "brand Markdown source",
        )
        check_rendered_file_targets(page, "#brand-body a, #brand-body img", "brand guide", local_links)

        page.locator('[data-view-button="templates"]').click()
        page.locator("#template-select").select_option(chosen_template_id)
        page.locator("#generated-asset-select").select_option(chosen_images[0]["id"])
        page.set_viewport_size({"width": 1280, "height": 900})
        page.evaluate(
            "() => { const top = document.getElementById('template-select').getBoundingClientRect().top + "
            "window.scrollY; window.scrollTo(0, Math.max(0, top - 24)); }"
        )
        desktop_width = page.evaluate(
            "({document: document.documentElement.scrollWidth, body: document.body.scrollWidth, inner: innerWidth})"
        )
        assert desktop_width["document"] == desktop_width["inner"]
        assert desktop_width["body"] == desktop_width["inner"]
        desktop_shot = EVIDENCE / "complete-browser-desktop.png"
        page.screenshot(path=str(desktop_shot))

        page.set_viewport_size({"width": 390, "height": 844})
        page.evaluate(
            "() => { const top = document.getElementById('template-select').getBoundingClientRect().top + "
            "window.scrollY; window.scrollTo(0, Math.max(0, top - 18)); }"
        )
        mobile_width = page.evaluate(
            "({document: document.documentElement.scrollWidth, body: document.body.scrollWidth, inner: innerWidth})"
        )
        assert mobile_width["document"] == mobile_width["inner"]
        assert mobile_width["body"] == mobile_width["inner"]
        mobile_shot = EVIDENCE / "complete-browser-mobile.png"
        page.screenshot(path=str(mobile_shot))

        assert not page_errors, page_errors
        assert not console_errors, console_errors
        assert not external_requests, external_requests
        assert not failed_requests, failed_requests

        checks["interactions"] = {
            "template_count": page.locator("#template-select option").count(),
            "asset_selector_previous_next": True,
            "template_previous_next": True,
            "light_dark_aria_pressed": True,
            "png_downloads_resolve_to_actual_files": len(asset_rows),
            "contact_sheets_resolve_to_actual_files": len(ui_template_rows),
            "archive_href": catalog["archive"],
            "archive_target_exists_without_fetch": archive_path.is_file(),
            "copy_first_prompt": True,
            "profiles": profile_rows,
            "wechat_source_gap_preserved": True,
            "coverage_and_brand_rendered": True,
        }
        checks["layout"] = {"desktop": desktop_width, "mobile": mobile_width}
        checks["screenshots"] = {
            "desktop": str(desktop_shot),
            "mobile": str(mobile_shot),
        }
        checks["local_file_links"] = local_links
        checks["result"] = "PASS"
        browser.close()
        browser = None
except Exception as error:
    checks["result"] = "FAIL"
    checks["failure"] = {"type": type(error).__name__, "message": str(error)}
    browser = None
    raise
finally:
    if browser is not None:
        browser.close()
    checks["browser_errors"] = page_errors
    checks["console_errors"] = console_errors
    checks["external_requests"] = external_requests
    checks["failed_requests"] = failed_requests
    CHECK_PATH.write_text(json.dumps(checks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

print(json.dumps(checks, ensure_ascii=False, indent=2))
