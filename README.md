# 织梦师 Oneirloom

**把想象，写成画面。**

织梦师是一套包含 15 个开放源代码视觉创作 Agent Skills 的集合。它帮助 AI 助手分析参考图、编写图像提示词、构思产品广告和角色方案，并根据生成结果修订画面要求。织梦师提供创作方法和提示词，不包含生图模型或生成服务。

[项目主页](https://www.pigeonyang.top/skills/oneirloom/) · [在线安装说明](https://www.pigeonyang.top/skills/oneirloom/install/) · [安全说明](https://www.pigeonyang.top/skills/oneirloom/safety/) · [English](README.en.md) · [完整详情页](docs/product-page/index-oneirloom-v4.html)

[安装文档](docs/INSTALL.md) · [兼容性说明](docs/COMPATIBILITY.md) · [安全与隐私](docs/SAFETY.md) · [第三方材料说明](THIRD_PARTY_NOTICES.md) · [提交指南](docs/SUBMISSION.md)

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

### 手动安装到 Codex 项目

先按[安装文档中的 Git LFS 步骤](docs/INSTALL.md#fetch-the-complete-source)取得完整图片文件。GitHub 自动生成的源码 ZIP 可能只包含 LFS 指针。

将仓库的 `skills/` 下全部 15 个 `oneirloom*` 技能目录复制到 Codex 项目根目录的 `.agents/skills/`，让这些目录保持同级。保留每个目录中的全部原有文件，包括其中已有的 `scripts/`、`references/`、`templates/` 和 `assets/`。不要只复制 `SKILL.md`。

在新对话中请求“织梦师”或“Oneirloom”，也可以显式调用 `$oneirloom`。织梦师负责分析与编写提示词。图像生成由你选择的工具或服务执行。

上传 ZIP 到普通聊天不等于安装技能。宿主必须支持 Agent Skills。参考图分析还要求宿主能把图像传给助手。更多安装与兼容性信息见[安装文档](docs/INSTALL.md)和[兼容性说明](docs/COMPATIBILITY.md)。

### 用一个真实需求开始

第一次使用，也可以直接说：“用织梦师，把这个视觉想法写成完整生图提示词。”下方两个例子展示了如何说明目标、保留项和修改方向。得到提示词后，再将提示词放进生图工具。

~~~text
用织梦师分析我上传的产品照片，帮我构思一张广告。
保留产品的形状、包装和主要配色，加入手绘微缩世界。
先根据产品本身选择创意，再给我完整提示词，只要中文。
~~~

~~~text
用织梦师检查我上传的结果图和原提示词。
现在鞋子被裁掉了，我想要完整全身取景。
保留人物、衣服、房间和光线，给我完整修订提示词。
~~~

有参考图时，说明每张图负责身份、姿势、配色还是风格。已有目标模型、工具入口、原提示词或结果图时，也一起提供。

### 通过 Codex 插件安装

仓库 marketplace 已公开。以下 GitHub 简写命令尚未直接实测，已验证的公开源码克隆与本地 marketplace 路径见[安装文档](docs/INSTALL.md)：

~~~bash
codex plugin marketplace add PigeonAI-Yang/oneirloom --ref main
codex plugin add oneirloom@oneirloom-local
codex plugin list --marketplace oneirloom-local --json
~~~

这些命令添加并安装本仓库提供的 marketplace。若已有同名 `oneirloom-local` marketplace，请保留现有安装和本地修改，先核对其来源。仓库 marketplace 的发布不代表 Oneirloom 已进入或获准进入 OpenAI 官方插件目录。安装步骤和核验状态见[安装文档](docs/INSTALL.md)。

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

## 使用边界

参考图、生成结果和提示词可能包含私人或可识别信息。宿主和你选择的图像服务会按各自隐私条款处理输入。上传前，请检查相关条款，并确认你可以向该服务提供这些材料。发布生成结果前，请检查图像内容、使用条件和所需授权，只发布你有权公开的材料。付费生成前，请核对服务、费用和所需授权；只有你确认后才开始提交付费任务。

织梦师只提供创作方法与提示词。它不包含图像生成模型或服务。模型、生成结果、费用和数据处理方式由你选择的宿主与服务决定。

可选的提示词卡片渲染器把已有图片和提示词排成 3:4 PNG。它需要本机 Python、Pillow、Playwright 和 Chromium 兼容浏览器，宿主还须允许本地文件执行。仓库不捆绑这些运行依赖。渲染不生成图片，也不需要模型或 API 凭据。

## 文档

- [安装文档](docs/INSTALL.md)
- [宿主兼容性](docs/COMPATIBILITY.md)
- [安全与隐私](docs/SAFETY.md)
- [提交指南](docs/SUBMISSION.md)
- [第三方材料与许可说明](THIRD_PARTY_NOTICES.md)
- [三层架构](docs/architecture.md)
- [模型证据](docs/model-evidence.md)
- [摄影模板索引](skills/oneirloom-style-photography/templates/index.md)
- [角色模板索引](skills/oneirloom-character-sheet/templates/index.md)
- [插画模板索引](skills/oneirloom-style-illustration/templates/index.md)
- [设计模板索引](skills/oneirloom-style-design/templates/index.md)
- [贡献指南](CONTRIBUTING.md)

## 许可证

项目自有的技能说明与代码采用 [MIT License](LICENSE)。MIT License 不覆盖第三方图片和参考资料。随包提供的 Qwen-Image-2.1 官方参考资料按 Qwen Research License 说明用于非商业研究与评估。商业用途需要另行取得许可。请在使用第三方材料前查看[第三方材料说明](THIRD_PARTY_NOTICES.md)。
