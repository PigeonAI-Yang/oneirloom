import hashlib
import json
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright


def main():
    directory = Path(__file__).resolve().parent
    root = directory.parent.parent
    assets = root / 'docs' / 'assets' / 'product-page'
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
        page = browser.new_page(viewport={'width': 1254, 'height': 1254}, device_scale_factor=1)
        page.goto((directory / 'portraits-native-v4.html').as_uri(), wait_until='load')
        page.evaluate('document.fonts.ready')
        page.locator('img').evaluate_all('(items) => Promise.all(items.map(image => image.decode()))')
        footer_bottom = page.locator('.footer').evaluate('(element) => element.getBoundingClientRect().bottom')
        if footer_bottom > 1254:
            raise RuntimeError('Portrait panel footer is clipped')
        page.screenshot(path=str(assets / '03-portraits-native-v4.png'))
        page.goto((directory / 'index-oneirloom-v4.html').as_uri(), wait_until='load')
        page.locator('img').evaluate_all('(items) => Promise.all(items.map(image => image.decode()))')
        if page.locator('main img').count() != 7:
            raise RuntimeError('The product page requires all seven panels')
        page.screenshot(path=str(assets / 'overview-oneirloom-v4.png'), full_page=True)
        names = page.locator('main img').evaluate_all('(items) => items.map(image => image.getAttribute("src").split("/").pop())')
        page.set_viewport_size({'width': 390, 'height': 844})
        if page.evaluate('document.documentElement.scrollWidth') != 390:
            raise RuntimeError('Product page overflows the mobile viewport')
        page.screenshot(path=str(assets / 'mobile-oneirloom-v4.png'))
        browser.close()
    records = []
    for name in names:
        path = assets / name
        with Image.open(path) as image:
            size = image.size
            image.save(path.with_suffix('.webp'), quality=92, method=6)
        records.append({'file': name, 'size': size, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'kind': 'archived-photo native layout' if name.startswith('03-') else 'reference-conditioned generated promotional artwork'})
    (assets / 'selection-oneirloom-v4.json').write_text(json.dumps({'panels': records, 'panelCount': 7, 'allImagesLoaded': True, 'mobileWidth': 390, 'imageInspected': False, 'portraitGeneration': 'Output rejected by service safety review; native archived-photo layout selected', 'remotePublication': 'Not published'}, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'panels': len(records), 'overview': str(assets / 'overview-oneirloom-v4.png')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
