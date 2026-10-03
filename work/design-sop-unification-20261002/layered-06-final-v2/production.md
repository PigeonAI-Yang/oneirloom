# Layered 06 v2 production evidence

Status: **partial, awaiting Primary review.** One permitted asset generation and one fixed-geometry composition are complete. The lower right image and lower left fragment now reach their required endpoints. The left upper occupied contour still misses the draft, and the right fit requires a large panel and star. This is a reviewable poster, not accepted completion.

## Fixed design and declared adaptations

The geometry source is `../layered-06-proof/adapted-layout.svg`, 1450 × 2040. Paper `#F4F0E8`, cobalt `#4164D8`, panel x 826.5 / width 507.5, and the 116 px right paper border are unchanged. All three editable text elements retain their draft text, Impact font, sizes, baselines, textLength and lengthAdjust. DREAM and WEAVER remain the chosen two-word adaptation of the reference's four-line headline; unsupported small copy is omitted. The left contour, all six rectangular windows and the right path are unchanged. Gray fills, cue ellipses and chevrons are removed.

One photographic identity supplies the continuous right view and a mirrored graphic duplicate on the left. This mirror is a declared composition decision, not a verified new three-dimensional character view. The crop preserves fur, the indigo fabric oval and the single antique-gold four-point star. The sling, crescent, complete body outline and limbs are outside this local identity adaptation. Fragment x offsets remain +14, 0, -16, +16, -16, +14 px.

## Asset generation and prompt comparison

The built-in `image_gen.imagegen` entry was called exactly once with `transparent_background: true`. Input 1 was the previous photographic right-facing asset for pose and material; input 2 was the approved frontal identity. Neither the poster nor its blue/layout draft was supplied to the generator. The complete equivalent Chinese and English asset prompts and exact `submitted.en.txt` are preserved. The generator's model identifier was not exposed and remains unknown.

The native result is copied without pixel edits to `subject-right.png`: 1024 × 1536 RGBA; SHA-256 `82fe1fa940c5398c960861f70b083c142c9b35d0716ad6a042d132b724aa4071`. Alpha ranges from 0 to 254; 24.253% of pixels are fully transparent. Corner alpha is 0, 0, 0, 1. The alpha >127 bounding box is (15, 35, 1016, 1536). Background RGB visible in a raw preview does not constitute an opaque backdrop: the actual compositing uses native alpha. No alpha repair, fur-strip repetition, pixel stretching or synthetic body extension was performed.

The inspected asset retains the gray-lilac fur, indigo woven panel, antique-gold four-point star, rounded left back, right-facing three-quarter volume, compact tuft/antennae and continuous genuine lower fur. It has no human face or neck. The broad lower body continues through the native bottom edge.

Measured visual estimates: star center (765, 596), bounding box approximately (699, 500, 831, 692). Its width is 12.89% of the asset, within the requested 10–13%. Its center is at 38.80% height, missing the requested 22–28%. The panel still spans approximately y 395–830, rather than sitting within the upper third. Consequently the asset prompt is only partially matched. The new usable lower expanse improves on v1 but does not independently prove the full fixed composition can be filled at the desired feature scale.

## Assembly and actual coverage

The native image is embedded in editable SVG. Right: uniform scale 2.3, translation (-703.5, -690.8), estimated star center (1056, 680), native image bottom y 2842. Left: mirrored uniform magnitude 1.65, base translation (1885.75, -616.2), estimated star center (623.5, 367.2), native image bottom y 1918.2. The right star is shifted 60.5 px left and 13.6 px up from the draft cue; its displacement magnitude is approximately 62 px, with each axis inside the approximately 0.03H placement allowance. Its projected star bounding box is approximately 304 × 442 px. The left star is approximately 218 × 317 px. There is no anisotropic warp. The stars remain recognizable; the intended horizontal left seam crosses the upper ray, and the rightmost star tip is close to the fixed right contour.

Canvas endpoints alone were not used to establish coverage. The renderer separately rasterized the target masks and actual image layers, thresholded rendered alpha at >127, and counted actual occupied target pixels:

| Area | Actual occupied fraction |
| --- | ---: |
| Entire right contour | 99.838% |
| Right, y 0–551 | 99.529% |
| Right, y 1900–2040 | 99.879% |
| Entire left masked windows | 87.820% |
| Left upper windows, y 0–551 | 85.694% |
| Left lower window, y 1326–1490 | 97.410% |

The right occupied bounds reach y 2040 and the left bounds reach y 1490. Tiny edge differences include alpha fringe and raster thresholds. The major remaining discrepancy is not such an edge effect: approximately 31,658 pixels of the left upper target remain unoccupied. The intended left contour begins near x 259, while the actual occupied left view begins at x 316 overall and substantially farther right along its top. The broad rounded upper mass is visibly reduced to a narrower sloping crop. The large indigo panels also dominate the photograph more than the requested small, high panel arrangement. The right upper area is filled with crown fur without the isolated dangling antenna remnant seen in v1.

The lower-coverage defect is repaired in this composition. Full asset usability against the fixed draft remains partial because left upper coverage and desired panel/star scale are not both achieved. No second generation or alternate layout strategy was attempted after this evidence.

## Source, draft and result comparison

The original 06 reference, the approved draft and the actual final PNG were inspected side by side at the same 720 px visual height with aspect ratios preserved. The right-biased continuous mass, central division, lower narrowing and bottom contact, blue field with right paper border, dark left title and horizontal fragmented left treatment are visible. The typography departure was already selected in the draft. The final right occupied contour closely follows that draft. The final left upper mass still misses the draft's rounded broad contour. Therefore this is a partial layout transfer, not exact source fidelity. The observation makes no general claim about model capability or repeated reliability.

## Reproducible checks and delivered files

`python work/design-sop-unification-20261002/layered-06-final-v2/render.py` uses existing Python Playwright and installed Microsoft Edge. It renders the actual SVG to 1450 × 2040 PNG, awaits fonts and embedded-image decode, opens the single-poster preview, and measures occupied alpha against the unchanged masks. Impact is available; text is exactly DREAM, WEAVER, ONEIRLOOM. Browser page errors are empty. The SVG document extent is exactly 1450 × 2040 with no overflow; the preview image decodes and has no horizontal overflow. Draft elements and all fragment windows pass preservation comparisons. Technical checks pass, while visual status remains partial and overall acceptance is false.

Files: `poster.svg`, `poster.png`, `preview.html`, `subject-right.png`, `render.py`, `asset-prompt.zh.txt`, `asset-prompt.en.txt`, `submitted.en.txt`, `generation.json`, `assembly-checks.json`, and this evidence record. `generation.json` records actual controls, native source path, hashes, dimensions, transparency and unknown model. `assembly-checks.json` records transforms, geometry comparisons, alpha coverage, browser evidence and output hashes. Earlier v1 assets and records are unchanged. The Primary owns the next decision and acceptance.
