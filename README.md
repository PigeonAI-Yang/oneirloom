# Oneirloom / 织梦师

将视觉需求、参考图和生成偏差转成可直接使用的图像提示词。项目采用 **1 个路由主 SKILL + 9 个可独立使用的子 SKILL**；当前提供 Krea 2 与 Qwen-Image-2.1 模型适配，以及摄影、插画、平面与产品设计的表现形式分支。

## 使用

1. 将 `skills/` 下的全部目录放在同一个技能搜索根目录。只使用某个子技能时，也可以单独安装它。
2. 让 AI 读取 `oneirloom`。主技能按任务选取必要的子技能；也可直接调用某个子技能。
3. 告诉 AI 目标模型、任务（文生图／参考图复现／编辑／诊断）、画面目标；有参考图或生成结果时附上。已经在对话里说明过的条件不用重复。
4. 默认只交付一份完整的**正向提示词**；明确要求多模型时每个模型各交付一份。参数、参考图通道与提示词正文分开。

例如：“用 Qwen-Image-2.1 把这张图的构图和色彩关系复现为摄影风格，直接给提示词。”

## 架构

| 层 | 技能 | 职责 |
| --- | --- | --- |
| 路由 | `oneirloom` | 继承会话约束、选择子技能、整合唯一最终结果 |
| 分析 | `oneirloom-visual-analysis` | 参考图可见事实、优先级与空间关系 |
| 语言 | `oneirloom-camera-composition`、`oneirloom-color-light` | 将镜头、构图、光色意图变为可检验描述 |
| 表现 | `oneirloom-style-photography`、`oneirloom-style-illustration`、`oneirloom-style-design` | 摄影、绘画／插画、平面／产品／三维设计 |
| 模型 | `oneirloom-model-krea-2`、`oneirloom-model-qwen-image-2-1` | 版本／入口能力核验与对应的任务组织 |
| 迭代 | `oneirloom-result-diagnosis` | 对照目标和输出做最小修正 |

主技能依赖子技能的**名称**而非私有目录 ID。仓库内的相邻目录只是查找后备；运行环境不会因 Markdown 链接而自动调用子技能。子技能各有完整触发描述，可独立使用。模型与风格是正交维度：一个任务最多选择一个表现分支，必要时加入镜头与光色，再加入目标模型；诊断任务优先加入迭代分支。

## 来源与限制

模型事实见 [`docs/model-evidence.md`](docs/model-evidence.md)，维护规则见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。模型、版本和托管入口会变化；使用前核验当前接口。仓库中的示例不等于当前提示词的生成效果实测。尚未得到同入口 A/B 证据的语言或长度偏好不会写成模型定律。

## 许可证

许可证为 MIT；Krea、Qwen 的模型与服务仍受各自条款约束。
