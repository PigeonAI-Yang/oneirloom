from pathlib import Path
from hashlib import sha256
import base64
import json
import io
import copy
import xml.etree.ElementTree as ET
from PIL import Image, ImageChops
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
    ET.SubElement(right_layer, tag('use'), {'href': '#right-view-asset', 'transform': 'translate(-703.5 -690.8) scale(2.3)'})
    left_layer = ET.Element(tag('g'), {'id': 'fragmented-left-mirrored-photo', 'clip-path': 'url(#left-local-view)'})
    windows = [(250,76,600,210,14),(250,300,600,235,0),(744,551,110,170,-16),(744,737,110,174,16),(744,927,110,175,-16),(744,1326,110,164,14)]
    for i,(x,y,w,h,offset) in enumerate(windows):
        cid = f'left-fragment-window-{i+1}'
        cp = ET.SubElement(defs, tag('clipPath'), {'id': cid, 'clipPathUnits': 'userSpaceOnUse'})
        ET.SubElement(cp, tag('rect'), {'x': str(x), 'y': str(y), 'width': str(w), 'height': str(h)})
        group = ET.SubElement(left_layer, tag('g'), {'id': f'left-photo-fragment-{i+1}', 'clip-path': f'url(#{cid})', 'data-horizontal-offset': str(offset)})
        ET.SubElement(group, tag('use'), {'href': '#right-view-asset', 'transform': f'translate({1885.75+offset} -616.2) scale(-1.65 1.65)'})
    title_index = list(root).index(by_id('adapted-title'))
    root.insert(title_index, right_layer)
    root.insert(title_index+1, left_layer)
    svg = OUT / 'poster.svg'
    ET.ElementTree(root).write(svg, encoding='utf-8', xml_declaration=True)
    (OUT / 'preview.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Dream Weaver — layered 06</title><style>html,body{margin:0;min-height:100%;background:#dedbd5}body{display:flex;justify-content:center;padding:24px;box-sizing:border-box}img{display:block;width:auto;max-width:100%;height:calc(100vh - 48px);object-fit:contain}</style><img id="poster" src="poster.png" alt="DREAM WEAVER — ONEIRLOOM"></html>', encoding='utf-8')
    errors=[]
    coverage={}
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
        overflow=page.evaluate('({width:innerWidth,height:innerHeight,scrollWidth:document.documentElement.scrollWidth,scrollHeight:document.documentElement.scrollHeight})')
        page.goto('about:blank')
        def layer_alpha(layer):
            test=ET.Element(tag('svg'),{'width':'1450','height':'2040','viewBox':'0 0 1450 2040'})
            test.append(copy.deepcopy(defs))
            test.append(copy.deepcopy(layer))
            page.set_content('<style>html,body{margin:0;background:transparent}</style>'+ET.tostring(test,encoding='unicode'))
            page.evaluate('''async () => Promise.all([...document.querySelectorAll('image')].map(async e => {const i=new Image();i.src=e.getAttribute('href');await i.decode();}))''')
            return Image.open(io.BytesIO(page.locator('svg').screenshot(omit_background=True))).getchannel('A').point(lambda v:255 if v>127 else 0)
        target_right=ET.Element(tag('path'),{'d':path,'fill':'white'})
        target_left=copy.deepcopy(next(e for e in draft.iter() if e.get('id')=='left-local-pieces'))
        for name,actual_layer,target_layer in [('right',right_layer,target_right),('left',left_layer,target_left)]:
            target_alpha=layer_alpha(target_layer)
            actual_alpha=layer_alpha(actual_layer)
            occupied=ImageChops.multiply(target_alpha,actual_alpha)
            missing=ImageChops.subtract(target_alpha,occupied)
            count=target_alpha.histogram()[255]
            coverage[name]={'target_pixels':count,'occupied_pixels':occupied.histogram()[255],'occupied_fraction':occupied.histogram()[255]/count,'missing_bbox':missing.getbbox(),'occupied_bbox':occupied.getbbox()}
            bands=[(0,0,1450,551),(0,1326,1450,1490),(0,1900,1450,2040)]
            coverage[name]['bands']=[]
            for box in bands:
                n=target_alpha.crop(box).histogram()[255]
                o=occupied.crop(box).histogram()[255]
                coverage[name]['bands'].append({'box':box,'target_pixels':n,'occupied_pixels':o,'occupied_fraction':o/n if n else None})
        page.goto((OUT/'preview.html').as_uri(),wait_until='load')
        preview=page.locator('img').evaluate('(i)=>i.decode().then(()=>({loaded:i.complete,width:i.naturalWidth,height:i.naturalHeight}))')
        preview['no_horizontal_overflow']=page.evaluate('document.documentElement.scrollWidth<=innerWidth')
        browser.close()
    im=Image.open(ASSET)
    a=im.getchannel('A')
    hist=a.histogram()
    assets={'path':'subject-right.png','dimensions':list(im.size),'mode':im.mode,'sha256':sha256(ASSET.read_bytes()).hexdigest(),'alpha_extrema':list(a.getextrema()),'alpha_nonzero_bbox':a.getbbox(),'alpha_gt_127_bbox':a.point(lambda x:255 if x>127 else 0).getbbox(),'fully_transparent_fraction':hist[0]/(im.width*im.height),'alpha_corners':[a.getpixel(v) for v in [(0,0),(1023,0),(0,1535),(1023,1535)]],'manual_star_center':[765,596],'manual_star_bbox':[699,500,831,692]}
    receipt={'entry':'built-in image_gen.imagegen','generation_calls':1,'model':'unknown; tool did not expose model identifier','reference_images':[str(OUT.parent/'layered-06-final/subject-right.png'),str(ROOT/'docs/assets/dream-cocoon/00-approved-reference.png')],'reference_role':'previous asset pose and material; approved frontal identity','controls':{'transparent_background':True,'referenced_image_paths':'identity reference only'},'submitted_prompt':'submitted.en.txt','submitted_prompt_sha256':sha256((OUT/'submitted.en.txt').read_bytes()).hexdigest(),'tool_saved_path':'J:/Users/yangda01/.codex/generated_images/01a0fb8b-d17b-7511-bbd9-c4a1134fe207/exec-f1af9c28-a400-4745-94c2-9164ad61307c.png','asset':assets}
    (OUT/'generation.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    fixed=['paper','blue-panel','adapted-title','title-dream','title-weaver','adapted-footer','left-local-view']
    same={ident:ET.tostring(next(e for e in draft.iter() if e.get('id')==ident))==ET.tostring(by_id(ident)) for ident in fixed}
    checks={'unchanged_draft_elements':same,'right_contour_unchanged':by_id('right-sculpture-contour').get('d')==path,'exact_text':[e['text'] for e in text]==['DREAM','WEAVER','ONEIRLOOM'],'screenshot_dimensions':list(Image.open(OUT/'poster.png').size),'source_asset_embedded':True,'uniform_scales':{'right':2.3,'left_mirrored':1.65},'star_centers_on_page':{'right':[1056,680],'left_base':[623.5,367.2]},'fragment_offsets':[r[4] for r in windows],'native_alpha':assets,'browser':str(EDGE),'fonts':fonts,'decoded_asset':decoded,'preview':preview,'page_errors':errors,'technical_checks_passed':all(same.values()) and not errors and preview['loaded'],'visual_status':'coverage failure; root decision required before changing fixed layout or making another asset','observed_coverage_limit':{'right_asset_canvas_bottom':2842.0,'required_right_contour_bottom':2040,'left_asset_canvas_bottom':1918.2,'lower_left_window_starts':1326},'overall_accepted':False}
    (OUT/'assembly-checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
    receipt['controls']['referenced_image_paths']='previous right-facing asset and approved frontal identity; no layout reference'
    receipt['asset']['prompt_star_center_height_fraction']=[0.22,0.28]
    receipt['asset']['observed_star_center_height_fraction']=596/1536
    receipt['asset']['observed_star_width_fraction']=132/1024
    receipt['asset']['prompt_match_status']='partial: star width is within requested range; star remains too low; panel remains taller than upper third'
    receipt['reference_sha256']={p:sha256(Path(p).read_bytes()).hexdigest() for p in receipt['reference_images']}
    checks['native_alpha_coverage']=coverage
    checks['document_extent']=overflow
    checks['visual_status']='partial: lower coverage repaired; left upper occupied contour still misses draft; large panel and star required for right upper coverage'
    checks['observed_coverage_limit']={'right_asset_canvas_bottom':2842.0,'required_right_contour_bottom':2040,'left_asset_canvas_bottom':1918.2,'required_left_window_bottom':1490,'actual_alpha_coverage':'See native_alpha_coverage; canvas bounds alone are not acceptance evidence.'}
    checks['fragment_windows_unchanged']=[dict(e.attrib) for e in target_left]==[{'x':str(x),'y':str(y),'width':str(w),'height':str(h)} for x,y,w,h,_ in windows]
    checks['poster_sha256']=sha256((OUT/'poster.png').read_bytes()).hexdigest()
    checks['svg_sha256']=sha256(svg.read_bytes()).hexdigest()
    checks['technical_checks_passed']=all(same.values()) and checks['fragment_windows_unchanged'] and not errors and preview['loaded'] and fonts['impactAvailable'] and list(Image.open(OUT/'poster.png').size)==[1450,2040]
    (OUT/'generation.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    (OUT/'assembly-checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
    print(json.dumps({'coverage':coverage,'document_extent':overflow},indent=2))
    print(json.dumps({'technical_checks_passed':checks['technical_checks_passed'],'visual_status':checks['visual_status'],'asset':assets,'text':text,'preview':preview,'page_errors':errors},indent=2))

if __name__=='__main__':
    main()
