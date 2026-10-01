import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import shutil

from PIL import Image, ImageStat
from playwright.sync_api import sync_playwright


def select_watermark(image_path, image_y, asset_dir):
    white_path = asset_dir / 'oneirloom-woven-signature-white-black-outline.png'
    with Image.open(white_path) as signature:
        mark_height = 360 * signature.height / signature.width
    with Image.open(image_path) as image:
        scale = max(1800 / image.width, 800 / image.height)
        offset_x = (image.width * scale - 1800) / 2
        offset_y = (image.height * scale - 800) * image_y / 100
        area = image.convert('RGBA').crop((
            (1404 + offset_x) / scale, (36 + offset_y) / scale,
            (1764 + offset_x) / scale, (36 + mark_height + offset_y) / scale,
        ))
        background = Image.new('RGBA', area.size, '#f7f4ef')
        background.alpha_composite(area)
        rgb = ImageStat.Stat(background.convert('RGB')).mean
    luminance = (0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]) / 255
    variant = 'white-black-outline'
    path = white_path
    return path.resolve(strict=True), variant, luminance


def render_card(args):
    image_path = Path(args.image).resolve(strict=True)
    prompt_path = Path(args.prompt).resolve(strict=True)
    output_dir = Path(args.output).resolve()
    if not 0 <= args.image_y <= 100:
        raise ValueError('Image crop position must be between 0 and 100')
    watermark_path, watermark_variant, background_luminance = select_watermark(
        image_path, args.image_y, Path(__file__).resolve().parent.parent / 'assets',
    )
    prompt = prompt_path.read_text(encoding='utf-8-sig').strip()
    if not prompt:
        raise ValueError('Prompt file is empty')
    output_dir.mkdir(parents=True, exist_ok=False)
    photo_name = 'photo' + image_path.suffix.lower()
    shutil.copyfile(image_path, output_dir / photo_name)
    shutil.copyfile(watermark_path, output_dir / 'watermark.png')
    (output_dir / 'prompt.txt').write_text(prompt + '\n', encoding='utf-8')
    paragraphs = re.split(r'\n\s*\n', prompt)
    paragraph_html = ''.join('<p>' + html.escape(p) + '</p>' for p in paragraphs)
    document = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><title>__TITLE__</title>
<style>
* { box-sizing: border-box; }
html, body { margin: 0; width: 1800px; color: #28241f; background: #f7f4ef; }
body { font-family: "Microsoft YaHei", "Noto Sans CJK SC", sans-serif; }
.card { width: 1800px; height: 2400px; }
.image-region { position: relative; width: 1800px; height: 800px; overflow: hidden; }
.photo { display: block; width: 1800px; height: 800px; object-fit: cover; object-position: 50% __IMAGE_Y__%; }
.watermark { position: absolute; top: 36px; right: 36px; display: block; width: 20%; height: auto; opacity: 0.9; filter: __WATERMARK_SHADOW__; }
.text-region { width: 1800px; height: 1600px; padding: 52px 66px 56px; }
h1 { font-size: 48px; line-height: 1.35; font-weight: 700; margin: 0; }
.heading { padding-bottom: 22px; border-bottom: 2px solid #d7cec2; margin-bottom: 24px; }
.prompt { font-size: __FONT_SIZE__px; line-height: 1.5; text-align: justify; overflow-wrap: anywhere; }
p { margin: 0 0 18px; }
p:last-child { margin-bottom: 0; }
</style></head><body><main class="card">
<section class="image-region"><img class="photo" src="__PHOTO__" alt="Source image"><img class="watermark" src="watermark.png" alt="织梦师 Oneirloom Skill signature"></section>
<section class="text-region"><header class="heading"><h1>__TITLE__</h1></header>
<div class="prompt">__PARAGRAPHS__</div></section>
</main></body></html>'''
    replacements = {
        '__TITLE__': html.escape(args.title),
        '__IMAGE_Y__': str(args.image_y),
        '__PHOTO__': html.escape(photo_name),
        '__PARAGRAPHS__': paragraph_html,
        '__WATERMARK_SHADOW__': 'drop-shadow(0 1px 3px rgba(0, 0, 0, 0.65))' if watermark_variant == 'white' else 'none',
    }
    for key, value in replacements.items():
        document = document.replace(key, value)
    with sync_playwright() as playwright:
        launch_args = {'headless': True}
        if args.browser:
            launch_args['executable_path'] = str(Path(args.browser).resolve(strict=True))
        browser = playwright.chromium.launch(**launch_args)
        page = browser.new_page(viewport={'width': 1800, 'height': 2400}, device_scale_factor=1.5)
        for font_size in range(44, 29, -1):
            layout = document.replace('__FONT_SIZE__', str(font_size))
            (output_dir / 'card.html').write_text(layout, encoding='utf-8')
            page.goto((output_dir / 'card.html').as_uri(), wait_until='load')
            page.evaluate('document.fonts.ready')
            page.locator('.photo').evaluate('(image) => image.decode()')
            page.locator('.watermark').evaluate('(image) => image.decode()')
            checks = page.evaluate('''() => {
                const image = document.querySelector('.photo');
                const top = document.querySelector('.image-region').getBoundingClientRect();
                const bottom = document.querySelector('.text-region').getBoundingClientRect();
                const signature = document.querySelector('.watermark');
                const mark = signature.getBoundingClientRect();
                const paragraphs = [...document.querySelectorAll('.prompt p')];
                return {
                    canvas: [document.documentElement.scrollWidth, document.documentElement.scrollHeight],
                    imageRegion: {x: top.x, y: top.y, width: top.width, height: top.height},
                    promptRegion: {x: bottom.x, y: bottom.y, width: bottom.width, height: bottom.height},
                    sourceSize: [image.naturalWidth, image.naturalHeight],
                    imageFit: getComputedStyle(image).objectFit,
                    imagePosition: getComputedStyle(image).objectPosition,
                    watermark: {
                        x: mark.x, y: mark.y, width: mark.width, height: mark.height,
                        sourceSize: [signature.naturalWidth, signature.naturalHeight],
                        widthRatio: mark.width / top.width,
                        heightRatio: mark.height / top.height,
                        topMargin: mark.top - top.top,
                        rightMargin: top.right - mark.right,
                        opacity: getComputedStyle(signature).opacity,
                        insideImageRegion: mark.left >= top.left && mark.top >= top.top && mark.right <= top.right && mark.bottom <= top.bottom
                    },
                    fontSize: getComputedStyle(document.querySelector('.prompt')).fontSize,
                    textBottom: Math.max(...paragraphs.map(p => p.getBoundingClientRect().bottom)),
                    textInside: paragraphs.every(p => {
                        const r = p.getBoundingClientRect();
                        return r.left >= bottom.left + 66 && r.right <= bottom.right - 66 && r.top >= bottom.top && r.bottom <= bottom.bottom - 56;
                    })
                };
            }''')
            if checks['textInside']:
                break
        else:
            raise RuntimeError('Complete prompt does not fit; preserve the fixed split and report this gap')
        rendered_text = page.locator('.prompt').inner_text()
        if re.sub(r'\s+', '', rendered_text) != re.sub(r'\s+', '', prompt):
            raise RuntimeError('Rendered text differs from the selected prompt')
        expected_regions = (
            {'x': 0, 'y': 0, 'width': 1800, 'height': 800},
            {'x': 0, 'y': 800, 'width': 1800, 'height': 1600},
        )
        if checks['canvas'] != [1800, 2400] or (checks['imageRegion'], checks['promptRegion']) != expected_regions:
            raise RuntimeError('Rendered geometry does not match the fixed 3:4 layout')
        if checks['imageFit'] != 'cover':
            raise RuntimeError('Image must use proportional cover cropping')
        watermark = checks['watermark']
        if (not watermark['insideImageRegion']
                or abs(watermark['widthRatio'] - 0.2) > 0.001
                or abs(watermark['height'] - watermark['width'] * watermark['sourceSize'][1] / watermark['sourceSize'][0]) > 0.01
                or abs(watermark['topMargin'] - 36) > 0.01
                or abs(watermark['rightMargin'] - 36) > 0.01
                or watermark['opacity'] != '0.9'):
            raise RuntimeError('Signature does not match the approved top-right placement')
        png_path = output_dir / 'prompt-card-3x4.png'
        page.screenshot(path=str(png_path), full_page=True)
        browser.close()
    with Image.open(png_path) as output:
        if output.size != (2700, 3600):
            raise RuntimeError('PNG dimensions do not match the 3:4 output')
    source_hash = hashlib.sha256(image_path.read_bytes()).hexdigest()
    if source_hash != hashlib.sha256((output_dir / photo_name).read_bytes()).hexdigest():
        raise RuntimeError('Archived photo bytes differ from the source')
    watermark_hash = hashlib.sha256(watermark_path.read_bytes()).hexdigest()
    if watermark_hash != hashlib.sha256((output_dir / 'watermark.png').read_bytes()).hexdigest():
        raise RuntimeError('Archived signature bytes differ from the approved asset')
    checks.update({
        'pngSize': [2700, 3600],
        'sourceImageSha256': source_hash,
        'watermarkSha256': watermark_hash,
        'watermarkVariant': watermark_variant,
        'watermarkBackgroundLuminance': background_luminance,
        'promptMatchesSource': True,
        'imageInspected': False,
    })
    (output_dir / 'render-checks.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(checks, ensure_ascii=False))
    print(str(png_path))


def main():
    parser = argparse.ArgumentParser(description='Render a fixed 3:4 image and prompt card')
    parser.add_argument('--image', required=True)
    parser.add_argument('--prompt', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--title', default='Prompt')
    parser.add_argument('--image-y', type=float, default=50)
    parser.add_argument('--browser')
    render_card(parser.parse_args())


if __name__ == '__main__':
    main()
