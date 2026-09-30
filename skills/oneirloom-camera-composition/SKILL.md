---
name: oneirloom-camera-composition
description: 将景别、机位、视角、透视、遮挡、裁切和运动意图写成明确的画面空间关系。用于摄影、电影感、广角仰拍、俯拍、主体布局和参考图构图复现。
---

# 镜头与构图语言

从相机位置、相机朝向、主体相对位置、远近尺度、边缘裁切、前后遮挡六项里选择必要内容。焦段词只描述视觉效果；未确认设备时不写具体毫米数。

For reference reconstruction with strong perspective, map three projected scales before writing the prompt: the nearest foreground element, the subject's head/torso, and the largest background form. Record their apparent frame-width or frame-height shares, overlap, and edge crops, plus the camera's apparent proximity to the nearest element and the direction of its optical axis. Express the decisive relations as affirmative, visible geometry in the prompt; a low-angle label alone does not preserve foreground exaggeration. Keep this scale map when changing medium, such as from illustration to realistic photography. In result comparisons, check actual frame proportions before attributing a scale mismatch to aspect ratio.

For a person pose, trace each important limb through its visible joints before choosing a pose label. Describe joint extension or flexion separately from the limb's direction in the frame. Crossed straight legs can form diagonal lines while both knees remain extended. State the knee condition, crossing height, and front/back order when these define the reference. A cropped ankle or foot does not establish a planted-foot stance or which leg carries the weight.

用户指定人像景别或裁切时，把景别落实到画框上下边界和身体地标，例如头顶至腰部、下缘截在腰线；裁切决定结果时可补主体在画面中的占比，不只重复“半身”一类景别词。动作或抓拍意图要写成进行中的可见瞬间，用身体朝向、重心变化、肢体动作或衣发惯性等相关线索呈现动作过程；静态肖像则保留静态姿势，不额外制造动势。

当躯干朝向、转头、视线与肢体动作的关系决定结果时，分别写清这些关系；仅有发丝或衣角动势，不等于人物完成了指定的回头动作。精确景别还需核对画幅比例、身体地标与主体占比，并检查背景等其他构图要求是否与裁切目标冲突。连续受控生成仍越过裁切边界时，转入结果诊断，不继续叠加景别同义词。

| 用户表达 | 可执行关系示例 |
| --- | --- |
| 强烈仰拍 | 相机在主体下方近距离向上；主体上部朝画面高处延伸；近处部位明显放大 |
| 压缩空间 | 远近物体的表观尺寸差缩小，背景层次紧贴主体 |
| 抓拍感 | 身体动作处于过渡瞬间，发丝或衣料呈同一方向动势，表情自然 |
| 大留白 | 明确主体在哪一侧，以及空白区域的位置和占比 |

优先写具体空间关系：“脸在画面上方，近侧肩膀抬至下巴旁，躯干斜向右下延伸，膝盖进入前景”。一个词如“广角仰拍”不足以锁定遮挡和裁切。夸张透视可能影响比例与面部，必须与用户期望核对；不要给没有依据的光圈、胶片或品牌名。
