# Three-layer architecture

## Responsibilities

| Layer | Owns | Reads |
| --- | --- | --- |
| Main skill | Current task, conversation constraints, method selection, conflict resolution, output contract | Required method skills and conditional shared guidance |
| Method skills | Reusable decisions for analysis, character identity, medium, camera, lighting, model adaptation, diagnosis, or tutorial writing | Relevant references and a local template index when a concrete preset is useful |
| Template documents | A specific visual recipe, adjustable slots, prompt scaffolds, and associated image records | Only the examples needed for the current task |

The main and method skills remain sibling directories under `skills/`. These are content layers, not a required three-level filesystem or an automatic tool invocation protocol. The host must resolve and read each selected skill by name; sibling paths are the repository fallback. Missing specialist content blocks only work that depends on it.

Supporting method references, such as model task tables or composition guidance, remain references. They do not become prompt templates merely to fit a directory scheme.

## Reading path

1. Read the main skill and inherit the current user's constraints.
2. Read only the applicable methods. Choose one primary medium, plus analysis, spatial, model, or diagnosis methods when needed.
3. If a concrete recipe helps, read the owning method's `templates/index.md`.
4. Read the matching `<template-id>/template.md`. Inspect relevant example images before describing their visible effects.
5. Adapt the visual specification and apply the requested model adapter. Return the complete deliverable under the main output contract.

When no template fits, compose using the method. A request for a new scene, style, or subject does not require creating a persistent template. Tutorial writing owns its article format and author voice; it uses prompt methods and examples only as required by the lesson.

## Template ownership and format

Each template belongs to one method skill. Keep the index short: template link, selection conditions, and defining visual relations. Store actual image paths only in the template and its associated example record; do not maintain a second image catalog in the router.

A template contains:

- Selection conditions.
- Defining visual anchors.
- Adjustable slots and scoped defaults.
- A complete prompt scaffold, with all slots resolved before delivery.
- Examples, or an explicit statement that no corresponding image is available.

Example assets and records stay inside the template directory so the owning method can be installed without a dependency on temporary work folders. Use paths relative to the document or record that contains them. Create image directories only when actual images exist.

Distinguish input reference images from generated outputs. A generated example record stores its image path, exact submitted prompt, known model/entry, relevant settings, and observations or unresolved deviations. Unknown metadata stays unknown. Keep the original image intact; record any processing if a derivative is added. Never edit an old submitted prompt to match a new scaffold while retaining its old image as evidence.

An untested template, a user-reported success without the image, and an inspected generated output are different evidence states. A queue completion or structural check is not a visual inspection. The generalized indoor-portrait scaffold, for example, is untested even though its directory contains an inspected historical example.

## Conflict resolution

- Current explicit user choices override defaults; confirmed conversation choices override generic templates.
- Explicit requested changes override conflicting reference facts while other reference relations remain.
- Example-image props, subjects, and settings are not requirements for a new task.
- Medium methods own visual treatment. Model adapters own actual entry capabilities and must not change the requested aesthetic.
- The observed entry takes precedence over generic model claims. Without entry evidence, provide portable text without invented controls.
- The main skill owns standalone prompt language and formatting. Tutorial requests use the requested article format. Preserve literal in-image text.

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

Actual generation quality requires inspecting outputs under the recorded entry and settings. New-session discovery requires a new host session; filesystem readback through a junction establishes only that the installed path resolves to the edited source.
