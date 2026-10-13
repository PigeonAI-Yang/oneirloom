# 织梦师产品扩展契约

2026-10-12 当前方向纠正：人类明确“我们不卖课”“我们只卖SKILL”。只有 Skill 可作为商业产品；撤销会员资源包和课程销售、旧建议价格及其待批准问题。教程、案例、四篇免费文章与现有六课完整匿名阅读，已公开免费 Skill 包与 MIT 许可保持。旧订单、权益、许可和不可变内容历史保留。第 10、14、17、19 节已有 membership/course 数据形状仅保留历史兼容，不再授权新销售；当前实施行为与后续 Skill 接入范围以[第 20 节](#20-当前只卖-skill-范围)为准。未定义的新 Skill 商品合同不阻挡本次免费内容发布。

日期：2026-10-11。状态：Primary 已接受本次产品设计，实施与验收进行中；不代表功能已实现或上线。本文定义官网扩展的数据、权限和业务边界。[网站 SPEC §13](../../../sites/pigeonyang-site/SPEC.md#13-oneirloom-product-expansion) 采纳本契约作为扩展部分的唯一详细定义；网站既有媒体、发布、缓存和历史兼容契约继续有效。[PLAN §9](../../../sites/pigeonyang-site/PLAN.MD#9-product-expansion-sequence) 管理执行顺序，[TASK.MD](../../../sites/pigeonyang-site/TASK.MD) 是唯一执行账本。

## 1. 目标、范围与证据

完整目标是把织梦师扩展为可查找案例、理解方法、安装确定版本 Skill、准备自己的任务、记录复现与迭代，并提供账号留存、参考资料与免费学习；商业产品仅为确定版本 Skill 的平台。设计文档交付只完成其中的契约工作。

2026-10-11 用户明确修改范围：“修改方案,把投稿、讨论这部分沟通的,BBS性质的功能都删掉”。因此删除第三方或创作者投稿、申请入驻、作者社交主页、帖子、评论、讨论、论坛、关注、私信、社区举报申诉与治理、社区贡献积分和悬赏。它们不进入 P0/P1/P2，不预留空导航、占位表或接口。保留官方内容编辑与审核、事实性作者署名、私人任务评审、账号收藏、课程进度和交易售后。已有匿名点赞与分享按网站 SPEC §7.5 保留；本次不把它扩展为社交关系。

当前产品方案以用户本次范围修订后的[修订稿](织梦师产品扩展方案_修订.docx)为准，用以定义本次用户修订后保留的计划范围；它描述产品需求，不是网站内容素材。原始[织梦师产品扩展方案与VSC功能对照.docx](织梦师产品扩展方案与VSC功能对照.docx)保持字节不变，仅作为历史研究来源。已接受的详细实施契约与网站 SPEC §13 继续有效，本次方案修订不改动它们。公开页面、导航、示例和元数据只使用 Oneirloom / 织梦师品牌，不出现比较对象、研究报告或私有来源路径。

### 1.1 当前事实与保留项

| 本地证据 | 本次读取到的事实 | 契约影响 |
| --- | --- | --- |
| 网站 `wrangler.jsonc`、`worker/gallery-engagement.mjs` | `site` 主入口为点赞 Worker，已有 `ASSETS` 与 `GALLERY_LIKES`；先处理 `/api/gallery/*`，其他路由交静态资源 | 复用既有 Worker，不把 D1 原型写成生产服务 |
| 网站 `worker/index.mjs`、`worker/schema.sql`、`worker/wrangler.local.jsonc` | 隔离的本地 D1 提交原型，已设计作品 revision 和回执原子性 | 保留 OI-07 证据；扩展按实际受影响表检查，不重复证明全部旧路径 |
| 网站 `scripts/library.mjs`、`scripts/maintain.mjs` | 本地 SQLite 与现有维护 CLI | 官方内容继续由本地编辑，避免第二个可写内容源 |
| 网站 `scripts/public-release.mjs` | `content/public-ids.json` 选择公开作品，并显式构造字段 | 新关联不能使未选中作品、私有提示词或素材自动公开 |
| 网站 `scripts/skill-pages.mjs` | 仍有旧的 15 技能、0.1.1 候选包文案及 `main` 源码链接；共享 `content/oneirloom-project.json` 尚未生成 | OI-31 复用现有元数据同步器并消费统一产物，不能把源码数量当安装包数量 |
| [技能架构](architecture.md)、[视觉能力扩展](visual-capability-expansion-plan.md) | 0.3.0-preview 源码有 22 入口；冻结 v0.2.0-preview.1 包有 18 免费技能 | 分别展示 source 与 package；不能把 22 入口写成可安装新版本 |
| [安装说明](INSTALL.md)、[冻结包发布记录](releases/0.2.0-preview.1-publication.md) | 已有固定 URL、ZIP hash、清单、许可和有限安装发现证据；当前行为与图像质量未完整验收 | 使用既有包，不重新打包，也不声称稳定版或新会话行为通过 |

以上是本地源码和文档证据，不是本次生产探测。网站工作区的十处未知来源跟踪删除不恢复、不覆盖；实现者只修改当前实际存在并归自己负责的文件。

### 1.2 不变的技能架构

十个家族是可重叠的检索维度，不是十条强制流程。清楚的需求直接进入已选方法。未成形的场景沿用织梦，视觉方向未定才按需读取家族线索。Skill、reference、template、evidence 各有单一正文负责人；官网只保存 ID、版本、摘要及来源引用，不复制一套技能方法正文。共享交互契约继续负责完整提示词、事实和已确认选择的连续性。官网安装、简报和任务记录不意味着站内模型调用、生成队列、自动 Agent 或新增模型费用。

## 2. 分期、页面与覆盖

| 阶段 | 必须交付 | 对应页面与完成证据 |
| --- | --- | --- |
| P0 复现主流程 | 官方案例与风格目录、确定 SkillVersion、完整配方、清楚与模糊需求两条路径、安装及诊断文档、官方内容维护和发布检查 | `/cases/`、`/cases/:id/`、`/styles/`、`/styles/:id/`、`/skills/`、`/skills/:slug/`、`/start/`、`/learn/`；至少一个真实有权使用的案例能完成查找、安装、外部执行、记录评审与迭代 |
| P1 内容与留存 | 账号、收藏、私有简报及任务版本、安装记录、系统教程和免费教学路径、视频或运镜参考、免费参考和完整教学；Skill 销售范围与获取方式待具体产品决定 | `/account/`、`/references/`、`/learn/:id/`；两个账号隔离、免费完整教学与参考的真实获取条件通过 |
| P2 免费系统学习与 Skill 交易范围 | 官方六课目录与完整匿名正文；私人进度和历史访问记录保留。Skill 商业接入须确定真实对象与交付，不复用课程售卖名义 | `/courses/` 及精确课时全文入口；匿名六篇与原文一致，旧售卖入口撤销、新订单拒绝，历史记录保持 |
| 待决定、非必需 | 非社区积分、官方工作坊、官方数字商品商店 | 当前无导航、表、接口、价格或承诺。仅在经营方明确供给、获取方式及条款后另立任务，不阻塞 P0/P1/P2 |

12 个案例与 12 个风格只是原方案的种子建议，不能成为填数门槛。先用实际授权资料完成真实闭环，其余按供给逐条上线。只有成品图的历史作品继续叫作品，不能自动变成“已验证复现案例”。缺图、缺步骤或未运行的内容明确保留其证据状态，不伪造样例。

旧首页、`/works/:id/`、`#gallery/:id` 及六个中英文 Skill/GEO 页面保留。已有 work ID 是案例 ID，不按标题生成新身份。`/cases/:id/` 是案例工作流入口，既有 `/works/:id/` 保持 canonical；两个页面由同一公开投影生成，案例页 canonical 指向作品页，避免复制两套可索引正文。历史 hash 链接继续打开同一 ID。详情升级时保留原筛选、顺序与返回位置。新页面沿用已选织梦师视觉与中英文布局；英文缺少正文时只给真实可用的语言入口，不伪造译文。

`/admin/` 在 P1 提供获授权运营人员的发布状态、内容定位、账户角色及交易异常操作。官方案例、风格、配方的可写事实源仍为本地 CLI；后台提供其版本及维护入口说明，不从浏览器另建云端草稿编辑器。P0 的最小内容后台由现有 CLI 的内容、版本、许可和审核操作实现，用户仍可让外部 AI 调用。该取舍保留现有“无需人工填 JSON、无需日常登录后台”的能力。

## 3. 存储与唯一所有权

| 数据 | 可写负责人和位置 | 公开方式 |
| --- | --- | --- |
| 官方内容草稿、来源许可、审核、原图、精确生成证据 | 现有本地 SQLite 与仓库外媒体目录；同一个 `npm run maintain -- ...` | 白名单投影。P0 可沿用静态构建链；完整按项发布仍由旧 OI-06 至 OI-22 的相关任务完成 |
| 官网公开内容 | P0 的 `content/product-public.json` 是可重建投影，不是第二个编辑源；媒体仍经 `public-ids` 与既有导出 | 新 `scripts/product-content.mjs` 只从授权公开数据装配关联；`scripts/build.mjs` 消费其结果 |
| 源码和已发布包元数据 | 技能仓库 `docs/project-status.json`，由既有 `scripts/sync_project_metadata.py` 生成 | `--write --site-root` 生成网站 `content/oneirloom-project.json`；页面与产品关联消费它，禁止再手写第二份技能数量、版本和下载地址 |
| 未来公开 D1/R2 | 网站 SPEC §3、§5、§7 的公开库与压缩对象；独立绑定 `PUBLIC_DB`、`PUBLIC_MEDIA` | 切换时由 OI-19/OI-21 更新实际名称与操作规则；不把原型 `DB` 静默当作生产绑定 |
| 用户、会话、收藏、Brief、任务修订、订单、权益、进度、运营审计 | 新独立 D1 绑定 `ACCOUNT_DB`，由既有 `site` Worker 的私有路由写入 | 只走服务端鉴权 API；不参与静态构建、公开搜索、sitemap 或公共 D1 导出 |
| 会员与课程受限正文、授权下载副本 | 官方本地事实源；发布为 `ACCOUNT_DB` 的受限文本，以及独立私有桶 `MEMBER_MEDIA` 的必要压缩副本 | 每次由 Worker 查权益后返回；不进 `dist` 或 `ASSETS`，不使用公开媒体缓存 |
| 用户商品原图、原始元数据、VI、完整私有提示词 | 用户自己的本地文件与外部 Skill 环境 | 本轮不上传云端。P0 简报导出与 P1 任务只保存显式提交的文本事实和不含路径的材料别名 |

本次新增私有账号库是明确的产品扩展，不能破坏原“公开 D1 只存公开投影”的约束。会员正文也有独立访问级别，付费可读不等于公共可读。没有公开资产引用能够指向私有任务或会员桶。私有响应全部 `Cache-Control: no-store`，不进入 Cache API；公开缓存继续遵守原 SPEC。

上述绑定可先在隔离的本地 Wrangler 配置准备，无真实 cloud ID、secret 或 paid service。生产 `wrangler.jsonc` 只在批准实际绑定与部署时改变。入口仍为 `worker/gallery-engagement.mjs`，增加清晰的产品路由分派，保留 `GalleryLikes` 导出和 migration。新账户路由及受限资源路径在启用时加入 `run_worker_first`，不能让 `ASSETS` 先返回受限正文。原 D1 原型继续隔离。

## 4. 内容关系与公开投影

新对象使用稳定 ID、正整数 `revision`、UTC 时间、明确 `locale` 和 `schemaVersion: 1`。hash 使用小写 SHA-256。公开函数逐字段构造对象，拒绝未知输入；不存在通过对象展开带出私有字段的路径。

| 对象 | 必须字段与关系 | 约束 |
| --- | --- | --- |
| Case | `id=workId, revision, goalIds, productCategoryIds, channelIds, styleIds, recipeVersionIds, assetIds, authorCreditId, evidenceStatus` | 既有 work 必须在 `public-ids.json`；关系不能提升可见性。前后图分别有来源与公开授权 |
| Style | `id, revision, familyIds, name, visibleMechanism, suitableSubjects, limits, variables, failureCorrections, methodRefs, exampleCaseIds` | 家族与媒介、用途、商品类别、模型分别存储；可关联多家族。方法正文链接唯一 owner；真实样例与未实测指导分开 |
| RecipeVersion | `id, recipeId, revision, caseId, requiredInputs, confirmedFacts, allowedVariables, steps, outputChecks, corrections, skillVersionIds, evidenceRefs` | 已发布版本不可改。步骤变更产生新版本；旧案例继续指旧版。产品事实与表现建议分栏 |
| Skill | `id=slug, purpose, ownerSourcePath, versionIds` | 页面摘要来自实际技能元数据；不制造另一个执行路由器 |
| SkillVersion | `id, skillId, version, packageId, entryPath, compatibility, evidenceRefs, channel, lifecycle` | 指向一个不可变包中的确定入口；`channel=preview/stable` 与验证证据独立，不因包可下载变 stable |
| Package | `id, version, filename, downloadUrl, sha256, manifestSha256, skillIds, sourceFingerprint, licenseRefs, publishedAt` | 文件及 hash 不可变；一个包可含多个 SkillVersion。只有已发布包有可用下载动作 |
| Asset | `id, revision, kind, derivativeHash, mediaRef, authorCreditId, licenseRecordId, visibility, alt, availability` | 来源许可只维护一份；反向引用索引定位影响页面。原图 hash、私有路径和证明文件不进入投影 |
| LicenseRecord | `id, author, sourceUrl, acquiredAt, licenseName, licenseVersion, permittedUses, requiredCredit, evidenceRef, status` | 私有依据保留。公开仅投影获准的署名、许可和用途。unknown 不授权复制或分发 |
| TaxonomyTerm | `id, dimension, parentId, aliases, labels, sortOrder, enabled` | 维度为 family/medium/use/product/channel/model，父项只能同维度，禁用不改变历史 ID |
| ArticleVersion | `id, articleId, revision, title, body, relatedCaseIds, skillVersionIds, accessPolicy, evidenceRefs` | 安装教程固定版本；免费正文与会员正文分别导出 |
| AuthorCredit | `id, displayName, approvedLink, attributionBasis` | 事实署名，与登录 User 无隐式绑定；没有作者主页、关注、申请或投稿能力 |

`evidenceStatus` 使用 `guidance_only / historical_example / text_checked / result_inspected / reproduction_verified`，每条记录附实际证据 ID、输入版本及范围。状态不由文件夹存在、下载、用户点击完成或课程付费推导。旧技能的 source-guided 文字练习不能给新官网案例盖“复现通过”。

公开关联只包含当前访问级别可见的摘要。会员内容可有单独授权的公开预告，预告不是从全文自动截取。免费入口不得依赖会员正文才能完成既有免费使用。详情可显示受限内容标题和获取条件，但索引、HTML 源码、预加载数据、source map、图片元数据均不得包含受限正文。

### 4.1 关系更新与查询

本地表以关联 ID 和目标版本维护反向索引，不在每个页面复制素材许可正文。新增 SkillVersion 只增加版本，不重写旧 Case；兼容失效则新增状态记录，详情显示事实性提醒和可用替代版本。Recipe 切换必须是显式编辑。

删除已被引用的 SkillVersion、RecipeVersion 或 Asset 记录失败，改为 retired/unavailable 状态，保留历史。素材许可失效时按反向引用停用受影响公开页面或移除该素材并发布新版本，不扫描无关原图。一次发布必须包含已存在或同批发布的所有可见依赖，不留下断链。

P0 从已批准的有限公开投影组合筛选，沿用现有静态规模，不称服务端分页或已满足万图库增量目标。动态库切换后扩展既有 `/api/v1/works` 查询为 `family,use,product,channel,medium` 的精确交集，仍遵守既有短词搜索、游标、24/100 项、窗口 96 卡和无 N+1 约束。P0 不额外实现向量推荐。

## 5. 确定版本安装

首个可安装 Package 是 `oneirloom@0.2.0-preview.1`，包含冻结的 18 个免费 Skill。ZIP SHA-256 为 `38abe37cfa430f4876fb573f94e7d17d3344681513d9c3c77a29781ce24bbb4b`，manifest SHA-256 为 `d9f9384c8111da20cb4a52ca401826b4a8ac3f91e0e5834b06d664ce03d1ebd4`。数值来源为本地发布记录，实施时对既有包按 hash 核对；本设计未重新下载或生成包。

技能版本 ID 采用 `skill:<slug>@0.2.0-preview.1`，`packageId` 指向同一个集合包。先用现有 `scripts/sync_project_metadata.py --write --site-root J:/PigeonYang/sites/pigeonyang-site` 生成网站共享元数据，再让 `scripts/skill-pages.mjs` 消费；无需创建新同步器。Package 的版本、数量、固定 download/checksum/release URL 来自该产物，哈希按已有发布记录补齐并检查，不能从源码 latest 推断。包内 `skillIds` 来自该冻结包的 `SOURCE-MANIFEST.json` 及对应安装记录；共享 JSON 的 `skills[]` 描述当前源码，不能直接当作已发布包清单。页面、下载文件名、校验值、安装步骤和变更记录由同一 Package 数据生成。支持环境只写已记录范围。新源码 `0.3.0-preview` 可独立展示开发状态及 22 个入口，但无对应 Package 时没有伪造下载按钮或安装命令。

安装页提供既有固定 release URL，显示 SHA-256 核对命令、完整清单、项目级 `.agents/skills/` 的复制步骤、共享资源闭包以及按原清单备份恢复方法。任何“安装”或“一键复制”动作都不能改成 `main` 下载、自动源码 ZIP、单独复制一个依赖不闭合的目录，或覆盖用户已有未知修改。默认获取整个已冻结集合包，单 Skill 页面只定位包内入口。

`InstallationRecord` 保存 `userId, packageId, packageHash, selectedSkillIds, environmentLabel, recordedAt, verificationState, evidenceNote`。下载是 `downloaded`，用户自报安装是 `user_reported`，真实宿主发现及新会话读取才可分别记 `discovered/read_verified`；网页不能自行检测本机安装成功。P0 可导出本地安装记录，P1 登录后显式保存。

保留 MIT 免费入口及第三方许可说明。新增会员不能拦住旧 18 个技能或把此前的免费授权追溯改为收费。旧 0.1.1 私有水印包不作为公开回退包重新分发。

## 6. Brief 与私有任务

### 6.1 P0 引导和本地交接

`/start/` 有“我知道要做什么”和“帮我确定方向”。前者可从 Case 预填公开方法引用并直接编辑目标、渠道和已知事实，不要求完成家族问卷。后者只收集会改变结果的缺口，生成带未知项的简报，再由外部 Skill 完成研究和少量方向比较；静态网站不伪装模型推理或自动生成创意。

P0 表单数据仅在当前页面内存，用户主动导出 UTF-8 JSON 或 Markdown 后交给自己的 Skill。不把商品事实塞进 URL、分析事件、localStorage 或构建文件。刷新前可提示保存；没有账号时不声称跨设备恢复。文件材料使用用户自定别名，网站不记录绝对路径或上传原图。

`BriefRevision` 字段为 `briefId, revision, goal, channels, productFacts[], unknowns[], constraints[], creativeChoices[], sourceAliases[], caseId?, recipeVersionId?, skillVersionIds[], confirmedBy, confirmedAt`。每条事实有来源别名及 `unknown/provided/confirmed` 状态。Case 的样例事实不能预填成用户商品事实。用户确认后新修改创建下一版，不改旧版证据。

### 6.2 P1 账号保存与外部执行记录

`Task` 含 `id, ownerUserId, currentRevision, status, createdAt, updatedAt`。`TaskRevision` 指向 BriefRevision、确定 RecipeVersion 与 SkillVersion，保留 `parentRevision`、本轮改动范围、用户确认、外部执行记录和评审。操作均提交 `expectedRevision` 与 `idempotencyKey`；同键同内容返回原结果，异内容冲突。旧 revision 返回 409，不静默合并已确认事实。

任务状态为 `needs_material → needs_confirmation → ready → external_execution → review → completed/iterate`。清楚且材料足够的需求可直接 ready；可修正地跳过不需要的引导状态。`external_execution` 只表示用户在外部执行或手动记录，不表示网站已派发工具。`iterate` 创建下一修订并只改变本轮指定范围。`completed` 是任务拥有者的记录，不自动提升公开案例的复现证据。

结果检查逐项记录颜色、形状、结构、包装、文字和标识的 `pass/fail/unknown/not_applicable` 与说明；未知不自动通过。保存结果别名和用户输入的摘要即可，不要求上传原图。任务没有公开开关、分享链接、投稿按钮或评论。转成官方案例不是隐含功能，必须另有素材范围和字段授权，经官方发布路径另建内容。

## 7. 身份、权限与私有 API

### 7.1 选定身份机制

采用标准 OIDC 授权码 + PKCE，由 Worker 完成回调校验和本地会话建立；首个实现适配 Google OIDC，实际 client 注册、登录可达性和账号条件仍须经营方确认并获授权接入。本地使用仅存在于测试配置的签名身份 fixture 验证流程，不在生产暴露模拟登录。复用现有 `jose`，不增加密码库或自建邮件验证服务。

User 主键独立生成；Identity 以 `(issuer, subject)` 唯一绑定 User，不用 email 当主键，不按相同 email 自动合并账号。验证 issuer、audience、签名、nonce、state、PKCE 和固定回调白名单。会话使用高熵随机 opaque token，D1 只存 token hash、userId、expiry 和 revokedAt；Cookie 使用 HttpOnly、Secure、SameSite=Lax、Path=/。登录后轮换 token，退出撤销服务端会话。私有写入校验同源 Origin 与 CSRF token。

User 最小保存 `id, state, createdAt`；私有 Profile 保存用户自选显示名和语言，不创建公开主页。StaffRole 以 `(userId, role)` 唯一存储，带授予者、理由和时间。第一个生产管理员通过获授权的本地管理操作绑定指定 issuer+subject，不能采用“首个登录者自动成为管理员”或按客户端 email 分配。后续角色变更必须有现有权限管理员的有效会话。测试管理员仅存在本地 fixture。

### 7.2 操作角色与内容权益分开

| 主体 | 允许操作 | 不获得的权限 |
| --- | --- | --- |
| 访客 | 公开浏览、免费 Skill、P0 本地简报、原有匿名点赞分享 | 账户保存、受限正文、运营操作 |
| 已登录用户 | 自己的收藏、安装记录、简报、任务、进度、订单和权益 | 其他用户数据、发布、改变角色 |
| 内容运营者 | 官方本地维护及公开状态核验；Web 仅显示职责范围内记录 | 默认读取用户 Brief、订单支付资料或原图 |
| 权限管理员 | 明确分配 staff role，撤销会话，记录原因 | 默认读取私有任务正文；角色不自动带会员或课程权益 |
| 交易运营者 | 查询必要订单信息、处理退款或人工权益补正并留审计 | 修改商品价格历史、读取任务或自动公开内容 |

私有任务的工作人员读取只通过用户对特定对象、指定人员、用途和截止时间的显式授权记录；默认不存在通用“管理员可看全部”接口。本轮不实现站内沟通或客服消息。售后利用经营方已公布的外部渠道，由用户提供必要订单号，不把工单系统混入产品范围。

每条私有查询由服务端会话得到 `userId`，SQL 同时限制对象 ID 和 ownerUserId；忽略客户端伪造 owner。对他人和不存在的对象统一 404。列表也按 owner 分页，limit 默认 24、最大 100；不可把全表读入 Worker 再过滤。账号的收藏唯一键为 `(userId, objectType, objectId)`，PUT/DELETE 幂等；撤下的内容只在本人的收藏显示不可用摘要，不泄露隐藏正文。

### 7.3 接口划分

| 路由 | 所有权与响应 |
| --- | --- |
| `/auth/login`、`/auth/callback`、`POST /auth/logout` | 身份适配与会话；无凭证进入前端 bundle |
| `GET /api/me` | 最小账号、当前权益摘要与 csrf token，no-store |
| `/api/me/favorites`、`/api/me/installations` | 本人有界列表及幂等变更 |
| `/api/me/briefs`、`/api/me/tasks` 及 `/:id/revisions` | 本人对象与版本门控；JSON 体上限 128 KiB，不接受原图或绝对路径 |
| `/api/me/orders`、`/api/me/entitlements`、`/api/me/progress` | 本人记录；金额及权益由服务端计算 |
| `GET /api/member/content/:id`、`GET /member-media/:id` | 每次检查可见性、有效权益和许可范围；拒绝时只给错误代码与正常获取入口 |
| `/api/admin/*` | 按职责校验 staff role，写操作记录 actor、reason、目标和变更前后值 |

私有路由不接受公开图库的匿名 visitor ID 作为身份，也不复用维护机器 Bearer 为用户 Cookie。公开内容发布凭证不能读账号库；交易 webhook 不能发布内容。缺少绑定时相关 API 返回明确 `SERVICE_UNAVAILABLE`，保留公开浏览，不能回退成匿名可写。生产构建不包含本地 fixture、用户材料或私有 canary。

## 8. 官方编辑、审核与许可

这部分是官方内容维护，不包含投稿或社区审核。`EditorialRevision` 属于官方 Case/Style/Article/Reference/Course；本地状态为 `draft → review_ready → approved → published → withdrawn`，审核退回为 `changes_requested` 并保留理由。一个经营者可承担编辑和检查，无新增强制双人审批。`EditorialReview` 记录实际 reviewer、revision/hash、来源许可、步骤证据、事实与文案检查结果；编辑后原批准不能套用新 hash。

发布复用维护 CLI 的计划、dry-run、apply、回执及明确发布授权；“审核通过”本身不授权 push 或部署。官方后台读取实际回执和已发布版本；不得把待审核草稿标成线上。P0 静态发布仍执行现行 runbook，动态切换后使用原 SPEC 的 complete snapshot、revision gate、幂等及匿名核验。

公开素材只用自制、明确授权或许可覆盖用途的内容。许可记录分别覆盖展示、派生、下载、商业使用和再分发；访问权不能扩大许可。许可不明时保留来源链接和说明，禁用该副本的发布或下载，其他有权内容可继续。商品材料与私有 VI 不因属于同一项目而变公开。版权变化触发受影响引用更新，不另建社区举报、申诉或审核队列。

## 9. 视频参考、教学路径与课程

`MotionReference` 包含 `id, revision, title, purpose, previewAssetId, inputFormat, outputFormat, modelCompatibility[], replaceableParameters, instructions, licenseRecordId, availability, checkedAt`。它描述运动或镜头参考，不宣称网站能生成视频。首版使用经营方已授权且已压缩的预览，不自动下载外站视频；模型兼容只记录实际证据。预览默认不自动播放，点击后加载，提供时长、文字说明和不可用状态。新视频预览设计预算为 30 秒、10 MiB 以内的常见 MP4/H.264，先针对实际供给验证；不为单个参考引入站内转码服务。历史图片预算保持不变。

`LearningPath` 是有顺序的 ArticleVersion 和 Case/SkillVersion 引用。P1 先完成安装、首个任务、商品保真、结果诊断四条学习内容，复用已经存在且可核对的文档；正文不足时明确待供给，不能用空课替代。

`Course` 与不可变 `LessonVersion` 继续组织免费系统学习。现有六课通过新 Course 修订 3、六个 LessonVersion @3 和 catalog@3，将 `isPreview=true` 的既有完整正文发布为公开全文；此字段沿用已有 whole-lesson public projection 机制，产品文案称“免费学习 / 阅读全文”，不截断正文或引导付费解锁。原正文、课名、旧版本、试看与许可保留，不为开放正文改写旧版。

`Progress` 的既有私人记录保持原精确引用；匿名阅读不要求账号或保存进度。历史订单若存在，仍按原快照与合法付款/退款事实处理；当前不销售课程或会员资源，旧状态机仅作兼容。


## 10. 商品、订单、权益与支付事件

本节保存历史 membership/course 合同与金融处理规则。当前不据此生成新订单或 checkout；Skill 商品尚未接入这一数据形状，见第 20 节。

### 10.1 权益是服务端查询结果

`OfferVersion` 不可变，字段为 `id, productKind, productId, currency, amountMinor, durationDays?, benefitSetVersionId, contentScope, updatePolicy, renewalMode, refundPolicyVersion, termsVersion, activeFrom, activeUntil`。`productKind=membership/course`。价格是币种最小单位整数；用户只提交 offerVersionId，服务端生成订单快照。下架 offer 只影响新订单，旧订单条款不变。

`Entitlement` 字段为 `id, userId, scopeType, scopeId, startsAt, endsAt?, status, sourceType, sourceId, ruleVersion, createdAt`。`sourceType=free/order/operator_adjustment`，各来源独立。免费规则在服务端公开内容规则中表达，不给每个访客插入权益行。会员 scope 指向确定 BenefitSetVersion，课程 scope 指向确定 courseId；会员只有明确包含该课程的 grant 才能访问。

访问算法先检查内容存在且允许提供，再检查 public/preview；否则要求有效账号，并存在匹配内容 scope、`status=active`、`startsAt <= now < endsAt` 的 grant。无 endsAt 表示该合同未设时间到期，不等于允许永久提供任何后来新增内容。多个有效来源取并集。撤销某订单只影响它产生的 grant；购买者另有合法来源时仍可访问。到期按请求时服务器时间判断，不依赖定时器及时修改状态。

### 10.2 订单与事件状态

`Order` 保存 `id, userId, offerVersionId, amountMinor, currency, termsSnapshotHash, status, provider, providerMode, providerCheckoutId, providerPaymentId, revision, createdAt`。`PaymentEvent` 以 `(provider, providerMode, eventId)` 唯一，保存 verified payload hash、必要交易事实、receivedAt、processingState、orderId 和处理结果；不保存卡号或完整无关客户资料。

| 事件或操作 | 订单结果 | 权益结果 |
| --- | --- | --- |
| 创建订单与 checkout | `created → pending` | 无权益；checkout 跳回成功页也不授权 |
| 已验证的成功付款事实，金额、币种、订单和 provider 对应 | `pending/failed/cancelled → paid`，晚到真实收款按事实记录 | 同一 order+benefit 唯一 grant；只授予一次 |
| 失败、取消、过期且无成功收款事实 | `failed/cancelled/expired` | 不授予；晚到失败事件不能覆盖已支付 |
| 申请退款 | `refund_pending` | 现有有效权益暂保持；不能把“已申请”当完成退款 |
| 确认全额退款 | `refunded` | 撤销该订单 grant；重复通知无追加效果 |
| 部分退款 | `partially_refunded` 并进入交易运营处理 | 首版没有自动折算天数；暂停该订单 grant，经营方按已批准条款明确恢复、缩短或撤销，留 operator_adjustment 记录 |
| 争议开始 | `disputed` | 暂停该订单 grant，不影响其他来源 |
| 争议撤销或商户胜诉 | 回到已确认付款/退款事实导出的状态 | 恢复剩余原时间段，不重置起止时间；已退款来源不复活 |
| 争议败诉或撤销收款 | `chargeback/reversed` | 撤销该订单 grant；晚到 paid 事件不得重新授权 |
| 到期、再次购买 | 原订单仍保留其财务状态；新购另建订单 | 到期访问失效；新订单增加确定的新时间段 |

续期首版采用主动购买、非自动续费。购买同一会员权益包时，新 grant 的起点为付款生效时刻与已有未撤销同包 grant 最晚结束时刻的较晚者，结束为起点加该 OfferVersion 的天数。时间窗在交易中一次确定。之后退款只撤销对应窗口，不重排其他已购窗口，不悄悄延长服务。不同权益包不自动折算或升级，初版只销售一个明确资源包。

### 10.3 支付处理与幂等

首个适配选 hosted checkout 的 Stripe 单次付款模式，本地只实现适配与 fixture。该选择不说明当前经营主体、地区、账号或币种符合开通条件。若经营方选微信支付直连，则另做同一支付契约的 provider adapter，不将两个供应商同时上线，也不以个人收款码截图自动授予权益。

`POST /api/orders` 创建本人的不可变金额订单；`POST /api/payments/checkout` 仅为该订单创建或读取原 checkout；`POST /api/payments/webhooks/:provider` 验证原始 body 的签名、时效和模式，再规范化事件。客户端参数和 redirect query 不能证明付款。提供者 secret 不进前端、Git 或日志。

收事件后先持久化唯一事件，状态 `received`。处理使用该订单和事件的当前记录；重复 eventId 相同 hash 返回原结果，异 hash 标冲突并拒绝处理。相同收款的不同事件仍靠 order+benefit 唯一约束防止重复授予。订单事实、grant、审计和 event `applied` 在同一 ACCOUNT_DB batch 事务提交，采用已有 OI-07 的 revision CHECK 机制适配新聚合。真实本地 D1 验证原子性后才依赖，不以先读后写替代并发门控。

支付提供者可能乱序通知。按已确认收款、累计退款与争议状态归约订单，不按 event 时间戳盲目覆盖。对无法从单个事件确定的状态先进行该 provider 的权威交易回读；结果不确定时保留 `received/needs_reconcile`，不新增 grant。退款事件先到时也记录其终止事实，后到 paid 不复活。网络失败保留原 eventId/请求幂等键供供应商重投或运营显式 reconcile；不得伪报已 applied。provider 401/403/429 或认证挑战停止相关在线操作并报告，不自动反复请求。

本地完成后分别检查成功、失败、双份相同事件、同付款不同事件、乱序成功与退款、并发续期、到期边界、全额退款、部分退款、争议恢复、其他 grant 不受影响。支付功能默认 disabled，未配置真实 provider、批准的价格条款和绑定时不显示可点击付款入口。

## 11. 经营方选择与 Skill 供给

商业方向只有 Skill。旧会员 29/199 与课程 99 的建议及批准问题已经撤销，不构成新方向的待办。

| 决策 | 当前具体范围 | 待经营方实际输入 |
| --- | --- | --- |
| Skill 对象 | 已交付 `oneirloom@0.3.0-preview.1` 22 项固定集合仍免费、MIT；自愿购买同版文件或新增真正 Skill 版本是审阅选项 | 选择真实对象及确切版本/文件/hash，不能把教程/课程/案例重新包装收费 |
| 售价与条款 | 没有批准的 Skill 售价或 Offer | 实际币种、金额、税费展示、生效时间、经营主体、交易与退款文本 |
| 许可与更新 | 现有免费 MIT 权利不追溯缩减；新产品不自动含未来更新 | 确切使用权、署名、修改/再分发范围、是否包含以后哪些版本及期限 |
| 支付供应商 | 保留微信普通直连 Native 与支付宝网站支付 `alipay.trade.page.pay` 适配器及合法历史事件处理；新订单/checkout 当前关闭 | 对应商户 API 权限、账户应用绑定、真实服务端字段；其启用只能服务确定的 Skill 产品 |
| 登录 | 保留 Google OIDC 适配；当前生产缺真实 client | 注册 client、域名/callback 与用户可达性 |
| 免费学习与案例 | 四篇文章、六课全文、案例和已公开免费 Skill 保留 | 不以经营输入未定阻挡已获授权的免费内容发布 |

真实对象、版本与交付边界、实际实现缺口和经营输入详见[Skill 商业接入范围](skill-commercial-scope-20261012.md)。本次不创建虚假商品、新枚举或伪造付款。新 Skill 商品数据合同由后续关键设计责任处理。

## 12. 定向验收与操作权限

| 验收 ID | 可观察结果 | 相关任务 |
| --- | --- | --- |
| PE-01 | Case/Style/Recipe/SkillVersion/Asset 双向定位，组合筛选、失效引用及空态正确；未授权对象无法被关联带出 | OI-29、OI-30 |
| PE-02 | 页面版本、包名、hash、清单一致；旧 18 包与新 22 源码分开；实际宿主安装和当前会话证据分别记录 | OI-31 |
| PE-03 | 清楚需求直接走，模糊需求导出可确认 Brief；未知事实不补造；局部迭代保留已有约束 | OI-32、OI-35 |
| PE-04 | 官方审核绑定准确 revision/hash；缺许可副本不能发布；public-ids、private prompt、VI 排除保持 | OI-33 |
| PE-05 | 两用户互换对象 ID、分页、导出、进度和订单均隔离；角色不绕过所有权；退出与过期会话失效 | OI-34、OI-35、OI-40 |
| PE-06 | 视频预览、兼容、许可、失效状态真实；教学路径回链准确，无空课程或虚构供给 | OI-36 |
| PE-07 | 免费、会员、课程、到期及多 grant 取并集正确；受限正文不在 dist、缓存、匿名响应或索引 | OI-37、OI-39 |
| PE-08 | 支付表中全部转换、乱序与并发定向样例通过，重复事件不重复授权，前端成功页不能授予 | OI-38 |
| PE-09 | 六课匿名完整阅读与原文一致；历史课文/授权/订单保留，课程与会员新销售关闭；私人进度保持原版引用 | OI-39 |
| PE-10 | 已交付入口在桌面、移动和键盘路径可操作；旧链接、六页、点赞分享、无 BBS 范围保持 | OI-30 至 OI-41 的实际受影响页面 |

本轮设计检查只验证引用、需求覆盖、状态语义和文档差异，不运行应用测试。实现后使用定向检查，不因新增能力自动要求重跑全套历史。完整测试、打包、release、commit、push、部署、生产绑定或 secret、付费开通、真实销售、公开材料各按当前明确授权执行；本设计均不提供这些批准。生产验收记录准确部署、真实域名与获授权业务回读，不用 local pass 或付款测试替代上线结果。

## 13. 设计变更记录

- 2026-10-11：以私有产品扩展方案、既有技能架构和实际站点源码定义产品关系、版本安装、账号隔离、官方编辑、会员及课程交易。P0 不等待旧增量库全部切换；P1 新私有库不污染公开投影。新工作使用 OI-28 至 OI-42，旧 OI-01 至 OI-27 状态和证据不改。
- 2026-10-11：按用户明确指令删除投稿、讨论及全部 BBS/社交沟通功能；事实作者署名和官方编辑检查保留。此范围变更优先于私有来源文档原 M06 投稿、M08 创作者申请、M09 社区、M11 贡献激励、AT09/AT10 社区部分及 AC10/AC11 的社区要求。课程、会员、收藏、私人任务与原有匿名点赞分享不因此删除。
- 2026-10-11：产品方案按用户本次范围修订，当前保留计划见[修订稿](织梦师产品扩展方案_修订.docx)；原始方案保持不变，仅作历史研究来源。

## 14. 受限发布与不可变内容范围

<a id="restricted-publication-and-immutable-content-scopes"></a>

### 内容权威与精确版本

现有私有产品版本库继续作为官方内容的唯一事实源，不新增第二个编辑器或旁路事实源。私有产品扩展 schema 升为 2。已有 v1 记录、原始字节、审核记录和关系仍然有效。公开投影继续使用 schema 1，字段白名单保持不变。

新增私有内容类型 `benefitSetVersion` 和 `offerVersion`。P2 使用 `course` kind 与 `lessonVersion`，并沿用同一内容权威。每个不可变版次使用 `revision=1` 和新 ID；`Course` 同一 ID 的后续 revision 保留旧版。已售内容范围不得重写。

所有受限引用都使用精确的 `ExactRef`：

```text
ExactRef = {kind, id, revision, payloadHash}
```

读取时必须核验引用所指的已存储 revision 与 hash，不能解析为当前 head。`ContentScope` 只包含精确引用：

```text
ContentScope = {entries:[{contentRef:ExactRef,actions:[read|download]}],courseRefs:[ExactRef]}
```

`entries` 和每个 `actions` 集合都必须无重复并按确定顺序排序。`scopeHash` 使用规范化 JSON 的 SHA-256。范围不支持 latest、通配符、标签、目录、嵌套范围或隐式课程展开。附件逐个引用。

`BenefitSetVersion` 在现有 envelope 上增加 `benefitSetId`、`contentScope` 和 `updatePolicy=fixed`。`OfferVersion` 保留第 10.1 节已有业务字段。其 `benefitSetVersionId` 必须引用一个精确的不可变版次，`contentScope` 必须等于该 `BenefitSetVersion` 的范围，且 `updatePolicy=fixed`。拒绝不支持的更新策略。

课程 Offer 的 `productId` 必须匹配其唯一的精确 `courseRef`。每个课程 Lesson 都必须属于该精确课程 revision。单独的 `courseRef` 不授予 Lesson 访问权。新增内容需要新的 `BenefitSet` 和 `Offer`。已付款的旧范围保持不变。

新的 `ArticleVersion` 使用 schema 2，保留全部现有字段，并增加 `licenseRefs` 和 `assetRefs`。它们是精确 `ExactRef` 数组，类型分别为 `licenseRecord` 和 `asset`。

`LessonVersion` 使用 schema 2。它包含原有 envelope，以及 `courseId`、`lessonId`、`title`、`body`、`assetRefs`、`licenseRefs`、`isPreview` 和 `evidenceRefs`。精确关系将 Lesson 绑定到固定课程 revision。

缺少受限发布许可证明的旧 Article v1 必须通过新建并正确审核的版次补齐，不得改写旧字节。附件使用已登记的引用；正文不得嵌入私有路径或对象键。新增精确关系按实际版本和 hash 解析，旧字符串 ID 关系保持原行为。

`BenefitSet`、`Offer`、`Lesson` 的正文和私有 `ExactRef` 不会自动进入公开投影。会员 Article 的 `publicPreview` 仍是单独编写的标题和摘要，不能是全文预览。`isPreview` 只适用于整篇 Lesson。

### 受限发布与回执

受限发布复用现有 maintain 产品操作系列的 plan、dry-run、apply 和 verify，不新增网页编辑器。`RestrictedReleasePlan` 使用 schema 1，字段如下：

```text
RestrictedReleasePlan = {
  schemaVersion: 1,
  operation: publish|withdraw|rights_update,
  operationId,
  environmentId,
  targetDatabaseId,
  expectedRevision,
  selection:[{ref,sourceBindingsHash,relationsHash,approvalEventId}],
  selectionHash,
  currentRightsRefs,
  resources:[{contentRef,projectionHash,media?:{sha256,byteLength,contentType,objectKey}}],
  scopeHashes,
  reason?
}
```

只准入精确且已批准的依赖闭包，以及已核验的当前许可。只有精确 hash 和目标回执都匹配时，才复用现有运行时依赖。规范化 manifest 的 SHA-256 是发布身份。

`ACCOUNT_DB` 中保存不可变的 `RestrictedContentVersion`、`BenefitSetVersion`、`BenefitContentRef`、`OfferVersion` 和 `GrantScopeBinding` 投影，以及 `RestrictedResourceState`、`RestrictedLicenseState`、单例 `RestrictedCatalogState` 和 `RestrictedPublicationReceipt`。这些表用于服务，不是内容编写权威。

正文保存在私有 D1，必要媒体只放在私有 `MEMBER_MEDIA`。媒体上传及 hash 回读必须先于 D1 可见状态提交。此流程不声称 D1 与媒体桶之间具有跨存储原子性。

一次 D1 batch 同时提交回执与 CAS、不可变投影、范围索引、当前状态和目录 revision。相同 `operationId` 与请求 hash 重放时返回原结果。相同 ID 携带不同 hash 时返回 409。结果不确定时使用同一个 key 对账。

回执状态为 `prepared`、`committed`、`verified` 或 `needs_reconcile`。提交后核验失败不能被误报为“未发布”，也不能被报为“已核验发布”。

现有 library 回执增加 `restricted_publish`、`restricted_withdraw` 和 `restricted_rights_update` 操作类型，不复用 `publication_items`。受限发布不改变 editorial 的 `approved` 状态。绑定环境的运行时回执只证明服务状态，不把全局公开导出标记为 `published`。

### 撤回与许可变化

撤回先通过 CAS 更新运行时精确资源状态，之后才可清理媒体。本地删除或生成 plan 不能证明内容已经撤回。运行时不可达时，状态为 `withdrawal_pending`。

本地许可记录变更必须通过显式 `rights_update` 操作和运行时回读，才对服务生效。恢复许可不会自动恢复已撤回内容。Offer 停售只影响新订单，保留现有范围和订单。因真实权利或安全原因撤回时，记录原因并单独处理客户补救，不得静默改写订单。

### 权益绑定与内容访问

`GrantScopeBinding` 是不可变记录，字段为 `entitlementId`、`benefitSetVersionId`、`scopeHash` 和可选的 `offerVersionId`。它与 grant 在同一事务创建。服务器从 `Order → Offer → Benefit` 推导绑定。运营调整只能选择明确批准的固定范围，并使用独立来源。

会员 `scopeId` 固定为精确的 `BenefitSetVersion.id`，不得使用逻辑 `benefitSetId`。课程 `scopeId` 为 course ID，且精确绑定限制可访问的已付款版次。只有 `courseRef` 不授予 Lesson 访问权。

请求必须指定精确内容版本。服务前先解析资源可用性和许可，再核验所属用户的 session 与 grants，并逐项核验每个精确 scope binding 及 action，最后执行纯权益判断。有效且在时间范围内的 grants 只能合并其各自授权的资源。

公开正文和整篇试看 Lesson 按各自实际发布政策开放。会员 Article 的摘要预览不能开放正文。媒体只在检查通过后串流返回。不得提供永久公开重定向、公开缓存、ETag，也不得泄漏私有对象键或正文。缺少 `MEMBER_MEDIA` 只阻断媒体。

所有绑定许可及其已同步的当前许可都必须允许实际请求用途。展示、阅读、派生、下载、商业使用和再分发是不同权限。会员资格不会创建许可权利。执行署名义务，但不得要求私有文本阅读或其他不涉及再分发的用途具备再分发许可。保留固定 Skill 包原有的下载许可要求。

### 本地实施顺序与定向检查

本地实施按以下顺序进行：

1. **A**：迁移现有 library、producer 和 CLI 到 schema 2，先备份，并保持旧记录及公开记录不变。
2. **B**：实现私有运行时投影、操作回执和本地 adapter，覆盖精确发布、CAS、对账与撤回检查。
3. **C**：实现真实内容 handler 与 grant binding，复用现有身份验证、纯权益判断和支付逻辑。

此顺序不授权配置云绑定、更换 provider、购买付费服务、运行全套测试、打包或发布。

定向检查覆盖以下结果：

- 旧资源包 A 的旧 grant 不能访问新增内容 B，即使新范围为 A+B。
- 旧课程的 Lesson v1 grant 不能访问 Lesson v2。
- 会员权益不会隐式包含课程。
- 整篇 Lesson 试看与 Article 摘要预览遵守不同规则。
- 只有展示权限的 grant 允许阅读，不允许下载。
- 撤销许可只影响绑定该许可的内容。
- 并发发布与撤回通过一次 CAS 竞争，不能同时提交为当前状态。
- 相同 key 重放返回原结果；不同 hash 冲突；响应丢失后可用原 key 恢复结果。
- 未批准选择、hash 错误或许可错误会原子失败。
- 匿名公开输出不含私有正文、私有 key、私有范围 manifest 或 canary。

2026-10-11：本节将已接受的 Astra 方案编码为产品契约。它不是已实现或已生产验收的结果。

### 14.1 精确记录形状与关系约束

本小节记录已接受的封闭字段、精确引用、范围规范化及 Unit A 定向检查。schema 2 记录使用以下 envelope，所有 schema 2 kind 均拒绝未列出的字段：

```text
E = {kind, schemaVersion:2, id, revision, locale, createdAt}
```

| kind | 完整封闭字段集合 |
| --- | --- |
| `articleVersion` | `E + articleId, title, body, relatedCaseIds, skillVersionIds, accessPolicy, evidenceRefs, licenseRefs, assetRefs` |
| `benefitSetVersion` | `E + benefitSetId, contentScope, updatePolicy` |
| `offerVersion` | `E + productKind, productId, currency, amountMinor, durationDays?, benefitSetVersionId, benefitSetVersionRef, contentScope, updatePolicy, renewalMode, refundPolicyVersion, termsVersion, activeFrom, activeUntil?` |
| `course` | `E + title, authorCreditId, authorCreditRef, summary, lessonIds, offerIds, accessPolicy, publicationStatus` |
| `lessonVersion` | `E + courseId, courseRef, lessonId, title, body, assetRefs, licenseRefs, isPreview, evidenceRefs` |

`licenseRefs` 与 `assetRefs` 是分别指向 `licenseRecord` 与 `asset` 的 `ExactRef` 数组；保留作者输入顺序，并要求目标 identity 唯一。`offerVersion.durationDays` 对 membership 必须存在且为正整数，对 course 可省略。若提供 `activeUntil`，它必须是晚于 `activeFrom` 的 UTC 时间；省略表示字段不存在，不等于 `null`。`productKind` 仅为 `membership|course`，`updatePolicy` 固定为 `fixed`，`renewalMode` 固定为 `manual`。

`accessPolicy` 沿用 `{audience:public|member,publicPreview}`；`member` 表示受限访问，不新增 course audience 或 payment reducer 行为。`publicationStatus` 沿用现有 editorial 状态词汇，只是内容声明，不证明已发布，也不能绕过真实 editorial 状态或环境回执。`Course.authorCreditRef` 为 `ExactRef<authorCredit>|null`：引用与 `authorCreditId` 同时为空，或两者 ID 相等。`courseRef` 必填且其 ID 等于 `courseId`；`benefitSetVersionRef` 必填且其 ID 等于 `benefitSetVersionId`。这些 exact refs 是来源记录 payload 的字段；`Offer` 的既有业务字符串 ID 及 payment reducer 保持不变。

`ArticleVersion`、`BenefitSetVersion`、`OfferVersion` 与 `LessonVersion` 不可原位更新，每个新版本使用新 ID 和 `revision=1`。`Course` 更新使用相同 ID 和递增 revision，并保留旧版。P2 kind 是 `course`，不是 `courseVersion`。`Course.lessonIds` 是有序的逻辑 `lessonId` 列表，不是 `LessonVersion` ID；每个 `LessonVersion.lessonId` 必须出现在其绑定的 `Course.lessonIds` 中。`Course.offerIds` 是原有字符串目录提示，不授权、不生成精确出边，也不要求先改 Course 才能建立 Offer。

精确关系只朝下列方向解析：`LessonVersion.courseRef → Course` revision、`OfferVersion.contentScope.courseRefs → Course` revision、`OfferVersion.benefitSetVersionRef → BenefitSetVersion`。course Offer 必须恰有一个 `courseRef`，其 ID 等于 `productId`；该 Offer 的所有 Lesson 引用必须绑定同一个完整 Course `ExactRef`。会员范围中的 Lesson entry 还必须在 `courseRefs` 中显式包含其 Course `ExactRef`。单独的 `courseRef` 不授予访问权；附件也不隐式纳入范围。`Course.lessonIds` 与 `offerIds` 不创建 Lesson 或 Offer 版本的精确反向引用，避免课程与课时 payload hash 循环；构建顺序为 Course、Lesson、BenefitSet、Offer，后续 Course head 不迁移旧绑定。

所有受限引用的封闭形状为：

```text
ExactRef = {kind, id, revision, payloadHash}
```

`payloadHash` 必须等于 `SHA256_UTF8(canonicalProductJson(target.record))`，并与 `product_versions.payload_hash` 及 `getProductVersion.hash` 一致。它散列完整目标 record，不散列单独正文、媒体、scope、bindings 或 projection hash；目标 record 不包含自己的 `payloadHash`。解析使用完整 `(kind,id,revision)`，可从数据库或同一 batch 读取；重算值、数据库存储值和引用值必须三方相等，且 `kind`、冗余 `id` 与目标一致。缺失或不匹配必须原子失败，禁止回退至当前 head。batch 中先写入所有版本，再写 exact edges；`sourceBindings` 保持现有封闭结构。读取、审核与发布时均重新核验 exact 字段、索引和目标 payload hash。

`ContentScope` 的封闭形状为 `entries:[{contentRef:ExactRef,actions:[read|download]}]` 与 `courseRefs:[ExactRef<course>]`。范围内只允许已登记的内容 kind；`entries` 禁止 `BenefitSetVersion`、`OfferVersion` 与 `Course` 容器。每个 `actions` 非空，且只按固定 `[read,download]` 顺序取子集。按 `(kind,id,revision,payloadHash)` 排序，其中字符串使用 code-unit 比较（不用 locale compare），revision 使用数值比较；`entries` 按 `contentRef` 排序，`courseRefs` 按 ref 排序。相同 `(kind,id,revision)` 即为重复，即使 `payloadHash` 不同也拒绝，且不合并 action。持久化输入必须已经排序；拒绝未排序输入，不在散列后静默重排。

唯一派生的 `scopeHash` 为 `SHA256(canonicalProductJson(contentScope))`；它不属于 `ContentScope` 或内容版本记录字段。`BenefitSetVersion` 与其 `OfferVersion` 的 `contentScope` 规范化字节必须完全相同。范围索引不是散列权威。运行时是否存在相应投影属于后续 Unit B 发布检查，不由 Unit A 伪造能力。

新增 exact relation descriptor 按以下来源字段写入既有 relation 表：

| 来源字段 | `name` | `ordinal` |
| --- | --- | --- |
| `licenseRefs[i]` | `licenseRefs` | `i` |
| `assetRefs[i]` | `assetRefs` | `i` |
| `courseRef` | `courseRef` | `0` |
| `authorCreditRef` | `authorCreditRef` | `0` |
| `benefitSetVersionRef` | `benefitSetVersionRef` | `0` |
| `contentScope.entries[i].contentRef` | `contentScope.entries` | `i` |
| `contentScope.courseRefs[i]` | `contentScope.courseRefs` | `i` |

持久化 relation 表仍只有原八列：`sourceKind, sourceId, sourceRevision, name, ordinal, targetKind, targetId, targetRevision`。内部 descriptor 可带 `targetRevision` 与 `targetPayloadHash`；校验后只写入上述原八列，不增加 hash 列。Hash 权威是来源 `ExactRef` 与目标 `payload_hash`，不能只依赖 relation index。新 exact 分支按完整三元组查询；若新 revision 已存在，不得用 entity-only `stagedByEntity` 替代。既有 `relatedCaseIds`、`skillVersionIds`、`licenseRecordId` 字符串关系继续走旧分支、保持当前冻结行为；不得推断为新 `ExactRef`，重复 put 不重新解析旧字符串关系。

私有 product schema 2 与公开投影 schema 1 并行。原有 11 种 kind 的 schema 1 校验、字段集合及 hash 行为保持不变；schema 2 下其余十种旧 kind 沿用原字段集合；schema 2 专属 kind 不得以 schema 1 写入。受限 `ArticleVersion` 使用 schema 2，绝不重写旧 v1 字节。公开 schema 1 的字段白名单保持不变：私有 kind 不参与自动选择，显式请求公开发布私有 kind 必须失败；Article v2 的私有 refs 不得进入公开 `relationRefs` 或依赖闭包。私有正文 canary、附件及许可引用均不得进入公开输出，既有公开 fixture 输出保持不变。

Unit A 只覆盖现有 `product-content`、library 与 `product-maintain`；`maintain` help 和定向检查为可选相关更新。实现时分离 private/public schema version 常量，补齐校验、排序、hash 与 exact relation 分支。迁移从 v1 到 v2 前要求经验证的备份，并在单一事务中更新 kinds、约束、schema marker 与 immutable guards；保留历史 payload、原始 sourceBindings 字符串、hash、relations 和 editorial 记录，不重新序列化旧记录。现有 `product-init` 保留显式 apply 边界及 report、backup、migration、dry-run 流程，不改写历史 payload；既有 put/get/relations/review 接口保持不变。此范围不包含 Worker、支付或 entitlement reducer、云绑定、媒体、运行时发布、真实销售或全套测试。

Unit A 的验收检查为：

- 必须增加可证明 v1 备份有效的检查；仅能验证 DDL 前状态的旧备份检查器不能证明此升级。v1→v2 可从备份恢复并保留原始字符串、hash、边关系、审核记录及旧公开 fixture。
- 私有 canary 不进入公开输出，公开 envelope 仍为 schema 1。
- 同一 batch 的 exact ref、显式旧 revision 和之后出现的新 head 均按完整 revision 解析。
- 缺失引用、错误 hash、kind/ID 不匹配会回滚。
- 四类不可变版本拒绝原位更新；追加 Course revision 不改变旧绑定。
- 未排序或重复范围、Offer 与 BenefitSet 范围不匹配、课程归属不匹配均拒绝。
- 使用真实 CLI 和临时数据库检查 report、备份、迁移、dry-run、apply、get 与 relations；运行 `verify-product-content`、`verify-product-maintain` 和新的 schema 2 定向检查，旧 fixture 继续按 v1 验证。

上述为已接受的设计与检查范围；本次仅记录契约，不表示 Unit A 已实现或这些检查已执行。

### 14.2 受限内容投影与精确发布

本小节定义受限运行时使用的内容投影、许可快照和媒体提交。它沿用第 14 节的私有产品版本库和第 14.1 节的 `ExactRef` 规则。受限投影不改变私有 schema 2，也不改变公开 schema 1。

`RestrictedContentProjection` 只允许以下封闭形状。`contentRef.kind` 决定 `data` 的唯一形状；拒绝额外字段。

~~~text
RestrictedContentProjection = {
	schemaVersion: 1,
	contentRef: ExactRef,
	locale,
	createdAt,
	boundLicenseRefs: ExactRef<licenseRecord>[],
	data: RestrictedProjectionData,
	media?: {sha256, byteLength, contentType, objectKey}
}

RestrictedProjectionData(contentRef.kind) =
	case articleVersion: {articleId, title, body, accessPolicy, assetRefs}
	case lessonVersion: {courseId, courseRef, lessonId, title, body, assetRefs, isPreview}
	case asset: {assetKind, derivativeHash, authorCreditRef, visibility, alt, availability}
	case licenseRecord: {author, licenseName, licenseVersion, permittedUses, requiredCredit, status}
	case authorCredit: {displayName, approvedLink}
	case course: {title, authorCreditRef, summary, lessonIds, accessPolicy, publicationStatus}
	case benefitSetVersion: {benefitSetId, contentScope, updatePolicy}
	case offerVersion: {
		productKind, productId, currency, amountMinor, durationDays?,
		benefitSetVersionId, benefitSetVersionRef, contentScope, updatePolicy,
		renewalMode, refundPolicyVersion, termsVersion, activeFrom, activeUntil?
	}
~~~

`offerVersion` 的数据包含第 14.1 节列出的全部业务字段，不含 envelope。`durationDays?` 与 `activeUntil?` 保留第 14.1 节定义的字段存在语义。`accessPolicy`、exact refs 和 `contentScope` 沿用第 14 节及第 14.1 节的闭合定义。正文来自私有 schema 2。来源字段、`locale` 与 `createdAt` 都按来源值复制，不规范化或改写。私有 schema 2 与公开 schema 1 的字段和 hash 语义不变。

`articleVersion` 与 `lessonVersion` 投影的 `boundLicenseRefs` 按来源 `licenseRefs` 的原顺序复制完整精确引用。`asset` 的旧 `licenseRecordId` 关系必须解析到既有八列 relation 表中的确切 revision，并核验目标 payload hash。该引用作为 `asset` 投影唯一的 `boundLicenseRefs` 项。`asset` 的 `authorCreditRef` 也按已存 relation 冻结到确切 revision；来源 `authorCreditId` 为空时使用 null。`course` 的 `authorCreditRef` 使用相同规则。以上关系不得解析当前 head。`licenseRecord`、`authorCredit`、`course`、`benefitSetVersion` 与 `offerVersion` 的 `boundLicenseRefs` 为空数组。

投影通过引用的 license 和 authorCredit 记录提供署名和许可信息。投影对象不得含 `sourceBindings`、`evidenceRefs`、审核 actor、`mediaRef` 或本地文件系统路径字段。只有 Asset 投影可以带 `media`，且 `media` 只能保存闭合形状列出的元数据。媒体 bytes 不进入 JSON。

投影 hash 按完整投影计算：

~~~text
projectionBytes = UTF8(canonicalProductJson(completeProjection))
projectionHash = lowercaseHex(SHA256(projectionBytes))
~~~

完整投影包含 `contentRef`、全部 `boundLicenseRefs` 与 `media` 元数据。它不包含执行时间、回执状态、catalog revision 或投影 hash 自身。系统保存规范化 bytes 与 hash。读取时必须核验 canonical bytes 完全相等，并重新计算 hash。已有不可变记录只有在 bytes 与 hash 都完全相同时才能复用；其他输入不得替换该行。`payloadHash` 始终散列完整私有 record，`scopeHash` 只散列 `contentScope`；两者都不能替代 `projectionHash`。

运行时只物化本小节列出的受限服务类型。其他已批准依赖只进入 `selection` 证明。若固定授权范围明确选择了不支持的资源，发布必须失败，不能静默丢弃该资源。固定 Skill 包沿用现有下载路径与许可检查。

### 14.2.1 提交形状与来源重验

提交请求只允许以下外层形状。媒体 bytes 单独作为本地非 JSON 输入提交：

~~~text
RestrictedReleaseSubmission = {
	plan: RestrictedReleasePlan,
	projections: RestrictedContentProjection[]
}

RestrictedReleaseMedia = {
	contentRef: ExactRef<asset>,
	bytes: Uint8Array
}
~~~

`plan.resources` 与 `projections` 一一对应。每项 resource 恰有一个投影；不得缺少或多出投影。两个数组都按既有 `(kind,id,revision,payloadHash)` tuple 排序。字符串按 code-unit 顺序比较，revision 按数值比较。拒绝重复、未排序、未知或缺失项。每个投影的完整 `contentRef` 必须等于对应 resource 的引用，重算后的 `projectionHash` 必须等于该 resource 中的值。

producer 从获准的本地 library 组装投影。`apply` 必须重新加载并验证来源，之后才能提交。调用者提交的投影不是内容权威。

对 selection 中的每个引用，验证器必须用显式 `kind`、`id` 与 `revision` 调用 `getProductVersion`。引用 hash、存储的 `payload_hash` 和对完整目标 record 重算的 hash 必须相同。`sourceBindingsHash` 必须用现有 canonical binding 函数重算。`relationsHash` 是按现有 library 顺序排列的八列关系行的 canonical product JSON SHA-256。

验证器通过 `listProductEditorialEvents` 查找匹配的 `approvalEventId`，并核对完整内容 identity、`snapshotSha256` 等于私有 payload hash、`relationBindingsSha256` 等于重算后的 `relationsHash`、`toStatus` 为 `approved`，且现有审核检查全部为 true。发布时还必须确认该精确版本当前的 editorial status 为 `approved` 或 `published`。较早的 approval 不得绕过之后对该版本的 withdrawal。

依赖闭包只使用来源 `ExactRef` 和冻结到目标 revision 的旧关系，不解析当前 head。显式当前许可快照与 selection 和 approval 一并核验。运行时只有在预期 `projectionHash` 匹配，且当前环境与目标 database 的回执匹配时，才能复用既有内容；仅凭资源 identity 相同不能复用。

`selectionHash` 与发布 manifest hash 使用既有 canonical product JSON：

~~~text
selectionHash = SHA256(canonicalProductJson(plan.selection))
manifestHash = SHA256(canonicalProductJson(plan))
~~~

`manifestHash` 直接覆盖完整 plan，其中包含 `schemaVersion: 1`，包括 plan 内明列的媒体元数据。计算时不增加 wrapper、不格式化 JSON、不增加独立 `mediaPath`，也不把 manifest hash 自身放入输入。

### 14.2.2 当前许可与实际用途

`currentRightsRefs` 是显式的当前许可快照：

~~~text
currentRightsRefs: ExactRef<licenseRecord>[]
~~~

数组按既有 `(kind,id,revision,payloadHash)` tuple 排序。字符串按 code-unit 顺序比较，revision 按数值比较。同一逻辑 license ID 即使绑定多个历史 revision，也最多出现一个当前引用。运营方必须明确选择当前 revision，不能按最大 revision 或当前 head 推断。selection 中保存完整 ExactRef。

Publish 为运行时依赖闭包中每个不同的绑定 license ID 指定一个当前引用。运行时按 license ID 将不可变的 `boundLicenseRefs` 映射到该显式当前引用。若运行时当前指针已存在，publish 必须匹配该指针；只有在指针不存在时，publish 才能用显式引用初始化。此后的许可指针变更只能使用 `rights_update`。

`rights_update.currentRightsRefs` 必须且只能包含本次改变的 license ID。未列 ID 的当前指针保持不变。Catalog CAS 与回执共同覆盖指针变化。本地许可 revision 或 head 变化不会自动改变运行时当前指针。

更新许可不会把 `withdrawn` 资源恢复为 `available`，也不会重新开放已撤回资源或改写范围。`rights_update` 必须能记录事实上的未知、过期或撤销许可，以便移除访问权。不能因为当前许可不再有效而拒绝撤权。

现有 `permittedUses` 继续只接受以下布尔权限，不增加 `read`：

~~~text
permittedUses = {
	display: boolean,
	derivative: boolean,
	download: boolean,
	commercial: boolean,
	redistribution: boolean
}

RequestedUse = {
	action: read|download,
	derivative: boolean,
	commercial: boolean,
	redistribution: boolean
}
~~~

`RequestedUse` 是内部请求事实，不是客户端 entitlement，也不增加许可 schema。操作根据实际操作和现有批准事实确定用途。读取对应 `display`，下载对应 `download`。每个值为 true 的用途 flag 都要求对应许可。所有绑定许可及已同步的当前许可都必须处于 `confirmed` 状态，并允许该用途。系统还必须履行 `requiredCredit`。

普通阅读不等于派生。读取私有正文不自动构成再分发。实际商业使用、派生、再分发与固定包下载继续使用原有含义。Unit B 核验实际提交的 publication 与固定范围用途。付费 Offer 为其中资源建立商业用途事实，但不授予未来用途。Unit C 对每次实际请求重新核验许可。缺少依据只阻止受影响的用途或条目，不触发全局 rights audit。

`isPreview`、受限发布回执和来源 `publicationStatus` 都不能单独授权匿名读取。审批、许可、匿名公开及受限发布回执仍是第 16.5 与 16.6 节所述的不同事实。

### 14.2.3 媒体可见性与操作边界

上传前必须对实际媒体 bytes 计算 SHA-256、长度和类型，并与 plan 中的媒体字段及支持的类型核对。媒体只能写入配置的私有 `MEMBER_MEDIA`。

在 D1 提交任何可见状态前，系统必须对同一对象执行 GET，并读取完整 bytes。读取结果的目标对象、bytes、类型、长度与 SHA-256 都必须匹配 plan。调用者提供的证明、上传回执、其他 bucket 中的对象或只有 metadata 的读取都不能替代这次验证。投影或媒体被篡改、对象不在正确 bucket，或 GET 验证失败时，D1 不得出现新的可见状态。

受限 projection 和媒体不得进入 `publication_items`、公开 exports 或 editorial publish。Withdraw 必须指向精确的已提交投影与历史 approval；即使当前 serving 权限已撤销，也必须允许移除访问权。删除流程不能要求当前许可仍为有效。

### 14.2.4 定向验收

以下检查是后续实现的定向验收，不是本次文档修改的执行结果：

- 为 `payloadHash`、`scopeHash`、`selectionHash`、`manifestHash` 与 `projectionHash` 使用独立固定向量。修改正文、许可或媒体后，核对各 hash 按其覆盖字段正确变化。
- 创建较新的 head 后，显式旧 revision 仍解析到旧记录。错误 approval、错误 bindings、依赖闭包缺项或冻结旧关系不匹配，都在提交前失败。
- 修改投影或媒体、使用错误 bucket、或让完整对象 GET 的任一校验失败时，D1 不产生新的可见状态。
- Publish 不能替换已有运行时当前许可指针。`rights_update` 只能改变点名的 license ID。恢复许可不能让已撤回资源重新可用。
- 只有 `display` 的许可允许 read、拒绝 download。私有文本 read 不自动要求 redistribution。commercial、derivative 与 redistribution 分别检查。
- 即使当前许可已过期或被撤销，也允许 withdraw 与撤权。保留已有的 CAS、幂等重放、对账、不可变范围和 public-canary 检查。

本小节记录已接受的设计。它不表示 Unit B 或 Unit C 已实现、这些检查已执行，或生产行为已经验证。

## 15. 员工权限、账户操作与审计（OI-40）

<a id="staff-management-and-audit"></a>

本节为 OI-40 定义员工侧的最小账户管理 API、角色权限、并发审计与幂等边界。它落实本契约第 1 节删除投稿、讨论及 BBS/社交沟通功能后的产品范围：不增加社区发帖、作者门户、支持私信或社区治理。官方案例、风格与配方的编辑事实源仍是第 3、8 节规定的本地 CLI；员工 API 不能成为云端草稿编辑器，也不提供虚假的内容或交易工具。

员工权限与会员、课程权益是两套独立授权。工作人员角色不授予任何会员或课程访问权；不得借员工身份绕过账户所有权或访问私人 Brief、Task、原始图片和其他私有正文。不得增加私有内容支持授权、受支持范围授权或其他新的 support-grant 系统。现有 <code>/api/me</code> 所有者 SQL 与响应契约保持不变；它仍提供现有会话的 CSRF token，员工 API 复用现有会话与同源 CSRF 检查。

### 15.1 角色与能力

复用 <code>ACCOUNT_DB</code> 现有 <code>StaffRole</code> 表，不使用 <code>UserRole</code>。表的既有列为 <code>userId</code>、<code>role</code>、<code>actorUserId</code>、<code>reason</code>、<code>createdAt</code>，并以 <code>(userId, role)</code> 唯一；管理角色时保留授予者、原因和原始授予时间。增加 <code>StaffRole(role, userId)</code> 索引供权限检查使用。未知的既有支持角色记录保留，但不授予能力，也不参与授权判断。

<code>RoleId</code> 只包含本节定义的三个已知角色，响应数组按本契约规定的顺序输出：

1. <code>content_operator</code>
2. <code>permission_admin</code>
3. <code>commerce_operator</code>

单个用户的有效能力是其已知角色所声明能力的并集；不支持通配符、继承、隐式角色或额外能力。<code>content_operator</code> 与 <code>commerce_operator</code> 当前只有员工自查范围，没有任何账户外能力；在真实内容或交易适配器存在前，不宣称已连接这些适配器，也不暴露占位工具。<code>permission_admin</code> 的能力数组按以下顺序固定：

1. <code>permissions.accounts.read</code>
2. <code>permissions.roles.write</code>
3. <code>permissions.sessions.revoke</code>
4. <code>permissions.audit.read</code>

上述角色和能力不产生会员或课程权益。角色变更会即时影响后续请求的授权判断，但不会自动撤销用户的全部会话。

### 15.2 私有 API 路由与错误

<code>/api/staff</code> 必须在 <code>ASSETS</code> 前由私有路由前缀接管；未知员工路径以 JSON <code>404</code> 结束，不得落入静态资源处理。<code>/api/admin</code> 继续拒绝访问，本节不为它创建别名或新入口。私有 API 响应统一发送 <code>Cache-Control: no-store</code>、<code>Pragma: no-cache</code>、<code>Vary: Cookie</code>；错误对象只使用 <code>{error: CODE}</code>。

| 方法与路径 | 查询 | 权限 | 请求与响应 |
| --- | --- | --- | --- |
| <code>GET /api/staff/me</code> | 无 | 已登录会话 | 返回 <code>{userId, roles: RoleId[], capabilities: Capability[]}</code>。已登录但无员工角色的普通账户返回空 <code>roles</code> 与空 <code>capabilities</code>。 |
| <code>GET /api/staff/accounts/:userId</code> | 无 | <code>permissions.accounts.read</code> | 返回 <code>{item: {userId, state, revision, roles: RoleAssignment[], sessions: {activeCount, asOf}}}</code>。 |
| <code>PUT /api/staff/accounts/:userId/roles/:role</code> | 无 | <code>permissions.roles.write</code> | 请求为 <code>Command</code>；返回 <code>{item: AuditItem}</code>。只授予路径中指定的一个角色。 |
| <code>DELETE /api/staff/accounts/:userId/roles/:role</code> | 无 | <code>permissions.roles.write</code> | 请求为 <code>Command</code>；返回 <code>{item: AuditItem}</code>。只撤销路径中指定的一个角色。 |
| <code>POST /api/staff/accounts/:userId/sessions/revoke</code> | 无 | <code>permissions.sessions.revoke</code> | 请求为 <code>Command</code>；返回 <code>{item: AuditItem}</code>。 |
| <code>GET /api/staff/accounts/:userId/audit</code> | 仅 <code>limit</code>、<code>cursor</code> | <code>permissions.audit.read</code> | 返回 <code>{items: AuditItem[], nextCursor}</code>。 |

不提供账户列表、电子邮件读取、搜索、账户状态变更或其他账户字段修改。已知路由先验证当前会话，再验证所需能力，随后才判断目标账户是否存在；无权访问者不能用目标是否存在来探测账户。错误状态固定为：未登录、过期或已撤销会话 <code>401</code>；缺少所需能力 <code>403 STAFF_FORBIDDEN</code>；无效方法 <code>405</code>；未知员工路径 <code>404</code>；缺少数据库或所需 schema <code>503</code>。<code>/api/me</code> 不加入员工字段、不改所有权查询。

写入继续使用现有流式 JSON 解析上限 <code>128 KiB</code>，要求 <code>application/json</code>，并使用 <code>currentSession</code> 与 <code>requireSameOriginCsrf</code>。写入请求只能包含其 schema 明确列出的字段；拒绝客户端附带的 actor、用户、scope、result 或时间字段。

### 15.3 标识、命令与记录形状

路径参数 <code>userId</code> 必须匹配 <code>^[A-Za-z0-9][A-Za-z0-9._:@-]{0,127}$</code>。<code>idempotencyKey</code> 必须匹配 <code>^[A-Za-z0-9._:-]{1,160}$</code>。<code>reason</code> 在去除首尾空白后长度为 1–1000，必须为单行且不得含控制字符。

<code>RoleAssignment</code> 的封闭形状是 <code>{role: RoleId, actorUserId: string, reason: string, createdAt: integer}</code>。<code>Command</code> 的封闭形状是 <code>{expectedRevision: nonnegative safe integer, idempotencyKey: string, reason: string}</code>。

<code>Command</code> 只接受所列字段。<code>expectedRevision</code> 是目标账户的管理修订，不是账户资料修订。员工审计项的封闭字段如下：

<code>AuditItem = {id: string, scope: "permissions", action: "role_grant" | "role_revoke" | "sessions_revoke", actorUserId: string, targetUserId: string, targetRole: RoleId | null, reason: string, expectedRevision: nonnegative integer, resultRevision: positive integer, before: object, after: object, createdAt: positive integer}</code>

角色操作的 <code>before</code> 与 <code>after</code> 都是 <code>{assignment: RoleAssignment | null}</code>。会话撤销的 <code>before</code> 是 <code>{activeCount}</code>；<code>after</code> 是 <code>{activeCount: 0, revokedCount, revokedAt}</code>，其中时间为正整数。会话数量只统计同一 <code>asOf</code> 时刻满足 <code>revokedAt IS NULL AND expiresAt &gt; asOf</code> 的记录。<code>User.state</code> 单独影响身份验证；它不改变上述会话计数定义。

### 15.4 操作回执、修订与原子性

在现有账户 schema 中新增不可变 <code>StaffOperation</code>。表仅有以下列：

| 列 | 约束 |
| --- | --- |
| <code>id TEXT</code> | 主键 |
| <code>actorUserId TEXT</code> | <code>User(id)</code> 外键 |
| <code>scope TEXT</code> | <code>CHECK scope = 'permissions'</code> |
| <code>idempotencyKey TEXT</code> | 非空 |
| <code>action TEXT</code> | <code>CHECK action IN ('role_grant', 'role_revoke', 'sessions_revoke')</code> |
| <code>targetUserId TEXT</code> | <code>User(id)</code> 外键 |
| <code>targetRole TEXT</code> | 角色操作为已知 <code>RoleId</code>；会话撤销为 <code>NULL</code> |
| <code>reason TEXT</code> | 非空 |
| <code>requestHash TEXT</code> | <code>CHECK</code> 为小写 64 位十六进制 |
| <code>expectedRevision INTEGER</code> | <code>CHECK expectedRevision &gt;= 0</code> |
| <code>actualRevision INTEGER</code> | <code>CHECK actualRevision = expectedRevision</code> |
| <code>resultRevision INTEGER</code> | <code>CHECK resultRevision = expectedRevision + 1</code> |
| <code>actorAuthorized INTEGER</code> | <code>CHECK = 1</code> |
| <code>lastAdminSafe INTEGER</code> | <code>CHECK = 1</code> |
| <code>beforeJson TEXT</code>、<code>afterJson TEXT</code> | JSON 有效且顶层为对象 |
| <code>responseStatus INTEGER</code> | <code>CHECK = 200</code> |
| <code>responseBody TEXT</code> | JSON 有效且顶层为对象 |
| <code>createdAt INTEGER</code> | <code>CHECK createdAt &gt; 0</code> |

表上有 <code>UNIQUE(actorUserId, scope, idempotencyKey)</code> 与 <code>UNIQUE(targetUserId, resultRevision)</code>。API 负责全部文本长度边界和安全整数校验。保留 <code>StaffOperation</code> 的所有记录；UPDATE、DELETE 必须由拒绝触发器阻止，且外键删除不得级联删除审计记录。增加 <code>(targetUserId, createdAt DESC, id DESC)</code> 索引，并保留新增的 <code>StaffRole(role, userId)</code> 索引。表中不存储 session token、token hash、CSRF token 或 CSRF hash。

目标管理修订号为该账户 <code>MAX(resultRevision)</code>，无操作记录时为 <code>0</code>；既有合法角色因此从修订 <code>0</code> 开始。每个成功的新命令恰好递增一次，包括业务状态不变的 no-op；幂等重放不递增。

写命令先完成会话、当前角色、Origin/CSRF 与请求体校验。规范化请求 hash 只基于 <code>{action, targetUserId, targetRole, expectedRevision, reason}</code>；不包含幂等键、token、hash 或时间。按 actor、scope、key 查到相同 hash 时返回已存的原始 status/body；同 key 不同 hash 返回 <code>409 IDEMPOTENCY_CONFLICT</code>。

一个 D1 batch 首先通过 <code>INSERT ... SELECT</code> 写入 <code>StaffOperation</code> 回执，并在同一事务快照中读取实际管理修订、操作前状态、当前会话 tokenHash、按服务端当前时间判断未撤销且未过期的会话，以及仍为 active 的用户和 <code>permission_admin</code> 授权。原始 session tokenHash 只作为查询参数，不写入任何表。<code>actorAuthorized</code> 的约束确保未授权操作无法提交；<code>lastAdminSafe</code> 也必须在该事务内成立。其后才执行角色或会话变更。回执、业务变更与其记录若任一失败，整个 batch 回滚，不留下半条回执或半个业务动作。before、after 和 response body 必须先由 SQL 按实际旧状态及确定性变更计算；提交后返回已保存的 response body。

<code>PUT</code> 对角色使用 <code>INSERT ... ON CONFLICT DO NOTHING</code>，冲突时保留原有授予者、原因与时间；<code>DELETE</code> 只删除精确路径指定的角色。即便授予已存在的角色或撤销不存在的角色，该新命令也写一条审计记录并推进修订。

会话撤销只针对目标账户在单一服务端 <code>asOf</code> 快照中实际处于 active 的那批 session 行，并以同一 <code>asOf</code> 计算撤销前数量和 <code>revokedAt</code>。该快照之后新建的登录不受本次命令影响。成功撤销操作者自己的当前 session 是允许的；本次响应完成后，后续请求因 session 已撤销返回 <code>401</code>。幂等重放只返回原回执，绝不再次撤销之后创建的新 session。角色移除不自动撤销该用户所有 session，也不改变任何会员或课程 entitlement。

任何角色写入都允许自操作。撤销 <code>permission_admin</code> 必须在事务中确认另有 active 用户仍持有该角色；否则以 <code>409 LAST_PERMISSION_ADMIN</code> 拒绝。该检查必须抗并发自撤销和交叉撤销，保证不会移除最后一名有效管理员。此流程不要求第二个人工审批。

D1 batch 失败后的分类顺序固定为：重新验证操作者授权、查询同 key 回执、确认目标存在、比较管理修订、检查最后管理员约束，最后返回 <code>503</code>。失去角色或 session 被撤销的操作者不能借幂等 key 重放受保护 API。失败分类不得自动重试业务变更。

### 15.5 账户审计分页与隐私

账户审计只按目标账户查询，SQL 必须限制 <code>targetUserId</code>，按 <code>createdAt DESC, id DESC</code> 排序，并多取一条以计算 <code>nextCursor</code>。默认每页 <code>24</code> 条，最大 <code>100</code> 条；对请求的 <code>limit</code> 按接受范围 clamp。游标是 canonical base64url 编码的封闭对象：

<code>{v: 1, owner: actorUserId, scope: "permissions", collection: "account-audit", targetUserId, createdAt: integer, id: string}</code>

游标的 owner、scope、collection 和 target 必须全部与当前操作者及请求路径一致；跨操作者、跨目标或跨 collection 的游标返回 <code>400</code>。游标不构成身份验证或权限证明。

员工响应及审计中绝不返回 session token、token hash、CSRF token、CSRF hash、OIDC Identity、电子邮件、设备信息、私人正文或其他私有内容。账户详情仅返回其表格规定的账户状态、管理修订、角色与 session 数量；会话撤销审计只保存定义中的 count 与操作时间，不暴露被撤销 session 标识。角色变化也不读取 Brief、Task、原图、会员正文或课程正文。

### 15.6 实施边界与定向验收

已接受的实现落点是：

- <code>worker/product/staff.mjs</code>：员工 API handlers。
- <code>worker/product/schema-account.sql</code>：<code>StaffOperation</code>、索引与阻止审计 UPDATE/DELETE 的触发器。
- <code>worker/product/router.mjs</code>：在 <code>ASSETS</code> 前接管 <code>/api/staff</code> 并分派员工路由。
- <code>scripts/verify-product-staff.mjs</code>：复用现有 <code>authVerifier</code> 与 <code>accountVerifier</code> hook；只有确有需要时才增加 hook。

仅在隔离的本地 Wrangler D1 验收：角色能力矩阵、未知支持角色不获权、staff 与会员/课程/私有内容隔离；精确账户读取、role PUT/DELETE、no-op 授予来源保留与审计；Origin/CSRF、伪造 actor、非法字段及超限 body 均不写入；同 key 重放/冲突、CAS 竞争；撤销期间事务授权与注入失败回滚；最后管理员竞争及自撤销 session；只撤销目标快照中的 session、后续新登录不受影响且旧回放不改变 entitlement；24/100 条分页、跨游标拒绝与无 PII；缺数据库、未知路径及不自动引导首个管理员。

生产环境不得按首个用户、电子邮件、请求头或环境变量自动授予初始角色。临时 D1 的本地 verifier 可使用已签名的现有 OIDC 用户，并只允许明确 fixture seed <code>StaffRole</code>。真实初始管理员必须由人工指定 issuer 与 subject，并另行批准相应操作。

本次实现范围不改变生产配置、身份验证算法、账户所有权 SQL、会员/课程 reducer、内容条款或 UI；不添加 dummy tools、远程角色授予或全套测试。本文记录已接受的设计，不表示员工 API 已实现、上述定向检查已执行，亦不表示获得生产授权或通过生产验收。

## 16. 学习内容、课程目录与运动参考的公开契约

本节补充第 9 节的学习路径、课程和运动参考，并保留第 14.1 节与第 15 节已接受的记录形状。本文记录的是已接受设计，不表示实现、发布或生产行为已经验证。

### 16.1 保留原公开投影，并单独生成学习投影

现有产品公开数据继续使用 <code>schema 1</code>、原有 11 个 kind 数组、字段白名单、hash 行为、空数据结构和 11 条现有路由。现有的公开文章页面继续使用真实公开正文。新投影不改变上述接口。

学习数据写入独立的派生文件 <code>content/product-learning-public.json</code>，构建产物写入 <code>output/product-learning-public.json</code>。它不是第二个内容权威，也不是原公开产品数据的第 12 个数组。原始内容仍由私有记录和已批准来源拥有。

学习投影只接受以下顶层形状：

~~~text
LearningPublic = {
  contract: "oneirloom.learning-public",
  schemaVersion: 1,
  baseProjectionHash: string,
  learningPaths: PublicLearningPath[],
  motionReferences: PublicMotionReference[],
  courses: PublicCourseCatalogVersion[],
  lessonPreviews: PublicLessonPreview[]
}
~~~

validator 必须独立校验和解析此投影，并拒绝未知顶层字段及未知嵌套字段。四个数组按 id、revision 排序。每条学习路径保留 steps 顺序，每份课程目录保留 lessons 顺序。

<code>baseProjectionHash</code> 是 <code>SHA-256</code>(<code>canonicalProductJson</code>(<code>validatedPublicV1</code>))。生成器和读取端必须把学习投影与该 hash 对应的已验证 <code>schema 1</code> 产品投影成对校验。读取端不得按当前 head 猜测旧引用。缺失或不匹配时，只让新学习投影不可用，现有 <code>schema 1</code> 投影继续运行。

现有 <code>assertProductPublicShape</code>、<code>emptyProductPublic</code> 和旧投影 resolver 保持原状。学习投影使用自己的 validator 和 resolver。现有 <code>/learn/:articleVersionId/</code> 路由继续工作。四条真实免费学习路径使用 <code>/learn/paths/:id/</code>。

### 16.2 私有 <code>schema 3</code> 只增加三个记录类型

当前 Unit A 发布后，存储扩展从版本 2 升到版本 3。迁移前必须有经过验证且内部一致的备份。迁移在单一事务中完成，并保留旧记录的原始 payload 字节、<code>sourceBindings</code>、payload hash、relations 与审核记录。<code>schema 1</code> 和 <code>schema 2</code> 的旧记录继续被接受，不重新序列化。

<code>schema 3</code> 只用于 <code>learningPath</code>、<code>motionReference</code> 和 <code>courseCatalogVersion</code> 三个新 kind。所有记录拒绝未列出的字段。

~~~text
E3 = {
  kind,
  schemaVersion: 3,
  id,
  revision,
  locale,
  createdAt
}

LearningPath = E3 + {
  title: string,
  summary: string,
  steps: LearningStep[],
  licenseRefs: ExactRef<licenseRecord>[]
}

MotionReference =
  E3 + {
    title: string,
    purpose: string,
    previewAssetId: string|null,
    previewAssetRef: ExactRef<asset>|null,
    preview: MotionPreview,
    inputFormat: string,
    outputFormat: string,
    modelCompatibility: ModelCompatibility[],
    replaceableParameters: ReplaceableParameter[],
    instructions: string,
    licenseRecordId: string,
    licenseRef: ExactRef<licenseRecord>,
    sourceCredit: SourceCredit,
    availability: available|missing_media|rights_pending|unavailable|withdrawn,
    checkedAt: UTC|null
  }

CourseCatalogVersion =
  E3 + {
    courseRef: ExactRef<course>,
    title: string,
    summary: string,
    authorCreditRef: ExactRef<authorCredit>|null,
    lessons: CourseCatalogLesson[],
    licenseRefs: ExactRef<licenseRecord>[]
  }

LearningStep = {contentRef: ExactRef<articleVersion|case|skillVersion>}

CourseCatalogLesson = {
  lessonRef: ExactRef<lessonVersion>,
  title: string,
  isPreview: boolean,
  previewAssetRefs: ExactRef<asset>[]
}

MotionPreview =
  null | {
    sha256,
    byteLength,
    durationMs,
    contentType: "video/mp4",
    codec: "h264"
  }

ModelCompatibility = {
  modelId,
  modelVersion,
  claim,
  evidenceRefs: string[]
}

ReplaceableParameter = {name, description}

SourceCredit = {
  label,
  url: null | approvedPublicHttpsUrl
}
~~~

<code>learningPath</code> 和 <code>motionReference</code> 更新时保留 id、递增 revision，并保留不可变历史。每个 <code>courseCatalogVersion</code> 使用新 id 和 revision 1，之后不可变。id、locale、UTC 时间和文本长度规则沿用现有记录约束。新记录拒绝未知字段。

精确引用仍使用第 14.1 节的 <code>ExactRef</code> 规则。解析键是完整的 kind、id、revision。<code>payloadHash</code> 仍散列完整 canonical target record，并继续要求重算值、存储值与引用值三方一致。新记录不改变旧 hash 语义，也不回退至当前 head。第 14.1 节的 <code>Course</code>、<code>Lesson</code>、<code>Offer</code>、<code>BenefitSet</code> 和其他旧记录形状保持不变。

<code>licenseRefs</code> 只引用精确 licenseRecord。<code>authorCreditRef</code> 只引用精确 authorCredit，或为 null。<code>licenseRefs</code> 与 <code>previewAssetRefs</code> 中的引用不得重复目标 identity。steps 和 lessons 是有序列表，保留原顺序。<code>previewAssetId</code> 与 <code>previewAssetRef</code> 必须同时为 null，或引用同一个 asset id。

### 16.3 课程目录必须绑定同一组精确课时

<code>courseCatalogVersion.courseRef</code> 引用一个完整的 <code>Course</code> <code>ExactRef</code>。目录中每个 <code>lessonRef</code> 引用的 <code>LessonVersion</code>，其 <code>courseRef</code> 必须与目录的 <code>courseRef</code> 完全相同。目录 lessons 中的逻辑 <code>lessonId</code> 必须与 <code>Course.lessonIds</code> 一一对应，顺序完全相同，不能缺少、重复或增加 <code>lessonId</code>。

精确关系只按第 14.1 节的关系表存储。关系表仍只有 <code>sourceKind</code>、<code>sourceId</code>、<code>sourceRevision</code>、name、<code>ordinal</code>、<code>targetKind</code>、<code>targetId</code> 和 <code>targetRevision</code> 八列，不增加 hash 列。新增关系按来源字段和顺序写入：

| 来源字段 | relation name | <code>ordinal</code> |
| --- | --- | --- |
| steps[i].<code>contentRef</code> | steps.<code>contentRef</code> | i |
| lessons[i].<code>lessonRef</code> | lessons.<code>lessonRef</code> | i |
| lessons[i].<code>previewAssetRefs</code>[j] | lessons.&lt;lesson-index&gt;.<code>previewAssetRefs</code> | j |
| <code>licenseRefs</code>[i] | <code>licenseRefs</code> | i |
| <code>previewAssetRef</code> | <code>previewAssetRef</code> | 0 |
| <code>licenseRef</code> | <code>licenseRef</code> | 0 |
| <code>courseRef</code> | <code>courseRef</code> | 0 |
| <code>authorCreditRef</code> | <code>authorCreditRef</code> | 0 |

这些关系不改变第 14.1 节已有八列的 hash 权威。目录可精确引用 <code>Course</code> 与 <code>Lesson</code>，<code>Lesson</code> 继续精确绑定 <code>Course</code>。不得给 <code>Course</code> 或 <code>Lesson</code> 增加反向目录 hash 引用。

课程目录中的 title、summary 和 lesson title 必须逐项审核为公开文字，不得从私有正文摘取。目录的 <code>isPreview</code> 只有在精确目标 <code>LessonVersion</code> 的 <code>isPreview</code> 为 true 时才可为 true。非 preview 课时的 <code>previewAssetRefs</code> 必须为空。<code>previewAssetRefs</code> 必须是该 <code>LessonVersion.assetRefs</code> 的子集。

公开一整份试看正文前，检查目标 <code>LessonVersion</code> 的全部许可及实际使用依据。公开所选附件前，只检查被选中的公开附件及其实际使用依据。试看正文必须是整篇获准正文，不按字符比例截取。

课程没有任何可公开的完整 <code>Lesson</code> 正文时，不生成公开课程卡片。公开课程目录不包含 <code>Offer</code> ID、Benefit <code>manifest</code>、价格、购买状态或 <code>entitlement</code>。

### 16.4 学习投影使用独立的公开引用和封闭记录

<code>PublicRef</code> 与私有 <code>ExactRef</code> 不同。<code>PublicRef</code> 的 hash 是目标公开记录的 canonical projection hash，不是私有 <code>payloadHash</code>。四个公开数组中的 kind 依次固定为 <code>learningPath</code>、<code>motionReference</code>、<code>courseCatalogVersion</code> 和 <code>lessonPreview</code>。

~~~text
PublicRef = {kind, id, revision, projectionHash}

PE = {kind, schemaVersion: 1, id, revision, locale, createdAt}

PublicAuthor =
  null | {displayName, approvedLink}

PublicCredit = {
  author,
  licenseName,
  licenseVersion,
  requiredCredit
}

PublicLearningPath =
  PE + {
    title,
    summary,
    steps: [{contentRef: PublicRef<articleVersion|case|skillVersion>}],
    credits: PublicCredit[]
  }

PublicMotionReference =
  PE + {
    title,
    purpose,
    inputFormat,
    outputFormat,
    modelCompatibility: [{modelId, modelVersion, claim}],
    replaceableParameters: ReplaceableParameter[],
    instructions: string,
    sourceCredit: SourceCredit,
    availability: available|missing_media|rights_pending|unavailable|withdrawn,
    checkedAt: UTC|null,
    preview: PublicVideo,
    credits: PublicCredit[]
  }

PublicCourseCatalogVersion =
  PE + {
    courseId,
    courseRevision,
    title,
    summary,
    authorCredit: PublicAuthor,
    lessons: PublicCourseLesson[],
    credits: PublicCredit[]
  }

PublicCourseLesson = {
  lessonId,
  lessonVersionId,
  lessonRevision,
  title,
  isPreview,
  previewRef: null | PublicRef<lessonPreview>
}

PublicVideo = null | {
  url,
  sha256,
  byteLength,
  durationMs,
  contentType: "video/mp4",
  codec: "h264"
}

PublicPreviewAsset = {
  id,
  revision,
  assetKind,
  url,
  derivativeHash,
  alt,
  credits: PublicCredit[]
}

PublicLessonPreview =
  PE + {
    courseId,
    courseRevision,
    lessonId,
    title: string,
    body: string,
    assets: PublicPreviewAsset[],
    credits: PublicCredit[]
  }
~~~

公开学习路径的每个 <code>contentRef</code> 都必须解析到配对的旧 <code>schema 1</code> 投影中的精确 <code>ArticleVersion</code>、<code>Case</code> 或 <code>SkillVersion</code>。试看 <code>previewRef</code> 只能解析到同一新学习投影中的 <code>LessonPreview</code>，不反向引用课程目录的 hash。<code>LessonPreview</code> 使用来源 <code>LessonVersion</code> 的 id 和 revision，并使用与 <code>lessonVersion</code> 不同的派生 kind。

<code>PublicLessonPreview.body</code> 是整篇获准公开的 <code>LessonVersion</code> 正文，不是正文片段。<code>PublicCourseCatalogVersion.courseId</code> 和 <code>courseRevision</code> 与来源 <code>courseRef</code> 精确匹配。<code>PublicCourseLesson.lessonVersionId</code> 和 <code>lessonRevision</code> 与 <code>lessonRef</code> 目标精确匹配。<code>PublicLessonPreview.courseId</code> 和 <code>courseRevision</code> 与绑定的 <code>Course</code> 精确匹配。<code>previewRef</code> 只能指向同一课程和课时版本的 <code>LessonPreview</code>。

公开 author 和 credit 只使用字段白名单。<code>sourceCredit.url</code> 只能是明确获准公开的 HTTPS 链接，不包含私有许可证明字段。任何新学习投影若包含 private <code>payloadHash</code>、<code>sourceBindings</code>、<code>evidenceRefs</code>、会员非试看正文、私有路径或 key、原始许可证明、<code>Offer</code>/Benefit 字段、<code>scopeHash</code> 或 <code>manifest</code>，校验必须失败。

### 16.5 审批、许可与匿名公开是不同事实

以下事实分别记录，任何一项都不能替代其他事实：

- 对精确内容版本的 editorial approval。
- 本地候选检查结果。
- 受限发布回执。
- 学习公开发布回执及实际读取结果。

<code>Lesson</code>.<code>isPreview</code>、<code>Course.publicationStatus</code>、<code>entitlement</code> 和受限发布回执都不能单独证明匿名用户能访问公开正文。公开正文前必须核对所有绑定许可、当前许可、实际用途和来源依据。公开附件还必须是该 <code>LessonVersion</code> 引用并选择的附件。

许可判断复用已有 <code>license.permittedUses</code>、明确来源事实、已批准记录或可信的历史自有公开证明。不得增加全局 rights audit、新许可 schema 或法律审核 gate。只有具体许可限制或实际 <code>SOURCE GAP</code> 才阻止受影响条目。不得虚构许可依据，也不得删除已确认的限制。地域或会员专用的明确许可，在没有相应访问控制时不能当作匿名公开许可。已确认属于自有内容且已有可信批准的来源可以直接复用，不重复审计。

### 16.6 发布、受限读取与撤回应分开记录

学习公开使用现有操作框架中的三个独立操作：

- <code>learning_public_publish</code>
- <code>learning_public_withdraw</code>
- <code>learning_public_rights_update</code>

计划与回执必须绑定精确选择、<code>approvalEventIDs</code>、<code>sourceBindingsHash</code>、<code>relationsHash</code>、目标环境、<code>baseProjectionHash</code>、<code>newProjectionHash</code>、媒体 hash 与长度，以及实际读取结果。旧 publication_items、旧证明和受限发布证明保持不变。

候选可以标记为 approved 的 <code>local_candidate</code>，并保持 <code>publicationPerformed</code> 为 false。这不表示已发布。实际学习公开发布依赖原有公开证明与原有依赖；新学习投影单独保存自己的发布证明。

受限读取 handler 必须核对当前精确的公开 preview 发布记录和许可。受限回执加 <code>isPreview</code>=true 不足以授权读取。静态公开 preview 可以先于受限发布操作发布。

撤回必须实际移除受影响的静态文件、媒体和缓存，并通过读取结果确认。<code>D1</code> 中仅有受限状态变化不足以证明撤回完成。任何移除或读取失败都保持 <code>pending</code> 或 <code>needs_reconcile</code>，直到实际完成对账。

### 16.6.1 Private runtime transport for current learning publication proof

The local library remains the sole authoring authority. ACCOUNT_DB may retain
a private serving mirror of the existing learning-public operation receipts
and one current publication pointer per environment. These records add no
product kind, public entity, grant, public projection field, or publication
operation. They do not reuse restricted publication receipts or require a
restricted publication.

For this transport, current source and license facts mean the facts explicitly
synchronized for the target environment by the existing learning-public
operations. A local draft, source revision, editorial event, or license head
change does not silently update that environment. An intended change to an
active public publication must use learning_public_publish,
learning_public_rights_update, or learning_public_withdraw as applicable.
Unsynchronized local facts must not be described as verified runtime facts.

Apply regenerates the exact source closure and current license facts from the
local library. The runtime mirror binds those facts to the same environment,
operation ID, expected revision, manifest, projection, and readback evidence.
Preparing an operation conditionally reserves that environment and makes its
anonymous resolver unavailable until reconciliation establishes a verified
current publication. A conflicting operation cannot replace the reservation.
The runtime commit uses the existing expected-revision CAS and preserves
same-key recovery. There is no atomic transaction across the local library,
D1, static files, or media storage.

Read the current pointer, receipt, and synchronized source facts from private
storage on every request. Do not reconstruct current facts from a historical
receipt alone. Require their exact agreement with the existing resolver
checks. Read the paired public projections and selected media through a
server-bound asset reader or a fixed owned origin. The caller supplies only
the accepted PublicRef. Reject arbitrary origins, manifest URLs, redirects,
and client-supplied proof.

Before returning a successful resolver result, confirm that the current
operation, revision, source facts, and verification evidence remain unchanged.
A changed or non-verified publication returns null. Required storage,
configuration, or integrity failures retain the section 17.1 service error.
Do not cache current authorization facts across requests.

Keep all source references, operation records, and proof private. Return only
the existing section 17.1 resolver result internally and the existing public
DTO externally. Runtime invalidation does not prove static withdrawal.
Section 16.6 still requires actual file, media, and cache removal readback.
Missing learning proof affects only anonymous learning reads and does not
change private purchase authorization.

### 16.7 运动参考只使用可验证的本地预览

<code>availability</code> 只允许 <code>available</code>、<code>missing_media</code>、<code>rights_pending</code>、<code>unavailable</code> 或 <code>withdrawn</code>。

<code>available</code> 必须对应实际可读的本地文件、真实 <code>sha256</code> 和 <code>byteLength</code>、MP4/H.264 格式，以及当前有效的公开使用授权。<code>durationMs</code> 必须大于 0 且不超过 30000。<code>byteLength</code> 必须大于 0 且不超过 10485760。只有 <code>availability</code> 为 <code>available</code> 且存在获准公开的派生 URL 时，<code>PublicVideo</code> 才能非空；不得指向会员媒体、私有文件路径、文件系统路径或外部下载。

<code>checkedAt</code> 只能写实际检查时的 UTC 时间或 null。生成时间不等于检查时间。<code>modelCompatibility</code> 中的 <code>claim</code> 只能基于精确 <code>modelId</code>、<code>modelVersion</code> 和证据。缺少模型证据时不输出模型 <code>claim</code>，但不因此阻止其他有依据的参考信息。<code>instructions</code> 本身仍须有公开依据。

播放器在用户点击前不设置 <code>src</code>，也不发起 <code>preload</code> 请求。用户点击后才加载，显示 <code>controls</code>，不自动播放，不循环。加载失败时显示真实不可用状态和文字说明。该设计不要求 <code>poster</code>，不增加站内转码、外部下载、生成式视频或图片轮播替代视频。

### 16.8 免费学习路径和空状态保持真实

四条真实免费文章路径按 [学习路径索引](learning/index.md) 的顺序排列。每条路径都精确引用对应 <code>ArticleVersion</code>。只有确有帮助时才增加 <code>Case</code> 或 <code>SkillVersion</code>，不按数量配额凑引用。保留现有文章正文、免费安装入口和 18 个固定 <code>SkillVersion</code>。四条路径不是 <code>Course</code>、<code>Offer</code> 或 Benefit。

课程页与参考页按第 9 节融入现有路线；未明确的路由不新增承诺。没有真实视频时不显示假视频。没有真实课程内容时显示实际空状态，不生成空课程、测试价格、假购买按钮或虚构的四门免费教程。合成 UI fixture 只用于隔离验收，不作为真实产品内容。

真实视频只有在提供压缩后的源文件、许可与 credit、参考说明后才进入实际播放验收。缺少 model compatibility 证据时，compatibility 可为空。真实课程需要完整撰写的 <code>Lesson</code>、作者信息和明确选定的一份整篇试看正文。价格、条款或支付服务商只阻止销售启用，不要求伪造课程内容。

### 16.9 后续实现单元和边界

以下单元描述后续 owner 释放对应资源后的工作范围，不增加协调者阶段审批，也不表示这些工作已经实现或验收。

1. 内容 producer、library 和 CLI 将存储从版本 2 扩到版本 3，加入三个新 kind、精确关系、独立学习投影和候选 CLI。经验证的备份迁移必须保留旧 payload 原始字节、hash、relations、审核记录和原 <code>schema 1</code> 公开输出。定向检查覆盖错误 exact hash、课程课时覆盖、未知嵌套字段和私有 canary。
2. 新增四条真实免费路径和独立公开 consumer。定向检查覆盖 <code>baseProjectionHash</code> 不匹配、精确引用、页面内容准确性、链接及现有 18 个固定 <code>SkillVersion</code> 与免费安装入口。
3. 课程、整篇试看和视频 UI 使用隔离的合成 fixture。检查完整正文、付费正文泄漏、点击前不请求媒体、播放失败状态和不出现假购买。实际媒体仅在满足本节真实视频输入条件后检查真实播放。
4. 发布 <code>Worker</code> 使用本地 adapter 检查当前公开回执、私有 grant 隔离、许可、<code>CAS</code>、重放、hash 冲突、对账和真实撤回读取结果。
5. <code>Progress</code> 继续按第 9 节由服务端 owner SQL 写入，按精确 <code>LessonVersion</code> 绑定，使用 user、course、lesson 唯一键和 revision 幂等。课程新版本不清除旧进度。个人 <code>Progress</code> 不进入公开学习投影。

本节不授权完整测试套件、打包、云端配置或新的实际公开发布。真实价格、条款和支付接入须在销售启用范围内单独处理。

## 17. Member content delivery, commerce, and learning progress

This section records the accepted contracts for exact member content, orders, payment facts, reconciliation, and learning progress. It does not claim implementation or production behavior.

### 17.1 Serve exact member content

Unit C exposes these read routes:

| Route | Accepted input |
| --- | --- |
| `GET /api/member/content/:kind/:id/:revision?payloadHash=…` | `kind` is only `articleVersion` or `lessonVersion`. The exact `payloadHash` is required once. |
| `GET /member-media/:id/:revision?payloadHash=…&action=read` or `GET /member-media/:id/:revision?payloadHash=…&action=download` | The path identifies an exact `Asset`. The exact `payloadHash` and one `action` are required. |
| `GET /api/member/content/lessonPreview/:id/:revision?projectionHash=…` | The exact `projectionHash` is required once and resolves the `PublicRef<lessonPreview>` defined in §16.4. |

Encode each ID once per path segment and decode it once. Require a positive integer revision. Reject `latest`, object keys, arbitrary URLs, user IDs, client-selected use, unknown query names, and duplicate query parameters.

Private read responses use closed DTOs. `PrivateArticleRead` has exactly these fields:

```text
{
  schemaVersion: 1,
  contentRef: ExactRef,
  articleId: string,
  locale: string,
  title: string,
  body: string,
  assets: [{
    contentRef: ExactRef<asset>,
    assetKind,
    alt,
    readUrl: string|null,
    downloadUrl: string|null
  }],
  credits: PublicCredit[]
}
```

`PrivateLessonRead` has the same fields, with `courseId`, `courseRef`, and `lessonId` in place of `articleId`. `courseRef` is the exact course reference. Neither DTO has additional fields.

For each attachment, issue only URLs whose exact action the current license permits. Omit an attachment when neither action is available. An unavailable attachment does not block permitted text. Anonymous requests may read only the existing whitelisted `PublicLessonPreview`. They never receive a private `payloadHash`, scope or license references, or a manifest.

Handle a request in this order:

1. Parse the method, path, and closed input.
2. Resolve the exact resource. Validate the complete projection bytes and hash, current resource state, binding, and current license.
3. For a public preview, require the current learning receipt. For private content, require the current session.
4. Resolve owner grants through each validated `GrantScopeBinding`, its `BenefitSetVersion`, and its canonical content scope, hash, exact content, and exact action. For order grants, also check the frozen `Offer`.
5. Pass only verified individual grants and scopes to the existing `checkContentAccess`. For private content, set `audience=member` and `isPreview=false`.
6. Read media and respond only after authorization succeeds.

A coarse `courseId` or `memberScopes` value cannot authorize another version. An article preview cannot authorize its body. Derive `RequestedUse` from the operation and trusted facts: `read` means `display`, and `download` means `download`. Ordinary reading does not authorize derivatives or redistribution. Paid-order authorization includes the commercial use in the frozen Offer. Evaluate each legitimate grant origin and use the union of valid grants. One invalid origin does not invalidate other valid origins.

Return these errors:

| Condition | Response |
| --- | --- |
| Invalid request | `400 INVALID_REQUEST` |
| Missing exact version, withdrawn content, or a license that cannot serve the request | `404 CONTENT_UNAVAILABLE` |
| Account required | `401 AUTH_REQUIRED` |
| Signed-in user lacks the exact grant and action | `403 ENTITLEMENT_REQUIRED` |
| Configuration, projection integrity, or required dependency failure | `503 SERVICE_UNAVAILABLE` |

A missing `MEMBER_MEDIA` binding affects only media. It does not block text that the user may read.

Set `Cache-Control: private, no-store`, `Pragma: no-cache`, and `Vary: Cookie` on every success, error, `HEAD`, and Range response. Do not send `ETag` or `304`, and do not redirect a private read to a public URL. An optional `HEAD` request uses the full authorization path. Accept at most one authorized byte range after authorization. Return `416` for an invalid range. No `HEAD`, Range, or filename path may bypass authorization.

Return credits through the approved `PublicCredit` DTO only. Do not expose private license records.

The internal resolver has this contract:

```text
resolveCurrentLearningPublicRead(publicRef, environmentId) ->
  null | {
    environmentId,
    publicationOperationId,
    newProjectionHash,
    publicRef,
    sourceContentRef,
    selectedAssetRefs,
    publicRecord,
    verificationEvidenceHash
  }
```

The learning owner supplies this result only from a current verified publication, this environment's current projection and exact selection, and a successful read proof. Return `null` for `local_candidate`, `pending`, `needs_reconcile`, `withdrawn`, or an old projection. Keep internal references and proof out of public responses. Do not add a client credential or a new entity for this resolver. A missing reader closes only anonymous access. It does not affect private purchases. A static preview may be published before restricted learning content. Do not require a restricted receipt for that static preview.

### 17.2 Create orders and check out

The order routes are:

| Route | Request |
| --- | --- |
| `POST /api/orders` | `Idempotency-Key` header and closed body `{offerVersionId}` |
| `POST /api/payments/checkout` | `Idempotency-Key` header and closed body `{orderId}` |
| `GET /api/orders?limit=…&cursor=…` | Current user's order list |
| `GET /api/orders/:orderId` | One order owned by the current user |
| `POST /api/payments/webhooks/stripe` | Raw body with a verified signature |

User operations require `currentSession`. Both POST routes require exact Origin and the existing session CSRF check in `auth.mjs:361`. Every order SQL query binds `userId` to the session user. Return `404` for another user's order or for an absent order.

The server sets price, currency, scope, provider, and user ID. It verifies that the current Offer is for sale. Preserve existing Order fields and add this immutable snapshot. The `offerProjection` field contains the full verified restricted-content projection:

```text
OrderOfferSnapshot = {
  orderId,
  offerProjection,
  scopeHash
}
```

Compute `termsSnapshotHash` as `SHA-256(canonicalProductJson({schemaVersion:1,offerProjection,scopeHash}))`. Build `reducerOffer` as `{id,...offerProjection.data}`. Bind provider checkout and payment IDs on the first write only. Accept a later write only as an identical replay. A later payment never replaces the frozen Offer, price, or sale state with current values.

The closed `UserOrderDTO` is `{id,offerVersionId,amountMinor,currency,termsSnapshotHash,status,revision,createdAt}`. Return a list as `{items,nextCursor}`. Never return the full Offer, scope, payment events, provider payloads, or another user's data.

Store one `OrderCheckout` per order:

```text
{
  orderId,
  requestHash,
  providerIdempotencyKey,
  state: "prepared"|"ready"|"needs_reconcile",
  providerCheckoutId: string|null,
  checkoutUrl: string|null,
  expiresAt: UTC|null,
  revision
}
```

Commit the `prepared` row before calling the provider. Then bind the provider result with compare-and-swap. Derive the provider idempotency key from provider, mode, and order ID. Do not derive it from a browser retry key.

On success, return `{orderId,checkoutUrl,expiresAt}`. If the response is lost, recover the original row and provider key. A timeout, a different browser key, or expired provider idempotency never creates a new checkout automatically. Record expiry explicitly and never invent a checkout URL.

By default, sales and checkout are disabled. Return `503 PAYMENTS_DISABLED` without calling a provider. Isolated fixture configuration is the only enablement mechanism. Do not add an HTTP toggle. Disabling sales does not stop valid existing webhooks. Keep `checkoutEnabled` and `webhookEnabled` separate.

Webhook handling does not use cookies, Origin, or CSRF. Verify raw bytes, signature, timestamp, mode, and configured account boundary before writing a transaction. Claim `/api/orders` and `/api/payments` and every child path before `ASSETS`, including unknown provider, method, or path combinations. Return private JSON errors. Never fall back to static assets.

### 17.3 Store payment facts and serialize grants

Preserve the existing pure financial-facts, event-facts, Order, and reducer model. Add `OrderFinancialFacts(orderId PRIMARY KEY, factsJson)` and version it with the Order revision.

Add `PaymentEvent` with primary key `(provider, providerMode, eventId)` and a `processingRevision`. It retains the verified payload hash, receipt time, necessary raw facts, and processing result. Enforce uniqueness for non-null `(provider, providerMode, providerPaymentId)` and for checkout identity. Keep the existing entitlement-source uniqueness.

Add `MembershipScopeRevision(userId, benefitSetVersionId, revision)`. Add one immutable `PaymentOperation` receipt and audit record in the existing CAS transaction. It records at least the operation key, input hash, event identity, expected and actual event revisions, expected and actual Order revisions, optional expected and actual membership revisions, the before and after financial summary or canonical facts, grant ID, result, and time. Read actual values with `SELECT` inside the batch and check expected values against them.

After webhook authentication, insert an event in `received` state with `ON CONFLICT DO NOTHING`. For the same event key and payload hash, read and return the original record. For the same key with a different hash, preserve conflict evidence and never overwrite the original.

Read the current Order, facts, event, grant, and membership scope, then run the reducer. One D1 batch writes the audit record, Order and facts, grant and first `GrantScopeBinding`, and final event state in that order. Any failure rolls back the whole batch. A separately committed `received` event remains. After an uncertain transaction result, read the original key before any retry.

A signed supported event without a real Order binding stays `received` with `orderId=NULL` and `needs_reconcile`. Do not construct a required bound normalized event or create a grant before the binding exists.

SQL triggers increment the matching `MembershipScopeRevision` in the same transaction for every `membershipEntitlement` insert, window-affecting update, and delete, including `operator_adjustment`. Do not increment only for manual payment paths. Treat a missing revision row as `0` and upsert the first change. If an allowed change moves an owner or scope, increment both the old and new keys. Prefer the existing immutable grant identity and window rules.

Different Orders for the same owner and exact benefit compete on the same membership scope revision, even when both Order revisions are `0`. After a CAS conflict, reload grants and recalculate. Recalculate at most twice per request. A persistent conflict leaves the event `received` and returns a retryable failure. Do not add a queue or background loop.

Keep the existing window calculation: `start=max(payment.effectiveAt, latest endsAt for the same owner and exact benefit among non-revoked grants)`, then `end=start+durationDays`. A suspended grant still counts when it is not revoked. An indefinite grant uses the existing reconciliation path. A refund never reorders another fixed window.

Use the [D1 batch transaction contract](https://developers.cloudflare.com/d1/worker-api/d1-database/#batch) and the existing `worker/index.mjs:106` CHECK mechanism. Local race and rollback checks are required. They do not replace the documented transaction contract.

### 17.4 Normalize Stripe events and reconcile facts

Use the Stripe `PaymentIntent` ID as the canonical payment ID. Do not mix it with a Session or Charge ID. Verify success mode, Order binding, currency, and amount against the known binding or trusted provider readback.

A `payment_intent.succeeded` event must have object status `succeeded` and an amount. A `checkout.session.completed` event is not paid when `payment_status` is unpaid. An asynchronous-success event, or a paid Session without canonical payment facts, enters reconciliation. Use the [Stripe event type definitions](https://docs.stripe.com/api/events/types).

Set `effectiveAt` from the first canonical `payment_intent.succeeded` event time, or from the same success time in authoritative reconciliation. Persist that first value for the payment. Later events for the same payment reuse it and retain their own event-created time as evidence. Never derive successful `effectiveAt` from `PaymentIntent.created`. See the [Stripe PaymentIntent object](https://docs.stripe.com/api/payment_intents/object). Keep an existing same-payment fact unchanged, but reject a conflicting amount, currency, or binding.

For `charge.refunded`, use the verified related Charge's cumulative `amount_refunded`. Do not use one `Refund.amount` or a pending refund as the cumulative total. Use the [Stripe Charge object](https://docs.stripe.com/api/charges/object).

A terminal refund first recorded before payment does not create paid status. A late paid event cannot revive it. Incomplete or conflicting refunds and dispute states enter `needs_reconcile`. Ordinary events continue through the existing reducer. A conflicting terminal repeat in the existing dispute merge remains `needs_reconcile`.

Use an explicit internal reconciliation adapter with trusted fixtures now. Future provider readback needs separate authorization and must stop at authentication or access denial. Do not expose client financial HTTP endpoints. The closed reconciliation input is:

```text
{
  provider,
  providerMode,
  orderId,
  providerCheckoutId,
  providerPaymentId,
  amountMinor,
  currency,
  financialFacts: existing,
  observedAt,
  evidenceHash,
  complete: boolean
}
```

Require an exact transaction binding. Incomplete reconciliation cannot create or restore a grant. Under the original Order and Event CAS, record explicit reconciliation facts and then run the reducer. A confirmed cumulative refund never decreases. A recorded reversed state never clears. A confirmed lost, refunded, or revoked Order never becomes paid or won later. An authoritative `won` or `open` to `lost` transition is allowed and audited in the same batch. If authoritative facts conflict with an irreversible state, keep `needs_reconcile`. Never choose the favorable state automatically.

If reconciliation facts change while `reducer.changed=false`, compare the actual stored aggregate and increment the Order revision when that aggregate changed. Retain every event for the same payment. Keep one canonical payment tuple, one grant, and the immutable payment binding.

### 17.5 Save exact learning progress

Do not invent learning time or change the Lesson schema. `LastPosition` is closed:

```text
Text = {kind: "text", basisPoints: integer 0..10000}
Media = {
  kind: "media",
  assetRef: ExactRef<asset>,
  positionMs: nonnegative safe integer
}
```

For text, compute `basisPoints` from the exact Lesson body as `scrollTop/(scrollHeight-clientHeight)*10000`. Store `0` when there is no scrollable range. Do not infer completion from position.

For media, accept only a supported time-based media attachment on the exact Lesson and require read permission. A restored position is user-reported progress, not watch time or automatic completion. Do not invent an upper duration when the real duration is unknown. The actual player clamps to the real media duration. Missing media does not block text progress or local fixtures.

The mutable `Progress` head has `{userId,courseId,lessonId,revision}` with primary key `(userId,courseId,lessonId)`. Store each immutable history row as `immutableProgressRevision` with `{userId,courseId,lessonId,revision,courseRefJson,lessonRefJson,lastPositionJson,completed,updatedAt}` and primary key `(userId,courseId,lessonId,revision)`. `completed` is an explicit boolean independent of position. Set `updatedAt` from server UTC. Never update or delete history rows. Follow the existing account deletion policy. Do not add a deletion API.

The routes are:

| Route | Request and response |
| --- | --- |
| `GET /api/me/progress?courseId=…&limit=…&cursor=…` | `{items,nextCursor}` |
| `GET /api/me/progress/:courseId/:lessonId?revision=N` | One head or requested revision in the existing response shape |
| `PUT /api/me/progress/:courseId/:lessonId` | `Idempotency-Key` and closed body `{expectedRevision,courseRef,lessonRef,lastPosition,completed}` |

Return an item as `{courseId,lessonId,revision,courseRef,lessonRef,lastPosition,completed,updatedAt}`. A missing item returns `404`. The first write uses `expectedRevision=0`.

Bind every SQL query and receipt key to the session owner. Do not accept a client user ID. The PUT route requires exact Origin and CSRF. Resolve the exact Lesson and Course references, course ID, and logical Lesson ID. Reuse Unit C's exact-read checks before writing progress, and require the media attachment read permission for media positions.

The owner can read progress history after membership expires. The response contains no lesson body and requires no access grant. For an idempotency key with the same request hash, return the original success even if `expectedRevision` is now stale. A different hash for that key returns `409`. A new key with a stale expected revision also returns `409`.

If references, position, and completion are unchanged, do not change the revision or time, but store the successful receipt. For changed progress, commit the CAS, receipt, history row, and head in one batch. New content does not change existing progress automatically. An explicit save creates a new revision and preserves old references and history. Old completion does not transfer to new content. Bind cursors to the owner, collection, and optional course filter.

Add an `IndependentProgressMutationReceipt` with the existing receipt shape. Do not widen the closed `AccountMutationReceipt.scope` check. Keep order-creation receipts independent as well.

### 17.6 Release units and their boundaries

Unit C adds the serving handlers after Unit B releases its reader and serializes the later router integration. It does not edit the pure entitlement reducer, content producer, or public schema. Its targeted checks cover rejection of an old grant for a new version, coarse-scope leakage, withdrawn licenses, an Article summary that cannot authorize or leak the member body, anonymous access without a current receipt, anonymous access with an exact receipt, media actions, no-cache headers on every response, and no key leakage.

OI-38 adds orders, checkout, Stripe normalization, and persistence. It reuses the independent signature verifier and pure reducer. One owner writes the schema. Targeted checks cover same-key replay, conflicting hashes, the same payment across different events with one grant, non-overlapping grants for different Orders in the same benefit scope, atomic rollback after every write failure, refund before payment, dispute restoration of original windows, and uncertain results recovered by the original key.

Progress adds its handler, head, history, receipt, serving, and auth wiring. Targeted checks cover owner binding, idempotency, hash conflicts, stale revisions, no-op clocks, concurrent single-winner writes, history across new content, and text and media positions.

Perform final router and schema integration with one writer after release. Claim every private prefix before `ASSETS`. Verify that disabled sales make no provider call, signed webhooks do not require CSRF, and user POST routes do.

If Unit B's final exports, the current learning receipt location, or schema ownership is refuted, or a check fails for an unexplained reason, return the concrete evidence. Do not alter the reducer, public whitelist, or authentication boundary to work around it. Missing Unit B exports or the learning receipt location blocks only the dependent wiring. Do not invent a replacement module or local fixture to stand in for either dependency.

Real prices, courses, videos, Stripe access, cloud configuration, and publication are outside the local implementation prerequisites.

## 18. Official WeChat Pay and Alipay merchant payments

### 18.1 Current choice and preserved boundaries

The first release supports ordinary direct-merchant WeChat Pay Native and Alipay website payments through `alipay.trade.page.pay`, with `FAST_INSTANT_TRADE_PAY` and the provider-hosted QR redirect mode. Both methods are single purchases. Membership renewal remains an explicit new purchase.

This section supersedes the first-release Stripe choice in sections 10.3, 11, 17.2, 17.4, and 17.6, and supersedes the cancelled personal-QR manual-confirmation proposal. Existing Stripe work may remain disabled. It is not required to activate either merchant method. Cryptocurrency remains outside this release.

Preserve immutable Offers, Order snapshots, exact content scope, current-rights checks, independent grant sources, financial facts, Order and Event CAS, membership-scope revisions, audit records, operation receipts, and refund rules. A provider adapter never fabricates a Stripe event or directly inserts an entitlement.

Merchant applications, actual commercial eligibility, credentials, provider environment access, deployment, and live sales are separate from local implementation.

### 18.2 Select a method before freezing the Order

Replace the closed order-creation body with:

```text
{offerVersionId, paymentMethod: "wechatpay_native"|"alipay_page"}
```

The browser selects only a public method. The server resolves that method to an enabled configuration and freezes the provider, provider mode, merchant-account binding, and method on the Order. Clients cannot supply an account, mode, price, currency, duration, scope, callback URL, or provider API endpoint.

`POST /api/payments/checkout` retains the closed body `{orderId}`. It cannot change the method or account of an existing Order.

Add `GET /api/payments/methods`, returning only:

```text
{items: [{paymentMethod}]}
```

Include only methods currently enabled for new checkout. This endpoint discloses no merchant identifiers or configuration. Existing user routes retain session ownership, Origin, CSRF, idempotency, and private-response rules. Add `paymentMethod` to `UserOrderDTO`.

New merchant Orders require a positive safe-integer CNY amount and an approved Offer with the existing commercial-use checks. Freeze the full verified Offer projection, `scopeHash`, and `termsSnapshotHash` as section 17.2 specifies. Neither a later callback nor a changed catalogue substitutes a newer Offer or scope.

### 18.3 Provider order identity

Preserve the existing internal Order UUID. For these two methods, encode its validated UUID bytes as 32 lowercase hexadecimal characters without hyphens:

```text
merchantOrderNo = lowercaseHex(uuidBytes(Order.id))
```

Do not truncate a UUID or prepend a prefix that exceeds WeChat's limit. Persist the encoding and its Order binding before exposing checkout.

Add an immutable `providerAccountBindingId` identifying the configured provider, mode, and merchant/application tuple. It contains no secret. One Order has one account binding, one `merchantOrderNo`, and at most one canonical provider payment ID.

Enforce unique merchant-order and payment bindings on the Order or a dedicated binding table:

```text
(provider, providerMode, providerAccountBindingId, merchantOrderNo)
(provider, providerMode, providerAccountBindingId, providerPaymentId)
```

The payment uniqueness constraint must not be placed on `PaymentEvent`; several events can describe the same payment.

WeChat's canonical payment ID is `transaction_id`. Alipay's is `trade_no`. Neither a QR string, merchant order number, notification ID, nor browser return token is a payment ID.

Native and PagePay need not produce a separate provider checkout/session ID. Keep `providerCheckoutId=null` when the provider supplies none. Do not invent one to satisfy a Stripe-shaped interface.

### 18.4 Checkout preparation and presentation

Extend the single `OrderCheckout` record with the frozen account binding, method, merchant order number, request parameters, and a typed presentation:

```text
CheckoutPresentation =
  {kind:"qr", provider:"wechatpay", codeUrl:string}
  | {kind:"redirect", provider:"alipay", url:string}

OrderCheckout.state =
  "prepared"|"ready"|"needs_reconcile"|"expired"|"closed"
```

The successful response is closed:

```text
{orderId, paymentMethod, presentation, expiresAt}
```

This replaces the mandatory `checkoutUrl` response. WeChat `code_url` is QR payload, not a website redirect. Alipay PagePay returns an actual signed official gateway URL. Do not fabricate an Alipay `qr_code` or label a merchant-created URL as provider output.

Persist `prepared` before the provider operation or before producing a usable signed redirect. Persist the frozen request, absolute expiry, presentation, and receipt before returning the presentation. `ready` means the presentation is available; it does not mean a provider transaction exists or is paid.

Use the same merchant order number and frozen financial parameters for every recovery. Browser idempotency keys identify browser operations; they cannot select another provider order.

Use a persisted absolute expiry, initially 30 minutes from checkout preparation. Send that deadline in each provider's supported format. A retry never extends it. Local expiration stops presentation but does not prove financial closure.

After a timeout or uncertain response, read the original checkout and operation receipt first. Authoritative query or close operations use the original merchant order number. An unknown provider outcome, expired QR, changed browser key, or gateway error must not automatically create another financial purchase.

Changing payment methods requires a new, explicit purchase after the preceding attempted payment is conclusively closed or resolved. Do not automatically replace an uncertain Order. A late authentic payment remains a financial fact and follows the original frozen terms.

### 18.5 Authenticate provider messages before financial processing

Add exact POST routes:

```text
/api/payments/webhooks/wechatpay
/api/payments/webhooks/alipay
```

Claim these routes and all unknown `/api/payments` descendants before static assets. Webhooks use provider authentication rather than cookies, Origin, or CSRF.

Use bounded raw-body reads. Preserve the raw bytes until authentication completes. Reject malformed encoding, duplicate security headers or form keys, unsupported algorithms, invalid signatures, and account or mode mismatches before inserting payment facts.

For WeChat:

- Use API v3 request signing and response verification.
- Verify the signature over the timestamp, nonce, and exact raw body using the configured WeChat public-key ID and public key.
- Enforce the five-minute signature timestamp window. A retried notification has a new transport signature; the original payment time can be much older.
- Decrypt `AEAD_AES_256_GCM` using the configured API v3 key, nonce, and associated data.
- Require the supported notification/resource types and matching `mchid`, `appid`, `out_trade_no`, currency, and total amount. Refund messages without an AppID resolve through the frozen merchant-order binding and verify every account field that the message actually supplies.
- Unknown key IDs cannot trigger key downloads or trust a key supplied by the request.

For Alipay:

- Accept the documented UTF-8 form notification format.
- Decode form values exactly once. Reject duplicate keys and malformed encodings.
- Require `RSA2`. Verify all signed parameters using the configured Alipay public key and the official notification canonicalization rules. Do not verify JSON reserialization of the form.
- Require `app_id`, `seller_id`, and `out_trade_no` to match the frozen configuration and Order. Reject unsupported delegated-account fields or account modes.
- Preserve `notify_time` as evidence. Do not apply Stripe's five-minute expiry to an Alipay business notification that may be retried later.
- The return URL never grants access, even when its parameters are signed.

Mode comes from the server-side route configuration and key/account binding. Neither provider is required to supply Stripe's `livemode` field. Fixture, sandbox, and live bindings remain distinct.

### 18.6 Separate delivery evidence from event identity

Keep the existing provider Event model. For these merchant adapters, qualify the provider notification ID with its immutable account binding. WeChat uses notification `id`; Alipay uses `notify_id`. A supported notification without a usable identity remains unbound reconciliation evidence and cannot grant.

Add an immutable callback receipt containing:

```text
{
  provider, providerMode, providerAccountBindingId,
  eventId, rawBodyHash, authenticationHash,
  verifiedPayloadHash, receivedAt, result
}
```

`rawBodyHash` covers the exact received bytes. `authenticationHash` covers the relevant authenticated transport metadata. Retain only necessary transaction facts and hashes, not unrelated payer information or full callback bodies in logs.

For merchant events, define `verifiedPayloadHash` as the hash of a versioned canonical envelope of authenticated source business facts. Include account binding, notification identity, event type, merchant order number, payment ID, original provider payment time, original amount/currency, and any original refund identity/status/amount.

Exclude transport signatures, form ordering, transport retry times, encryption randomness, and locally computed aggregates. This definition supersedes raw-body hashing for merchant event deduplication only. Existing Stripe hashing remains unchanged.

An authenticated retry with the same event identity and business hash returns the existing processing result, even if its raw body or signature differs. Retain additional delivery evidence without overwriting the original event. The same identity with different business facts records a conflict and never replaces the first event.

Different notification IDs for the same financial transaction remain separate Events. The immutable payment binding and entitlement-source uniqueness prevent a second grant.

### 18.7 Normalize payment amounts and effective time

Produce the existing provider-independent financial facts.

A WeChat payment requires `TRANSACTION.SUCCESS`, `trade_state=SUCCESS`, the expected Native transaction type, an exact binding, and matching `amount.total` and CNY currency. Use `success_time` for successful `effectiveAt`.

An Alipay payment requires `TRADE_SUCCESS` or `TRADE_FINISHED`, an exact transaction binding, and matching `total_amount`. Use the authenticated `gmt_payment`, or authoritative successful-payment time from provider reconciliation. `TRADE_FINISHED` means a completed trade; it is not a refund signal.

Convert Alipay decimal amount strings to integer fen using decimal-string parsing and integer arithmetic. Reject signs, exponent notation, excess fractional digits, unsafe integers, and malformed amounts. Do not use floating-point multiplication, `buyer_pay_amount`, or net merchant receipts to compare against the Order's gross price. WeChat integer amounts must also be safe integers.

Interpret documented Alipay local datetime strings explicitly in the configured China time zone and convert to canonical UTC. Never use the Worker host's local timezone, callback receipt time, transaction creation time, or notification creation time as successful payment time.

Freeze the first supported successful payment time. Later events retain their original time evidence and reuse the canonical payment fact. Conflicting payment identities, amounts, currencies, or incompatible paid times require reconciliation.

### 18.8 Refund facts and unresolved financial states

Preserve the section 10.2 refund behavior. Pending refunds retain existing valid grants. Confirmed partial refunds suspend only the affected Order grant. Confirmed full refunds revoke that grant. Neither refund processing nor dispute processing changes other purchased windows or independent grant sources.

Add provider refund facts keyed by account, canonical payment, and unique refund identity. WeChat uses `refund_id`, with its `out_refund_no` binding. Alipay uses the original `out_request_no` and trade binding from an authenticated refund result or query.

Each confirmed refund amount is counted once. Successful refund identity, payment binding, currency, and amount are immutable. Store refund facts and their resulting aggregate under the same Order CAS used for the financial transition.

A WeChat refund notification's `amount.refund` describes that refund, not an order-wide cumulative total. `REFUND.SUCCESS` with a matching success status can contribute a confirmed refund fact. Processing, closed, and abnormal refund states do not prove returned money.

For Alipay, use authenticated refund API results or `alipay.trade.fastpay.refund.query` results that establish successful refund status and identity. An ambiguous notification `refund_fee` is not automatically a cumulative total. `TRADE_CLOSED` can describe unpaid closure or a completed full refund, so that status alone cannot determine either outcome.

Calculate confirmed totals from unique successful refund facts. Authoritative cumulative reconciliation can advance the total, but a cumulative total must not be added to its constituent refund rows. Confirmed totals never decrease or exceed the original amount. Missing coverage remains explicit.

Record refund facts that arrive before payment. A later paid event cannot revive a confirmed fully refunded, reversed, lost, or revoked source.

An unresolved financial conflict or ambiguous terminal/refund event blocks creation or restoration of a grant for that Order until complete authoritative reconciliation resolves it. Persist that blocking reason on the existing Event processing record. The store checks unresolved blocking Events when preparing a reducer input and supplies `completeness="needs_reconcile"` where required. Changes to this blocking state participate in Order revision/CAS. An unrelated informational event does not block grants.

This adapter rule preserves the pure reducer. Do not add provider names or provider status strings to its financial logic.

### 18.9 Atomic processing and acknowledgement

After authentication, persist the Event as `received` and its callback receipt. For the financial transition, use one D1 batch for the operation receipt and audit, Order and financial facts, refund-fact changes, entitlement and first exact `GrantScopeBinding`, membership revision effects, and final Event state.

Retain section 17.3's CHECK-based CAS and rollback behavior. Different Orders for one owner and exact benefit compete on the shared membership-scope revision. Reload and recalculate at most twice. Read the original operation key after an uncertain commit.

The provider's successful acknowledgement follows committed processing or a committed, explicitly classified reconciliation result. It does not follow an in-memory parse or an untracked `waitUntil` task.

Return WeChat's supported successful HTTP acknowledgement and Alipay's exact plain-text `success` for authenticated, durably accepted messages, including duplicate completed messages. Temporary database failures or unresolved CAS retries receive a retryable failure. Authentication or binding rejection cannot receive a success acknowledgement.

A durable `needs_reconcile` receipt means accepted for reconciliation, not paid or granted. The existing internal reconciliation route processes it with the original identities. Do not add a queue, scheduler, public financial override, or staff payment-confirmation shortcut.

Membership windows retain the existing same-benefit calculation. Course grants retain their frozen course scope and agreed time window. Neither method creates recurring billing, extends an old window, or grants future content outside the original exact scope.

### 18.10 Runtime implementation and configuration

Keep Cloudflare Workers and D1. Use Workers `fetch`, Web Crypto, and supported `node:crypto` operations. Do not add a Go or Java service solely to use a provider SDK.

Reuse the official Alipay SDK's relevant request canonicalization, website-payment signing, response verification, and `checkNotifySignV2` behavior. The inspected SDK source depends on `urllib`, creates an Agent at module load, and sends requests through that transport. Its complete package has not been verified in this Worker.

The selected bounded implementation is an attributed, pinned subset of those official MIT-licensed signing and verification routines, adapted to the existing Worker crypto APIs and `fetch`. Retain upstream source/version information and license text. Do not copy unrelated file, stream, certificate-download, or HTTP transport code. Do not implement RSA or AES algorithms.

WeChat uses its documented API v3 canonical messages with native RSA-SHA256 and AES-GCM. The current project already uses Web Crypto for verification and has `nodejs_compat`. Targeted Worker-runtime signed-fixture checks establish this adapter's compatibility.

Required configuration is limited to:

| Scope | Values |
|---|---|
| Common | Allowed payment methods, account binding IDs, provider modes, canonical callback origin, absolute checkout lifetime |
| Switches | Separate `checkoutEnabled`, `webhookEnabled`, `providerReadbackEnabled`, and isolated `trustedFixtureEnabled` |
| WeChat | `mchid`, bound `appid`, merchant API certificate serial, merchant private key, API v3 key, pinned WeChat public-key ID and public key |
| Alipay | `app_id`, seller ID, application private key, Alipay public key, `RSA2`, UTF-8, fixed allowed gateway, fixed notify and return URLs |

All switches default to disabled. There is no HTTP toggle. Fixture enablement requires isolated server configuration and fixture keys; request fields cannot enable it.

Disabling new checkout does not disable valid callbacks or already-authorized reconciliation for existing Orders. Keep historical account bindings and required verification keys while those Orders still need processing. Do not automatically reuse production keys in fixtures or sandbox.

### 18.11 Operator inputs and verification boundary

The human operator applies for the website payment products appropriate to the actual membership/course business. A personal or ordinary offline merchant collection code does not establish website API access.

For WeChat, the operator confirms ordinary direct-merchant Native permission, the merchant and AppID binding, the chosen public-key verification mode, and the website application requirements.

For Alipay, the operator confirms website-payment product permission, the application and seller identities, application readiness, and the public-key signing mode selected here. If the approved product requires a different integration mode, adapt only the affected provider boundary before activation.

The operator supplies approved products, prices, durations, exact benefits, terms, refund policy, and commercial content rights. Configure real HTTPS notification URLs and the fixed Alipay return URL. Payment and refund notifications must reach their claimed Worker routes without a login challenge or static fallback.

Local implementation uses real cryptographic operations with synthetic keys and trusted provider-shaped fixtures. It requires no real account or merchant private key. Local fixture success does not establish provider sandbox access, real callback delivery, commercial approval, deployment, or live collection.

## 19. Customer offer selection and authorized content discovery

### 19.1 Preserve existing authorities

This section adds read-only customer DTOs derived from existing approved Offers, frozen scopes, current grants, and restricted content. It adds no product kind, content manifest, grant, publication operation, or payment state.

Keep the closed public projections in sections 14 and 16, `UserOrderDTO`, and the private body DTOs in section 17 unchanged. A customer response is neither a content authority nor proof of payment or continued access.

All new routes require `currentSession`. Resolve the owner from that session. Accept no client user ID. Return `Cache-Control: private, no-store`, `Pragma: no-cache`, and `Vary: Cookie` on success and failure. Do not return an ETag, 304, public redirect, or permissive cross-origin response.

The new routes perform no writes. Existing order, checkout, and progress writes retain their exact-Origin, CSRF, idempotency, and ownership rules.

### 19.2 Offer quotes

Add these routes:

| Route | Response |
|---|---|
| `GET /api/offers?limit=…&cursor=…` | `{items: CustomerOfferQuote[], nextCursor}` |
| `GET /api/offers/:offerVersionId` | `CustomerOfferQuote` |

`CustomerOfferQuote` is closed:

```text
{
	offerVersionId,
	productKind: "membership"|"course",
	productId,
	title,
	summary,
	amountMinor,
	currency,
	durationDays?,
	updatePolicy: "fixed",
	renewalMode: "manual",
	termsVersion,
	termsText,
	refundPolicyVersion,
	refundPolicyText,
	termsSnapshotHash
}
```

Copy financial values, duration, product identity, and version identifiers from the exact verified Offer. Preserve the optional-field meaning of `durationDays`. For the methods in section 18, require the existing positive safe-integer CNY amount.

Use the same current sale-eligibility checks as order creation. Require the approved exact Offer, valid current runtime state, active sale window, matching Benefit and canonical scope, and existing commercial-use checks. A past approval, local candidate, or proposed price alone cannot qualify an Offer.

Human-readable title, summary, terms, and refund policy must come from explicitly approved customer copy. Maintain this copy as bounded server-side source configuration keyed by immutable Offer ID and its exact terms and refund-policy version identifiers. This configuration supplies presentation text only. It cannot supply or override price, scope, duration, approval, availability, or grants.

The configuration creates no new database entity or authoring system. Reuse an existing approved source if one is available. Otherwise, the production mapping starts empty. Missing approved copy excludes the affected Offer. Isolated fixtures may supply synthetic copy and Offers.

Text bound to an existing terms or refund-policy version is immutable. Substantive changes require new version identifiers and a new Offer. Retain old versioned text for existing purchases. Do not generate terms from a version identifier or promote the suggested prices in section 11.

`termsSnapshotHash` uses the existing section 17.2 formula over the verified Offer projection and scope hash. It is an opaque comparison value. Do not return the Offer projection, content scope, private content hashes, Benefit identifiers, provider configuration, or publication proof.

A quote does not reserve availability. Order creation revalidates the Offer and freezes its own values. The client sends only `{offerVersionId,paymentMethod}`. It never sends a price, scope, duration, or quoted terms as authority.

Before checkout, the client compares the returned Order's Offer ID, amount, currency, and `termsSnapshotHash` with the displayed quote. A mismatch stops checkout and refreshes the review state. It never automatically creates a replacement purchase.

Payment choices come only from `GET /api/payments/methods`. Map its returned method identifiers to customer labels. Do not display an enabled payment action for an absent method. A missing enabled method does not invent merchant readiness or require real credentials for local implementation.

The default response is an empty list when no approved sale Offer and customer copy exist. An enabled method alone does not create a product.

### 19.3 Discover currently authorized exact content

Add these routes:

| Route | Response |
|---|---|
| `GET /api/me/content?limit=…&cursor=…` | `{items: AuthorizedContentDescriptor[], nextCursor}` |
| `GET /api/me/content/:kind/:id/:revision` | One `AuthorizedContentDescriptor` |

The detail route accepts only `articleVersion`, `lessonVersion`, or `asset`, an existing valid ID, and a positive integer revision. It accepts no query parameters, hash supplied by the caller, `latest`, URL, object key, use, action, or owner.

The closed descriptor shapes are:

```text
ArticleDescriptor = {
	contentRef: ExactRef<articleVersion>,
	locale,
	title
}

LessonDescriptor = {
	contentRef: ExactRef<lessonVersion>,
	locale,
	title,
	courseRef: ExactRef<course>,
	lessonId
}

AssetDescriptor = {
	contentRef: ExactRef<asset>,
	locale,
	assetKind,
	alt,
	readUrl: string|null,
	downloadUrl: string|null
}

AuthorizedContentDescriptor =
	ArticleDescriptor|LessonDescriptor|AssetDescriptor
```

Return article and lesson descriptors only when the current user can read that exact text. Return an asset descriptor only when at least one exact supported action is currently available. Emit each media URL only for its permitted action, using the existing session-protected section 17.1 media route. Omit assets when the required media binding is absent. Permitted text remains discoverable.

Descriptors contain no body, full Course, other lesson list, scope, grant source, private license record, storage key, or publication proof. The Course reference on a lesson describes that lesson's validated binding. It authorizes no other lesson.

Authenticate before discovering candidate references. Enumerate candidates only through the session owner's existing grants and `GrantScopeBinding` records. Do not start from a global private-content catalogue.

For each returned descriptor:

1. Validate the exact grant origin, immutable binding, Benefit, canonical scope, scope hash, and requested resource/action.
2. For an Order origin, validate the frozen Offer and its scope. Current sale withdrawal alone does not cancel a valid old purchase.
3. Validate current grant status and server-time window. Suspended, revoked, not-yet-active, and expired grants contribute no access.
4. Resolve the complete exact resource and, for a lesson, its exact Course binding. Reuse Unit C's projection integrity, current resource state, bound and current license, and trusted-use checks.
5. Evaluate valid origins using the same Unit C authorization logic. One invalid origin does not invalidate an independent valid origin.
6. Return only descriptors permitted by that evaluation.

A coarse course ID, entitlement `activeNow`, public catalogue entry, Order status, or stored progress row is insufficient. Never resolve to the current content head or expand a fixed scope to future content.

For paid content, preserve the commercial-use checks for the relevant Order origin. Do not transfer one origin's permission or license context to another origin.

Discovery must not expose the payload hash or media URL of an inaccessible exact resource. For the detail route, absent, inaccessible, and unavailable content returns the same `404 CONTENT_UNAVAILABLE` response. Missing authentication returns `401 AUTH_REQUIRED`. Malformed input returns `400 INVALID_REQUEST`. Required service or integrity failures return `503 SERVICE_UNAVAILABLE`.

An invalid grant origin is excluded independently. A shared dependency failure or corrupt resource projection must not be reported as a successful empty result.

The list is a view of current access. Existing entitlement, Order, and progress history remains available under its existing contract after expiry or refund. Historical references do not authorize a read and are not used to populate the current-access list.

### 19.4 Pagination and changing access

Both list routes accept only `limit` and `cursor`, once each. Reuse the existing default of 24 and maximum of 100. Return closed `{items,nextCursor}` envelopes.

Use deterministic ordering and keyset pagination. Order quotes by `offerVersionId`. Order content by `(kind,id,revision)` with code-unit string ordering and numeric revisions. Deduplicate content by exact identity across valid grant origins.

Bind each cursor to the session owner, collection, and ordering boundary. Reject another owner's cursor or a cursor from another collection. A cursor grants no authority.

Content cursors may contain only the identity of a descriptor already returned to that owner, never a rejected resource, payload hash, scope, or private provider data. Revalidate current access on every page and detail request.

Bound SQL reads and filter candidates through owner-constrained joins before loading them. Do not read the complete entitlement or content table into the Worker. Continue candidate validation as needed to find permitted items and the next permitted item. Never return an unverified candidate merely to fill a page.

Pagination is not an access snapshot. A refund, expiry, rights update, or withdrawal can change later results. The subsequent body, media, or progress operation always repeats its existing authorization checks.

### 19.5 Client integration

Keep public catalogue and preview rendering independent of signed-in discovery. A public preview continues to use `PublicRef<lessonPreview>` and current public-publication evidence.

On a signed-in course or lesson page, resolve a paid lesson through `/api/me/content/lessonVersion/:id/:revision`. Match the returned exact lesson and Course binding to the selected catalogue identity before presenting that lesson as part of the catalogue. A mismatch does not select a newer lesson or another Course revision.

The personal content list also opens authorized material that has no current public catalogue entry. Private access must not depend on a learning-public receipt.

Use the discovered `contentRef` with the unchanged section 17.1 body route. Use the returned body DTO's exact lesson and Course references for progress. Restore progress only when its exact references match the loaded content. Do not transfer completion to a different version.

The existing private body DTO supplies authorized attachment references and URLs. The content list additionally supports explicitly granted standalone assets. Neither route implicitly grants attachments through a parent lesson.

A successful checkout return does not unlock content. Refresh the existing Order and current-access reads after a payment result. Only server-authorized discovery and content responses expose access.

Clear private in-memory results when the session changes or a read returns an access failure. Do not put private references, bodies, or media URLs in public JSON, static HTML output, shared caches, analytics, or persistent browser storage.

### 19.6 Implementation and evidence boundary

Implement customer discovery in separate customer-read modules after the current Unit C owner releases its exports. Reuse Unit C's resolver and authorization evaluator. If an internal helper must be exposed, the Unit C owner adds a thin export around the existing logic. Do not create a second interpretation of access rules.

Read sale eligibility through the released commerce/restricted-store interface. Preserve the financial store, reducer, Order snapshots, and section 18 adapters. Any missing shared export is a bounded integration dependency, not permission to edit another owner's active files.

Claim the new API paths and unknown descendants before static-asset fallback. Unsupported methods return private JSON errors.

Local fixtures can prove quote selection, both method presentations, verified fixture payment, exact content discovery, body/media access, and progress. Fixture success does not establish actual publication, merchant permission, live payment, or real product approval. Missing real business inputs leaves real sales disabled while local implementation proceeds.
## 20. 当前只卖 Skill 范围

最新人类方向优先于本文所有旧会员或课程销售描述。现有 `membership|course` 枚举、受限内容闭包、订单快照与 reducer 保留历史兼容；不能猜测增加 `skill` 枚举或把旧商品改名当成 Skill 支持。新建订单和 checkout 统一返回 `410 PRODUCT_SALES_CLOSED`，方法列表为空，旧类型不提供当前可购买报价；原订单读取、合法签名通知及退款处理保留。

免费课文采用现有 exact Course/Lesson/Catalog 与 whole-public-preview 发布链：只新增许可允许展示的完整正文版本，公开六篇，保留旧对象。网站不显示会员/课程购买入口，不把当前教程、案例或免费 Skill 放到收费门后。

Skill 销售要先确定确切 SkillVersion/Package、文件依赖闭包、hash 与许可，再定义实际付款后文件获取和退款/更新含义。这是尚未实施的新商业接入；本次只交付可审阅的[具体对象与边界](skill-commercial-scope-20261012.md)，不冒称已完成支付交付，也不把未定销售合同作为免费纠正的门槛。
