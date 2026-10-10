# Oneirloom visual families 0.3.0-preview text exercises

Date: 2026-10-11

Outcome: Initial run, 4/5 cases met their criteria. Case-1 failed because its English prompt omitted the Chinese empty-street and no-people requirement. Correction run, 5/5 case outcomes pass, with cases 3-5 carried forward unchanged. The correction was manual and unblinded, with no new installed session.

The initial run contains five independent text-only fixture conversations routed through the local source skill. The root router and shared interaction contract were read once and reused unchanged. No images were viewed or generated, and no network, package, installation, or full-suite operation was run. This exercises source text behavior only; it does not prove a runtime installation or requested-model routing.

The original response blocks remain intact as initial-run evidence. The correction records new text only for cases 1 and 2; cases 3-5 are carried forward unchanged. This is a manual, unblinded correction, not a new installed session.

The architecture plan and ideal-answer sources were not read.

## Cases

### case-1

**Input**

> 写一个水彩街景提示词：雨后老街，一辆红色自行车靠在门边，无人物，只要提示词。

**Route rationale**

The user fixes watercolor as the medium and gives a formed street scene, so the router sends it directly to the illustration method. The watercolor checklist supplies pencil structure, transparent washes on damp paper, and paper-white edges; the visual-family index and styles catalog are not needed.

**Necessary limit**

No blocking input is missing. This is authored prompt text only; no image was generated or inspected.

**Actual assistant response (verbatim)**

**中文提示词**

```text
雨后的老街近景，一辆红色自行车靠在门边停放，车身与门口石板路接触自然，街巷空无一人。用轻铅笔线勾出门框、石板缝和自行车的车架轮廓，再以透明水彩薄洗铺开墙面与路面，水色沿微湿纸纹自然晕染。自行车的车架以饱和红色水彩明确突出，周围墙面、门和远处街巷用克制的灰蓝、浅赭与雨后淡灰分层。窗沿、车架受光边和几处石板反光保留纸白，纸张纤维与淡铅笔底稿隐约可见。自行车和门置于画面前部，街道向后收窄，用更淡、更松的水彩层次延伸；安静清凉的雨后氛围，手绘水彩插画。
```

**English prompt**

```text
A close view of an old street after rain, with a red bicycle resting beside a doorway and its wheels meeting the stone paving naturally. Use light pencil lines to define the door frame, paving seams, and bicycle frame, then build the walls and street with transparent watercolor washes that bloom into slightly damp paper grain. Make the bicycle frame a clear saturated red against restrained blue-gray, pale ochre, and rain-softened gray washes in the surroundings. Preserve paper white along the window edges, lit edges of the bicycle, and a few paving reflections; let paper fibers and a faint pencil underdrawing remain visible. Place the bicycle and doorway in the foreground and let the street narrow into the distance through paler, looser watercolor layers. Quiet, cool after-rain mood, hand-painted watercolor illustration.
```

**Criteria**

- **PASS** — Direct illustration route without family index or forced catalog: The route rationale and read paths contain the illustration method only, with no family index or catalog.
- **FAIL.** Watercolor wash, paper white, pencil structure, red bicycle, no people. The Chinese prompt says the alley is empty, but the English prompt omits an empty-street or no-people condition. The original bilingual prompts do not preserve every scene relation.

**Actual instruction files used**

- `skills/oneirloom/SKILL.md` (read once and reused unchanged)
- `skills/oneirloom/references/interaction-contract.md` (read once and reused unchanged)
- `skills/oneirloom-style-illustration/SKILL.md`

**Instruction source SHA-256**

- `skills/oneirloom/SKILL.md`: `ED0C782B7CB80A9A6F899DB9A2F4A0F845C7D55945C1D7342E8A82C902CF06F6`
- `skills/oneirloom/references/interaction-contract.md`: `6922D5220F34397A16CBABD8BA7F6E6987219183930CDC9CAB879BCDA2DDBD93`
- `skills/oneirloom-style-illustration/SKILL.md`: `5234052CB03D7C9DA89BBC0E91EFD2752B4FD812D69A39C105B76013E2762D41`

**Correction run.** The same fixture input and source instructions were used. The original response above stays verbatim as initial-run evidence and fails the second criterion. This correction is manual and unblinded, not a new installed session.

**Correction actual response (verbatim)**

**中文提示词**

```text
雨后的老街近景，一辆红色自行车靠在门边停放，车轮与门口石板路接触自然，街巷空无一人。用轻铅笔线勾出门框、石板缝和自行车的车架轮廓，再以透明水彩薄洗铺开墙面与路面，水色沿微湿纸纹自然晕染。自行车的车架以饱和红色水彩明确突出，周围墙面、门和远处街巷用克制的灰蓝、浅赭与雨后淡灰分层。窗沿、车架受光边和几处石板反光保留纸白，纸张纤维与淡铅笔底稿隐约可见。自行车和门置于画面前部，街道向后收窄，用更淡、更松的水彩层次延伸；安静清凉的雨后氛围，手绘水彩插画。
```

**English prompt**

```text
A close view of an old street after rain, with a red bicycle resting beside a doorway and its wheels meeting the stone paving naturally. The street is empty, with no people. Use light pencil lines to define the door frame, paving seams, and bicycle frame, then build the walls and street with transparent watercolor washes that bloom into slightly damp paper grain. Make the bicycle frame a clear saturated red against restrained blue-gray, pale ochre, and rain-softened gray washes in the surroundings. Preserve paper white along the window edges, lit edges of the bicycle, and a few paving reflections; let paper fibers and a faint pencil underdrawing remain visible. Place the bicycle and doorway in the foreground and let the street narrow into the distance through paler, looser watercolor layers. Quiet, cool after-rain mood, hand-painted watercolor illustration.
```

**Correction criteria**

- **PASS.** Direct illustration route without family index or forced catalog. The corrected route still uses the settled watercolor method without a family index or styles catalog.
- **PASS.** Watercolor wash, paper white, pencil structure, red bicycle, no people. The corrected Chinese and English prompts preserve the same rainy street, red bicycle by the doorway, wheel contact with the stone paving, empty street, and watercolor treatment.

### case-2

**Input**

> 场景已经清楚：雨后老街、门边红色自行车，无人物。想拓展视觉做法，你给我几个能看出差别的方向，先不要写最终提示词。

**Route rationale**

This is a formed scene with an open visual direction, so the optional family index is selected. Only the Craft, Digital, and Graphic notes were read to compare distinct mechanisms; the scene is not an unformed fragment, and no final medium has been chosen.

**Necessary limit**

No blocking limitation. The final prompt is deliberately omitted because the user asked to stay at the direction stage.

**Actual assistant response (verbatim)**

场景已经成形，可以沿不同制作机制拓展：

- **叠层纸浮雕**：把门面、石板路和远处街巷拆成前后错开的裁纸层，用外露切边、层间间距和接触阴影做出可触摸的纵深；红色自行车作为前层主体。
- **数字微缩场景**：把街道组织成统一的小型三维布景，让门、路面和巷道体块连贯，车轮清楚落在地面上；雨后水迹以贴地的细窄反光表现，重点是体块连接和空间深度。
- **图形构成海报**：把街巷压缩成几块平整色面与方向性线条，用大面积留白把视线引向唯一的红色自行车；重点由色块层级和形状关系建立。

The scene is already formed, so its visual directions can differ by construction mechanism:

- **Layered paper relief:** Split the storefront, paving, and receding alley into offset cut-paper planes. Exposed cut edges, small gaps between layers, and contact shadows create tactile depth, with the red bicycle as the foreground subject.
- **Digital miniature:** Organize the street as one coherent small-scale 3D setting, with connected volumes for the doorway, road, and alley and the bicycle wheels clearly resting on the ground. Show rain traces as narrow reflections close to the paving; the emphasis is on connected volumes and spatial depth.
- **Graphic poster composition:** Reduce the street to a few flat color fields and directional lines, using generous negative space to lead the eye to the single red bicycle. Let color hierarchy and shape relationships carry the composition.

我先停在方向层，不展开成最终提示词。
I'll stay at the direction level and leave the final prompt unwritten.

**Criteria**

- **PASS.** Optional family exploration with mechanisms beyond default photography or illustration. The response offers layered-paper construction, digital miniature geometry, and graphic color-field hierarchy.
- **PASS.** No forced dream weaving or all-ten-family catalogue. The scene is treated as already formed; only three relevant family notes are read and used.
- **PASS.** Useful differences without a forced count or approval gate. Each option names a different visual mechanism and its effect; the response does not require a selection or approval before stopping.

**Actual instruction files used**

- `skills/oneirloom/SKILL.md` (read once and reused unchanged)
- `skills/oneirloom/references/interaction-contract.md` (read once and reused unchanged)
- `skills/oneirloom/references/visual-families/index.md`
- `skills/oneirloom/references/visual-families/craft.md`
- `skills/oneirloom/references/visual-families/digital.md`
- `skills/oneirloom/references/visual-families/graphic.md`

**Instruction source SHA-256**

- `skills/oneirloom/SKILL.md`: `ED0C782B7CB80A9A6F899DB9A2F4A0F845C7D55945C1D7342E8A82C902CF06F6`
- `skills/oneirloom/references/interaction-contract.md`: `6922D5220F34397A16CBABD8BA7F6E6987219183930CDC9CAB879BCDA2DDBD93`
- `skills/oneirloom/references/visual-families/index.md`: `8DC66E7FB90C98DAAE774020456B6BE9C0C13DD8F412CEB526A1731AF033BECB`
- `skills/oneirloom/references/visual-families/craft.md`: `170D8685973D9187DD15AE65D443E81521DB5A1E5C75FC7FA09BD91DCFBFD938`
- `skills/oneirloom/references/visual-families/digital.md`: `4084E63DF51FC70BFC4B904E9BD40F41DB07AB17DBA09973831F575AAD2D353F`
- `skills/oneirloom/references/visual-families/graphic.md`: `3578EE152051D693328FCC841A2F5D4A4FFE86D6E35AAB820ABF6062893672E1`

**Correction run.** The same fixture input and source reads were used. The original response above stays verbatim as initial-run evidence. The correction removes its unrequested English translation. The original direction criteria remain PASS, and language cleanup is outside those criteria. This is a manual, unblinded correction, not a new installed session.

**Correction actual response (verbatim)**

场景已经成形，可以沿不同制作机制拓展：

- **叠层纸浮雕**：把门面、石板路和远处街巷拆成前后错开的裁纸层，用外露切边、层间间距和接触阴影做出可触摸的纵深；红色自行车作为前层主体。
- **数字微缩场景**：把街道组织成统一的小型三维布景，让门、路面和巷道体块连贯，车轮清楚落在地面上；雨后水迹以贴地的细窄反光表现，重点是体块连接和空间深度。
- **图形构成海报**：把街巷压缩成几块平整色面与方向性线条，用大面积留白把视线引向唯一的红色自行车；重点由色块层级和形状关系建立。

我先停在方向层，不展开成最终提示词。

**Correction criteria**

- **PASS** — Optional family exploration with mechanisms beyond default photography or illustration: The response offers layered-paper construction, digital miniature geometry, and graphic color-field hierarchy.
- **PASS** — No forced dream weaving or all-ten-family catalogue: The scene is treated as already formed; only three relevant family notes are read and used.
- **PASS** — Useful differences without a forced count or approval gate: Each option names a different visual mechanism and its effect; the response does not require a selection or approval before stopping.

### case-3

**Input**

> 给这款真实饼干做纸构造海报，只写提示词。已知事实：一袋蓝色密封包装，正面只有我提供的品牌字样“麦香”；旁边三块圆形饼干。主文案“下午的小确幸”。纸构造用在布景，产品外观保持这些事实，不补成分或功效。

**Route rationale**

This is a real-product poster with explicit paper scenery. The product method is read first; the composed-graphic method owns poster hierarchy and exact copy, while craft construction and its layered-paper mechanism guide the staging. Product facts come only from the text fixture; no imagery was provided or inspected.

**Necessary limit**

No blocking input is missing. The result is ungenerated and visually unverified; product facts remain text-supplied.

**Actual assistant response (verbatim)**

**中文提示词**

```text
竖幅纸构造海报中，一袋蓝色密封包装的饼干完整陈列在画面中央，包装正面朝向观看者，正面唯一的品牌字样清晰写作“麦香”。包装旁摆放三块彼此分开的圆形饼干。主文案“下午的小确幸”以准确清晰的中文排在上方；海报的文字层只包含“麦香”和“下午的小确幸”，其余区域保留无字留白。

纸构造只用于布景：几片有厚度的彩纸裁片搭出简洁的层叠背景和承托台面，前后遮挡关系明确，露出的切边、轻微错层和接触阴影可见。蓝色密封包装保持完整的袋装外观，与纸片布景清楚区分；三块圆形饼干作为独立实物放在包装一侧。标题、包装和饼干形成清楚的视觉层级，光线柔和，画面呈静物海报质感。
```

**English prompt**

```text
Create a vertical paper-construction poster with one blue sealed biscuit bag displayed intact at the center, its front facing the viewer and its only brand wording clearly reading “麦香”. Place three separate round biscuits beside the package. Set the headline “下午的小确幸” clearly across the upper area in its exact Chinese wording; the poster contains only “麦香” and “下午的小确幸” as text, with the remaining areas left open and unlettered.

Use paper construction only for the staging: several thick cut-paper pieces form a simple layered backdrop and display surface, with clear front-to-back overlap, exposed cut edges, slight layer offsets, and visible contact shadows. Keep the blue sealed bag intact and visually distinct from the paper scenery; show the three round biscuits as separate real objects beside it. Give the headline, package, and biscuits a clear visual hierarchy, with soft light and a still-life poster finish.
```

**Criteria**

- **PASS** — Product facts, graphic design, and craft integrated in one prompt per language: Each complete prompt combines the package, cookies, exact poster title, layout, and layered paper staging.
- **PASS** — Real food and package facts preserved; paper limited to scenery: Both prompts keep a blue sealed bag and three separate round biscuits as the product, with cut paper used only for backdrop and display surface.
- **PASS** — No invented product claim or copy; Chinese copy literal in both languages: The only text specified is the exact supplied brand “麦香” and title “下午的小确幸”; no ingredient, benefit, or other copy is added.

**Actual instruction files used**

- `skills/oneirloom/SKILL.md` (read once and reused unchanged)
- `skills/oneirloom/references/interaction-contract.md` (read once and reused unchanged)
- `skills/oneirloom-product-art-direction/SKILL.md`
- `skills/oneirloom-style-design/SKILL.md`
- `skills/oneirloom-craft-construction/SKILL.md`
- `skills/oneirloom-craft-construction/references/construction.md`

**Instruction source SHA-256**

- `skills/oneirloom/SKILL.md`: `ED0C782B7CB80A9A6F899DB9A2F4A0F845C7D55945C1D7342E8A82C902CF06F6`
- `skills/oneirloom/references/interaction-contract.md`: `6922D5220F34397A16CBABD8BA7F6E6987219183930CDC9CAB879BCDA2DDBD93`
- `skills/oneirloom-product-art-direction/SKILL.md`: `08698A16A11460075CBF5405B5CC25245F91B61A93C7C89AA8E9E0664F33EB5E`
- `skills/oneirloom-style-design/SKILL.md`: `5DA1EB4C63A662FFD586E44FF128500120F4F5ED5F7827D381916424A8976B44`
- `skills/oneirloom-craft-construction/SKILL.md`: `4475C789061DDE60BB84A0AE0CE85B5B728D6923E0090F5606BDF48C97ADBD73`
- `skills/oneirloom-craft-construction/references/construction.md`: `FF68D7DE26E4A114633C85AA2DFA15631CCE1EB16F81DE9D797313C8F3D166A8`

### case-4

**Input**

> 把我的头像描述转为拼豆视觉样机，只写提示词：人物侧脸朝左，黑色短发，左耳银色小耳钉，深蓝上衣。以上文字就是本次内容依据，无需查看图片。接近俯拍的实体展示。

**Route rationale**

A person-based fuse-bead mockup selects craft construction, person defaults, the construction reference, and the matching fuse-bead template. The user explicitly supplies text as the only content basis, so the response describes only those traits and does not claim an image input or inspection.

**Necessary limit**

No blocking input is missing. No source image was provided or inspected; the output is a visual mockup prompt, not a counted pattern or verified build plan.

**Actual assistant response (verbatim)**

**中文提示词**

```text
制作一件头像拼豆视觉样机：人物呈朝画面左侧的侧脸，黑色短发，左耳佩戴一枚小型银色耳钉，穿深蓝上衣；画面显示头部与肩部，侧脸轮廓、发型、耳钉和衣服色块清楚可辨。将头像表现为平面拼豆作品：均匀的短圆柱塑料豆立在同一平面并按规则行列排列，每个被图案占用的网格单元放一颗豆；每颗豆都有清楚的中央圆孔、圆润环形顶面和可见侧壁。用单颗纯色豆的排列表现黑发、面部色块、银色耳钉和深蓝上衣，外轮廓沿网格形成细小阶梯边。作品为单豆厚薄片，外沿以一圈奶油白拼豆收边，平放在温暖的象牙白哑光台面上。以接近垂直俯拍的展示视角完整呈现作品并留出周围空间；头像图案本身仍保持朝左的侧脸，俯拍只描述实体拼豆作品的展示角度。柔光在豆粒边缘形成轻微塑料高光，孔内呈自然暗部，豆间和作品边缘下方有柔和接触阴影。
```

**English prompt**

```text
Create a fuse-bead avatar mockup of a head-and-shoulders figure in left-facing profile, with short black hair, one small silver stud in the left ear, and a deep navy top. Keep the profile silhouette, hairstyle, earring, and clothing color blocks clearly recognizable. Build the flat fuse-bead artwork from uniformly sized short cylindrical plastic beads standing in one shared plane and aligned in regular rows and columns, with one bead in each occupied grid cell. Give every bead a visible central hole, rounded ring-shaped top, and discernible sidewall. Use solid-colored beads to show the black hair, facial color areas, silver earring, and deep navy top; let the outer silhouette step along the grid. Make the artwork a single-bead-thick piece with a cream-white bead border, resting on a warm ivory matte surface. Show the complete piece with space around it from a near-vertical overhead display view; the avatar motif itself remains a left-facing profile, while overhead describes only how the physical piece is displayed. Soft light creates subtle plastic highlights on bead rims, natural darkness inside the holes, and gentle contact shadows between beads and beneath the edge of the piece.
```

**Criteria**

- **PASS** — Craft construction and matching template: The prompt includes central holes, regular grid with one bead per occupied cell, one-bead thickness, stepped edges, and contact shadows.
- **PASS** — Profile direction distinct from physical display view: The avatar remains left-facing while near-overhead describes only the display view of the bead sheet.
- **PASS** — Text-only provenance with no false image or build claims: The recorded prompt introduces no reference-image token or inspection statement and gives no bead count or buildability claim.

**Actual instruction files used**

- `skills/oneirloom/SKILL.md` (read once and reused unchanged)
- `skills/oneirloom/references/interaction-contract.md` (read once and reused unchanged)
- `skills/oneirloom-craft-construction/SKILL.md`
- `skills/oneirloom-craft-construction/references/construction.md`
- `skills/oneirloom/references/person-prompts.md`
- `skills/oneirloom-craft-construction/templates/index.md`
- `skills/oneirloom-craft-construction/templates/fuse-bead/template.md`

**Instruction source SHA-256**

- `skills/oneirloom/SKILL.md`: `ED0C782B7CB80A9A6F899DB9A2F4A0F845C7D55945C1D7342E8A82C902CF06F6`
- `skills/oneirloom/references/interaction-contract.md`: `6922D5220F34397A16CBABD8BA7F6E6987219183930CDC9CAB879BCDA2DDBD93`
- `skills/oneirloom-craft-construction/SKILL.md`: `4475C789061DDE60BB84A0AE0CE85B5B728D6923E0090F5606BDF48C97ADBD73`
- `skills/oneirloom-craft-construction/references/construction.md`: `FF68D7DE26E4A114633C85AA2DFA15631CCE1EB16F81DE9D797313C8F3D166A8`
- `skills/oneirloom/references/person-prompts.md`: `A58FA4E477A1D81C2333D9040B12060DBD8ADBB75A512220221CF147280D43FC`
- `skills/oneirloom-craft-construction/templates/index.md`: `3AFCBA820CD934537429197AFDA9B6FB93F24818288B1F1B9E9B185A19057D75`
- `skills/oneirloom-craft-construction/templates/fuse-bead/template.md`: `8306772D9F1F1A57E3CF3B7B543888720A394007FF6978C0E82EC403C1267D86`

### case-5

**Input**

> 写透明分层的虚构香水瓶外形概念提示词。不是在售产品：连续透明外壳、窄瓶颈，壳内两层半透明弧形薄片；放在素色底座上。只要视觉概念，暂不建模。

**Route rationale**

This is a fictional object-form concept, so digital form owns silhouette, continuity, and layer order. Its form reference includes the relevant fictional layered-perfume example; color and light plus material response supply supported transparency, transmission, refraction, and reflection cues. No real-product art direction or modeling route is needed.

**Necessary limit**

No blocking input is missing. The deliverable is prompt text for a visual concept only; no render or editable model was produced.

**Actual assistant response (verbatim)**

**中文提示词**

```text
虚构香水瓶外形的三维视觉概念渲染：一只连续完整的透明外壳由窄瓶颈平顺过渡至肩部和瓶身，整体保持单一连通的外轮廓。壳体内部悬置两层半透明弧形薄片，沿瓶身内侧弧度展开，分别处在不同的前后深度；两片薄层的边界清楚可见，并始终位于透明外壳之内。瓶体直立放在素色简洁底座上，背景干净，使窄瓶颈、连续外壳、双层弧片和底座接触关系一眼可辨。

以中性柔光表现材质：透明外壳边缘出现窄而清楚的高光，壳壁厚度处带有轻微折射和明暗变化，透过前壁仍可辨认后层弧片；两片薄层让光线柔和透过，同时保留清晰的弧线轮廓，表面反射克制。高光、透射和反射沿外壳的连续曲面保持一致，画面突出几何连续性、连接关系和前后层次。
```

**English prompt**

```text
Create a 3D visual concept render of a fictional perfume-bottle form. One continuous clear outer shell transitions smoothly from a narrow neck through the shoulder into the body, maintaining a single connected outer silhouette. Inside the shell, suspend two translucent curved thin sheets that follow the body's inner curve at distinct front-to-back depths. Keep both sheet boundaries visible and contained within the transparent shell. Stand the bottle on a plain, simple display plinth against a clean background so the narrow neck, continuous shell, two inner layers, and contact with the base are easy to read.

Use neutral soft light to show the materials: narrow, clear highlights trace the shell edges; slight refraction and value shifts at the wall reveal its thickness, while the rear sheet remains visible through the front wall. Let light pass softly through both sheets while preserving their curved outlines, with restrained surface reflections. Keep highlights, transmission, and reflections consistent along the shell's continuous surface, emphasizing geometric continuity, connections, and front-to-back layering.
```

**Criteria**

- **PASS** — Geometry, continuous shell, narrow neck, two inner curved layers, plain base: Both prompts state one connected outer contour, a narrow neck, two translucent sheets at distinct depths inside the shell, and a plain display plinth.
- **PASS** — Supported material response: The prompts localize edge highlights, transmission through the shell, visible rear layer, slight refraction/value shifts, and restrained reflection.
- **PASS** — Fictional concept stays out of product facts, manufacturing, or editable-model claims: The response identifies a fictional form concept and makes no retail-product, manufacturing, or actual-model claim.

**Actual instruction files used**

- `skills/oneirloom/SKILL.md` (read once and reused unchanged)
- `skills/oneirloom/references/interaction-contract.md` (read once and reused unchanged)
- `skills/oneirloom-digital-form/SKILL.md`
- `skills/oneirloom-digital-form/references/form-and-transformation.md`
- `skills/oneirloom-color-light/SKILL.md`
- `skills/oneirloom-color-light/references/material-response.md`

**Instruction source SHA-256**

- `skills/oneirloom/SKILL.md`: `ED0C782B7CB80A9A6F899DB9A2F4A0F845C7D55945C1D7342E8A82C902CF06F6`
- `skills/oneirloom/references/interaction-contract.md`: `6922D5220F34397A16CBABD8BA7F6E6987219183930CDC9CAB879BCDA2DDBD93`
- `skills/oneirloom-digital-form/SKILL.md`: `1B044AD248DAE3E426519A5522A0C202A48EEF6928B2BA5DF1B0AE24F635DC37`
- `skills/oneirloom-digital-form/references/form-and-transformation.md`: `B721C6B83C6FCB3B5A2AAD2C8475C3B60BC283976CA1FAEC7ECF000056D1F2BF`
- `skills/oneirloom-color-light/SKILL.md`: `1511A8D759235CB09A3C4D94D0A5BD249E334BAF8679E50EF4D31B9A541DB2E3`
- `skills/oneirloom-color-light/references/material-response.md`: `FC1E1484950A99988D5A8FAB6F9B0CF4BF7F087F94BA212082F6400442E1E3BD`

## Execution context

Global/project execution instructions read: `J:/PigeonYang/AGENTS.md`, `J:/PigeonYang/pigeonstack/AGENTS.md`, `J:/PigeonYang/pigeonstack/pstack/CODEX.md`, `J:/PigeonYang/pigeonstack/pstack/MODELS.md`, and `PROJECT-FILES.md`. These are process context, not additional Oneirloom fixture routes.

## Source hashes

- `skills/oneirloom/SKILL.md`: `ED0C782B7CB80A9A6F899DB9A2F4A0F845C7D55945C1D7342E8A82C902CF06F6`
- `skills/oneirloom/references/interaction-contract.md`: `6922D5220F34397A16CBABD8BA7F6E6987219183930CDC9CAB879BCDA2DDBD93`
- `skills/oneirloom-style-illustration/SKILL.md`: `5234052CB03D7C9DA89BBC0E91EFD2752B4FD812D69A39C105B76013E2762D41`
- `skills/oneirloom/references/visual-families/index.md`: `8DC66E7FB90C98DAAE774020456B6BE9C0C13DD8F412CEB526A1731AF033BECB`
- `skills/oneirloom/references/visual-families/craft.md`: `170D8685973D9187DD15AE65D443E81521DB5A1E5C75FC7FA09BD91DCFBFD938`
- `skills/oneirloom/references/visual-families/digital.md`: `4084E63DF51FC70BFC4B904E9BD40F41DB07AB17DBA09973831F575AAD2D353F`
- `skills/oneirloom/references/visual-families/graphic.md`: `3578EE152051D693328FCC841A2F5D4A4FFE86D6E35AAB820ABF6062893672E1`
- `skills/oneirloom-product-art-direction/SKILL.md`: `08698A16A11460075CBF5405B5CC25245F91B61A93C7C89AA8E9E0664F33EB5E`
- `skills/oneirloom-style-design/SKILL.md`: `5DA1EB4C63A662FFD586E44FF128500120F4F5ED5F7827D381916424A8976B44`
- `skills/oneirloom-craft-construction/SKILL.md`: `4475C789061DDE60BB84A0AE0CE85B5B728D6923E0090F5606BDF48C97ADBD73`
- `skills/oneirloom-craft-construction/references/construction.md`: `FF68D7DE26E4A114633C85AA2DFA15631CCE1EB16F81DE9D797313C8F3D166A8`
- `skills/oneirloom/references/person-prompts.md`: `A58FA4E477A1D81C2333D9040B12060DBD8ADBB75A512220221CF147280D43FC`
- `skills/oneirloom-craft-construction/templates/index.md`: `3AFCBA820CD934537429197AFDA9B6FB93F24818288B1F1B9E9B185A19057D75`
- `skills/oneirloom-craft-construction/templates/fuse-bead/template.md`: `8306772D9F1F1A57E3CF3B7B543888720A394007FF6978C0E82EC403C1267D86`
- `skills/oneirloom-digital-form/SKILL.md`: `1B044AD248DAE3E426519A5522A0C202A48EEF6928B2BA5DF1B0AE24F635DC37`
- `skills/oneirloom-digital-form/references/form-and-transformation.md`: `B721C6B83C6FCB3B5A2AAD2C8475C3B60BC283976CA1FAEC7ECF000056D1F2BF`
- `skills/oneirloom-color-light/SKILL.md`: `1511A8D759235CB09A3C4D94D0A5BD249E334BAF8679E50EF4D31B9A541DB2E3`
- `skills/oneirloom-color-light/references/material-response.md`: `FC1E1484950A99988D5A8FAB6F9B0CF4BF7F087F94BA212082F6400442E1E3BD`
