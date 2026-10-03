from pathlib import Path
from hashlib import sha256
import json
import shutil

ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).resolve().parent
DEST = ROOT / 'docs/assets/portraits'
DEST.mkdir(parents=True, exist_ok=True)
GROUPS = [
    ('取景', [('19_close_fixed', '脸部特写'), ('20_half_fixed', '上半身人像'), ('01_full', '完整全身')]),
    ('姿态', [('09_seated', '短裙坐姿'), ('e07_backlace', '侧身回望'), ('e11_longseated', '长裙坐姿')]),
    ('穿搭', [('e03_short', '短裙轮廓'), ('e04_long', '长裙垂坠'), ('e09_layeropen', '开衫叠穿')]),
    ('光线', [('25_hard_fixed', '硬光与窗影'), ('26_warm_fixed', '夜间暖光'), ('e25_backlight', '逆光与发丝轮廓')]),
]
records = []
blocks = []
jobs = {j['id']:j for j in json.loads((ROOT / 'work/article-tutorial/jobs.json').read_text(encoding='utf-8'))}
for group, items in GROUPS:
    cells = []
    for key, label in items:
        src = ROOT / f'work/article-tutorial/images/{key}.png'
        dst = DEST / f'{key}.png'
        shutil.copyfile(src, dst)
        digest = sha256(src.read_bytes()).hexdigest()
        assert sha256(dst.read_bytes()).hexdigest() == digest
        raw = json.loads((ROOT / f'work/article-tutorial/evidence/{key}.json').read_text(encoding='utf-8'))
        job = raw.get('job', jobs.get(key, {}))
        graph = raw.get('graph', {})
        sampler = next((v['inputs'] for v in graph.values() if v.get('class_type') == 'KSampler'), {})
        unet = next((v['inputs'].get('unet_name') for v in graph.values() if v.get('class_type') == 'UNETLoader'), None)
        rec = {'id':key, 'label':label, 'group':group, 'image':f'{key}.png', 'original_path':src.relative_to(ROOT).as_posix(), 'sha256':digest, 'exact_submitted_prompt':job.get('prompt'), 'prompt_id':raw.get('prompt_id'), 'model_checkpoint':unet, 'seed':job.get('seed',sampler.get('seed')), 'sampling':{k:sampler.get(k) for k in ['steps','cfg','sampler_name','scheduler','denoise']}, 'processing':'Original PNG copied byte-for-byte. No crop, resizing, retouch, or regeneration.', 'evidence_path':f'work/article-tutorial/evidence/{key}.json'}
        assert rec['exact_submitted_prompt'], key
        records.append(rec)
        image=f'docs/assets/portraits/{key}.png'
        cells.append(f'<td width="33%" align="center"><a href="{image}"><img src="{image}" alt="{label}的已有人像作品" width="280"></a><br>{label}</td>')
    blocks.append(f'### {group}\n\n<table class="portrait-row"><tr>\n'+ '\n'.join(cells) +'\n</tr></table>\n')
(DEST / 'manifest.json').write_text(json.dumps({'source_collection_png_count':62, 'selected_originals':records, 'scope':'Archived text-to-image outputs. Image differences include multiple changing details; not a strict identity-lock or single-variable claim.'}, ensure_ascii=False, indent=2), encoding='utf-8')
source = (WORK / 'README.v2.md').read_text(encoding='utf-8')
source = source.replace('docs/assets/hero-v2.png','docs/assets/hero-v3.png')
source = source.replace('一个想法、一张参考图、一件产品，都可以成为创作的起点。', '先从你最想画好的人像开始，也可以继续做角色设定、插画与产品广告。')
start=source.index('## 作品与案例')
end=source.index('## 创作方式')
portfolio='''## 作品与案例

先看美女人像。下面选了此前人像教程里的 12 张原图，分别展示取景、姿态、穿搭与光线。整个教程保留 62 张生成原图，首页展示的图片直接复制自已有结果。

'''+ '\n'.join(blocks)+'''
一张脸可以拍得更近，一个坐姿会改变衣料的褶皱，同一类黑裙也可以有不同的长度与背部结构。织梦师会把这些意图写成具体画面关系，让你有方向地继续创作。

[查看这 12 张图的原始提示词与参数记录](docs/assets/portraits/manifest.json) · [阅读完整人像教程](work/article-tutorial/美女生图教程.md)

<details>
<summary>这组图说明了什么</summary>

它们来自已记录的 Qwen-Image-2.1 本地文生图案例，首页未裁切、修图或重新生成。样本之间可能同时改变脸部、姿态、衣料和房间细节；这些图展示各自的实际画面，不表示精确身份锁定或单变量实验。原记录中的生成偏差继续保留。

</details>

### 继续做角色、插画和广告

<table><tr>
<td width="50%" align="center"><a href="skills/oneirloom-style-design/templates/product-origin-world/template.md"><img src="skills/oneirloom-style-design/templates/product-origin-world/images/example-01.png" alt="摄影巧克力与手绘可可庄园的广告案例" width="420"></a><br><strong>让产品走进它的故事</strong><br>摄影质感的巧克力，流入手绘可可庄园。</td>
<td width="50%" align="center"><a href="skills/oneirloom-style-illustration/templates/zhiguai-narrative/template.md"><img src="skills/oneirloom-style-illustration/templates/zhiguai-narrative/images/example-01.png" alt="山雾与月色中的志怪叙事插画" width="420"></a><br><strong>让氛围服务于叙事</strong><br>旧纸、山雾、月色与人物之间的关系。</td>
</tr></table>

巧克力案例保留原始提示词，志怪插画的氛围得到用户认可；两者的模型与生成参数均未知。点击图片查看对应记录。

<details>
<summary>看角色衣橱设定</summary>

![包含服装、配件与材质细节的已有角色衣橱设定图](skills/oneirloom-character-sheet/templates/wardrobe-sheet/images/result-01.png)

这个用户提供的结果展示了服装、配件、材质与版面安排。转身视图和部分服装头像仍有偏差，模型与参数未知。[查看角色衣橱模板与记录](skills/oneirloom-character-sheet/templates/wardrobe-sheet/template.md)。

</details>

### 从一份外卖，构思一张广告

<table><tr>
<td width="50%" align="center"><img src="skills/oneirloom-product-art-direction/references/takeaway-food-town/images/source.png" alt="原始外卖产品照片" width="420"><br>原始产品照片</td>
<td width="50%" align="center"><img src="skills/oneirloom-product-art-direction/references/takeaway-food-town/images/accepted.png" alt="用户认可的微缩食物小镇结果" width="280"><br>用户认可的结果</td>
</tr></table>

春卷成为屋顶，薯条成为台阶，餐盒里出现手绘街巷与微缩人物。食物仍保留摄影质感，创意从产品的形状和场景中展开。

织梦师的[产品创意方法](skills/oneirloom-product-art-direction/SKILL.md)会先检查产品，再选择故事和表现手法。这个案例记录了用户认可的一次结果，实际提交提示词、模型与参数未知。[查看案例记录](skills/oneirloom-product-art-direction/references/takeaway-food-town/evidence.json)。

'''
source=source[:start]+portfolio+source[end:]
start=source.index('## 创作方式')
end=source.index('## 你可以用它做什么')
methods='''## 创作方式

你不必一开始就准备完整提示词。先说目标，再给出已有材料。织梦师会沿用对话中已经确认的条件，明确目标、拆解画面，选择需要的方法，再适配模型并交付完整提示词。有结果图时，继续对照目标修正。

想改取景，就明确画框与身体的位置；想改姿态，就写清躯干、头部和四肢的关系；想改穿搭，就组织衣料、剪裁与叠穿；想改光线，就说明光从哪里来、哪些区域亮起来。

默认交付完整中文提示词和语义对应的英文版，每个版本独立可复制。明确要求只用一种语言时，就按你的要求输出。

首页主视觉以已有美女人像为参考，通过生图模型制作成新的宣传合成图；上面的 12 张作品图保留原始结果。

'''
source=source[:start]+methods+source[end:]
(ROOT / 'README.md').write_text(source, encoding='utf-8')
print(json.dumps({'selected_originals':len(records), 'source_collection':62, 'all_copies_hash_match':True}, ensure_ascii=False))
