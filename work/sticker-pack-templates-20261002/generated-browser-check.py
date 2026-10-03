from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILDER_PATH = ROOT / "skills" / "oneirloom-expression-stickers" / "scripts" / "build_template_browser.py"
EDGE = Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
EVIDENCE = ROOT / "work" / "sticker-pack-templates-20261002"

spec = importlib.util.spec_from_file_location("sticker_browser_builder", BUILDER_PATH)
builder = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = builder
spec.loader.exec_module(builder)

image_rows = [
    {
        "id": "P01-celebrate",
        "caption": "太好了！",
        "intent": "为已完成的事情表达庆祝。",
        "file": "assets/generated/pose-decomposition/P01-celebrate.png",
        "kind": "reaction",
        "review": "本地动作检查记录。",
    },
    {
        "id": "P02-apologize",
        "caption": "对不起",
        "intent": "为刚才的失误表达歉意。",
        "file": "assets/generated/pose-decomposition/P02-apologize.png",
        "kind": "reaction",
    },
    {
        "id": "P03-consider",
        "caption": "让我想想",
        "intent": "表示正在认真考虑。",
        "file": "assets/generated/pose-decomposition/P03-consider.png",
        "kind": "reaction",
    },
]
fixture = {
    "date": "2026-10-03",
    "image_count": len(image_rows),
    "templates": [
        {
            "id": "pose-decomposition",
            "count": len(image_rows),
            "preview": "assets/generated/pose-decomposition/preview.png",
            "images": image_rows,
            "notes": "三张本地动作示例。",
        }
    ],
}

assert not builder.GENERATED_CATALOG.exists(), "the fixture must remain in memory"
for row in image_rows:
    assert (builder.SKILL / row["file"]).is_file(), row["file"]
assert (builder.SKILL / fixture["templates"][0]["preview"]).is_file()

engine = builder._markdown_engine()
default_data = builder.build_data(engine)
assert all(item.get("generated") is None for item in default_data["templates"])
fixture_data = builder.build_data(engine, generated_catalog=fixture)
pose = next(item for item in fixture_data["templates"] if item["id"] == "pose-decomposition")
assert len(pose["generated"]["images"]) == 3
assert pose["generated"]["images"][0]["file"] == "../assets/generated/pose-decomposition/P01-celebrate.png"
assert pose["generated"]["preview"] == "../assets/generated/pose-decomposition/preview.png"
assert next(item for item in fixture_data["templates"] if item["id"] == "daily-sixteen").get("generated") is None
for invalid_path in ("https://example.invalid/image.png", "../../outside.png", "//example.invalid/image.png"):
    try:
        builder._generated_asset_url(invalid_path)
    except ValueError:
        pass
    else:
        raise AssertionError(f"non-local generated path was accepted: {invalid_path}")

original_html = builder.BROWSER_PATH.read_bytes()
page_errors: list[str] = []
console_errors: list[str] = []
external_requests: list[str] = []
checks: dict[str, object] = {}

try:
    fixture_html = builder.HTML_TEMPLATE.replace("__BROWSER_DATA__", builder._safe_json(fixture_data))
    builder.BROWSER_PATH.write_text(fixture_html, encoding="utf-8", newline="\n")

    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=str(EDGE), headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=1)
        page.on("pageerror", lambda error: page_errors.append(str(error)))
        page.on("console", lambda message: console_errors.append(message.text) if message.type == "error" else None)
        page.on("request", lambda request: external_requests.append(request.url) if not request.url.startswith("file:") and not request.url.startswith("data:") else None)
        page.goto(builder.BROWSER_PATH.as_uri(), wait_until="load")

        checks["fallback"] = page.locator("#generated-empty").inner_text()
        assert "暂无生成图像" in checks["fallback"]
        identity_src = page.locator(".identity-reference img").get_attribute("src")
        assert identity_src and "mascot-reference.png" in identity_src

        page.locator("#template-select").select_option("pose-decomposition")
        assert page.locator("#generated-count").inner_text() == "3 张生成图像"
        assert page.locator("#generated-date").inner_text() == "2026-10-03"
        assert page.locator("#generated-kind").inner_text() == "reaction"
        assert page.locator("#generated-asset-image").get_attribute("src").endswith("P01-celebrate.png")
        assert page.evaluate("(() => { const image = document.getElementById('generated-asset-image'); return image.complete && image.naturalWidth > 0; })()")
        assert page.locator("#generated-asset-caption").inner_text() == "太好了！"
        assert page.locator("#generated-asset-intent").inner_text() == "为已完成的事情表达庆祝。"
        assert page.locator("#generated-asset-review").inner_text() == "本地动作检查记录。"
        assert page.locator("#generated-contact-sheet").get_attribute("href").endswith("preview.png")
        assert page.locator("#generated-download").get_attribute("href").endswith("P01-celebrate.png")
        assert page.locator("#generated-archive").is_hidden()
        assert "身份参考" in page.locator(".identity-reference").inner_text()
        assert page.locator("#workspace-preview").get_attribute("data-visible") == "false"
        page.locator('[data-generated-background="dark"]').click()
        assert page.locator("#generated-stage").get_attribute("data-background") == "dark"
        assert page.locator('[data-generated-background="dark"]').get_attribute("aria-pressed") == "true"
        page.locator('[data-generated-background="light"]').click()
        assert page.locator("#generated-stage").get_attribute("data-background") == "light"

        page.locator("#generated-asset-next").click()
        assert page.locator("#generated-asset-image").get_attribute("src").endswith("P02-apologize.png")
        page.locator("#generated-asset-select").select_option("P03-consider")
        assert page.locator("#generated-asset-caption").inner_text() == "让我想想"
        assert page.locator("#generated-asset-position").inner_text() == "03 / 03"
        page.locator("#template-select").select_option("eight-slot-workspace")
        assert page.locator("#workspace-preview").get_attribute("data-visible") == "true"
        assert page.locator("#workspace-preview img").get_attribute("alt") == "空白绘制工作表，8个动作待绘制"
        assert page.locator("#generated-empty").is_visible()
        assert page.locator("#template-source-file").is_visible()
        assert page.locator("#copy-prompt").is_visible()
        assert page.locator("#profile-select option").count() == 5
        page.locator("#copy-prompt").click()
        assert page.locator("#copy-status").inner_text() in (
            "已复制首段英文提示词。",
            "自动复制不可用，提示词已选中，可使用系统复制。",
        )

        page.locator('[data-view-button="platform"]').click()
        assert len(page.locator("#platform-intro").inner_text()) > 100
        page.locator("#profile-next").click()
        assert page.locator("#profile-title").inner_text() == "Telegram 静态贴图"
        assert len(page.locator("#profile-body").inner_text()) > 500
        page.locator('[data-view-button="coverage"]').click()
        assert len(page.locator("#coverage-body").inner_text()) > 500
        page.locator('[data-view-button="brand"]').click()
        assert len(page.locator("#brand-body").inner_text()) > 500
        page.locator('[data-view-button="templates"]').click()

        page.locator("#template-select").select_option("pose-decomposition")
        page.set_viewport_size({"width": 1280, "height": 900})
        page.screenshot(path=str(EVIDENCE / "generated-browser-desktop.png"), full_page=True)
        desktop_width = page.evaluate("({document: document.documentElement.scrollWidth, body: document.body.scrollWidth, inner: innerWidth})")
        assert desktop_width["document"] == desktop_width["inner"]
        assert desktop_width["body"] == desktop_width["inner"]
        page.set_viewport_size({"width": 390, "height": 844})
        page.screenshot(path=str(EVIDENCE / "generated-browser-mobile.png"), full_page=True)
        mobile_width = page.evaluate("({document: document.documentElement.scrollWidth, body: document.body.scrollWidth, inner: innerWidth})")
        assert mobile_width["document"] == mobile_width["inner"]
        assert mobile_width["body"] == mobile_width["inner"]
        checks["desktop_width"] = desktop_width
        checks["mobile_width"] = mobile_width
        checks["template_count"] = page.locator("#template-select option").count()
        checks["platform_count"] = page.locator("#profile-select option").count()
        checks["current_generated_image"] = page.locator("#generated-asset-image").get_attribute("src")

        hostile_fixture = json.loads(json.dumps(fixture_data))
        hostile_pose = next(item for item in hostile_fixture["templates"] if item["id"] == "pose-decomposition")
        hostile_pose["generated"]["notes"] = "</script><script>window.generatedInjected = true</script>"
        hostile_html = builder.HTML_TEMPLATE.replace("__BROWSER_DATA__", builder._safe_json(hostile_fixture))
        builder.BROWSER_PATH.write_text(hostile_html, encoding="utf-8", newline="\n")
        page.goto(builder.BROWSER_PATH.as_uri(), wait_until="load")
        page.locator("#template-select").select_option("pose-decomposition")
        assert page.locator("#generated-notes").inner_text() == "模板备注：</script><script>window.generatedInjected = true</script>"
        assert page.evaluate("window.generatedInjected === undefined")
        checks["untrusted_json_text_only"] = True
        browser.close()
finally:
    try:
        builder.build()
    except Exception:
        builder.BROWSER_PATH.write_bytes(original_html)
        raise

final_html = builder.BROWSER_PATH.read_text(encoding="utf-8")
embedded = re.search(r'<script type="application/json" id="browser-data">(.*?)</script>', final_html, re.S)
assert embedded is not None
final_data = json.loads(embedded.group(1))
assert final_data["generatedCatalog"] is None
assert all(item["generated"] is None for item in final_data["templates"])
assert "暂无生成图像" in final_html
checks["default_build_without_catalog"] = True

checks["page_errors"] = page_errors
checks["console_errors"] = console_errors
checks["external_requests"] = external_requests
checks["browser"] = "Microsoft Edge"
assert not page_errors, page_errors
assert not console_errors, console_errors
assert not external_requests, external_requests
(EVIDENCE / "generated-browser-checks.json").write_text(
    json.dumps(checks, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(json.dumps(checks, ensure_ascii=False, indent=2))
