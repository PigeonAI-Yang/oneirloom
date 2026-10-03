from pathlib import Path
from hashlib import sha256
import json
from playwright.sync_api import sync_playwright

WORK = Path(__file__).resolve().parent
ROOT = WORK.parents[1]
manifest = json.loads((WORK / 'assets-manifest.json').read_text(encoding='utf-8'))
for record in manifest['source_artwork'].values():
    assert sha256((ROOT / record['path']).read_bytes()).hexdigest() == record['sha256']
assert (ROOT / 'README.en.md').read_bytes() == (WORK / 'README.before.md').read_bytes()
checks = {}
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 1080}, device_scale_factor=1)
    page.goto((WORK / 'preview.html').as_uri(), wait_until='load')
    image_status = page.locator('img').evaluate_all('(items) => items.map(i => ({src:i.getAttribute("src"),loaded:i.complete && i.naturalWidth>0}))')
    assert len(image_status) == 5 and all(i['loaded'] for i in image_status), image_status
    anchors = page.locator('a[href^="#"]').evaluate_all('(items) => items.map(a => ({href:a.getAttribute("href"),exists:!!document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1)))}))')
    assert all(a['exists'] for a in anchors), anchors
    page.locator('summary').click()
    assert page.locator('details table tbody tr').count() == 14
    page.evaluate('window.scrollTo(0, 0)')
    page.screenshot(path=str(WORK / 'desktop-top.png'))
    page.screenshot(path=str(WORK / 'desktop-full.png'), full_page=True)
    for name in ['showcase', 'product-case', 'workflow', 'prompt-anatomy']:
        page.locator(f'img[src$="{name}.png"]').screenshot(path=str(WORK / f'page-{name}.png'))
    checks['desktop'] = {'images': image_status, 'navigation': anchors, 'skill_rows': 14}
    page.set_viewport_size({'width': 390, 'height': 844})
    page.goto((WORK / 'preview.html').as_uri(), wait_until='load')
    sizes = page.evaluate('({viewport:innerWidth,page:document.documentElement.scrollWidth})')
    assert sizes['page'] <= sizes['viewport'], sizes
    page.screenshot(path=str(WORK / 'mobile-top.png'))
    checks['mobile'] = sizes
    checks['chromium_version'] = browser.version
    browser.close()
checks['source_artwork_unchanged'] = True
checks['english_overview_preserved'] = True
checks['hosted_github_rendering'] = 'Not published or tested remotely; local Markdown rendering inspected.'
(WORK / 'verification.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(checks, ensure_ascii=False))
