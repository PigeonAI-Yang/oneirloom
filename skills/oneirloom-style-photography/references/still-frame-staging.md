# Still-frame staging

Use this reference when a single photographic frame should make an event and the relationships within it legible. It guides still-image staging only; it does not describe motion sequences or claim video-production capability.

## Build the frame

1. State the event at one chosen instant. Use a beginning, contact, reaction, or aftermath only when it fits the brief; do not compress a whole sequence into one frame.
2. Establish the people and objects that matter to the event. Describe who is acting, responding, or sharing an object, and where each stands in relation to the others.
3. Direct eyelines toward the person, object, or off-frame cause that carries the moment. Make gaze direction consistent with head and body orientation.
4. Choose a readable action moment and preserve its physical relations: contact, support, reach, or separation should agree with the visible pose.
5. Stage figures and objects across foreground, middle distance, and background. Use placement, scale, overlap, and open space to show who is central and how the setting surrounds the action.
6. Use light and color to direct attention and carry the scene's tone. Keep the source direction, key and fill, shadow, highlights, and background response coherent with the event.

The film-like result comes from the chosen event, shot scale, eyelines, staging, depth, and light-color narrative. Select a palette and depth of field to fit the scene; teal-orange color, high contrast, and shallow depth of field are options only when they serve the intended image.

## Product-use instant

- **ID:** `cinema.product-use-instant`
- **Owner:** `oneirloom-style-photography`
- **Tags:** C/P/T
- **Search synonyms (zh):** 商品使用瞬间、产品交接静帧、手与商品接触
- **Search synonyms (en):** product-use moment, product handoff still, hand-object contact
- **Authored:** 2026-10-11
- **Source:** Oneirloom-authored guidance based on the [shared interaction contract](../../oneirloom/references/interaction-contract.md), [material response](../../oneirloom-color-light/references/material-response.md), and [visual-capability expansion plan](https://github.com/PigeonAI-Yang/oneirloom/blob/main/docs/visual-capability-expansion-plan.md) section 5.
- **Evidence status:** New written guidance, unrendered. The linked recipe's fictional teaching example has not been generated or visually checked.

**Mechanism and scope.** This entry applies the staging steps above to one product-use event in one still image. Choose a single instant, such as the moment a recipient's hand first supports a product. Show the hand-to-object contact and the support that keeps the product in a plausible position. Keep the product's supported identity and package visible. Let hand position and gaze point to the same action. Place the product in the clearest part of the frame, with people or hands in the middle distance and only enough background to identify the setting. Keep background information tied to the brief or source.

**Fixed relations.** Keep the event, contact, supported product facts, and package fixed.

**Variables.** Adjust the instant, crop, camera angle, hand positions, gaze, product placement, depth, and light to fit the request. A hand-only crop has no gaze cue, so use wrist and finger direction to point toward the product.

| Common miss | Repair |
| --- | --- |
| The image reads as a posed display | Name the exact event instant and show who acts, who responds, and where their hands touch the product. |
| Hands cover the product or do not support it | Move contact to a supported part and keep the product outline and package face visible. |
| The product looks suspended or tilted without support | Set hand contact, product orientation, support, and contact shadow together. |
| Faces, hands, and product suggest different actions | Align gaze, hand direction, and product placement with the same event. |
| The setting implies unsupported shop details | Keep only sourced setting facts; otherwise use a generic, unlettered background. |

Use the [product-use instant recipe](../templates/product-use-instant/template.md) for full-scene and hand-only prompt examples. The following portable scaffold shows the complete relationships to resolve in both languages:

```text
一张写实摄影风格的单幅静帧，呈现 {一个产品使用事件} 在 {一个确切瞬间} 的画面。{人物或手}位于 {画面位置}，{手部接触与支撑关系}作用于 {产品及包装正面}，产品呈现 {清楚的朝向与可见区域}。{人物视线}落在 {产品、另一人物或动作焦点}。前景呈现 {前景内容}，中景呈现 {人物、手与产品的关系}，后景为 {场景内容或空白背景}。主光从 {方向} 照射，补光从 {方向} 以 {强弱} 提亮暗部。阴影沿着接触点、人物位置和场景光线延展，画面凝结在一个摄影瞬间。
```

```text
A realistic single photographic frame of {one product-use event} at {one exact instant}. {The person or hands} occupy {frame position}, with {hand contact and support} on {the product and package face}. The product shows {clear orientation and visible area}, while {the person's gaze} falls on {the product, the other person, or the action focus}. {Foreground detail} fills the foreground; {the relationship among the person, hands, and product} occupies the middle distance; {setting detail or blank backdrop} fills the background. Key light comes from {direction}, with fill from {direction} at {strength}. Shadows extend from the contact points in the same direction as the scene lighting. The photograph captures one frozen instant.
```

## Correct the main miss

If the frame reads as posed rather than eventful, clarify the action moment, eyeline, or contact between people and objects. If the space feels flat, correct placement, overlap, and light separation before adding blur. If the mood feels generic, revise the scene-specific light and color relationships instead of adding a generic cinematic label.

Keep the complete prompt within the active task's output contract. This guidance does not establish that an unrendered prompt will produce the intended frame.
