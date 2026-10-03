# 11. Transparent botanical

Read the [collection contract](../template.md) before adapting this recipe. It binds the sample slots and the checks below to the current brief and the shared graphic-design SOP.

## Selection conditions

Choose this recipe when translucency, internal structure, and layered botanical forms should carry an airy editorial composition.

## Source observations and uncertainty

The [style crop](images/reference.png) shows blue translucent petals spread across the upper and central field, darker centers and overlaps, fine vein-like lines, and slender stems descending toward the footer. Smaller floral forms sit below the largest bloom. Sparse notes occupy the corners and open side areas.

The crop does not establish species, an exact count of distinct blooms, creator, font, model, or production process. "X-ray-like" describes an appearance. Medical X-rays and cyanotype are unverified. Two irises and a roughly two-thirds-width arrangement are the archived sample's explicit choices, not source facts.

Source metadata remains in the [collection reference record](../reference.json).

## Defining mechanism and relational anchors

- Spread the floral arrangement through the upper and middle image field, with stems descending toward a separate bottom type region. Keep pale space around and within the arrangement.
- Render petals as thin translucent layers through which the paper and finer internal structures remain visible.
- Deepen the chosen hue where petals overlap. Concentrate the darkest values at centers and crossings, with fine stems linking the forms.
- Arrange the current number of blooms with a clear size hierarchy. Keep each requested bloom distinguishable when count matters.
- Let the translucent image lead. Small supplied labels occupy clear side or corner regions, with a restrained footer below.

## Adaptation map

Map the source's translucent membranes and visible veins to the requested botanical structure. Resolve the actual species, count, relative sizes, and arrangement independently of the source crop's ambiguous overlap. For other translucent subjects, name the equivalent thin layers and internal structures rather than borrowing flower anatomy.

## Adjustable slots and scoped sample values

| Slot | Archived sample value | Resolve for the current brief |
| --- | --- | --- |
| Subject and count | Two iris blooms, larger above smaller | Requested species or subject, current count, and size hierarchy |
| Image width | Roughly two-thirds of page width | Current occupancy, outer clearance, and visible stems |
| Layer treatment | Translucent blue petals, navy centers and stems | Chosen palette, visible internal structures, and overlap darkening |
| Copy | `VISIBLE` / `WITHIN`; `Layers` / `Light` / `Structure`; `FIELD 11`; `Botanical study` | Exact supplied labels and footer/caption roles |
| Format | Portrait 2:3, airy off-white field | Requested canvas and pale field |

## Construction and handoff

In the SOP layout, resolve the number of forms, their size hierarchy, stem paths, image width, and clear type regions. Specify those before translucent detail. The prompt must state where overlap darkens and where the paper stays visible through the layers.

## Acceptance against the resolved brief

- The requested subject and resolved count remain distinct within the agreed arrangement.
- The image fits the current occupancy target and leaves the resolved pale margins and type clearance.
- Thin layers reveal internal structure and the paper beneath, with darker intersections.
- The selected palette serves translucency. A solid blue silhouette does not meet this treatment.
- Exact supplied labels retain the image-first hierarchy. The historical v2 width is an observation, not a replacement for the current target.

## Prompt files and historical evidence

- [Archived Chinese sample prompt](prompt.zh.txt)
- [Archived English sample prompt](prompt.en.txt)

The first English attempt (v1) used the style reference once; see [first-attempt prompt](submitted.en.txt), [first-attempt result](images/transfer-01.png), and [first-attempt run record](example.json). V1 shows three distinct flower heads and floral artwork spanning about 90% of the poster width, so it missed the requested two blooms and roughly two-thirds width. A single built-in `image_gen.imagegen` edit (v2) of transfer-01.png was run with [the saved edit prompt](submitted-v2.en.txt); the selected corrected result is [the v2 result](images/transfer-02.png), with its [v2 run record](example-v2.json) identifying transfer-01.png as the edit target. Visual inspection confirms two iris heads, one large above one smaller, each with upright inner petals, three broader drooping outer petals, and its own fine curved navy stem. The translucent blue membranes, visible veins, dark overlaps, navy centers, paper grain, and all specified wording and placements are preserved. Approximate saturated-blue artwork bounds are x=118..872 of 1024 pixels (about 73.7% of the width), close to but somewhat wider than two-thirds. The output PNG is opaque RGB; translucency is visual. The tool response did not expose the underlying model. The Chinese prompt remains untested, and repeatability is unknown.
