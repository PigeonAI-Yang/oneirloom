![织梦师 Oneirloom：把画面想清楚，把提示词写到位](docs/assets/hero.png)

# 织梦师 · Oneirloom

**让你的 AI 助手学会拆解画面、写好生图提示词，并修正生成偏差。**

织梦师是一套开源的视觉提示词 Skill。给它一个想法、一张参考图，或一张没画对的结果图，它会结合主体、空间、材质、光色与风格，整理成完整、可复制的提示词。你也可以用它设计角色设定图、构思产品广告，或撰写带图的生图教程。

`Agent Skills` · `中文 + English` · `Krea 2` · `Qwen-Image-2.1` · `MIT`

[看案例](#看它能帮你做什么) · [开始使用](#开始使用) · [工作方式](#它怎样把需求写成提示词) · [技能目录](#技能目录) · [English](README.en.md)

## 画面没对，先找出哪一处没说清

你想要一张全身照，结果鞋子被裁掉。你让巧克力流进插画里的河流，结果变成了上下两张拼图。你换了模型，原来的提示词又需要调整。

织梦师会把这些问题落到具体的画面关系上：人物占多少空间、镜头从哪里看、液体跨过哪条边界、光照在哪块材质上。你可以用日常语言说出意图，由 AI 助手组织这些细节。

已有结果图时，它会对照目标找出主要偏差，再交付完整的修订提示词，让你继续生成。

## 看它能帮你做什么

![已有案例：产品广告、志怪插画、生活摄影与角色服装设定](docs/assets/showcase.png)

上图使用仓库已有案例，等比缩放并排版，保留完整画面。它们展示的是各自已有结果；提示词、参数和已知偏差见下方记录。

| 你想做的画面 | 织梦师会关注什么 | 案例与记录 |
| --- | --- | --- |
| 产品广告 | 产品特征、创意关系，以及摄影与插画之间的连接 | [巧克力与可可庄园](skills/oneirloom-style-design/templates/product-origin-world/template.md)，有原始提示词和用户提供的结果，模型与参数未知 |
| 志怪叙事插画 | 人物关系、环境层次、纸张肌理与含蓄的异样感 | [月下志怪](skills/oneirloom-style-illustration/templates/zhiguai-narrative/template.md)，用户认可氛围，实际提交提示词与模型未知 |
| 生活人像摄影 | 人物姿态、取景范围、房间布局与光线方向 | [室内全身人像](skills/oneirloom-style-photography/templates/indoor-full-length/template.md)，保留 Qwen-Image-2.1 本地生成记录，脚距和人物占比仍有偏差 |
| 角色服装设定 | 同一角色的外观、不同服装、配件、细节和版面 | [角色衣橱](skills/oneirloom-character-sheet/templates/wardrobe-sheet/template.md)，已有用户提供的结果，转身视图和部分服装头像仍有偏差 |

### 一张外卖照片，也能成为广告创意的起点

![原始外卖照片与用户认可的微缩食物小镇结果](docs/assets/product-case.png)

这个案例保留了食物的摄影质感，把春卷变成屋顶、薯条变成台阶，在餐盒里加入手绘街巷与人物。创意围绕这份食物展开，产品本身仍然是画面的主角。

织梦师的[产品创意方法](skills/oneirloom-product-art-direction/SKILL.md)先检查你提供的产品，再选择合适的故事和表现手法。模板提供可以借鉴的关系，具体构思随产品调整。

这是用户认可的一次结果，实际提交提示词、模型与参数未记录。[查看原图、建议提示词与案例记录](skills/oneirloom-product-art-direction/references/takeaway-food-town/evidence.json)。

## 把它用在你的创作里

| 你给它什么 | 你能得到什么 |
| --- | --- |
| 一个想法，比如“暖色、安静的卧室人像” | 主体、姿态、环境、构图与光色完整的提示词 |
| 一张参考图，并说明想保留的部分 | 对可见画面的分析，以及按目标重写的提示词 |
| 一张产品照片和广告需求 | 围绕产品特征设计的创意方向与提示词 |
| 角色资料、参考图与版式要求 | 角色三视图、表情卡或服装设定图的提示词 |
| 原提示词、结果图和最想修正的问题 | 对主要偏差的判断，以及完整的修订提示词 |
| 同一个画面要用于不同模型 | 保持视觉意图的各模型版本，参数建议单独列出 |
| 教学主题、现有稿件或生成案例 | 带具体提示词、配图说明与结果分析的教程稿件 |

默认交付完整中文提示词和语义对应的英文版，每个版本各放在可复制的文本块中。明确要求只用一种语言时，就按你的要求输出。参考图输入、种子和其他参数放在提示词之外。

## 它怎样把需求写成提示词

![织梦师工作流程：明确目标、拆解画面、选择方法、适配模型、交付与修正](docs/assets/workflow.png)

织梦师沿用对话里已确认的模型、参考图职责和输出偏好，根据当前任务读取所需方法。有合适模板时，它借用模板的构图关系与可调整项；没有合适模板时，也能直接组织新画面。

模型适配发生在视觉意图确定之后。现在提供 Krea 2 和 Qwen-Image-2.1 两个专门适配技能，区分任务类型与使用入口。没有专门适配的模型，先交付通用的自然语言提示词。

![写作示意：将“暖色卧室全身照”展开为可见的取景、布局、光色与材质关系](docs/assets/prompt-anatomy.png)

这张图展示提示词的写作方法，其中片段用于说明，未作为一组新提示词生成测试。

## 开始使用

### 安装完整技能集合

克隆或下载仓库：

```bash
git clone https://github.com/PigeonAI-Yang/oneirloom.git
```

将仓库 `skills/` 下的所有 `oneirloom*` 目录放进你所用 AI 助手的技能搜索目录，保持它们为同级目录。保留每个目录内的 `references/`、`templates/` 和图片文件。这里只安装提示词与创作方法，生图模型仍通过你使用的工具运行。

```text
<你的技能搜索目录>/
├── oneirloom/
│   └── SKILL.md
├── oneirloom-visual-analysis/
├── oneirloom-camera-composition/
├── oneirloom-color-light/
├── oneirloom-style-photography/
├── oneirloom-model-qwen-image-2-1/
└── ...（其他方法目录也在同一级）
```

在新的对话中检查技能列表是否出现 `oneirloom`。你可以称呼它“织梦师”“织梦师Skill”或“Oneirloom”；支持显式技能调用的助手可用 `$oneirloom`。各方法技能也可以单独调用。

### 先给它一个真实需求

下面是发给 AI 助手的指令。得到提示词后，再把提示词放进生图工具。

**从想法开始：**

```text
用织梦师帮我写一组卧室全身人像提示词。
画面暖色、安静，人物从头顶到鞋底完整入画，左侧窗光。
目标模型是 Qwen-Image-2.1。请给我完整的中英文版本。
```

**围绕产品构思：**

```text
用织梦师分析我上传的产品照片，帮我构思一张广告海报。
保留产品的形状、包装和主要配色，加入手绘微缩世界。
先根据产品本身选择创意，再给我完整提示词，只要中文。
```

**修正生成偏差：**

```text
用织梦师检查我上传的结果图和原提示词。
我最想修正的是取景：现在鞋子被裁掉了。
保留人物、衣服、房间和光线，给我完整的修订提示词。
```

有参考图时，一起提供图片，并说明每张图负责身份、姿势、配色还是风格。已有模型、工具入口、原提示词或结果图时，也一并给它。

## 技能目录

集合包含一个主技能和 13 个方法技能。主技能负责理解任务和整合交付，方法技能负责各自的判断，具体画面配方保存在所属方法的模板目录中。

<details>
<summary>展开查看全部技能</summary>

| 技能 | 用途 |
| --- | --- |
| [oneirloom](skills/oneirloom/SKILL.md) | 主入口、上下文继承、方法选择与完整交付 |
| [oneirloom-visual-analysis](skills/oneirloom-visual-analysis/SKILL.md) | 参考图拆解、视觉关系与复现分析 |
| [oneirloom-product-art-direction](skills/oneirloom-product-art-direction/SKILL.md) | 围绕产品设计广告概念与画面故事 |
| [oneirloom-camera-composition](skills/oneirloom-camera-composition/SKILL.md) | 景别、机位、透视、裁切与遮挡 |
| [oneirloom-color-light](skills/oneirloom-color-light/SKILL.md) | 区域配色、光向、明暗与材质受光 |
| [oneirloom-character-sheet](skills/oneirloom-character-sheet/SKILL.md) | 角色设定、三视图、表情卡与服装设定 |
| [oneirloom-figure-art](skills/oneirloom-figure-art/SKILL.md) | 成人非露骨人物艺术的姿态与遮挡关系 |
| [oneirloom-style-photography](skills/oneirloom-style-photography/SKILL.md) | 写实摄影、生活人像与电影感画面 |
| [oneirloom-style-illustration](skills/oneirloom-style-illustration/SKILL.md) | 绘画、版画、纸质拼贴与叙事插画 |
| [oneirloom-style-design](skills/oneirloom-style-design/SKILL.md) | 海报、文字版式、包装、产品与 3D 表现 |
| [oneirloom-model-krea-2](skills/oneirloom-model-krea-2/SKILL.md) | Krea 2 提示词与入口适配 |
| [oneirloom-model-qwen-image-2-1](skills/oneirloom-model-qwen-image-2-1/SKILL.md) | Qwen-Image-2.1 提示词与任务适配 |
| [oneirloom-result-diagnosis](skills/oneirloom-result-diagnosis/SKILL.md) | 对照结果识别偏差并修改提示词 |
| [oneirloom-image-tutorial](skills/oneirloom-image-tutorial/SKILL.md) | 图文生图教程的写作、扩写与润色 |

</details>

查看[三层架构](docs/architecture.md)、[模型证据](docs/model-evidence.md)，或浏览[摄影](skills/oneirloom-style-photography/templates/index.md)、[角色设定](skills/oneirloom-character-sheet/templates/index.md)、[插画](skills/oneirloom-style-illustration/templates/index.md)与[设计](skills/oneirloom-style-design/templates/index.md)模板。

## 常见问题

**它会直接生成图片吗？**

织梦师的核心交付是提示词与创作方法。图片生成依赖你所用助手的工具和模型入口。写教程时，可以使用已有案例；需要新图时，仍要通过可用的生图工具执行并检查结果。

**只能用于两个模型吗？**

画面分析、构图、光色与风格方法可用于通用提示词。Krea 2 和 Qwen-Image-2.1 另有专门适配；其他模型先用通用描述，具体控件以实际入口为准。

**示例能保证复现吗？**

每个案例只说明其记录中的结果。部分案例没有完整生成参数，概括出的模板也可能尚未生成验证。使用时根据你的结果继续修正；相关记录会保留已知偏差。

## 一起补充可用的方法与案例

欢迎提交新画面配方、修正已有方法，或补充有原图与提示词的案例。具体场景放进所属方法的模板目录，让后来的人能看到使用条件、可调整项和实际结果。[阅读贡献指南](CONTRIBUTING.md)。

如果织梦师帮你写清了一张想画的图，欢迎给项目一颗 Star，或在 [Issues](https://github.com/PigeonAI-Yang/oneirloom/issues) 分享需求与结果。

## 许可证

仓库采用 [MIT License](LICENSE)。模型与生成服务的使用条款另行适用。
