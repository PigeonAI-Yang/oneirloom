# Oneirloom 0.3.0-preview continuity text exercises

This run records five actual child responses for cases 6 through 10 against the local Oneirloom source. The parent assignment supplied the criteria before response writing, so the run was unblinded. It records this child’s source-guided replies. It does not establish behavior in a fresh installed session, image quality, or repeatability.

The Oneirloom router was read before the shared interaction contract. Only the instructions selected by each current route were read. Source files remained read-only. The only created files are this report, its JSON record, and `fixture-arrow.svg`.

No image was generated or viewed. No network lookup, package, installation, or full test suite ran. The SVG was parsed and checked at the source level. It was not rendered.

## Case 6. Fictional paper-craft exhibition hall

### Input

> 写纸艺展厅概念提示词：前方入口、中间展示岛、后墙均可见，入口沿展示岛左侧通向后墙，空间是虚构的，无人物，不要工程图。

### Read paths, hashes, and reuse

| Source path | SHA-256 | Read and reuse |
|---|---|---|
| `skills/oneirloom/SKILL.md` | `ED0C782B7CB80A9A6F899DB9A2F4A0F845C7D55945C1D7342E8A82C902CF06F6` | Shared router read before case 6; reused unchanged in cases 6-10. |
| `skills/oneirloom/references/interaction-contract.md` | `6922D5220F34397A16CBABD8BA7F6E6987219183930CDC9CAB879BCDA2DDBD93` | Shared contract read before case 6; reused unchanged in cases 6-10. |
| `skills/oneirloom-space-conception/SKILL.md` | `1BA85762918369A9F8000A658C980B2371CFE02B8FA78BF57BD6DA900A3F39D6` | Selected route instruction for case 6; read once before drafting. |
| `skills/oneirloom-space-conception/references/spatial-relations.md` | `54FE573ED4047596541339F3B75B5DF1F3080493DECC55072BA279D24E4D2171` | Required space-conception reference for case 6; read once before drafting. |
| `skills/oneirloom-camera-composition/SKILL.md` | `AD3BB5F2BD1989CB0541A21227F91242BF5F045A25B7CC4E67AF3D03D1A038CB` | Required viewpoint instruction for case 6; read once before drafting. |
| `skills/oneirloom-craft-construction/SKILL.md` | `4475C789061DDE60BB84A0AE0CE85B5B728D6923E0090F5606BDF48C97ADBD73` | Selected craft route for case 6; reused unchanged in case 7. |
| `skills/oneirloom-craft-construction/references/construction.md` | `FF68D7DE26E4A114633C85AA2DFA15631CCE1EB16F81DE9D797313C8F3D166A8` | Required layered-paper reference for case 6; reused unchanged in case 7. |

### Actual response

**中文提示词**

```text
一幅虚构的纸艺展厅概念画面。空间结构先清楚呈现：展厅前方是一处敞开的入口，中间是展示岛，后方是完整可见的墙面。入口进入后有一条连续可见的通道，沿展示岛左侧经过并通向后墙；展示岛不遮住通道。入口、展示岛和后墙分别落在前景、中景、背景，展示岛是主要视觉焦点，后墙仍从岛台上方和两侧露出。画面采用层叠剪裁纸片搭成的立体布景，墙边、入口轮廓与岛台侧面露出纸层厚度，层片之间有细小间距和柔和接触阴影；地面和岛台下方可见折叠纸托片，支撑关系作为纸艺造型的一部分。相机位于入口外侧略高处，以斜向内看的三分之四视角拍摄，使入口、岛台左侧通道与后墙同时完整入画。无人物。画面呈现虚构的纸艺概念布景，不带尺寸标注、平面图符号或工程图布局。
```

**English prompt**

```text
A fictional paper-craft exhibition-hall concept image. Make the room layout clear first. Place an open entrance at the front, a display island in the middle, and the rear wall fully visible at the back. A continuous visible walkway leaves the entrance, passes along the island's left side, and leads toward the rear wall; the island does not block the path. Keep the entrance, island, and rear wall in the foreground, middle distance, and background, with the island as the main focal mass and the wall still visible above and on both sides of it. Build the scene as a dimensional set of layered cut-paper pieces. Show paper thickness along the wall edges, entrance outline, and island sides, with small gaps and soft contact shadows between layers. Folded paper tabs beneath the floor pieces and island show how the paper construction is supported. Place the camera just outside the entrance at a slightly raised three-quarter angle looking inward, so the entrance, left-side walkway, and rear wall all fit fully in frame. No people. Present a fictional paper-craft concept set without dimensions, floor-plan symbols, or engineering-drawing layout.
```

### Criteria

| Criterion | Result | Observed basis |
|---|---|---|
| Space is organized before camera placement. | PASS | The response first places the entrance, island, rear wall, depth layers, and route, then specifies the camera. |
| The entrance, island, rear wall, and route along the island's left side remain legible. | PASS | The continuous path begins at the entrance, passes the island's left side, and leads toward the visible rear wall; the island does not block it. |
| Paper construction and needed support are visible. | PASS | The prompt specifies cut-paper layers, exposed thickness, layer gaps, contact shadows, and folded support tabs. |
| The response makes no CAD, measured-plan, or buildability claim. | PASS | It calls the space fictional and omits dimensions and engineering-plan symbols without asserting physical feasibility. |

## Case 7. Localized product-background revision

### Input

> Setup accepted current prompt (user facts, not image): '蓝色密封“麦香”饼干袋居中，旁边三块圆饼干，标题“下午的小确幸”居上，暖黄色纸层背景；摄影结合纸艺布景；中文和英文提示词已确认，无需换风格。'
> New user: '只把背景改成深绿色，其余保持，只给完整修订提示词。'

### Read paths, hashes, and reuse

| Source path | SHA-256 | Read and reuse |
|---|---|---|
| `skills/oneirloom/SKILL.md` | `ED0C782B7CB80A9A6F899DB9A2F4A0F845C7D55945C1D7342E8A82C902CF06F6` | Shared router read before case 6; reused unchanged. |
| `skills/oneirloom/references/interaction-contract.md` | `6922D5220F34397A16CBABD8BA7F6E6987219183930CDC9CAB879BCDA2DDBD93` | Shared contract read before case 6; reused unchanged. |
| `skills/oneirloom-product-art-direction/SKILL.md` | `08698A16A11460075CBF5405B5CC25245F91B61A93C7C89AA8E9E0664F33EB5E` | Selected product route for case 7; read once before drafting. |
| `skills/oneirloom-color-light/SKILL.md` | `1511A8D759235CB09A3C4D94D0A5BD249E334BAF8679E50EF4D31B9A541DB2E3` | Selected regional color route for the requested background edit; read once before drafting. |
| `skills/oneirloom-color-light/references/material-response.md` | `FC1E1484950A99988D5A8FAB6F9B0CF4BF7F087F94BA212082F6400442E1E3BD` | Material-response reference for localized separation against the new background; read once before drafting. |
| `skills/oneirloom-craft-construction/SKILL.md` | `4475C789061DDE60BB84A0AE0CE85B5B728D6923E0090F5606BDF48C97ADBD73` | Read for case 6; reused unchanged because this setup retains paper-craft staging. |
| `skills/oneirloom-craft-construction/references/construction.md` | `FF68D7DE26E4A114633C85AA2DFA15631CCE1EB16F81DE9D797313C8F3D166A8` | Read for case 6; reused unchanged because this setup retains paper-craft staging. |

### Actual response

**中文提示词**

```text
画面中央是一袋蓝色密封的“麦香”饼干，包装上的“麦香”字样清楚可读；旁边摆放三块圆饼干。标题“下午的小确幸”位于画面上方，完整可读。背景改为深绿色的层叠纸艺布景，露出裁切纸边和纸层之间的轻柔阴影。整体采用摄影结合纸艺布景的呈现方式。只在蓝色包装和饼干与深绿色背景相接处加入轻微局部补光，让它们的轮廓保持清晰，其他构图与光线保持克制。
```

**English prompt**

```text
Center a sealed blue '麦香' biscuit bag in the frame, with '麦香' clearly readable on the package. Place three round biscuits beside it. Set the complete, legible headline '下午的小确幸' at the top of the composition. Change the background to a deep-green layered-paper set, with cut paper edges and soft shadows between layers. Use the confirmed combination of photographic product presentation and paper-craft staging. Add slight local fill only where the blue package and biscuits meet the deep-green background so their outlines remain clear. Keep the composition and the rest of the lighting restrained.
```

### Criteria

| Criterion | Result | Observed basis |
|---|---|---|
| All supplied product facts, exact copy, layout, and photographic-plus-paper-craft medium remain; only the background changes to deep green. | PASS | The full prompts retain the sealed blue 麦香 bag at center, three round biscuits beside it, the exact upper headline, and photography with layered-paper staging. The background is deep green. |
| No family exploration, result diagnosis, or style re-ideation appears. | PASS | The response gives one direct revision and no alternate directions, diagnosis, or style menu. |
| Any lighting response stays localized and necessary. | PASS | It adds slight local edge fill only where the product meets the deep-green background and does not introduce a new light direction or effect. |
| Both Chinese and English prompts are complete and standalone. | PASS | Each block repeats the subject, quantity, copy, placement, medium, new background, and local light adjustment. |

Text-only setup. No product image or prior full prompt was supplied or inspected.

## Case 8. Native navigation arrow SVG

### Input

> 给我一个实际SVG文件：24×24画布、黑色向右箭头，线宽2、圆端点，透明背景，用于界面导航；不要图片生成提示词。

### Read paths, hashes, and reuse

| Source path | SHA-256 | Read and reuse |
|---|---|---|
| `skills/oneirloom/SKILL.md` | `ED0C782B7CB80A9A6F899DB9A2F4A0F845C7D55945C1D7342E8A82C902CF06F6` | Shared router read before case 6; reused unchanged. |
| `skills/oneirloom/references/interaction-contract.md` | `6922D5220F34397A16CBABD8BA7F6E6987219183930CDC9CAB879BCDA2DDBD93` | Shared contract read before case 6; reused unchanged. |
| `skills/oneirloom-icon-design/SKILL.md` | `CC432AEBA14BAC9A2214FF8ACE48EBF80BD6C6CBCB4A6AC55020BCE031E19E70` | Selected icon-design route for case 8; read once before drafting. |
| `skills/oneirloom-style-design/SKILL.md` | `5DA1EB4C63A662FFD586E44FF128500120F4F5ED5F7827D381916424A8976B44` | Icon skill's required shared graphic-design process; read once before drafting. |

### Actual response

SVG 已创建：J:\PigeonYang\skills\oneirloom\work\visual-families-20261010\fixture-arrow.svg

### Source checks

The XML parser succeeded. The source has `width="24"`, `height="24"`, `viewBox="0 0 24 24"`, one geometric path, `stroke="#000000"`, `stroke-width="2"`, round line caps, and `fill="none"`. It has no rectangle background, image element, linked image, data URI, or base64 payload. No visual render was made.

### Criteria

| Criterion | Result | Observed basis |
|---|---|---|
| The SVG follows the native icon contract: 24 by 24 canvas, black right arrow, 2-unit stroke, round caps, and transparent background. | PASS | Source checks confirm width and height 24, viewBox 0 0 24 24, black stroke, stroke-width 2, round caps, right-pointing path geometry, fill none, and no background rectangle. |
| An actual geometric SVG fixture exists without embedded raster content. | PASS | fixture-arrow.svg parses as XML and contains exactly one path and no image element, data URI, base64 payload, or linked image. |
| XML and source contract checks passed. | PASS | The XML parser succeeded and every requested source attribute check returned true. |
| The report makes no visual-render claim. | PASS | No renderer or image viewer was used; visual_rendered is recorded as false. |
| The response returns the file path rather than an image prompt. | PASS | The actual response is one line with the saved SVG path and contains no generation prompt. |

## Case 9. Rainy-station emotional seed

### Input

> 我只记得雨夜车站灯下的感觉，说不清画面，像终于等到一个人又担心认错。先陪我想想，不用写提示词。

### Read paths, hashes, and reuse

| Source path | SHA-256 | Read and reuse |
|---|---|---|
| `skills/oneirloom/SKILL.md` | `ED0C782B7CB80A9A6F899DB9A2F4A0F845C7D55945C1D7342E8A82C902CF06F6` | Shared router read before case 6; reused unchanged. |
| `skills/oneirloom/references/interaction-contract.md` | `6922D5220F34397A16CBABD8BA7F6E6987219183930CDC9CAB879BCDA2DDBD93` | Shared contract read before case 6; reused unchanged. |
| `skills/oneirloom-dream-weaving/SKILL.md` | `EDA6C1668A0730737440FF243EA65D6D019644B654F60D48D0F2C49160964971` | Selected dream-weaving route for case 9; read once before drafting. Optional dialogue examples were not needed. |

### Actual response

也许先停在那个还不能确认的瞬间：雨夜车站的灯下，等候的人站在近处；远处一道身影走进站台，却还隔着雨幕和地面反光看不清脸。两人之间留着一段空站台，灯影沿湿地面伸向那道身影，像终于等到了，也让人担心认错。你更想让那道身影继续走近，还是停在灯光边缘？

### Criteria

| Criterion | Result | Observed basis |
|---|---|---|
| The unformed feeling routes to scene development without producing a prompt. | PASS | The reply proposes one scene relation in ordinary Chinese and does not present prompt blocks. |
| The reply offers a concrete, tentative visual relation in concise Chinese. | PASS | A nearby waiting figure faces a second, rain-obscured figure at the edge of the station light, with an empty wet platform between them. |
| The reply avoids invented biography, forced surreal style, bilingual output, generation, and an approval questionnaire. | PASS | It assigns no backstory or medium, asks one scene-shaping question, and does not mention prompt production or image generation. |

## Case 10. Portable text for an unknown image entry

### Input

> 用“未来画笔X”的未知入口写一幅无人街景提示词：夕阳下的砖墙和门边红自行车。暂时只要文本，没有参数资料，不需要替我查询。

### Read paths, hashes, and reuse

| Source path | SHA-256 | Read and reuse |
|---|---|---|
| `skills/oneirloom/SKILL.md` | `ED0C782B7CB80A9A6F899DB9A2F4A0F845C7D55945C1D7342E8A82C902CF06F6` | Shared router read before case 6; reused unchanged. It directs unknown entries to portable visual text. |
| `skills/oneirloom/references/interaction-contract.md` | `6922D5220F34397A16CBABD8BA7F6E6987219183930CDC9CAB879BCDA2DDBD93` | Shared contract read before case 6; reused unchanged. |

### Actual response

**中文提示词**

```text
夕阳下的一段无人街景。砖墙沿街延伸，墙上有一扇门，一辆红色自行车停在门边。夕阳的暖光落在砖墙、门和自行车上，并在街面投下自然的长影。画面把砖墙、门与自行车放在同一条连贯街景里，三者的位置清楚。
```

**English prompt**

```text
An empty street at sunset. A brick wall runs along the street, with a doorway in it and a red bicycle parked beside the door. Warm sunset light falls across the wall, doorway, and bicycle, casting natural long shadows onto the street. Show the wall, doorway, and bicycle together in one continuous street view, with their positions easy to read.
```

### Criteria

| Criterion | Result | Observed basis |
|---|---|---|
| The visual facts appear in complete Chinese and English prompts. | PASS | Both blocks include an empty sunset street, brick wall, door, and red bicycle beside the door in one coherent view. |
| The language remains portable across unknown image entries. | PASS | The prompts contain only ordinary visual descriptions and exact scene relations. |
| No unsupported model settings, native tokens, adapters, or network lookup are added. | PASS | No parameters, tokens, adapter claims, or external research appear. |
| Missing optional model details do not block the text-only request. | PASS | The response delivers both complete prompts without asking for model capability details. |

## Result

All 20 listed criteria passed across 5 cases. These are manual semantic checks against the supplied criteria, not an independent blind judgment. The cases exercise this child’s local source-guided response path only.
