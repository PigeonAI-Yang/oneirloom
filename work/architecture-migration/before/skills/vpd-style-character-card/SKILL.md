---
name: vpd-style-character-card
description: Provides indexed prompt templates for four-view plus four-expression character cards and basic three-view production cards. Use only when the requested layout matches one of these formats.
---

# Character-card layout templates

Use this skill when a user requests a character-card layout that matches one of the indexed templates. Use `vpd-character-sheet` for identity anchors and general information hierarchy. When a reference image is present, use `vpd-visual-analysis` for visible facts.

## Select a template

- For a two-row card with four full-body views above four expression close-ups, read [Four-view plus four-expression template](references/four-plus-four.md).
- For a basic production turnaround with front, side, and back views, read [Three-view production-card template](references/three-view.md).

Use a template only when its panel count, hierarchy, and purpose fit the request or reference. When neither layout fits, follow `vpd-character-sheet` and choose a layout for the task.

Fill slots from explicit user instructions, directly visible reference facts, or an applicable default from the router. Templates may retain adjustable slots, but the delivered prompt must resolve every slot: omit optional unknown details and ask only when an unknown changes the requested design. Keep one character's identity and outfit consistent across views unless the user requests a variation. Use a panel-specific prop only when the user specifies it or the reference shows it; otherwise remove the entire prop sentence. Do not infer unseen features to complete a template.

Return a complete positive prompt for each language required by the main skill's output contract. Keep image-reference inputs and model controls outside the prompt text. If exact label glyphs matter, prepare them in an editable layout after image generation and keep that production note outside the prompt.
