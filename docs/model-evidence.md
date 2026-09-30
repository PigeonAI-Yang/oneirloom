# 模型证据卡

核验日期：2026-09-26。`official_documented` 表示官方公开资料明确说明；`observed_local` 必须有同入口记录；`hypothesis` 仅供 A/B 测试；`unknown` 不应宣称为能力。

| 目标 | 入口与任务 | 已核验事实 | 证据 |
| --- | --- | --- | --- |
| Krea 2 | 托管网站文生图 | Medium、Large、Turbo；网站提供风格参考、情绪板、创意模式和生成滑块 | [Krea 用户文档](https://www.krea.ai/docs/user-guide/features/krea-2) |
| Krea 2 | 官方 API | Medium/Large 文档把 `prompt`、`aspect_ratio`、`seed`、`creativity`、风格参考、moodboards 与 sliders 分作字段；`creativity=raw` 是不扩展提示词 | [Krea API 概览](https://www.krea.ai/docs/developers/krea-2/overview) |
| Krea 2 | 开放权重 | RAW 为基础检查点，Turbo 是后训练／蒸馏检查点；RAW 模型卡说明偏向微调与后训练 | [Krea RAW 官方模型卡](https://huggingface.co/krea/Krea-2-Raw) |
| Qwen-Image-2.1 | Official model card, QwenLM README, and Diffusers examples retrieved 2026-09-29 UTC | Model-level sources document text-to-image, image-conditioned editing, up to 10 reference images, local edits guided by circles, painted annotations, or masks, and native RGBA. These sources do not establish support in the active third-party entry or guarantee its output. | [Local official-document archive](../skills/oneirloom-model-qwen-image-2-1/references/official/README.md); [Qwen model card](https://huggingface.co/Qwen/Qwen-Image-2.1) |

以上是模型或官方入口事实，**不是**第三方封装已经实现的承诺。Krea API 与开放权重使用不同接口；Krea 托管 `creativity=raw` 与 RAW 权重不同。当前无项目级同环境 A/B 记录，因此“某模型必须用英文短词／中文长文”标记为 `unknown`。

## 新证据记录模板

`日期 / 模型精确版本 / 平台入口 / 任务模式 / 参考图通道 / 参数与提示词增强状态 / 只改变的一项变量 / 样本与判据 / 结论 / 证据等级 / 来源 URL 或结果文件`。

接口变化时复核官方资料并更新表格。不要从模型卡的输出质量描述推出必然命中率。

## Task-writing evidence checked 2026-09-30

Krea's hosted user guide and API overview were retrieved and preserved in the [Krea official archive](../skills/oneirloom-model-krea-2/references/official/README.md). They document scene prose and prompt-expansion controls. The local task map keeps those controls separate from style references and local RAW/Turbo inputs. The reconstruction prose order is a local procedure, not a documented performance rule.

The official Qwen T2I and I2I enhancer system prompts were retrieved at pinned checkpoint revisions and added to the [Qwen official archive](../skills/oneirloom-model-qwen-image-2-1/references/official/README.md). They provide distinct writing procedures for finished-image description and operation-first editing. Their language, ratio, reference-tag, length, and JSON rules belong to those enhancer contracts. They are not universal requirements for the image model or an unidentified entry. Local adaptation is in the [Qwen writing guide](../skills/oneirloom-model-qwen-image-2-1/references/writing.md).

These official sources were inspected for prompt writing. No new image generation, active-entry operation, or language comparison was performed.
