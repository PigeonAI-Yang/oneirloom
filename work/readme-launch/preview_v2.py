from pathlib import Path
from hashlib import sha256
import html
import json
import re
import markdown
from markdown.extensions.toc import slugify_unicode
from playwright.sync_api import sync_playwright
from PIL import Image

WORK = Path(__file__).resolve().parent
ROOT = WORK.parents[1]
source = (ROOT / 'README.md').read_text(encoding='utf-8')
body = markdown.markdown(source.replace('<details>', '<details markdown="1">'), extensions=['tables', 'fenced_code', 'md_in_html', 'toc'], extension_configs={'toc': {'slugify': slugify_unicode}})
existing = (WORK / 'preview.html').read_text(encoding='utf-8')
css = re.search(r'<style>(.*?)</style>', existing, re.S).group(1)
css += 'td img{width:auto;max-width:100%;max-height:560px;margin:8px auto 18px}td{vertical-align:middle}table:has(img){display:table;table-layout:fixed}table:has(img) td{min-width:0}table:has(img) tr{background:white}main>p:first-child img{margin-top:0}@media(max-width:650px){table:has(img) td{padding:8px;font-size:12px;line-height:1.6}td img{max-height:240px}table:has(img) strong{font-size:12px}}'
base = html.escape(ROOT.as_uri() + '/', quote=True)
page_html = '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><base href="'+base+'"><title>织梦师 · Oneirloom</title><style>'+css+'</style></head><body><main>'+body+'</main></body></html>'
(WORK / 'preview.html').write_text(page_html, encoding='utf-8')
refs = re.findall(r'\]\(([^)]+)\)', source) + re.findall(r'(?:src|href)="([^"]+)"', source)
missing = [r for r in refs if not r.startswith(('https://', '#')) and not (ROOT / r).exists()]
assert not missing, missing
old = json.loads((WORK / 'assets-manifest.json').read_text(encoding='utf-8'))
for record in old['source_artwork'].values():
    assert sha256((ROOT / record['path']).read_bytes()).hexdigest() == record['sha256']
checks = {'local_references_checked': len(refs), 'missing_local_references': missing, 'archived_case_art_unchanged': True, 'new_promotion_images': {}, 'generation_tool': 'built-in image_gen', 'hosted_github': 'Not published or remotely tested'}
for name in ['hero-v2.png', 'workflow-v2.png', 'prompt-anatomy-v2.png']:
    asset = ROOT / 'docs/assets' / name
    checks['new_promotion_images'][name] = {'size_px': Image.open(asset).size, 'sha256': sha256(asset.read_bytes()).hexdigest()}
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width':1440,'height':1080})
    page.goto((WORK / 'preview.html').as_uri(), wait_until='load')
    images = page.locator('img').evaluate_all('(items)=>items.map(i=>({src:i.getAttribute("src"),loaded:i.complete&&i.naturalWidth>0}))')
    assert len(images) == 9 and all(i['loaded'] for i in images), images
    anchors = page.locator('a[href^="#"]').evaluate_all('(items)=>items.map(a=>({href:a.getAttribute("href"),exists:!!document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1)))}))')
    assert all(a['exists'] for a in anchors), anchors
    page.get_by_text('展开全部技能', exact=True).click()
    assert page.locator('details table tbody tr').count() == 14
    page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(WORK / 'desktop-top-v2.png'))
    page.screenshot(path=str(WORK / 'desktop-full-v2.png'), full_page=True)
    page.locator('table').first.screenshot(path=str(WORK / 'gallery-v2.png'))
    page.locator('img[src$="workflow-v2.png"]').screenshot(path=str(WORK / 'workflow-page-v2.png'))
    checks['desktop'] = {'loaded_images':images,'anchors':anchors,'skill_rows':14}
    page.set_viewport_size({'width':390,'height':844})
    page.goto((WORK / 'preview.html').as_uri(), wait_until='load')
    sizes = page.evaluate('({viewport:innerWidth,page:document.documentElement.scrollWidth})')
    assert sizes['page'] <= sizes['viewport'], sizes
    page.screenshot(path=str(WORK / 'mobile-top-v2.png'))
    page.locator('table').first.screenshot(path=str(WORK / 'gallery-mobile-v2.png'))
    checks['mobile'] = sizes
    browser.close()
(WORK / 'verification.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(checks, ensure_ascii=False))
