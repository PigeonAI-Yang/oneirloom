---
name: oneirloom
description: "Oneirloom (织梦师), also called 织梦师Skill or Oneirloom Skill. Turn visual requests, references, and generation misses into complete image prompts, route illustrated tutorial writing, or package an image and prompt into a 3:4 card. Select relevant method skills and their concrete templates."
---

# Oneirloom

Oneirloom is the public name of this skill collection. Treat "织梦师", "织梦师Skill", "Oneirloom", and "Oneirloom Skill" as names for this main skill when the user requests visual prompting or its other supported work. The main technical invocation is `$oneirloom`. Method skills use the `oneirloom-` namespace.

## Workflow

1. Inherit the user's confirmed model, entry, reference roles, successful details, and output preferences. Identify the deliverable: new image prompt, reference reconstruction, edit, character sheet, result diagnosis, cross-model adaptation, tutorial, or image-and-prompt card. Ask only when a missing input changes the task path; an unknown entry need not block portable text.
2. Select the required method skills below. For reference reconstruction, always load `oneirloom-visual-analysis` and its reconstruction workflow before drafting. Add camera/composition for visible pose or framing, and color/light for decisive colors, transparent fabrics, or illumination. Resolve each exact skill name through the host catalog; the repository fallback is `../<name>/SKILL.md`. Read the file explicitly: a Markdown link does not invoke a skill. If a branch is unavailable, report that limitation and continue the reachable general work.
3. Form one internal visual specification from user intent and visible evidence. For a creative ad based on a supplied product image, use `oneirloom-product-art-direction` to inspect the product and choose a product-specific concept before selecting a style or template. Treat a named template as a visual intention to adapt to the inspected item. Lead with 3–5 checkable anchors, while retaining all required reference relations. The owning method skill selects a matching template through its local index; no match means composing from the method. User choices and confirmed reference relations override template defaults. Example-image subjects and props are not implicit requirements.
4. Apply the requested model adapter after the visual specification. Read its task-specific writing guidance and relevant local official sources. When a requested version or task is undocumented, check primary official documentation and save the relevant text with its source, retrieval date, revision when available, and hash under that adapter's references. Keep source snapshots separate from local interpretation. An unavailable source blocks only the unsupported model claim. Keep model controls and reference-image inputs outside the prompt. For diagnosis, distinguish the model/entry that produced the sample from the desired target model. Unknown facts stay unknown; one result does not establish a model rule. Multiple requested models share the same visual intent.
5. Integrate one complete prompt per required language and model. State decisive spatial, scale, and occlusion relations first; mention supporting details once. Audit both directions: all required relations survive, and every visual claim comes from visible evidence, user intent, or an applicable default. For person prompts, including new images and grid panels, read [person defaults and proportions](references/person-prompts.md).

## Method routing

| Condition | Read |
| --- | --- |
| Combine an existing image and prompt into a shareable card, including a 3:4 vertical layout | `oneirloom-prompt-card` first; its artifact contract replaces the standalone prompt format. The cropped image fills the upper third and the prompt occupies the lower two thirds. |
| Write, expand, or polish an illustrated image-generation tutorial | `oneirloom-image-tutorial` first; its requested article language and format replace the standalone prompt format |
| Creative advertisement or story scene based on a supplied product image | `oneirloom-product-art-direction` first; inspect the item and choose its visual concept before selecting a medium or recipe |
| Character sheet, wardrobe sheet, identity continuity, or character card, including 4+4 and three-view layouts | `oneirloom-character-sheet`; add `oneirloom-visual-analysis` for references |
| Reference reconstruction, unclear visible relations, or an abstract aesthetic | `oneirloom-visual-analysis` |
| Viewpoint, perspective, crop, scale, or occlusion matters | `oneirloom-camera-composition` |
| Regional color, light direction, value, or atmosphere matters | `oneirloom-color-light` |
| Photography, film stills, or lifestyle portraits, including crouching selfies | `oneirloom-style-photography` |
| Drawing, painting, print illustration, or halftone paper-cut collage | `oneirloom-style-illustration` |
| Posters, text layout, products, packaging, or 3D rendering | `oneirloom-style-design` |
| Clearly adult non-explicit figure art or requested concealment | `oneirloom-figure-art`, alongside the relevant medium and spatial methods |
| Krea 2 requested | `oneirloom-model-krea-2` |
| Qwen-Image-2.1 requested | `oneirloom-model-qwen-image-2-1` |
| An existing result misses the goal or needs a local correction | `oneirloom-result-diagnosis` |

Load only relevant methods, normally one primary medium and the explicitly requested model adapters. Camera, lighting, and analysis are conditional additions. Tutorials reuse existing evidence for prose-only edits and load visual methods only for examples that need them. Unknown models use portable visual language until their actual capabilities are established.

For a card made from an existing image and prompt, follow `oneirloom-prompt-card` without redrafting the prompt or invoking a generation model. Its 3:4 card canvas is separate from any generation aspect ratio written in the prompt.

## Output contract

- For each explicitly requested model, or one portable version when unspecified, give a complete Chinese prompt followed by its semantically equivalent English counterpart. Follow an explicit single-language request instead. Preserve all visual details across languages.
- Put each complete prompt in its own copyable block. Keep titles, numbering, language labels, explanations, reference inputs, masks, seeds, and other entry controls outside. Include controls only when confirmed and useful.
- Use affirmative, observable image states. Before delivery, scan every prompt sentence and rewrite prohibitions or exclusions as positive visual relations. Preserve literal in-image text. Supply separate negative prompts, alternatives, explanations, or additional formats only when requested.
- For edits, describe the target change and the relations that must remain. For corrections, change the requested main dimension where possible and return the complete revised prompt.
- Do not invent original prompts, camera specifications, model capabilities, or success rates. A prompt without an inspected generated result is untested. A stored example demonstrates its recorded prompt and settings, not a subsequently edited template.
