---
name: oneirloom-model-qwen-image-2-1
description: 为 Qwen-Image-2.1 文生图、图像编辑、透明背景与多参考图任务编写提示词，并核对当前部署入口是否支持相应输入。用于 Qwen-Image-2.1 提示词生成和跨模型迁移。
---

# Qwen-Image-2.1 模型适配

Before giving Qwen-specific guidance, read the [local official-document index](references/official/README.md) and only the snapshot relevant to the current task. Keep model-level facts separate from active-entry controls and observed results. Do not reread the full archive.

Read [task-specific writing](references/writing.md) before composing a Qwen prompt. Select finished-image description for text-to-image or reference reconstruction, and an operation followed by preservation for an actual image edit. Keep confirmed material colors and limb joint states unchanged across adaptation.

The official sources document text-to-image, image-conditioned editing, up to 10 reference images, local edits guided by circles, painted annotations, or masks, and native RGBA. Confirm which capabilities the active UI or API exposes, then verify the result.

1. 文生图描述目标画面与区域关系；编辑描述目标变化，同时明确保留的主体、构图和细节。输入图应走入口的图像字段，不能只把文件名写进文本。
2. 多参考图明确每张图的职责（身份、姿势、配色、风格），确认当前入口支持张数、顺序与标注方式后再给操作字段。局部修改优先确认蒙版或标注能力。A workspace-specific edit-entry convention documents literal `<image1>`, `<image2>`, and later labels in upload order. This is not a Qwen model requirement. Confirm that exact entry is active before using those labels; otherwise follow the active host's observed input syntax. Use labels only for supplied images and give each reference a clear role. Use no image labels for text-to-image without references.
3. 透明图要明确 RGBA／透明背景目标，并确认当前部署是否输出 alpha；参数和分辨率与正文分开。The model supports native RGBA, but output from the active entry is unverified until you inspect the file for an alpha channel. Transparency wording alone does not establish that the active entry exposes RGBA output. Keep transparency as the target instead of silently switching to white.
4. The companion prompt-rewriter documentation describes separate fine-tuned Qwen3.5-VL checkpoints for text-to-image and editing. Its text-to-image checkpoint outputs a detailed English prompt from input in any language. This does not show that English outperforms Chinese with Qwen-Image-2.1. Follow the main skill's output-language contract and avoid a fixed length without comparative evidence.
5. Follow the main skill's output contract, providing one complete positive prompt in each required language for every requested model unless the current request explicitly asks for one language only. For image text-layout tasks, specify exact in-image copy and remind the user to verify readability after generation.

生成、编辑、多参考与透明输出的任务切换详见 [Qwen 任务表](references/tasks.md)。
