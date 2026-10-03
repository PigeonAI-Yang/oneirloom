# Reserve Oneirloom custom-caption space

## Selection

Use this template when the user selects customizable-caption stickers, or wants an original layout with editable text. A fixed caption sticker can use the geometry without claiming LINE custom-sticker support.

## Source mechanism and local adaptation

[LINE's How to Make Custom Stickers](https://creator.line.me/en/guideline/customsticker/detail/) documents caption placement, font settings, set-wide style application, previews, and import or export of `custom-{sticker_id}.style`. It supports one custom caption per sticker and recommends space for the caption. Its four-to-six-character guidance is a recommendation, not an absolute limit.

Adapt the reserve-space method to [Oneirloom's identity](../../references/oneirloom-brand.md). The `.style` mechanism belongs to LINE's custom-sticker editor. Do not invent a file schema, hand-author a purported compatible file, or claim an export or import that has not happened. The source's example artwork and style files were not acquired.

## Select a caption reserve

Use a 1024 by 1024 local working square. Coordinates below are fractions of width and height, measured from the top-left. They describe local layout choices, not official platform geometry. Select actual target dimensions and supported text behavior through the [platform profiles](../../references/platform-profiles.md).

| Reserve | Caption bounds x, y | Character and net bounds x, y | Brand placement |
| --- | --- | --- | --- |
| Top greeting | x 0.12–0.88, y 0.06–0.22 | x 0.12–0.88, y 0.28–0.84 | Small fixed wordmark at x 0.35–0.65, y 0.90–0.95 |
| Left reply | x 0.06–0.38, y 0.28–0.60 | x 0.44–0.94, y 0.12–0.84 | Small fixed wordmark at x 0.54–0.84, y 0.90–0.95 |
| Bottom reassurance | x 0.12–0.88, y 0.75–0.89 | x 0.16–0.84, y 0.06–0.69 | Small fixed wordmark at x 0.35–0.65, y 0.94–0.98 |

Use one reserve per sticker. Treat the fixed Oneirloom wordmark as artwork, separate from the one customizable caption. If a layout makes the brand unreadable, use the actual brand lockup on the pack cover and omit the tiny sticker wordmark. Keep the caption clear of the antenna balls, navy window, star, four grips, and supported crescent.

Choose the caption language explicitly. For example, use the exact Chinese text "你好呀" or the exact English text "Hello" in separate intended variants. Do not silently translate the user's in-image text. Select a font with the required glyphs. Test the actual longest intended input and the selected editor's allowed length, line breaks, and fallback behavior. A character count alone does not predict a multilingual caption's width.

For LINE custom stickers, place the caption in the platform editor after producing the caption-free artwork. Export and import styles through that editor only when available and authorized. Preview every item after a set-wide style change because the same text box can collide with different poses.

## Resolved base-art prompt for the top greeting reserve

```text
Create a square Oneirloom greeting sticker base with an empty caption area across x 12 to 88 percent and y 6 to 22 percent of the canvas. Keep that caption reserve as uninterrupted white space. Place the entire character and net within x 12 to 88 percent and y 28 to 84 percent. Use a front view of a round periwinkle cocoon with small rounded tufts, two arched antennae ending in gold balls, a central uninterrupted navy oval window holding exactly one gold four-point star, and a short curled tail on its own left, visible on the viewer's right. Keep the periwinkle surface around the oval smooth and continuous. Give it exactly four small connected arms with mitten-like curled ends. Tilt the body slightly toward the viewer's left. Raise the upper-left arm while it grips its blue outer net thread. Keep the upper-right arm's separate grip at shoulder height. The two lower arms hold separate lower side threads and keep the net's lower support level. Rest one gold crescent moon on the visible woven blue hammock. Keep every arm origin and grip distinct. Use flat body and arm color #9994E8, window #25244C, star, antenna balls, and crescent #FFD873, blue threads #71B9E8, and black #000000 outlines. Place the exact fixed word "Oneirloom" within x 35 to 65 percent and y 90 to 95 percent, below the action. Use a plain white design-preview background, with lettering confined to the fixed word specified above.
```

For a fixed-caption rendering of this resolved layout, add the exact caption "你好呀" centered in the top reserve. Use rounded bold black lettering with a light outline. For a custom-caption output, keep that reserve empty in the base image and set "你好呀" as a preview input in the actual platform editor. Preserve the distinction in the delivery description.

## Check and evidence status

Inspect the real text preview for exact characters, spacing, clipping, and collisions. Test the longest intended caption in each selected language. Confirm that style reuse preserves the reserve while the four net grips and single star remain clear. Check actual exports against the selected profile. Claim `.style` portability only after a real editor export and import succeeds.

Status: six local image examples are available: three uncaptioned bases and three fixed-caption renderings. They are not LINE-customizable stickers; no `.style` file, multilingual render, or platform import has been produced or tested.

## Local production evidence — 2026-10-03

The [review preview](../../assets/generated/custom-caption-layout/review-light-dark-128-384.png) shows three uncaptioned bases and three fixed-caption examples. The [production record](../../assets/generated/custom-caption-layout/production.json) retains the selected files and known limitations. These are fixed-caption raster examples, not editor-controlled stickers.

The local examples were produced or reused and inspected on 2026-10-03. Native reaction files are 1254 × 1254 RGBA PNGs with an actual alpha channel. These are working masters, not verified platform imports. AI inspection does not establish recipient comprehension, platform acceptance, or animation behavior. Actual prompts, known entry settings, selected paths, and visual limitations are retained in the linked production record. Light/dark review at 128 and 384 px is recorded there.
