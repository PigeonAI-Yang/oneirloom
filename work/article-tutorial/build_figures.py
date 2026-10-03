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


def board(filename, title, subtitle, panels, note="照片由同一工作流生成，标题和说明为后期添加"):
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
    d.text((38, 30), "01 / 先想好人物、动作、取景、房间和光线", font=font(38), fill=INK)
    canvas.paste(im, (38, 120))
    items = [
        ("01 人物", "成年女性、栗棕色长发、黑色发带与黑色缎面裙。"),
        ("02 动作", "站立，肩膀放松，两只手自然下垂。"),
        ("03 取景", "从头顶拍到鞋底，留意有没有裁掉头或脚。"),
        ("04 房间", "左侧电视柜，右侧床，远处房门，脚下木地板。"),
        ("05 光线", "左侧窗光；看脸、裙面和地板上的明暗变化。"),
    ]
    y = 162
    for label, detail in items:
        d.text((845, y), label, font=font(31), fill=ACCENT)
        text_lines(d, detail, (845, y+58), 510, size=26)
        y += 185
    d.text((38, 1190), "先看这些要求有没有做到，再补充装饰和风格。", font=font(22), fill=MUTED)
    canvas.save(OUT / "figure-01-plan.jpg", quality=94, subsampling=0)


plan()
board("figure-02-framing.jpg", "02 / 景别：照片拍到身体的哪个部位", "看照片下边缘到哪里，脸在画面里有多大", [
    ("19_close_fixed", "面部近照", "脸部明显放大，仍保留肩胸局部。"),
    ("20_half_fixed", "上半身取景", "看照片下边缘拍到了身体哪里。"),
    ("01_full", "全身取景", "头、裙摆和鞋都完整入画。"),
])
board("figure-03-camera.jpg", "03 / 机位：相机从哪里拍", "别只看人物抬头低头，也看地板、床面和天花板", [
    ("04_high", "从高处向下看", "地板与床面露出更多。"),
    ("01_full", "接近水平", "人物和房间看起来较接近平视。"),
    ("21_low_fixed", "从低处向上看", "看近处鞋子的大小和露出的天花板。"),
])
board("figure-04-direction.jpg", "04 / 朝向：分别看身体和头朝哪边", "看肩膀、衣服正反面和脸分别朝哪里", [
    ("01_full", "正面", "身体与目光都朝镜头。"),
    ("06_side", "侧身", "鼻尖、肩膀与脚尖朝一侧。"),
    ("07_back", "背身回头", "背部朝镜头，头向右肩转回。"),
])
board("figure-05-composition.jpg", "05 / 构图：人物放在哪里，房间留出多少", "先看人物站在哪里，再看两边露出了多少房间", [
    ("01_full", "人物居中", "人物在中间，两边都能看到家具。"),
    ("28_left_wood", "人物偏左", "右侧有更多空间展示房间。"),
])
board("figure-06-pose.jpg", "06 / 姿势：站得稳，坐得自然", "看脚怎样落地，身体怎样坐在椅子上", [
    ("01_full", "站立", "身体直立，双脚落地。"),
    ("09_seated", "坐椅", "坐在椅面上，膝盖弯曲。"),
    ("10_walk", "迈步", "两脚前后错开，手臂随动作变化。"),
])
board("figure-07-gaze.jpg", "07 / 眼神：看镜头，还是看画面外", "观察瞳孔方向，并检查头部有没有一起改变", [
    ("20_half_fixed", "看镜头", "像是在与看照片的人对视。"),
    ("23_gaze_fixed", "看向画外", "目光偏向画面右侧。"),
])
board("figure-08-hands.jpg", "08 / 手部动作：每只手放在哪里", "看手掌接触哪里，抬起的手在做什么", [
    ("09_seated", "双手放在膝盖上", "手与膝盖之间有明确接触。"),
    ("12_hairhand", "一手整理头发", "另一只手放在膝盖上。"),
])
board("figure-09-room.jpg", "09 / 场景：卧室里，家具怎样摆", "两张都是卧室，区别在于有没有写清家具的位置", [
    ("13_vague_scene", "只写卧室", "床和家具的位置由模型自行安排。"),
    ("01_full", "写清左右和远近", "左侧电视、右侧床，远处有门，地上铺木地板。"),
])
board("figure-10-fabric.jpg", "10 / 材质：颜色相同，表面不同", "观察光泽的形状与布面纹理", [
    ("20_half_fixed", "黑色缎面", "寻找平滑而连续的亮面。"),
    ("24_knit_fixed", "黑色针织", "寻找线圈、罗纹与哑光表面。"),
])
board("figure-11-light.jpg", "11 / 光线：比较阴影和房间明暗", "三种不同的照明方式，夜景中的房间也更暗", [
    ("20_half_fixed", "柔和日光", "脸部明暗过渡较柔和。"),
    ("25_hard_fixed", "直射日光", "看窗框投影和阴影的边缘。"),
    ("26_warm_fixed", "暖色台灯", "人物受暖光，房间背景更暗。"),
])
board("figure-12-focus.jpg", "12 / 背景：房间要不要看得清楚", "先看人物是否清楚，再看能否辨认家具", [
    ("20_half_fixed", "能辨认家具", "床和房门保留轮廓。"),
    ("27_blur_fixed", "背景更模糊", "家具边缘更模糊，仍能认出大致轮廓。"),
])
board("figure-13-complete.jpg", "13 / 完整提示词的实际结果", "依次检查人物、动作、取景、房间和光线", [
    ("01_full", "先保存这张全身照", "左侧电视、右侧床、远处房门，头与鞋完整入画。"),
])
board("figure-14-repair.jpg", "14 / 一次真实的景别修正", "模型、种子和图片尺寸相同，修改了取景要求", [
    ("02_close", "原稿要求特写，结果仍是全身", "提示词仍要求鞋与双手可见、房间布局完整。"),
    ("19_close_fixed", "修订后重新生成", "脸明显放大，仍露出一些肩胸。"),
])
board("figure-15-grid.jpg", "15 / 四宫格：人物相同，动作各有变化", "四格和白色分隔线都是一次生成的", [
    ("18_grid", "逐格检查", "左上坐床、右上回头、左下坐椅、右下靠墙。"),
])
board("figure-16-exercise.jpg", "16 / 练习：先把全身照改成近照", "重点改取景，也看看长相和背景有没有跟着变", [
    ("01_full", "保存原来的全身照", "连同提示词和生成参数一起保存。"),
    ("19_close_fixed", "比较修改后的近照", "看脸的大小、画框下缘和背景范围。"),
])
print("Built 16 teaching figures")
