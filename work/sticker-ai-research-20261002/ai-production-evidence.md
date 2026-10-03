# AI production evidence for character sticker packs

Research date: 2026-10-02. This is a bounded evidence note for the Primary's integration, not a replacement SOP. No images were generated, edited, cropped, or visually tested. No model was installed or called for inference. Existing skills and ledgers were not changed.

## Findings that affect production choices

Current official documentation supports reference-conditioned generation and editing without subject-specific training. This makes a reference-led reaction workflow a supported option. The documentation does not establish which tool produces the best complete sticker pack, nor does it establish success for the local Oneirloom entry point.

Identity, style, structure, and edit location are different controls. Adobe describes style references in terms of look and feel, while structure references transfer outline and depth. A style match therefore cannot establish character identity. A structure match cannot establish that a unusual appendage retains its original meaning. These distinctions matter when expressive deformation changes a character's outline. [S02, S03]

A transparent-output option is a documented capability, not evidence that a particular delivered image contains a usable alpha channel. The current Qwen-Image-2.1 repository explicitly documents RGBA output. Adobe documents a background-removal route to transparent PNG. These are separate production paths. [S05, S09]

Four operations must remain distinct: supplying multiple references to one generation, requesting several output candidates, dispatching several independent reaction jobs, and generating a grid containing several stickers. Vendor support for the first two does not prove the last two produce a consistent, complete pack.

## Source register

All sources below were retrieved on 2026-10-02. There are 14 unique supporting sources: 11 official vendor documents or repositories and 3 primary research papers. Entries paraphrase the sources. No long source passages are reproduced. Page dates are reported only when visible. Vendor statements establish documented behavior or author claims, not independent comparative results.

### S01. OpenAI image generation guide

- URL: https://developers.openai.com/api/docs/guides/image-generation
- Author: OpenAI. Page date not displayed in fetched content. Retrieved through the official OpenAI Docs MCP after a documentation search.
- Exact sections: Overview; Generate Images; Multi-turn image generation; Create a new image using image references; Edit an image using a mask; Size and quality options; Limitations.
- Assertion checked: reference input, multiple output candidates, editing, transparency, text, and limitations.
- Finding: The fetched Overview names `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`. The guide documents one or more image references, Image API `n` outputs, and Responses API iterative edits. Transparent output uses `background: "transparent"` with PNG or WebP. The mask guides editing but is not an exact shape constraint. The guide explicitly retains limitations in recurring-character consistency, precise text placement and clarity, and structured composition.
- Limitation: These are current API documentation claims. They do not establish account access, the model selected by a desktop tool, its exposed parameters, or measured sticker performance. No API request was made. The names are a retrieval snapshot, not a universal workflow dependency.

### S02. Adobe style reference images

- URL: https://developer.adobe.com/firefly-services/docs/firefly-api/guides/concepts/style-image-reference/
- Author: Adobe. Page date not displayed.
- Assertion checked: whether a style reference is an identity lock and whether variations are separate files.
- Finding: Style references guide colors, artistic treatment, mood, and overall appearance. The API exposes strength from 1 to 100 with a default of 50. Its example requests four variations and receives four output URLs.
- Limitation: This describes style conditioning and candidate output. It does not promise character anatomy, exact identity, four different reaction intents, or pack-wide consistency.

### S03. Adobe structure reference images

- URL: https://developer.adobe.com/firefly-services/docs/firefly-api/guides/concepts/structure-image-reference/
- Author: Adobe. Page date not displayed.
- Assertion checked: what structural guidance preserves.
- Finding: Structure references transfer characteristics such as outline and depth while allowing different details, styles, or moods. The `structure` object includes reference input and adjustable strength.
- Limitation: Structural resemblance is not a guarantee of semantic anatomy or pixel equality. Applying a fixed structure to every reaction is a production choice that can restrict pose variety, not a documented requirement.

### S04. Adobe reference images for Generative Fill

- URL: https://helpx.adobe.com/photoshop/desktop/create-open-import-images/create-images/use-reference-images-for-consistent-results.html
- Author: Adobe. Updated 2026-08-18.
- Assertion checked: reference-assisted local replacement versus full-scene guidance.
- Finding: With a selection, Photoshop offers Firefly Fill & Expand references for an object or the whole image, and intents to swap or place content in the selected area. Partner-model reference limits are separately documented on this page.
- Limitation: Photoshop integration behavior and reference limits cannot be transferred to a provider's direct API. Selection controls do not establish that the resulting character is correct. This source supplies a conditional repair route, not a reason to require selections before every generation.

### S05. Adobe remove background from images

- URL: https://helpx.adobe.com/uk/firefly/web/work-with-images/edit-images/remove-background.html
- Author: Adobe. Updated 2026-09-23.
- Assertion checked: actual transparent export versus a visually blank background.
- Finding: Firefly's Remove background tool isolates the subject. Downloading immediately after removal saves a transparent PNG.
- Limitation: The page does not guarantee correct segmentation of every thin appendage, translucent effect, or detached symbol. No local export or edge inspection was performed.

### S06. Qwen-Image technical report

- URL: https://arxiv.org/abs/2508.02324
- Authors: Chenfei Wu and colleagues. Submitted 2025-08-04.
- Assertion checked: basis for text rendering and editing consistency claims.
- Finding: The report describes training for complex text, including Chinese, and separate semantic and reconstructive encoding of the source image to balance editing semantics and visual fidelity.
- Limitation: This is the 2025 report. It does not establish every later Qwen model's capabilities or prove exact captions and character identity in a sticker pack. No reported ranking is reused here.

### S07. Qwen-Image official repository

- URL: https://github.com/QwenLM/Qwen-Image
- Author: QwenLM. Relevant release entries include 2025-09-22 for Edit-2509 and 2025-12-23 for Edit-2511.
- Assertion checked: whether Qwen editing has one universal reference-input contract.
- Finding: The repository labels original Qwen-Image-Edit as single-image input and gives multi-image examples for Edit-2509 and Edit-2511. The original editing section reports instability without prompt rewriting. Examples include `num_images_per_prompt` but do not demonstrate a complete reaction pack.
- Limitation: Version-specific notes must remain version-specific. The older prompt-rewriting warning is not proof of identical failure behavior in 2.1. A seeded example is not evidence that a shared seed alone preserves identity.

### S08. Qwen-Image-Edit-2511 model card

- URL: https://huggingface.co/Qwen/Qwen-Image-Edit-2511
- Author: Qwen. The official repository dates release to 2025-12-23.
- Assertion checked: identity preservation and whether extra LoRA training is compulsory.
- Finding: The card documents multi-image input and claims reduced image drift, stronger character and multi-person consistency, and incorporation of selected community LoRA capabilities into the base model.
- Limitation: Built-in stylistic or editing effects do not mean that a user's specific character has been trained. The card's examples are not independent sticker-pack tests. Better consistency does not mean guaranteed identity.

### S09. Qwen-Image-2.1 official repository

- URL: https://github.com/QwenLM/Qwen-Image-2.1
- Author: QwenLM. Release dated 2026-09-20 in News.
- Exact sections: Introduction; News; Image Editing (Single Image); Image Editing (Multiple Reference Images); Transparent Image Generation (RGBA); Prompt Rewriting.
- Assertion checked: current unified generation, reference editing, and transparency support.
- Finding: The repository documents one model for generation and editing, up to 10 reference images, and native RGBA output. It describes local guidance through circles, painted annotations, or separate masks. Its transparency example names the alpha channel in the prompt. Prompt rewriting is recommended.
- Limitation: These statements do not prove that our installed backend exposes all options or that every result contains correct alpha. The code examples were read, not executed. No claim about exact mask confinement or superiority over Edit-2511 follows from this source.

### S10. Black Forest Labs FLUX.1 Kontext image editing

- URL: https://docs.bfl.ai/kontext/kontext_image_editing
- Author: Black Forest Labs. Page date not displayed.
- Assertion checked: reference editing, text replacement, annotations, and training requirements.
- Finding: Kontext uses a prompt and source image for editing. The page presents iterative character consistency, quoted-text replacement, and colored annotation boxes for targeted edits. It describes operation without fine-tuning and now labels Kontext a previous-generation option.
- Limitation: These are provider descriptions and examples. Output PNG format alone does not establish native transparent generation. The documented single-source endpoint must not inherit FLUX.2's reference limits.

### S11. Black Forest Labs FLUX.2 image editing

- URL: https://docs.bfl.ai/flux_2/flux2_image_editing
- Author: Black Forest Labs. Page date not displayed.
- Assertion checked: current reference editing and API versus interface limits.
- Finding: The page documents single-reference and multi-reference editing, including text edits. Its overview distinguishes up to 8 references through the API and 10 in the playground. Its sample identifies `flux-2-pro-preview` as changing and `flux-2-pro` as pinned.
- Limitation: A generic overview is not the final contract for every variant. The page supplies no evidence of native alpha output or a multi-reaction output contract. Provider marketing language about perfect proportions is not adopted as a guarantee.

### S12. Black Forest Labs multi-reference editing help

- URL: https://help.bfl.ai/articles/6546682167-what-is-multi-reference-editing
- Author: Black Forest Labs. The opened page shows a relative update age of 3 months. Search extraction exposed 2026-06-12, which is not treated as a stronger exact-date record.
- Assertion checked: variant-specific count limits and reference attribution.
- Finding: The help page distinguishes pro API at 8 references and 9 MP total, pro playground at 10, flex at 10, and a recommended maximum of 6 for dev. It documents both natural-language reference attribution and explicit image indexing.
- Limitation: Counts vary by model and integration. Only use the count for the selected endpoint after checking its current contract. More inputs are not evidence of better consistency.

### S13. DreamBooth

- URL: https://arxiv.org/abs/2208.12242
- Title: DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation.
- Authors: Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein, and Kfir Aberman. Submitted 2022-08-25, revised 2023-03-15, CVPR 2023.
- Assertion checked: whether subject-specific tuning is an established optional mechanism.
- Finding: DreamBooth learns a subject identifier from a few images by fine-tuning a pretrained model, then generates the subject in new contexts. Prior preservation is part of the proposed method.
- Limitation: This establishes a mechanism, not a requirement to train every sticker character. It does not prove that any specific modern model, LoRA recipe, or small dataset will preserve a nonhuman character under expressive deformation.

### S14. IP-Adapter

- URL: https://arxiv.org/abs/2308.06721
- Title: IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models.
- Authors: Hu Ye, Jun Zhang, Sibo Liu, Xiao Han, and Wei Yang. Submitted 2023-08-13.
- Assertion checked: whether image conditioning can coexist with textual control without per-subject fine-tuning.
- Finding: The paper separates image and text conditioning through decoupled cross-attention while freezing the base diffusion model. It demonstrates an image-prompt route that can combine with text and structural controls.
- Limitation: The adapter itself was trained. This is not proof that arbitrary models accept it, or that its general image conditioning guarantees character identity. It supports an optional compatible-backend route, not a mandatory installation.

## Conditional production branches: local synthesis

The following judgments combine the documented mechanisms with the sticker task. They are proposals for the Primary, not vendor prescriptions or experimentally validated rankings.

| Branch | Conditions that make it useful | Main inspection burden |
| --- | --- | --- |
| Direct generation of one sticker | The character is being invented, or an already tested prompt and backend reproduce its important features. Generate one reaction per independent output when each must have a distinct intent. | Identity drift between outputs, anatomy, action clarity, exact caption, alpha. A descriptive prompt is not an identity guarantee. |
| Reference editing for each reaction | A usable master character exists and the backend accepts reference input. Attribute each input's role, such as identity, pose, or style. | Whether identity survives the new pose without copying the old expression. Check unintended props, clothing, proportions, and appendage meaning. |
| Contact sheet followed by crop | A compact set needs rapid side-by-side concept review, or the actual sheet already has separable cells with enough resolution for delivery. | Cell count, duplicates, bleed, clipped limbs, captions crossing cells, equal usable resolution, and every individual crop. A correct-looking sheet preview does not prove individual exports. |
| Optional lettering and compositing | Exact lettering, placement, localization, or a repair is more reliable in an editor. This can be chosen after an observed text defect or an explicit editable-lettering requirement. | Lettering must fit the pose and remain legible at delivery scale. Adding text cannot rescue an unreadable reaction. Compositing may protect approved pixels but is not the source of expressive design. |
| Optional identity tuning | A recurring production need remains after representative reference-guided trials show identity failures, and there is a suitable reference set and a compatible backend. | Identity retention and expression range on held-out reactions. A character that only repeats the training pose has not solved the task. Training cost is justified by recurring need, not by the word "consistent." |

Reference editing can start each new reaction from the approved master or a selected approved view. This reduces dependence on a long chain of already altered results. Iterative editing remains useful inside a reaction, especially for a local correction. Neither approach eliminates review.

The contact-sheet branch should not be the automatic export strategy. A sheet spends one image's pixel budget on several cells and couples their layout. It can still be useful for discovery or comparison. Cropping is a file operation after acceptable artwork exists, not a guarantee that each cell contains complete artwork.

## Order that limits redesign: local synthesis

1. Define the conversational action before drawing. Record what the sender communicates, the relationship and tone, and whether the image must work without a caption. The same mouth shape can mean joy, mockery, or panic depending on the body and context.
2. Identify the character's meaning-bearing anatomy. Record which forms are eyes, mouth, limbs, ears, antennae, accessories, or symbols; their attachment and count; and a few identity-defining proportions and color relationships. Avoid freezing every contour or requiring a fixed silhouette across poses.
3. Choose the smallest available production branch that can carry those facts. Use the actual backend's supported inputs. A pose guide or annotation is optional when a concrete pose needs it. A fixed mask is not a universal character definition.
4. Before expanding the pack, inspect a few reactions that stress different requirements: a quiet expression, a strong body action, and an extreme emotion or occlusion relevant to this character. This is a proposed economical sample, not a scientifically established count. Reject semantic-anatomy mistakes before typography and export work.
5. Expand accepted directions with varied body action, gaze, gesture, framing, and rhythm. Preserve identity facts, not a repeated pose with changed eyes. Review the whole pack for redundant meanings and review each file for defects.
6. Resolve exact caption rendering and background handling through the selected branch. Inspect the real alpha channel and composites on contrasting backgrounds. Review edges, detached effects, and lettering at the target display size. Exported dimensions and file validity cannot establish emotion or anatomy.

## What still needs inspection or evidence

- Semantic anatomy needs comparison with the character definition. Automated similarity can reward an almost unchanged pose while missing that an antenna became a finger or an accessory became a limb.
- Expressive variety needs review of both the intended chat action and the visible gesture. Color consistency alone is insufficient.
- Captions need character-by-character checking, including punctuation, line breaks, omissions, and unwanted extra text. OCR can assist but is not acceptance evidence on its own.
- Transparency needs file-level alpha verification and visual inspection. A checkerboard rendered into opaque pixels is not transparency. A technically valid alpha channel can still remove an important thin feature or leave a visible fringe.
- Edits need before-and-after comparison outside the intended region when preserving surrounding artwork matters. A mask or annotation does not by itself establish exact confinement.
- Human judgment can resolve humor, tone, brand fit, and readability. AI visual review can help locate discrepancies but should not claim pixel-level accuracy or author approval.

No experiments were performed. No local capability mapping, sample-output alpha, batch success rate, rejection rate, speed, cost, or best-model ranking was measured. The evidence supports conditional methods, not a promise that an untested starter recipe is ready for production.

## Evidence gaps and exclusions

The Qwen 2.1 blog search result contained useful text, but opening the page returned no body. The official repository independently supplied the retained 2.1 claims and exact section anchors, so the blog is not counted as a supporting source. No authentication challenge, access denial, or rate-limit response was encountered on the retained research endpoints.

No retained vendor document specifies a complete chat-sticker contact-sheet-to-individual-export acceptance procedure. That branch and the proposed review order are local synthesis. Sticker-specific benchmarks and communication research belong to the Primary's separate research assignment. This note does not duplicate them or claim to be the final cross-domain SOP.
