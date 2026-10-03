# Three-layer architecture

## Responsibilities

| Layer | Owns | Reads |
| --- | --- | --- |
| Main skill | Current task, conversation constraints, method selection, conflict resolution, output contract | Required method skills and conditional shared guidance |
| Method skills | Reusable decisions for analysis, character identity, stickers, icons, brand identity, medium, camera, lighting, model adaptation, diagnosis, or tutorial writing | Relevant references and a local template index when a concrete preset is useful |
| Template documents | A specific visual recipe, adjustable slots, prompt scaffolds, and associated image records | Only the examples needed for the current task |

The main and method skills remain sibling directories under `skills/`. These are content layers, not a required three-level filesystem or an automatic tool invocation protocol. The host must resolve and read each selected skill by name; sibling paths are the repository fallback. Missing specialist content blocks only work that depends on it.

The main skill retains the current brief and valid conversation choices. Product art direction supplies product decisions, visual analysis supplies evidence, style design supplies composition, and result diagnosis compares source, current agreed intent, and result. Ecommerce work uses these existing owners without a new skill, schema, or workflow layer.

Supporting method references, such as model task tables or composition guidance, remain references. They do not become prompt templates merely to fit a directory scheme.

`oneirloom-style-design` owns the single [graphic-design SOP](../skills/oneirloom-style-design/references/graphic-design-sop.md). Graphic work first understands communication intent and subject identity, then observes the actual selected style reference, then designs the adaptation. Subject understanding includes form, connected parts, visible action, and meaning, with facts and interpretations kept separate. The resolved design determines production. Direct generation, native design, and compositing are conditional paths; a rendered skeleton and separate assets are not universal prerequisites. Sketch contours remain provisional when actual anatomy requires revision. Prompt-only work returns complete usable bilingual prompts for the chosen path. Finished work returns a final preview and actual inspection status, with editable source and assets when warranted. These responsibilities stay within the existing three layers.

The SOP governs original and reference-based posters, covers, editorial layouts, infographics, and composed product ads. Visual analysis supplies source observations and applicable subject checks; product art direction supplies factual product inspection, clear and vague ecommerce briefs, optional sale-specific research, permitted creative transformations, and revision decisions; illustration supplies medium decisions. These methods do not define competing graphic-design sequences. Pure photography, isolated 3D rendering, character turnarounds, tutorial writing, and existing image-and-prompt card rendering retain their own procedures. Explicit code, vector, model, and single-model requests remain fixed constraints when selecting production.

The [expression-sticker method](../skills/oneirloom-expression-stickers/SKILL.md), [icon method](../skills/oneirloom-icon-design/SKILL.md), and [brand identity method](../skills/oneirloom-brand-identity/SKILL.md) are sibling methods with their own template collections. They specialize the same Understand, Observe, and Design stages. They inspect actual references before stored recipes, preserve meaningful subject anatomy, and carry material relationships into production where relevant. They add no parallel SOP or routing layer.

- Expression stickers own communicative intent, the reaction matrix, stable identity, caption and gesture relationships, individual exports, transparent edges, and legibility in chat. Character sheets remain identity references rather than finished sticker packs.
- Icons own functional metaphors, family construction, optical consistency, and legibility at intended sizes. They distinguish UI glyphs, app symbols, and illustrative pictograms. Supplied marks remain fixed, and real vector output requires vector geometry rather than a raster in an SVG wrapper.
- Brand identity owns coherent decisions across marks and lockups, color roles, typography, auxiliary graphics, image and icon language, the agreed applications, and guidelines. It coordinates icon or sticker methods only when those assets are requested. The design SOP still owns each graphic composition. A full VI requires the agreed foundations, applications, manual, and usable files; a concept board or one generated image cannot establish that delivery.

Artifact requests govern artifact delivery. Native SVG, code, individual assets, and VI guidelines do not require standalone image prompts or image generation. Prompt-only requests retain complete Chinese and English prompts for every needed image or asset. Unknown business facts, font rights, print profiles, and platform specifications remain explicit gaps only for dependent work.

## Reading path

1. Read the main skill and inherit the current user's constraints.
2. Read only the applicable methods. Choose the primary deliverable method and relevant medium, plus analysis, spatial, model, or diagnosis methods when needed. For a full VI, brand identity coordinates its requested components.
3. For graphic-design tasks, read the design method's SOP before template adaptation. If a concrete recipe helps, read the owning method's `templates/index.md`.
4. For graphics, inspect the selected reference image before reading the matching `<template-id>/template.md`. For other routes, read the selected template and inspect relevant images before describing their effects.
5. Adapt the visual specification and apply the requested model adapter when image prompting or generation needs it. Return the complete deliverable under the main output contract.

When no template fits, compose using the method. A request for a new scene, style, or subject does not require creating a persistent template. Tutorial writing owns its article format and author voice; it uses prompt methods and examples only as required by the lesson.

## Template ownership and format

Each template belongs to one method skill. Keep the index short: template link, selection conditions, and defining visual relations. Store actual image paths only in the template and its associated example record; do not maintain a second image catalog in the router.

A template contains:

- Selection conditions.
- Defining visual anchors.
- Adjustable slots and scoped defaults.
- A complete prompt scaffold for prompt-only use, with layout and asset guidance when the chosen production path needs them. A native artifact request uses the recipe's design relations and required files rather than forcing image generation. Resolve relevant slots before delivery.
- Examples, or an explicit statement that no corresponding image is available.

Graphic-design templates separate defining relations, adjustable presentation, and replaceable sample content. Read the actual reference before relying on a stored recipe. Describe hierarchy, crop, direction, text interleaving, accents, and local construction as the source supports them. Distinguish local tone changes from displaced fragmentation and estimates from source facts. Bind adaptation and acceptance to the current subject, intended meaning, and exact copy. Cropping can preserve identity, but meaningful parts require a deliberate semantic decision before omission. Template contours cannot impose another subject's anatomy. Explicit user choices remain fixed. Keep recipe-specific relations in the template and the common process in the SOP.

Example assets and records stay inside the template directory so the owning method can be installed without a dependency on temporary work folders. Use paths relative to the document or record that contains them. Create image directories only when actual images exist.

Distinguish input reference images from generated outputs. A generated example record stores its image path, exact submitted prompt, known model/entry, relevant settings, and observations or unresolved deviations. Unknown metadata stays unknown. Keep the original image intact; record any processing if a derivative is added. Never edit an old submitted prompt to match a new scaffold while retaining its old image as evidence.

An untested template, a user-reported success without the image, and an inspected generated output are different evidence states. A queue completion or structural check is not a visual inspection. The generalized indoor-portrait scaffold, for example, is untested even though its directory contains an inspected historical example.

## Conflict resolution

- Current explicit user choices override defaults; confirmed conversation choices override generic templates.
- Explicit creative changes override the affected reference presentation while other valid reference relations remain. For real-product work, a creative request does not certify a changed ingredient, structure, label, specification, or claim. Surface critical conflicts between product evidence and user statements before the dependent depiction, and record confirmed factual corrections with their source.
- Example-image props, subjects, and settings are not requirements for a new task.
- Medium methods own visual treatment. Model adapters own actual entry capabilities and must not change the requested aesthetic.
- The observed entry takes precedence over generic model claims. Without entry evidence, provide portable text without invented controls.
- The main skill owns standalone prompt language and formatting. Artifact requests use the selected method's deliverable contract. Tutorial requests use the requested article format. Preserve literal in-image text.

## Migrated recipes

| Previous location | Current owner and template |
| --- | --- |
| `vpd-style-xiaohongshu-beauty-squat` | [Photography: crouching selfie](../skills/oneirloom-style-photography/templates/xiaohongshu-squat/template.md) |
| `vpd-style-character-card` and its two references | [Character-sheet templates](../skills/oneirloom-character-sheet/templates/index.md) |
| Illustration reference `decorative-rainy-night.md` | [Illustration: rainy-night print](../skills/oneirloom-style-illustration/templates/decorative-rainy-night/template.md) |
| `vpd-style-halftone-cutout` | [Illustration: halftone cutout](../skills/oneirloom-style-illustration/templates/halftone-cutout/template.md) |
| Existing tutorial full-length portrait evidence | [Photography: indoor portrait](../skills/oneirloom-style-photography/templates/indoor-full-length/template.md) |

The retired recipe names no longer define separate active skills. Invoke their owning method or the main skill with the desired recipe. The migration preserves the existing character-card and rainy-night prompt blocks. It adds untested scaffolds for the former squat and halftone instruction-only recipes.

## Verification boundary

The nine initial sticker, icon, and brand identity recipes are researched starting points with no associated generated examples. Their presence establishes authored methods and routes, not tested visual quality, platform acceptance, or complete VI production.

Actual generation quality requires inspecting outputs under the recorded entry and settings. New-session discovery requires a new host session; filesystem readback through a junction establishes only that the installed path resolves to the edited source.
