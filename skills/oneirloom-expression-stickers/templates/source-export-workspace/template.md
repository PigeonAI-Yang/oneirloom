# Prepare Oneirloom editable source and exports

## Selection

Use this template when the deliverable includes an editable source or repeatable exports. Select the actual drawing editor and target platform before making source-format or packaging claims.

## Source mechanism and local adaptation

[Okayama's Part 1. Let's Create a LINE Sticker With Clip Studio Paint](https://tips.clip-studio.com/en-us/articles/1579) explains a canvas preset, a masked layer folder to preserve margins, proportional scaling of canvas and mask, and repeated export settings recorded as an Auto Action. It also describes numbered sticker files, `main.png`, `tab.png`, and a ZIP package. This is a documented method, not a verified downloadable source template. Historical numerical requirements in that tutorial are not current platform authority.

Adapt the repeatable workspace to [Oneirloom's identity](../../references/oneirloom-brand.md). Use the [platform profiles](../../references/platform-profiles.md) for the selected route. The editable file is the source; exported stickers, a pack cover, and a chat tab are distinct outputs. Do not impose LINE's supporting images or ZIP convention on other routes.

## Prepare a usable source

1. Choose a 1024 by 1024 working canvas for a square reaction. This is a local drawing choice. For a different target aspect ratio, preserve that ratio in the working source.
2. Keep the approved mascot reference available beside the canvas. Draw a front-view reaction with four connected arms and a moon-bearing blue net.
3. If editable layers are requested, separate the body, navy window, gold details, blue net, outlines, and caption in the selected editor. Keep each color part editable without treating a flattened raster as vector source.
4. Add a margin guide for the chosen profile. Use a mask only when clipping or a repeated export workflow needs it. If the working canvas is scaled, scale the guide and mask with it.
5. Preserve the editor-native source. Create an export copy when merging is necessary. Record the actual export settings only after selecting the route.
6. Reuse a proven preset or Auto Action when the selected editor supports it. Inspect the first exported reaction before applying those settings to the remaining items.

Use descriptive working names such as `oneirloom-thanks-source` and `oneirloom-thanks-preview`. Let the editor supply its actual native extension. Do not rename a raster file to `.psd` or `.clip`.

| Output | Local content choice | Route-dependent handling |
| --- | --- | --- |
| Individual reaction | One complete body, four connected arms, explicit net-support grips, supported crescent, and any exact caption | Use the selected route's dimensions, alpha, format, and count. Number files only where the route expects that convention |
| Main or pack image | A representative Oneirloom pose with the actual brand lockup outside the action | Use `main.png` only when required or accepted by the selected LINE route. Compose it separately rather than assuming a sticker crop fits |
| Chat tab or picker image | A compact crop that preserves the navy window and single star, plus enough silhouette to identify the character | Use `tab.png` only for a route that needs it. Avoid unreadable miniature captions |
| Editable source | The actual source document with retained layers requested by the brief | Name the real editor and format. Do not claim compatibility without opening or importing it |
| Delivery package | Only the requested and inspected outputs | Create a ZIP only when the selected route or user requests one |

Use the actual [brand lockup](../../assets/brand-lockup.svg) for a pack image or package cover. Do not put it over the four grips, net, or star. Native alpha settings belong to the chosen production entry, not to a promise in prompt text.

## Resolved source-art prompt

```text
Create one square Oneirloom thank-you sticker illustration. Show the front of a round periwinkle cocoon with small rounded tufts, two arched antennae with gold ball tips, an uninterrupted navy oval window holding exactly one gold four-point star, and a short curled tail on its own left, visible on the viewer's right. Keep the periwinkle surface around the oval smooth and continuous. Give the character exactly four connected small arms with mitten-like curled ends. Bow the body slightly and bend the antennae toward the net. The two upper arms each grip a separate upper outer blue thread and draw the rim inward. The two lower arms each grip a separate lower side thread and gather the hammock close to the body. One gold crescent moon rests on the woven blue threads in the center. Keep the four arm origins, four grips, and single star readable. Use flat fills with body and arms #9994E8, window #25244C, star, antenna balls, and crescent #FFD873, threads #71B9E8, and black #000000 outlines. Set the exact caption "谢谢你" in rounded black lettering with a light outline above the antennae. Put a small "Oneirloom" wordmark beneath the net, separated from its threads. Use a plain white design-preview background and leave a clear margin around the complete artwork.
```

This prompt specifies visible artwork. Build editable layers in the chosen editor when the brief requires them. The prompt alone does not provide a layered file.

## Check and evidence status

Open the actual source and confirm the claimed layers. Inspect the individual exports for identity, lettering, alpha where required, dimensions, and complete edges. Check the main image and tab separately when the route needs them. Package only files that exist, and distinguish file inspection from platform import or review acceptance.

Status: a local source/export demonstration reuses one PNG in an editable raster-placement SVG. The SVG is not vector sticker artwork or a PSD. No CSP or PSD template, Auto Action, ZIP, or platform submission is supplied or tested here.

## Local production evidence — 2026-10-03

One native reaction PNG byte-copied from [Daily Sixteen D04](../../assets/generated/daily-sixteen/D04.png) is available alongside an [editable SVG placement source](../../assets/generated/source-export-workspace/editable-source.svg). The [preview](../../assets/generated/source-export-workspace/preview.png) and [production record](../../assets/generated/source-export-workspace/production.json) record this authoring demonstration; they do not establish vector artwork, PSD layers, or a platform export.

The local examples were produced or reused and inspected on 2026-10-03. Native reaction files are 1254 × 1254 RGBA PNGs with an actual alpha channel. These are working masters, not verified platform imports. AI inspection does not establish recipient comprehension, platform acceptance, or animation behavior. Actual prompts, known entry settings, selected paths, and visual limitations are retained in the linked production record. The source/export record documents full/native inspection and light/dark picker review at 128 px. Its 384 px review belongs to the reused Daily D04 source record, not this demonstration.
