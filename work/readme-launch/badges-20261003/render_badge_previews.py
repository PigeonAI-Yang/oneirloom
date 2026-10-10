from __future__ import annotations

import hashlib
import html
import json
import re
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

from markdown import Markdown
from markdown.extensions.toc import slugify_unicode
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BADGE_HOST = "img.shields.io"
VIEWPORTS = {
    "desktop": {"width": 1280, "height": 1000},
    "mobile": {"width": 390, "height": 844},
}
CSS_SOURCE = ROOT / "docs" / "product-page" / "readme-preview-oneirloom-v4.html"


class ImageSourceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.sources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "img":
            return
        source = dict(attrs).get("src")
        if source:
            self.sources.append(html.unescape(source))


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def extract_preview_css() -> str:
    source = CSS_SOURCE.read_text(encoding="utf-8")
    match = re.search(r"<style>(.*?)</style>", source, flags=re.DOTALL | re.IGNORECASE)
    if not match:
        raise RuntimeError(f"No style block in {CSS_SOURCE}")
    shared = match.group(1)
    additions = """
main > div[align="center"] h1 { border: none; }
main > div[align="center"] p img[src^="https://img.shields.io/"] {
  display: inline-block; width: auto; height: 20px; max-width: 100%;
}
"""
    return shared + additions


def render_markdown(source_path: Path, language: str, css: str) -> str:
    source = source_path.read_text(encoding="utf-8")
    renderer = Markdown(
        extensions=["tables", "fenced_code", "md_in_html", "toc"],
        extension_configs={"toc": {"slugify": slugify_unicode}},
    )
    rendered = renderer.convert(source)
    base = ROOT.as_uri().rstrip("/") + "/"
    return (
        "<!doctype html><html lang=\""
        + language
        + "\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        + "<base href=\""
        + base
        + "\"><style>"
        + css
        + "</style></head><body><main>"
        + rendered
        + "</main></body></html>"
    )


def image_sources(markdown_html: str) -> list[str]:
    parser = ImageSourceParser()
    parser.feed(markdown_html)
    base = ROOT.as_uri().rstrip("/") + "/"
    result: list[str] = []
    for source in parser.sources:
        resolved = urllib.parse.urljoin(base, html.unescape(source))
        if urllib.parse.urlsplit(resolved).hostname == BADGE_HOST and resolved not in result:
            result.append(resolved)
    return result


def fetch_badges_once(urls: list[str]) -> tuple[dict[str, bytes], list[dict[str, object]]]:
    payloads: dict[str, bytes] = {}
    records: list[dict[str, object]] = []
    for url in urls:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Oneirloom README badge preview"},
        )
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                status = response.status
                body = response.read(1_000_000)
        except urllib.error.HTTPError as error:
            if error.code in (401, 403, 429):
                raise RuntimeError(f"Badge request stopped after HTTP {error.code}: {url}") from error
            raise RuntimeError(f"Badge request failed with HTTP {error.code}: {url}") from error
        except (TimeoutError, urllib.error.URLError) as error:
            raise RuntimeError(f"Badge request failed without retry: {url}: {error}") from error
        if status != 200:
            raise RuntimeError(f"Badge request returned HTTP {status}: {url}")
        try:
            root = ET.fromstring(body)
        except ET.ParseError as error:
            raise RuntimeError(f"Badge response is not valid SVG: {url}") from error
        if not root.tag.endswith("svg"):
            raise RuntimeError(f"Badge response root is not SVG: {url}")
        svg_label = " ".join(root.get("aria-label", "").split())
        if not svg_label:
            text_labels = [
                " ".join(" ".join(node.itertext()).split())
                for node in root.iter()
                if node.tag.rsplit("}", 1)[-1] == "text"
            ]
            svg_label = " ".join(label for label in text_labels if label)
        if not svg_label:
            raise RuntimeError(f"Badge SVG has no readable label: {url}")
        svg_text = " ".join([svg_label, *root.itertext()]).casefold()
        error_labels = (
            "badge error",
            "service unavailable",
            "internal server error",
            "bad gateway",
            "rate limit",
            "invalid response",
            "could not fetch",
        )
        matched_errors = [label for label in error_labels if label in svg_text]
        if matched_errors:
            raise RuntimeError(f"Badge SVG contains a service-error label {matched_errors}: {url}")
        payloads[url] = body
        records.append(
            {
                "url": url,
                "http_status": status,
                "bytes": len(body),
                "svg_label": svg_label,
                "service_error_label": False,
            }
        )
    return payloads, records


def source_file_status(source: str) -> dict[str, object]:
    parsed = urllib.parse.urlsplit(source)
    if parsed.scheme or parsed.netloc or source.startswith("data:"):
        return {"src": source, "relative": False, "exists": None}
    path = (ROOT / urllib.parse.unquote(parsed.path)).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError:
        return {"src": source, "relative": True, "exists": False, "outside_root": True}
    return {"src": source, "relative": True, "exists": path.is_file()}


def browser_checks(page, expected_x_href: str, expected_x_alt: str, expected_xhs_href: str, expected_xhs_alt: str, expected_badges: int) -> dict[str, object]:
    return page.evaluate(
        """({ expectedXHref, expectedXAlt, expectedXhsHref, expectedXhsAlt, expectedBadges }) => {
          const header = document.querySelector('main > div[align="center"]');
          const images = Array.from(document.images).map((img) => ({
            src: img.getAttribute('src') || '',
            complete: img.complete,
            naturalWidth: img.naturalWidth,
            naturalHeight: img.naturalHeight
          }));
          const headerBadges = header ? Array.from(header.querySelectorAll('img')) : [];
          const internalLinks = Array.from(document.querySelectorAll('a[href^="#"]')).map((a) => {
            const fragment = decodeURIComponent(a.getAttribute('href').slice(1));
            return { href: a.getAttribute('href'), target: fragment, exists: !!document.getElementById(fragment) };
          });
          const xhsLinks = header ? Array.from(header.querySelectorAll('a')).filter((a) => {
            const img = a.querySelector('img');
            return img && /xiaohongshu/i.test(img.getAttribute('src') || '');
          }) : [];
          const xLinks = header ? Array.from(header.querySelectorAll('a')).filter((a) => {
            const img = a.querySelector('img');
            const href = a.getAttribute('href') || '';
            const alt = img ? img.getAttribute('alt') || '' : '';
            return /^https?:\/\/(?:www\.)?(?:x\.com|twitter\.com)\//i.test(href) || /^X(?:\s|$|[-_])/i.test(alt);
          }) : [];
          const repoBadgeTargets = header ? Array.from(header.querySelectorAll('a img')).filter((img) => {
            return ['GitHub stars', 'GitHub forks', 'GitHub watchers'].includes(img.getAttribute('alt'));
          }).map((img) => ({ alt: img.getAttribute('alt'), href: img.parentElement.getAttribute('href') })) : [];
          const textItems = header ? Array.from(header.querySelectorAll('h1,p,a')).filter((el) => {
            return !!((el.innerText || '').trim());
          }).map((el) => {
            const rect = el.getBoundingClientRect();
            let clipped = false;
            for (let node = el; node && node !== header.parentElement; node = node.parentElement) {
              const style = getComputedStyle(node);
              if (style.overflowX === 'hidden' || style.overflowY === 'hidden' || style.overflow === 'hidden') {
                const clip = node.getBoundingClientRect();
                if (rect.left < clip.left - 1 || rect.right > clip.right + 1 || rect.top < clip.top - 1 || rect.bottom > clip.bottom + 1) clipped = true;
              }
            }
            return { text: (el.innerText || '').trim(), visible: rect.width > 0 && rect.height > 0, clipped };
          }) : [];
          const h1 = header && header.querySelector('h1');
          const headerRect = header ? header.getBoundingClientRect() : null;
          const xhs = xhsLinks[0] || null;
          const x = xLinks[0] || null;
          return {
            viewport: { width: innerWidth, height: innerHeight },
            document: { clientWidth: document.documentElement.clientWidth, scrollWidth: document.documentElement.scrollWidth },
            header: header ? {
              badgeCount: headerBadges.length,
              scrollWidth: header.scrollWidth,
              clientWidth: header.clientWidth,
              left: headerRect.left,
              right: headerRect.right,
              h1BorderBottomStyle: h1 ? getComputedStyle(h1).borderBottomStyle : null
            } : null,
            allImages: images,
            headerBadgesLoaded: headerBadges.length === expectedBadges && headerBadges.every((img) => img.complete && img.naturalWidth > 0 && img.naturalHeight > 0),
            headerText: textItems,
            headerTextReadable: textItems.length > 0 && textItems.every((item) => item.visible && !item.clipped),
            internalLinks,
            internalAnchorsValid: internalLinks.every((link) => link.exists),
            repoBadgeTargets,
            repoBadgeTargetsValid: repoBadgeTargets.length === 3 && repoBadgeTargets.some((item) => item.alt === 'GitHub stars' && item.href === 'https://github.com/PigeonAI-Yang/oneirloom/stargazers') && repoBadgeTargets.some((item) => item.alt === 'GitHub forks' && item.href === 'https://github.com/PigeonAI-Yang/oneirloom/forks') && repoBadgeTargets.some((item) => item.alt === 'GitHub watchers' && item.href === 'https://github.com/PigeonAI-Yang/oneirloom/watchers'),
            xhsHref: xhs ? xhs.getAttribute('href') : null,
            xhsAlt: xhs && xhs.querySelector('img') ? xhs.querySelector('img').getAttribute('alt') : null,
            xhsHrefExact: !!xhs && xhs.getAttribute('href') === expectedXhsHref,
            xhsAltExact: !!xhs && xhs.querySelector('img').getAttribute('alt') === expectedXhsAlt,
            xHref: x ? x.getAttribute('href') : null,
            xAlt: x && x.querySelector('img') ? x.querySelector('img').getAttribute('alt') : null,
            xBadgeUnique: xLinks.length === 1,
            xHrefExact: !!x && x.getAttribute('href') === expectedXHref,
            xAltExact: !!x && x.querySelector('img').getAttribute('alt') === expectedXAlt,
            horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
            headerHorizontalOverflow: !!header && header.scrollWidth > header.clientWidth,
            headerWithinViewport: !!header && headerRect.left >= -1 && headerRect.right <= innerWidth + 1,
            headerH1BorderRemoved: !!h1 && getComputedStyle(h1).borderBottomStyle === 'none'
          };
        }""",
        {"expectedXHref": expected_x_href, "expectedXAlt": expected_x_alt, "expectedXhsHref": expected_xhs_href, "expectedXhsAlt": expected_xhs_alt, "expectedBadges": expected_badges},
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    css = extract_preview_css()
    inputs = {
        "zh": (ROOT / "README.md", "zh-CN"),
        "en": (ROOT / "README.en.md", "en"),
    }
    rendered: dict[str, str] = {}
    for language, (source_path, html_language) in inputs.items():
        rendered[language] = render_markdown(source_path, html_language, css)
        (OUT / f"{language}.html").write_text(rendered[language], encoding="utf-8", newline="")

    badge_urls: list[str] = []
    for content in rendered.values():
        for url in image_sources(content):
            if url not in badge_urls:
                badge_urls.append(url)
    if len(badge_urls) != 10:
        raise RuntimeError(f"Expected ten unique badge endpoints, found {len(badge_urls)}")
    badge_payloads, badge_records = fetch_badges_once(badge_urls)

    page_records: list[dict[str, object]] = []
    unexpected_remote: list[str] = []
    requested_badges: set[str] = set()
    browser_errors: list[str] = []
    x_href = "https://x.com/KimbomArtist"
    x_alt = "X KimbomArtist"
    xhs_href = "https://www.xiaohongshu.com/user/profile/689af6b90000000019016082"
    source_hashes = {name: sha256(path.read_bytes()) for name, (path, _) in inputs.items()}

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        for language in ("zh", "en"):
            for viewport_name, viewport in VIEWPORTS.items():
                context = browser.new_context(
                    viewport=viewport,
                    device_scale_factor=1,
                    is_mobile=viewport_name == "mobile",
                    has_touch=viewport_name == "mobile",
                )
                page = context.new_page()
                page.on("pageerror", lambda error: browser_errors.append(str(error)))

                def route_request(route) -> None:
                    request_url = route.request.url
                    parsed = urllib.parse.urlsplit(request_url)
                    if parsed.hostname == BADGE_HOST:
                        body = badge_payloads.get(request_url)
                        if body is None:
                            unexpected_remote.append(request_url)
                            route.abort()
                            return
                        requested_badges.add(request_url)
                        route.fulfill(status=200, content_type="image/svg+xml", body=body)
                        return
                    if parsed.scheme in ("http", "https"):
                        unexpected_remote.append(request_url)
                        route.abort()
                        return
                    route.continue_()

                page.route("**/*", route_request)
                page.goto((OUT / f"{language}.html").as_uri(), wait_until="load")
                page.wait_for_function("Array.from(document.images).every((img) => img.complete)", timeout=25000)
                xhs_alt = "Xiaohongshu Dibo" if language == "en" else "小红书 Dibo"
                checks = browser_checks(page, x_href, x_alt, xhs_href, xhs_alt, 10)
                relative_status = [
                    source_file_status(str(image["src"]))
                    for image in checks["allImages"]
                    if isinstance(image, dict) and str(image["src"]) and not urllib.parse.urlsplit(str(image["src"])).scheme and not str(image["src"]).startswith("data:")
                ]
                relative_ok = all(
                    bool(item["exists"])
                    and next(
                        (bool(image["complete"] and image["naturalWidth"] > 0) for image in checks["allImages"] if image["src"] == item["src"]),
                        False,
                    )
                    for item in relative_status
                )
                checks["relativeImagePaths"] = relative_status
                checks["relativeImagesExistAndLoaded"] = relative_ok
                checks["allImagesLoaded"] = all(
                    bool(image["complete"] and image["naturalWidth"] > 0)
                    for image in checks["allImages"]
                )
                screenshot_name = f"{language}-{viewport_name}.png"
                page.screenshot(path=str(OUT / screenshot_name), full_page=False)
                page_records.append(
                    {
                        "language": language,
                        "viewport_name": viewport_name,
                        "checks": checks,
                        "screenshot": screenshot_name,
                    }
                )
                context.close()
        browser.close()

    expected_pages = len(inputs) * len(VIEWPORTS)
    all_pages_ok = len(page_records) == expected_pages and all(
        record["checks"][key]
        for record in page_records
        for key in (
            "headerBadgesLoaded",
            "headerTextReadable",
            "internalAnchorsValid",
            "repoBadgeTargetsValid",
            "xhsHrefExact",
            "xhsAltExact",
            "xBadgeUnique",
            "xHrefExact",
            "xAltExact",
            "horizontalOverflow",
            "headerHorizontalOverflow",
            "headerWithinViewport",
            "headerH1BorderRemoved",
            "relativeImagesExistAndLoaded",
            "allImagesLoaded",
        )
        if key not in ("horizontalOverflow", "headerHorizontalOverflow")
    ) and all(
        not record["checks"][key]
        for record in page_records
        for key in ("horizontalOverflow", "headerHorizontalOverflow")
    )
    if unexpected_remote:
        all_pages_ok = False
    if browser_errors:
        all_pages_ok = False
    if requested_badges != set(badge_urls):
        all_pages_ok = False

    receipt = {
        "result": "passed" if all_pages_ok else "failed",
        "rendering_scope": "Local Markdown and Chromium preview; hosted GitHub rendering was not checked.",
        "source_sha256": source_hashes,
        "css_source": str(CSS_SOURCE.relative_to(ROOT)).replace("\\", "/"),
        "preview_html": ["zh.html", "en.html"],
        "badge_endpoints_fetched_once": badge_records,
        "browser_badge_requests_fulfilled_from_memory": len(requested_badges),
        "unexpected_remote_requests": unexpected_remote,
        "browser_errors": browser_errors,
        "pages": page_records,
    }
    (OUT / "verification.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="",
    )
    print(f"result={receipt['result']} pages={len(page_records)} badge_endpoints={len(badge_records)} browser_badges={len(requested_badges)}")
    if not all_pages_ok:
        raise SystemExit("README preview verification did not pass; see verification.json")


if __name__ == "__main__":
    main()
