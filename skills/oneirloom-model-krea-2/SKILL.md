---
name: oneirloom-model-krea-2
description: 为 Krea 2 Medium、Large、Turbo 及开放权重 RAW/Turbo 编写和校验提示词，区分托管网站、API 与自部署入口的参考图和参数能力。用于 Krea 2 文生图、风格参考和跨模型迁移。
---

# Krea 2 model adapter

Read the [shared interaction contract](../oneirloom/references/interaction-contract.md) before the first substantive response unless its unchanged content is already available. For person prompts, including new images and grid panels, read [person defaults and proportions](../oneirloom/references/person-prompts.md).

为 Krea 2 编写和校验提示词，区分托管与自部署入口的参考图和参数能力。视觉规范在适配期间保持固定，只有行文跟随入口变化。

## When to use

- Krea 2 文生图、风格参考与跨模型迁移任务（主技能路由指定 Krea 2 时加载）

## Workflow

1. Confirm the variant and entry. 先记录精确变体与入口。托管产品有 Medium、Large、Medium Turbo，文档列出风格参考、情绪板、创意模式、生成滑块；开放权重的 RAW 与 Turbo 是另一个发布路径。不要把托管 `creativity=raw` 当作 RAW 权重。自部署 RAW/Turbo 的接口与托管字段分开核验；开放权重 RAW 官方模型卡偏向微调／后训练，不把托管 Sref、moodboard、滑块移植进本地 pipeline。官方来源与核验日期见仓库 `docs/model-evidence.md`；若该文件不在运行环境，直接核查 Krea 官方文档。
2. Read the sources. Before model-specific advice, read the [official-document index](references/official/README.md) and the [task map](references/tasks.md). Read only the source relevant to the active hosted or local entry. Keep the reconstructed pose, material identities, and illuminated appearance fixed while adapting the prose.
3. Compose. 用清晰的自然语言描述主体、空间关系、区域光色与风格。Krea 官方示例采用自然语言，但“英文短词一定更好”没有本项目的同条件对照证据。托管入口明确可用时，将 `aspect_ratio`、`seed`、`creativity`、风格参考和 moodboard 作为独立控件／字段；风格参考负责外观倾向，不承诺精确姿态，姿态和遮挡仍写在提示词中。用户要求严格复现且托管入口支持时，考虑较低的提示词扩展；只作为待实测设置建议，不替用户预设。网站、API 与第三方封装有不同字段，以用户当前入口为准。
4. 入口字段与提示词模板详见 [Krea 2 任务表](references/tasks.md)，仅在对应入口实际可用时引用。

## Maintain relevant source evidence

For an undocumented requested version or task, check primary official documentation and save relevant text under this adapter's references with its source, retrieval date, revision when available, and hash. Keep source snapshots separate from local interpretation. An unavailable source blocks only the unsupported model claim. Confirm actual entry support before giving controls, and preserve the resolved visual intent across models. For diagnosis, distinguish the sample's producing model and entry from the requested target.

## Output and handoff

Follow the shared interaction contract: one complete positive prompt in each required language for every requested model, unless the current request explicitly asks for one language only; keep both versions semantically matched. List concrete settings separately only when the user needs them and the entry is confirmed; if the entry is unknown, provide portable natural-language prompt text.
