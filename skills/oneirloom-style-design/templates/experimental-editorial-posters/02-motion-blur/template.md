# 02. Directional motion drag

Read the [collection contract](../template.md) before adapting this recipe. It binds the sample slots and the checks below to the current brief and the shared graphic-design SOP.

## Selection conditions

Choose this recipe when one subject can provide a stable lower anchor and a distinct part that carries directional motion. The contrast between those two parts supplies the composition.

## Source observations and uncertainty

The [style crop](images/reference.png) shows a large chair in the middle field. Its lower structure is comparatively crisp, while upper parts repeat and streak horizontally toward the left. The feet approach the lower image boundary above the bold footer. A condensed title at upper left and tiny notes at upper right remain sharp.

"Motion drag" describes visible repeated forms, not a verified exposure technique or movement history. The exact number of echoes, original typeface, creator, and model are unknown.

Source metadata remains in the [collection reference record](../reference.json).

## Defining mechanism and relational anchors

- Give the subject most of the central image field, between the upper type and lower footer regions. Keep the stable lower anchor visible and close to the bottom of that field.
- Extend offset echoes from the chosen moving part in one direction. Fade their tone and definition with distance, retaining an identifiable original shape.
- Confine the motion to the declared moving region. The lower anchor and the type remain sharp.
- Let the trail pass behind the type region at low contrast, or end before it, according to the resolved layout. Establish that overlap before rendering detail.

## Adaptation map

Map the chair's lower structure to a stable base, foot, stem, or other anchor on the new subject. Map its repeated upper region to a part whose displacement can be read without duplicating the whole object. A subject with no such division needs an explicit choice of stable and moving regions before this recipe can be resolved.

## Adjustable slots and scoped sample values

| Slot | Sample value | Resolve for the current brief |
| --- | --- | --- |
| Subject | Black articulated desk lamp | Requested subject and stable versus moving parts |
| Placement | Centered, about 60% page width, base lower-center | Image-field occupancy and visible lower anchor |
| Motion | Leftward horizontal echoes over about one lamp-head width | Direction, reach, fading pattern, and image/type overlap |
| Copy | `STILL` / `IN` / `MOTION`; `Observe` / `Shift` / `Repeat`; `FIELD STUDIES`; `A poster study` | Exact supplied copy and sharp type regions |
| Tone and format | Monochrome, warm paper, portrait 2:3 | Current palette and format |

The lamp, numerical scale, and trail distance are archived sample choices.

## Construction and handoff

In the SOP's low-detail layout, mark the crisp anchor, original moving part, trail envelope, and sharp text blocks. Carry those regions into the resolved prompt. Add the localized echoes after the stable subject is established, then place the sharp typography above the motion layer.

## Acceptance against the resolved brief

- The requested subject fills the resolved image field and retains its declared stable anchor.
- Only the selected moving part carries echoes, with the agreed direction and reach.
- The original part remains identifiable. Fading trails do not turn into several equally solid complete subjects.
- All supplied type remains sharp and follows the resolved reading order.

## Prompt files and historical evidence

- [Archived Chinese sample prompt](prompt.zh.txt)
- [Archived English sample prompt](prompt.en.txt)

One English run submitted [prompt.en.txt](prompt.en.txt) verbatim, recorded in [submitted.en.txt](submitted.en.txt), with the style-only crop; its generated result is [images/transfer-01.png](images/transfer-01.png), documented in [example.json](example.json). The built-in image-generation tool did not return the generated model name. The Chinese prompt remains unrun, and repeatability is unknown because no repeated run was performed.
