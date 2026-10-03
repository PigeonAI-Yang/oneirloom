---
name: oneirloom
description: "Oneirloom (织梦师), also called 织梦师Skill or Oneirloom Skill. Turn visual requests and references into complete image prompts, graphic designs, sticker packs, icon assets, or brand identities. Diagnose results, route illustrated tutorial writing, or package an image and prompt into a 3:4 card. Select relevant methods and templates."
---

# Oneirloom

Oneirloom is the public name of this collection. Treat "织梦师", "织梦师Skill", "Oneirloom", and "Oneirloom Skill" as aliases for this entry. The main technical invocation is `$oneirloom`; capabilities retain the `oneirloom-` namespace.

## Coordinate the current request

1. Read the [shared interaction contract](references/interaction-contract.md) before the first substantive response unless its unchanged content is already available. Identify the actual deliverable and carry confirmed conversation choices. Distinguish prompts, concepts, specifications, and finished usable files.
2. Select only the capabilities the current task needs. Resolve each exact name through the host catalog, with `../<name>/SKILL.md` as the repository fallback, and read it explicitly. A link does not invoke a skill. Reuse unchanged instructions already read. An unavailable branch blocks only dependent work.
3. Resolve visual intent before model adaptation. For real products, begin with product evidence and the current concept. For composed graphics, use the design capability's complete process, with a specialist for stickers, icons, or VI when applicable. For reconstruction, read visual analysis and its reconstruction workflow before drafting. Other image prompts lead with 3–5 checkable anchors while preserving all required relations.
4. Add the requested model adapter only when image prompting or generation needs it, after the visual specification. Multiple models share that intent. Unknown models or entries receive portable visual text until capabilities are established. Native vector and document work needs no image-model adapter. Use the selected capability's delivery and inspection procedure.

## Select capabilities by task

| Current task | Read |
| --- | --- |
| Existing image and prompt card | `oneirloom-prompt-card` |
| Illustrated tutorial or article edit | `oneirloom-image-tutorial` |
| Real-product depiction, clear or vague selling brief, or product revision | `oneirloom-product-art-direction` |
| Full VI or defined identity extension | `oneirloom-brand-identity`, which coordinates only the requested components |
| Individually usable chat reactions | `oneirloom-expression-stickers` |
| UI icon family, app symbol, or product identifier | `oneirloom-icon-design` |
| Character, wardrobe, multi-view, or expression reference sheet | `oneirloom-character-sheet`; add visual analysis for supplied references |
| Reconstruction, unclear visible relations, or abstract aesthetic | `oneirloom-visual-analysis` |
| Decisive viewpoint, perspective, pose, crop, scale, or occlusion | `oneirloom-camera-composition` |
| Decisive regional color, transparent material, illumination, or atmosphere | `oneirloom-color-light` |
| Photography, lifestyle portrait, or film still | `oneirloom-style-photography` |
| Drawing, painting, print, animation illustration, or collage | `oneirloom-style-illustration` |
| Composed graphic, packaging, isolated product study, 3D render, or craft mockup | `oneirloom-style-design`; its graphic process applies when there is a composition task |
| Clearly adult non-explicit figure art or requested concealment | `oneirloom-figure-art` and the relevant medium |
| Requested Krea 2 or Qwen-Image-2.1 adaptation | `oneirloom-model-krea-2` or `oneirloom-model-qwen-image-2-1` respectively |
| Actual or user-reported result miss | `oneirloom-result-diagnosis`; a routine edit with no reported miss uses the current confirmed prompt and choices |

Use the primary deliverable capability plus its needed medium and conditional analysis, spatial, or lighting support. Let the owner select an optional recipe; no match means composing from the method. Do not reopen settled choices or load an unchanged medium for a local edit.

For person prompts, including new images and grid panels, read [person defaults and proportions](references/person-prompts.md). For requested Oneirloom watermarks, use the approved signature guidance in [prompt cards](../oneirloom-prompt-card/SKILL.md); the icon capability retains its no-automatic-watermark rule.
