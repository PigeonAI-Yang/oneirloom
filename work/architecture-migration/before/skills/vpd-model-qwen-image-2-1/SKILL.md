---
name: vpd-model-qwen-image-2-1
description: 为 Qwen-Image-2.1 文生图、图像编辑、透明背景与多参考图任务编写提示词，并核对当前部署入口是否支持相应输入。用于 Qwen-Image-2.1 提示词生成和跨模型迁移。
---

# Qwen-Image-2.1 模型适配

官方模型卡展示文生图、单图编辑、透明图输出，并描述多参考图与局部标注／蒙版能力；这不等于任意第三方入口均提供这些控件。来源与核验日期见仓库 `docs/model-evidence.md`，缺文件时核对 Qwen 官方模型卡及当前入口文档。

1. 文生图描述目标画面与区域关系；编辑描述目标变化，同时明确保留的主体、构图和细节。输入图应走入口的图像字段，不能只把文件名写进文本。
2. 多参考图明确每张图的职责（身份、姿势、配色、风格），确认当前入口支持张数、顺序与标注方式后再给操作字段。局部修改优先确认蒙版或标注能力。For this user's confirmed local edit entry, uploaded images are addressed by literal `<image1>`, `<image2>`, and so on in upload order. Use only labels for images actually supplied, and assign each a clear role when multiple images are present. For text-to-image without supplied references, use no image labels. Do not assume these labels attach images or apply to other entries or APIs; use only the active host's confirmed convention.
3. 透明图要明确 RGBA／透明背景目标，并确认当前部署是否输出 alpha；参数和分辨率与正文分开。In this user's confirmed local edit entry, alpha output remains unverified: use a confirmed alpha control if available, otherwise report that support is unverified. Transparency wording alone does not establish RGBA output; keep transparency as the target rather than silently substituting white.
4. Official examples include both complete sentences and short descriptions, so they do not establish a fixed length or prove that Chinese is superior to English. Follow the main skill's output language contract and keep the visual details matched across languages.
5. Follow the main skill's output contract, providing one complete positive prompt in each required language for every requested model unless the current request explicitly asks for one language only. For image text-layout tasks, specify exact in-image copy and remind the user to verify readability after generation.

生成、编辑、多参考与透明输出的任务切换详见 [Qwen 任务表](references/tasks.md)。
