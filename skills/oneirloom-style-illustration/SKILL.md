---
name: oneirloom-style-illustration
description: Compose watercolor, print, comic, animation, concept-art, folkloric narrative, and paper-collage prompts through visible linework, color layers, texture, and spatial structure. Select indexed presets for decorative rainy-night prints, halftone portrait cutouts, or zhiguai narrative illustrations.
---

# Illustration and painting

绘画与插画类提示词的方法技能：先定媒介与画面结构，再写线、纹理、色彩层与主体背景关系。本技能是判断规则库，按清单检查；具体风格配方在 templates。

## When to use

- Watercolor, print, comic, animation, concept-art, folkloric narrative, or paper-collage prompts
- A specific preset with an indexed template, such as a decorative rainy-night print, halftone portrait cutout, or zhiguai narrative illustration

## Method checklist

When illustration is used in a poster, cover, editorial layout, infographic, or composed ad, read the [graphic-design SOP](../oneirloom-style-design/references/graphic-design-sop.md) before adapting a recipe. It owns the brief, layout, mechanism transfer, and review order; this method supplies linework, medium, texture, and color-layer decisions. Preserve the intended crop, relative areas, and overlap when changing medium. Illustration without a graphic-layout task keeps the checklist below.

- Establish the medium and image structure, then specify lines and edges, marks and texture, color layers, the role of paper or canvas, and subject/background relationships.
- The same style name can describe different techniques; specify the visible result.
- For watercolor streets, describe light pencil structure, transparent washes spreading into damp paper, and paper-white window edges.
- For comics, prioritize gaze, action direction, framing continuity, and panel reading order.
- For concept art, prioritize shape language, scale references, and atmosphere.
- Introduce photographic imaging terms only for an expressly mixed medium.

## Templates and references

- Read the [illustration styles](references/styles.md) for medium choices.
- For a specific preset, read the [template index](templates/index.md), then the matching template only. Match defining visual relations rather than one color or weather word. Use the method above if nothing fits.
- Preserve user and source-image details when adapting slots, and inspect example images before describing their results. A sample image is not automatically a generation input.

## Output and handoff

Deliver the illustration description integrated into the main skill's complete prompt. Composition and color relations follow `oneirloom-camera-composition` and `oneirloom-color-light` when they are loaded; reference inspection follows `oneirloom-visual-analysis`. When a generated result misses the intended illustration, hand off to `oneirloom-result-diagnosis`.
