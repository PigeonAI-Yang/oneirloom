from pathlib import Path
from hashlib import sha256
import json
import math
import re
import html
import markdown
from markdown.extensions.toc import slugify_unicode
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs/assets'
WORK = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)
INK = '#262923'
PAPER = '#F5F1E8'
MUTED = '#6D7167'
GOLD = '#CCAC74'
GREEN = '#3A5748'
FONT = Path('C:/Windows/Fonts/msyh.ttc')
BOLD = Path('C:/Windows/Fonts/msyhbd.ttc')
SERIF = Path('C:/Windows/Fonts/georgia.ttf')
SOURCES = {
    'chocolate': 'skills/oneirloom-style-design/templates/product-origin-world/images/example-01.png',
    'folklore': 'skills/oneirloom-style-illustration/templates/zhiguai-narrative/images/example-01.png',
    'portrait': 'skills/oneirloom-style-photography/templates/indoor-full-length/images/result-01.png',
    'wardrobe': 'skills/oneirloom-character-sheet/templates/wardrobe-sheet/images/result-01.png',
    'food_source': 'skills/oneirloom-product-art-direction/references/takeaway-food-town/images/source.png',
    'food_result': 'skills/oneirloom-product-art-direction/references/takeaway-food-town/images/accepted.png',
}
TEXT_BOXES = []


def font(size, bold=False, serif=False):
    return ImageFont.truetype(str(SERIF if serif else BOLD if bold else FONT), size)


def write(im, xy, value, size=32, color=INK, bold=False, serif=False, spacing=14):
    d = ImageDraw.Draw(im)
    f = font(size, bold, serif)
    d.multiline_text(xy, value, font=f, fill=color, spacing=spacing)
    box = d.multiline_textbbox(xy, value, font=f, spacing=spacing)
    assert box[0] >= 0 and box[1] >= 0 and box[2] <= im.width and box[3] <= im.height, (value, box)
    TEXT_BOXES.append({'text': value, 'box': box, 'canvas': im.size})


def art(im, key, box):
    source = Image.open(ROOT / SOURCES[key]).convert('RGB')
    x, y, w, h = box
    fitted = ImageOps.contain(source, (w, h), Image.Resampling.LANCZOS)
    im.paste(fitted, (x + (w - fitted.width) // 2, y + (h - fitted.height) // 2))


def header(im, number, eyebrow, title):
    d = ImageDraw.Draw(im)
    write(im, (64, 32), f'{number}  /  {eyebrow}', 22, GREEN)
    write(im, (64, 75), title, 48, bold=True)
    d.line((64, 150, 1736, 150), fill='#D9D5CA', width=2)


def save(im, name):
    im.save(OUT / name, optimize=True)


im = Image.new('RGB', (1800, 950), '#1D2923')
d = ImageDraw.Draw(im)
for i in range(12):
    points = [(x, 610 + i * 7 + int(18 * math.sin(x / 88 + i / 3))) for x in range(64, 781, 4)]
    d.line(points, fill=(48 + i * 2, 67 + i, 55 + i), width=2)
write(im, (80, 62), 'VISUAL PROMPTING SKILL COLLECTION', 24, GOLD)
write(im, (76, 140), 'Oneirloom', 90, PAPER, serif=True)
write(im, (76, 262), '织梦师', 116, PAPER, bold=True)
write(im, (80, 430), '把画面想清楚，\n把提示词写到位。', 48, PAPER, spacing=18)
write(im, (80, 740), '参考拆解  ·  模型适配  ·  结果修正', 29, GOLD)
write(im, (80, 830), '中文 + English     /     Agent Skills', 25, '#BEC6BC')
for j, (key, label) in enumerate([('chocolate', '产品创意'), ('folklore', '叙事插画'), ('portrait', '生活摄影')]):
    x = 864 + j * 288
    d.rectangle((x, 210, x + 266, 636), fill='#304036')
    art(im, key, (x + 8, 218, 250, 410))
    write(im, (x + 12, 666), label, 27, PAPER)
write(im, (866, 750), '图像选自仓库已有案例', 22, '#BEC6BC')
save(im, 'hero.png')

im = Image.new('RGB', (1800, 940), PAPER)
header(im, '01', 'ARCHIVED EXAMPLES', '同一套方法，组织不同的画面')
d = ImageDraw.Draw(im)
cards = [
    ('chocolate', '产品广告', '摄影产品与插画世界连接', '原始提示词已保存'),
    ('folklore', '志怪插画', '人物叙事与山间氛围', '用户认可氛围'),
    ('portrait', '生活摄影', '全身取景与卧室窗光', '本地生成记录已保存'),
    ('wardrobe', '角色衣橱', '服装、配件与细节编排', '已有结果及偏差记录'),
]
for j, (key, title, desc, status) in enumerate(cards):
    x = 64 + j * 424
    d.rectangle((x, 182, x + 396, 710), fill='#E8E3D8')
    art(im, key, (x, 182, 396, 528))
    write(im, (x, 738), title, 34, bold=True)
    write(im, (x, 790), desc, 25, MUTED)
    write(im, (x, 842), status, 23, GREEN)
write(im, (64, 900), '已有案例完整画面，等比缩放展示。各例的参数、提示词与局限见对应记录。', 21, MUTED)
save(im, 'showcase.png')

im = Image.new('RGB', (1800, 1030), PAPER)
header(im, '02', 'PRODUCT ART DIRECTION', '让创意围绕产品展开')
d = ImageDraw.Draw(im)
write(im, (72, 181), '原始产品照片', 29, bold=True)
write(im, (742, 181), '用户认可的结果', 29, bold=True)
d.rectangle((72, 250, 674, 930), fill='#E8E3D8')
art(im, 'food_source', (72, 250, 602, 680))
d.rectangle((742, 250, 1138, 930), fill='#E8E3D8')
art(im, 'food_result', (742, 250, 396, 680))
write(im, (1220, 277), '外卖盒里的\n微缩食物小镇', 41, bold=True, spacing=17)
for y, n, title, desc in [
    (449, '01', '保留食物质感', '摄影质感的食物仍是主角'),
    (576, '02', '寻找形状联系', '春卷屋顶，薯条台阶'),
    (703, '03', '加入画面故事', '手绘街巷与微缩人物'),
]:
    write(im, (1220, y), n, 23, GREEN)
    write(im, (1278, y - 5), title, 28, bold=True)
    write(im, (1220, y + 49), desc, 25, MUTED)
write(im, (1220, 890), '一次已认可的结果\n模型与实际提交参数未知', 23, MUTED, spacing=10)
write(im, (72, 983), '原图与结果均保留完整画面。此比较展示创意过程，不是单变量实验。', 22, MUTED)
save(im, 'product-case.png')

im = Image.new('RGB', (1800, 700), PAPER)
header(im, '03', 'WORKFLOW', '先确定画面，再适配模型')
d = ImageDraw.Draw(im)
steps = [
    ('明确目标', '想画什么\n保留哪些参考关系\n继承已确认偏好'),
    ('拆解画面', '主体与环境\n空间与遮挡\n光色与材质'),
    ('选择方法', '读取相关方法\n有合适模板就借用\n也可组织新场景'),
    ('适配模型', '保持视觉意图\n区分任务与入口\n参数独立列出'),
    ('交付与修正', '完整可复制提示词\n默认中文与英文\n按结果修正偏差'),
]
for j, (title, body) in enumerate(steps):
    x = 64 + j * 342
    d.rounded_rectangle((x, 208, x + 306, 535), radius=14, fill='#ECE8DE')
    write(im, (x + 24, 226), f'0{j+1}', 43, GREEN, serif=True)
    write(im, (x + 24, 307), title, 31, bold=True)
    write(im, (x + 24, 379), body, 24, MUTED, spacing=16)
    if j < 4:
        d.line((x + 315, 360, x + 333, 360), fill=GREEN, width=3)
        d.polygon([(x + 334, 360), (x + 327, 354), (x + 327, 366)], fill=GREEN)
d.line((1715, 555, 1715, 592, 1432, 592), fill=GREEN, width=2)
d.polygon([(1430, 592), (1438, 586), (1438, 598)], fill=GREEN)
write(im, (835, 576), '有结果图时，对照目标继续修正', 26, GREEN)
write(im, (64, 651), '按当前任务读取所需技能。没有匹配模板，也能继续创作。', 23, MUTED)
save(im, 'workflow.png')

im = Image.new('RGB', (1800, 820), PAPER)
header(im, '04', 'PROMPT WRITING', '把日常描述，展开为可见的画面关系')
d = ImageDraw.Draw(im)
d.rounded_rectangle((64, 208, 470, 728), radius=16, fill='#263D31')
write(im, (100, 250), '你可以这样说', 27, GOLD)
write(im, (100, 332), '暖色、安静的\n卧室全身照', 42, PAPER, bold=True, spacing=22)
write(im, (100, 567), '织梦师会组织\n取景、布局、光色\n与材质细节', 28, '#CBD3C9', spacing=12)
rows = [
    ('取景', '从头顶到鞋底完整入画，脚下留出一段地板。'),
    ('布局', '床在画面右侧，电视柜在左侧，人物站在中间过道。'),
    ('光色', '左侧窗光照亮面部，右侧保留轻微阴影。'),
    ('材质', '缎面呈流动高光，黑裙保留深色层次，床品为乳白色。'),
]
for j, (title, body) in enumerate(rows):
    y = 208 + j * 133
    d.rounded_rectangle((542, y, 1736, y + 112), radius=12, fill='#ECE8DE')
    write(im, (572, y + 32), title, 31, GREEN, bold=True)
    write(im, (678, y + 36), body, 29, INK)
write(im, (64, 773), '写作示意。以上片段未作为一组新提示词进行生成测试。', 23, MUTED)
save(im, 'prompt-anatomy.png')

originals = {key: {'path': path, 'sha256': sha256((ROOT / path).read_bytes()).hexdigest()} for key, path in SOURCES.items()}
assets = {p.name: {'size_px': Image.open(p).size, 'bytes': p.stat().st_size, 'sha256': sha256(p.read_bytes()).hexdigest()} for p in sorted(OUT.glob('*.png'))}
manifest = {
    'date': '2026-09-30',
    'source_artwork': originals,
    'assets': assets,
    'processing': 'Existing artwork placed in deterministic layouts with proportional resizing. No crop, retouch, recoloring, or new image generation.',
    'copy_claims': 'The prompt anatomy is an untested writing illustration. Existing cases retain their evidence limitations in README.md.',
    'text_boxes_within_canvas': len(TEXT_BOXES),
    'structural_references': ['https://github.com/obra/superpowers', 'https://github.com/Comfy-Org/ComfyUI', 'https://github.com/anthropics/skills'],
}
(WORK / 'assets-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
source = (ROOT / 'README.md').read_text(encoding='utf-8')
body = markdown.markdown(source.replace('<details>', '<details markdown="1">'), extensions=['tables', 'fenced_code', 'md_in_html', 'toc'], extension_configs={'toc': {'slugify': slugify_unicode}})
base = html.escape(ROOT.as_uri() + '/', quote=True)
page = '''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><base href="BASE"><title>织梦师 · Oneirloom</title><style>
*{box-sizing:border-box}body{margin:0;background:#f6f8fa;color:#1f2328;font:16px/1.8 -apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif}main{max-width:1040px;margin:32px auto;padding:40px 48px;background:#fff;border:1px solid #d1d9e0;border-radius:8px}h1,h2,h3{line-height:1.4;color:#1f2328}h1{font-size:32px;border-bottom:1px solid #d1d9e0;padding-bottom:12px}h2{font-size:25px;margin-top:42px;border-bottom:1px solid #d1d9e0;padding-bottom:10px}h3{font-size:21px;margin-top:30px}a{color:#0969da;text-decoration:none}a:hover{text-decoration:underline}img{width:100%;height:auto;display:block;margin:22px 0}table{border-collapse:collapse;width:100%;font-size:14px;display:block;overflow:auto}th,td{border:1px solid #d1d9e0;padding:10px 14px;min-width:140px}th{background:#f6f8fa}tr:nth-child(2n){background:#f6f8fa}pre{padding:18px;background:#f6f8fa;overflow:auto;border-radius:6px;font:14px/1.75 Consolas,"Microsoft YaHei",monospace}code{background:#eff1f3;border-radius:4px;padding:2px 5px;font:0.88em Consolas,"Microsoft YaHei",monospace}pre code{padding:0;background:none}summary{cursor:pointer;padding:10px 0;color:#0969da}details{margin:16px 0}p{margin:17px 0}@media(max-width:650px){body{background:white}main{margin:0;border:0;border-radius:0;padding:18px}h1{font-size:27px}h2{font-size:23px}img{margin:16px 0}table{font-size:13px}}
</style></head><body><main>BODY</main></body></html>'''.replace('BASE', base).replace('BODY', body)
(WORK / 'preview.html').write_text(page, encoding='utf-8')
local_refs = re.findall(r'\]\(([^)]+)\)', source)
missing = [ref for ref in local_refs if not ref.startswith(('https://', '#')) and not (ROOT / ref).exists()]
assert not missing, missing
print(json.dumps({'assets': assets, 'text_boxes_checked': len(TEXT_BOXES), 'markdown_links_checked': len(local_refs), 'missing_links': missing, 'preview': str(WORK / 'preview.html')}, ensure_ascii=False))
