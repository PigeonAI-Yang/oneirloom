# Fashion styling

Use this guidance when clothing coordination is a meaningful part of a single fashion image or a related set of views. A single image does not require a wardrobe sheet. For a requested wardrobe board, use its selected template for panel layout and read this reference for reusable styling and continuity decisions.

For one real garment shown as the main item for sale, use the [single-garment product-display template](../templates/single-garment-look/template.md) when its garment-lock scaffold fits. Keep product facts fixed while treating pose, crop, model, accessories, and setting as separate choices.

When a source image is involved, use [visual analysis](../../oneirloom-visual-analysis/SKILL.md) to establish observed garment facts. Keep unseen construction, fit, and rear-view details unknown unless the user supplies them or authorizes a design inference. Styling guidance does not change the supported facts of a real garment.

## Coordinate the look

1. Preserve the wearer's confirmed identity anchors while treating the outfit as its own design choice. Keep silhouette and palette consistent with the requested image or series.
2. Describe the silhouette through visible fit and outline: where the garment follows, layers over, or separates from the body. Use the requested direction rather than turning one example's proportions into a default.
3. State layer order and the visible construction that makes it readable, including necklines, openings, closures, waistlines, hems, and overlaps. Keep separate garments distinct where the image shows them as separate pieces.
4. Assign footwear and accessories to the specific look. Their shape, placement, and scale should support the outfit and the requested use; do not infer unseen items from an occupation or accessory.
5. For a series, keep identity anchors stable and vary only the requested or agreed styling dimensions. Give each look its own complete clothing, footwear, and accessory description rather than reusing one outfit sentence across different views.
6. Bind visible clothing to each view. Structural views share one base outfit unless variation is requested. A portrait or crop shows the neckline and upper garment belonging to its corresponding look; do not copy a signature neckline across unlike outfits.

The wardrobe-sheet template's six coordinated looks are that template's default, not a general fashion-image requirement. Use [the wardrobe-sheet recipe](../templates/wardrobe-sheet/template.md) only when its board layout is requested or useful.

If a generated series changes identity along with the outfit, reassert the stable identity anchors and make the intended clothing variation explicit. If a crop hides a garment feature, omit the unseen claim or mark it as a design inference when one was requested.

## Reusable method

### Single-garment merchant display

- **ID:** `fashion.single-garment-merchandising`
- **Tags:** F (Fashion), P (Photography), T (Product)
- **Owner:** `oneirloom-character-sheet` (sole owner of fashion-styling knowledge and the single-garment recipe)
- **Synonyms (EN):** single-garment product display; one-item apparel catalog image
- **Synonyms (ZH):** 单件服装商品展示；单件服装商品图
- **Authored:** 2026-10-11
- **Visible mechanism:** Keep one real garment as the primary sellable item in one image. Preserve its source-supported appearance while allowing presentation to change around it. Separate garment facts from the model, pose, crop, accessories, light, and setting.
- **Variables:** Display mode (worn, mannequin, hanger, or flat lay), view, crop, model, requested pose, accessories, background, light, and optional copy. Choose an on-body crop only when the garment features named in the selling brief remain visible; widen the frame when length or the full hem matters.
- **Fixed relations:** Preserve confirmed garment category, visible silhouette, neckline, openings and closures, hem, visible material appearance, and readable marks or logos. Use supplied specifications for fiber or construction claims; a visual texture alone does not establish composition. Keep accessories and other styling outside the garment's identity. Show the user-named selling feature without covering it with hair, hands, jewelry, layers, or props. One item and one view are enough unless the user requests a comparison or board.
- **Failure and correction:** If an accessory or pose changes the garment, restate the garment's supported features and vary only the presentation. If a crop or occlusion hides a selling feature, move the obstruction, select a clearer view, or widen the frame; do not claim the hidden feature. If only the front is supported, do not present an unknown back or interior as confirmed; request the missing view or label an authorized design inference. If a single image expands into outfit variants or panels, return to one garment and one requested view. Do not turn visual description into cutting, patternmaking, or manufacturing guidance.
- **Source paths:** [Product art direction](../../oneirloom-product-art-direction/SKILL.md); [visual analysis](../../oneirloom-visual-analysis/SKILL.md); [photography method](../../oneirloom-style-photography/SKILL.md); [photography template index](../../oneirloom-style-photography/templates/index.md); [single-garment recipe `fashion.single-garment-look`](../templates/single-garment-look/template.md); [wardrobe-sheet record](../templates/wardrobe-sheet/template.md); [white-architecture pose record](../../oneirloom-style-photography/templates/white-architecture-portrait-poses/template.md).
- **Source and evidence:** Independently authored from the linked local methods on 2026-10-11; no external text or image was imported. The wardrobe-sheet and white-architecture records remain case-specific, with their recorded deviations intact; neither establishes single-garment preservation. The new template uses a fictional text fixture only. This entry and its prompt scaffold are unrendered; no generated result, repeatability, or sales outcome is established.
