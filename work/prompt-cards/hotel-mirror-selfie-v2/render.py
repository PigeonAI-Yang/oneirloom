from pathlib import Path
import html
import json
import re
import shutil

from PIL import Image
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parents[2]
SOURCE_PHOTO = Path('J:/Users/yangda01/Temp/codex-clipboard-8918622d-c45a-4f87-b57d-46e6958666d1.png')
SOURCE_PROMPT = PROJECT / 'skills/oneirloom-style-photography/templates/hotel-mirror-selfie/current-prompt-02-zh.txt'
EDGE = Path('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
WIDTH, HEIGHT = 2400, 3200

prompt = SOURCE_PROMPT.read_text(encoding='utf-8-sig').strip()
paragraphs = re.split(r'\n\s*\n', prompt)
assert len(paragraphs) == 8
shutil.copyfile(SOURCE_PHOTO, ROOT / 'photo.png')
(ROOT / 'prompt.txt').write_text(prompt + '\n', encoding='utf-8')
columns = ''.join(
    '<div class="column">' + ''.join('<p>' + html.escape(p) + '</p>' for p in group) + '</div>'
    for group in (paragraphs[:4], paragraphs[4:])
)
document = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><title>酒店镜面全身自拍</title>
<style>
* { box-sizing: border-box; }
html, body { margin: 0; width: 2400px; background: #f7f4ef; color: #28241f; }
body { font-family: "Microsoft YaHei", sans-serif; }
.card { width: 2400px; height: 3200px; padding: 64px 80px 68px; }
.photo-area { height: 1920px; display: flex; justify-content: center; }
.photo { display: block; width: 1440px; height: 1920px; }
.heading { margin-top: 50px; padding-bottom: 24px; border-bottom: 2px solid #d5cbbd; display: flex; align-items: baseline; justify-content: space-between; }
h1 { margin: 0; font-size: 56px; line-height: 1.35; font-weight: 700; letter-spacing: 2px; }
.label { font-size: 28px; letter-spacing: 3px; color: #7a6b57; }
.prompt { margin-top: 28px; display: grid; grid-template-columns: 1fr 1fr; gap: 64px; font-size: FONT_SIZEpx; line-height: 1.55; text-align: justify; }
p { margin: 0 0 20px; }
p:last-child { margin-bottom: 0; }
</style></head><body><main class="card">
<div class="photo-area"><img class="photo" src="photo.png" alt="酒店镜面全身自拍照片"></div>
<header class="heading"><h1>酒店镜面全身自拍</h1><span class="label">完整中文提示词</span></header>
<section class="prompt">PROMPT_COLUMNS</section>
</main></body></html>'''.replace('PROMPT_COLUMNS', columns)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(executable_path=str(EDGE), headless=True)
    page = browser.new_page(viewport={'width': WIDTH, 'height': HEIGHT}, device_scale_factor=1)
    for font_size in range(38, 31, -1):
        layout = document.replace('FONT_SIZE', str(font_size))
        (ROOT / 'card.html').write_text(layout, encoding='utf-8')
        page.goto((ROOT / 'card.html').as_uri(), wait_until='load')
        page.evaluate('document.fonts.ready')
        page.locator('.photo').evaluate('(image) => image.decode()')
        checks = page.evaluate('''() => {
            const image = document.querySelector('.photo');
            const box = image.getBoundingClientRect();
            const paragraphs = [...document.querySelectorAll('.prompt p')];
            return {
                sourceSize: [image.naturalWidth, image.naturalHeight],
                displayedSize: [box.width, box.height],
                fontSize: getComputedStyle(document.querySelector('.prompt')).fontSize,
                canvasSize: [document.documentElement.scrollWidth, document.documentElement.scrollHeight],
                textBottom: Math.max(...paragraphs.map(p => p.getBoundingClientRect().bottom)),
                textInside: paragraphs.every(p => {
                    const r = p.getBoundingClientRect();
                    return r.left >= 80 && r.right <= 2320 && r.top >= 0 && r.bottom <= 3132;
                })
            };
        }''')
        if checks['textInside']:
            break
    else:
        raise RuntimeError('Complete prompt does not fit the 3:4 card')
    actual = page.locator('.prompt').inner_text()
    assert re.sub(r'\s+', '', actual) == re.sub(r'\s+', '', prompt)
    assert checks['canvasSize'] == [WIDTH, HEIGHT], checks
    assert abs(checks['displayedSize'][0] / checks['displayedSize'][1] - checks['sourceSize'][0] / checks['sourceSize'][1]) < 0.001
    page.screenshot(path=str(ROOT / 'hotel-selfie-prompt-3x4.png'), full_page=True)
    browser.close()

with Image.open(ROOT / 'hotel-selfie-prompt-3x4.png') as output:
    assert output.size == (WIDTH, HEIGHT)
    assert output.width * 4 == output.height * 3

(ROOT / 'render-checks.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(checks, ensure_ascii=False))
print(str(ROOT / 'hotel-selfie-prompt-3x4.png'))
