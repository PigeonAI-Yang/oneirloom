import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
jobs = json.loads((ROOT / "jobs.json").read_text(encoding="utf-8"))
person = "一位25岁的东亚成年女性，鹅蛋脸，深棕色眼睛，栗棕色微卷长发，黑色缎带蝴蝶结固定半扎发，脸侧少量碎发，自然淡妆，柔和粉色唇，真实皮肤纹理。"
outfit = "黑色细肩带缎面衣料，领口镶细窄花卉蕾丝，腰部合身，布料呈柔和流动高光。"
day = "柔和日光从画面左侧照入，脸部左侧明亮，右侧留有淡淡阴影，肤色自然暖亮。"
half = "写实近距离上半身人像，画框下缘紧贴人物腰线，头顶接近画框上缘，头、双肩和腰部填满竖幅画面，人物身体的腰线以下处于画框外。相机与双眼同高，正面水平拍摄。"
background = "背景是卧室浅米色墙壁，左侧边缘可见一部分电视柜，右侧边缘可见一部分白床品，较远处有深棕色房门局部，家具轮廓仍可辨认。"


def add(name, text):
    if not any(j["id"] == name for j in jobs):
        jobs.append(dict(id=name, prompt=text, seed=2026092807, revision="After inspecting initial crop and viewpoint misses"))


add("19_close_fixed", "写实面部特写肖像，整张脸占画面高度约七成，头顶靠近画面上缘，画框下缘切在锁骨下方，只呈现头部、颈部和一小部分双肩。相机接近眼睛高度。" + person + "目光直视镜头，嘴唇轻闭，表情平静。肩部可见黑色细肩带和少量缎面领口。" + day + "背景是柔和的卧室米色墙面与深棕色门的局部色块。")
add("20_half_fixed", half + person + outfit + "肩膀放松，头部朝向正前方，目光直视镜头，嘴唇轻闭。" + background + day)
add("21_low_fixed", "写实竖幅全身摄影，极低机位，摄影机贴近地面，在人物脚踝高度向上仰拍，画面从近处黑色平底鞋向上延伸到较远的脸。近处的鞋和腿比远处头部明显放大，人物站得高，后方门框竖线向画面上方汇聚，天花板和墙面上部占据大半背景。" + person + "黑色细肩带缎面及膝连衣裙，领口花卉蕾丝，双臂自然下垂，低头看向低处镜头。人物从鞋到头完整入画。家中卧室，右侧白床的侧沿、左侧电视柜下部和后方深棕色门形成空间参照。" + day)
add("22_left_fixed", "写实竖幅环境全身人像。人物站在画面最左侧，人物中轴位于整张画面宽度的四分之一处，右侧超过一半画幅用于展示白色床铺和米色墙面。头顶到黑色平底鞋完整入画，人物占画面高度约八成。" + person + "黑色细肩带缎面及膝连衣裙，领口花卉蕾丝，腰部合身。正面站立，双臂放松下垂，目光看镜头。家中卧室，左边缘是木质电视柜，右半幅是白色床和墙，远处深棕色房门。" + day)
add("23_gaze_fixed", half + person + outfit + "肩膀放松，头部朝向正前方，两只眼睛的瞳孔都向画面右侧移动，视线看向画外右侧，嘴唇轻闭，表情平静。" + background + day)
add("24_knit_fixed", half + person + "黑色细肩带粗针织衣料，领口细窄蕾丝，腰部合身，黑色线圈和纵向罗纹清楚，布料表面哑光。肩膀放松，头部朝向正前方，目光直视镜头，嘴唇轻闭。" + background + day)
add("25_hard_fixed", half + person + outfit + "肩膀放松，正对镜头，目光直视镜头，嘴唇轻闭。" + background + "强烈直射阳光从画面左侧窗户照入，窗框投下的一道深色阴影斜穿脸颊与肩膀，明暗交界边缘清楚。受光面明亮，背光面明显暗淡，缎面有集中的亮面反光。")
add("26_warm_fixed", half + person + outfit + "肩膀放松，正对镜头，目光直视镜头，嘴唇轻闭。" + background + "夜晚室内，左侧一盏带米色布艺灯罩的床头灯发出暖琥珀色光，照亮左侧脸颊，右侧脸颊处于柔和暗部，房间背景明显暗于人物，床铺与墙面呈现深暖棕色，黑色缎面保留柔和光泽。")
add("27_blur_fixed", half + person + outfit + "肩膀放松，头部朝向正前方，目光直视镜头，嘴唇轻闭。" + "背景是卧室浅米色墙壁、左侧电视柜、右侧白床品和较远的深棕色房门。浅景深，双眼、发丝和衣料清晰，背景家具完全失焦成模糊色块，边缘柔化。" + day)
(ROOT / "jobs.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
print(len(jobs), "total jobs")
