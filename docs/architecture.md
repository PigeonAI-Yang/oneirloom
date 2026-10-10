# Progressive-disclosure architecture

Proposal A was approved for source implementation on 2026-10-03. This document describes the edited source files. Structural checks, actual assistant read paths, installed resource availability, new-session discovery, and visual results are different evidence states. See the [migration decision and ownership record](architecture-progressive-disclosure-proposal.md) for the baseline, rationale, and remaining acceptance work.

## Responsibilities and reading units

The 0.3.0-preview source contains 22 sibling `skills/*/SKILL.md` entries: the 19 entries present before this change and three added methods for craft construction, digital form, and space conception. It is a development source preview with no corresponding package or installation. The new method guidance is text only; no new render or native-model result validates it. The frozen `v0.2.0-preview.1` package remains at 18 skills. A host discovers metadata and explicitly reads the chosen entry. The coordinator is optional for direct capability use. This is a document-reading design, not a runtime loader or a required layer count.

| Owner | Responsibility | Conditional reads |
| --- | --- | --- |
| [Coordinator](../skills/oneirloom/SKILL.md) | Public aliases, current deliverable selection, and visual intent before model adaptation | Selected capabilities only |
| [Shared interaction contract](../skills/oneirloom/references/interaction-contract.md) | Output-type selection, complete affirmative prompt language and blocks, continuity, portable Doubao limits, and evidence status | No capability-body dependencies |
| [Dream weaving](../skills/oneirloom-dream-weaving/SKILL.md) | Collaboratively develop unformed feelings, memories, and fragments into a drawable scene while preserving the initial feeling and accepted choices | Shared contract at entry; product art direction before transforming a real product; visual analysis only for unresolved relations; medium and production after the scene is formed |
| [Product art direction](../skills/oneirloom-product-art-direction/SKILL.md) | Product facts and provenance, unknowns, critical conflicts, concepts, permitted fiction, and product-result checks | Ecommerce collaboration for vague briefs, research, copy gaps, or portable handoff; design for a composed graphic |
| [Graphic design](../skills/oneirloom-style-design/SKILL.md) | Complete Understand, Observe, Design, production-selection, review, and correction process for composed graphics and packaging graphics | Observation for reference transfer, production for actual artifacts or selected composites, and review for actual or reported results |
| [Craft construction](../skills/oneirloom-craft-construction/SKILL.md) | Physical craft units, joins, layers, thickness, edges, and support | Its construction reference and optional fuse-bead template; product art direction for real-product facts; graphic design for a composed layout |
| [Digital form](../skills/oneirloom-digital-form/SKILL.md) | Digital geometry, volume, repeated parts, deformation, connections, and form transformation | Its form mechanisms; material response for surface appearance; camera composition for the view; graphic design for composed layout |
| [Space conception](../skills/oneirloom-space-conception/SKILL.md) | Masses, enclosure, openings, adjacency, circulation, focus, scale, and depth | Its spatial reference first; camera composition for viewpoint after the place is organized; photography for capture |
| [Visual analysis](../skills/oneirloom-visual-analysis/SKILL.md) | Source evidence, reconstruction anchors, portrait and garment checks, and abstract visual language | Its reconstruction and subject references; graphic observation directly for graphic evidence |
| [Result diagnosis](../skills/oneirloom-result-diagnosis/SKILL.md) | Source-to-prompt versus prompt-to-result misses and bounded causal attribution | Graphic review directly, product art direction for real products, and design only for a conceptual repair |
| Other public capabilities | Medium, camera, light, characters, stickers, icons, brand systems, model adaptation, tutorials, and prompt cards | Their actual task references and optional recipes |

Every public entry explicitly reads the shared contract before its first substantive response unless the unchanged content is already available. No capability reads the whole coordinator merely to obtain policy. A directly chosen capability maintains the current conversation notes itself. Unchanged prior reads and confirmed decisions remain reusable; reading another file does not evict earlier context.

Each relevant person-producing entry directly links [person defaults](../skills/oneirloom/references/person-prompts.md) under a person-prompt trigger. Product-only work does not load portrait detail. Photography and illustration style catalogues are conditional on medium selection or a needed technique distinction; an already specified medium uses its entry checklist.

An unformed feeling or fragment goes to dream weaving. A formed scene with an open visual direction can optionally read the [visual-family index](../skills/oneirloom/references/visual-families/index.md) and only notes that help compare mechanisms. Its ten names are overlapping search dimensions, so they do not replace the deliverable owner or require a medium change. A settled style and a clear medium such as watercolor go directly to their methods.

Resolve a selected skill through the actual host catalog, with its sibling path as the repository fallback, and read the file explicitly. Markdown links are navigation, not automatic calls. Missing specialist resources block only dependent work. Independent distribution of a capability requires that its shared contract and selected resources remain resolvable; the source migration does not prove a particular installed package includes them.

## Graphic decisions and conditional detail

The graphic-design entry owns the whole common process. Subject understanding includes form, connected parts, visible action, and meaning, with observations and interpretations kept separate. Observe the actual style image before a stored recipe, then design how its relations fit this subject and exact copy. Choose production after these decisions. A sketch remains provisional when real anatomy requires revision. Masks and coordinates cannot establish a sound design.

Its references expand particular tasks without another routing layer:

- [Graphic observation](../skills/oneirloom-style-design/references/graphic-observation.md) covers detailed source reading, depicted versions, tone versus fragmentation, joins and coverage, material interpretation, meaningful crops, and anatomy-aware subject transfer. Analysis-only work can read it directly.
- [Graphic production](../skills/oneirloom-style-design/references/graphic-production.md) covers actual sketches, assets, native design, compositing, source delivery, and unavailable-tool boundaries. Prompt-only direct generation does not require it.
- [Graphic review](../skills/oneirloom-style-design/references/graphic-review.md) covers whole-image comparison, intended viewing size, exact copy, material relationships, correction, and honest inspection status. Diagnosis reads it directly rather than loading creation first. Design becomes relevant only when findings require a design change.

The former `graphic-design-sop.md` is retired from active instructions. Historical snapshots and records preserve their original contents and are not runtime guidance. The [source notes](../skills/oneirloom-style-design/references/graphic-design-sources.md) retain the rationale and external-source limits.

Pure photography, digital form, craft construction, spatial layout, character turnarounds, tutorials, and existing image-and-prompt cards retain their own procedures. Direct generation, native design, and compositing remain conditional choices. A rendered skeleton and separate assets are not universal prerequisites. Explicit code, vector, model, and single-model requests remain constraints.

## Specialist deliverables retain their owners

[Expression stickers](../skills/oneirloom-expression-stickers/SKILL.md), [icons](../skills/oneirloom-icon-design/SKILL.md), and [brand identity](../skills/oneirloom-brand-identity/SKILL.md) specialize the common design process and keep their existing template collections. They inspect actual references before stored recipes, preserve meaningful anatomy, and carry relevant material relationships into production.

- Stickers own conversational intent, the reaction matrix, identity, caption and gesture relationships, individual exports, alpha, and legibility in chat. Character sheets supply identity references, not finished sticker packs.
- Icons own functional metaphors, family construction, optical consistency, and legibility at intended sizes. UI glyphs, app symbols, and pictograms remain distinct. Supplied marks stay fixed. True vector delivery requires vector geometry rather than a raster in an SVG wrapper. Icons receive no automatic watermark.
- Brand identity owns marks and lockups, color roles, typography, auxiliary graphics, image and icon language, agreed applications, and guidelines. It coordinates icon or sticker work only when requested. A full VI requires the agreed foundations, applications, manual, and usable files; a concept board or one generated image does not establish delivery.

Native artifacts and guidelines use their owners' delivery contracts. Prompt-only requests receive complete prompts for every necessary image or asset. Finished graphics require a final preview and actual inspection status, plus editable source and assets when warranted. Unknown business facts, font rights, print profiles, and platform specifications remain explicit gaps only for dependent work.

[Prompt cards](../skills/oneirloom-prompt-card/SKILL.md) retain their existing-image layout, prompt-preservation, renderer, and approved signature contract. Their 3:4 canvas does not rewrite a generation aspect ratio embedded in the prompt. Requested Oneirloom watermark guidance stays with this owner; no additional watermark reference was created. [Tutorial writing](../skills/oneirloom-image-tutorial/SKILL.md) retains article language, teaching depth, author voice, and illustration evidence rules.

The selected model adapter owns its relevant official sources, snapshot maintenance, task writing, and observed-entry controls. It adapts established visual intent and cannot change the requested aesthetic. Native artifacts need no model adapter. Unspecified or unknown entries use portable text rather than invented settings.

## Representative read paths

Read the shared contract once while unchanged. Main-entry paths begin with the coordinator; a direct capability path omits it.

| Current request | Instructions needed |
| --- | --- |
| Unformed feeling, memory, or fragments with no drawable scene | Shared contract and dream weaving; product art direction first for a real product, then the relevant medium and production owner after the scene forms. |
| Clear photographic product poster, prompt only | Shared contract, product, design, photography. No automatic ecommerce reference, style catalogue, production, or review file. |
| Vague product selling brief | Shared contract, product, ecommerce collaboration. Add design and a medium after the selected direction needs them. |
| Confirmed background-only prompt change | Current notes and prompt, shared contract, and product rules for a real item. No automatic diagnosis or new concept search. |
| Reported wrong package in a graphic result | Shared contract, diagnosis, product, and graphic review. Add design only if findings require redesign. |
| Original illustration poster | Shared contract, design, illustration. Add observation for a chosen style reference and catalogue detail only for an unresolved technique. |
| Clear watercolor prompt | Shared contract and illustration. No family-index read is needed for a settled medium. |
| Formed scene with an open visual direction | Shared contract, the optional family index, relevant family notes, and the selected owner after direction is chosen. |
| Physical fuse-bead conversion | Shared contract, craft construction and its recipe; add product art direction for a real product or graphic design when the result needs a composed layout. |
| Fictional 3D form concept | Shared contract, digital form, and its selected mechanism; add color and light or camera only for those decisions. |
| Room or set with undecided layout | Shared contract and space conception before camera composition or photography. |
| Finished graphic or selected composite | Relevant capability plus graphic production, then review when a result exists. |
| Existing-image prompt card or prose-only article edit | Shared contract and the card or tutorial owner. New generation branches remain conditional. |

These are intended source reading paths, not evidence of executed conversations. They do not impose a file-count or token budget. A style-reference task inspects its actual image before the matching recipe. A short local template index remains useful only when selecting a concrete recipe; a known selected recipe can be read directly. No match permits composing from the capability without creating a persistent template.

## Template ownership and format

Each template belongs to one method skill. Keep the index short: template link, selection conditions, and defining visual relations. Store actual image paths only in the template and its associated example record; do not maintain a second image catalog in the router.

A template contains:

- Selection conditions.
- Defining visual anchors.
- Adjustable slots and scoped defaults.
- A complete prompt scaffold for prompt-only use, with layout and asset guidance when the chosen production path needs them. A native artifact request uses the recipe's design relations and required files rather than forcing image generation. Resolve relevant slots before delivery.
- Examples, or an explicit statement that no corresponding image is available.

Graphic-design templates separate defining relations, adjustable presentation, and replaceable sample content. Read the actual reference before relying on a stored recipe. Describe hierarchy, crop, direction, text interleaving, accents, and local construction as the source supports them. Distinguish local tone changes from displaced fragmentation and estimates from source facts. Bind adaptation and acceptance to the current subject, intended meaning, and exact copy. Cropping can preserve identity, but meaningful parts require a deliberate semantic decision before omission. Template contours cannot impose another subject's anatomy. Explicit user choices remain fixed. Keep recipe-specific relations in the template and the common process in the design entry.

Example assets and records stay inside the template directory so the owning method can be installed without a dependency on temporary work folders. Use paths relative to the document or record that contains them. Create image directories only when actual images exist.

Distinguish input reference images from generated outputs. A generated example record stores its image path, exact submitted prompt, known model/entry, relevant settings, and observations or unresolved deviations. Unknown metadata stays unknown. Keep the original image intact; record any processing if a derivative is added. Never edit an old submitted prompt to match a new scaffold while retaining its old image as evidence.

An untested template, a user-reported success without the image, and an inspected generated output are different evidence states. A queue completion or structural check is not a visual inspection. The generalized indoor-portrait scaffold, for example, is untested even though its directory contains an inspected historical example.

## Conflict resolution

- Current explicit choices override defaults; confirmed conversation choices override generic recipes.
- Creative changes override only the agreed presentation dimension. Real-product facts, unknowns, source conflicts, and factual corrections remain governed by product art direction. An invented ingredient, structure, label, specification, or claim cannot be certified by a creative request.
- Example subjects, props, and settings do not become requirements for another task. Medium owners set visual treatment; adapters set only supported expression and entry controls.
- The observed entry takes precedence over generic model claims. An unknown entry permits portable text, not invented capabilities.
- The shared contract owns standalone prompt language and formatting. Native artifacts use their capability's deliverable rules; articles and existing-image cards retain their respective formats. Literal image text stays unchanged.

## Migrated recipes

| Previous location | Current owner and template |
| --- | --- |
| `vpd-style-xiaohongshu-beauty-squat` | [Photography: crouching selfie](../skills/oneirloom-style-photography/templates/xiaohongshu-squat/template.md) |
| `vpd-style-character-card` and its two references | [Character-sheet templates](../skills/oneirloom-character-sheet/templates/index.md) |
| Illustration reference `decorative-rainy-night.md` | [Illustration: rainy-night print](../skills/oneirloom-style-illustration/templates/decorative-rainy-night/template.md) |
| `vpd-style-halftone-cutout` | [Illustration: halftone cutout](../skills/oneirloom-style-illustration/templates/halftone-cutout/template.md) |
| Existing tutorial full-length portrait evidence | [Photography: indoor portrait](../skills/oneirloom-style-photography/templates/indoor-full-length/template.md) |
| `skills/oneirloom-style-design/templates/fuse-bead/` | [Craft construction: physical fuse-bead artwork](../skills/oneirloom-craft-construction/templates/fuse-bead/template.md) |

The retired recipe names no longer define separate active skills. Invoke their owning method or the main skill with the desired recipe. The migration preserves the existing character-card and rainy-night prompt blocks. It adds untested scaffolds for the former squat and halftone instruction-only recipes.

## Verification boundary

Source implementation and local structural checks do not establish actual assistant behavior. The [proposal record](architecture-progressive-disclosure-proposal.md) preserves the before measurements, ownership migration, and pending exercises. The [verification directory](../work/progressive-disclosure-20261003/) is reserved for receipts from this migration. It does not itself prove completion.

The nine initial sticker, icon, and brand recipes remain researched starting points without associated generated examples. Existing later cases retain only their recorded evidence. A historical accepted result or text judgment does not validate the new instruction revision.

The initial seven fresh native child-agent conversations explicitly read the edited source and produced 14 actual text responses. They do not verify installed discovery or a production image-tool entry. The initial ecommerce judgments were 6 passed, 3 failed, and 4 not executed, with two additional nonproduct text exercises passing. Core product evidence and revision behavior passed in the covered exchanges; the initial failures concerned a missing copyable prompt block and internal prohibition lists appearing in generation prose. See the [actual answers](../work/progressive-disclosure-20261003/actual-answers.md) and [acceptance report](../work/progressive-disclosure-20261003/acceptance-report.md) in the verification directory. No image generation or visual inspection was performed by this migration. Installation, deployment, publication, image fidelity, and repeatability remain unverified by this task.

Prompt-delivery closure executed 11 fresh native source-reading conversations with 17 actual text responses. The first closure batch passed 12 of 13 ecommerce cases. One response still serialized an unknown-fact inventory. A one-sentence clarification of the shared contract was followed by a fresh run of that case, which passed. The latest case judgments are 13 passed, 0 failed, and 0 unexecuted.

Twelve results came from C1 and one rerun from C2. This does not establish that all cases were rerun on C2 or that behavior is repeatable. Original failed answers remain preserved. The [actual closure answers](../work/progressive-disclosure-20261003/closure-actual-answers.md) and [closure acceptance report](../work/progressive-disclosure-20261003/closure-acceptance-report.md) record the inputs, outputs, read hashes, and verdicts.

The [C1 structural receipt](../work/progressive-disclosure-20261003/closure-structure-checks.json) records 18 successful entry validations and 60 unchanged evaluation fixtures. The [C2 author receipt](../work/progressive-disclosure-20261003/closure-inventory-author-checks.json) verifies the exact sentence replacement and preservation of all other shared-contract bytes. Product and diagnosis cues remain unchanged from C1. The 18-entry validation was not rerun on C2. Installation discovery, native Doubao invocation, generation, image inspection, image fidelity, deployment, and publication remain unverified.

For 0.3.0-preview, the approved source foundation and reviewed fuse-bead migration are recorded in the [implementation record](../work/visual-families-20261010/implementation-0.3.0-preview.md) and [migration record](../work/visual-families-20261010/migration-preservation-0.3.0-preview.json). Ten actual local source-guided text cases are preserved in the [visual route report](../work/visual-families-20261010/text-exercises-visual-0.3.0-preview.md) and [continuity report](../work/visual-families-20261010/text-exercises-continuity-0.3.0-preview.md): the initial visual run passed 4/5 cases, with case 1 failing one bilingual-equivalence criterion; a manual, unblinded correction supplied corrected outputs for cases 1 and 2 and carried cases 3–5 forward unchanged, bringing the visual result to 5/5 cases and 14/14 current criteria. Case 2 had passed its original criteria; its correction only removed an unrequested English translation. Continuity cases 6–10 passed all 20 listed criteria. The reports preserve the initial responses and case-1 failure. These source-guided text results do not establish automatic invocation or fresh installed-session behavior. The SVG case passed XML and source-contract checks without rendering. No image generation or image-quality review, installation, packaging, or publication is claimed.
