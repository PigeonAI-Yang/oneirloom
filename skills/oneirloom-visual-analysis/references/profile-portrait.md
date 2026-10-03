# Portrait reconstruction profile

人像反推的必查维度清单，补全 [reconstruction workflow](reconstruction-workflow.md) 第 2 步的 inventory。人像反推必须完成本清单的全部行，再进入第 3 步选锚点；每行同样需要“可观察关系 + 与结果对比的标准”。比例数值一律从源图量取，本清单只规定要查什么、怎么写成可检验的关系。

检查顺序：先查画框取景（workflow 表格 Frame and scale 行），再按本清单由外到内推进——出彩点 → 比例骨架 → 透视修正 → 姿态关节 → 面部身份 → 服装影响；光色与环境交回 workflow 对应行和 `oneirloom-color-light`。

## 出彩点（第一位，先于一切拆解）

动笔前先回答两个问题：这张人像图出彩的点在哪里？如果是性感，性感的部位是哪里？

- 从源图找出 1–2 个让这张图成立的视觉焦点：可能是裸露的部位、突出的身材特征、姿势张力、光影或表情。
- 焦点写成最高优先级的锚点，在提示词里有独立、明确的句子；位置、面积、裸露程度按源图写实，不因为含蓄而弱化。
- 每一轮修改都先检查焦点句还在不在、准不准；焦点丢失的版本不合格，其余锚点全中也不合格。

The focus check above is scoped to the current reference and user intent; it does not prescribe sensuality, a preferred body type, or an aesthetic hierarchy for every portrait. Structural preservation anchors from workflow step 3 remain required regardless of focal emphasis.

## Proportions（每张人像必查）

先定性再量数：用几个特征词回答“这是个什么身材”——大长腿、臀部饱满、胸部体量、细腰、窄肩、肌肉线条、脖颈修长等，源图有什么写什么，没有的不编造。每个特征词再用身体地标相对关系支撑，例如“大长腿：膝盖到脚踝的可见小腿约两个头高”。比例一律用身体部位当尺子（头长、脸宽、肩宽、头高）；画面占比式数字（如“头高占画面高度的八分之一”）实测对生成模型约束力弱，不写进提示词，只留在分析记录里。

从源图量取以下比例，写成与身体地标或画框的相对关系，不写孤立的形容词或凭印象的数字：

- **头身比**：头顶到下巴的头高，占可见身高（或可见身段）的份数，写成“头高约为可见身高的七分之一”一类的相对关系。裁切图只写可见段：半身像写“头高约占画面上部三分之一”这类画框关系，不推断被裁掉部分的身高比例。
- **头肩比**：肩峰全宽相对头宽的倍数；同时记录肩线斜度（左右肩的高低差）。
- **躯干分段**：肩线—腰线—髋线三条线的高度位置与间距关系；腰线的可见高度（高腰／自然腰／低腰）。
- **四肢相对长度**：上臂与前臂相对躯干；大腿与小腿相对躯干。被服装遮蔽的分段边界未知不猜，改写外轮廓比例。
- **手足校验**：手长约等于脸长，脚长约等于头高。手足可见时用这两个关系校验表观尺寸，防止生成结果手过大或过小。
- **体型轮廓**：整体体型写成可见的宽度关系（如“肩宽腰窄的轮廓”“匀称”）。局部丰满遵守主技能 [person defaults](../../oneirloom/references/person-prompts.md) 的纪律：丰满词只锚定在该区域，不升级为全局体型词。

## Apparent proportions under perspective（透视下的表观比例）

- 区分真实比例与当前视角的表观比例；提示词写表观比例，因为要复现的是画面效果。
- 相机近距离、广角或低机位会放大近侧：记录近侧相对远侧的表观尺寸差，如近侧手比脸大、近侧腿明显长于远侧腿。
- 肢体朝向镜头时透视缩短：表观变短不等于真实短，写成“前臂朝向镜头透视缩短，表观只到肩高”这类可见关系。

## Pose and support（引用已有关卡）

- 躯干轴线与肩线的判定走 workflow 第 2 步的 torso-posture evidence gate；四肢关节链走 Main body and limbs 行。
- 重心与支撑：站／坐／倚靠，承重侧；坐姿时臀部与支撑面的接触点决定大腿的表观长度，先记接触点再写腿的可见长度。

- **Held objects and concealment**: apply the workflow's held-object check to visible props, including their own direction, grip, body landmarks, and covering span. A conventional prop pose must not replace the observed arrangement. Hidden contacts stay unknown.

## Face and gaze

- 面部朝向：正脸／四分之三侧／正侧，加下巴抬起或收低的程度。
- 视线：看镜头／看向画框内某处（写明看什么）／看向画外。
- 表情：优先写成可见的面部状态（嘴角、眉形、眼神），情绪词（如“浅笑”“沉静”）可作补充，但不可单独替代可见描述。
- 发际线、脸型轮廓与发型体积相对头部的比例。
- 五官的显著比例特征（如脸长相对脸宽、眼距）只有在构成这张脸的身份特征时才锚定为必查行，不逐项罗列。

## Garment and footwear effects

- Map each visible garment layer's coverage, openings, connectors, and overlap using the workflow's garment gate; retain source-specific construction alongside a confirmed category.
- Check hosiery and footwear independently at visible foot regions. Record exposed toes or instep and visible connecting strips only when supported; distinguish sheer coverage from openings. If feet or cuffs are hidden, leave their construction unknown.

- 高跟鞋或厚底鞋改变身高与小腿线条：写可见的线条变化，不推断鞋的隐含高度。
- 宽松或垂坠服装遮蔽真实分段时，边界未知不猜，写服装外轮廓与身体的相对比例（garment gate）。
- 皮肤质感与色调的判定交给 `oneirloom-color-light` 的 evidence checks。

## 交付前自查

进入第 3 步前检查：比例行是否全部写成了相对关系而非孤立数字或形容词；裁切处是否标注了不可见；透视导致的表观差异是否与真实比例分开记录。
