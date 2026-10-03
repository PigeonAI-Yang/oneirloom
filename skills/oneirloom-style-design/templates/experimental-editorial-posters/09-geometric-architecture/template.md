# 09. Geometric architecture

Read the [collection contract](../template.md) before adapting this recipe. It binds the sample slots and the checks below to the current brief and the shared graphic-design SOP.

## Selection conditions

Choose this recipe when a building or constructed form provides strong converging lines and a diagonal crop that can interact with one flat color plane.

## Source observations and uncertainty

The [style crop](images/reference.png) shows a low-angle monochrome building rising through sharp diagonal image regions. A large orange triangle occupies the upper-left area behind parts of the photograph. The photo reaches the side of the image field and continues down toward a broad footer. Small notes occupy the upper right and a lower-left gap.

The building's exact identity, source creator, model, and font are unknown. The exposed-concrete museum and about 15% orange coverage are archived sample decisions, not source measurements.

Source metadata remains in the [collection reference record](../reference.json).

## Defining mechanism and relational anchors

- Fill the central image field with an upward-looking architectural photograph. Crop the facade into angular regions whose edges reinforce its perspective.
- Let the photo extend to selected page edges. Preserve connected facade lines across the visible parts so it reads as architecture rather than unrelated polygon fragments.
- Place one flat accent triangle in the upper-left field. Overlap it with the architecture so the photograph visibly passes in front of part of the color plane.
- Anchor the diagonal movement with a large horizontal footer below. Place supplied small notes in the remaining upper-right and lower-left paper spaces.
- Read the diagonal building and broad footer before the small notes.

## Adaptation map

Map the source facade to the requested building's recognizable openings, structural edges, or material divisions. Resolve a view in which those elements support a coherent upward diagonal. Do not invent a building's use from its appearance. For a different object, identify equivalent real structural planes and label the adaptation.

## Adjustable slots and scoped sample values

| Slot | Archived sample value | Resolve for the current brief |
| --- | --- | --- |
| Subject | Exposed-concrete art museum | Requested structure and visible identifying features |
| View and crop | Low-angle diagonal photo mask | Perspective direction, clipped edges, and continuity lines |
| Accent | Orange upper-left triangle, about 15% page area | Chosen hue, area, and the portion hidden by the photo |
| Copy | `Different` / `angles` / `New` / `possibilities`; `Space` / `Form` / `Light`; `NEW ANGLES`; `FIELD 09` | Exact supplied copy and footer/side-note roles |
| Tone and format | Grayscale photo, warm paper, portrait 2:3 | Current palette and canvas |

## Construction and handoff

At the SOP layout stage, draw the facade's main directional lines, the angular photo mask, the triangle behind it, and the bottom type baseline. Carry the photo-over-triangle overlap into the prompt. Add architectural surface detail only after those regions and the type clearance work together.

## Acceptance against the resolved brief

- The requested structure retains the named visible features and coherent perspective.
- The diagonal photo crop and building lines reinforce the same upward movement.
- One chosen accent triangle is partly hidden behind the photograph at the resolved size.
- The broad footer and supplied small copy occupy their agreed regions with exact wording.
- Do not count an inferred building function as visually confirmed identity.

## Prompt files and historical evidence

- [Archived Chinese sample prompt](prompt.zh.txt)
- [Archived English sample prompt](prompt.en.txt)

| Asset | Role | Record | Status |
| --- | --- | --- | --- |
| [Cell 09 crop](images/reference.png) | Style reference only | [Collection reference record](../reference.json) | The supplied source cell was visually inspected. The original creator, model, and font are unknown. |

An earlier version of the English prompt was submitted verbatim once through the built-in image_gen.imagegen entrypoint: [submitted prompt](submitted.en.txt), using the [cell 09 style reference](images/reference.png). After that run, the current prompt baseline was revised to use affirmative wording while preserving the visual intent; this current baseline was not resubmitted verbatim. The saved result is [transfer-01.png](images/transfer-01.png); [example.json](example.json) records the tool response and visual inspection. The poster is 1024 x 1536 px, matching the requested 2:3 ratio. Inspection confirms the low-angle concrete facade, diagonal photo crop, orange triangle behind the photo, upper-right note column, lower-left note, large NEW ANGLES footer, and tiny FIELD 09; all requested copy is present with no extra text. The building reads as contemporary exposed-concrete architecture, while its museum function is not independently identifiable. The Chinese prompt remains unrun, and repeatability is unverified.
