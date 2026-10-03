# 03. Mirror sphere

Read the [collection contract](../template.md) before adapting this recipe. It binds the sample slots and the checks below to the current brief and the shared graphic-design SOP.

## Selection conditions

Choose this recipe when a reflected place or scene can carry the main image inside one oversized spherical surface. It depends on recognizable reflection distortion and a complete orb.

## Source observations and uncertainty

The [style crop](images/reference.png) shows a nearly page-width circular reflective object in the middle and upper field. A monochrome room curves across it. A large serif footer sits directly below, while small editorial notes and blue handwriting occupy upper corners.

The continuous convex reflection is a visible effect. Calling the object polished chrome and requiring physically coherent curvature are recipe interpretations. The exact optical setup, source creator, model, and font are unknown.

Source metadata remains in the [collection reference record](../reference.json).

## Defining mechanism and relational anchors

- Keep the sphere complete and close to both side margins. Its circle occupies most of the image field, with a separate footer below.
- Wrap the chosen scene across the convex surface. Straight architectural lines bend and compress together, while enough scene detail remains recognizable.
- Use the serif footer as a firm horizontal base beneath the circle. The eye moves from sphere to footer, then to small corner copy.
- Keep any handwritten accent secondary in the upper-right margin. Its visual weight must leave the circle dominant.

## Adaptation map

Map the source room to the requested interior or scene, selecting visible structures that will remain recognizable after curvature. A flat photograph clipped into a circle does not preserve this recipe. If the subject is an object rather than a place, resolve what the sphere reflects and what identifies that subject before handoff.

## Adjustable slots and scoped sample values

| Slot | Sample value | Resolve for the current brief |
| --- | --- | --- |
| Reflected scene | Conservatory with arches and plants | Requested scene and recognizable reflected structures |
| Orb scale | About 90% page width, complete circle | Side clearance and image-to-footer separation |
| Copy | `FIELD 03`; `A different view`; `More` / `ways` / `to see` | Exact supplied copy; no invented upper-left microtype |
| Accent | Small blue handwritten upper-right phrase | Chosen hue, wording, and bounded corner area |
| Format | Portrait 2:3 on off-white paper | Requested canvas |

The 90% width and conservatory are sample specifications. The source supports a nearly page-width orb, not an exact measured percentage.

## Construction and handoff

At the SOP layout stage, reserve a complete circle and its footer baseline, then bound both corner text areas. In the resolved prompt, describe the chosen scene's continuous curvature and the relative size of handwriting. Keep the corner phrase out of the sphere's primary hierarchy.

## Acceptance against the resolved brief

- The sphere has a complete circular boundary and the agreed narrow side margins.
- The requested scene is recognizable and visibly curves across one continuous reflected surface.
- The footer is separated below the sphere on a clear baseline.
- The chosen handwritten accent stays within its small assigned region. Unspecified microtype and the historical sample's oversized handwriting are deviations.

## Prompt files and historical evidence

- [Archived Chinese sample prompt](prompt.zh.txt)
- [Archived English sample prompt](prompt.en.txt)

The reusable prompts are provided in [Chinese](prompt.zh.txt) and [English](prompt.en.txt). One transfer sample was generated with the built-in `image_gen.imagegen` entry point using the English prompt and the reference image for style and layout. The exact submitted text is saved in [submitted.en.txt](submitted.en.txt), and the inspected sample is [transfer-01.png](images/transfer-01.png), with its run details in [example.json](example.json).

The sample is 1024 × 1536 pixels, matching the requested 2:3 ratio. Inspection found a complete sphere at about 92% of the canvas width, a recognizable curved monochrome conservatory reflection, the requested three-line blue phrase, and the serif “FIELD 03” footer on a straight baseline. The upper-left microtype reads “03 Portfolio Studies Edition.” The blue handwriting is substantially larger than the prompt’s requested small accent, and the upper-left wording was supplied by generation rather than specified in the prompt. The tool response did not identify an underlying model. This records one generated result and does not establish repeatability or model-wide quality.

