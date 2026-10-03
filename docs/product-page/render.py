import hashlib
import html
import json
from pathlib import Path
import re

import markdown
from markdown.extensions.toc import slugify_unicode
from PIL import Image
from playwright.sync_api import sync_playwright


def main():
    source = Path(__file__).resolve().parent / 'index.html'
    output = source.parent.parent / 'assets' / 'product-page'
    output.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
        page = browser.new_page(viewport={'width': 1080, 'height': 900}, device_scale_factor=1)
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(source.as_uri(), wait_until='load')
        page.evaluate('document.fonts.ready')
        page.locator('img').evaluate_all('(images) => Promise.all(images.map(image => image.decode()))')
        images = page.locator('img').evaluate_all('(images) => images.map(image => ({src:image.getAttribute("src"), loaded:image.complete && image.naturalWidth > 0}))')
        if errors or not all(image['loaded'] for image in images):
            raise RuntimeError({'errors': errors, 'images': images})
        if page.evaluate('document.documentElement.scrollWidth') != 1080:
            raise RuntimeError('Page overflows its 1080 pixel canvas')
        panels = []
        for section in page.locator('section[data-panel]').all():
            name = section.get_attribute('data-panel')
            box = section.bounding_box()
            box['y'] += page.evaluate('window.scrollY')
            section.screenshot(path=str(output / (name + '.png')))
            with Image.open(output / (name + '.png')) as image:
                image.save(output / (name + '.webp'), quality=92, method=6)
            panels.append({'name': name, 'geometry': box})
        page.screenshot(path=str(output / 'overview.png'), full_page=True)
        root = source.parent.parent.parent
        readme = (root / 'README.md').read_text(encoding='utf-8')
        refs = re.findall(r'\]\(([^)]+)\)', readme)
        missing = [ref for ref in refs if not ref.startswith(('https://', '#')) and not (root / ref).exists()]
        if missing:
            raise RuntimeError({'missingReadmeReferences': missing})
        body = markdown.markdown(readme.replace('<details>', '<details markdown="1">'), extensions=['tables', 'fenced_code', 'md_in_html', 'toc'], extension_configs={'toc': {'slugify': slugify_unicode}})
        preview = source.parent / 'readme-preview.html'
        css = 'body{margin:0;color:#24292f;background:white;font:16px/1.7 "Microsoft YaHei",sans-serif}main{max-width:1012px;margin:auto;padding:32px}img{display:block;max-width:100%;height:auto}main>p:has(img){margin:0}a{color:#0969da}h1,h2{border-bottom:1px solid #d0d7de;padding-bottom:10px}pre{background:#f6f8fa;padding:16px;overflow:auto}table{border-collapse:collapse;display:block;overflow:auto}th,td{padding:8px 12px;border:1px solid #d0d7de}summary{cursor:pointer}@media(max-width:600px){main{padding:16px}body{font-size:14px}}'
        preview.write_text('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><base href="' + html.escape(root.as_uri() + '/') + '"><style>' + css + '</style></head><body><main>' + body + '</main></body></html>', encoding='utf-8')
        page.goto(preview.as_uri(), wait_until='load')
        page.evaluate('document.fonts.ready')
        page.locator('img').evaluate_all('(images) => Promise.all(images.map(image => image.decode()))')
        anchors = page.locator('a[href^="#"]').evaluate_all('(links) => links.map(link => ({href:link.getAttribute("href"), exists:!!document.getElementById(decodeURIComponent(link.getAttribute("href").slice(1)))}))')
        if not all(anchor['exists'] for anchor in anchors):
            raise RuntimeError({'missingAnchors': anchors})
        readme_checks = {'localReferences': len(refs), 'missingReferences': missing, 'anchors': anchors, 'viewports': []}
        for width, height, name in ((1080, 900, 'readme-desktop.png'), (390, 844, 'readme-mobile.png')):
            page.set_viewport_size({'width': width, 'height': height})
            page.evaluate('window.scrollTo(0, 0)')
            actual_width = page.evaluate('document.documentElement.scrollWidth')
            if actual_width > width:
                raise RuntimeError({'readmeOverflow': actual_width, 'viewport': width})
            page.screenshot(path=str(output / name))
            readme_checks['viewports'].append({'width': width, 'pageWidth': actual_width})
        browser.close()
    root = source.parent.parent.parent
    assets = []
    for entry in images:
        asset = (source.parent / entry['src']).resolve(strict=True)
        assets.append({'path': asset.relative_to(root).as_posix(), 'sha256': hashlib.sha256(asset.read_bytes()).hexdigest()})
    checks = {'html': source.relative_to(root).as_posix(), 'width': 1080, 'panels': panels, 'allImagesLoaded': True, 'horizontalOverflow': False, 'pageErrors': errors, 'sourceAssets': assets, 'readme': readme_checks, 'imageInspected': False}
    (output / 'render-checks.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'panels': len(panels), 'images': len(images), 'output': str(output)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
