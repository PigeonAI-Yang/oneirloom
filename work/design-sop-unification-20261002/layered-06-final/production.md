# Layered 06 production evidence

Status: **partial — the asset and editable assembly are rendered and inspected; the poster fails photo coverage and is not accepted.** The single permitted generation and initial fixed-geometry composition are complete. No second generation, pixel extension, invented fur strips, layout redesign, installation, or changes to earlier records were performed.

## Chosen production path

The approved 1450 × 2040 draft is the geometry source. Paper remains `#F4F0E8`; the `#4164D8` panel remains at x 826.5 with width 507.5 and a 116 px right paper border. Editable Impact text remains DREAM at (101.5, 794), WEAVER at (101.5, 1054), both 300 px, with textLength 551 and 638. ONEIRLOOM remains at (101.5, 1804), 62 px, textLength 360. Draft masks and rectangular fragment windows are preserved. Gray placeholders, direction arrows, and cue ellipses are absent.

The source's four-line title was deliberately replaced by two complete words, DREAM and WEAVER, in the approved draft. Small source copy is omitted. These are declared adaptations, not exact source reproduction.

One photographic right-facing asset supplies both views. The left image is a declared mirrored graphic duplicate, not a newly verified three-dimensional side canon. The original identity is cropped to fur, an indigo textile panel and one antique-gold four-point star per visible version. The full sling, crescent and limbs are outside this adaptation. The fixed masks crop away much of the tuft, antennae and local curl.

## Asset versus submitted prompt

The built-in `image_gen.imagegen` entry was called once with `transparent_background: true` and only `00-approved-reference.png` as an identity input. The model identifier was not exposed and remains unknown. `submitted.en.txt` is the exact submitted prompt; complete equivalent Chinese and English prompts are saved separately. Layout coordinates, words and color-field geometry were not sent to the generator.

`subject-right.png` is the copied native result: RGBA, 1024 × 1536, SHA-256 `0e34d35e3b6b321906032352762d8c4137b0831e66eeb2624b98aefb77f072a9`. Alpha ranges from 0 to 254; 25.487% of pixels are fully transparent. Corner alpha values are 0, 0, 1, 20. The nonzero-alpha box touches the full canvas because of faint fringe pixels and the intended bottom crop; the alpha >127 box is (16, 59, 1021, 1536). This is real native alpha, not a white rectangle or a checkerboard painted into RGB. No alpha repair or photographic pixel editing was performed.

Inspected matches: one nonhuman continuous cocoon body, tactile gray-lilac fibers, the indigo woven oval on the right-facing surface, one gold four-point star, rounded back mass on the left, compact tuft and two gold-tipped curved antennae, and a local curl. The rightward three-quarter orientation is evident in the standalone asset. There are no human eyes, nose, mouth or neck. Fur continues through the bottom crop.

Decisive limitation: the generator made the indigo panel large and the star around (780, 780), leaving only about 756 source pixels below it. The prompt requested a long lower fur expanse, but the delivered crop does not supply enough relative coverage for the locked page geometry. A correct identity and transparent output do not establish a usable asset for this layout.

## Draft versus rendered assembly

The image is embedded in SVG. The right view has uniform scale 1.05 and translation (297.5, -125.4), placing its star at (1116.5, 693.6). The left mirrored view has uniform magnitude 1.25 and base translation (1598.5, -607.8), placing its star at (623.5, 367.2). Fragment x offsets are +14, 0, -16, +16, -16, +14 px, inside the unchanged rectangular windows and local contour. The right image is continuous. There is no anisotropic warp.

The actual assembled PNG was inspected. Both stars remain recognizable, the left is fragmented and mirrored, the right is continuous, the headline remains dominant and editable, the left whitespace and right paper border survive, and there is no visible opaque asset rectangle or gray placeholder. The partial image does not cover the draft:

- The right asset ends at y 1487.4, creating an abrupt horizontal photographic edge and leaving approximately 553 px of the intended lower path empty. The draft's narrowing lower mass and bottom contact are missing.
- The left asset ends at y 1312.2. The last fixed window begins at y 1326, so that lower local fragment is empty.
- The large panel dominates the left upper crop. The intended broad furry upper silhouette is not occupied; its visible left edge begins substantially farther right than the gray draft. Both complete panel shapes are not shown, although both stars are clear.
- At the top right, the fixed contour cuts the antenna into a thin residual end. This is an observed undesirable crop.

Uniform enlargement sufficient to fill the lower right path would also enlarge the panel/star beyond the fixed local space; the existing asset cannot preserve the selected star placement, recognizable full star and required lower coverage together. No attempt was made to fill the missing mass with repeated strips or new anatomy. This is the return condition for a Primary decision on the asset requirement or approved layout, before any further generation or layout revision.

## Source versus rendered assembly

The original 06 reference, the approved draft and the result were viewed. The source's right-biased image mass, central division, blue field with a paper border, dark left title, local left horizontal cuts and opposed view treatment are represented locally. The two-line title departure was already selected in the draft. The rendered poster fails the defining large-area contour: its lower right mass stops far above the bottom and its left upper occupancy is narrower than the draft. Therefore local mechanisms match in part, while complete layout transfer has failed. This record makes no claim of exact source fidelity or general model capability.

## Actual checks and files

`python work/design-sop-unification-20261002/layered-06-final/render.py` used the installed Python Playwright package and Microsoft Edge. It rendered `poster.png` at 1450 × 2040, awaited font readiness and decoded the embedded asset, loaded the single-poster `preview.html`, and reported no page errors. Unchanged draft paper, panel, text and left-mask elements were compared; the right path data is also unchanged. `assembly-checks.json` marks technical checks passed and visual status failed. `generation.json` preserves entry controls, known metadata, prompt hash and measured native asset evidence.

Deliverables in this directory: `poster.svg`, `poster.png`, `preview.html`, `subject-right.png`, complete bilingual asset prompts, `submitted.en.txt`, `generation.json`, `assembly-checks.json`, this record, and the reproducible `render.py`. This directory contains one poster composition, not a contact sheet. The root Primary owns final review and the next decision.
