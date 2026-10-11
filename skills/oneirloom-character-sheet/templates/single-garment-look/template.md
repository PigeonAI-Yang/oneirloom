# Single-garment product display

## Record

- **ID:** `fashion.single-garment-look` (stable recipe ID)
- **Reference mechanism:** `fashion.single-garment-merchandising` ([fashion styling](../../references/fashion-styling.md))
- **Owner:** `oneirloom-character-sheet`
- **Tags:** F (Fashion), P (Photography), T (Product)
- **Synonyms (EN):** single-garment product display; one-item apparel catalog image
- **Synonyms (ZH):** 单件服装商品展示；单件服装商品图
- **Authored:** 2026-10-11

## Selection

Use for one static merchant image in which one real garment is the item being sold. This recipe contributes garment facts and visibility checks; it does not require a character sheet, several outfits, a fixed pose, or a particular display mode. It is an image-presentation recipe, not garment patternmaking, cutting, or manufacturing guidance. For an actual garment reference, establish observed facts with [visual analysis](../../../oneirloom-visual-analysis/SKILL.md) and use [product art direction](../../../oneirloom-product-art-direction/SKILL.md). Choose the requested photographic treatment through the [photography method](../../../oneirloom-style-photography/SKILL.md).

## Product facts and presentation choices

Keep these categories separate when resolving the prompt:

- **Product facts:** The garment's category and source-supported visible silhouette, neckline, openings and closures, hem, visible surface appearance, and legible marks or logos. Treat user-supplied specifications as user-stated facts with their source. A visible texture does not establish fiber content or manufacturing method.
- **Unknowns:** A hidden back, lining, interior construction, unseen closure, exact material composition, and unreadable brand text remain unknown unless a source supplies them. If the requested view depends on one of them, ask for the smallest useful reference or mark an authorized design inference as such.
- **Presentation choices:** Display mode, camera angle, body crop, model or mannequin, pose, accessories, background, light, and optional copy can change around the garment. Do not let a styling change silently redesign the item.

One view of one garment is the default. Do not add a six-look board, variants, comparison panels, or extra products unless requested. Keep the garment large enough to read. A full silhouette is useful when length or the whole hem is part of the selling brief. A body crop is optional when it retains the specific product features that matter; move the crop or camera if it cuts through a relevant neckline, closure, sleeve, pocket, or hem. Keep the named selling feature visible and unobstructed by hair, hands, jewelry, layers, or props. If another element covers it, move or remove that element or choose a clearer view; do not alter or omit the garment to preserve the obstruction.

## Conditional photography route

Use the [photography template index](../../../oneirloom-style-photography/templates/index.md) only when a listed scene or pose matches the request. Follow that template's pose and scene method there, then add this recipe's garment facts and visibility constraints. This recipe defines no new pose method and does not import styling defaults from an unrelated template. When no indexed template fits, compose from the photography checklist.

## Complete prompt scaffold

Resolve every bracketed slot from the selling brief, the supplied image, confirmed product specifications, or the selected photography route. Use only source-supported garment details and confirmed specifications. Keep unknown material, marks, and hidden construction outside the prompt and frame. Resolve the display mode, view, crop, pose, styling, background, light, copy, and photographic treatment before writing the image prompt. Describe the visible mark and wording at their observed placement, or describe a clean unlettered surface when the source shows an unmarked garment.

### 中文

```text
制作一张{已选画幅规格}的单件服装商品摄影图，呈现{已选摄影表现}。画面以一件{服装类别与商品身份}为唯一主商品，采用{已选展示方式}，呈现{已选视角}。商品位于{画面位置}，占据{主体比例}；背景为{背景与环境}，光线呈现{光线方向、明暗与阴影关系}。

服装呈现{可见轮廓与衣长}、{领口}、{袖型与肩部结构}、{可见开口与闭合方式}、{下摆}以及{参考中可见的表面纹理与颜色}。商品正面呈现{已确认的正面表面状态}。

{本次销售重点}与{还需展示的结构}在画面中完整可见。画面采用{已选取景范围}，裁切边界位于{裁切位置}。展示主体以{已选姿态与陈列关系}呈现，销售重点周围保留清晰留白，商品特征易于辨认。

画面聚焦一件服装和一个主视角，服装轮廓清晰，镜头透视连贯，摄影效果为{已选摄影表现}。
```

### English

```text
Create one {selected image format} static apparel product photograph with {selected photographic treatment}. The image presents one {garment category and product identity} as its featured item in {selected display mode} from {selected view}. Position the garment at {frame position} and {subject scale}. Set the scene against {background and setting}, with {light direction, contrast, and shadow relationships}.

The garment shows its {visible silhouette and length}, {neckline}, {sleeve and shoulder construction}, {visible openings and closures}, {hem}, and {reference-visible surface texture and colors}. Its front presents {the resolved front-surface state}.

The {selling feature for this image} and {other structure to be shown} remain fully visible and easy to read. The selected framing shows {the resolved garment view}, with boundaries at {crop position}. The display presents {the resolved pose and arrangement}, with clear open space around the selling feature so the garment details remain easy to read.

One garment and one main view form a readable silhouette with coherent camera perspective. The photograph has {the selected photographic treatment}.
```

## Original text fixture: one garment

This fictional fixture supplies text facts only. It is not a real brand, garment observation, or generation record.

- **Garment:** One deep teal, short-sleeved cotton-knit top with a mock neckline, a short center-front zipper, fine vertical ribbing, and a straight hem at the upper hip. It is unbranded.
- **Display:** A single front-view catalog photograph on a plain torso mannequin, cropped from the base of the neck to just below the full hem. No accessories, other garments, panels, or copy.
- **Selling features:** The mock neckline, short zipper, sleeve shape, ribbed surface, and complete hem remain in frame.

### Resolved prompt (中文)

```text
制作一张4:5竖版的单件服装商品摄影图，呈现清晰写实的棚拍效果。一件深青绿色短袖棉质针织上衣是画面唯一主商品，正面穿着在简洁的无头躯干人台上。画面范围从人台颈部下方延伸至上胯，并在完整衣摆下方保留少量空间。背景为干净的暖灰色摄影棚背景，左前方的大面积柔光均匀照亮织物，衣摆和人台边缘形成轻柔接触阴影。

上衣呈现立领、短款正中拉链、短袖、细密竖向罗纹表面和落在上胯位置的平直下摆。这个虚构的无品牌商品以整洁无字的深青绿色罗纹织面呈现在画面中。立领、拉链起止位置、两侧袖型、竖向纹理与完整下摆均清晰可见。画面由这件上衣、人台和暖灰色摄影棚背景构成，织物质感自然，轮廓清楚，棚拍光线克制。
```

### Resolved prompt (English)

```text
Create one 4:5 vertical apparel product photograph in a clear, realistic studio style. One deep teal short-sleeved cotton-knit top is the featured item, shown front-facing on a simple headless torso mannequin. The top is centered in the frame from just below the mannequin's neck to the upper hips, with the full hem and a little space below it visible. A clean warm-gray studio background fills the scene. Broad soft light from the front left illuminates the knit evenly, with gentle contact shadows along the hem and mannequin edges.

The top has a mock neckline, a short center-front zipper, short sleeves, fine vertical ribbing, and a straight hem at the upper hip. Its fictional unbranded front presents a clean, unlettered deep-teal ribbed surface. The neckline, zipper endpoints, both sleeve shapes, vertical texture, and complete hem are easy to see. The image consists of the top, its mannequin, and the warm-gray studio background. The knit texture looks natural, the garment outline is clear, and the studio light is restrained.
```

## Source and evidence state

Independently authored on 2026-10-11 from [product art direction](../../../oneirloom-product-art-direction/SKILL.md), [visual analysis](../../../oneirloom-visual-analysis/SKILL.md), [photography](../../../oneirloom-style-photography/SKILL.md), and [fashion styling](../../references/fashion-styling.md). No external text or image was imported. The [wardrobe-sheet example](../wardrobe-sheet/template.md) and [white-architecture pose records](../../../oneirloom-style-photography/templates/white-architecture-portrait-poses/template.md) remain separate and retain their own case-specific deviations; they are not evidence of this garment-lock mechanism. The linked item-6 run is a single pass for the fictional teaching fixture only. It establishes no real-garment facts or repeatability.

## Output checks

- The mock neckline, short sleeves, and short upper-chest zipper match the fictional teaching brief.
- Continuous teal knit extends below the zipper to the complete hem. The headless torso and warm-gray scene remain in the requested crop.
- Keep this fictional fixture separate from real garment facts and specifications.
