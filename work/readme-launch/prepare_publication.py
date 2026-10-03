from pathlib import Path
from hashlib import sha256
import json
import re
import shutil
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).resolve().parent
PUB = WORK / 'publish-checkout'
assert (PUB / '.git').is_file()
for name in ['README.md','README.en.md','CONTRIBUTING.md','LICENSE','docs/architecture.md','docs/model-evidence.md']:
    dst=PUB / name
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / name, dst)
for src in (ROOT / 'skills').glob('oneirloom*'):
    shutil.copytree(src, PUB / 'skills' / src.name, dirs_exist_ok=True)

mapping={}
metrics=[]

def encode(src, dst, lossless=False):
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        im.save(dst, 'WEBP', lossless=lossless, quality=90 if src.name=='hero-v3.png' else 87, method=6)
        with Image.open(dst) as encoded:
            assert im.size == encoded.size
            if lossless:
                assert im.convert('RGBA').tobytes() == encoded.convert('RGBA').tobytes()
    original=src.relative_to(ROOT).as_posix()
    published=dst.relative_to(PUB).as_posix()
    mapping[original]=published
    metrics.append({'source':original,'published':published,'original_bytes':src.stat().st_size,'published_bytes':dst.stat().st_size,'original_sha256':sha256(src.read_bytes()).hexdigest(),'published_sha256':sha256(dst.read_bytes()).hexdigest(),'lossless':lossless,'dimensions_unchanged':True})

for png in list((PUB / 'skills').rglob('*.png')):
    rel=png.relative_to(PUB)
    encode(ROOT / rel, png.with_suffix('.webp'), True)
    png.unlink()

encode(ROOT / 'docs/assets/hero-v3.png',PUB / 'docs/assets/hero-v3.webp')
for src in (ROOT / 'docs/assets/portraits').glob('*.png'):
    encode(src,PUB / 'docs/assets/portraits' / src.with_suffix('.webp').name)

src_article=ROOT / 'work/article-tutorial/美女生图教程.md'
dst_article=PUB / 'docs/美女生图教程.md'
article=src_article.read_text(encoding='utf-8')
for old in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', article):
    filename=old.replace('\\','/').split('/')[-1]
    src=ROOT / 'work/article-tutorial/images' / filename
    dst=PUB / 'docs/assets/tutorial' / Path(filename).with_suffix('.webp')
    if not dst.exists():
        encode(src,dst)
    article=article.replace(old,'assets/tutorial/'+dst.name)
dst_article.write_text(article,encoding='utf-8')

for src in (ROOT / 'work/article-tutorial/images').glob('*.png'):
    if src.relative_to(ROOT).as_posix() not in mapping:
        encode(src,PUB / 'docs/assets/tutorial-originals' / src.with_suffix('.webp').name)
for record in metrics:
    if record['source'].startswith('work/article-tutorial/images/') and record['source'].endswith('.png'):
        old=ROOT / 'work/article-tutorial/evidence' / (Path(record['source']).stem+'.json')
        if old.exists():
            dst=PUB / 'docs/portrait-evidence' / old.name
            dst.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(old,dst)

manifest=json.loads((ROOT / 'docs/assets/portraits/manifest.json').read_text(encoding='utf-8'))
for item in manifest['selected_originals']:
    key='docs/assets/portraits/'+item['image']
    compressed=next(x for x in metrics if x['source']==key)
    item['original_png_sha256']=item['sha256']
    item['sha256']=compressed['published_sha256']
    item['image']=Path(item['image']).with_suffix('.webp').name
    item['processing']='Published WebP derivative, quality 87, original dimensions preserved. Original PNG remains in the author workspace.'
    item['evidence_path']='docs/portrait-evidence/'+item['id']+'.json'
(PUB / 'docs/assets/portraits/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')

for doc in list(PUB.rglob('*.md'))+list(PUB.rglob('*.txt'))+list(PUB.rglob('*.json')):
    if '.git' in doc.parts:
        continue
    text=doc.read_text(encoding='utf-8')
    for old,new in mapping.items():
        text=text.replace(old,new)
        if old.startswith('skills/'):
            old_abs=ROOT / old
            new_abs=PUB / new
            import os
            old_rel=os.path.relpath(old_abs,ROOT / doc.relative_to(PUB).parent).replace('\\','/')
            new_rel=os.path.relpath(new_abs,doc.parent).replace('\\','/')
            text=text.replace(old_rel,new_rel)
    if doc.suffix=='.json':
        data=json.loads(text)
        for row in metrics:
            if row['source'].startswith('skills/') and row['original_sha256'] in text.lower():
                text=re.sub(row['original_sha256'],row['published_sha256'],text,flags=re.I)
                data=json.loads(text)
                if isinstance(data,dict):
                    data.setdefault('publication_encoding',[]).append({'image':row['published'],'format':'lossless WebP','original_png_sha256':row['original_sha256'],'pixel_values_preserved':True})
                    text=json.dumps(data,ensure_ascii=False,indent=2)
    doc.write_text(text,encoding='utf-8')

readme=(PUB / 'README.md').read_text(encoding='utf-8')
readme=readme.replace('work/article-tutorial/美女生图教程.md','docs/美女生图教程.md')
readme=readme.replace('首页展示的图片直接复制自已有结果。','首页展示的是已有结果的 WebP 压缩版，保留原尺寸。')
readme=readme.replace('首页未裁切、修图或重新生成。','首页只做 WebP 编码压缩，未裁切、修图或重新生成。')
readme=readme.replace('上面的 12 张作品图保留原始结果。','上面的 12 张作品图展示已有结果的压缩版。')
(PUB / 'README.md').write_text(readme,encoding='utf-8')
total_before=sum(x['original_bytes'] for x in metrics)
total_after=sum(x['published_bytes'] for x in metrics)
home_paths=set(re.findall(r'(?:src|href)="([^"]+)"',readme)+re.findall(r'!\[[^\]]*\]\(([^)]+)\)',readme))
homepage=[x for x in metrics if x['published'] in home_paths]
report={'all_images':len(metrics),'original_bytes':total_before,'compressed_bytes':total_after,'reduction_percent':round(100*(1-total_after/total_before),1),'homepage_images':len(homepage),'homepage_original_bytes':sum(x['original_bytes'] for x in homepage),'homepage_compressed_bytes':sum(x['published_bytes'] for x in homepage),'records':metrics}
(PUB / 'docs/image-compression.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
(PUB / 'docs/assets/README.md').write_text('''# Published images

The homepage uses a generated fashion-portrait hero and twelve archived portrait outputs. Display images are WebP derivatives with their original dimensions preserved. The original PNGs remain in the author workspace.

Skill example images use lossless WebP and preserve every decoded RGBA pixel. Their records retain the original PNG hashes under publication encoding metadata. Portrait and tutorial display images use quality 87; the hero uses quality 90. No crops or retouching were applied.

See [compression records](../image-compression.json) and [portrait prompts and parameters](portraits/manifest.json). The full [portrait tutorial](../美女生图教程.md) uses compressed copies of its existing explanatory figures.
''',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='records'},ensure_ascii=False))
