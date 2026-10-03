# Illustrated tutorial revision

## X article draft

- Authorized: transfer the accepted tutorial and its figures to an X Article draft, format it, and create a Chinese 5:2 cover. Publication is reserved to the user; never click Publish.
- Existing authenticated Edge session at port 9334, account `@KimbomArtist` (Dibo). Existing unrelated untitled draft is preserved.
- Created draft: `https://x.com/compose/articles/edit/2104389078770917376`.
- X editor visibly recommends a 5:2 cover. Built-in browser runtime failed before browser selection because its service module was missing; existing local Playwright/CDP is used for the accessible Edge session.
- [x] Generate a new Chinese cover with the built-in GPT image tool, following the user's explicit correction. The latest output is `x-draft/X文章封面-GPT生成-新标题.png` (1983 x 793, approximately 5:2). It uses the user's requested headline. Both the X draft title and the local publishing source are updated. The first generation was blocked; a fully clothed professional portrait cover succeeded.
- X editing observation: media uploads and draft saves can restore an earlier editor selection. Native selection, confirmed save responses, and caption-position checks are required between insertions. Reload verified the first nine images and the new title persisted; the remaining transfer is in progress.
- [ ] Insert and format the full article with 39 figures in order.
- [ ] Verify saved draft contents and preview; leave unpublished.

## Tutorial-writing subskill

- [x] Extract the accepted teaching and editing practices into `skills/dreamweaver-image-tutorial/SKILL.md`, with a focused depth reference and UI metadata. All new instructions are in English; reader-facing Chinese tutorials retain the author's requested voice.
- [x] Add the parent route and an explicit tutorial-format exception to standalone bilingual prompt output. Register the new skill in the existing catalog and structural checker; add four behavior scenarios without rewriting existing cases.
- [x] Create a source-preserving junction at `J:/Users/yangda01/.codex/skills/dreamweaver-image-tutorial` and verify installed files match source and the installed parent can read the route.
- Validation: skill-creator quick validation passed; repository check passed for 15 skills, 27 behavior-case definitions and 2 prompt examples. New metadata and English-only instructions checked.
- These checks establish file validity and installation readback. The four scenarios are evaluation definitions, not executed behavioral tests; fresh-session automatic selection and a new end-to-end tutorial run have not been tested.

## Language polish

- [x] Personally revise every chapter into natural first-person Chinese. Replace abstract or procedural jargon, smooth transitions, and explain necessary photography terms in ordinary language.
- [x] Revise headings, alt text, short instructional prompts, observation paragraphs, and text printed on all 39 figures. Keep the four quoted generation prompts verbatim and identify them as the actual original requests.
- [x] Preserve all 16 chapters, 37 subsections, the 39-image sequence, disclosed generation misses, and 62 original outputs. No new generation was required.
- [x] Rebuild the same HTML, desktop Markdown, portable Markdown and ZIP. Preserve the preceding source and deliveries in `archive-before-language-polish/`.
- Current publishing source: `article-polished.template.md`, approximately 19,700 characters after inserting actual prompts and observations.
- Evidence: `evidence/language-polish-check.json` confirms image order, exact quoted prompts, wording scan and ZIP integrity. `evidence/browser-check.json` confirms all images load, copy and lightbox work, and desktop/mobile layouts have no horizontal overflow. Revised screenshots were personally inspected; figure titles and subtitles fit their canvases.
- This is a prose revision ready for user review, not a claim of user approval or new image-model behavior.

## Current expansion request

- User requests substantive depth in every chapter, with wardrobe coverage beyond front-view fabric changes. Previous first-person voice, illustrated-section requirement and Primary-only ownership remain in force.
- Preserve the completed illustrated edition in `archive-illustrated-v1/`.
- Expand all 16 chapters with decision criteria, multiple concrete variants, prompt construction, visual checks, and relevant failure handling.
- Wardrobe must cover silhouette, length, necklines/straps/sleeves, front/side/back structure, layering/occlusion, drape and material, with actual generated demonstrations.
- [x] Produce and personally inspect 34 new runs through the existing 8188 workflow, including six corrected examples after first-pass misses.
- [x] Expand all 16 chapters in first person to 37 illustrated subsections; build 23 additional comparison figures, 39 total.
- [x] Update the same Markdown/HTML deliveries and portable package. Preserve the previous illustrated edition in `archive-illustrated-v1/`.
- [x] Verify all 37 subsections have figures; all 62 generation records report success and copied source bytes match; inspect desktop/mobile rendering and interactions.

## Expansion acceptance

- Manuscript: `article-expanded.template.md`, rendered to 20,050 characters including full prompts; 16 chapters and 37 subsections.
- Coverage extends across framing, camera/head separation, directions, composition, body support, expressions, object contact, room depth, clothing, light, focus, full prompts, diagnosis, grids, and practice.
- Actual generation: 34 new outputs, 62 total; graph, prompt ID, source path and history retained per run. `evidence/generation-check.json` verifies successful run records, exact prompts and byte-identical source copies.
- Personal visual review: `expansion-observations.json`. Corrected head lowering, rear orientation, sleeve length, flower focus, environment scale, and cup-bottom support. Remaining hand/leg directions, support details and identity variations are disclosed where used.
- Delivery: same Markdown and HTML paths, portable Markdown, ZIP with 39 teaching figures and 62 original PNGs. `evidence/delivery-check.json` confirms no missing images or unresolved placeholders.
- Real browser evidence: `evidence/browser-check.json`; 39/39 images decoded, all 37 subsections illustrated, 34 copy buttons, copy feedback succeeded, lightbox opened, no page errors, no horizontal overflow at desktop 1440px or mobile 390px.
- Personally inspected browser screenshots: `evidence/expanded-desktop-pose.png`, `evidence/expanded-desktop-layers.png`, and `evidence/expanded-mobile-contact.png`.
- Completion means the expanded artifact and checks are ready for user review; it does not imply user acceptance of the prose or exact identity preservation.

- Owner: Primary only. User explicitly prohibits subagents for this revision.
- Deliverable: first-person Chinese tutorial, an explanatory figure in every section, images generated through the existing Qwen-Image-2.1 workflow on localhost:8188.
- Source: existing article and source-article text in this directory. Previous draft preserved as `美女生图教程-旧稿.md`.
- Workflow: copied from successful local history `a1e2c7cb-a299-43f4-8ac1-74dea3a7c363`; Qwen-Image-2.1 int8, 40 steps, CFG 1, Euler/simple. No source workflow or server settings changed.
- Acceptance: inspect every selected image; captions describe observed results; every section has a relevant figure; prompts and generation history are retained; article voice is the author teaching readers.

## Previous illustrated edition

- [x] Inspect live endpoint and queue; preserve previous draft and source workflow.
- [x] Generate and personally inspect 28 completed runs. Select 18 source images for positive examples and one initial crop miss for diagnosis.
- [x] Write the 16-section first-person article around observed outputs, including the crop repair and remaining hand/grid deviations.
- [x] Build 16 explanatory figures, Markdown, standalone HTML with embedded images, and a portable ZIP including original generations and prompts.
- [x] Verify all 16 sections contain a figure; all 16 HTML images load; desktop/mobile have no horizontal overflow; lightbox opens; browser reports no page errors.

## Acceptance evidence

- Per-run prompts, graph, prompt IDs and actual outputs: `evidence/01_full.json` through the named 28 run records.
- Personal image review: `observations.json`.
- Structural delivery checks: `evidence/delivery-check.json`.
- Actual browser rendering checks: `evidence/browser-check.json`, desktop/mobile screenshots and prompt preview.
- Main deliveries: `美女生图教程.md`, `美女生图教程.html`, `美女生图教程-图文包.zip`.
- Limits are teaching observations, not blocked work: exact crop boundary, hand laterality and some grid crop requirements did not match perfectly; article labels them explicitly. No claim of general model guarantees.
