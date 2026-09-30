# Krea 2 任务表

| 入口 | 提示词 | 独立控制项 | 注意 |
| --- | --- | --- | --- |
| 官方网站 Medium/Large/Turbo | 主体 + 关系 + 光色 + 风格 | 画幅、风格参考、情绪板、创意模式、滑块（实际界面为准） | Sref 是风格控制，不保证位置或姿态 |
| 官方 API Medium/Large | 同上 | `aspect_ratio`、`seed`、`creativity`、`image_style_references`、`moodboards` 等 | `creativity=raw` 仅指提示词扩展，不是权重 |
| 开放权重 RAW/Turbo | 与本地 pipeline 匹配的自然语言 | 推理步数、引导、宽高等由本地代码决定 | 托管控件不自动存在；RAW 官方卡偏向微调 |
| 第三方封装 | 保持纯文本可移植性 | 按该服务实际文档核实 | 不假定官方功能全部开放 |

复现提示词骨架：`[主体与动作]。[相机位置、遮挡、裁切]。[背景、区域光色]。[表现形式与材质]。` 自由探索可适度留白；精确复现优先补足可检验关系。用户只问提示词时不附控件教程。

官方依据：https://www.krea.ai/docs/user-guide/features/krea-2 ，https://www.krea.ai/docs/developers/krea-2/overview ，https://huggingface.co/krea/Krea-2-Raw 。核验于 2026-09-26。

## Write for the active task

For hosted text-to-image, write clear scene prose from the inspected specification. Use the reconstruction workflow's order: opening scene, framing and pose, subject and garments, environment, then light and surface treatment. Explicitly name decisive joint states and garment base colors. Keep transparency and visible light response beside the relevant material. This order is a local writing method; Krea's documents do not claim a required order or a language advantage.

For strict reconstruction, check prompt expansion in the active entry. The official API describes `creativity=raw` as no expansion and `low` as minimal expansion. Offer these only when that entry exposes the field, and label the result untested. Neither setting guarantees pose or color fidelity.

For style references, keep the image's appearance role distinct from a pose or identity constraint. Describe the required body geometry and material identities in text. Do not promise that style references lock those attributes. A reference upload field must have the documented role in the active entry.

For a requested local edit, first verify that the chosen entry actually accepts a content image and an edit operation. Do not route it through a hosted style-reference field as if that field were an editing canvas. If editing is unavailable, deliver the reachable text and report the entry gap.

For local RAW or Turbo, verify the pipeline's own inputs. Hosted creativity and style-reference controls do not automatically apply. Read the local [official-document index](official/README.md) for the 2026-09-30 hosted snapshots and provenance.
