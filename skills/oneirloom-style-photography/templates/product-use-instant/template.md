# Product-use instant

## Selection

Use this recipe when one photographic frame should show a person using, receiving, or handing over a product. Choose one event and one exact instant. The recipe describes a still photograph, not a video or motion sequence.

- **ID:** `photo.product-use-instant`
- **Related reference:** `cinema.product-use-instant` in [still-frame staging](../../references/still-frame-staging.md)
- **Owner:** `oneirloom-style-photography`
- **Tags:** C/P/T
- **Search synonyms (zh):** 商品使用瞬间、产品交接静帧、手与商品接触
- **Search synonyms (en):** product-use moment, product handoff still, hand-object contact
- **Authored:** 2026-10-11
- **Source:** Oneirloom-authored guidance based on the [shared interaction contract](../../../../skills/oneirloom/references/interaction-contract.md), [still-frame staging](../../references/still-frame-staging.md), and [visual-capability expansion plan](https://github.com/PigeonAI-Yang/oneirloom/blob/main/docs/visual-capability-expansion-plan.md) section 5.
- **Evidence status:** One hand-only run is not_pass in the [item 2 evidence record](../../../oneirloom/references/teaching-observations.md). Right fingers cover the front-right gray sleeve. The left support and base gap remain visible. The full-scene branch and repeat reproduction were not run.

## Mechanism and scope

The frame centers on one readable event. Hand placement shows who acts and who receives. Contact, support, gaze, product visibility, depth, and subject hierarchy all point to the same instant.

Use this method for a single frame. It does not describe a sequence of actions or establish video-generation capability. For a real product, preserve its identity, package, marks, and supported claims from the user's source. Keep any confirmed background choice fixed. When the user changes only the background, preserve every other confirmed choice. If accommodating the background requires an adjustment to another choice, state outside the prompt that it needs the user's decision; do not make the adjustment implicitly. Keep ingredients, effects, and venue details out of the prompt unless a source establishes them.

## Fixed relations and adjustable choices

Keep one event and the contact needed to read it. Make the product visible between or beside the hands. Hands must support or touch the object in a physically readable way. Set foreground, middle distance, and background so the product remains the main subject while the people and place explain the action.

| Choice | Adjust it to | Keep it consistent with |
| --- | --- | --- |
| Event instant | A handoff, placement, opening, or other requested use moment | One action at one moment |
| Framing | Full-scene view or hand-only view | Whether faces and gaze matter to the requested story |
| Hand contact | Who supports, offers, receives, or uses the product | The product's visible support and orientation |
| Gaze | The product, the other person, or the relevant action | Head and body direction; omit it when faces are outside the crop |
| Product position | Center, foreground, or another clear position | A readable product outline and package |
| Depth and light | Background clarity, separation, light direction, and fill | A coherent scene in which shadows and contact agree |

## Fictional teaching example

Both prompt branches use the same invented, unbranded takeaway cup: a cream-colored cup, a fitted white lid, and a blank pale-gray sleeve. The visible contents remain hidden. The generic counter and unlettered wall do not describe a real shop. Do not carry these invented details into a real product task.

### Full-scene view

Use this branch when faces, eyelines, and the counter setting help explain the handoff.

```text
一张写实风格的单幅产品交接摄影，捕捉简洁柜台前的一次杯子交接。画面以中景呈现柜台两侧的两位成年人，从腰部拍到头部。递杯者位于画面左侧，接杯者位于画面右侧，两人的视线都落在杯子上。

一只奶油色直壁杯由双手共同托持，竖直位于两人之间的前景、浅木色柜台上方，杯底与台面之间留有清晰可见的小间隙；杯子配有闭合的白色平盖和空白浅灰色套筒。完整杯身、套筒正面和杯盖清楚入画。递杯者伸出的左手从杯底正下方托住杯底；接杯者伸出的右手从相对两侧握住杯身上半部。画面凝结在两人共同完成交接的一个瞬间，两只手自然接触并共同支撑杯子，浅灰套筒正面保持完整可见。

浅木色柜台从前景延伸到两人之间，柔和的浅色空白墙面位于后景。杯子是画面最清晰、最醒目的主体，双手围绕杯子形成明确的动作关系，人物与柜台位于中景。柔和主光从画面左前方照亮杯子和双手，右侧较弱的补光提亮暗部。杯子在柜台上投下柔和、与杯底分离的阴影，并略向右后方延伸。相机从略高于柜台的位置以轻微俯角拍摄，空间层次、杯身轮廓和交接关系清楚可见。
```

```text
A realistic single-frame photograph capturing one cup handoff at a simple counter. Two adults stand on opposite sides of the counter in a medium view from the waist up. The person offering the cup stands on image left and the person receiving it on image right; both look toward the cup.

One upright cream-colored takeaway cup is held just above the counter in the foreground between them, with a small, clearly visible gap beneath its base. It has a fitted closed white lid and a blank pale-gray sleeve. The full cup, sleeve face, and lid are clear in the frame. The giver's extended left hand supports the cup directly beneath its base. The receiver's extended right hand grips the upper sides from the opposite side. The frame captures their shared handoff instant: both hands touch and support the cup naturally, with the pale-gray sleeve face visible between their fingers.

A pale wood counter runs through the foreground and between the people. A softly lit pale wall with a blank surface fills the background. The cup is the clearest and most prominent subject, with the hands framing the action, the people and counter in the middle distance, and the wall behind them. Soft key light from the front left illuminates the cup and hands, with weaker fill from the right. A soft cast shadow from the cup falls onto the counter, visibly separated from the cup base, and extends slightly toward the back right. The camera sits just above counter height at a slight downward angle, with the space, cup outline, and handoff clearly visible.
```

### Hand-only view

Use this branch when the contact matters more than faces or the wider setting. Wrist and finger direction carry the action in place of gaze.

```text
一张写实风格的单幅交接摄影，画面仅呈现柜台前的前臂、双手和一只无品牌外带杯。画面凝结在交接瞬间：奶油色直壁杯由双手共同托持，竖直位于浅木色柜台上方，杯底与台面之间留有清晰可见的小间隙，配有闭合的白色平盖和空白浅灰色套筒，套筒正面朝向相机，杯盖与杯身轮廓完整清楚。

画面左侧伸入的手从杯底正下方托住杯底，画面右侧伸入的手握住杯身上半部两侧。接杯者的手指自然贴合杯身上半部两侧，空白套筒正面完整可见，递杯者的手持续承托杯底。两只手与杯子的接触清楚，杯子保持竖直并由双手稳稳支撑，杯底与台面之间的小间隙清晰可见。手腕和手指方向共同指向杯子，动作焦点落在手与杯身的交接处。

杯子位于画面中央偏前，双手从左右两边构成动作主体。浅木色柜台形成连续前景，远处是柔和的浅色空白背景。主光从画面左前方照亮杯身和手背，较弱的右侧补光勾出杯身边缘。杯子在柜台上投下柔和、与杯底分离的阴影，并向右后方延伸。相机从略高于杯盖的位置以轻微俯角近距离拍摄，杯盖、套筒、手指接触和杯子轮廓清楚可见。
```

```text
A realistic single-frame handoff photograph framed around the forearms, hands, and one unbranded takeaway cup at a counter. The instant shows an upright cream-colored cup held slightly clear of a pale wood counter, with a small, clearly visible gap beneath its base. It has a closed white lid and a blank pale-gray sleeve facing the camera. The complete cup is clear in the frame.

A hand enters from image left and supports the cup directly beneath its base. A hand enters from image right and grips the upper sides. The receiver's fingers make contact along the cup's upper sides, leaving the sleeve face fully visible, while the giver supports the base. Both wrists and fingers point toward the cup, and the action centers on the shared hand-to-cup contact.

The cup is positioned just forward of frame center, with the hands forming the action around it from both sides. The pale wood counter forms a continuous foreground. A softly lit pale background with a blank surface sits farther away. Soft key light from the front left illuminates the cup and backs of the hands. Weaker fill from the right traces the cup edge. A soft cast shadow from the cup falls onto the counter, visibly separated from the cup base, and extends toward the back right. The camera is close and just above lid height at a slight downward angle, with the lid, sleeve, finger contact, and cup outline clearly visible.
```

## Common misses and repairs

| Miss | Repair |
| --- | --- |
| The scene reads as a posed product display | Name the exact instant and show which hand acts, which hand responds, and where contact occurs. |
| Hands cover the product or appear detached | Move fingers to a supported part of the product and keep its outline and package face visible. |
| The product seems to float or tip | Specify the supporting hand, base contact, orientation, and contact shadow together. |
| The frame implies several actions | Keep only the one event that can fit in a still frame. |
| Background details imply a specific venue | Use only sourced venue details; otherwise use a generic, unlettered setting. |
| The crop removes gaze but still depends on facial expression | Use the hand-only branch and direct wrist and finger orientation toward the product. |

## Evidence record

The cup's design and counter scene above are original fictional teaching material. The item-2 evidence covers one hand-only still frame; it does not establish the full-scene branch, repeatability, or video/motion capability.

## Output checks

- One requested action instant reads clearly. The giver supports the cup beneath its base, and the receiver contacts its upper sides.
- The cup remains upright. The visible base gap, sleeve face, and complete cup outline stay clear of fingers.
- Treat this as one still frame. Do not infer motion or video behavior.
