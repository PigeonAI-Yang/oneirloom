# Arrange an eight-slot Oneirloom workspace

## Selection

Use this template when an editor with layers and saved selections can hold eight reactions in one source document. Keep individual exports as the delivery target. A filled sheet is still a preview until each file is exported and inspected.

## Source mechanism and local adaptation

[UTK's 8 template slots for LINE stickers](https://assets.clip-studio.com/en-us/detail?id=2232417) is a listed free CLIP STUDIO PAINT PRO/EX layer template. Its text describes eight slots, a masked Drawing folder, draft layers excluded from export, and selection-based export after merging layers. The listing was read, but its source file was not downloaded or imported. Its exact grid geometry was not visually verified. The linked Auto Action was not tested.

The four-column, two-row arrangement below is an original local choice. Use the editable [Oneirloom workspace](workspace.svg) as a blank worksheet. Do not claim it is UTK's geometry or redistribute the original material. Follow the [Oneirloom brand reference](../../references/oneirloom-brand.md) and use the approved front mascot. Select export requirements through the [platform profiles](../../references/platform-profiles.md).

## Set up the local workspace

The SVG canvas is 2184 by 1288 pixels. It contains eight 512 by 512 working cells in a four-column, two-row grid, with 24-pixel gutters and 32-pixel left and right margins. The first row begins at y = 160 below the brand header; the second begins at y = 696. Keep the existing 40-pixel internal guide in each cell. These are local authoring dimensions, not LINE submission dimensions. The half-open cell bounds below use the full SVG canvas origin, not the grid origin.

| Slot | Cell bounds x, y | Local intent | Concrete pose |
| --- | --- | --- | --- |
| 01 | 32–544, 160–672 | Hello | Lift the upper-left thread grip; keep the other upper grip steady and the lower pair level beneath the crescent |
| 02 | 568–1080, 160–672 | Receipt | Keep the body upright; hold upper threads evenly and lower threads close in a small level net |
| 03 | 1104–1616, 160–672 | Thanks | Bow the body; gather the upper rim and lower side threads close around the supported crescent |
| 04 | 1640–2152, 160–672 | Question | Tilt the body and antennae unevenly; offset the upper grips while the lower pair keeps the crescent level |
| 05 | 32–544, 696–1208 | Celebrate | Lift the body; raise and spread upper grips while lower grips open a broad shallow crescent cradle |
| 06 | 568–1080, 696–1208 | Tired | Compress the body and droop the antennae; lower all four grips while keeping the moon-bearing net above the cell edge |
| 07 | 1104–1616, 696–1208 | Affection | Lean toward the crescent; bring the upper rim close and cup the lower support without covering the star |
| 08 | 1640–2152, 696–1208 | Good night | Settle the body behind the net; lower upper grips and draw lower grips inward to deepen the hammock |

Keep exactly four connected arms in every cell. Each arm holds its own net thread. The blue hammock carries only the character's existing gold crescent.

1. Use the existing `slot-01` through `slot-08` containers and their empty `art-01` through `art-08` groups. The corresponding editor display names may be `01-hello`, `02-receipt`, `03-thanks`, `04-question`, `05-celebrate`, `06-tired`, `07-affection`, and `08-goodnight`. These logical names are not IDs already present in the SVG.
2. Author inside each `art-NN` group. The groups use full-canvas coordinates without a local translation. For 512-square artwork authored at a local origin, translate a nested artwork group to the cell's listed x and y origin. Keep the existing `art-NN` group and `clip-slot-NN` clip in full-canvas coordinates. Add separate draft and optional caption layers only in the working editor as needed.
3. The existing `clip-slot-NN` paths bound each full 512-square cell. Treat the 40-pixel inset as a composition guide rather than a second hard crop. Keep antennae and threads complete inside the cell.
4. Save a rectangular selection for each listed full-cell rectangle as `export-01` through `export-08`. The 24-pixel gutters, header, and outer margins are outside those rectangles. Exclude `guides`, `cell-surfaces`, `sheet-background`, header elements, and drafts from individual exports. Continuous 512-pixel cuts from the sheet origin do not match these cells.
5. Preserve the editable source. Merge or flatten a copy only when the selected export method needs it.
6. Export each saved selection into an individual file using the chosen platform profile. Inspect every export for crop, dimensions, and real alpha when required.

Keep the actual brand lockup in the worksheet header outside the eight export cells. Individual stickers can carry a small Oneirloom wordmark below the action if it remains legible and fits the selected brief. The SVG worksheet's blank art layers are places to author poses, not finished reactions. Its [PNG preview](workspace-preview.png) includes opaque cell surfaces for browsing; neither that preview nor a white-background prompt establishes alpha in an individual export.

## Resolved prompt for the 02-receipt artwork

```text
Draw one standalone Oneirloom received-message reaction for a square workspace cell. Show the front of a round periwinkle cocoon with small rounded tufts, two arched antennae with gold ball tips, a central uninterrupted navy oval window containing exactly one gold four-point star, and a short curled tail on the character's own left, visible on the viewer's right. Keep the periwinkle surface around the oval smooth and continuous. Keep the body upright and dip the antenna tips slightly forward. Give it exactly four small connected arms with mitten-like curled ends. The upper-left and upper-right arms grip separate upper outer blue threads at equal height. The lower-left and lower-right arms grip separate lower side threads close to the body. Form a small level woven blue hammock with one gold crescent moon visibly resting in its center. Keep all four grips and the star clear. Use flat colors: body and arms #9994E8, window #25244C, star, antenna balls, and crescent #FFD873, threads #71B9E8, outlines #000000. Place the exact caption "收到" above the antennae in rounded black lettering with a light outline. Put the exact word "Oneirloom" in a smaller line beneath the net, clear of the threads. Keep all artwork inside the central 84.375 percent of the square. Use a plain white design-preview background.
```

## Check and evidence status

Confirm eight groups, eight saved selections, and eight independent exported files only after those objects exist. Check selection boundaries and excluded draft layers. Check every sticker individually, then compare the overview for visual consistency. A masked source or successful export command does not prove clean edges.

Status: a local authoring demonstration places eight reused native PNGs in a filled SVG as editable raster images. The original blank worksheet remains unchanged. Sticker artwork stays raster; no CSP file, imported UTK material, saved editor selections, or platform export has been tested.

## Local production evidence — 2026-10-03

Eight selected native PNGs were byte-copied into the [filled SVG demonstration](../../assets/generated/eight-slot-workspace/filled-workspace.svg); the [original blank worksheet](workspace.svg) remains blank. The [preview](../../assets/generated/eight-slot-workspace/preview.png) and [production record](../../assets/generated/eight-slot-workspace/production.json) document the local authoring result. The SVG provides editable raster placement, not vector sticker artwork or a PSD.

The local examples were produced or reused and inspected on 2026-10-03. Native reaction files are 1254 × 1254 RGBA PNGs with an actual alpha channel. These are working masters, not verified platform imports. AI inspection does not establish recipient comprehension, platform acceptance, or animation behavior. Actual prompts, known entry settings, selected paths, and visual limitations are retained in the linked production record. Light/dark review at 128 and 384 px is recorded there.
