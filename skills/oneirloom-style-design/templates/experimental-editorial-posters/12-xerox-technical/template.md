# 12. Xerox-technical macro study

Read the [collection contract](../template.md) before adapting this recipe. It binds the sample slots and the checks below to the current brief and the shared graphic-design SOP.

## Selection conditions

Choose this recipe when a recognizable detail can fill a close-cropped image field and support an overlaid technical grid and one translucent color block.

## Source observations and uncertainty

The [style crop](images/reference.png) shows a high-contrast grayscale eye enlarged across the upper and middle page. The surrounding face is cut by the frame and rectangular image boundaries. Thin white grid lines and alignment marks cross the image. A translucent green rectangle overlaps its upper-right area, beside a narrow right-side text rail. A heavy footer anchors the bottom.

"Xerox-technical" is a working descriptor. The actual printer or process, source author, date, typeface, model, and original prompt are unknown. The fingerprint in the sample is an intentional subject substitution.

Source metadata remains in the [collection reference record](../reference.json).

## Defining mechanism and relational anchors

- Enlarge a diagnostic macro detail across most of the upper and middle image field. Crop the surrounding subject at the frame or photo-mask edges, keeping the selected detail readable.
- Use coarse monochrome reproduction texture while preserving the detail's continuous structure.
- Overlay a fine white grid and aligned registration or crop marks on the image. Their lines describe a technical reading of the image and remain subordinate to it.
- Place one translucent accent rectangle over the upper-right portion of the photograph. The subject detail remains visible through the block.
- Keep a narrow right-side rail for supplied notes and a heavy lower-left footer. Read the macro detail, overlay, and footer before the smallest copy.

## Adaptation map

Map the source eye's iris and skin detail to the new subject's diagnostic macro structure, such as ridges or a material pattern. Preserve that structure through the crop and reproduction texture. The grid is a graphic device unless the brief supplies real measurements; do not invent technical claims or dates.

## Adjustable slots and scoped sample values

| Slot | Archived sample value | Resolve for the current brief |
| --- | --- | --- |
| Subject | Fingertip fingerprint with radial whorl | Requested macro detail and continuous recognizable structure |
| Occupancy | Upper two-thirds with narrow right rail | Current image crop, rail width, and footer clearance |
| Marks | Thin white grid, registration crosses, crop corners, ticks | Resolved grid region and subordinate line density |
| Accent | Translucent green rectangle, about one-quarter page width by one-sixth height | Chosen hue, current size, and image overlap |
| Copy | `PATTERNS` / `IN` / `PLAIN SIGHT`; `OCT 02` / `2026`; `FIELD 12`; `Observe the ordinary` | Exact supplied notes, date if supplied, and footer/caption |
| Format | Portrait 2:3, warm off-white paper | Requested canvas |

The old date, percentages, fingerprint, and wording are sample choices. They are not future defaults.

## Construction and handoff

At the SOP layout stage, reserve the cropped macro image, right rail, accent rectangle, and bottom type block. Carry their overlap order into the prompt: photograph, reproduction texture, fine technical marks, translucent accent, and typography. Keep the subject's diagnostic detail readable through that stack.

## Acceptance against the resolved brief

- The requested macro structure remains recognizable at the resolved enlarged scale and crop.
- Coarse reproduction texture leaves its continuous detail readable.
- Fine white marks cross the intended image region and remain subordinate.
- One rectangle in the chosen accent overlaps the image at the agreed size with visible detail beneath it.
- Supplied copy, including any explicitly supplied date, is exact and stays within the rail and footer regions.

## Prompt files and historical evidence

- [Archived Chinese sample prompt](prompt.zh.txt)
- [Archived English sample prompt](prompt.en.txt)

The English prompt in `prompt.en.txt` was submitted once through the built-in `image_gen.imagegen` entrypoint; its returned image is `images/transfer-01.png`, and the submitted text is saved as `submitted.en.txt`. The output was visually inspected. The built-in result exposed no underlying-model metadata. The Chinese prompt in `prompt.zh.txt` was not run, and repeatability remains unknown after this single English generation; `example.json` records the observed result and deviations.
