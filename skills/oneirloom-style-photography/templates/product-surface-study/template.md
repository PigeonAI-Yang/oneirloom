# Product surface study

## Selection

Use this recipe when a product photograph needs a clear product outline, package, or observed surface appearance. Start from a user-provided product or a source that identifies the product. This recipe supports photography, not package redesign.

- **ID:** `photo.product-surface-study`
- **Owner:** `oneirloom-style-photography`
- **Tags:** M/P/T
- **Search synonyms (zh):** 商品表面摄影、产品表面研究、商品全貌与细节
- **Search synonyms (en):** product surface photography, product surface study, full product and detail views
- **Authored:** 2026-10-11
- **Source:** Oneirloom-authored guidance based on the [shared interaction contract](../../../../skills/oneirloom/references/interaction-contract.md), [material response](../../../oneirloom-color-light/references/material-response.md), and [visual-capability expansion plan](https://github.com/PigeonAI-Yang/oneirloom/blob/main/docs/visual-capability-expansion-plan.md) section 5.
- **Evidence status:** The fictional full-product branch has one recorded pass in the [item 1 evidence record](../../../oneirloom/references/teaching-observations.md). Close-detail, transparent-bag, other surface branches, and repeat reproduction have not been run.

## Mechanism and scope

This recipe uses background contrast, light size and direction, camera angle, and crop to make a product surface readable. It keeps the product's supported identity, base color, package, marks, and shape fixed while changing the photographic treatment.

Use one view per image. A full-product view shows the complete visible outline, parts, and current package. A close-detail view centers a confirmed surface region and keeps one nearby edge, seam, or component in frame so the detail remains tied to the same product. If both views are requested, deliver separate complete prompts with the same product, base color, package, and chosen light direction.

## Fixed relations and adjustable choices

Keep the source-visible outline, component arrangement, folds, package shape, base colors, and exact visible marks. Preserve supplied wording on the same package face. Leave areas without supplied text unlettered. Keep any confirmed background choice fixed. Adjust background luminance only when the task leaves it open. Keep the contact shadow attached to the product's support points. Highlights and reflections must agree with the chosen light and visible surroundings.

| Choice | Adjust it to | Keep it consistent with |
| --- | --- | --- |
| Background luminance | Separate the outline from the background when the task leaves the background open | The product's supported base color and visible edge |
| Light area and direction | Set highlight width, edge softness, and shadow direction | One selected direction across separately delivered views |
| Camera angle | Show the required face, contour, seam, or surface region | The product's proportions and visible part relationships |
| Detail region and crop | Focus on one confirmed area while retaining a nearby recognition cue | The same product and current package |
| Surface appearance | Choose only a branch supported by the source or user | The appearance visible in that region |

Choose one appearance branch when it fits the source. Describe appearance rather than naming an unconfirmed material.

| Branch | Visible description |
| --- | --- |
| Transparent soft-bag appearance | Show the supported silhouette through the bag, broad transmitted light, soft folds, and local edge highlights that follow the observed shape. |
| Matte-paper appearance | Use broad, low-contrast highlights and a restrained surface texture only where the source shows them. |
| Local glossy surface | Put a defined highlight and controlled reflection on the observed glossy region. Keep its boundary and the underlying color clear. |

## Common misses and repairs

| Miss | Repair |
| --- | --- |
| A highlight changes the product's apparent base color | Separate the base color from illumination and revise only the lit region. |
| A close crop no longer reads as the same product | Include a nearby edge, seam, package face, or component as a scale and identity cue. |
| Every surface gets the same gloss | Select the appearance branch from visible evidence and keep highlights local to the matching region. |
| The whole product and detail are combined into an unintended collage | Write and deliver one prompt per requested view. Keep product identity, package, base color, and light direction fixed across them. |
| A reflection points away from the light or surroundings | Align the highlight and reflected scene with the selected light direction and visible environment. |

## Prompt scaffold

Resolve each slot from the current source or user direction, then remove unused choices. Each prompt describes one view. If both whole and detail views are requested, deliver two separate prompts with the same product, base color, package, and light direction. The code blocks are visual prompt scaffolds; keep provenance checks, unsupported-fact rules, and evidence status in this recipe prose.

```text
一张写实的单幅商品摄影，画面呈现 {商品的可见外形与部件}，包装为 {包装形状、颜色与图形或字样}。本张是 {完整全貌或局部细节} 视图，画幅为 {比例}，相机位于 {观察角度}，商品处于 {画面位置} 并占据约 {画面比例}。

商品位于 {支撑表面} 上，轮廓、部件排列、褶皱、包装形状和基色清晰可见。包装正面呈现 {图形与准确字样}，表面其余区域呈现 {图形或简洁空白面}。背景为 {背景色调与亮度}，商品边缘与背景清楚分离。主光从 {方向} 照射，形成 {光面范围与边缘}；补光从 {方向} 以 {强弱} 照亮暗部。接触阴影贴合实际支撑点，高光与反射沿着这组光线关系呈现。

表面呈现 {色泽、纹理与高光}。完整全貌显示商品的连续轮廓与全部可见部件；局部细节显示 {细节区域} 与邻近的 {边缘、接缝或组件}。商品基色、包装和整体识别在画面中保持清楚。
```

```text
A realistic single-frame product photograph showing {the product's visible form and parts}, with {package shape, color, graphics, and wording}. This is a {full-product or close-detail} view in a {aspect ratio} frame. The camera sits at {camera angle}; the product occupies {frame position} and about {frame occupancy}.

The product rests on {support surface}, with its outline, component layout, folds, package shape, and base colors clearly visible. The package face shows {graphics and exact wording}, while the remaining surface shows {graphics or a plain blank face}. The background is {background hue and luminance}, with a clear edge around the product. Key light from {direction} creates {light-area size and edge quality}; fill from {direction} at {strength} illuminates the shadows. The contact shadow follows the actual support points, and highlights and reflections follow the same light direction.

The surface shows {color, texture, and highlights}. The full-product view shows the continuous outline and all visible parts; the close-detail view shows {detail region} beside {an edge, seam, or component}. The product's base color, package, and identity remain clear in the frame.
```

## Fictional teaching example

The fictitious unbranded package below demonstrates two separately delivered views. Both prompts use the same warm-cream rectangular package, deep-teal vertical panel, small coral circle, blank cream face, pale blue-gray background, and soft upper-left light. Its surface description is an observed appearance for this example, not a claim about its physical material. Both prompts are original teaching text. The full-product branch has one recorded pass. The close-detail branch has not been run.

### Full-product view

```text
一张写实的单幅商品摄影，画面中央是一只无品牌长方形小包装盒，暖奶油色基底上有一条深青绿色竖向色块和一个小珊瑚红圆点，正面留有一块空白奶油色区域。商品完整全貌位于浅蓝灰色背景前，正面略朝向相机，画幅为四比五竖幅，相机从略高于包装中心的位置轻微俯拍，包装占画面约三分之二。

盒体边缘笔直，顶部折线清楚，正面基色和图形边界清晰。盒子落在浅蓝灰色台面上，底部接触阴影沿着实际支撑边缘轻柔延展。背景与包装之间保留清楚的轮廓分离。柔和主光从画面左上方照射，形成宽阔、低反差的表面亮区；右侧弱补光照亮阴影。表面呈现细微、低反差的纹理和柔和宽亮区，暖奶油色、深青绿色与珊瑚红保持自然。阴影和亮区沿用左上方光线关系，包装边缘和正面图形保持清楚。
```

```text
A realistic single-frame product photograph centered on an unbranded rectangular small package. Its warm cream base carries one vertical deep-teal panel and a small coral-red circle, with a blank cream area on the front. The complete package sits against a pale blue-gray background, with the front turned slightly toward the camera. A four-by-five portrait frame is photographed from just above the package center at a gentle downward angle; the package fills about two-thirds of the frame.

The box edges are straight, the top folds are clear, and the base color and graphic boundaries remain distinct. The package rests on a pale blue-gray surface, with a soft contact shadow following its supporting lower edge. Its outline separates clearly from the background. Soft key light from the upper left creates a broad, low-contrast lit area; gentle fill from the right lifts the shadows. The surface shows a fine, low-contrast texture and broad soft highlights, while warm cream, deep teal, and coral red remain natural. Shadows and highlights follow the upper-left light, and the package edges and front graphics stay clear.
```

### Close-detail view

```text
一张写实的单幅商品局部摄影，呈现同一只无品牌长方形小包装盒的正面右上区域，边框与顶部折线同时入画。暖奶油色基底、深青绿色竖向色块、小珊瑚红圆点和空白奶油色区域与全貌视图完全相同。画幅为四比五竖幅，相机从略高的正面角度近距离拍摄，放大包装正面纹理，同时保留右侧边缘作为识别参照。

包装表面呈现细微、低反差的纹理与宽阔柔和的亮区，基色仍为暖奶油色，色块边界清楚。左上方柔和主光在表面形成低反差亮区，右侧弱补光保留边缘细节。深青绿色竖向色块与小珊瑚红圆点保持原有形状和相对位置，空白奶油色区域保持干净。浅蓝灰色背景只在包装边缘外留出窄幅，柔和阴影和亮区继续沿用全貌视图的左上方光线。
```

```text
A realistic single-frame close-detail photograph of the upper-right front area of the same unbranded rectangular small package, with its border and top fold both in frame. The warm cream base, vertical deep-teal panel, small coral-red circle, and blank cream area match the full-product view. A four-by-five portrait frame shows it from a close, slightly elevated frontal angle, enlarging the front surface texture with the right edge as a recognition cue.

The package surface shows fine, low-contrast texture and broad soft highlights, with a warm cream base color and crisp graphic boundaries. Soft upper-left key light creates a restrained lit area, while gentle right fill retains the edge detail. The vertical deep-teal panel and small coral-red circle keep their original shapes and relative positions; the cream area stays plain. A narrow band of pale blue-gray background remains beyond the package edge. Soft shadows and highlights continue the same upper-left light direction as the full-product view.
```

## Evidence record

The item-1 example shows the complete cream package, teal stripe, coral dot, blank label, pale blue-gray setting, and upper-left light. This records visible appearance only; it does not establish physical material.

## Output checks

- The full-product branch keeps the complete package outline and blank front area visible. The cream base, teal panel, and coral dot remain distinct against the pale blue-gray setting.
- The upper-left light and resulting surface appearance remain consistent with the selected source. Describe visible appearance only; do not infer physical material.
