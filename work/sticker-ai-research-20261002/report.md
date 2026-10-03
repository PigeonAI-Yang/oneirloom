# AI 表情贴纸设计研究：从聊天意图到可交付文件

研究日期：2026-10-02。本文是研究结论与流程提案，没有修改或启用现有 SKILL，也没有生成表情、组织真人测试、导入聊天软件或提交平台审核。

## 先把“好表情包”定义清楚

AI 表情包的核心问题是：收到上一条消息后，人为什么会选择这张图，对方又会怎样理解它。画面漂亮、角色相似、情绪标签正确、文件符合尺寸，各自只能证明一部分。一个微笑的角色可以表示感谢、敷衍、赞同或讽刺；“收到”也不等于“同意”。因此，设计单位应当是有使用情境的回应，而不只是“开心、伤心、生气”词表。

这一判断有不同强度的支持。Konrad 等人的研究记录了确认、调节语气、开始或结束对话、幽默和关系表达等用途，但数据采集于 2014 年，不能直接代表今天的中文聊天。Yang 等人的实验让受试者辨认明确情绪，没有测试真实上下文，也没有测试无脸角色。两类研究共同说明，情绪辨认与聊天适用性需要分开讨论。[S06](https://scholarworks.iu.edu/iuswrrest/api/core/bitstreams/d133da65-199f-4ed2-a061-4b9e2eddc5ef/content) [S08](https://journals.sagepub.com/doi/pdf/10.1177/27523543231188778?download=true)

本次证据分为四层，不能互相替代。

| 证据层 | 能支持什么 | 不能据此宣布什么 |
| --- | --- | --- |
| 设计与传播研究、专业教学 | 聊天功能、姿态可读性、变形与身份的设计理由 | 某个拟议动作必然被目标用户理解 |
| 模型论文、厂商能力文档 | 某方法或入口记载了参考图、编辑、文字、透明输出等能力 | 本地入口具备全部参数，或某模型最适合整套表情 |
| 平台官方规范 | 指定产品、文件类型、发布路径的要求与建议 | 通用表情包尺寸、统一描边、统一帧数 |
| 本文流程提案 | 基于上述证据形成的操作与检查方法 | 已经实测有效，或已经成为现行 SKILL |

三份证据笔记与补充论文共列出 **39 个不同的支持性 URL**，相同 LINE 静态指南已去重。WhatsApp 仓库首页和 README 是不同 URL，但共享内容；同一厂商的多个页面也不是独立交叉验证。这个数字不代表 39 项独立实验，更不代表已完成视觉样本库。完整书目在文末，阅读范围和失败访问单列。

研究范围也决定结论的边界。关于聊天用途，访谈和回忆式问卷能说明人们怎样使用，却不能保证每次接收都理解准确；情绪选择实验能比较辨认表现，却可能让受试者从给定选项中猜答案；贴纸检索实验测的是查询与候选的匹配，可能同时存在几个合理选择。它们适合帮助设计问题，不适合合并成一个“表情好用率”。本文因此不设统一理解分数，也不把一篇研究的平均正确率变成新角色的验收线。

另一个区别是“通行做法”与“必须遵守”。动作轮廓、变化和小尺寸可读性来自设计教学与平台建议，可以指导判断；尺寸、编码和审核流程由具体平台约束。原生 alpha、多参考和微调属于技术能力。把这些内容都叫“规范”，容易让流程堆上不必要的训练、蒙版和固定模板。本报告只在来源明确给出硬要求时使用硬要求，其余写出采用理由和适用条件。

## 六条可用于设计的原则

**1. 先写发送者在做什么。** “让对方知道消息已收到”“温和地拒绝”“接住对方的玩笑”比“可爱、开心”更接近设计任务。还要写关系、语气和预期下一步。Lim 的案例说明贴纸可参与道歉、感谢和缓和尴尬，但只是具体互动的分析，不能当成普遍成功率。[S07](https://journals.sagepub.com/doi/pdf/10.1177/2056305115578137)

**2. 身份包括部件的含义与连接。** 颜色相同并不足够。触手不能变成人手，天线不能变成眉毛，承托物体的网不能变成装饰花边。允许弯曲、压缩和遮挡，但要保留角色成立的关系。动画教学支持通过变形表达重量和材质，同时提醒避免丢失角色模型；它没有提供通用变形百分比。[S05](https://www.animationmentor.com/blog/squash-and-stretch-the-12-basic-principles-of-animation/)

**3. 动作必须在缩小后仍然成立。** 判断倾斜方向、重心、伸展、接触点和轮廓是否表达同一件事。关键动作埋在身体内部，就可能只剩一个毛团。无脸角色可以通过身体和物体互动表演，但不能把人形骨架教学直接翻译成不存在的肩膀、手指和嘴。[S03](https://www.animationmentor.com/blog/tutorial-building-appealing-character-poses-for-animation/) [S04](https://www.animationmentor.com/blog/tutorial-animating-emotion-through-body-language/)

**4. 风格要从图中读出关系。** “可爱 3D”不能说明形体压缩、绒毛密度、光泽、轮廓处理、文字位置或动作强度。先看实际风格图在聊天尺寸下怎样组织这些要素，再决定哪些可迁移。身份参考、姿态参考和风格参考需要分别标注。Adobe 明确区分风格控制与轮廓、深度等结构控制；二者都不是身份锁定保证。[S14](https://developer.adobe.com/firefly-services/docs/firefly-api/guides/concepts/style-image-reference/) [S15](https://developer.adobe.com/firefly-services/docs/firefly-api/guides/concepts/structure-image-reference/)

**5. 整套统一的是角色与视觉语言，变化的是回应。** 统一材质、色彩关系、文字处理和视觉尺度，同时让动作、视角、强度与关系语气产生有效区别。LINE 推荐日常可用、容易理解和有变化的组合；这支持检查重复，却不意味着每套都要凑齐固定情绪清单。[S01](https://creator.line.me/en/guideline/sticker/)

**6. 文字、透明度与文件检查服务于意义。** 字幕可以直接承担回应，不必强迫每张无字也完全自明；但必须检查字词是否准确、姿态是否矛盾。透明通道需要读实际文件，并在不同背景上看边缘。白底、棋盘格图案或 PNG 扩展名都不能单独证明透明。LINE 的消息贴纸预览建议支持把字图组合放进聊天情境检查。[S02](https://creator.line.me/en/guideline/messagesticker/detail/)

把这些原则用到整套设计时，统一程度需要服从使用区别。工作群里的克制确认与朋友间的夸张确认，可以保留同一角色，却采用不同姿态幅度和字图比例；如果任务只面向一种关系，就不必为了“丰富”加入另一种。相反，两个近似姿态若分别标成“等一下”和“辛苦了”，需要解释可见动作为什么支持不同目的。无法解释时，应合并、改动作或换意图，而不是增加装饰。

视觉参考也应回答这种具体问题。一个参考可以帮助观察毛绒角色怎样缩成紧凑轮廓，另一个帮助看文字如何绕开触手，第三个帮助理解某种动作的重心。来源多不等于需要把所有参考同时喂给模型。先明确各自贡献，才能判断生成结果借用了哪些关系、又错误复制了哪些服装、道具或人体动作。本次尚未取得实际看过的代表图，因此不会把文字归纳冒充完成的风格提炼。

## 平台要求没有共同的一套数字

以下是本次读取的官方页面快照。数字只属于表中产品与路径；需要实际导入或发布时，还应针对目标入口核对。硬要求与建议分开保留。

| 平台与交付类型 | 已核实文件要求 | 套包、配套文件与流程 | 建议或证据边界 |
| --- | --- | --- | --- |
| LINE Creators Market 静态贴纸 | PNG、RGB、透明；宽高偶数，最大 370×320；单图最大 1 MB | 8/16/24/32/40 张；主图 240×240，聊天图标 96×74；ZIP 最大 60 MB；售卖前审核 | 约 10 px 留白是 LINE 建议；至少 72 dpi 是页面元数据要求，不能解释为通用屏幕清晰度标准。[S01](https://creator.line.me/en/guideline/sticker/) [S28](https://creator.line.me/en/review_guideline/) |
| Telegram 静态贴纸 | PNG 或 WebP；一边恰为 512 px，另一边不超过 512 px | 官方指向 @Stickers 管理与发布 | 所读页面未给静态文件大小或套包数量上限，不能补写常见的 512 KB；透明、白边和黑影列为提示。[S29](https://core.telegram.org/stickers) |
| WhatsApp 第三方 Android 套包 | 静态 WebP、512×512、透明，最大 100 KB | 每包 3–30 张，静态与动态分包；托盘图 96×96、最大 50 KB；独立 App 经用户确认添加 | 8 px 白色外描边是建议。此处证据来自官方仓库 Android 路径，不等于已经核实当前 App 内置制作器。[S33](https://github.com/WhatsApp/stickers/blob/main/Android/README.md) |
| Discord 自定义服务器贴纸 | PNG 或 APNG，320×320，最大 512 KB；动画最高 60 FPS | 有权限者在桌面或网页服务器设置中逐个上传，关联 emoji 用于推荐 | 透明背景是建议；所读页没有总帧数、时长或统一留白数值。槽位与跨服务器使用另受账户和服务器条件影响。[S34](https://support.discord.com/hc/en-us/articles/4402687377815-Tips-for-Sticker-Creators-FAQ) [S35](https://support.discord.com/hc/en-us/articles/4403089981975-Custom-Stickers-FAQ) |
| Slack 自定义 emoji | JPG、PNG、GIF；GIF 最多 50 帧 | 上传并命名，受工作区权限控制 | 这是 emoji，不是贴纸提交系统；正方形、透明、低于 128 KB 是“效果最好”的建议，不能写成硬上限；所读页没有像素尺寸。[S36](https://slack.com/help/articles/206870177-Add-custom-emoji-and-aliases-to-your-workspace) |
| 微信表情开放平台 | **SOURCE GAP** | 官方入口已定位，但制作规范正文未读到 | 第三方转述有文件大小、数量冲突。本报告不填入未经官方正文核实的数字，也不把工具错误推断成登录要求。 |

动态另走对应分支。LINE APNG 有 5–20 帧、1–4 次循环及总播放不超过 4 秒等要求；Telegram 视频贴纸采用 VP9 WebM，最长 3 秒、最高 30 FPS、最大 256 KB且无音轨；WhatsApp Android 仓库要求动态文件最大 500 KB、单帧至少 8 ms、总时长不超过 10 秒。这些差异本身就否定了统一帧数方案。[S27](https://creator.line.me/en/guideline/animationsticker/) [S29](https://core.telegram.org/stickers) [S30](https://core.telegram.org/stickers/webm-vp9-encoding) [S33](https://github.com/WhatsApp/stickers/blob/main/Android/README.md)

## 建议流程：每一步都要产生可以判断的设计

下表是本研究的流程提案，不是行业规定的八个阶段。它延续现有 Understand → Observe → Design，先解决对象和意图，再选工具。已有可用角色母版时直接复用；只有身份构造尚未解决，才需要补角色设定。

| 步骤 | 真正需要思考的问题 | 留下的成果 | 怎么检查，失败返回哪里 |
| --- | --- | --- | --- |
| 1. 明确聊天任务 | 谁对谁说？前一句是什么？希望对方知道或做什么？要提示词、预览还是成套文件？ | 简短任务说明，固定文案、目标平台与已知边界 | 找一个具体使用场景。无法说明使用时机，先缩小意图，不能用情绪词代替。 |
| 2. 理解角色 | 哪些是身体、附肢、符号和工具？怎样连接？什么可以变形？ | 固定身份与可变表达的区分，未知结构单列 | 对照实际母版追踪连接和语义。遮挡不等于减少部件；未知背面不擅自补全。 |
| 3. 观察风格 | 实图中什么先被看见？形体、动作、字、材质和颜色怎样配合？ | 标明来源和参考用途的观察，选择保留与改变的关系 | 缩小看轮廓、重叠和字图比例。没有实图就标为原创设定，不虚构观察。 |
| 4. 设计套包和单张 | 相邻回应怎样区别？视角怎样解释接触？字幕放哪里才不挡动作？ | 意图矩阵；每张的动作、文案、视角、姿态关系与可能误读 | 用上一句消息尝试选图。多个项目只是换标签，就重新设计动作或语气差异。 |
| 5. 解决关键不确定性 | 无脸是否读得懂？大幅变形会丢身份吗？所选工具能写准确文字吗？ | 少量有差异的校准案例及观察 | 案例数量由问题决定，不设固定数量或逐步审批；结果揭示哪层失败，就回哪层修。 |
| 6. 逐项生产 | 当前入口能接受哪些参考和控制？每项是否真有独立回应？ | 实际输出、已知提示词和入口设置 | 区分能力文档与本地实测。每项从合适母版或认可视图开始，局部修复保留成功部分。 |
| 7. 单张与整套检查 | 意图、身份和变化成立吗？字准确吗？缩略图和背景上读得清吗？ | 逐项缺陷与整套重复、缺项记录；可用时收集接收者解释 | AI 可先做图文检查。真人反馈缺失只留下真人理解未验证，不阻塞其他可完成工作。 |
| 8. 导出和交付 | 每个文件独立完整吗？目标平台路径真的验证了吗？ | 单图、文件—意图—字幕映射、预览、来源与已知生成信息 | 实际读尺寸、编码、alpha，并看每个导出文件。概念板、透明通过、聊天理解与平台导入分别报告。 |

流程不要求每一步都交给用户审批。AI 可以先整理聊天场景、读取已有身份、提出矩阵、写完整提示词和检查输出；只有材料不足以决定关键身份含义、用户偏好或授权边界时，才需要提问。校准也不是固定仪式。若已有近期可复用的输出证明温和动作稳定，新的问题只是文字准确性，就针对文字做验证；不必重新从角色设定开始。反过来，若试图把织梦网改成礼物容器，已经触及含义，应回到身份与动作设计，而不是只调参考权重。

修正记录应当能够解释下一次改什么。例如“第三触手与网脱开，动作像递礼物”比“缺乏灵动感”有用。前者可以分别检查连接和前伸关系，保留已经正确的材质与字体；后者无法判断问题来自设计还是生成。连续修正仍出现同一关键错误时，应保留失败图、实际提示词和入口信息，按现有诊断方法限定调查范围，不靠不断增加同义形容词继续抽图。

## AI 生产路线按实际条件选择

当前官方资料支持参考图生成与编辑，也承认身份、文字和构图仍需检查。Qwen-Image-2.1 文档记载多参考与 RGBA；OpenAI 文档记载参考图、多个候选和透明选项；FLUX 编辑文档支持参考驱动的修改。这证明存在可选机制，不证明本地入口开放了相同参数，也不构成模型排名。[S13](https://developers.openai.com/api/docs/guides/image-generation) [S21](https://github.com/QwenLM/Qwen-Image-2.1) [S23](https://docs.bfl.ai/flux_2/flux2_image_editing)

| 路线 | 适用条件 | 必须承担的检查 |
| --- | --- | --- |
| 母版参考生成或编辑 | 已有身份图，入口支持适当参考 | 每张既保留身份，又真正改变动作；避免把上一张变形不断传给下一张。 |
| 单张直接生成 | 原创角色或已验证提示词能满足当前身份要求 | 不能把文字描述当身份保证；逐张比对。 |
| 联系表／网格 | 需要并排选方向；或实际网格已具备可独立导出的质量 | 概念板不自动变成套包。每个裁片仍需检查分辨率、断肢、串字、跨格和透明度。 |
| 可选文字、alpha 或合成修复 | 观察到文字、边缘缺陷，或明确需要可编辑字稿 | 修复不能掩盖动作歧义；检查新增字与图的关系、细触手和绒毛边缘。 |
| 可选身份训练 | 反复生产中，代表性参考试验仍持续失败；且有兼容后端和合适素材 | 使用未训练的回应检查身份与表达范围。不要把只会复现原姿态当成功。 |

必须分清四件事：多张输入参考、同一任务的多个候选、多个不同回应任务，以及一张图里的多个格子。它们的数量与含义不相同。蒙版、分层、矢量代码或训练都不应成为默认前置条件。DreamBooth 和 IP-Adapter 支持可选技术路径，不能据此要求所有表情包安装和训练。[S25](https://arxiv.org/abs/2208.12242) [S26](https://arxiv.org/abs/2308.06721)

贴纸专门研究也没有消除设计工作。Text-to-Sticker 分别评估画质、提示符合度、风格与场景多样性，其特定平面、无文字训练目标不是通用规范。SEAL 讨论单图训练中身份与背景、原姿态纠缠，实验基于 SD 2.1 和 20 个概念，不能推出当前工具优劣。VSD2M 说明动态贴纸的离散动作与一般写实视频不同，实验所用八帧也不是导出标准。[S37](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08828.pdf) [S38](https://arxiv.org/html/2604.26883v1) [S39](https://arxiv.org/html/2412.08259v1)

这些论文对验收更有价值的启示，是不要用一个指标包办所有结果。SEAL 所讨论的身份保留与新动作控制可能相互牵制：过于接近母版的图也许姿态没变，动作丰富的图也可能已经换了角色。Text-to-Sticker 将风格与场景多样性分开评估，同样提醒我们分别观察“这一套像一家人”和“这一套真的能说不同的话”。这是从研究问题得到的流程推论，不是本文完成的对比实验。

动态设计应先写关键姿态、动作转折、可读停留与循环关系，再检查跨帧身份、alpha 和首帧。在不播放时仍需表达完整信息的平台，要单独检查首帧；选帧数和编码则服从目标平台。

## 织梦师的两个待验证案例

以下身份依据现有任务描述，不是本轮重新看图所得：紫色毛绒无脸身体，暗色正面及金星，金球天线，四条触手与蓝色织梦网。金星和暗面不是人脸。具体连接、柔韧度和可见范围仍以真实母版为准。

| 拟议回应 | 设计及网的作用 | 误读与修正方向 |
| --- | --- | --- |
| “收到”回应一项通知 | 身体朝向交流对象，网被稳定收持，表示已经接住信息；动作克制，字幕明确“收到”。四触手逐条交代，允许有依据的遮挡。 | 举高网、庆祝或大幅鞠躬可能变成“赞同”或“谢谢”。网不额外承载礼物；在“稍后再讨论方案”的上下文检查是否暗示同意。 |
| “谢谢你”回应帮助 | 身体做适度致意，网仍由角色收持在身侧或身体附近，支持温和态度；字幕参与表达感谢。具体倾斜程度待母版与实图确定。 | 把网和物体递到画面前方可能读成送礼、索取或交付。先调整朝向、距离和接触关系，再考虑文字，不凭爱心装饰宣布感谢成立。 |

这两个方案都没有通过生成或接收者测试。可以先请目标接收者自由解释，再给出前一句消息询问“发送者是什么意思、你接下来会怎样回应”。这种开放回答比只让人勾选预设情绪更容易暴露误读，但属于本地拟议测试方法；相关 emoji 与贴纸检索研究不能直接证明本角色的理解率。[S09](https://grouplens.org/site-content/uploads/Emoji_Interpretation_Paper.pdf) [S10](https://arxiv.org/html/2506.01668v1)

测试时还应允许“都可以”“都不适合”以及直接发文字。强迫从套包里选一张，会隐藏缺失的回应。字幕版与无字幕版可分别观察，但无字幕检查只是定位图像贡献，并不是要求删字。若有人把“收到”读成“感谢”，需要记录他看到的版本和前文，再查究竟是鞠躬幅度、网的位置还是双方关系造成了理解；不能只把答案改名，宣称这张已经通过。

## 验收保留四种独立结论

| 层次 | 需要的直接证据 | 不能代替它的东西 |
| --- | --- | --- |
| 语义与使用 | 指定上下文下的回应判断；若声称真人理解，则记录实际参与者、版本和解释 | 情绪词、AI 自评、漂亮程度；没有真人测试就保留该缺口。 |
| 视觉家族 | 逐张与整套的实际图像检查，包含身份、动作变化、字幕及缩小显示 | 相似度数值、同一色板、只看一张母版。 |
| 文件 | 每个实际导出文件的尺寸、编码、alpha、裁切与边缘证据 | 成功调用、导出计划、网格预览。 |
| 平台 | 目标路径真实导入、显示或审核结果，按承诺范围记录 | 规范阅读、文件合格、模拟界面；导入也不等于商店审核通过。 |

现有 SKILL 已经包含先理解身份、参考角色区分、意图矩阵、条件校准、alpha 检查及逐文件交付，因此本次不建议推倒重写。优先缺口是：第一，三个模板都明确没有对应图像或生成记录，需要真实可观察的风格／动作样例；第二，把意图矩阵补足前文、关系、预期下一步和邻近误读；第三，进一步区分参考角色、候选数量、不同任务与网格；第四，为已请求的动态任务增加关键姿态和时间检查；第五，把现有字幕、alpha、整套检查转成真实结果证据。英文提案另见 [proposed-sticker-sop.md](proposed-sticker-sop.md)，仍是待审阅方案。

## 书目、阅读范围与证据缺口

下列 URL 的研究读取日期均为 2026-10-02。官方文档无可见日期的，按本次读取快照使用；论文年份是发表或预印本版本日期。原始证据见 [传播与设计笔记](design-communication-evidence.md)、[AI 生产笔记](ai-production-evidence.md) 和 [平台笔记](platform-evidence.md)。教学文章的文字阅读不计为已看嵌入视频或视觉案例。

| 编号 | 直接来源 | 类型与本次阅读范围 |
| --- | --- | --- |
| S01 | [LINE 静态贴纸指南](https://creator.line.me/en/guideline/sticker/) | 官方正文；设计建议与特定平台要求。 |
| S02 | [LINE 消息贴纸制作](https://creator.line.me/en/guideline/messagesticker/detail/) | 官方正文；特定可编辑文案产品。 |
| S03 | [Anthony Wong：Building Appealing Character Poses](https://www.animationmentor.com/blog/tutorial-building-appealing-character-poses-for-animation/) | 专业教学，2026-04-07；文字，未看视频。 |
| S04 | [Natasha Krinsky：Animating Emotion Through Body Language](https://www.animationmentor.com/blog/tutorial-animating-emotion-through-body-language/) | 专业教学，2026-06-30；文字，未看视频。 |
| S05 | [Chris Hurtt：Squash and Stretch](https://www.animationmentor.com/blog/squash-and-stretch-the-12-basic-principles-of-animation/) | 专业教学，2017-06-05；正文。 |
| S06 | [Konrad、Herring、Choi：Sticker and Emoji Use in Facebook Messenger](https://scholarworks.iu.edu/iuswrrest/api/core/bitstreams/d133da65-199f-4ed2-a061-4b9e2eddc5ef/content) | JCMC 2020；全文，访谈与回忆式问卷，数据于 2014 年采集。 |
| S07 | [Sun Sun Lim：On Stickers and Communicative Fluidity](https://journals.sagepub.com/doi/pdf/10.1177/2056305115578137) | 2015；全文，具体互动的反思文章。 |
| S08 | [Yang、Atkin、Labato：Gleaning Emotions from Virtual Stickers](https://journals.sagepub.com/doi/pdf/10.1177/27523543231188778?download=true) | Emerging Media 2023；全文，受限样本的情绪选择任务。 |
| S09 | [Miller 等：Blissfully Happy or Ready to Fight](https://grouplens.org/site-content/uploads/Emoji_Interpretation_Paper.pdf) | ICWSM 2016；全文，emoji 解释实验，非贴纸实验。 |
| S10 | [Chee 等：Small Stickers, Big Meanings](https://arxiv.org/html/2506.01668v1) | 2025-06-02 预印本；全文，检索式标注，所读版本标注审稿中。 |
| S11 | [Hu 等：Emotion and Intention Guided Multi-Modal Learning](https://ojs.aaai.org/index.php/AAAI/article/view/38509) | AAAI 2026；仅论文页与摘要，未采用实验效果量。 |
| S12 | [Zhang 等：STICKERCONV](https://aclanthology.org/2024.acl-long.417/) | ACL 2024；仅摘要，合成对话不等于真人使用。 |
| S13 | [OpenAI image generation guide](https://developers.openai.com/api/docs/guides/image-generation) | 官方 Docs MCP 正文；API 能力与限制，未调用模型。 |
| S14 | [Adobe style image reference](https://developer.adobe.com/firefly-services/docs/firefly-api/guides/concepts/style-image-reference/) | 官方正文；风格控制与输出变体。 |
| S15 | [Adobe structure image reference](https://developer.adobe.com/firefly-services/docs/firefly-api/guides/concepts/structure-image-reference/) | 官方正文；轮廓和深度控制。 |
| S16 | [Adobe reference images for consistent results](https://helpx.adobe.com/photoshop/desktop/create-open-import-images/create-images/use-reference-images-for-consistent-results.html) | 官方正文，更新 2026-08-18；Photoshop 集成，非通用 API 合同。 |
| S17 | [Adobe remove background](https://helpx.adobe.com/uk/firefly/web/work-with-images/edit-images/remove-background.html) | 官方正文，更新 2026-09-23；透明 PNG 下载路径。 |
| S18 | [Wu 等：Qwen-Image Technical Report](https://arxiv.org/abs/2508.02324) | 2025-08-04 论文摘要页；不代表所有后续版本。 |
| S19 | [Qwen-Image 官方仓库](https://github.com/QwenLM/Qwen-Image) | 官方正文；版本各自的编辑输入能力。 |
| S20 | [Qwen-Image-Edit-2511 model card](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) | 官方模型卡；一致性是作者声明，非本地测试。 |
| S21 | [Qwen-Image-2.1 官方仓库](https://github.com/QwenLM/Qwen-Image-2.1) | 官方正文；新闻发布于 2026-09-20，多参考及 RGBA 示例未执行。 |
| S22 | [BFL FLUX.1 Kontext image editing](https://docs.bfl.ai/kontext/kontext_image_editing) | 官方正文；页面已称上一代选项。 |
| S23 | [BFL FLUX.2 image editing](https://docs.bfl.ai/flux_2/flux2_image_editing) | 官方正文；API 与界面区别，未实测。 |
| S24 | [BFL multi-reference editing help](https://help.bfl.ai/articles/6546682167-what-is-multi-reference-editing) | 官方正文；不同变体限制，非统一参考数。 |
| S25 | [Ruiz 等：DreamBooth](https://arxiv.org/abs/2208.12242) | 2022 预印本／CVPR 2023；论文摘要页，主体微调机制。 |
| S26 | [Ye 等：IP-Adapter](https://arxiv.org/abs/2308.06721) | 2023 论文摘要页；适配器机制，非任意模型兼容声明。 |
| S27 | [LINE 动态贴纸指南](https://creator.line.me/en/guideline/animationsticker/) | 官方正文；APNG 专属要求。 |
| S28 | [LINE 审核指南](https://creator.line.me/en/review_guideline/) | 官方相关章节；商店审核。 |
| S29 | [Telegram Stickers](https://core.telegram.org/stickers) | 官方正文；静态、TGS、视频与 emoji 分开。 |
| S30 | [Telegram WebM VP9 encoding](https://core.telegram.org/stickers/webm-vp9-encoding) | 官方正文；视频编码与发布路径。 |
| S31 | [WhatsApp stickers 官方仓库](https://github.com/WhatsApp/stickers) | 官方正文；与 S32 部分重复。 |
| S32 | [WhatsApp stickers README](https://github.com/WhatsApp/stickers/blob/main/README.md) | 官方正文；第三方 App 路径和 iOS 商店边界。 |
| S33 | [WhatsApp Android README](https://github.com/WhatsApp/stickers/blob/main/Android/README.md) | 官方正文；本文 WhatsApp 数值的主要依据。 |
| S34 | [Discord Tips for Sticker Creators](https://support.discord.com/hc/en-us/articles/4402687377815-Tips-for-Sticker-Creators-FAQ) | 官方正文，页面更新 2022-05-26。 |
| S35 | [Discord Custom Stickers FAQ](https://support.discord.com/hc/en-us/articles/4403089981975-Custom-Stickers-FAQ) | 官方正文，页面更新 2025-10-04。 |
| S36 | [Slack Add custom emoji and aliases](https://slack.com/help/articles/206870177-Add-custom-emoji-and-aliases-to-your-workspace) | 官方正文；emoji，不是贴纸规范。 |
| S37 | [Sinha 等：Text-to-Sticker](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08828.pdf) | ECCV 2024；PDF 文本首 300 行，后续定位和截图失败，没有看图验证。 |
| S38 | [Roh 等：SEAL](https://arxiv.org/html/2604.26883v1) | 2026-04-29 预印本全文；同行评审状态未核实，不采用有矛盾的表格增幅。 |
| S39 | [Yuan 等：VSD2M](https://arxiv.org/html/2412.08259v1) | 2024-12-11 预印本全文；未移用实验帧数，人工评估人数前后不一致未引用。 |

S11 和 S12 只作为研究方向支持：前者把情绪与意图纳入回应选择，后者研究合成多模态对话，本文不借它们宣布真人有效性。S16–S20、S22、S24 为条件生产路线的能力背景，不能替代选定入口的运行检查。

未计入支持性来源的缺口包括：LINE 2018 [表达指南](https://lineforbusiness.com/files/en_LINE%20Sticker%20Expression%20Guide_2018.pdf)截图没有返回可见图像；[WhatsApp 语用分类论文](https://www.benjamins.com/online/prag/articles/prag.24063.lin)正文读取失败；WhatsApp [iOS README](https://github.com/WhatsApp/stickers/blob/main/iOS/README.md)后续读取返回 503，两个[帮助中心页面](https://faq.whatsapp.com/1056840314992666/)及[使用说明](https://faq.whatsapp.com/639351827594474/?locale=en_US&cms_platform=web)没有正文。微信[制作规范入口](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html#/makingSpecifications)和[平台首页](https://sticker.weixin.qq.com/)均发生不可重试工具错误。WACV 2026 StickerNet 原文返回 403，已停止访问，未作为支持证据。Qwen 2.1 博客未取得正文，相关保留结论改由官方仓库支持。

本轮取得的是文献、文档及现有 SKILL 的研究证据。实际视觉参考收藏、生成案例、真人聊天理解、动画播放和平台导入的完成数均为零。
