import json, time, os, sys, urllib.request, urllib.parse

BASE = "http://127.0.0.1:8188"
OUT_DIR = r"J:\PigeonYang\skills\oneirloom\gen"

POSITIVE = """写实手机随手拍质感，3:4 竖幅，全身入画。第1张参考图为准：参考图定义人物的长相、发型妆容、蹲姿姿势、身体朝向、构图与镜头，按参考图生成同一画面。

身体特征：大长腿、臀部饱满圆润、腰细、肩窄、头小——可见身段约为六个半头高，脸宽约为肩宽的五分之二；腿长明显长于躯干，膝盖到脚踝的可见小腿约有两个头高，小腿肚约为半张脸宽，脚踝极细、踝围不到小腿肚的一半；膝盖窄小，膝宽约等于一张脸宽。

姿势与相机：姿势、朝向与构图完全依据第1张参考图——正面微侧的深蹲，胸口与双膝朝向观者，臀部向画面左下方突出；相机离人物很近，约在胸口高度、接近水平并略下俯，膝盖离镜头最近；人物位置略偏画左，头顶约在画面上四分之一处，脚底几乎贴到画面下缘。

出彩焦点：极短的黑色短裤缩到胯上只剩腰头，圆润光洁的臀部与大腿上段大面积裸露，在画面左下形成约一个半头高的裸露弧形轮廓；她的一只手臂沿体侧下垂、肘部微屈，指尖正好搭在这段裸露弧线的下缘、紧挨蕾丝袜口边缘，手腕戴红金串珠手链；另一只手臂被躯干和膝盖完全遮挡不可见。

头部与面部：正脸朝镜头，目光平视镜头，下巴微收；深色头发向后收拢成蓬松发包，发包高约为头高的三分之一，几缕碎发垂在颊侧；肤色白皙，眼下腮红明显，粉色水光唇微张，双耳戴珍珠耳坠。

服装：她穿 oversize 黑色短袖T恤，落肩、袖口在肘上方，胸口有大面积白色单色照片风印花，衣摆堆在胯部与大腿根。黑色短裤极短，蹲姿下只剩胯后侧的腰头可见，腰头上有两粒小金属扣。双腿穿高透明度黑丝袜，肤色透出，小腿带浅色反光；宽幅荷叶边黑蕾丝袜口位于大腿中段，蕾丝属于丝袜而不是短裤，近侧袜口在阴影里略带蓝调；短裤与袜口之间是大面积裸露的臀腿皮肤。双脚都穿黑色漆皮尖头细高跟鞋，鞋头尖锐、鞋面有明亮高光、细跟触地，高跟鞋把小腿线条绷直拉长。

环境：身后是暖白色大规格瓷砖墙，右上方墙面上装白色擦手纸圆角方盒（正面有深色圆口）和白色电源插座，右上角裁入深色木框镜子；画面右侧一列白色台面厚边与深胡桃木高柜向右下延伸；地面为哑光深灰棕色大砖，她的软影投在身前偏右的地面。

光：暖调柔和室内光，整体微暗调、四周轻微暗角，左上方墙面有一道斜向亮痕；写实手机摄影质感，轻微噪点柔化。

装饰贴纸（后期叠加风格）：左上角手绘粉色郁金香配绿色花茎；六七枚粉色蝴蝶结贴纸散布在头部周围；头顶偏右一枚金棕色椒盐卷饼贴纸；一枚亮闪闪的金色星星贴纸随机点缀在头部附近——只有一枚，位置随意、不接触皮肤、与五官无关。"""

NEGATIVE = ""

wf = {
    "4": {"class_type": "UNETLoader", "inputs": {
        "unet_name": "qwen_image_2.1_int8_convrot.safetensors", "weight_dtype": "default"}},
    "5": {"class_type": "CLIPLoader", "inputs": {
        "clip_name": "qwen3vl_8b_int8_convrot.safetensors", "type": "qwen_image", "device": "default"}},
    "6": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_2.1_vae_bf16.safetensors"}},
    "7": {"class_type": "TextEncodeQwenImage21", "inputs": {
        "clip": ["5", 0], "prompt": POSITIVE, "negative_prompt": NEGATIVE, "resolution": 1024,
        "images": {"image_1": ["19", 0]}}},
    "19": {"class_type": "LoadImage", "inputs": {"image": "oneirloom_ref_source.png"}},
    "17": {"class_type": "ResolutionSelector", "inputs": {
        "aspect_ratio": "3:4 (Portrait Standard)", "megapixels": 2.0, "multiple": 8}},
    "8": {"class_type": "EmptyLatentImage", "inputs": {
        "width": ["17", 0], "height": ["17", 1], "batch_size": 1}},
    "9": {"class_type": "KSampler", "inputs": {
        "model": ["4", 0], "positive": ["7", 0], "negative": ["7", 1], "latent_image": ["8", 0],
        "seed": 20260930, "steps": 40, "cfg": 1.0, "sampler_name": "euler", "scheduler": "simple",
        "denoise": 1.0}},
    "15": {"class_type": "VAEDecode", "inputs": {"samples": ["9", 0], "vae": ["6", 0]}},
    "16": {"class_type": "SaveImage", "inputs": {
        "images": ["15", 0], "filename_prefix": "oneirloom_gen/reverse_20260930_v10_ref"}},
}


def http_json(path, data=None, timeout=30):
    if data is not None:
        req = urllib.request.Request(BASE + path, data=json.dumps(data).encode("utf-8"),
                                     headers={"Content-Type": "application/json"})
    else:
        req = BASE + path
    return json.load(urllib.request.urlopen(req, timeout=timeout))


r = http_json("/prompt", {"prompt": wf, "client_id": "zcode-oneirloom"})
pid = r.get("prompt_id")
print("submitted prompt_id:", pid, flush=True)

deadline = time.time() + 570  # keep under the 10-min shell cap; re-poll if needed
last_note = 0
while time.time() < deadline:
    time.sleep(15)
    h = http_json(f"/history/{pid}")
    if pid not in h:
        if time.time() - last_note > 60:
            q = http_json("/queue")
            running = len(q.get("queue_running", []))
            pending = len(q.get("queue_pending", []))
            print(f"waiting... queue_running={running} queue_pending={pending}", flush=True)
            last_note = time.time()
        continue
    entry = h[pid]
    status = entry.get("status", {})
    print("status:", status.get("status_str"), "completed:", status.get("completed"), flush=True)
    if status.get("status_str") == "error":
        msgs = [m for m in status.get("messages", []) if m and m[0] == "execution_error"]
        print(json.dumps(msgs, ensure_ascii=False)[:2000], flush=True)
        sys.exit(2)
    if status.get("completed"):
        os.makedirs(OUT_DIR, exist_ok=True)
        saved = []
        for node_id, node_out in entry.get("outputs", {}).items():
            for img in node_out.get("images", []):
                q = urllib.parse.urlencode({"filename": img["filename"],
                                            "subfolder": img.get("subfolder", ""),
                                            "type": img.get("type", "output")})
                blob = urllib.request.urlopen(BASE + "/view?" + q, timeout=120).read()
                path = os.path.join(OUT_DIR, img["filename"])
                with open(path, "wb") as f:
                    f.write(blob)
                saved.append((path, len(blob)))
                print("saved:", path, len(blob), "bytes", flush=True)
        if not saved:
            print("completed but no images in outputs:", json.dumps(entry.get("outputs", {}), ensure_ascii=False)[:1000], flush=True)
            sys.exit(3)
        sys.exit(0)
print("STILL_RUNNING after 570s; re-run poll for", pid, flush=True)
sys.exit(1)
