---
name: oneirloom-visual-analysis
description: 拆解参考图或模糊视觉需求，提取可检验的主体、空间、区域色彩和媒介锚点。用于参考图反推、图像复现、跨模型迁移与将“梦幻”“高级”等抽象词转成具体画面关系。
---

# Visual analysis

Split a reference image or a vague visual request into checkable anchors before any prompt is drafted. This skill feeds the main skill's internal visual specification; it does not redraft the final prompt itself.

## When to use

Route the incoming task before reading further:

| Task | Procedure |
| --- | --- |
| Reconstruct a supplied reference, or correct its reconstruction | Follow [references/reconstruction-workflow.md](references/reconstruction-workflow.md) end to end, steps 1–6. For a designed graphic, use the graphic-design route below for process order. |
| Port a confirmed visual specification to another model | Workflow steps 1, 5, and 6 against the already-confirmed specification; the anchors stay fixed, the adapter changes |
| Turn an abstract word (“梦幻”, “高级”) into concrete picture relations, no image supplied | Use [Decode abstract words](#decode-abstract-words) below; no image inventory applies |
| The user asks for the analysis itself, not a prompt | Workflow steps 1–2, then deliver the inventory with facts, inferences, and unknowns kept separate |

For any reconstruction, keep observed facts, user-confirmed targets, reasonable inferences, and unknowns separate throughout. Only facts and user-confirmed intent go into the prompt; do not guess lens models, the original prompt, or unseen garment parts.

For a poster, cover, editorial layout, infographic, or composed product ad, read the [graphic-design SOP](../oneirloom-style-design/references/graphic-design-sop.md). Its Understand, Observe, and Design stages own the process order. During understanding, inspect content and identity images for form, silhouette, connected parts, defining color and material, and visible action. Separate visible facts, user-stated meaning, tentative readings, and unknowns. During observation, inspect the actual selected style image before its stored recipe. Read large composition and hierarchy first, then each depicted version's position, direction, visible portions, type interleaving, accent bounds, and local construction. Record local tone changes and rectangular interruptions separately from displaced fragments; global continuity does not rule out a local dark segment. Label estimates and leave exact cuts or hidden production unknown when resolution cannot support them. Hand these observations to the SOP's design stage before selecting production tools. Preserve existing portrait, garment, and pose checks wherever those details must survive; a style-only example does not make its pose or content mandatory.

## Workflow overview

The full procedure with per-step checks lives in [references/reconstruction-workflow.md](references/reconstruction-workflow.md). Complete its frame, limb, garment, color, and evidence checks before drafting. For a portrait reference, the [portrait profile](references/profile-portrait.md) is a mandatory extension of step 2: highlight, proportion, perspective, pose-support, face, and garment-effect rows, checked in their stated order.

| Step | Produces |
| --- | --- |
| 1. Fix the task and evidence | Deliverable type; confirmed model, entry, and reference roles; facts vs. inferences vs. unknowns |
| 2. Inspect the frame, then the subject | Internal inventory: one observable relation plus one comparison criterion per row |
| 3. Select the defining relations | Ranked anchors and mandatory structural preservation relations with checkable acceptance conditions |
| 4. Draft in a predictable order | Ordered draft: opening sentence → framing and pose → subject head to body → environment → light → surface details |
| 5. Apply the model and task adapter | Entry-confirmed controls separated from prompt text |
| 6. Compare the prompt with the source | Pre-delivery check of every defining relation, including structural counterexamples |

## Hard gates

Three gates are mandatory during steps 2–3 of any reconstruction. The workflow defines each in full; they are named here so none is skipped:

- **Garment gate** — trace waistlines, hems and openings, seams and fastenings, cloth-skin boundaries, and occlusion paths before naming or revising any clothing category. Map each layer and its overlap order; check openings and visible connectors, separating hosiery from footwear; describe visible shape and coverage first, and leave the category unknown when construction cues do not support a name. Do not infer hidden anatomy.
- **Torso-posture evidence gate** — trace the shoulder line and torso axis through ribcage, waist, and pelvis before using labels such as leaning forward, bending, squatting, or lowered hips. When source cues do not converge, describe only the visible relation and omit the inferred label.
- **Area/salience budget** — estimate each dominant region's apparent frame area, position, and prominence from the source. A user-corrected feature is mandatory to retain but never promoted to focal point; mention a tiny feature once, bounded by a source-derived ratio.

## Decode abstract words

Split an abstract effect into candidate mechanisms and keep only the ones the image or the text supports. “梦幻” may come from soft edges, glowing objects, non-real spaces, or color contrast; do not preset pastel, brightness, or low saturation.

## Output and handoff

Hand the next branch one internal specification: `priority anchors / allowed to vary / unknowns / checkable criteria`. By default deliver only the final prompt; show the analysis when the user asks for it.

For multiple references, state each image's role — identity, pose, color, or style; a style reference is not a pose lock. A reconstruction task keeps identifying relations; a creation task may fill unspecified creative content. For a real product, route to `oneirloom-product-art-direction`: unreadable labels, hidden fillings, internal construction, ingredients, and performance claims remain unknown. Keep observed facts, user-stated facts, and creative intent distinct. Surface critical conflicts between material and user statements before depicting the disputed fact; a style reference or similar item cannot establish this product's facts.

When two focused correction rounds still miss the same key anchor, hand off to `oneirloom-result-diagnosis` instead of adding near-synonyms.
