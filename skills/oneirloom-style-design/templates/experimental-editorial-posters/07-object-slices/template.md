# 07. Object slices

Read the [collection contract](../template.md) before adapting this recipe. It binds the sample slots and the checks below to the current brief and the shared graphic-design SOP.

## Selection conditions

Choose this recipe when a familiar object can remain recognizable after its form is separated into ordered horizontal slabs.

## Source observations and uncertainty

The [style crop](images/reference.png) shows a large apple-like object, with a stem at the top and a rounded base, divided into horizontal grayscale bands with light gaps and lateral offsets. One band carries green. The object occupies most of the image field between a small upper-right heading and the bottom footer. Small side copy uses the open right margin.

The exact original cut count and physical process are not established by this low-resolution crop. The seven-slab pear is the archived sample's explicit construction choice. Source publication, creator, model, entry, and settings are unknown.

Source metadata remains in the [collection reference record](../reference.json).

## Defining mechanism and relational anchors

- Keep the object's whole outer form in view, from its diagnostic top to its base. Enlarge it across most of the image field, with clearance for the upper-right type and bottom footer regions.
- Divide that form into the resolved number of horizontal slabs in natural top-to-bottom order.
- Separate the slabs with slim paper gaps and small alternating lateral shifts. The combined outline must still read as one recognizable object.
- Put the chosen accent on one slab while retaining its surface texture and lighting continuity. Keep the other slabs in the resolved monochrome treatment.
- Let the object lead, followed by the supplied headline and small side or footer copy. The colored slab redirects attention within the object rather than adding a background decoration.

## Adaptation map

Use a supplied content photograph, when present, for the requested object's shape and surface. Without one, use the brief's description. Map each slice to its real location in that object, retaining diagnostic top and base features. Resolve count and stagger before rendering so separate pieces do not become duplicated complete objects.

## Adjustable slots and scoped sample values

| Slot | Archived sample value | Resolve for the current brief |
| --- | --- | --- |
| Object | Ripe pear with curved stem | Requested object and identifying top/base features |
| Slab count | Seven | Requested count; seven remains the local fallback when unspecified |
| Gaps and offsets | Slim warm-white gaps, alternating small shifts | Clear gaps and a stagger that preserves the combined outline |
| Accent | One green center slab | Chosen hue and chosen slab |
| Copy | Sample strings in the prompt files | Exact supplied wording, omitting unprovided side and footer copy |
| Format | Portrait 2:3 | Current canvas and image-field occupancy |

## Construction and handoff

In the SOP layout, establish the full subject silhouette and its type clearance. Mark the current slice count, gaps, offsets, and accent slab before detailed shading. Carry those current choices into the prompt, including the top-to-bottom continuity.

## Acceptance against the resolved brief

- The requested object reads as one whole at the resolved scale, with its diagnostic top and base visible.
- Exactly the resolved number of slabs appears in the correct order.
- Slim gaps and alternating offsets remain visible without destroying the overall contour.
- Exactly the resolved accent slab is colored, and its texture and light agree with the other pieces.
- Only supplied copy occupies the resolved headline, side, and footer regions.

## Prompt files and historical evidence

- [Archived Chinese sample prompt](prompt.zh.txt)
- [Archived English sample prompt](prompt.en.txt)

| Asset | Role | Record | Status |
| --- | --- | --- | --- |
| [Cell 07 crop](images/reference.png) | Style reference only | [Collection reference record](../reference.json) | The supplied sheet was visually inspected. Original publication, source image, model, entry, and settings are unknown. |
| [English submission](submitted.en.txt) | Prompt submitted for this attempt | Copied from [English prompt](prompt.en.txt) | SHA-256 matches the source prompt exactly. |
| [Generated poster](images/transfer-01.png) | Single built-in `image_gen` attempt | [Attempt record](example.json) | Inspected at 1024 × 1536 px; actual ratio is 2:3 as requested. |

The English prompt was run once through the built-in `image_gen` entry. The pear is centered and recognizable, with seven ordered slabs, visible warm-white gaps, and a readable left-right stagger. Only the fourth slab is green; the other six are grayscale. The title, right-side annotation, and both footer lines appear with the exact submitted wording. The Chinese prompt was not run. The model and repeatability are unknown; the tool response did not expose a model, and this record covers one attempt.
