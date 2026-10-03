from pathlib import Path
from hashlib import sha256
import html
import json
import re
from urllib.parse import unquote
import markdown
from markdown.extensions.toc import slugify_unicode
from playwright.sync_api import sync_playwright
from PIL import Image

WORK = Path(__file__).resolve().parent
PUB = WORK / 'publish-checkout'
report = json.loads((PUB / 'docs/image-compression.json').read_text(encoding='utf-8'))
for row in report['records']:
    path = PUB / row['published']
    assert sha256(path.read_bytes()).hexdigest() == row['published_sha256'], path
    with Image.open(path) as im:
        assert im.format == 'WEBP'
for path in (PUB / 'docs/portrait-evidence').glob('*.json'):
    data = json.loads(path.read_text(encoding='utf-8'))
    row = next(r for r in report['records'] if r['published'] == f'docs/assets/tutorial-originals/{path.stem}.webp')
    data['published_image'] = row['published']
    data['published_sha256'] = row['published_sha256']
    data['publication_encoding'] = 'WebP quality 87; original dimensions preserved. Historical source paths describe the author workspace.'
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
case = PUB / 'skills/oneirloom-style-photography/templates/indoor-full-length/example-01.json'
case.write_text(case.read_text(encoding='utf-8').replace('work/article-tutorial/evidence/01_full.json', 'docs/portrait-evidence/01_full.json'), encoding='utf-8')
readme_path = PUB / 'README.md'
source = readme_path.read_text(encoding='utf-8').replace('整个教程保留 62 张生成原图', '教程案例包含 62 张生成结果')
readme_path.write_text(source, encoding='utf-8')
missing = []
refs_count = 0
for path in PUB.rglob('*.md'):
    if 'official' in path.parts or 'oneirloom-prompt-card' in path.parts:
        continue
    text = re.sub(r'```.*?```', '', path.read_text(encoding='utf-8'), flags=re.S)
    refs = re.findall(r'\]\(([^)]+)\)', text) + re.findall(r'(?:src|href)="([^"]+)"', text)
    for ref in refs:
        if ref.startswith(('http:', 'https:', '#', 'mailto:')) or '<' in ref:
            continue
        target = unquote(ref.split('#')[0])
        refs_count += 1
        if not (path.parent / target).exists():
            missing.append([str(path.relative_to(PUB)), ref])
assert not missing, missing
body = markdown.markdown(source.replace('<details>', '<details markdown="1">'), extensions=['tables', 'fenced_code', 'md_in_html', 'toc'], extension_configs={'toc': {'slugify': slugify_unicode}})
css = re.search(r'<style>(.*?)</style>', (WORK / 'preview.html').read_text(encoding='utf-8'), re.S).group(1)
page_html = '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><base href="' + html.escape(PUB.as_uri() + '/', quote=True) + '"><style>' + css + '</style></head><body><main>' + body + '</main></body></html>'
preview = WORK / 'publication-preview.html'
preview.write_text(page_html, encoding='utf-8')
checks = {'local_references_checked': refs_count, 'missing': missing, 'compressed_image_hashes_verified': report['all_images']}
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 1080})
    page.goto(preview.as_uri(), wait_until='load')
    loaded = page.locator('img').evaluate_all('(items)=>items.map(i=>i.complete&&i.naturalWidth>0)')
    assert len(loaded) == 18 and all(loaded), loaded
    checks['homepage_images_loaded'] = len(loaded)
    page.screenshot(path=str(WORK / 'publication-desktop.png'))
    page.locator('table').first.screenshot(path=str(WORK / 'publication-faces.png'))
    page.locator('table').nth(3).screenshot(path=str(WORK / 'publication-light.png'))
    page.get_by_text('展开全部技能', exact=True).click()
    assert page.locator('details table tbody tr').count() == 14
    page.set_viewport_size({'width': 390, 'height': 844})
    page.goto(preview.as_uri(), wait_until='load')
    checks['mobile'] = page.evaluate('({viewport:innerWidth,page:document.documentElement.scrollWidth})')
    assert checks['mobile']['page'] <= checks['mobile']['viewport']
    browser.close()
(WORK / 'publication-verification.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(checks, ensure_ascii=False))
