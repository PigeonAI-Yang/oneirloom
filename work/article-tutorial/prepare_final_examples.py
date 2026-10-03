import json
from pathlib import Path

root = Path(__file__).resolve().parent
path = root / 'jobs.json'
jobs = json.loads(path.read_text(encoding='utf-8'))
source = {j['id']: j for j in jobs}
new = [
    ('e32_focus_flowers_fixed', 'e27_focus_flowers', '室内花束静物摄影，焦点严格落在距离镜头30厘米的粉白花束上，花束占画面左侧一半，花瓣纹理与花蕊锐利。极浅景深，花束后方3米处的床沿坐着一位25岁成年女性，穿黑色吊带裙，棕色长发带黑色蝴蝶结。远处人物是明显失焦的柔软色块，脸部五官无法分辨，只能辨认坐姿与服装颜色。花束与人物之间有很大的距离。镜头聚焦花朵，背景床铺、人物与米色墙面全部形成强烈光学散焦，窗边柔和日光，横幅写实照片。'),
    ('e33_environment_fixed', 'e15_environment', '从宽大卧室入口向内远距离拍摄的横幅室内空间照片，画面以房间建筑和家具为主。完整展示天花板、左右墙面、大面积近处木地板，右侧床铺、左侧电视柜、远处深棕色门。人物在远端门前，距离相机约6米，是画面中一个很小的完整站立人影，仅占画面高度四成；头顶上方与脚下都有大量房间空间。人物是一位25岁成年女性，栗棕色长发、黑色蝴蝶结，黑色细肩带及膝连衣裙和黑色平底鞋，身体正面，双臂下垂。不需要看清脸部细节。家中卧室，窗户从画面左侧透入柔和日光，床、电视柜与木地板清楚可见，真实室内摄影。'),
    ('e34_mug_fixed', 'e22_mug', '竖幅腰部以上照片，完整展示双臂与手。一位25岁成年女性坐在家中卧室，栗棕色长发、黑色蝴蝶结、黑色细肩带缎面裙，微笑看向镜头。一个白色陶瓷杯竖直放在她左手向上摊平的手掌上，左掌是水平托盘，杯底压在掌心，左手指朝侧方伸展，位于杯子下方；右手从侧面握住杯把，稳定杯子。左手在下、右手在侧，两手呈上下错开的关系。杯子位于胸口下方，全部杯底和托底手掌可见。背景右侧床铺、左侧电视柜、木地板，左侧柔和窗光，写实摄影。'),
]
for key, base, prompt in new:
    if key not in source:
        jobs.append({**source[base], 'id':key, 'prompt':prompt})
path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding='utf-8')
