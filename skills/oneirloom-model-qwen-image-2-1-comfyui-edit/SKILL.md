---
name: oneirloom-model-qwen-image-2-1-comfyui-edit
description: 在本地 ComfyUI 上编排 Qwen-Image-2.1 图像编辑流程：先判断需求属于真编辑还是重绘，据此接线、设置 denoise、控制画幅、分配多参考图角色，按官方 I2I 规则写编辑提示词，并在交付前验证改动范围、画幅与身份一致性。
---

# ComfyUI image-editing workflow for Qwen-Image-2.1

Read the [shared interaction contract](../oneirloom/references/interaction-contract.md) before the first substantive response unless its unchanged content is already available. For person prompts, including new images and grid panels, read [person defaults and proportions](../oneirloom/references/person-prompts.md).

本技能负责**执行层**：把已经确认的视觉意图落到一个可运行的图像编辑流程上，并核对结果是否真的只改了指定部分。提示词的写作规则仍以 [Qwen-Image-2.1 适配器](../oneirloom-model-qwen-image-2-1/SKILL.md)及其[官方 I2I 文档](../oneirloom-model-qwen-image-2-1/references/official/pe-i2i-system-prompt.txt)为准；本技能不替代它。

## When to use

- 要在本地 ComfyUI 上用 Qwen-Image-2.1 修改一张已有图像
- 用户报告"改了这里结果整张都变了"、"构图被改了"、"画幅变成正方形了"、"镜里镜外不是同一个人"
- 需要判断某个需求是否属于可编辑范围

不要把本技能用于纯文生图或纯提示词交付；那两条路径归适配器与摄影／设计方法。

## 1. 先分类：真编辑，还是重绘

这一步决定后面全部参数，必须先做。

| 需求 | 性质 | 做法 |
| --- | --- | --- |
| 改一个属性：长度、颜色、材质、明暗、局部细节 | 真编辑 | 从已有图 latent 起步，低 denoise |
| 换服装、加删物件、明显改姿态细节 | 真编辑（幅度较大） | 从已有图 latent 起步，中等 denoise |
| 换机位、转身、换朝向、换场景、改人物骨架 | 重绘 | 回到文生图，在提示词里重写机位与朝向 |

判据只有一处：**KSampler 的 `latent_image` 接的是什么**。

- 接已有图的编码结果 → 是真编辑，图像结构在去噪中被逐步修正
- 接 `EmptyLatentImage`（纯噪声）→ 是重绘；此时输入图只通过 conditioning 起引导作用，**画面结构会被完全重排**，提示词里写"保持构图不变"不会生效

### 一条必须记住的边界

**结构性改动（机位、朝向、骨架）不能靠编辑完成，调高 denoise 也不行。** 实测把 denoise 从 0.62 提到 0.85 试图让人物转身 90°，两版结果几乎一致，身体朝向纹丝不动。`img2img` 能改属性，改不了骨架与朝向；这类需求直接回文生图，并在提示词里写清相机方位、人物朝向、以及画面各处分别看到什么。

## 2. 两条可用的真编辑接线

### A. VAEEncode 路径（优先，最可控）

```
LoadImage ──► VAEEncode ──► latent ──────────────┐
                                                 ├──► KSampler ──► VAEDecode ──► SaveImage
VAELoader ──►（VAE 同时供给 VAEEncode / VAEDecode / TextEncodeQwenImage21）
参考图 LoadImage ──► TextEncodeQwenImage21.images.image_1 …
```

`KSampler.denoise` 设 0.4–0.7。输出画幅等于输入图尺寸，因此应先把输入图裁到目标比例。

### B. 参考图 latent 路径

`TextEncodeQwenImage21` 的第 3 个输出（latent）直接接 `KSampler.latent_image`。这条路径的输出尺寸跟随参考图；`resolution` 填具体数值会缩放参考图并改变输出画幅。

## 3. denoise 档位

| 目标 | denoise |
| --- | --- |
| 单个属性（长度、颜色、材质、明暗） | 0.40–0.55 |
| 换服装、加删物件、姿态细节 | 0.55–0.70 |
| 结构性改动 | 编辑不可用，改走文生图 |

`cfg` 保持 1.0，负向提示词留空。

## 4. 画幅与分辨率

- 输出画幅由 `latent_image` 的尺寸决定。
- `VAEEncode` 路径：画幅 = 输入图尺寸。
- 参考图 latent 路径：`resolution=0` 表示按参考图自身尺寸、对齐 32 的倍数。若输出被压成正方形，先检查 `resolution` 是否被填了具体数值。
- 模型原生支持到 2K；3:4 竖幅常用 1088×1440。

## 5. 编辑提示词写法

先读 [官方 I2I 规则](../oneirloom-model-qwen-image-2-1/references/official/pe-i2i-system-prompt.txt)。三条要点：

1. **先说改什么**：开头用动词点明操作对象与区域，不要先描述成品画面。
2. **保留部分不要细写**：原文 *"A preservation description reads to the model as a generation instruction: the more concretely you describe something you meant to keep, the more likely it drifts."*——保留内容描述得越具体，模型越容易把它当成生成目标而画跑。保留内容按"类型 + 位置 + 作用"点名即可。
3. **改动要推到极强、不含糊**：不使用"至少""略微""尽量"这类留余地的说法，那属于欠改；同时不碰未点名的内容。

**本地执行的折中**：官方规则针对官方 prompt enhancer 与更服从的模型。本地以纯噪声起步或只写"其余完全不变"时，模型会无视约束而重排画面。因此本地用**中等具体度**：点名需要保留的类型与位置，明确写"镜头距离、取景范围与构图与输入图一致"，但不重描保留对象的材质与外观细节。

每版只处理一个改动目标，便于归因。

## 6. 多参考图的角色

`TextEncodeQwenImage21` 的 `images` 支持多张参考图，按 `image_1` … 顺序上传，提示词里用 `<image1>`、`<image2>` 引用。

- `image_1` 是**画布**：被编辑的那张，构图与未点名的内容以它为准。
- 其余参考图逐张分配明确职责：身份、姿势、配色、风格。

**身份一致性必须靠参考图，不靠文字。** 官方文档指出，用文字描述五官会让模型重新生成并降低相似度——文字清单越细，越像"生成一张新脸"的指令。需要跨视角保持同一人时，把该人的脸部裁出来作为独立参考图，并在提示词里指明"该处的身份以该图为准"。

## 7. 对称与镜像类任务

- 朝向属于结构：镜外看到背影、镜中看到正面这类关系，必须在文生图阶段写清（相机方位、人物朝向、镜外与镜中分别看到什么）。
- 不要同时锁死两个视角：既要求"镜中头部角度不变"又要求"镜外身体保持原样"，模型会因无法同时满足而重新生成一张脸。放开其中一个视角，身份才可能对齐。
- 画面内不要出现手机、相机或屏幕：会触发"画面里套画面"，模型会把界面中的人物画成另一个人。
- 声明画面中的形体数量（例如"只有她本人和她的一个倒影、没有第三个人"），可压掉复制人问题。

## 8. 交付前验证

不要只用"看起来对了"判断，逐项核对：

1. **确认它真是编辑**：比较输入图与输出图的像素差异，量化改动范围。整图差异率过高说明结构被重排。
2. **确认画幅**：读取输出文件尺寸，比对目标比例。
3. **确认身份**：把需要一致的两处人像裁出并排比对。
4. **确认局部改动生效**：把关注区域放大并加坐标参考后比对关键点位置。

## 9. 排查顺序

结果不对时按此顺序检查：

1. `latent_image` 是否接了 `EmptyLatentImage`？→ 是的话没有编辑能力。
2. `denoise` 是否过高（结构漂移）或过低（改动不生效）？
3. `resolution` 是否填了具体数值导致画幅改变？
4. 提示词中"要保留的"是否比"要改的"写得还详细？→ 保留描述会变成生成指令。
5. 身份是否靠文字描述而非参考图？
6. 这个需求是否属于结构性改动？→ 是的话回文生图。

## Evidence boundary

本技能的规则来自本地实测与官方 I2I 文档，两者须分开对待：官方文档提供提示词写法与参考图角色规则；接线、denoise 档位与"结构改动不可编辑"属于本地实测结论，其具体数值随模型、采样器与入口而变。交付时区分已检查的结果与未验证的推断，不把一次成功表述为可重复能力。
