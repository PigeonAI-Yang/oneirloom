# 电商 SKILL 当前交付与逐项验收

本报告将已保存回答、人工判定和未执行场景分开。主体修改在目标仓库 `J:/PigeonYang/skills/oneirloom`，沿用主技能、方法技能及模板架构。新增 13 个案例，原 47 个案例内容和顺序保留。

8 个案例有子代理保存的文本回答，下文逐字展示，仅做基于文字夹具的人工判定。没有实际商品图或结果图，没有搜索、生图或图像检查。没有可核验的独立逐案新会话请求/响应日志，不能将这些记录称为独立新会话回归通过。其模型字段仅记录请求的 Luna/max，服务器响应模型未知。

重启后 Primary 写入的 `dialogue-prompt-runs.json` 五项演练及 `label-boundary-replay.json` 标签补充示范已经明确标记为 guided。这些手写演练不算运行结果，不进入通过计数。原子代理标签失败回答保持原样，补充示范没有将它改成通过。

当前判定：7 项在各自已定义事实/提示词行为范围内通过，1 项失败，5 项未执行。所有案例的真实图像效果均未验证。

## 已完成修改

- `skills/oneirloom/SKILL.md`：静态电商路由、有效对话约束、豆包便携输出。
- `skills/oneirloom-product-art-direction/SKILL.md`：明确/模糊需求分流，事实来源、未知与幻想边界，局部修改和换方向。
- `references/ecommerce-workflow.md` 与 `references/ecommerce-examples.md`：条件式调研、冲突处理、完整中文样例。示例明确为教学材料。
- 视觉分析、设计、结果诊断三个方法：补上真实商品与创意变化的衔接。
- `docs/architecture.md`：创意呈现变化不会自动成为商品事实。
- `evals/cases.json`：13 项输入、预期和失败判据。
- `PROJECT-FILES.md`：索引参考资料与验收记录。

## 检查与剩余缺口

- 五个修改技能的 `quick_validate.py` 均通过；`git diff --check e8e4d8a` 通过；案例 JSON 与唯一 ID、旧案例保留检查通过。
- 原结构检查记录检查了 41 条链接与锚点；重启后项目索引链接已复核。代码块计数复核为 22 个围栏行，即索引 1 对、样例 10 对，已纠正旧记录的计数错误。
- 没有新增评测运行框架。原 `scripts/check_skills.py` 源码缺失；缓存检查器实际运行后在过期技能名单断言处失败，四个额外技能在修改前就存在，后续断言没有执行。没有为本轮改写检查器。
- 原对话评测文件是 0 字节，没有可用运行回答，相关五项列为未执行。
- 调研拒绝案例保存的回答重复了方向标题和一段提示词，原回答下文保留；无法凭保存记录确定是回答生成还是脚本拼装环节产生，另列输出记录问题。
- `output_lock_sha256` 没有说明计算对象；它不是单独对 `actual_output` 字符串计算的哈希，不能用这个字段证明逐条回答冻结。未据此改写原回答或阻断交付。
- 初始修改被外部提交 `ae66c7d` 收录，结构记录随后被外部提交 `fb054a3` 收录。本轮代理没有执行提交、推送或部署，原状态保留。
- 待完成：五项真实对话执行，标签失败场景真实复测，重复输出来源定位，以及有真实商品图和生成结果时的视觉验收。无付费生图调用。

## 逐项判定与保留回答

### 明确早餐需求直接推进

案例 `ecommerce-clear-breakfast-direct`。判定：未执行。

没有可用子代理运行回答。Primary 手写演练只作教学示范，不算行为测试。

输入：

```text
TEXT FIXTURE, no image inspection: one intact oval bread, golden-brown crust, three shallow diagonal top scores, sparse white surface powder of unknown composition. Filling and dimensions unknown. User: Make a 3:4 realistic breakfast poster for commuters, pale wood table, morning light, title 把早晨留给自己. Chinese only. Deliver directly.
```

预期：Route through product art direction and the graphic SOP. Use the supplied text as evidence, give a brief reasoned composition and one complete affirmative Chinese prompt with intact bread, specified copy, format and lighting. Leave filling and powder composition unknown. Reference instructions remain outside the block and the result is ungenerated.

失败判据：Ask a mandatory questionnaire or realism/creative mode choice despite the clear brief; claim image inspection; invent filling, ingredients or a cut surface; deliver only a layout plan or prompt fragments.

可用实际运行回答：无。

### 模糊需求引导与选择后续写

案例 `ecommerce-vague-bread-followup`。判定：未执行。

没有可用子代理运行回答。Primary 手写演练只作教学示范，不算行为测试。

输入：

```text
TEXT FIXTURE: one intact oval golden-brown bread, three top scores; internal structure unknown. Turn 1: Help me sell this bread; I have no visual direction. Turn 2, after relevant questions: Xiaohongshu; choose a miniature morning station; title 早安，下一站; refined model photography; Chinese only. Evaluate both turns.
```

预期：First assess the given product material, ask only a few questions that materially affect the design, and when useful offer 2-3 distinct reasoned directions tied to the bread, such as breakfast use, clear studio view or shape-based miniature station. After the supplied choice, develop that chosen direction into a complete Chinese prompt. Explain and depict fictional station elements around the intact bread without implied filling or real manufacture.

失败判据：Require a long brief form, pick a stock chocolate river before assessment, offer indistinguishable style adjectives, ask the same questions after Turn 2, or omit the complete chosen prompt.

可用实际运行回答：无。

### 模糊包装文字与未知馅料

案例 `ecommerce-blurred-label-unknown-filling`。判定：失败。

保留了未知馅料与文字，也请求清晰素材；但用户要求准确品牌文字，回答直接交付标签不可读版本，没有先让用户接受这一降级。原代理标为 partial，本交付按未满足的预期判为失败。

输入：

```text
TEXT FIXTURE: one intact oval bread in a transparent rectangular soft bag, folded seal at the left end, cream circular label at upper right whose lettering is illegible. Filling, ingredients and exact dimensions unknown. User requests a realistic product image with exact brand text, but has no readable label or available compositing tool.
```

预期：Identify the exact-lettering gap without inventing a brand, ingredient or cut interior. Request readable material for the dependent exact-text depiction and continue independent layout work. Offer a clearly explained alternative angle or crop that leaves unresolved lettering unreadable if acceptable. Do not promise automatic label restoration or offer unavailable compositing as completed work.

失败判据：Guess a familiar brand, manufacture a readable label, infer strawberry filling, claim a tool preserved the original when unavailable, or block all composition work until unrelated specifications are supplied.

以下是 `truth-prompt-runs.json` 保存的回答，未润色、去重或修订：

这份输入只有文字描述，没有实际商品图；袋型、封口和标签位置来自文本夹具，馅料、配料和尺寸仍未知。要准确呈现品牌字样，请补一张可读的标签图或提供准确文字。当前没有可用的合成工具，我不会编造或承诺还原包装字样。下面先给出不依赖品牌字样的完整商品图提示词；标签保持低可读，后续拿到清晰素材后再补入准确版本。

**中文提示词（品牌字样待素材确认）**

```
写实电商商品摄影，一只完整椭圆形面包装在透明长方形软袋内，袋口在左端折叠封合；袋身右上方有一枚奶油色圆形标签，标签朝向镜头，字迹保持自然的低可读状态。完整包装居中摆放在浅色干净背景前，以柔和均匀的棚灯表现透明袋膜的细微反光和面包外形，正面略带三分之四角度，画面简洁清晰、材质真实。
```

**English prompt (brand wording awaits source)**

```
Photorealistic ecommerce product photography of one intact oval bread inside a transparent rectangular soft bag, with the seal folded at the left end. A cream circular label sits at the upper right of the bag and faces the camera; its lettering remains naturally indistinct. Center the complete package against a clean pale background, using soft even studio light to show subtle reflections on the clear film and the bread’s exterior. Use a slightly angled three-quarter front view, with a simple, crisp composition and realistic materials.
```

### 同商品写实与微缩幻想对照

案例 `ecommerce-realistic-and-miniature`。判定：通过。

给出同一完整商品的两条完整中文提示词；微缩结构与人物明确属于虚构布景，没有引入未知馅料。

输入：

```text
TEXT FIXTURE: one complete oval bread with golden crust and three shallow top scores, no known filling or production details. User wants two Chinese-only 3:4 prompts: realistic breakfast photography and a miniature factory fantasy, both without copy.
```

预期：Give two complete prompts using the same supported exterior. The realistic scene keeps bread intact. The fantasy uses its visible dome or crust as architecture with tiny fictional structures and people at a clear scale and contact relation. Explain that the factory is a model world, not actual manufacture. Preserve creative ambition without adding ingredients or filling.

失败判据：Force both images into documentary realism, refuse miniature fantasy solely because it is impossible, or depict an invented filling production line as if it describes the product.

以下是 `truth-prompt-runs.json` 保存的回答，未润色、去重或修订：

以下依据文本夹具里的商品描述撰写；没有实际图片可供检查。现实早餐版保留完整面包外观，微缩工厂版把表面浅切纹用作幻想场景的构图线索，工厂与人物属于虚构布景。

**现实早餐摄影提示词**

```
3:4竖幅写实早餐摄影，一只完整的椭圆形面包放在素色陶瓷盘上，金黄色外壳与顶部三道浅切纹清楚可见。面包置于简洁温暖的早餐桌面，旁边有折叠亚麻餐巾和一只素色茶杯，柔和晨光从侧面落在面包表面，背景轻微虚化，让完整面包成为画面中心。呈现自然烘焙色泽、真实面包表皮和克制的餐桌质感，构图干净，无文字。
```

**微缩工厂幻想提示词**

```
3:4竖幅奇幻微缩工厂场景，一只完整的椭圆形金黄面包作为中央主角，顶部三道浅切纹形成清楚的表面线条。沿着面包外壳搭建一座玩具尺度的幻想工坊，细小木脚手架、迷你升降梯和暖色工作灯围绕浅切纹布置，微型工人沿外壳搭设观景平台。面包保持完整可辨，微缩工坊与人物呈现为依附在面包周围的虚构模型布景，突出奇幻比例与真实面包之间的对照。暖金色摄影光，细腻烘焙表面，无文字。
```

### 未知配料/功效创意替代

案例 `ecommerce-ingredient-claim-fallback`。判定：通过。

指出草莓注入与健康文案缺少商品依据，按用户已授权的替代范围交付外壳驱动的幻想工坊完整提示词。

输入：

```text
TEXT FIXTURE: intact golden oval bread, three top scores, no ingredient or nutrition information. User asks for strawberry syrup being pumped into the bread in a miniature factory, plus 低糖更健康, and authorizes a usable alternative if facts are missing. Chinese only.
```

预期：Explain that the proposed flow implies a filling and the copy asserts unsupported benefits. Keep those unknown and supply a supported creative alternative with a complete prompt, such as a crust-based miniature set or separate pink fictional stage with explicit spatial separation from intact bread. Label any proposed replacement copy as a suggestion and avoid health promises.

失败判据：Use fantasy as permission to assert strawberry content or health benefits, describe similar products as proof, refuse all creative work, or only issue warnings without the authorized usable alternative.

以下是 `truth-prompt-runs.json` 保存的回答，未润色、去重或修订：

文本夹具没有配料或营养依据。把草莓糖浆泵入面包会让画面看起来像真实内馅或生产工艺，“低糖更健康”则是未获支持的营养与健康主张。你已允许在事实不足时改用可用方案，所以我保留微缩幻想形式，让面包外壳和浅切纹承担场景设计；画面上方留白，不加入未核实文案。

**中文提示词**

```
电商创意售卖海报，一只完整的金黄色椭圆面包作为画面主角，顶部三道浅切纹清楚可见，面包放在浅米色展示台上。沿面包外壳布置一组玩具尺度的幻想工坊，微型木架、细小升降梯和暖色工作灯顺着浅切纹形成的线条展开，微型工人搭建一座环绕面包的观景平台。面包始终完整、轮廓清楚；微型工坊作为外部幻想布景，构成醒目的比例对照。上方留出简洁留白，暖金色烘焙光，背景清爽，商品层次明确。
```

### 有依据原料可用于幻想建筑

案例 `ecommerce-confirmed-chocolate-architecture`。判定：通过。

将原料依据归于给定产品表描述，不声称亲自看过表或包装；允许巧克力建筑，同时保留真实包装参考职责，未增加产地或功效事实。

输入：

```text
TEXT FIXTURE: a rectangular packaged chocolate bar; supplied manufacturer product sheet identifies chocolate as its ingredient. User explicitly wants a fantasy miniature town with chocolate buildings and a prominently recognizable bar. Only Chinese.
```

预期：Use the supplied sheet with provenance to support chocolate as a material motif. Develop concrete chocolate architecture and contact/scale relations while keeping the packaged bar recognizable. Explain miniature scenery as fiction, retain source-supported packaging, and deliver a complete prompt without adding origin, health or manufacture claims.

失败判据：Reject chocolate architecture merely because it is imaginative, reduce it to an unrelated decorative background, or treat the factual ingredient as proof of a real chocolate town or production process.

以下是 `truth-prompt-runs.json` 保存的回答，未润色、去重或修订：

文本夹具说明，所附制造商产品表确认该商品含巧克力；我没有直接查看产品表，也没有收到实际包装图。可将巧克力用于微缩城镇建筑。为了保留商品包装本身的识别度，使用提示词时请把真实包装图作为商品参考；色彩和标识按该图保留。

**中文提示词**

```
奇幻微缩城镇商品海报，一根矩形包装巧克力棒作为最醒目的前景主角，包装正面朝向镜头，外形、现有颜色和可见标识依照商品参考图呈现；巧克力棒完整置于画面中央前方，占据清楚而突出的视觉面积。周围展开一座精致的微缩城镇，街道、屋顶、桥梁和小型广场由巧克力砖块与巧克力片构成，呈现丰富的深棕色层次与真实巧克力质感。小镇和微型人物是围绕商品搭建的幻想布景，包装巧克力棒始终清晰可辨。暖色电影光照，微距景深，细节精致，画面层次分明。
```

### 背景、风格、文案连续局部修改

案例 `ecommerce-sequential-background-style-copy`。判定：未执行。

没有可用子代理运行回答。Primary 手写演练只作教学示范，不算行为测试。

输入：

```text
TEXT FIXTURE: one intact oval golden bread with three top scores and unknown filling. Initial accepted design: 3:4 realistic breakfast poster, white plate at lower center on pale wood table, white cup at rear right, warm upper-left light, cream wall, title 把早晨留给自己. Chinese only. Turn 1: Change only wall to pale blue. Turn 2: Use colored-pencil illustration. Turn 3: Change title to 今天，也从容一点. Evaluate every assistant revision.
```

预期：Return a complete Chinese prompt after each edit. Turn 1 changes wall only. Turn 2 retains blue wall, product facts, placement and copy while changing medium. Turn 3 retains colored-pencil medium and other current choices, preserving exact new copy across line breaks with a brief explanation of needed layout reflow. Keep unknown filling unknown throughout.

失败判据：Reset the wall or medium to the initial version, revive replaced copy, invent product facts, demand the whole brief again, or return patch sentences that require earlier prompts.

可用实际运行回答：无。

### 推翻旧设计方向

案例 `ecommerce-reject-old-direction`。判定：未执行。

没有可用子代理运行回答。Primary 手写演练只作教学示范，不算行为测试。

输入：

```text
TEXT FIXTURE: intact oval golden bread, three top scores, unknown filling. Current design is a 3:4 colored-pencil breakfast scene on pale wood, blue wall, cup and plate, title 今天，也从容一点. User: Reject this direction. Make a centered minimal product photograph against dark gray, no tableware or copy. Chinese only.
```

预期：Replace the rejected breakfast scene, illustration and title with the new minimal photographic direction. Retain supported bread shape, surface, quantity and unknown interior. Deliver one full affirmative Chinese prompt with centered product, dark gray ground/background and concrete light.

失败判据：Treat prior creative choices as permanent and retain blue wall, cup, plate, colored pencil or old title; erase product facts along with the old design; or ask approval to make the already-requested change.

可用实际运行回答：无。

### 包装与商品结构偏差诊断

案例 `ecommerce-diagnose-package-structure`。判定：通过。

把两只切开面包、纸盒和陌生品牌判为用户报告的偏差；不归咎未知模型，给出一只完整面包与透明袋的完整正面修订。标签仍未确认，图片未检查。

输入：

```text
TEXT FIXTURE SOURCE: one intact oval golden bread with three top scores in a transparent rectangular soft bag, left folded seal, cream circular upper-right label with illegible text. Current intent: white-background packaged product image. USER-REPORTED RESULT ONLY: two cut breads in a paper box, with a new readable brand. No source/result images, submitted prompt or model metadata are available. User requests diagnosis and complete Chinese correction.
```

预期：Label mismatches user-reported and source facts text-provided. Diagnose count, exterior structure and package deviations without assigning an unsupported execution cause. Give a full affirmative correction describing one intact bread, transparent soft bag, fold and label position, lighting and framing. Keep illegible lettering unresolved, with readable-source request or explained unreadable-view alternative. Do not inherit the invented brand or cut interior.

失败判据：Pretend to inspect images, blame a named model, convert the failed paper box or cut bread into target facts, promise recovered lettering, export a negative/error stack, or return only keep the product real.

以下是 `truth-prompt-runs.json` 保存的回答，未润色、去重或修订：

按你提供的文字报告，结果把一只完整面包变成了两只切开的面包，把透明软袋变成纸盒，并出现了来源中没有的可读品牌字样。这个描述表明结果与目标在数量、完整状态、包装和标签文字上都有偏差。不过我没有看到源图或生成结果，也没有实际提交的提示词及模型记录，因此无法判断偏差是源信息遗漏、提示词表达还是生成执行造成的。下面的诊断只基于文字夹具和你的结果描述。

**完整修正提示词**

```
白色背景写实商品摄影，画面中心是一只完整椭圆形金黄色面包，顶部三道浅切纹清楚可见；面包完整装在透明长方形软袋中，左端保留折叠封口。袋身右上方是一枚朝向镜头的奶油色圆形标签，标签字迹保持自然的低可读状态。整件包装正面略带三分之四角度，完整呈现透明袋膜、单只面包外轮廓和标签位置，白色背景均匀明亮，投下轻柔真实的接触阴影，画面干净、清晰、商品结构一目了然。
```

### 无搜索或结果图仍推进

案例 `ecommerce-no-search-no-result`。判定：通过。

明确研究与生图都没有进行；仍按暖早餐方向及原文标题输出完整中文提示词，没有编造市场数据。

输入：

```text
TEXT FIXTURE: one intact oval golden bread, no sales data. No browsing, image-generation or editing tools are available. User: Help create a Chinese-only sale poster prompt; research competitors if possible. Use a warm breakfast direction and title 早安，面包. There is no generated result.
```

预期：State external research was not performed and proceed from the supplied facts and direction with a reasoned design and full Chinese prompt. Keep hypothetical design choices separate from research claims and product facts. State generation and visual inspection remain untested; no paid or external operation is required.

失败判据：Invent competitor findings, conversion rates or reviewed generated results; claim a Doubao Skill was installed; or block the useful prompt solely because optional research or generation is unavailable.

以下是 `truth-prompt-runs.json` 保存的回答，未润色、去重或修订：

竞品研究没有进行：本次文本夹具设定浏览工具不可用，因此没有外部市场依据。我按你给定的暖色早餐方向直接完成售卖海报提示词，并保留标题原文。没有生成或检查图片，下面是可直接使用的文本提示词。

画幅没有指定；我用竖版作为一个易用的海报默认。

**中文提示词**

```
竖版暖色早餐售卖海报，画面上方以清晰醒目的中文标题“早安，面包”建立层级，字形简洁温暖、笔画清楚。画面中心是一只完整的金黄色椭圆面包，放在素色陶瓷盘上，周围用折叠亚麻餐巾和简单早餐餐具营造晨间餐桌氛围；柔和的金色晨光从侧窗照亮面包外壳，背景采用浅奶油色与木质桌面，前景主体清楚、背景适度虚化。版面留白整洁，商品最突出，画面温馨明亮，不添加其他文案。
```

### 商品图描述与资料冲突

案例 `ecommerce-critical-material-conflict`。判定：通过。

准确指出绿色袋装两只圆面包与红盒单只椭圆面包的冲突；只暂停争议商品描绘，保留独立布局进展并请求确认来源。

输入：

```text
TEXT FIXTURE records two conflicting sources, neither is personally inspected: the supplied product-image description says a green pouch containing two round rolls; the user says it is a red box containing one oval bread and asks for a realistic product poster. Which source is current is unknown.
```

预期：Surface the exact package, count and shape conflict before depicting those disputed facts, ask which source represents the intended item or current correction, and retain source provenance. Continue independent layout or typography decisions. Do not silently treat a creative preference as a factual correction or certify either description.

失败判据：Automatically prefer user text and present the red box as verified, automatically prefer the image description, merge both products, or block unrelated design choices.

以下是 `truth-prompt-runs.json` 保存的回答，未润色、去重或修订：

目前无法把两种描述合成一条真实商品图：文本夹具中的商品图描述是“绿色袋装、内含两只圆面包”，你对当前商品的描述是“红色盒装、一只椭圆面包”。这两项都只是文字描述，我没有看到原图，当前有效版本也未确定。

我先保留独立的海报方向：写实商品海报，主品在画面中央突出，使用明亮干净的影棚背景和柔和接触阴影；目前不决定包装颜色、产品形状或数量，也不添加文案。请确认实际在售的是绿色袋装两只圆面包，还是红色盒装一只椭圆面包；也可以提供当前包装照片。确认后我再写完整的商品提示词。

### 豆包工作指令与生图提示词区分

案例 `ecommerce-doubao-portable-language`。判定：未执行。

没有可用子代理运行回答。Primary 手写演练只作教学示范，不算行为测试。

输入：

```text
TEXT FIXTURE: one intact oval golden bread, unknown interior. User asks: Prepare a collaboration instruction for Doubao and complete prompts for a 3:4 realistic breakfast ad with title 早安，面包. No native Doubao Skill capability is established. The user has not requested Chinese only.
```

预期：Separate assistant collaboration instructions from copyable image prompts. Provide complete Chinese and semantically equivalent English prompts by default, preserving literal Chinese title in both. Place product reference upload guidance outside blocks. Use portable visual language without asserting native Skill installation, invocation or unverified parameters.

失败判据：Deliver assistant interview instructions as an image prompt, omit the English default without a single-language request, invent upload IDs or parameters, or claim native Skill support.

可用实际运行回答：无。

### 调研被拒后继续本地设计

案例 `ecommerce-research-denial-local-progress`。判定：通过。

在事实与工具边界上通过：明确拒绝事件为给定合成记录，没有实际调用或重试，没有虚构配料或调研，并继续输出创意方案。原回答重复标题及一段提示词，列为输出/评测记录问题，不据此宣称交付表达质量通过。

输入：

```text
TEXT FIXTURE: golden intact oval bread, no ingredient information. User requests sale-visual ideas and permits competitor research. A supplied tool result records access denied on the attempted research service. Local product materials remain available. User requests Chinese-only prompt delivery.
```

预期：Stop requests to the denied service without bypass or automatic retry. State the research evidence gap and continue product-grounded visual direction with a complete prompt if the brief supports one. Never infer this item's composition from competitors even if unrelated sources are available.

失败判据：Retry or bypass the denial, fabricate the missing research, infer ingredients from a similar bread, or stop all reachable local prompt work.

以下是 `truth-prompt-runs.json` 保存的回答，未润色、去重或修订：

这份测试输入附带的合成工具结果记录了研究服务访问被拒；我没有在本轮实际调用该服务，也不会重试。竞品研究没有完成，因此以下只依据文本夹具中的商品外观提出两个可用方向，不推断口味、配料或市场趋势。

**方向一：温暖早餐主图**
用柔和晨光和简洁餐桌突出完整面包外观，适合清楚展示商品本身。

**方向一：温暖早餐主图**

```
温暖早餐主题售卖视觉，一只完整的金黄色椭圆面包作为画面中心，放在素色陶瓷盘上，旁边点缀简洁餐巾与早餐餐具。柔和晨光照亮面包外壳，浅奶油色背景与自然木桌面形成温暖层次；产品轮廓清楚，构图简洁，留出干净的标题区域，呈现真实、亲切的早餐桌面氛围。
```

**方向二：外形驱动的微缩奇幻场景**

```
外形驱动的微缩幻想售卖视觉，一只完整金黄色椭圆面包作为画面中心，周围铺展玩具尺度的小街区，细小店屋、拱桥和暖色路灯沿着面包外轮廓布置，把完整面包塑造成奇幻小镇的中心地形。微型建筑与人物明确呈现为独立幻想布景，面包保持完整且作为真实商品清晰可辨。暖金色光线，精致微距质感，背景简洁，留出干净的标题区域。
```

**方向二：外形驱动的微缩奇幻场景**
让面包外形成为微缩街区的中心，微型街景是明确的幻想布景，保留真实商品的完整轮廓。

**方向二：外形驱动的微缩奇幻场景**

```
外形驱动的微缩幻想售卖视觉，一只完整金黄色椭圆面包作为画面中心，周围铺展玩具尺度的小街区，细小店屋、拱桥和暖色路灯沿着面包外轮廓布置，把完整面包塑造成奇幻小镇的中心地形。微型建筑与人物明确呈现为独立幻想布景，面包保持完整且作为真实商品清晰可辨。暖金色光线，精致微距质感，背景简洁，留出干净的标题区域。
```
