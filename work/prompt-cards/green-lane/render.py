from pathlib import Path
import json
import re
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
EDGE = Path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
EXPECTED = re.sub(r'\s+', '', (ROOT / 'prompt.txt').read_text(encoding='utf-8'))

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(executable_path=str(EDGE), headless=True)
    for name, width, height in [('side-by-side', 3200, 2200), ('stacked', 1800, 3142)]:
        path = ROOT / f'{name}.html'
        page = browser.new_page(viewport={'width': width, 'height': height}, device_scale_factor=1)
        page.goto(path.as_uri(), wait_until='load')
        page.evaluate('document.fonts.ready')
        if name == 'side-by-side':
            for size in range(42, 31, -1):
                page.locator('.prompt').evaluate('(el, size) => el.style.fontSize = size + "px"', size)
                fits = page.evaluate('''() => {
                    const last = document.querySelector('.prompt p:last-child').getBoundingClientRect();
                    const parent = document.querySelector('.copy').getBoundingClientRect();
                    return last.bottom <= parent.bottom - 42;
                }''')
                if fits:
                    break
            html = path.read_text(encoding='utf-8')
            html = re.sub(r'font-size:32px;line-height:1\.58', f'font-size:{size}px;line-height:1.58', html)
            path.write_text(html, encoding='utf-8')
        text = page.locator('.prompt').inner_text()
        assert re.sub(r'\s+', '', text) == EXPECTED, name
        checks = page.evaluate('''() => {
            const image = document.querySelector('.artwork');
            const imageBox = image.getBoundingClientRect();
            const paragraphs = [...document.querySelectorAll('.prompt p')];
            return {
                source: [image.naturalWidth, image.naturalHeight],
                image: [imageBox.width, imageBox.height],
                font: getComputedStyle(document.querySelector('.prompt')).fontSize,
                textWithinPage: paragraphs.every(p => {
                    const r=p.getBoundingClientRect();
                    return r.left>=0 && r.top>=0 && r.right<=innerWidth && r.bottom<=innerHeight;
                })
            };
        }''')
        assert checks['textWithinPage'], checks
        assert abs(checks['image'][0] / checks['image'][1] - checks['source'][0] / checks['source'][1]) < 0.001
        page.screenshot(path=str(ROOT / f'{name}.png'), full_page=True)
        print(json.dumps({'layout': name, **checks}, ensure_ascii=False))
        page.close()
    browser.close()
