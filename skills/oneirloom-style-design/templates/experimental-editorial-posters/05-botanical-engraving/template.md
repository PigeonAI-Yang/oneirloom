# 05. Botanical engraving collage

Read the [collection contract](../template.md) before adapting this recipe. It binds the sample slots and the checks below to the current brief and the shared graphic-design SOP.

## Selection conditions

Choose this recipe when a large botanical form can support monochrome line texture, sparse contour accents, and a compact handwritten response.

## Source observations and uncertainty

The [style crop](images/reference.png) shows a large flower and dark leaves spanning most of the page width. Their forms approach or meet the side edges. The flower occupies the upper and middle field, while leaves extend toward the lower right. Orange lines follow selected contours. Handwriting and a small arrow sit upper-right, with bold type lower-left.

The species, original creator, font, model, and production medium are unknown. Engraving-like hatching is a recipe interpretation of the visible linework, not proof of a historical print technique.

Source metadata remains in the [collection reference record](../reference.json).

## Defining mechanism and relational anchors

- Enlarge the plant across the upper and middle field. Let selected leaves or stems meet or cross the frame where the resolved crop calls for it, retaining the diagnostic flower structure.
- Use fine monochrome hatching to distinguish overlapping petals and leaves. The plant remains the main tonal mass.
- Attach narrow accent strokes to actual outer contours and selected internal edges. Their irregular line follows the plant instead of forming a detached decorative frame.
- Reserve small upper-right space for supplied handwriting and a directional mark. Place the main supplied title in the open lower-left area, secondary to the plant.

## Adaptation map

Map the source flower's layered petals and broad leaves to the new botanical subject's distinctive structure. Select the exact contours that receive accent lines. For a non-botanical subject, identify an equivalent layered surface and state the adaptation instead of inventing plant anatomy.

## Adjustable slots and scoped sample values

| Slot | Sample value | Resolve for the current brief |
| --- | --- | --- |
| Subject | Blooming iris with curling petals and long leaves | Requested subject, diagnostic structure, and cropped extremities |
| Occupancy | Illustration roughly in the upper two-thirds | Actual image region and footer clearance |
| Accent | Sparse orange contour traces | Chosen hue and named edges to trace |
| Copy | `Study` / `Explore` / `Repeat`; `FIELD 05`; `Botanical observations` | Exact supplied handwriting and title/caption hierarchy |
| Format | Portrait 2:3, warm off-white paper | Requested canvas and paper treatment |

The iris and upper-two-thirds target belong to the archived sample.

## Construction and handoff

During the SOP layout stage, establish the plant mass and clear copy regions, then identify a few contour paths on that mass. Carry the crop and those paths into the prompt. Resolve hatching before applying the accent lines so each line has a visible edge to follow.

## Acceptance against the resolved brief

- The requested subject's defining forms remain readable at the resolved large scale and crop.
- Accent traces stay attached to selected real contours. They do not become detached scribbles or a general outline around the page.
- Monochrome hatching separates overlapping forms without filling every light region.
- The image leads, followed by supplied handwriting and lower-left title/caption in their agreed regions.

## Prompt files and historical evidence

- [Archived Chinese sample prompt](prompt.zh.txt)
- [Archived English sample prompt](prompt.en.txt)

the English prompt was submitted once with the style-only reference through the built-in `image_gen.imagegen` entry point. The result was visually inspected and saved at [images/transfer-01.png](images/transfer-01.png); the submitted prompt and inspection record are in [submitted.en.txt](submitted.en.txt) and [example.json](example.json). The requested and actual frame are 2:3 (1024 × 1536). The Chinese prompt remains untested; the style reference is not a generated result.
