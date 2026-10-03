# Poster template instruction revision

Date: 2026-10-02.

## Scope and result

Revised the collection contract and all twelve local `template.md` files under `skills/oneirloom-style-design/templates/experimental-editorial-posters/`. Each recipe now has the same eight sections: selection, source observations and uncertainty, defining mechanism, adaptation map, scoped sample slots, construction and handoff, acceptance against the resolved brief, and prompt files with historical evidence.

The collection links the canonical [graphic-design SOP](../../skills/oneirloom-style-design/references/graphic-design-sop.md). It owns sample replacement, reference roles, current-brief acceptance binding, and a portable resolved-prompt scaffold. Local recipes retain their different crop, occupancy, image/type, and layer relationships. All twelve source crops were viewed before writing. No image was generated and no validator was run.

## Decisive 06 correction

Reviewed both the [failed creature prompt](../dream-creature-realistic-06-20261002/prompt.en.txt) and [actual output](../dream-creature-realistic-06-20261002/output.png), alongside the [06 source crop](../../skills/oneirloom-style-design/templates/experimental-editorial-posters/06-swiss-sculpture/images/reference.png).

The failed prompt explicitly required a nearly frontal complete creature, every hand and accessory visible, every part inside the margins, and a torn seam behind the readable character. The output follows those instructions with a complete mascot and a right blue backdrop. That prompt changed the source's mechanism before generation. This evidence does not establish a general model limitation.

| Before | Revised instruction |
| --- | --- |
| Half-width readable sculpture cutout, rough edge, one-fifth blue panel | Near-page-height image mass with explicit upper/lower crops and a strong directional contour |
| Rough boundary could remain behind a complete subject | Boundary must cross, interrupt, offset, or organize named parts of the subject |
| Left type alignment without a firm relation to the image | Compact middle-left stack resolved together with the portrait, seam, and exposed color area |
| Identity could be interpreted as every part visible | Identify retained local features and permitted crops separately; keep explicit full-body constraints and label the resulting adaptation |
| Material detail could dominate the instruction | Resolve crop, image mass, type, and layer order before material and microtexture |
| Acceptance named the marble sample and fixed panel width | Acceptance uses the current subject, crop, direction, type, color extent, and any explicit adaptation |

The source is too small to establish the exact number of cuts, whether each boundary is torn or cut, the original construction process, or exact blue coverage. The recipe records those limits. Similar count uncertainty is explicit for the source landscape bands, object slices, and overlapping flowers. Sample counts remain available as named design choices.

## History integrity and checks

Before and after SHA-256 snapshots cover all 81 non-template files in the collection, including the source sheet, crops, generated images, prompt baselines, exact submitted prompts, example JSON files, `reference.json`, and `browse.html`.

- Before: 81 files. After: 81 files.
- Changed hashes: 0. Missing files: 0.
- File types: 15 json, 27 png, 38 txt, 1 html.
- Both snapshots yield the same normalized path/hash manifest. Its SHA-256 is `5790262f8f000ef25c374663343d8c7b0d44618fcdcf002d860b06866fe1e00f`. The manifest uses repository-relative paths, uppercase file hashes, one space between path and hash, LF separators, no final newline, and path order from the snapshot comparison.
- All Markdown link targets in the 13 revised templates exist. All previous Markdown link destinations are retained.
- All 12 recipe documents use the same eight section headings. The collection has its own shared contract sections.
- Historical evidence paragraphs retain recorded defects, baseline-versus-submission distinctions, source roles, and unknown metadata. Examples 04, 06, and 09 still distinguish their prompt baseline from the actual run. The first failures and single edits for 08 and 11 remain recorded.
- No prompt text, submitted text, JSON, image, browser, index, other skill, architecture document, configuration, installation, or publication was changed by this assignment.

The revised instructions and scaffold remain untested in generation. Preserved historical inspections do not validate them. New-session discovery and installed plugin-cache behavior were not tested.

## Changed paths

- `skills/oneirloom-style-design/templates/experimental-editorial-posters/template.md`
- `skills/oneirloom-style-design/templates/experimental-editorial-posters/01-sculpture-tear/template.md`
- `skills/oneirloom-style-design/templates/experimental-editorial-posters/02-motion-blur/template.md`
- `skills/oneirloom-style-design/templates/experimental-editorial-posters/03-mirror-sphere/template.md`
- `skills/oneirloom-style-design/templates/experimental-editorial-posters/04-torn-landscape/template.md`
- `skills/oneirloom-style-design/templates/experimental-editorial-posters/05-botanical-engraving/template.md`
- `skills/oneirloom-style-design/templates/experimental-editorial-posters/06-swiss-sculpture/template.md`
- `skills/oneirloom-style-design/templates/experimental-editorial-posters/07-object-slices/template.md`
- `skills/oneirloom-style-design/templates/experimental-editorial-posters/08-zine-silhouette/template.md`
- `skills/oneirloom-style-design/templates/experimental-editorial-posters/09-geometric-architecture/template.md`
- `skills/oneirloom-style-design/templates/experimental-editorial-posters/10-paper-typography/template.md`
- `skills/oneirloom-style-design/templates/experimental-editorial-posters/11-transparent-botanical/template.md`
- `skills/oneirloom-style-design/templates/experimental-editorial-posters/12-xerox-technical/template.md`
- `work/design-sop-unification-20261002/template-change-notes.md`

No unresolved design decision remains within this assignment. A future brief that demands both literal cropped-source reconstruction and incompatible full-body visibility still requires the main skill to resolve that specific conflict.
