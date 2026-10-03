import html
import json
import re
from pathlib import Path

from markdown_it import MarkdownIt
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'x-draft'
OUT.mkdir(exist_ok=True)
source = (ROOT / '美女生图教程-便携版.md').read_text(encoding='utf-8')
title, body = source.split('\n', 1)
figures = []


def figure_marker(match):
    index = len(figures) + 1
    marker = f'〔教程配图{index:02d}〕'
    figures.append({'index':index, 'marker':marker, 'caption':match.group(1), 'path':str(ROOT / match.group(2))})
    return marker + '\n\n' + match.group(1)


body = re.sub(r'!\[([^\]]*)\]\((images/[^)]+)\)', figure_marker, body)
rendered = MarkdownIt('commonmark').render(body)
rendered = rendered.replace('<h2>', '<h1>').replace('</h2>', '</h1>').replace('<h3>', '<h2>').replace('</h3>', '</h2>')
(OUT / 'article-paste.html').write_text(rendered, encoding='utf-8')
(OUT / 'article-paste.txt').write_text(body.strip(), encoding='utf-8')
(OUT / 'manifest.json').write_text(json.dumps({'title':title[2:], 'draft_url':'https://x.com/compose/articles/edit/2104389078770917376', 'figures':figures}, ensure_ascii=False, indent=2), encoding='utf-8')

W,H = 2000,800
canvas = Image.new('RGB',(W,H),'#24211f')
d = ImageDraw.Draw(canvas)
regular='C:/Windows/Fonts/msyh.ttc'
bold='C:/Windows/Fonts/msyhbd.ttc'


def label(x,y,text,size,color='#f9f4ea',weight=True):
    d.text((x,y),text,font=ImageFont.truetype(bold if weight else regular,size),fill=color)


portrait = Image.open(ROOT/'images/e20_smile.png').convert('RGB')
portrait = ImageOps.fit(portrait,(740,800),centering=(0.5,0.32))
canvas.paste(portrait,(1260,0))
d.rectangle((0,0,1259,799),fill='#24211f')
d.rectangle((90,110,158,117),fill='#dba47c')
label(180,89,'从单张写真到一组四宫格',32,'#dfc2a9',False)
label(84,203,'AI 美女写真',112)
label(84,340,'提示词怎么写',108)
label(91,511,'姿势 · 服装 · 光线 · 四宫格',37,'#e0c8b2',False)
d.line((92,624,893,624),fill='#5e5047',width=2)
label(93,664,'16章实操   /   39组图例讲解',31,'#ede0d3',False)

card = Image.open(ROOT/'images/e09_layeropen.png').convert('RGB')
card = ImageOps.fit(card,(256,414),centering=(0.5,0.5))
d.rounded_rectangle((991,177,1285,682),radius=14,fill='#e8d6c3')
canvas.paste(card,(1010,196))
label(1030,630,'看图学写法',25,'#463429',False)
canvas.save(OUT/'X文章封面-中文版-5比2.jpg',quality=96,subsampling=0)
canvas.save(OUT/'X文章封面-中文版-5比2.png')
print(json.dumps({'title':title[2:],'figures':len(figures),'cover_size':[W,H],'cover':str(OUT/'X文章封面-中文版-5比2.jpg')},ensure_ascii=False))
