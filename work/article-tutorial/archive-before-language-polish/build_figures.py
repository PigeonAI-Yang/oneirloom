from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "images"
PAPER = "#f5f1ea"
INK = "#292723"
MUTED = "#70675e"
ACCENT = "#9a593b"
FONT_PATH = "C:/Windows/Fonts/msyh.ttc"


def font(size):
    return ImageFont.truetype(FONT_PATH, size)


def text_lines(draw, text, xy, width, size=23, fill=INK, line_height=None):
    f = font(size)
    x, y = xy
    current = ""
    for c in text:
        if c == "\n" or draw.textlength(current + c, font=f) > width:
            draw.text((x, y), current, font=f, fill=fill)
            y += line_height or int(size * 1.55)
            current = "" if c == "\n" else c
        else:
            current += c
    if current:
        draw.text((x, y), current, font=f, fill=fill)
        y += line_height or int(size * 1.55)
    return y


def photograph(name):
    return Image.open(OUT / (name + ".png")).convert("RGB")


def board(filename, title, subtitle, panels, note="同一工作流实际出图 · 标签与对照排版为后期添加"):
    n = len(panels)
    width = 1560 if n >= 3 else (1000 if n == 1 else 1400)
    margin, gap = 36, 22
    cell = (width - margin * 2 - gap * (n - 1)) // n
    photo_height = 650 if n >= 3 else (1280 if n == 1 else 830)
    top = 142
    canvas = Image.new("RGB", (width, top + photo_height + 206), PAPER)
    d = ImageDraw.Draw(canvas)
    d.text((margin, 27), title, font=font(37), fill=INK)
    d.text((margin, 86), subtitle, font=font(22), fill=MUTED)
    for i, (name, label, detail) in enumerate(panels):
        x = margin + i * (cell + gap)
        img = photograph(name)
        img.thumbnail((cell, photo_height), Image.Resampling.LANCZOS)
        px = x + (cell - img.width) // 2
        py = top + (photo_height - img.height) // 2
        canvas.paste(img, (px, py))
        d.text((x, top + photo_height + 22), label, font=font(25), fill=ACCENT)
        text_lines(d, detail, (x, top + photo_height + 64), cell, size=21, fill=INK)
    d.text((margin, canvas.height - 34), note, font=font(17), fill=MUTED)
    canvas.save(OUT / filename, quality=94, subsampling=0)


def plan():
    im = photograph("01_full")
    im.thumbnail((760, 1050), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (1400, 1240), PAPER)
    d = ImageDraw.Draw(canvas)
    d.text((38, 30), "01 / 先安排这张照片里的五件事", font=font(38), fill=INK)
    canvas.paste(im, (38, 120))
    items = [
        ("01 人物", "成年女性、栗棕色长发、黑色发带与黑色缎面裙。"),
        ("02 动作", "站立，肩膀放松，两只手自然下垂。"),
        ("03 取景", "从头顶到鞋底；检查上下画框有没有截断身体。"),
        ("04 房间", "左侧电视柜，右侧床，远处房门，脚下木地板。"),
        ("05 光线", "左侧窗光；看脸、裙面和地板上的明暗变化。"),
    ]
    y = 162
    for label, detail in items:
        d.text((845, y), label, font=font(31), fill=ACCENT)
        text_lines(d, detail, (845, y+58), 510, size=26)
        y += 185
    d.text((38, 1190), "实际生成结果。先逐项找得到，再增加装饰与风格细节。", font=font(22), fill=MUTED)
    canvas.save(OUT / "figure-01-plan.jpg", quality=94, subsampling=0)


plan()
board("figure-02-framing.jpg", "02 / 景别：画框收进多少人物", "观察每张图的下边缘，以及脸在画面里占多大", [
    ("19_close_fixed", "面部近照", "脸部明显放大，仍保留肩胸局部。"),
    ("20_half_fixed", "上半身取景", "检查下缘实际切在身体哪里。"),
    ("01_full", "全身取景", "头、裙摆和鞋都完整入画。"),
])
board("figure-03-camera.jpg", "03 / 机位：我从哪里看她", "别只看人物抬头低头，也看地板、床面和天花板", [
    ("04_high", "从高处向下看", "地板与床面露出更多。"),
    ("01_full", "接近水平", "人物与房间比例较自然。"),
    ("21_low_fixed", "从低处向上看", "观察近远比例和上方空间。"),
])
board("figure-04-direction.jpg", "04 / 朝向：身体和头分别看", "判断依据是肩线、衣服正反面与脸的方向", [
    ("01_full", "正面", "身体与目光都朝镜头。"),
    ("06_side", "侧身", "鼻尖、肩膀与脚尖朝一侧。"),
    ("07_back", "背身回头", "背部朝镜头，头向右肩转回。"),
])
board("figure-05-composition.jpg", "05 / 构图：人在哪里，空间留给谁", "先找人物中轴，再比较两侧留出的环境", [
    ("01_full", "人物居中", "人物与两侧家具形成对照。"),
    ("28_left_wood", "人物偏左", "右侧有更多空间展示房间。"),
])
board("figure-06-pose.jpg", "06 / 姿势：身体靠什么支撑", "看脚底、椅面与身体接触点", [
    ("01_full", "站立", "身体直立，双脚落地。"),
    ("09_seated", "坐椅", "臀部落在椅面，膝盖弯曲。"),
    ("10_walk", "迈步", "两脚前后错开，手臂随动作变化。"),
])
board("figure-07-gaze.jpg", "07 / 目光：看镜头还是看画外", "观察瞳孔方向，并检查头部有没有一起改变", [
    ("20_half_fixed", "看镜头", "目光与读者直接相接。"),
    ("23_gaze_fixed", "看向画外", "目光偏向画面右侧。"),
])
board("figure-08-hands.jpg", "08 / 手的位置：每只手都有落点", "看手掌接触哪里，抬起的手在做什么", [
    ("09_seated", "双手放在膝盖上", "手与膝盖之间有明确接触。"),
    ("12_hairhand", "一手整理头发", "另一只手留在膝上，分工清楚。"),
])
board("figure-09-room.jpg", "09 / 场景：房间类别与布局是两件事", "简单提示也能出卧室；明确关系是为了约定具体位置", [
    ("13_vague_scene", "只给房间类别", "家具由这次生成自行安排。"),
    ("01_full", "明确左右与远近", "左电视、右床、远处门、木地板。"),
])
board("figure-10-fabric.jpg", "10 / 材质：颜色相同，表面不同", "观察光泽的形状与布面纹理", [
    ("20_half_fixed", "黑色缎面", "寻找平滑而连续的亮面。"),
    ("24_knit_fixed", "黑色针织", "寻找线圈、罗纹与哑光表面。"),
])
board("figure-11-light.jpg", "11 / 光线：方向、阴影和房间气氛", "这些是三种完整拍法，夜景同时改变了环境亮度", [
    ("20_half_fixed", "柔和日光", "脸部明暗过渡较柔和。"),
    ("25_hard_fixed", "直射日光", "观察窗框投影与明暗边界。"),
    ("26_warm_fixed", "暖色台灯", "人物受暖光，房间背景更暗。"),
])
board("figure-12-focus.jpg", "12 / 背景：要不要让房间讲信息", "同样观察脸与肩，再看家具还能否辨认", [
    ("20_half_fixed", "环境仍可辨", "床和房门保留轮廓。"),
    ("27_blur_fixed", "背景更模糊", "家具弱化成色块，人物更突出。"),
])
board("figure-13-complete.jpg", "13 / 完整提示词的实际结果", "检查顺序：人物 → 动作 → 取景 → 房间 → 光线", [
    ("01_full", "保留这张作为起点", "左侧电视、右侧床、远处房门，头与鞋完整入画。"),
])
board("figure-14-repair.jpg", "14 / 一次真实的景别修正", "同模型、同种子、同画幅；修订裁切与可见内容的描述", [
    ("02_close", "原稿要求特写，结果仍是全身", "提示词仍要求鞋与双手可见、房间布局完整。"),
    ("19_close_fixed", "修订后重新生成", "把画面内容收紧为脸、颈部与少量双肩。"),
])
board("figure-15-grid.jpg", "15 / 四宫格：共同设定，分别安排动作", "四格由一次模型生成完成，白色分隔线来自生成结果", [
    ("18_grid", "逐格检查", "左上坐床、右上回头、左下坐椅、右下靠墙。"),
])
board("figure-16-exercise.jpg", "16 / 练习：先把全身照改成近照", "这次只处理取景目标；记录人物外观等附带变化", [
    ("01_full", "保留一张起点图", "保存完整提示词和实际参数。"),
    ("19_close_fixed", "检查修改是否到位", "看脸的大小、画框下缘和背景范围。"),
])
print("Built 16 teaching figures")
