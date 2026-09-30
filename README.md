![织梦师 Oneirloom：把想象，写成画面。](docs/assets/hero-v3.webp)

# 织梦师 · Oneirloom

**把想象，写成画面。**

织梦师是一套开源的视觉创作 Skill，让你的 AI 助手学会看图、构思、写提示词，再根据生成结果继续修改。先从你最想画好的人像开始，也可以继续做角色设定、插画与产品广告。

`Agent Skills` · `中文 + English` · `Krea 2` · `Qwen-Image-2.1` · `MIT`

[作品与案例](#作品与案例) · [创作方式](#创作方式) · [开始使用](#开始使用) · [技能目录](#技能目录) · [English](README.en.md)

## 你说出想法，它组织画面

“想要一张安静的卧室全身照。”

“让这份外卖，变成一座微缩小镇。”

“这张图的氛围很好，但人物姿势不对。”

织梦师接住这些日常表达，把它们展开为可以写进提示词的细节：人物与环境的位置、镜头的取景、材质的质感，以及落在画面不同区域的光和颜色。

有参考图时，它先分析图中可见的关系。需要广告创意时，它先看产品，再构思故事。已有结果时，它对照目标找出主要偏差，交付完整的修订提示词。

## 作品与案例

先看美女人像。下面选了此前人像教程里的 12 张原图，分别展示取景、姿态、穿搭与光线。教程案例包含 62 张生成结果，首页展示的是已有结果的 WebP 压缩版，保留原尺寸。

### 取景

<table class="portrait-row"><tr>
<td width="33%" align="center"><a href="docs/assets/portraits/19_close_fixed.webp"><img src="docs/assets/portraits/19_close_fixed.webp" alt="脸部特写的已有人像作品" width="280"></a><br>脸部特写</td>
<td width="33%" align="center"><a href="docs/assets/portraits/20_half_fixed.webp"><img src="docs/assets/portraits/20_half_fixed.webp" alt="上半身人像的已有人像作品" width="280"></a><br>上半身人像</td>
<td width="33%" align="center"><a href="docs/assets/portraits/01_full.webp"><img src="docs/assets/portraits/01_full.webp" alt="完整全身的已有人像作品" width="280"></a><br>完整全身</td>
</tr></table>

### 姿态

<table class="portrait-row"><tr>
<td width="33%" align="center"><a href="docs/assets/portraits/09_seated.webp"><img src="docs/assets/portraits/09_seated.webp" alt="短裙坐姿的已有人像作品" width="280"></a><br>短裙坐姿</td>
<td width="33%" align="center"><a href="docs/assets/portraits/e07_backlace.webp"><img src="docs/assets/portraits/e07_backlace.webp" alt="侧身回望的已有人像作品" width="280"></a><br>侧身回望</td>
<td width="33%" align="center"><a href="docs/assets/portraits/e11_longseated.webp"><img src="docs/assets/portraits/e11_longseated.webp" alt="长裙坐姿的已有人像作品" width="280"></a><br>长裙坐姿</td>
</tr></table>

### 穿搭

<table class="portrait-row"><tr>
<td width="33%" align="center"><a href="docs/assets/portraits/e03_short.webp"><img src="docs/assets/portraits/e03_short.webp" alt="短裙轮廓的已有人像作品" width="280"></a><br>短裙轮廓</td>
<td width="33%" align="center"><a href="docs/assets/portraits/e04_long.webp"><img src="docs/assets/portraits/e04_long.webp" alt="长裙垂坠的已有人像作品" width="280"></a><br>长裙垂坠</td>
<td width="33%" align="center"><a href="docs/assets/portraits/e09_layeropen.webp"><img src="docs/assets/portraits/e09_layeropen.webp" alt="开衫叠穿的已有人像作品" width="280"></a><br>开衫叠穿</td>
</tr></table>

### 光线

<table class="portrait-row"><tr>
<td width="33%" align="center"><a href="docs/assets/portraits/25_hard_fixed.webp"><img src="docs/assets/portraits/25_hard_fixed.webp" alt="硬光与窗影的已有人像作品" width="280"></a><br>硬光与窗影</td>
<td width="33%" align="center"><a href="docs/assets/portraits/26_warm_fixed.webp"><img src="docs/assets/portraits/26_warm_fixed.webp" alt="夜间暖光的已有人像作品" width="280"></a><br>夜间暖光</td>
<td width="33%" align="center"><a href="docs/assets/portraits/e25_backlight.webp"><img src="docs/assets/portraits/e25_backlight.webp" alt="逆光与发丝轮廓的已有人像作品" width="280"></a><br>逆光与发丝轮廓</td>
</tr></table>

一张脸可以拍得更近，一个坐姿会改变衣料的褶皱，同一类黑裙也可以有不同的长度与背部结构。织梦师会把这些意图写成具体画面关系，让你有方向地继续创作。

[查看这 12 张图的原始提示词与参数记录](docs/assets/portraits/manifest.json) · [阅读完整人像教程](docs/美女生图教程.md)

<details>
<summary>这组图说明了什么</summary>

它们来自已记录的 Qwen-Image-2.1 本地文生图案例，首页只做 WebP 编码压缩，未裁切、修图或重新生成。样本之间可能同时改变脸部、姿态、衣料和房间细节；这些图展示各自的实际画面，不表示精确身份锁定或单变量实验。原记录中的生成偏差继续保留。

</details>

### 继续做角色、插画和广告

<table><tr>
<td width="50%" align="center"><a href="skills/oneirloom-style-design/templates/product-origin-world/template.md"><img src="skills/oneirloom-style-design/templates/product-origin-world/images/example-01.webp" alt="摄影巧克力与手绘可可庄园的广告案例" width="420"></a><br><strong>让产品走进它的故事</strong><br>摄影质感的巧克力，流入手绘可可庄园。</td>
<td width="50%" align="center"><a href="skills/oneirloom-style-illustration/templates/zhiguai-narrative/template.md"><img src="skills/oneirloom-style-illustration/templates/zhiguai-narrative/images/example-01.webp" alt="山雾与月色中的志怪叙事插画" width="420"></a><br><strong>让氛围服务于叙事</strong><br>旧纸、山雾、月色与人物之间的关系。</td>
</tr></table>

巧克力案例保留原始提示词，志怪插画的氛围得到用户认可；两者的模型与生成参数均未知。点击图片查看对应记录。

<details>
<summary>看角色衣橱设定</summary>

![包含服装、配件与材质细节的已有角色衣橱设定图](skills/oneirloom-character-sheet/templates/wardrobe-sheet/images/result-01.webp)

这个用户提供的结果展示了服装、配件、材质与版面安排。转身视图和部分服装头像仍有偏差，模型与参数未知。[查看角色衣橱模板与记录](skills/oneirloom-character-sheet/templates/wardrobe-sheet/template.md)。

</details>

### 从一份外卖，构思一张广告

<table><tr>
<td width="50%" align="center"><img src="skills/oneirloom-product-art-direction/references/takeaway-food-town/images/source.webp" alt="原始外卖产品照片" width="420"><br>原始产品照片</td>
<td width="50%" align="center"><img src="skills/oneirloom-product-art-direction/references/takeaway-food-town/images/accepted.webp" alt="用户认可的微缩食物小镇结果" width="280"><br>用户认可的结果</td>
</tr></table>

春卷成为屋顶，薯条成为台阶，餐盒里出现手绘街巷与微缩人物。食物仍保留摄影质感，创意从产品的形状和场景中展开。

织梦师的[产品创意方法](skills/oneirloom-product-art-direction/SKILL.md)会先检查产品，再选择故事和表现手法。这个案例记录了用户认可的一次结果，实际提交提示词、模型与参数未知。[查看案例记录](skills/oneirloom-product-art-direction/references/takeaway-food-town/evidence.json)。

## 创作方式

你不必一开始就准备完整提示词。先说目标，再给出已有材料。织梦师会沿用对话中已经确认的条件，明确目标、拆解画面，选择需要的方法，再适配模型并交付完整提示词。有结果图时，继续对照目标修正。

想改取景，就明确画框与身体的位置；想改姿态，就写清躯干、头部和四肢的关系；想改穿搭，就组织衣料、剪裁与叠穿；想改光线，就说明光从哪里来、哪些区域亮起来。

默认交付完整中文提示词和语义对应的英文版，每个版本独立可复制。明确要求只用一种语言时，就按你的要求输出。

首页主视觉以已有美女人像为参考，通过生图模型制作成新的宣传合成图；上面的 12 张作品图展示已有结果的压缩版。

## 你可以用它做什么

| 创作任务 | 交付内容 |
| --- | --- |
| 从想法开始生图 | 包含主体、环境、构图、光色与风格的完整提示词 |
| 借鉴或重构参考图 | 可见画面分析，以及按目标重写的提示词 |
| 构思产品广告 | 围绕产品特征设计的画面概念与提示词 |
| 制作角色设定 | 三视图、表情卡与服装设定图的提示词 |
| 修正生成偏差 | 对主要偏差的判断，以及完整修订版本 |
| 换用目标模型 | 保持视觉意图的模型版本，参数单独列出 |
| 写图文生图教程 | 具体提示词、配图说明与结果分析 |

集合提供 Krea 2 与 Qwen-Image-2.1 的专门适配。其他模型先使用通用自然语言描述，具体参考图输入与参数以你使用的入口为准。

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

一个主技能负责理解任务与整合交付，13 个方法技能负责各自的判断。具体画面配方放在所属方法的模板目录中。

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
| [oneirloom-figure-art](skills/oneirloom-figure-art/SKILL.md) | 成人非露骨人物艺术的姿态与遮挡 |
| [oneirloom-style-photography](skills/oneirloom-style-photography/SKILL.md) | 写实摄影、生活人像与电影感画面 |
| [oneirloom-style-illustration](skills/oneirloom-style-illustration/SKILL.md) | 绘画、版画、拼贴与叙事插画 |
| [oneirloom-style-design](skills/oneirloom-style-design/SKILL.md) | 海报、文字版式、包装、产品与 3D |
| [oneirloom-model-krea-2](skills/oneirloom-model-krea-2/SKILL.md) | Krea 2 提示词与入口适配 |
| [oneirloom-model-qwen-image-2-1](skills/oneirloom-model-qwen-image-2-1/SKILL.md) | Qwen-Image-2.1 提示词与任务适配 |
| [oneirloom-result-diagnosis](skills/oneirloom-result-diagnosis/SKILL.md) | 生成偏差分析与提示词修正 |
| [oneirloom-image-tutorial](skills/oneirloom-image-tutorial/SKILL.md) | 图文教程写作、扩写与润色 |

</details>

[三层架构](docs/architecture.md) · [模型证据](docs/model-evidence.md) · [摄影模板](skills/oneirloom-style-photography/templates/index.md) · [角色模板](skills/oneirloom-character-sheet/templates/index.md) · [插画模板](skills/oneirloom-style-illustration/templates/index.md) · [设计模板](skills/oneirloom-style-design/templates/index.md)

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
