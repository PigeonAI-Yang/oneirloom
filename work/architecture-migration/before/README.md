# Visual Prompt Director / 视觉提示词导演

Turn visual requests, references, and generation misses into usable image prompts, or develop illustrated image-generation tutorials. The collection contains **1 routing skill and 14 independently usable subskills**, covering Krea 2, Qwen-Image-2.1, character sheets and templates, photography, illustration, design, result correction, and tutorial writing.

## 使用

1. 将 `skills/` 下的全部目录放在同一个技能搜索根目录。只使用某个子技能时，也可以单独安装它。
2. 让 AI 读取 `visual-prompt-director`。主技能按任务选取必要的子技能；也可直接调用某个子技能。
3. 告诉 AI 目标模型、任务（文生图／参考图复现／编辑／诊断）、画面目标；有参考图或生成结果时附上。已经在对话里说明过的条件不用重复。
4. 默认只交付一份完整的**正向提示词**；明确要求多模型时每个模型各交付一份。参数、参考图通道与提示词正文分开。

例如：“用 Qwen-Image-2.1 把这张图的构图和色彩关系复现为摄影风格，直接给提示词。”

For a teaching article, invoke `vpd-image-tutorial` directly or ask the main skill to write, expand, or polish an illustrated image-generation tutorial. Tutorial requests use the requested article language and author voice rather than the standalone prompt-only format. The tutorial branch requires relevant visual examples and accurate descriptions of inspected results; prose-only edits reuse existing evidence.

## 架构

| 层 | 技能 | 职责 |
| --- | --- | --- |
| 路由 | `visual-prompt-director` | 继承会话约束、选择子技能、整合唯一最终结果 |
| 分析 | `vpd-visual-analysis` | 参考图可见事实、优先级与空间关系 |
| 角色设定 | `vpd-character-sheet` | 角色身份依据、跨视角锚点与设定板信息层级 |
| Character-card templates | `vpd-style-character-card` | Indexed 4+4 and three-view prompt templates for matching layouts |
| Figure art | `vpd-figure-art` | Adult non-explicit figure composition, requested concealment, and preservation of visual anchors |
| 语言 | `vpd-camera-composition`、`vpd-color-light` | 将镜头、构图、光色意图变为可检验描述 |
| 表现 | `vpd-style-photography`、`vpd-style-xiaohongshu-beauty-squat`、`vpd-style-illustration`、`vpd-style-design` | 摄影、小红书蹲姿生活自拍、绘画／插画、平面／产品／三维设计 |
| 模型 | `vpd-model-krea-2`、`vpd-model-qwen-image-2-1` | 版本／入口能力核验与对应的任务组织 |
| 迭代 | `vpd-result-diagnosis` | 对照目标和输出做最小修正 |
| Tutorial writing | `vpd-image-tutorial` | Author-voiced lessons, substantive section development, explanatory figures, evidence-based captions, and natural prose |

主技能依赖子技能的**名称**而非私有目录 ID。仓库内的相邻目录只是查找后备；运行环境不会因 Markdown 链接而自动调用子技能。子技能各有完整触发描述，可独立使用。模型与风格是正交维度：一个任务最多选择一个表现分支，必要时加入镜头与光色，再加入目标模型；诊断任务优先加入迭代分支。

## 来源与限制

模型事实见 [`docs/model-evidence.md`](docs/model-evidence.md)，维护规则见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。模型、版本和托管入口会变化；使用前核验当前接口。仓库中的示例和静态检查不等于生成效果实测。尚未得到同入口 A/B 证据的语言或长度偏好不会写成模型定律。

## 验证

运行 `python3 scripts/check_skills.py` 检查技能名称、路由、文件链接与示例。回归任务在 `evals/cases.json`，用于人工或代理评测。许可证为 MIT；Krea、Qwen 的模型与服务仍受各自条款约束。
