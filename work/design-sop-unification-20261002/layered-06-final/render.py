from pathlib import Path
from hashlib import sha256
import base64
import json
import xml.etree.ElementTree as ET
from PIL import Image
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
DRAFT = OUT.parent / 'layered-06-proof' / 'adapted-layout.svg'
ASSET = OUT / 'subject-right.png'
EDGE = Path('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)

def tag(name):
    return '{' + NS + '}' + name

def main():
    draft = ET.parse(DRAFT).getroot()
    root = ET.fromstring(ET.tostring(draft))
    by_id = lambda ident: next(el for el in root.iter() if el.get('id') == ident)
    by_id('title').text = 'Dream Weaver — layered 06 composition proof'
    by_id('description').text = 'One generated photographic cocoon asset, mirrored for the left fragmented view, placed in the approved editable layout. Asset coverage limitations are documented outside the poster.'
    defs = root.find(tag('defs'))
    right = by_id('right-sculpture-mass')
    path = right.get('d')
    root.remove(right)
    for ident in ['left-local-pieces', 'left-local-cue', 'right-local-cue', 'left-view-direction', 'right-view-direction']:
        root.remove(by_id(ident))
    rc = ET.SubElement(defs, tag('clipPath'), {'id': 'right-photo-contour', 'clipPathUnits': 'userSpaceOnUse'})
    ET.SubElement(rc, tag('path'), {'id': 'right-sculpture-contour', 'd': path})
    data = 'data:image/png;base64,' + base64.b64encode(ASSET.read_bytes()).decode('ascii')
    ET.SubElement(defs, tag('image'), {'id': 'right-view-asset', 'width': '1024', 'height': '1536', 'href': data})
    right_layer = ET.Element(tag('g'), {'id': 'continuous-right-photo', 'clip-path': 'url(#right-photo-contour)'})
    ET.SubElement(right_layer, tag('use'), {'href': '#right-view-asset', 'transform': 'translate(297.5 -125.4) scale(1.05)'})
    left_layer = ET.Element(tag('g'), {'id': 'fragmented-left-mirrored-photo', 'clip-path': 'url(#left-local-view)'})
    windows = [(250,76,600,210,14),(250,300,600,235,0),(744,551,110,170,-16),(744,737,110,174,16),(744,927,110,175,-16),(744,1326,110,164,14)]
    for i,(x,y,w,h,offset) in enumerate(windows):
        cid = f'left-fragment-window-{i+1}'
        cp = ET.SubElement(defs, tag('clipPath'), {'id': cid, 'clipPathUnits': 'userSpaceOnUse'})
        ET.SubElement(cp, tag('rect'), {'x': str(x), 'y': str(y), 'width': str(w), 'height': str(h)})
        group = ET.SubElement(left_layer, tag('g'), {'id': f'left-photo-fragment-{i+1}', 'clip-path': f'url(#{cid})', 'data-horizontal-offset': str(offset)})
        ET.SubElement(group, tag('use'), {'href': '#right-view-asset', 'transform': f'translate({1598.5+offset} -607.8) scale(-1.25 1.25)'})
    title_index = list(root).index(by_id('adapted-title'))
    root.insert(title_index, right_layer)
    root.insert(title_index+1, left_layer)
    svg = OUT / 'poster.svg'
    ET.ElementTree(root).write(svg, encoding='utf-8', xml_declaration=True)
    (OUT / 'preview.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Dream Weaver — layered 06</title><style>html,body{margin:0;min-height:100%;background:#dedbd5}body{display:flex;justify-content:center;padding:24px;box-sizing:border-box}img{display:block;width:auto;max-width:100%;height:calc(100vh - 48px);object-fit:contain}</style><img id="poster" src="poster.png" alt="DREAM WEAVER — ONEIRLOOM"></html>', encoding='utf-8')
    errors=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path=str(EDGE))
        page=browser.new_page(viewport={'width':1450,'height':2040},device_scale_factor=1)
        page.on('pageerror',lambda error:errors.append(str(error)))
        page.goto(svg.as_uri(),wait_until='load')
        page.evaluate('document.fonts.ready')
        decoded=page.evaluate('''async () => Promise.all([...document.querySelectorAll('image')].map(async e => { const i=new Image(); i.src=e.getAttribute('href'); await i.decode(); return {width:i.naturalWidth,height:i.naturalHeight,loaded:i.complete}; }))''')
        page.locator('svg').screenshot(path=str(OUT/'poster.png'),animations='disabled')
        text=page.locator('text').evaluate_all('(es)=>es.map(e=>({id:e.id,text:e.textContent,font:getComputedStyle(e).fontFamily,size:getComputedStyle(e).fontSize}))')
        fonts=page.evaluate('({status:document.fonts.status,impactAvailable:document.fonts.check("300px Impact")})')
        page.goto((OUT/'preview.html').as_uri(),wait_until='load')
        preview=page.locator('img').evaluate('(i)=>i.decode().then(()=>({loaded:i.complete,width:i.naturalWidth,height:i.naturalHeight}))')
        browser.close()
    im=Image.open(ASSET)
    a=im.getchannel('A')
    hist=a.histogram()
    assets={'path':'subject-right.png','dimensions':list(im.size),'mode':im.mode,'sha256':sha256(ASSET.read_bytes()).hexdigest(),'alpha_extrema':list(a.getextrema()),'alpha_nonzero_bbox':a.getbbox(),'alpha_gt_127_bbox':a.point(lambda x:255 if x>127 else 0).getbbox(),'fully_transparent_fraction':hist[0]/(im.width*im.height),'alpha_corners':[a.getpixel(v) for v in [(0,0),(1023,0),(0,1535),(1023,1535)]],'manual_star_center':[780,780],'manual_star_bbox':[689,650,868,909]}
    receipt={'entry':'built-in image_gen.imagegen','generation_calls':1,'model':'unknown; tool did not expose model identifier','reference_images':[str(ROOT/'docs/assets/dream-cocoon/00-approved-reference.png')],'reference_role':'identity only','controls':{'transparent_background':True,'referenced_image_paths':'identity reference only'},'submitted_prompt':'submitted.en.txt','submitted_prompt_sha256':sha256((OUT/'submitted.en.txt').read_bytes()).hexdigest(),'tool_saved_path':'J:/Users/yangda01/.codex/generated_images/01a0fb7e-7107-7da2-a59a-281d130d7106/exec-88be24d2-2969-4ad9-a652-306e1f128cf2.png','asset':assets}
    (OUT/'generation.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    fixed=['paper','blue-panel','adapted-title','title-dream','title-weaver','adapted-footer','left-local-view']
    same={ident:ET.tostring(next(e for e in draft.iter() if e.get('id')==ident))==ET.tostring(by_id(ident)) for ident in fixed}
    checks={'unchanged_draft_elements':same,'right_contour_unchanged':by_id('right-sculpture-contour').get('d')==path,'exact_text':[e['text'] for e in text]==['DREAM','WEAVER','ONEIRLOOM'],'screenshot_dimensions':list(Image.open(OUT/'poster.png').size),'source_asset_embedded':True,'uniform_scales':{'right':1.05,'left_mirrored':1.25},'star_centers_on_page':{'right':[1116.5,693.6],'left_base':[623.5,367.2]},'fragment_offsets':[r[4] for r in windows],'native_alpha':assets,'browser':str(EDGE),'fonts':fonts,'decoded_asset':decoded,'preview':preview,'page_errors':errors,'technical_checks_passed':all(same.values()) and not errors and preview['loaded'],'visual_status':'coverage failure; root decision required before changing fixed layout or making another asset','observed_coverage_limit':{'right_asset_canvas_bottom':1487.4,'required_right_contour_bottom':2040,'left_asset_canvas_bottom':1312.2,'lower_left_window_starts':1326},'overall_accepted':False}
    (OUT/'assembly-checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
    print(json.dumps({'technical_checks_passed':checks['technical_checks_passed'],'visual_status':checks['visual_status'],'asset':assets,'text':text,'preview':preview,'page_errors':errors},indent=2))

if __name__=='__main__':
    main()
