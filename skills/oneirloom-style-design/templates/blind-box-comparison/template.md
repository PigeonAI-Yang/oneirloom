# Portrait to blind-box figure comparison

## Selection

Use for a vertical before-and-after image with the original portrait above and a collectible figure of the same person below. The input content reference is always written as `<image1>` in the prompt. Supply the actual photograph through the entry's image input; the text label alone is not an uploaded image.

Keep the requested two-panel deliverable. A standalone toy image does not fulfill this template. The example hairstyle, face, clothing, or gender is not a default for a new subject; derive those details from the supplied photograph.

## Visual anchors

- Two equal-width panels stacked vertically, approximately 45% of the height for the original photograph and 55% for the toy.
- The upper panel retains the source person's photographic appearance, clothing, and background; the lower panel translates the same identifiable features into a toy.
- A large head, compact body, rounded short limbs, semi-matte vinyl face and hands, glossy eyes, sculpted hair, and miniature textile clothing.
- A complete seated figure with bent legs opened to either side, soles facing forward, and both hands resting between the feet.
- A warm blush-beige studio background in the lower panel, soft light, and grounded contact shadows.

## Adjustable slots

The accepted prompts below are complete instructions. Adapt identity, hair, clothes, and colors from `<image1>`. Keep the upper-source/lower-toy arrangement unless the user explicitly changes it. Panel proportions, toy expression, shoe-sole color, background, and material treatment are adjustable when requested.

An image-generation instruction to retain the upper photograph does not prove exact pixel preservation. If exact original pixels are required, generate the lower toy panel and assemble it with the original photograph using a layout workflow.

## Prompt scaffold

Deliver the required language or the Chinese/English pair under the router's output contract. Keep input images and canvas controls outside the copyable text.

### Chinese

```text
制作一张竖版上下对照图，画面分为上下两个等宽区域，上半部分约占总高度的45%，下半部分约占55%，两部分直接上下拼接。

上半部分展示<image1>原始照片，保留原照片中的人物、真实面貌、发型、表情、服装、背景和摄影质感。按原图比例等比缩放，以完整保留人物头部与主要服装特征的方式排入上方区域。

下半部分展示根据<image1>中同一人物设计的精致收藏级盲盒玩偶。让上下两个人物在发型轮廓、发色、眉眼特点、神态以及服装款式和配色上形成明确对应。将真人特征转译成大头短身的玩偶造型：头部连同头发约占坐姿总高度的一半，头宽明显大于躯干，身体短小紧凑，四肢圆润。脸颊饱满，下巴小巧，眼睛适度放大并保留原人物的眼形特点，呈现侧目浅笑的俏皮神态，双颊与鼻尖带有柔和粉色晕染。

玩偶面部和双手采用细腻的半哑光搪胶质感，眼睛具有清澈的玻璃感与小而明亮的反光。头发以层叠、厚实的立体发束塑造，保留原发型的分缝、蓬松轮廓与发丝走向，发束具有清楚的体积和细致刻纹。服装沿用<image1>中的款式和配色，以精细微缩织物制作，绒面部分具有细密短绒，衣袖和衣身形成柔软厚实的褶皱。

玩偶正面坐在地面上，头部轻微侧转并略微倾斜，肩膀微微抬起。两条短腿向身体两侧自然打开，膝盖弯曲，两只圆润的脚朝向镜头，露出柔软的粉色织物鞋底。双臂垂在身体前方，两只小手从袖口探出，并排落在两脚之间，指尖朝前，形成乖巧、略带羞涩的坐姿。

下半部分采用暖粉米色无缝背景与同色地面，完整容纳玩偶的头发、身体、双手和双脚。柔和的大面积光线塑造圆润体积，地面保留轻柔的接触阴影，呈现真实实体玩偶的精细产品摄影效果。上下两部分的主体中心对齐，上方呈现原始真人照片，下方呈现对应的完整坐姿玩偶，构成清楚直观的改造前后对照。
```

### English

```text
Create a vertical before-and-after comparison image with two equal-width panels stacked directly above and below each other. The upper panel occupies approximately 45% of the total height, and the lower panel occupies approximately 55%.

In the upper panel, display the original photograph from <image1>, preserving the person’s real appearance, hairstyle, expression, clothing, background, and photographic texture. Scale the photograph proportionally and arrange it to retain the entire head and the principal clothing features.

In the lower panel, display a finely crafted collectible blind-box figure designed from the same person in <image1>. Establish clear correspondence between the two versions through the hair silhouette and color, characteristic eyebrows and eyes, expression, clothing design, and clothing colors. Translate the person into a large-headed, compact toy: the head including its hair occupies approximately half the seated figure’s height, the head is distinctly wider than the torso, and the body and limbs are short and rounded. Give the face full cheeks, a small chin, and moderately enlarged eyes that retain the person’s characteristic eye shape. Use a playful sidelong glance and subtle smile, with soft pink blush on the cheeks and nose tip.

Render the figure’s face and hands in finely finished semi-matte vinyl, with clear glass-like eyes and small bright catchlights. Construct the hair from layered, substantial sculpted locks that preserve the original parting, volume, and hair direction, with distinct three-dimensional forms and delicate engraved strands. Recreate the clothing design and colors from <image1> in detailed miniature textiles, with fine short-pile texture on plush areas and soft, thick folds across the sleeves and body.

Seat the figure facing forward, with the head slightly turned and tilted and the shoulders gently raised. Spread the short bent legs naturally to either side. Point both rounded feet toward the camera, showing soft pink fabric soles. Lower the arms in front of the body, with both small hands emerging from the cuffs and resting side by side between the feet, fingertips pointing forward. The seated pose feels endearing and slightly shy.

Use a seamless warm blush-beige background and matching floor in the lower panel. Include the figure’s entire hair silhouette, body, hands, and feet. Soft broad lighting shapes the rounded forms, with gentle contact shadows on the floor and the detailed product-photography appearance of a physical collectible. Align the subjects centrally across both panels: the original real-person photograph above and the corresponding complete seated toy below, forming a clear before-and-after transformation comparison.
```

## Canvas setup

Select a portrait output canvas suitable for two stacked panels, such as the user's selected 9:16 ratio. A ratio written in the prompt does not replace the entry's actual canvas controls.

In the local 8188 Qwen workflow inspected during this conversation, the grouped node exposed a `custom_size` switch. When false, sampling used the latent sized from the first reference image. When true, it selected the separate Empty Latent connected to the resolution selector. Use `custom_size=true` in that workflow when the selector should control the output canvas; the image remains connected as a reference.

This is an observation about that particular workflow, not a universal Qwen setting. Three inspected runs kept producing 1312×1184 from a 1316×1195 input despite changing the selector from 3:4 to 9:16, because the switch remained false. The setting change was explained but not executed or generation-tested in that diagnosis. Recheck connections if the workflow changes.

## Examples

The user approved saving this corrected two-panel template. No user-designated finished comparison image is archived here, and visual success or repeatability has not been established for this template. The earlier illustrative comparison was used to understand the requested design, not archived as a result generated by these prompts.

Add a user-approved source/result pair with its known generation details when supplied. Keep any missing run metadata explicit rather than inferring it from the accepted prompt.
