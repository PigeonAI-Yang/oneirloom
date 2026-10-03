# 织梦师 · Oneirloom

**把想象，写成画面。**

一套开源的视觉创作 Skill。让你的 AI 助手学会看图、构思、写完整提示词，再对照生成结果继续修改。你可以从人像开始，也可以做产品广告、角色设定和叙事插画。

[开始使用](#开始使用) · [案例与记录](#案例与记录) · [技能目录](#技能目录) · [English](README.en.md) · [完整详情页](docs/product-page/index-oneirloom-v4.html)

[![织梦师商品主视觉：织梦兽把人像、志怪插画与产品广告织进梦网。把想象，写成画面。](docs/assets/product-page/01-hero-oneirloom-v4.webp)](docs/assets/product-page/01-hero-oneirloom-v4.webp)

[![一句日常表达，展开成一张画面。将卧室全身照的想法拆解为完整取景、居中姿态、缎面材质和左侧窗光。支持从零写提示词、分析参考图、构思广告和检查结果。](docs/assets/product-page/02-value-oneirloom-v4.webp)](docs/assets/product-page/02-value-oneirloom-v4.webp)

[![人像案例：脸部特写、完整全身、坐姿、硬光、夜间暖光和逆光发丝。选自既有人像教程的 Qwen-Image-2.1 结果。](docs/assets/product-page/03-portraits-native-v4.webp)](docs/assets/product-page/03-portraits-native-v4.webp)

[![产品广告案例：外卖照片参考与微缩食物小镇创意示意。春卷成为屋顶，薯条成为台阶，餐盒里出现手绘街巷。](docs/assets/product-page/04-product-oneirloom-v4.webp)](docs/assets/product-page/04-product-oneirloom-v4.webp)

[![继续做广告与插画：巧克力流入手绘可可庄园；人物关系、山雾与月色构成志怪叙事。根据已有案例制作的宣传画面。](docs/assets/product-page/05-worlds-oneirloom-v4.webp)](docs/assets/product-page/05-worlds-oneirloom-v4.webp)

[![角色资产案例：从织梦兽形象延展织梦、好奇、休息、完成四种动作。角色正面已获认可，新增资产设计稿待验收。](docs/assets/product-page/06-character-oneirloom-v4.webp)](docs/assets/product-page/06-character-oneirloom-v4.webp)

[![使用流程：给目标和材料，明确画面关系，交付完整中英提示词，检查结果继续修改。还可制作3:4提示词分享卡片。开源MIT，提供Krea 2和Qwen-Image-2.1专门适配。](docs/assets/product-page/07-start-oneirloom-v4.webp)](docs/assets/product-page/07-start-oneirloom-v4.webp)

## 案例与记录

这套详情页由织梦师的视觉分析、设计与光色方法指导制作。六张宣传图参考既有案例重新绘制；人像六宫格直接排版归档原图。宣传图中的场景与提示词示意不等同于原始案例记录，原图与已知提示词见下方链接。[打开完整详情长图](docs/assets/product-page/overview-oneirloom-v4.webp)。

- **人像摄影**：[12 张已归档人像的提示词与参数](docs/assets/portraits/manifest.json) · [62 张生成结果的完整教程](docs/美女生图教程.md)。各样本可能同时改变身份、姿态、衣料与环境，不能据此判断精确身份锁定或单项调整的效果。
- **外卖小镇广告**：[原始照片与认可结果记录](skills/oneirloom-product-art-direction/references/takeaway-food-town/evidence.json)。实际提交提示词、模型与参数未记录。
- **巧克力广告**：[原始提示词与案例](skills/oneirloom-style-design/templates/product-origin-world/template.md)；**志怪插画**：[氛围与观察记录](skills/oneirloom-style-illustration/templates/zhiguai-narrative/template.md)。两者的模型与参数均未知。
- **织梦兽资产**：[角色参考、配色、三视图与动作稿](docs/assets/dream-cocoon/README.md)。正面形象已获认可，新增资产设计稿仍待单独验收。

<details>
<summary>继续看角色衣橱设定</summary>

![包含服装、配件与材质细节的已有角色衣橱设定图](skills/oneirloom-character-sheet/templates/wardrobe-sheet/images/result-01.webp)

这个用户提供的结果展示服装、配件、材质与版面安排。转身视图和部分服装头像仍有偏差，模型与参数未知。[查看模板与记录](skills/oneirloom-character-sheet/templates/wardrobe-sheet/template.md)。

</details>

## 开始使用

### 安装技能集合

```bash
git clone https://github.com/PigeonAI-Yang/oneirloom.git
```

将 `skills/` 下的所有 `oneirloom*` 目录放进 AI 助手的技能搜索目录，保持同级关系，并保留各目录中的参考资料、模板和图片。

在新的对话中检查是否出现 `oneirloom`。你可以称呼它“织梦师”“织梦师Skill”或“Oneirloom”；支持显式调用的助手可用 `$oneirloom`。

### 用一个真实需求开始

以下指令发给 AI 助手。得到提示词后，再将提示词放进生图工具。

```text
用织梦师分析我上传的产品照片，帮我构思一张广告。
保留产品的形状、包装和主要配色，加入手绘微缩世界。
先根据产品本身选择创意，再给我完整提示词，只要中文。
```

```text
用织梦师检查我上传的结果图和原提示词。
现在鞋子被裁掉了，我想要完整全身取景。
保留人物、衣服、房间和光线，给我完整修订提示词。
```

有参考图时，说明每张图负责身份、姿势、配色还是风格。已有目标模型、工具入口、原提示词或结果图时，也一起提供。

## 技能目录

主技能负责理解任务与整合交付，方法技能负责各自的判断。具体画面配方放在所属方法的模板目录中。

<details>
<summary>展开全部技能</summary>

| 技能 | 用途 |
| --- | --- |
| [oneirloom](skills/oneirloom/SKILL.md) | 主入口、上下文继承与完整交付 |
| [oneirloom-visual-analysis](skills/oneirloom-visual-analysis/SKILL.md) | 参考图拆解与视觉关系分析 |
| [oneirloom-product-art-direction](skills/oneirloom-product-art-direction/SKILL.md) | 产品广告概念与画面故事 |
| [oneirloom-camera-composition](skills/oneirloom-camera-composition/SKILL.md) | 景别、机位、透视、裁切与遮挡 |
| [oneirloom-color-light](skills/oneirloom-color-light/SKILL.md) | 区域配色、光向与材质受光 |
| [oneirloom-character-sheet](skills/oneirloom-character-sheet/SKILL.md) | 角色设定、三视图、表情与服装 |
| [oneirloom-expression-stickers](skills/oneirloom-expression-stickers/SKILL.md) | Reaction intent, consistent character identity, and individual sticker delivery |
| [oneirloom-icon-design](skills/oneirloom-icon-design/SKILL.md) | UI icon families, app symbols, and native vector assets |
| [oneirloom-brand-identity](skills/oneirloom-brand-identity/SKILL.md) | Coherent VI foundations, applications, guidelines, and asset handoff |
| [oneirloom-figure-art](skills/oneirloom-figure-art/SKILL.md) | 成人非露骨人物艺术的姿态与遮挡 |
| [oneirloom-style-photography](skills/oneirloom-style-photography/SKILL.md) | 写实摄影、生活人像与电影感画面 |
| [oneirloom-style-illustration](skills/oneirloom-style-illustration/SKILL.md) | 绘画、版画、拼贴与叙事插画 |
| [oneirloom-style-design](skills/oneirloom-style-design/SKILL.md) | 海报、文字版式、包装、产品与 3D |
| [oneirloom-model-krea-2](skills/oneirloom-model-krea-2/SKILL.md) | Krea 2 提示词与入口适配 |
| [oneirloom-model-qwen-image-2-1](skills/oneirloom-model-qwen-image-2-1/SKILL.md) | Qwen-Image-2.1 提示词与任务适配 |
| [oneirloom-result-diagnosis](skills/oneirloom-result-diagnosis/SKILL.md) | 生成偏差分析与提示词修正 |
| [oneirloom-image-tutorial](skills/oneirloom-image-tutorial/SKILL.md) | 图文教程写作、扩写与润色 |
| [oneirloom-prompt-card](skills/oneirloom-prompt-card/SKILL.md) | 作品与完整提示词的 3:4 分享卡片 |

</details>

[三层架构](docs/architecture.md) · [模型证据](docs/model-evidence.md) · [摄影模板](skills/oneirloom-style-photography/templates/index.md) · [角色模板](skills/oneirloom-character-sheet/templates/index.md) · [插画模板](skills/oneirloom-style-illustration/templates/index.md) · [设计模板](skills/oneirloom-style-design/templates/index.md)

[Expression-sticker templates](skills/oneirloom-expression-stickers/templates/index.md) · [Icon templates](skills/oneirloom-icon-design/templates/index.md) · [Brand identity templates](skills/oneirloom-brand-identity/templates/index.md)

These three methods contain nine researched starter recipes. No corresponding generated examples or end-to-end VI production tests are recorded. A requested SVG, asset set, or VI guideline uses its artifact contract; prompt-only work retains complete bilingual prompts.

## 常见问题

**需要额外安装生图模型吗？**

织梦师安装的是提示词与创作方法。图片生成通过你所用助手的工具或生图入口运行，是否需要本地模型由该工具决定。

**模板里的例图都能复现吗？**

案例记录会说明已有结果、已知参数和偏差。部分模板尚未生成验证；实际效果需要在你的入口中生成并检查。

**可以只要中文吗？**

可以。默认是中英文完整提示词，你也可以指定一种语言。教程采用你要求的文章语言和文风。

## 一起把好用的方法留下来

欢迎补充画面配方、修正方法，或提交带原图与提示词的案例。[贡献指南](CONTRIBUTING.md)说明了模板和记录的组织方式。

如果织梦师帮你写清了想画的图，欢迎给项目一颗 Star，或在 [Issues](https://github.com/PigeonAI-Yang/oneirloom/issues) 分享需求与结果。

## 许可证

[MIT License](LICENSE)。模型与生成服务的使用条款另行适用。
