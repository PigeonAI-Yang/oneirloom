import base64
import html
import json
import re
import zipfile
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent
jobs = json.loads((ROOT / "jobs.json").read_text(encoding="utf-8"))
job_map = {j["id"]: j for j in jobs}
observations = json.loads((ROOT / "observations.json").read_text(encoding="utf-8"))
source = (ROOT / "article-first-person.template.md").read_text(encoding="utf-8")
source = source.replace("{{FULL_PROMPT}}", job_map["01_full"]["prompt"])
source = source.replace("{{GRID_PROMPT}}", job_map["18_grid"]["prompt"])
source = source.replace("{{REPAIR_OBSERVATION}}", observations["repair_paragraph"])
source = source.replace("{{GRID_OBSERVATION}}", observations["grid_paragraph"])
assert "{{" not in source
sections = re.split(r"(?m)^## ", source)[1:]
assert len(sections) == 16
assert all(re.search(r"!\[[^\]]*\]\(images/figure-", s) for s in sections)
image_paths = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", source)
assert len(image_paths) == 16
assert all((ROOT / p).exists() for p in image_paths)

portable_md = source
desktop_md = re.sub(r"(!\[[^\]]*\]\()images/", r"\g<1>" + ROOT.as_posix() + "/images/", source)
(ROOT / "美女生图教程.md").write_text(desktop_md, encoding="utf-8")
(ROOT / "美女生图教程-便携版.md").write_text(portable_md, encoding="utf-8")
body = MarkdownIt("commonmark").render(source)
title_match = re.search(r"<h1>(.*?)</h1>", body)
title = title_match.group(1)
body = body.replace(title_match.group(0), "", 1)
nav = []


def heading(match):
    index = len(nav) + 1
    label = match.group(1)
    nav.append(f'<a href="#section-{index:02d}">{label}</a>')
    return f'<h2 id="section-{index:02d}">{label}</h2>'


body = re.sub(r"<h2>(.*?)</h2>", heading, body)


def embed_image(match):
    path = ROOT / match.group(1)
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    alt = match.group(2)
    return f'<figure><img src="data:image/jpeg;base64,{encoded}" alt="{alt}" loading="lazy" tabindex="0"/><figcaption>{alt} · 点击放大</figcaption></figure>'


body = re.sub(r'<p><img src="(images/[^"]+)" alt="([^"]*)"\s*/?></p>', embed_image, body)
assert 'src="images/' not in body
body = re.sub(r'(<pre><code[^>]*>.*?</code></pre>)', r'<div class="prompt"><button class="copy" type="button">复制提示词</button>\1</div>', body, flags=re.S)
completed = sum(1 for p in (ROOT / "evidence").glob("*.json") if p.name not in ("workflow-source.json", "workflow-api.json") and json.loads(p.read_text(encoding="utf-8")).get("completed"))
css = """
:root{color-scheme:light;--paper:#faf8f4;--ink:#292823;--muted:#79736a;--accent:#885238;--line:#e5ded4}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:30px}body{margin:0;background:var(--paper);color:var(--ink);font-family:'Microsoft YaHei','PingFang SC',sans-serif;line-height:1.95;font-size:17px}a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}.layout{max-width:1310px;margin:auto;padding:56px 34px 80px;display:grid;grid-template-columns:235px minmax(0,900px);gap:52px}.toc{position:sticky;top:32px;height:calc(100vh - 64px);overflow:auto;font-size:13px;line-height:1.65;padding-right:15px}.toc strong{font-size:12px;letter-spacing:2px;color:var(--muted);display:block;margin-bottom:20px}.toc a{display:block;padding:8px 0;color:#655f56;border-bottom:1px solid var(--line)}.toc a:hover{color:var(--accent)}.eyebrow{font-size:12px;letter-spacing:2px;color:var(--accent)}h1{font-size:37px;line-height:1.5;letter-spacing:-.7px;margin:14px 0 22px;font-weight:650}.stats{color:var(--muted);font-size:13px;padding:16px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin-bottom:32px}.article>p{margin:18px 0}h2{font-size:26px;line-height:1.65;margin:70px 0 24px;padding-top:28px;border-top:1px solid var(--line);font-weight:650}figure{margin:26px 0 30px}figure img{display:block;width:100%;height:auto;border-radius:8px;cursor:zoom-in;background:#f5f1ea}figcaption{text-align:center;color:var(--muted);font-size:12px;line-height:1.7;margin-top:10px}.prompt{position:relative;margin:24px 0;background:#f0ece5;border:1px solid var(--line);border-radius:9px;overflow:hidden}pre{margin:0;padding:49px 24px 23px;white-space:pre-wrap;overflow-wrap:anywhere;line-height:1.85;font-size:14px}code{font-family:Consolas,'Microsoft YaHei',monospace}p code{font-size:.86em;background:#eee9e1;border-radius:4px;padding:2px 5px}.copy{position:absolute;right:12px;top:10px;color:var(--accent);background:#faf8f4;border:1px solid #d6cbbd;border-radius:5px;padding:4px 10px;cursor:pointer;font-size:12px}hr{border:0;border-top:1px solid var(--line);margin:50px 0 30px}hr~p{font-size:13px;color:var(--muted)}dialog{border:0;border-radius:10px;padding:12px;background:var(--paper);max-width:96vw;max-height:96vh}dialog::backdrop{background:#171511dc}dialog img{display:block;max-width:92vw;max-height:87vh;width:auto;height:auto}dialog button{display:block;margin:0 0 8px auto;background:transparent;border:0;cursor:pointer;color:var(--ink)}.mobile-toc{display:none}@media(max-width:1050px){.layout{grid-template-columns:minmax(0,880px);justify-content:center;padding:30px 24px}.toc{display:none}.mobile-toc{display:block;border-bottom:1px solid var(--line);padding:12px 0;margin-bottom:22px}.mobile-toc a{display:block;font-size:13px;padding:4px 0}}@media(max-width:600px){body{font-size:16px}.layout{padding:25px 17px 60px}h1{font-size:29px}h2{font-size:22px;margin-top:50px}pre{font-size:13px;padding-left:16px;padding-right:16px}.stats{font-size:12px}figure{margin-left:-7px;margin-right:-7px}}@media print{.toc,.mobile-toc,.copy,dialog{display:none}.layout{display:block;padding:0}.prompt,figure{break-inside:avoid}h2{break-after:avoid;margin-top:30px}a{color:inherit}.stats{font-size:11px}}
"""
script = """
const modal=document.querySelector('dialog');
document.querySelectorAll('figure img').forEach(img=>{const open=()=>{modal.querySelector('img').src=img.src;modal.querySelector('img').alt=img.alt;modal.showModal()};img.addEventListener('click',open);img.addEventListener('keydown',e=>{if(e.key==='Enter')open()})});
modal.querySelector('button').onclick=()=>modal.close();modal.addEventListener('click',e=>{if(e.target===modal)modal.close()});
document.querySelectorAll('.copy').forEach(button=>button.addEventListener('click',async()=>{const text=button.parentElement.querySelector('code').textContent;try{await navigator.clipboard.writeText(text);button.textContent='已复制'}catch{const area=document.createElement('textarea');area.value=text;document.body.appendChild(area);area.select();const ok=document.execCommand('copy');area.remove();button.textContent=ok?'已复制':'请手动选择复制'}setTimeout(()=>button.textContent='复制提示词',1800)}));
"""
document = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{css}</style></head><body><div class="layout"><nav class="toc" aria-label="教程目录"><strong>图文教程 / 目录</strong>{''.join(nav)}</nav><main><header><div class="eyebrow">美女写真 · 从描述到实际出图</div><h1>{title}</h1><div class="stats">16 个小节 · 16 张教学图版 · {completed} 次实际生成 · Qwen-Image-2.1</div></header><details class="mobile-toc"><summary>展开教程目录</summary>{''.join(nav)}</details><article class="article">{body}</article></main></div><dialog aria-label="放大配图"><button type="button">关闭 ×</button><img alt=""/></dialog><script>{script}</script></body></html>'''
(ROOT / "美女生图教程.html").write_text(document, encoding="utf-8")
with zipfile.ZipFile(ROOT / "美女生图教程-图文包.zip", "w", compression=zipfile.ZIP_DEFLATED) as archive:
    archive.write(ROOT / "美女生图教程.html", "美女生图教程.html")
    archive.writestr("美女生图教程.md", portable_md)
    archive.write(ROOT / "jobs.json", "生成提示词与种子.json")
    archive.write(ROOT / "observations.json", "实测观察.json")
    for p in image_paths:
        archive.write(ROOT / p, p)
    for p in sorted((ROOT / "images").glob("*.png")):
        archive.write(p, "原始生成图/" + p.name)
report = {"sections":len(sections),"figures":len(image_paths),"completed_generations":completed,"markdown_characters":len(source),"html_bytes":(ROOT / "美女生图教程.html").stat().st_size,"missing_images":[],"unresolved_placeholders":False}
(ROOT / "evidence/delivery-check.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(report,ensure_ascii=False))
