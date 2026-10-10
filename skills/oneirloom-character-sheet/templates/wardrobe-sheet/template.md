# Character wardrobe sheet

## Selection

Use for a character wardrobe board that combines outfit variation with identity references, accessories, garment details, material samples, and costume portraits. The recorded format is a 3:4 page with six looks. Preserve a different outfit count or layout when the user requests it. For an illustration-to-photography conversion, use the photography method alongside visual analysis. Keep this recipe distinct from a simple turnaround or a four-view/four-expression card.

## Visual anchors

- One consistent character appears in every outfit, portrait, and structural view. Translate an illustrated face into plausible human proportions while preserving its hair, face shape, expression, and palette.
- A narrow left rail contains front and profile identity portraits, a color palette, and small front/side/back views in the signature outfit.
- One enlarged signature-outfit figure stands beside five smaller complete figures in the upper-right area. The default six looks are signature, casual, active, formal, winter, and lounge.
- The lower-right area contains accessory flat lays, garment close-ups, and a horizontal material-sample strip. A bottom row contains six costume portraits, one in each corresponding outfit.
- Full-length figures include complete footwear. Keep each garment's layers, openings, hems, pleats, and shoe structure readable; stockings, socks, tights, skirts, and shorts remain distinct pieces.

## Adjustable slots

Resolve identity, medium, outfits, accessories, palette, labels, background, and light from the user or visible reference. The sample's black hair, adult woman, monochrome palette, clothing, and accessories belong to the example. They are not requirements for another character. Apply the router's person defaults only when appropriate to the new brief.

Assign reference roles outside the prompt. A drawn wardrobe board can supply layout and clothing; an actual portrait can supply facial identity. Clothing or layout references do not establish an unrelated person's exact face. Unknown rear garment construction remains unknown or an explicitly identified design inference.

For reusable outfit coordination beyond this six-look layout, read the [fashion styling reference](../../references/fashion-styling.md). The six looks remain this template's default.

Keep the six outfit descriptions separate and complete, including shoe and accessory assignments. The front/side/back views use the signature outfit. Each bottom portrait uses its corresponding outfit's actual neckline, rather than repeating the signature shirt across the row. Describe selected lighting and observable materials when changing medium. Preserve requested labels as literal text; exact label accuracy remains a result to inspect.

The scaffold is in Chinese. Deliver its complete English equivalent when required by the router. Resolve every slot before delivery. The generalized scaffold below has not been generation-tested.

## Prompt scaffold

```text
一张{画幅比例，未指定时为3:4竖幅}的角色衣橱设定页，使用{真实棚拍摄影或用户指定媒介}，由同一位{已确定的角色身份与外貌}的全身造型、脸部特写、服装局部和配饰平铺组成。全页保持{脸型、五官位置、发型、发色、肤色与身体比例}一致。{背景、分隔线、字体和整体配色}，布局清楚，留白整洁。页面左上标题为“{页面主标题}”。

左侧窄栏从上到下排列同一角色的正面与侧面脸部特写、{已确定颜色}组成的配色卡，以及基础造型的正面、侧面和背面三张完整全身图。三视图使用同一套基础服装：{基础造型的完整服装与鞋履}，保持统一人物高度、姿态与脚底基线。左栏标签为“{身份标签}”“{配色标签}”“{三视图标签}”。

中央偏左放置一张明显较大的基础造型全身图，完整呈现头顶、手部和鞋底，角色{主造型姿势与表情}，清楚展示{基础造型的服装层次、领口、腰头、裙片或裤腿、袜类与鞋履结构}。标题为“{01基础造型标题}”，副标题为“{副标题}”。

右侧上方横向排列五张较小的完整全身造型图，人物保持同一身份和自然比例，每套服装独立完整。第二套为“{02标题}”：{休闲服装、鞋履、配饰和姿态}。第三套为“{03标题}”：{运动服装、鞋履、配饰和姿态}。第四套为“{04标题}”：{正式服装、鞋履、配饰和姿态}。第五套为“{05标题}”：{季节服装、鞋履、配饰和姿态}。第六套为“{06标题}”：{居家服装、鞋履或赤脚状态、配饰和姿态}。各造型的服装结构、材质、颜色及遮挡关系清楚，双脚与鞋履完整入画。

右侧造型下方设“{配饰区标题}”区域，将{本角色已确定的鞋履、包袋、饰品与可拆卸服装单品}分别平铺，完整展示每件物品轮廓。旁边设“{服装细节区标题}”区域，用整齐的局部照片展示{已确定的领口、纽扣、腰头、裙褶、裤脚、拉链、蕾丝或针织细节}，细节与对应全身造型一致。下方设“{面料区标题}”水平样本带，展示{实际使用的面料及其纤维、纹理和受光差异}。

页面底部是一行六张等宽胸像，标题为“{肖像区标题}”。六格依次穿着上方第一至第六套造型的对应上衣、领口与配饰，分别呈现{六种已确定表情或轻微姿态变化}。所有肖像保留同一角色的五官比例与发型，服装领口与上方造型准确对应。

全页使用一致的{光线方向、主光与补光关系}，{肤色、头发、浅色织物、深色服装和配饰的区域色彩及高光}。完整人物脚下与平铺物品旁有自然接触阴影，{所选媒介的真实皮肤、织物、皮革或金属表现}，全部栏目对齐、层级明确，呈现统一角色的完整衣橱档案。
```

## Examples

| ID | Role | Image | Prompt or record | Verification |
| --- | --- | --- | --- | --- |
| reference-01 | User-provided illustrated wardrobe/layout reference | [Original reference](images/reference-01.webp) | [Reference record](reference-01.json) | Inspected; six outfits, a large signature look, identity rail, accessory/details areas, material strip, and six costume portraits |
| result-01 | User-provided realistic generated output | [Original output](images/result-01.webp) | [Output record](result-01.json); [Chinese prompt delivered in this chat](delivered-prompt-01-zh.txt) | Inspected with deviations; actual submitted prompt, model, entry, and settings were not provided |

The user selected this case for template reuse. Both original PNGs are copied unchanged. The archived Chinese text is the delivered prompt, not a verified execution receipt. The result shows a coherent photographic wardrobe board, but its left turnaround repeats front-facing views instead of providing a clear side view, and several bottom portraits repeat the signature shirt instead of matching all six outfits. It therefore supports this recorded visual example, not exact satisfaction of every slot or repeatable success of the new scaffold. No new image generation was performed during template collection.
