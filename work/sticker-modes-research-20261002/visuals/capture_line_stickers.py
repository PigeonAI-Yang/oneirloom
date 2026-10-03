import asyncio
import re
import time
from pathlib import Path

from playwright.async_api import async_playwright


ROOT = Path(__file__).resolve().parent
EDGE = Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
PROXY = "http://127.0.0.1:17890"
PRODUCT_IDS = [
    "1000560",
    "1094842",
    "31275612",
    "26448605",
    "31019125",
    "30812091",
    "32815343",
    "31434473",
]
DENIAL_TEXT = re.compile(
    r"access denied|request blocked|too many requests|rate limit|temporarily blocked|"
    r"verify you are human|authentication required|log in to continue|sign in to continue",
    re.IGNORECASE,
)


INSPECT_PAGE = r"""() => {
    const clean = value => (value || '').replace(/\s+/g, ' ').trim();
    const cssPath = element => {
        const parts = [];
        let current = element;
        while (current && current.nodeType === 1 && current !== document.body) {
            let part = current.tagName.toLowerCase();
            if (current.id) {
                part += `#${CSS.escape(current.id)}`;
                parts.unshift(part);
                break;
            }
            const siblings = [...current.parentElement.children].filter(item => item.tagName === current.tagName);
            if (siblings.length > 1) part += `:nth-of-type(${siblings.indexOf(current) + 1})`;
            parts.unshift(part);
            current = current.parentElement;
        }
        return ['body', ...parts].join('>');
    };
    const candidates = [...document.querySelectorAll('main,section,ul,ol,div')]
        .map(element => {
            const images = [...element.querySelectorAll('img')];
            const box = element.getBoundingClientRect();
            const identity = `${element.id || ''} ${typeof element.className === 'string' ? element.className : ''}`;
            const galleryHint = /gallery|sticker|emoji|preview|item|image|thumb/i.test(identity) ? 1000 : 0;
            const listHint = /^(UL|OL)$/.test(element.tagName) ? 100 : 0;
            return {element, images, box, score: images.length * 10 + galleryHint + listHint};
        })
        .filter(candidate => candidate.images.length >= 2 && candidate.box.width >= 200 && candidate.box.height >= 80)
        .sort((a, b) => b.score - a.score || (a.box.width * a.box.height) - (b.box.width * b.box.height));
    const gallery = candidates[0] || null;
    const creatorSelectors = [
        'a[href*="/author/"]', 'a[href*="/artist/"]', 'a[href*="creator"]',
        '[class*="Artist"] a', '[class*="artist"] a', '[class*="Creator"] a',
        '[class*="creator"] a', '[class*="Author"] a', '[class*="author"] a'
    ];
    let creator = null;
    for (const selector of creatorSelectors) {
        const found = [...document.querySelectorAll(selector)].map(element => clean(element.innerText)).find(Boolean);
        if (found && found.length < 120) { creator = found; break; }
    }
    if (!creator) {
        const heading = document.querySelector('h1');
        const scope = heading && (heading.closest('section,main,article,div') || heading.parentElement);
        if (scope) {
            const found = [...scope.querySelectorAll('a')].map(element => clean(element.innerText)).find(text => text && text !== clean(heading.innerText) && text.length < 120);
            if (found) creator = found;
        }
    }
    const bodyText = clean(document.body?.innerText || '').slice(0, 1800);
    return {
        title: document.title || null,
        productTitle: clean(document.querySelector('h1')?.innerText || '') || null,
        creator,
        bodyText,
        pageHeight: Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0),
        imageCount: document.images.length,
        gallerySelector: gallery ? cssPath(gallery.element) : null,
        galleryIdentity: gallery ? `${gallery.element.tagName.toLowerCase()}${gallery.element.id ? `#${gallery.element.id}` : ''}${typeof gallery.element.className === 'string' && gallery.element.className.trim() ? `.${gallery.element.className.trim().split(/\s+/).slice(0, 5).join('.')}` : ''}` : null,
        galleryCount: gallery ? gallery.images.length : 0,
        galleryLoaded: gallery ? gallery.images.filter(image => image.complete && image.naturalWidth > 0).length : 0,
        galleryImages: gallery ? gallery.images.slice(0, 8).map(image => ({alt: clean(image.alt), complete: image.complete, naturalWidth: image.naturalWidth, naturalHeight: image.naturalHeight, src: image.currentSrc || image.src})) : [],
        loadedImages: [...document.images].filter(image => image.complete && image.naturalWidth > 0).length
    };
}"""


async def write_receipt(rows, stop_reason):
    previous_path = ROOT / "collection-receipt.md"
    previous = previous_path.read_text(encoding="utf-8") if previous_path.exists() else "# LINE sticker-mode visual collection receipt\n"
    lines = [
        "\n\n## Proxy-enabled capture run",
        "",
        "- Attempt date: 2026-10-02",
        f"- Browser: installed Microsoft Edge via isolated headless Python Playwright; explicit proxy `{PROXY}`.",
        f"- Stop reason: {stop_reason or 'all eight one-time page navigations completed.'}",
        "- Each listed product URL was navigated at most once. Gallery images were loaded by the page; no image files were separately downloaded.",
        "",
        "| Product ID | HTTP status | Page title | Product title | Creator | Gallery images loaded | Screenshot | Outcome |",
        "| --- | ---: | --- | --- | --- | ---: | --- | --- |",
    ]
    for row in rows:
        page = row.get("page", {})
        vals = [
            row["id"],
            str(row.get("status") or "Unavailable"),
            page.get("title") or "Unavailable",
            page.get("productTitle") or "Unavailable",
            page.get("creator") or "Unavailable",
            f"{page.get('galleryLoaded', 0)}/{page.get('galleryCount', 0)}",
            row.get("screenshot") or "None",
            row.get("outcome", "unvisited"),
        ]
        lines.append("| " + " | ".join(str(value).replace("|", "\\|").replace("\n", " ") for value in vals) + " |")
    if rows:
        lines.extend(["", "Captured gallery selector and render evidence:", ""])
        for row in rows:
            page = row.get("page", {})
            if page:
                lines.append(f"- `{row['id']}`: selector `{page.get('gallerySelector') or 'none'}` ({page.get('galleryIdentity') or 'no gallery candidate'}); loaded page images {page.get('loadedImages', 0)}/{page.get('imageCount', 0)}; viewport 1280×1000 at device scale 1.")
            elif row.get("error"):
                lines.append(f"- `{row['id']}`: navigation error `{row['error']}`.")
    previous_path.write_text(previous.rstrip() + "\n" + "\n".join(lines) + "\n", encoding="utf-8")


async def main():
    rows = []
    stop_reason = None
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(
            executable_path=str(EDGE),
            headless=True,
            proxy={"server": PROXY},
        )
        try:
            context = await browser.new_context(viewport={"width": 1280, "height": 1000}, device_scale_factor=1)
            try:
                page = await context.new_page()
                for index, product_id in enumerate(PRODUCT_IDS):
                    url = f"https://store.line.me/stickershop/product/{product_id}/en"
                    row = {"id": product_id, "url": url, "outcome": "unvisited"}
                    rows.append(row)
                    try:
                        response = await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                    except Exception as error:
                        message = str(error).replace("\n", " ")
                        row.update(outcome="navigation error", error=message)
                        stop_reason = f"Stopped on `{product_id}` after its single navigation failed: {message}"
                        break
                    row["status"] = response.status if response else None
                    render_deadline = time.monotonic() + 10
                    try:
                        await page.evaluate("""async () => {
                            const height = Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0);
                            const step = Math.max(400, Math.floor(innerHeight * 0.75));
                            const maxSteps = Math.min(32, Math.ceil(height / step));
                            for (let index = 0; index < maxSteps; index++) {
                                window.scrollTo(0, Math.min(height, index * step));
                                await new Promise(resolve => setTimeout(resolve, 35));
                            }
                            window.scrollTo(0, 0);
                        }""")
                        remaining = render_deadline - time.monotonic()
                        if remaining > 0:
                            try:
                                await page.wait_for_function(
                                    "Array.from(document.images).length > 0 && Array.from(document.images).every(image => image.complete)",
                                    timeout=int(remaining * 1000),
                                )
                            except Exception:
                                pass
                    except Exception:
                        pass
                    page_data = await page.evaluate(INSPECT_PAGE)
                    row["page"] = page_data
                    page_text = page_data.get("bodyText", "")
                    blocked = row["status"] in (401, 403, 429) or DENIAL_TEXT.search(page_data.get("title") or "") or DENIAL_TEXT.search(page_text)
                    if blocked:
                        row["outcome"] = "authentication/access/rate page; stopped"
                        stop_reason = f"Stopped on `{product_id}` after detecting HTTP {row['status']} or an authentication/access/rate page."
                        break
                    row["outcome"] = "loaded"
                    if page_data.get("galleryLoaded", 0) > 0:
                        name = f"line-{product_id}.png"
                        if page_data.get("pageHeight", 0) <= 14000:
                            await page.screenshot(path=str(ROOT / name), full_page=True)
                        elif page_data.get("gallerySelector"):
                            await page.locator(page_data["gallerySelector"]).screenshot(path=str(ROOT / name))
                        else:
                            row["outcome"] = "page loaded; no bounded gallery selector for tall page"
                            name = None
                        if name:
                            row["screenshot"] = f"work/sticker-modes-research-20261002/visuals/{name}"
                    else:
                        row["outcome"] = "page loaded; no gallery image with naturalWidth > 0; screenshot omitted"
            finally:
                await context.close()
        finally:
            await browser.close()
    await write_receipt(rows, stop_reason)
    print(f"stop_reason={stop_reason or 'all eight one-time page navigations completed'}")
    for row in rows:
        page = row.get("page", {})
        print({
            "id": row["id"],
            "status": row.get("status"),
            "title": page.get("title"),
            "productTitle": page.get("productTitle"),
            "creator": page.get("creator"),
            "galleryLoaded": f"{page.get('galleryLoaded', 0)}/{page.get('galleryCount', 0)}",
            "screenshot": row.get("screenshot"),
            "outcome": row.get("outcome"),
            "error": row.get("error"),
        })


asyncio.run(main())
