# 08. Zine silhouette

Read the [collection contract](../template.md) before adapting this recipe. It binds the sample slots and the checks below to the current brief and the shared graphic-design SOP.

## Selection conditions

Choose this recipe when an enlarged profile and expressive hand lettering should dominate a rough monochrome poster.

## Source observations and uncertainty

The [style crop](images/reference.png) shows a dark animal-head profile facing right, enlarged beyond the left and bottom page edges. Its ear rises close to the top. The muzzle projects into a pale right margin. Large purple handwriting crosses the dark lower-middle mass, with small notes on the open right and a thin purple underline near the bottom.

"Zine" and "photocopy" describe the visible texture and lettering relationship. They do not establish the original production process. The source creator, lettering typeface, and model are unknown.

Source metadata remains in the [collection reference record](../reference.json).

## Defining mechanism and relational anchors

- Crop the back and lower extent of the profile at the left and bottom edges. Keep the diagnostic ear, muzzle, and facing direction legible.
- Maintain a large dark image mass against a narrow pale right region. Rough copier grain and broken-ink edges add texture without erasing the outline.
- Cross the lower-middle silhouette with oversized accent-colored handwriting. The letters must visibly sit on the image, not retreat into a separate clean headline box.
- Use the same accent for the associated underline. Keep any supplied right-side note and footer small.
- Read the profile first, the crossing phrase next, then the small copy.

## Adaptation map

Map the source animal's direction and outline to the requested animal or profile subject. Name the diagnostic shape that distinguishes that subject from similar ones. Keep the large edge crop while retaining that feature. A fox needs a long tapered muzzle; the source's short feline muzzle is not an identity default.

## Adjustable slots and scoped sample values

| Slot | Archived sample value | Resolve for the current brief |
| --- | --- | --- |
| Subject | Right-facing fox, pointed ears and tapered muzzle | Requested subject and diagnostic profile shape |
| Crop | Large profile across most of the page | Back/lower edge crop and open right margin |
| Main lettering | `STAY` / `CURIOUS`, purple marker | Exact supplied phrase, line breaks, and chosen accent |
| Small copy | `SEE` / `MORE`; `FIELD 08` / `A poster study` | Supplied note/footer only |
| Format and texture | Portrait 2:3, coarse copier grain | Requested canvas and readable grain strength |

## Construction and handoff

In the SOP layout, establish the cropped silhouette and right margin, then draw the handwriting block across the dark mass. Check the diagnostic profile before adding grain. The resolved prompt must state both the required subject feature and the lettering/image overlap.

## Acceptance against the resolved brief

- The requested subject is identifiable from its diagnostic profile, not merely from the prompt's label.
- Its back and lower mass meet the agreed frame edges, while the directional outline remains clear.
- The supplied marker phrase crosses the silhouette at the resolved scale and uses the chosen accent.
- Grain leaves the outline and lettering readable. Any small right-side copy stays subordinate.
- A related but different animal, as in the historical cat-like first result, fails the current subject requirement.

## Prompt files and historical evidence

- [Archived Chinese sample prompt](prompt.zh.txt)
- [Archived English sample prompt](prompt.en.txt)

| Asset | Role | Record | Status |
| --- | --- | --- | --- |
| [Cell 08 crop](images/reference.png) | Style reference only | [Collection reference record](../reference.json) | Local crop and collection record are present; used as style reference only. |
| [First generated poster](images/transfer-01.png) | Initial English-prompt sample; reference used for style only | [Submitted English prompt](submitted.en.txt), [inspection record](example.json) | One built-in generation; the short feline muzzle and prominent whiskers make it read as a cat rather than an unmistakable fox. |
| [Edited poster](images/transfer-02.png) | Single subject-correction edit, using the first poster as the edit target | [Submitted edit prompt](submitted-v2.en.txt), [edit record](example-v2.json), edit target [transfer-01](images/transfer-01.png) | One built-in edit call; visually inspected at 1024 × 1536 px; underlying model unknown. |

### Subject check

The first result reads as a cat-like feline: its muzzle is short and rounded, and the long whiskers reinforce that reading, so the intended fox did not transfer clearly. The single edit result has two tall triangular ears and a long narrow, tapered muzzle projecting well past the cheek to a small canine nose; its sloping bridge and shaggy cheek and neck fur make the profile read as a fox. The six requested strings remain visible and correctly spelled, with the purple two-line headline and underline, right-side note, and lower-left footer in their established regions. This is a visual comparison, not a pixel-level preservation check.

The original English prompt and first result remain filed with their inspection record; the edit prompt, edit target, result, and one-call inspection are filed with the edit record. The Chinese prompt was not run, and repeatability is untested. The source creator, lettering typeface, underlying model, and generation settings remain unknown.
