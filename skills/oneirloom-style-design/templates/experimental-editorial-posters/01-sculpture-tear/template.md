# 01. Sculpture tear

Read the [collection contract](../template.md) before adapting this recipe. It binds the sample slots and the checks below to the current brief and the shared graphic-design SOP.

## Selection conditions

Choose this recipe when a short display title and an enlarged, cropped portrait can share a page divided by a narrow torn accent. The title and the face compete in scale, while small copy occupies the remaining left margin.

## Source observations and uncertainty

The [style crop](images/reference.png) shows a black high-contrast serif title across the upper left, a large grayscale sculpture face below and to the right, and a narrow red strip at the far right. The face fills much of the lower page and continues beyond the bottom edge. A jagged white boundary cuts alongside the right side of the sculpture. Small text runs down the open left region. The title reaches close to the accent region.

The font, creator, original model, and physical or digital production process are unknown. The white edge resembles torn paper. Its fibers and exact path cannot be reconstructed from this small raster.

Source metadata remains in the [collection reference record](../reference.json).

## Defining mechanism and relational anchors

- Enlarge the chosen portrait until its face or defining local feature carries the lower-right field. Crop the lower extent at the page edge instead of shrinking the entire object into the page.
- Place the display title in the upper-left field. Its large serif forms balance the image mass, followed by any supplied smaller left-side copy.
- Run one narrow accent strip along the right edge. Put an irregular white tear between that strip and the grayscale image, so the boundary visibly clips or conceals the image edge.
- Keep the tear, image, and strip adjacent. An intact small cutout floating beside a straight colored bar loses this mechanism.

## Adaptation map

Map the sculpture face to the requested subject's most recognizable local feature. Record which lower or outer parts leave the frame and which identifying contours stay visible. Keep the display title and the image in opposing upper-left and lower-right regions. A change to a landscape or full-body requirement needs a stated layout adaptation.

## Adjustable slots and scoped sample values

| Slot | Sample value | Resolve for the current brief |
| --- | --- | --- |
| Subject and crop | Athena bust, face about half the page width | Requested subject, retained local feature, and explicit edge crops |
| Title and copy | `FORM` / `01`; `Old shapes` / `New readings`; `FIELD STUDIES` / `A poster study` | Exact supplied copy and its hierarchy |
| Accent | Red strip narrower than one-sixth of page width | Chosen color, strip extent, and tear path |
| Format and scale | Portrait 2:3, large upper-left serif title | Requested format and resolved title-to-image balance |

These are sample design choices, including the width threshold. They are not measurements of the original artwork.

## Construction and handoff

At the SOP layout stage, place the title block, cropped face mass, white tear, and narrow accent strip before resolving surface detail. The prompt must name the cropped edges and say where the tear masks the image. Set the small copy only in the left region reserved by the resolved layout.

## Acceptance against the resolved brief

- The requested local identity remains readable at the agreed scale, with the recorded crop visible.
- The title leads from the upper left into the lower-right image. Supplied small copy stays secondary.
- The irregular white tear separates and clips the image against the narrow chosen accent strip.
- The title fits the resolved type region. The historical sample's title intrusion into the accent is not a required feature.

## Prompt files and historical evidence

- [Archived Chinese sample prompt](prompt.zh.txt)
- [Archived English sample prompt](prompt.en.txt)

- [Complete Chinese prompt](prompt.zh.txt)
- [Complete English prompt](prompt.en.txt)
- [Submitted English prompt](submitted.en.txt)
- [Transfer sample 01](images/transfer-01.png)
- [Sample record](example.json)

One poster was generated with the built-in `image_gen.imagegen` tool and visually inspected. It reads as a single flat poster with a grayscale Athena bust, a jagged white tear, a far-right red strip, warm off-white paper, and the requested copy. The title reaches across most of the canvas and intrudes into the tear/red-strip area, reducing the intended open space. This records one generation and visual inspection only; repeatability is untested. The tool response did not identify the underlying model. The linked reference image remains style-only; its creator and font are unknown.
