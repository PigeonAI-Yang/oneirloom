# 04. Torn landscape

Read the [collection contract](../template.md) before adapting this recipe. It binds the sample slots and the checks below to the current brief and the shared graphic-design SOP.

## Selection conditions

Choose this recipe when one continuous landscape and a large condensed headline can share an image-to-type junction. Torn bands disrupt the scene while preserving its geographic continuity.

## Source observations and uncertainty

The [style crop](images/reference.png) shows grayscale mountains across the upper field, interrupted by horizontal ragged white seams and slight offsets. The large word `FRAGMENTS` occupies the lower-middle field. A yellow note crosses the right side of the image/type junction, above quiet bottom copy.

The small raster does not establish an exact count of source cuts or a physical tearing process. Three strips are the archived coastal sample's construction choice. The source creator, model or entry, and typeface are unknown.

Source metadata remains in the [collection reference record](../reference.json).

## Defining mechanism and relational anchors

- Spread one scene across the upper image field, reaching close to the side edges. Divide it with horizontal irregular paper gaps, keeping landmarks aligned enough to read as one scene.
- Apply small distinct offsets to the bands. The fragments retain their top-to-bottom order and scene continuity.
- Give the condensed headline a broad lower-middle block directly adjoining the image. It leads the reading order, followed by the fragmented scene and the small accent note.
- Place the accent note across the right image/type junction. It belongs to that joint rather than floating in unrelated empty space.

## Adaptation map

Map the mountain contours to the new landscape's horizon, cliffs, buildings, or other connected landmarks. Choose a band count and offsets that preserve those connections. Map the source headline to the supplied wording, resolving line breaks and width together instead of copying its letter count.

## Adjustable slots and scoped sample values

| Slot | Sample value | Resolve for the current brief |
| --- | --- | --- |
| Landscape | Coastal cliffs and breaking waves | Requested scene and continuity landmarks |
| Bands | Three strips with small different offsets | Current count, gaps, and offset directions |
| Headline | `COAST` / `LINES`, about 80% page width | Exact wording, line breaks, and resolved block width |
| Note | Yellow, below 10% page area; `Edges` / `keep` / `changing` | Chosen accent and supplied note, if any |
| Footer and format | `FIELD STUDIES`, portrait 2:3 | Supplied footer and requested format |

Counts, shifts, percentages, and sample copy are design choices, not exact source measurements.

## Construction and handoff

In the SOP layout, mark the scene bands, headline block, and their shared junction. Fit the requested title before fixing note placement. The resolved prompt must state the current band count and the landmarks that continue across the gaps.

## Acceptance against the resolved brief

- The requested landscape remains one coherent scene through the agreed number of offset bands.
- Ragged white gaps visibly interrupt the image without scrambling its natural order.
- The headline reaches the resolved width and leads the hierarchy. Compare against that current target, not the historical 70–75% result.
- Any supplied note sits at the agreed junction and stays subordinate to the headline.

## Prompt files and historical evidence

- [Archived Chinese sample prompt](prompt.zh.txt)
- [Archived English sample prompt](prompt.en.txt)

One English sample was generated with the built-in image_gen entry using the exact prompt archived in [submitted.en.txt](submitted.en.txt). At the time of that run, the archived prompt matched [prompt.en.txt](prompt.en.txt) byte for byte; after the run, the current prompt baseline was revised to remove exclusion wording while preserving the visual intent. The current prompt baseline was not resubmitted verbatim, so the archived sample and inspection evidence below apply to submitted.en.txt only. The tool response did not identify a model. The archived [sample](images/transfer-01.png) is 1024 × 1536 px, matching the requested 2:3 portrait ratio; see the [inspection record](example.json).

Visual inspection found three slightly offset grayscale coastal strips with irregular fibrous white gaps, a warm paper field, a yellow torn note, and the lower-left footer. “COAST” / “LINES”, “Edges” / “keep” / “changing”, and “FIELD STUDIES” render exactly. The widest headline line appears about 70–75% of the canvas width, slightly short of the requested about 80%; the coast also has grainy photographic detail. The Chinese prompt has not been tested, and repeatability remains unknown from one result.
