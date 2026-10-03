---
name: visual-prompt-director
description: Turn image requests, references, aesthetics, and generation misses into model-adapted prompts, or route illustrated image-generation tutorial writing and revision. Use for text-to-image, reference reconstruction, editing, cross-model adaptation, result correction, and teaching articles; select camera, lighting, medium, Krea 2, Qwen-Image-2.1, or tutorial subskills as needed.
---

# 视觉提示词导演

## 执行顺序

For an image-generation teaching article or its expansion or prose revision, load `vpd-image-tutorial` first. Its article format and requested teaching language govern the deliverable; the standalone prompt-only and bilingual-pair rules below do not replace an expressly requested tutorial. Load visual/model branches only for the examples that need them. A wording-only revision does not require new image generation.

1. Inherit the model, entry, reference-image purpose, successful parts, and non-language output preferences already confirmed in the current conversation. Use the bilingual default in the output contract unless the current user request explicitly asks for only one language. Proceed when missing information does not affect a natural-language prompt; ask one question only when a key input would change the task path.
2. 判断任务：角色设定板与人物一致性设计、新建单图、参考图可见特征复现、已有图编辑、结果诊断或跨模型迁移。反推只重建可见关系，不声称找回原始提示词。有生成结果时区分实际生成模型／入口与当前期望的目标模型：前者用于诊断样本，后者用于组织修改后的提示词；任一项未知则保留未知，不凭单次结果断言模型特性。
3. 内部建立最多 3–5 个成功锚点，标记主体、空间／遮挡、区域光色、表现形式、必须保留内容。每个锚点要能从生成图中检验。
   For reference reconstruction, treat these as lead anchors, not an omission limit; use the completeness audit in `vpd-visual-analysis` to retain every visible key relation.
4. 按下表选择必要子技能。通过运行环境提供的技能目录按精确 `name` 找到并读取其 `SKILL.md`；若目录不可搜索，在本仓库从本文件相邻路径读取 `../<name>/SKILL.md`。链接本身不自动执行。未找到时说明未加载该专门规则，仍用通用流程完成任务。
5. 先用视觉分支形成画面规范，再用模型分支检查入口和输出方式；参数与参考通道放在提示词之外。多模型共享同一视觉意图，不为了制造差别而改写画面。
   - Compose the final prompt from that same internal visual spec. State decisive spatial, scale, and occlusion relations first; keep supporting details subordinate and mention each once. Before delivery, audit in both directions: every required source relation, user-intent relation, and active output-contract default survives in the prompt, and every visual claim in the prompt is supported by visible evidence, explicit user intent, or a stated generation default. Remove unsupported anatomical explanations and duplicated wording.
   - For every person prompt, including new text-to-image and each grid panel, keep requested local body volume separate from overall build. Preserve an overall build specified by the user, a reference, or an established design. Fuller buttocks or thighs do not imply a heavier face, torso, waist, arms, or calves. If overall build is unspecified, infer neither generalized heaviness nor an extreme skinny default. Ground local size in the requested region's silhouette, projection, and proportions; keep fullness terms scoped to that region. For a thigh target, do not counter it by requiring all legs to remain thin. Use whole-body terms such as full-figured, voluptuous, or plus-size only when an overall fuller build is intended. Carry this distinction into both Chinese and English prompts.
6. For each image-prompt task, output a complete Chinese-and-English prompt pair for every explicitly requested model; when no model is specified, output one pair for the portable prompt. Put Chinese first, then English. Both versions must preserve the same visual specification, claims, and details. If the current user request explicitly asks for only one language, follow that request. Keep both prompts affirmative, omit negative prompts, and do not include exclusions such as “不要／避免／not ...” in the prompt body. Provide explanations, alternatives, negative prompts, or extra formats only when explicitly requested.
   Before delivery, scan the copyable prompt sentence by sentence for prohibitions or exclusions and rewrite each as an observable affirmative image state. Check the final prompt itself, not only the accompanying explanation.

## 路由表

| 条件 | 读取子技能 |
| --- | --- |
| Writing, expanding, or polishing an illustrated image-generation tutorial | `vpd-image-tutorial`; add visual and model branches only for examples that require them |
| 角色设定板、人物一致性设计或 IP 角色形象卡 | `vpd-character-sheet`；有参考图时同时读取 `vpd-visual-analysis` |
| A requested character-card layout matches the indexed 4+4 or three-view templates | `vpd-style-character-card`; also load `vpd-character-sheet` for character identity and continuity |
| Adult artistic or implied nudity, or requested concealment of an unclothed figure | `vpd-figure-art`, plus any relevant `vpd-visual-analysis`, `vpd-camera-composition`, `vpd-color-light`, and medium/style branch; it does not replace medium/style selection |
| Xiaohongshu-style crouching beauty or lifestyle selfie | `vpd-style-xiaohongshu-beauty-squat`; add separate model, analysis, camera, or lighting branches only when their conditions apply |
| 参考图、含糊审美或元素关系难辨 | `vpd-visual-analysis` |
| Photographic reference reconstruction, or any task where viewpoint, perspective, crop, or occlusion matters | `vpd-camera-composition` |
| 色相、冷暖、明暗、光线与氛围关键 | `vpd-color-light` |
| 摄影或电影剧照 | `vpd-style-photography` |
| 绘画、漫画、动画、水彩或概念艺术 | `vpd-style-illustration` |
| Vintage black-and-white halftone newspaper paper-cut portrait | `vpd-style-halftone-cutout` |
| 海报、文字版式、产品图或三维渲染 | `vpd-style-design` |
| 指定 Krea 2 | `vpd-model-krea-2` |
| 指定 Qwen-Image-2.1 | `vpd-model-qwen-image-2-1` |
| 已有输出跑偏、只修局部或迭代 | `vpd-result-diagnosis` |

一般只加载相关分支：一项任务类型 + 一个表现形式 + 一个模型；镜头与光色在重要时附加。未知模型保留视觉规范并核实官方入口，不推测专用语法。

## 输出契约

- For each requested model (or the portable prompt when no model is specified), put the complete Chinese prompt first and its complete English counterpart second, each in a separate copyable block. Keep language labels outside the blocks. Make both versions semantically equivalent and preserve every visual claim and detail across them. If the current request explicitly asks for only one language, provide only that language.
- Keep titles, theme labels, numbering, language labels, and explanations outside copyable prompt blocks, including code fences and writing blocks. Each block must contain only one complete prompt.
- Present the complete requested-language prompt or pair first. List aspect ratio, seed, reference images, masks, and other entry settings separately only when the entry is confirmed and the user needs them.
- For a requested young beauty portrait without a specified age, state a concrete adult age in the prompt; default to 25 years old. Default to East Asian when ethnicity is unspecified. Preserve explicit user choices and relevant visible reference traits; a chosen age is a generation target, not an age proven from a photo.
- 把强约束写成目标画面关系，例如“肩膀贴近下巴并遮住部分颈部”；把色彩写到区域，例如“天空浅雾蓝、云层杏桃、肤色暖粉”。
- 编辑时写“目标变化 + 必须保持的画面”，保持可操作的正向陈述。修正只改变一个主要维度，交付整合后的完整新提示词。
- 不虚构镜头毫米数、拍摄参数、模型能力或命中率。若无生成图可检验，称为待实测。
