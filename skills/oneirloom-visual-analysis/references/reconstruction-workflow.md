# Reconstruct a reference image

Use this procedure for a supplied reference and for corrections to its reconstruction. Inspect the source image before drafting. A failed generated image shows a miss; it does not replace the source as the target.

## 1. Fix the task and evidence

Identify whether the user wants a portable prompt, a model-specific prompt, an edit instruction, or an actual image. Inherit the confirmed model, entry, reference roles, and corrections. Keep observed facts, user-confirmed targets, uncertain interpretations, and unknown execution details separate. Reference reconstruction does not authorize filling unseen areas with invented details.

## 2. Inspect the frame, then the subject

Build a short internal inventory in this order. Every row needs an observable relation and a criterion for comparison with a result. Keep it internal unless the user requests analysis.

| Inspect | Record before writing |
| --- | --- |
| Frame and scale | Orientation, upper and lower crop landmarks, subject position and frame occupancy, camera height and direction when supported, near/far size, foreground and background overlap. |
| Main body and limbs | Head direction and gaze separately from torso direction and pitch. Trace shoulders, elbows, wrists, and hand contacts. Trace each leg from hip through knee to ankle, recording joint extension or flexion, crossing height, front/back order, and visible support. Mark hidden joints unknown. |
| Clothing and objects | Distinct layers, neckline, waistline, seams, hems, coverage, folds, tension, contact points, and overlap. Identify garment categories from construction cues or user confirmation. |
| Color and material | For each dominant item, separate base color, observed illuminated color, transparency and underlying color, surface texture, and reflection. Record evidence and uncertainty for the base-color judgment. Compare lit areas with shadows, folds, edges, and overlaps where visible. |
| Environment | Large background structures, their position and scale, ground surface, and the amount of setting retained by the crop. |
| Light and medium | Supported light direction, subject/background exposure, highlight width and falloff, cast shadows, background clarity, and photographic or illustrated surface treatment. |
| Text and small details | Exact readable text when needed, accessory position, and source-sized coverage. Leave unreadable or ambiguous details unresolved. |

For each visible hand, trace the arm to its actual contact point. Name the contacted object and the action, such as gripping a fabric edge or resting on a support. A nearby railing does not establish that the forearm rests on it. When a garment is lifted, trace the lifted edge to the hand that holds it. Keep an occluded hand's contact unknown.

For a crossed-leg pose, crossing and bending are separate observations. Inspect both knees and both hip-to-ankle paths. If both legs are extended, write straight knees and extended legs explicitly, then state where and in which order they cross. Do not infer knee flexion from leg overlap or a diagonal leg axis. Describe cropped feet as cropped, rather than inventing their placement or weight distribution.

For sheer fabric, its apparent brightness does not establish its base color. Skin transmission and flash can make black hosiery look pale. A user-confirmed black fabric remains black in the specification. Write its high transparency and illuminated appearance alongside that identity. If the base color is uncertain and would change the image substantially, inspect the available evidence again and ask a narrow question when it remains unresolved. Do not silently choose nude, white, or opaque black.

Treat sheen, weave, seams, and damage as separate properties. A bright line alone does not establish a run or tear. Describe supported geometry or leave the cause unknown. Do not turn an ambiguous highlight into invented fabric damage.

## 3. Select the defining relations

Choose the few relations that make this reference distinctive. Preserve all required inventory items; priority controls order, not omission. A confirmed correction is mandatory but retains its source-sized area. For each defining relation, ask whether a visibly different pose, garment, color, or crop could satisfy the sentence. Tighten that sentence when it could.

## 4. Draft in a predictable order

For a portable single-subject reconstruction, use this order:

1. Identify the medium, main subject, and scene in one opening sentence.
2. State framing, viewpoint, placement, and the defining pose. Describe torso orientation, arm contacts, and leg joint states before supporting appearance details.
3. Describe the subject from head to body, including garment construction, base colors, transparency, and visible objects. Place a material's decisive light response in its own description when the two are inseparable.
4. Place the environment around the subject using source-supported scale and overlap.
5. State light direction, regional illuminated colors, highlights, and shadows. Preserve the previously fixed material identities.
6. Add only source-supported surface treatment and small details that remain necessary.

For a divided layout, walk its regions in reading order instead. A documented model-specific writing order may replace this prose order, but it must preserve the same visual specification. These are local composition procedures, not claims about token priority or guaranteed model performance.

For image editing, lead with the requested operation and region, then the preservation requirement. Describe the changed attributes precisely. Avoid repainting every unchanged region in words. Confirm the entry's actual image inputs before supplying reference labels or controls.

## 5. Apply the model and task adapter

Read the selected adapter and its relevant local official source. Separate text-to-image, reference-conditioned creation, local editing, and style-reference inputs. Preserve one visual specification across requested models and languages. Unknown entries get portable text rather than invented syntax. Do not invent a language advantage, fixed prompt length, or model-specific pose recipe.

## 6. Compare the prompt with the source

Before delivery, check every defining relation in the final prompt, not only in the notes:

- Crop, subject occupancy, viewpoint, and overlap remain consistent.
- Each important limb has the intended orientation, joint state, crossing order, and contact. A general pose name is insufficient.
- Garment layers, coverage, base colors, transparency, and illuminated appearance agree. Bright highlights have not renamed the material.
- Small uncertain marks have not become invented damage or new focal points.
- Every visual claim comes from the source, user intent, or an identified applicable default.
- Each required language and model preserves the same color, pose, and spatial relations.

After a correction, remove the rejected description and all dependent cues from the complete prompt. Recheck other matched anchors. A prompt revision is untested until its actual generated result is inspected. An independent text-only pass can verify interpretation and instruction use, not image fidelity.
