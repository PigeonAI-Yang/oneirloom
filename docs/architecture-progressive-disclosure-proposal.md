# Oneirloom progressive-disclosure remediation proposal

Status: **Proposal A approved by the user and implemented in source on 2026-10-03. Structural checks are recorded below; behavioral acceptance and deployment remain pending.**

Prepared on 2026-10-03 against source checkout `J:/PigeonYang/skills/oneirloom`, commit `d5df2ed`. The original proposal recorded a clean working tree at preparation. The user subsequently authorized implementation with "可以实施". The [architecture](architecture.md) now describes the edited source. At implementation start, `.gitattributes`, `.gitignore`, `AGENTS.md`, and `PROJECT-FILES.md` were dirty, and this proposal was untracked. Existing unrelated working-tree changes were preserved. A separate operator advanced HEAD and staged files during authorship; the instruction baseline remains pinned to `d5df2ed`, and those external Git/LFS changes are not this migration's work. Installed skills, deployment, historical prompts, images, and evaluation answers were not updated by this migration.

The research, baseline counts, alternatives, proposed topology, and staged acceptance below retain the decision record. Their original future-tense wording describes the approved plan, not an assertion that implementation is still unapproved. The final implementation section records what changed and what remains unverified.

## Decision proposed

Replace the current broad main-body contract with a compact coordinator, directly usable capability skills, and conditional task references. Extract one shared interaction contract that every active entry reads explicitly. Consolidate the common graphic procedure into the design skill, then load detailed reference observation, artifact production, and result review only when those tasks occur.

Keep the current public skill names for discovery. Keep product art direction as the owner of product decisions. Do not add a new ecommerce entry above it. Keep recipes optional and historical cases separate from instructions. The number of conceptual layers is not an acceptance criterion. The criterion is that each task reads the instructions it needs without first reading unrelated instructions.

This is a concrete change to where instructions live and when they are read. It follows the user's mandatory progressive-disclosure requirement. Runtime evidence is still needed to establish that assistants follow the new read paths and preserve behavior. No context-limit failure, token saving, latency improvement, or image-quality gain has been measured.

## What the external research establishes

The Agent Skills specification distinguishes discoverable metadata, the activated skill body, and resources loaded on demand. Its loading model does not prescribe Oneirloom's current main-method-template responsibility split. An activated body is read in full, so conditions inside a long body do not remove that body's reading cost. [Agent Skills specification](https://agentskills.io/specification)

Anthropic recommends concise entry instructions, references organized by domain or condition, and direct links to needed files. It warns that nested references can lead to incomplete reads and recommends testing actual use. These are authoring recommendations, not proof that a particular repository topology performs better. [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

The following are observed choices in pinned original repositories. They supply design alternatives, not benchmarks or endorsements of every rule they contain.

| Original source and pinned revision | Observed organization | Implication for this proposal |
| --- | --- | --- |
| Anthropic [frontend-design](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/frontend-design/SKILL.md) | A single focused skill grounds design in the subject and brief, then plans and critiques the result. | A meaningful creative process can remain inside a capability entry. A separate business layer is not necessary merely because the process has stages. |
| Anthropic [theme-factory](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/theme-factory/SKILL.md) | Theme details live outside the entry. The selected theme is read after selection; a custom theme is allowed when none fits. | Separate reusable decisions from a chosen preset. Preserve Oneirloom's no-match path. Do not import this repository's mandatory theme-choice dialogue into clear Oneirloom briefs. |
| Anthropic [skill-creator](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/SKILL.md) | It describes metadata, activated instructions, and conditional resources, with explicit resource-reading cues and actual skill runs for feedback. | Give every resource a trigger and evaluate real assistant behavior. Its larger evaluation machinery is not required for this migration. |
| Remotion [router](https://github.com/remotion-dev/skills/blob/0b5db9daae40f42c73544d1cc0a8c733bd530eaa/skills/remotion-best-practices/SKILL.md) and [creation task](https://github.com/remotion-dev/skills/blob/0b5db9daae40f42c73544d1cc0a8c733bd530eaa/skills/remotion-best-practices/remotion-create/REFERENCE.md) | The entry maps concrete tasks to reference files. Creation, captions, maps, and rendering have distinct triggers. Creation also links to further task details. | A task workflow can be a reference rather than another discoverable skill. Adopt explicit triggers, but do not copy nested chains where a direct reference would suffice. Video capability is outside this proposal. |
| UI UX Pro Max [design skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/09170eec67eefd46a7ae85de61b40c194020f997/.claude/skills/design/SKILL.md) | One design entry combines sibling capabilities with task references for slides, banners, icons, and other work. Some operational details remain inline. | Business tasks and shared methods can coexist. This is evidence against a mandatory uniform layer count, not a reason to reproduce its broad entry body or its tool requirements. |
| Superpowers [using-superpowers](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/using-superpowers/SKILL.md) and [Codex reference](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/using-superpowers/references/codex-tools.md) | General skill-use guidance selects host-specific instructions. | Host adaptation is a conditional concern. Do not copy another repository's invocation, staffing, or lifecycle policy into Oneirloom. Actual host tools and user rules remain authoritative. |
| OpenAI [imagegen](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/imagegen/SKILL.md) | Shared prompting guidance is separate from fallback-only CLI references. The entry distinguishes creative intent from execution mode. | Load model and entry details when the requested production path needs them. A prompt task need not inherit every tool's setup instructions. This repository's output formatting is not Oneirloom's output contract. |

The local installed imagegen source was inspected before using its pinned upstream source. The research used original documents and source files. An initial Remotion URL used the wrong directory and returned 404; the verified path is `skills/remotion-best-practices/`. No online authentication, denial, or rate-limit barrier affected the sources used here.

The design inference is narrower than “modularity is good.” Oneirloom needs small, complete reading units with explicit triggers and owners. Adding a fourth named layer would not by itself provide those units. Conversely, preserving three names would not by itself prevent them.

## Current loading costs and dependencies

There are 18 active `skills/*/SKILL.md` files, each with discoverable frontmatter. These are sibling capabilities, not 18 bodies assumed to be present at startup. The following measurements are from the current files, not model context telemetry.

| Current file | UTF-8 bytes | Decoded characters | Lines | Body characters excluding frontmatter |
| --- | ---: | ---: | ---: | ---: |
| `skills/oneirloom/SKILL.md` | 14,153 | 14,127 | 57 | 13,754 |
| `skills/oneirloom-product-art-direction/SKILL.md` | 7,285 | 7,281 | 29 | 6,960 |
| `skills/oneirloom-style-design/SKILL.md` | 4,601 | 4,601 | 34 | 4,253 |
| `skills/oneirloom-style-design/references/graphic-design-sop.md` | 14,746 | 14,746 | 93 | Not applicable |
| `skills/oneirloom-product-art-direction/references/ecommerce-workflow.md` | 6,803 | 6,787 | 45 | Not applicable |
| `skills/oneirloom-result-diagnosis/SKILL.md` | 7,537 | 6,289 | 39 | 6,150 |
| `skills/oneirloom-visual-analysis/SKILL.md` | 6,661 | 6,461 | 56 | 6,327 |

Characters include stored newline characters after UTF-8 decoding. Lines use `splitlines()`. Bytes are the exact file byte counts. These measures do not estimate tokens. The main body's 57 lines illustrate why a line ceiling would be a poor local acceptance rule.

The current main entry requires its whole body to be read. That body includes general routing and output rules alongside product collaboration, model-source maintenance, person defaults, VI completeness, card layout, and watermark placement. Those clauses are not relevant to every use, even when their execution is conditional.

The dependency graph contains useful conditional reads already:

- The main skill selects product art direction for real-product work, design plus the graphic SOP for composed graphics, and a medium when needed. It selects model adapters only after the visual specification.
- Product art direction directly links to the graphic SOP for composed graphics. Its ecommerce reference expands vague briefs, research, facts, revisions, and portable handoff. Its two historical cases are consulted only after a concept is resolved, if useful.
- Design links to the SOP for graphics and to domain checks for isolated product, packaging, 3D, or craft work. It also points real-product tasks back to product art direction. These are responsibility links, not automatic calls.
- Photography and illustration explicitly direct the reader to their styles references. Template indices and matching recipes are conditional. Illustration also reads the graphic SOP for a poster or other composed graphic.
- Result diagnosis reads the graphic SOP for graphics and adds product art direction for product misses. Visual analysis also contains a long graphic-specific restatement and points to the SOP.

The same graphic process is summarized in the main entry, design entry, visual analysis, and result diagnosis, while the SOP carries its full version. Product truth and revision rules appear in the main entry, product entry, ecommerce reference, and diagnosis. Some repetition provides a useful trigger, but repeating the detailed rule creates several places to maintain and several opportunities to load the same reasoning.

There is also a direct-entry contract ambiguity. Product art direction and other methods say to follow the main output contract without explicitly reading it. Icon design links to the entire main skill. A host that selects a method directly may either miss shared rules or load the whole coordinator to find them. This is a static dependency risk. No inspected runtime trace proves that it caused a failed answer.

### Representative current read sets

These are static, representative sets derived from the instructions, counted once per unique file. They are not executed conversations, mandatory closures for every host, or observed maximums. They exclude images, conversation text, host instructions, discovery metadata outside these files, unselected adapters, and optional templates. Camera, color, source-reconstruction, or model files add to a set when the actual brief needs them. If “viewpoint matters” is interpreted broadly, the current router can load more than these sets.

Aliases below name exact current files:

| Alias | File |
| --- | --- |
| M | `skills/oneirloom/SKILL.md` |
| P | `skills/oneirloom-product-art-direction/SKILL.md` |
| E | `skills/oneirloom-product-art-direction/references/ecommerce-workflow.md` |
| D | `skills/oneirloom-style-design/SKILL.md` |
| G | `skills/oneirloom-style-design/references/graphic-design-sop.md` |
| F | `skills/oneirloom-style-photography/SKILL.md` |
| FS | `skills/oneirloom-style-photography/references/styles.md` |
| I | `skills/oneirloom-style-illustration/SKILL.md` |
| IS | `skills/oneirloom-style-illustration/references/styles.md` |
| R | `skills/oneirloom-result-diagnosis/SKILL.md` |

| Representative task and assumption | Current unique-file set | Files | Bytes | Characters | Lines |
| --- | --- | ---: | ---: | ---: | ---: |
| Clear realistic bread breakfast **poster**, supplied facts and copy, portable Chinese-only prompt | M P D G F FS | 6 | 45,639 | 44,563 | 267 |
| Vague bread selling brief, first reply explores direction before composition | M P E | 3 | 28,241 | 28,195 | 131 |
| The vague brief then selects a photographed miniature breakfast poster | M P E D G F FS | 7 | 52,442 | 51,350 | 312 |
| Only the background changes in the same breakfast poster; cold entry with the confirmed brief supplied | M P D G F FS R | 7 | 53,176 | 50,852 | 306 |
| Wrong package structure in a composed product result; supplied source and current intent, no reference-reconstruction request | M P D G R | 5 | 48,322 | 47,044 | 252 |
| Nonproduct original illustration poster, no style-image transfer or named recipe | M D G I IS | 5 | 37,978 | 36,886 | 235 |

For the vague first turn, the SOP's own order permits product understanding before a graphic direction exists. Its read is deferred until that branch is selected. The background row reflects the present broad diagnosis route for a local correction; it does not assert that a failed result exists. The package row omits medium drafting because diagnosis can preserve the supplied treatment without redesigning it. These choices make the accounting reproducible without pretending the prose specifies one deterministic loader.

In a continuing chat, unchanged files already read need not be read again. The unique-file totals describe cumulative instruction content for a cold task, not additional content on every turn. Reading sequentially does not evict older resources from the host context.

To reproduce the counts without a new script file, use Python's `Path.read_bytes()` on each listed file, decode with `utf-8-sig`, count `len(text)` and `len(text.splitlines())`, and sum unique paths. Remove only the initial YAML frontmatter when measuring body characters. Count active skills with `Path('skills').glob('*/SKILL.md')` from the named source checkout.

## Alternatives considered

Progressive disclosure is mandatory for all candidates. “Keep the current three layers and test them” does not meet the requested remediation.

| Candidate | Structure and loading | Strength | Cost or failure mode | Decision |
| --- | --- | --- | --- | --- |
| A. Compact coordinator and directly usable capabilities | Preserve public capability SKILL entries. Each reads one shared contract and selects task references directly. Move specialist detail out of the broad coordinator and split the graphic SOP by actual task. | Supports both named method use and general Oneirloom use. Retains meaningful owners while reducing unrelated compulsory reading. | Cross-skill links require the collection's shared contract to be available. File splits must preserve constraints and avoid another chain of routers. | **Accepted as A and implemented in source.** It addresses observed file organization without adding a business hierarchy. |
| B. Business-first hierarchy | Main routes to new ecommerce, editorial, identity, or other business entries; each routes to methods and recipes. Entries can still load references conditionally. | Useful if those businesses acquire distinct multi-deliverable policies and procedures. | Adds an obligatory entry to today's ecommerce path, duplicates product art direction, and requires domains that do not yet exist. Direct method entry still needs a shared contract. | Reject for current scope. Reconsider only after a real task needs business policy that no existing owner can hold. |
| C. One discoverable SKILL with all capabilities as references | Keep only Oneirloom discoverable; route directly to product, graphic, medium, adapter, and diagnosis reference files. | Small discovery metadata and one shared starting contract. Short internal paths are possible. | Removes existing public method entry points and requires migration of invocation names and installations. Gains from metadata reduction have not been measured. | Viable for a new collection, excessive migration for this one. Do not retire working entry names without evidence. |

Candidate A preserves useful public interfaces while changing compulsory reading. Its references are owned decisions, not one-file-per-stage wrappers. The graphic design skill contains the complete common design procedure; it does not forward every graphic to another mandatory workflow file. The product skill contains product truth rules; it does not require a second file merely to learn that unseen filling is unknown.

## Proposed topology and ownership

The following topology was proposed and has now been implemented in source. The implementation record below supplies the status boundary.

```text
Discovery metadata: the existing 18 public SKILL entries

oneirloom/SKILL.md                         compact coordination and routing
  -> oneirloom/references/interaction-contract.md
  -> selected capability SKILL.md

Any directly selected capability SKILL.md
  -> oneirloom/references/interaction-contract.md
  -> relevant capability or task reference, with an explicit trigger

oneirloom-product-art-direction/SKILL.md   product evidence and concept decisions
  -> references/ecommerce-workflow.md     vague brief, research, copy or handoff detail
  -> oneirloom-style-design/SKILL.md      only for composed graphics

oneirloom-style-design/SKILL.md           complete common graphic design procedure
  -> references/graphic-observation.md   detailed style-reference transfer
  -> references/graphic-production.md    finished graphics and asset assembly
  -> references/graphic-review.md        an actual or reported graphic result
  -> references/styles.md                isolated product, 3D or craft domain checks

Other capabilities: medium, source analysis, spatial relations, model adapters,
diagnosis, characters, stickers, icons, identity, tutorials, prompt cards
  -> their own task references only when needed
  -> local templates/index.md -> one selected recipe -> relevant evidence
```

All paths in this sketch are relative to `skills/`. Discovery metadata advertises capability and trigger. The activated body supplies enough instruction to perform its normal task. A reference contains conditional detail without a separate discovery identity. A template describes a particular visual mechanism and adjustable choices. A historical record preserves what actually happened. These are different information roles, not a required number of filesystem or call layers.

Retain the short template index as the deliberate lookup exception. It avoids loading every recipe. Once the selected recipe is known, read it directly. Do not make a template index the route to a general rule, model contract, or required product constraint. Keep original evidence paths with their recipe or case.

### One current owner for each invariant

| Invariant | Proposed authoritative owner | Availability and consumer behavior |
| --- | --- | --- |
| Prompt language, copyable blocks, affirmative complete prompts, literal image text, controls outside prompts, truthful verification status | `skills/oneirloom/references/interaction-contract.md` | Main and every capability explicitly read this file before their first substantive response, unless its unchanged content is already available. Prompt clauses apply only when delivering or revising prompts. Artifact and article formats remain with their capability owners. |
| Current task, confirmed choices, local revisions, replacement of rejected directions, coupled-change explanation | The same interaction contract defines the rule; the active assistant maintains the compact notes | The coordinator manages selection when entered through main. A directly selected capability uses the current chat itself; it does not invoke main to obtain continuity. Notes preserve facts, sources, unknowns, creative choices, and the latest change without a schema or service. |
| Real product facts, unknowns, conflicts, and the distinction between fiction and product claims | `skills/oneirloom-product-art-direction/SKILL.md` | Any depiction or correction of a real product reads P. Keep critical truth rules in P's body. Do not defer them to an optional case or category file. |
| Graphic process, subject meaning, composition, production selection, and recipe adaptation | `skills/oneirloom-style-design/SKILL.md` | Any composed graphic reads D. D owns Understand, Observe, Design, production selection, review obligation, and correction direction. Conditional references expand observation, execution, and review without redefining their order. |
| Generic template choice | Each owning capability's SKILL body, applying the interaction contract's user-priority rule | Read its short index only if a recipe could help. A named recipe still must fit the inspected subject. No match permits composition from the method. Graphic recipes obey D's adaptation rules. |
| Model capabilities and actual entry controls | The selected `skills/oneirloom-model-*/SKILL.md` and its relevant primary-source references | Select only the requested model, after visual intent is established. Confirm actual entry capabilities before giving controls. Unknown or missing entry permits portable text; it does not permit invented settings. |
| Source observation and uncertainty | `skills/oneirloom-visual-analysis/SKILL.md` | Use for reconstruction, ambiguous visible relations, or requested analysis. Graphic layout observations use D's `graphic-observation.md`; portrait and garment checks retain their present source-analysis owner. Product facts retain P's owner. |
| Source-to-prompt versus prompt-to-result diagnosis and causal uncertainty | `skills/oneirloom-result-diagnosis/SKILL.md` | Use for an actual or user-reported miss, not every requested edit. R compares source, current intent, submitted prompt, and result separately. It reads P for product facts and `graphic-review.md` for graphic results. |

The shared contract is a dependency in the existing collection, not a new discoverable skill. Its body must remain limited to rules every entry needs or must select immediately by output type. It must not accumulate VI inventories, watermark instructions, model setup, or product scenarios. Independently distributing a capability requires including this dependency or resolving it by the host's supported resource mechanism. This proposal does not claim standalone copies currently include it.

The wording at each entry must name the file and the action: read the shared interaction contract unless the unchanged content is already available. “Follow main” and a bare link are insufficient. A Markdown link is navigation, not a tool call. No helper skill is automatically invoked. Resolve the exact selected skill through the actual host catalog and use the repository sibling path as fallback.

Avoid circular reads. The shared contract links to no capability body. A capability never reads main to discover shared policy. A graphic result can read the graphic-review leaf directly from R without first loading D and then returning to R. If diagnosis reveals a conceptual mistake, D becomes relevant work, not an unconditional read-back loop. Reuse already read, unchanged content throughout.

### What the compact coordinator retains

Main retains the public aliases, deliverable selection, a short condition-to-capability table, priority of explicit user choices, and the instruction to read the shared contract. It also retains the timing rule that visual intent precedes model adaptation. It does not repeat product truth examples, the graphic SOP, artifact inventories, card geometry, watermark placement, or model-source archival procedures.

Person defaults remain in `skills/oneirloom/references/person-prompts.md`. Each relevant person-producing entry must directly name this reference under a person-prompt trigger, including direct photography, character, figure-art, and relevant illustration use. The shared contract contains only that trigger. It does not contain the portrait rules themselves.

The core output contract preserves Chinese and equivalent English prompts unless the user requests another language scope; complete revisions rather than appended fragments; affirmative visible construction; exact literal copy; separate requested or entry-required negative fields; and honest generation and inspection status. Explicit native artifacts, tutorials, and existing-image prompt cards retain their own deliverable formats. A prompt card preserves its supplied prompt rather than rewriting it to satisfy a new bilingual request that the user did not make.

Portable Doubao guidance remains text and ordinary reference-upload advice. It establishes no native Skill installation, invocation, identity lock, or unsupported control. The short shared contract states that boundary; detailed assistant-brief versus image-prompt examples remain conditional ecommerce guidance.

## Concrete file migration

Paths are relative to the source repository. This table preserves the approved migration plan; new targets now exist as recorded below. Historical exact prompts, images, records, and existing evaluation answers are not migration input to be rewritten.

| Current location and material | Proposed destination or retained responsibility | Concrete change and preserved reason |
| --- | --- | --- |
| `skills/oneirloom/SKILL.md`: output contract and continuity rules | New `skills/oneirloom/references/interaction-contract.md` | Move the common rules into one compact dependency. Main and all direct entries explicitly read it. Keep output-type selection and current user priority intact. |
| `skills/oneirloom/SKILL.md`: product workflow paragraphs | `skills/oneirloom-product-art-direction/SKILL.md` | Retain only the routing trigger in main. P keeps factual provenance, unknowns, conflicts, creative transformations, and product-specific concept development. |
| `skills/oneirloom/SKILL.md`: graphic procedure and artifact inventories | `skills/oneirloom-style-design/SKILL.md` and the already owning sticker, icon, brand, and card SKILL files | Main selects the deliverable. The owner defines completeness. Preserve actual files versus previews and prompts versus finished art distinctions. |
| `skills/oneirloom/SKILL.md`: watermark placement paragraph | Existing `skills/oneirloom-prompt-card/SKILL.md`, new `references/oneirloom-watermark.md` only if another current caller needs the same placement detail | Remove placement details from main. Keep a watermark-specific route. Prefer the existing card owner for card work; do not create the new file absent a second caller. Preserve the approved creature, outlines, lettering, and no-automatic-icon-watermark rule. |
| `skills/oneirloom/SKILL.md`: model-source maintenance detail | Existing `skills/oneirloom-model-krea-2/SKILL.md` and `skills/oneirloom-model-qwen-image-2-1/SKILL.md` | Keep visual-intent-before-adapter in main. Each adapter owns its source snapshot and entry-specific guidance. Avoid creating another generic adapter layer. |
| `skills/oneirloom-style-design/references/graphic-design-sop.md`: common process | `skills/oneirloom-style-design/SKILL.md` | Move the complete concise process into D. Retire the old mandatory SOP path after migrating every active caller. Preserve Understand, Observe, Design and the reasons identity, action, and meaning precede production. |
| Same SOP: detailed reference reading, fragments, joins, material interpretation, subject transfer examples | New `skills/oneirloom-style-design/references/graphic-observation.md` | Load for style-reference transfer or a concrete uncertainty in these relations. Preserve the original distinctions and rationale. D keeps the mandatory inspect-before-recipe instruction. |
| Same SOP: actual sketches, generated assets, compositing, native sources, exports | New `skills/oneirloom-style-design/references/graphic-production.md` | Load when producing a finished artifact or planning a selected composite requiring asset assembly. Prompt-only direct generation does not need this file. Preserve tool constraints, provisional anatomy, real source delivery, and unavailable-tool boundaries. |
| Same SOP: detailed whole-image comparison and correction review | New `skills/oneirloom-style-design/references/graphic-review.md` | Load when a graphic result exists or is reported. Preserve identity before local polish, source-result comparison, exact-copy checks, and actual inspection status. R retains causal attribution. |
| `skills/oneirloom-visual-analysis/SKILL.md` and `skills/oneirloom-result-diagnosis/SKILL.md`: repeated graphic paragraphs | Direct conditional links to the appropriate new D reference | Replace detailed repetition with scope and trigger. Retain reconstruction-specific structural checks and diagnostic uncertainty with their existing owners. Do not make analysis-only use read the whole graphic creation procedure. |
| `skills/oneirloom-product-art-direction/SKILL.md` and `references/ecommerce-workflow.md` | Same paths | Keep truth and clear-brief defaults in P. E expands vague choice, useful research, exact-copy gaps, and portable handoff. Remove duplicated common formatting and revision prose in favor of the shared contract. E must not become compulsory for every bread image. |
| `skills/oneirloom-style-photography/references/styles.md` and `skills/oneirloom-style-illustration/references/styles.md` | Same paths | Change their SKILL read triggers to medium selection or a needed technique distinction. A fully specified medium can use its SKILL checklist without an automatic style catalogue read. |
| `skills/oneirloom/references/person-prompts.md` | Same path | Keep its existing defaults and proportions. Add explicit direct-entry triggers where relevant. Do not load person detail for bread-only or packaging-only work. |
| The existing 18 `skills/*/SKILL.md` entry points | Same paths and public names | Add the shared-contract read cue. Change only coupled references and duplicate policy needed by this migration; do not redesign unrelated sticker, VI, tutorial, or card capabilities. |
| `skills/*/templates/index.md`, selected `template.md`, and case folders | Same ownership and paths | Keep recipe selection optional. Remove only duplicated runtime policy when a shared rule replaces it, if authorized during migration. Preserve recipe-specific relations and all exact historical evidence. The chocolate folder remains a historical case despite its `template.md` filename. |
| `docs/architecture.md` | Same file, revised only after acceptance and authorized migration | Replace the layer-count premise with the selected loading and ownership model. Preserve still-valid invariants and historical migration rationale. The source implementation now supersedes its former layer-count premise. |

During the SOP move, account for each current paragraph in its new owner before retiring the active file. Git history preserves the original revision, but it is not a substitute for retaining still-valid rationale in the live guidance. Update runtime callers only. Historical snapshots under `work/architecture-migration/before/`, exact submitted prompts, and evidence records retain their original links and contents as historical material.

## Triggers and intended reads

The proposed shared contract is C: `skills/oneirloom/references/interaction-contract.md`. Existing aliases M, P, E, D, F, I, and R refer to their proposed contents at the same paths. O, X, and V mean D's new `graphic-observation.md`, `graphic-production.md`, and `graphic-review.md` respectively. Baseline counts remain historical working-tree measurements. Any after comparison must use the same newline convention and does not establish token, speed, or runtime-context savings.

| Condition | Read now | Postpone or omit |
| --- | --- | --- |
| Any fresh main entry | M and C, then the selected capability | Every unselected capability body and its references |
| Any fresh directly named capability | That capability and C | M. Main is not a contract dependency. |
| Real product depiction | P, retaining supported facts and unknowns | Historical product cases, category references, research, and graphic design unless needed |
| Clear composed graphic | D, plus relevant subject and medium capability | Vague-brief examples, actual-production detail, and result review until their trigger occurs |
| Vague product request | P and E before choosing direction | Medium, composition detail, recipe, and adapter until the choice makes them relevant |
| Selected style image or layout reconstruction | O, source analysis when reconstruction checks apply, then the matching recipe if useful | Unrelated recipes and production detail |
| Background-only prompt revision with a confirmed design and no reported miss | C and P when it is a real product; reuse the confirmed prompt and notes | R, fresh concept exploration, template search, and unchanged medium files |
| Actual or reported product result miss | R and P; V for graphics | New concepts unless diagnosis identifies a concept failure; generated details as product facts |
| Finished graphic or selected composite production | X and the selected capability's deliverable instructions | Unused execution modes and model adapters for native code work |
| Requested model after intent is resolved | Only that adapter, its writing or task reference, and relevant official source | Other models and irrelevant source archives; unsupported entry controls |
| Existing image-and-prompt card or article-only edit | Card or tutorial capability and C | Product, graphic generation, medium, and model branches unless the task actually changes |

The following usage sketches are proposed read paths, not assistant runs. Each main-entry path has a direct-method variant that omits M and retains C. Read C once when unchanged. Necessary input images still require actual inspection when an image task is later authorized.

| Scenario | Intended main-entry reads | What the assistant does and defers |
| --- | --- | --- |
| Clear bread breakfast poster with exact Chinese-only copy | M C P D F | Use the supplied product evidence and chosen scene immediately. D supplies the graphic process; F supplies photographic treatment. No E, style catalogue, recipe, production file, or result-review file is needed for the prompt-only request. Do not invent filling or claim a generated image. |
| “Help me sell this bread,” then a miniature morning station is selected | First M C P E. After selection, add D and F. | Ask only consequential questions and offer distinct product-linked mechanisms if helpful. After the choice, write the complete chosen prompt. Fictional station elements remain scenery; the bread's internal composition stays unknown. No automatic chocolate-river case. |
| Change only the background of that confirmed prompt | No new file read when C and P remain available. A cold direct product entry reads P C and uses the supplied current prompt and choices. | Preserve valid product, copy, layout, and medium decisions. Explain any required coupled change. A pure edit request is not evidence of a failed result. If the current target is missing, obtain only the missing target rather than inventing continuity. |
| A result changes a folded soft package into a rigid box | Main M C R P V. Direct R entry reads R C P V. | Compare the original product, current intent, submitted prompt if available, and actual or reported result. Restore supported package relations in the full correction. Read D only if understanding or composition must be redesigned. If the result is only described, do not claim visual inspection. |
| Original nonproduct illustration poster | M C D I | Develop message, subject, layout, and the specified medium. No product files. Add O only for a selected style reference; add the illustration styles reference only for an unresolved medium distinction. No-match template selection remains valid. |
| A selected model is added to any prompt task | Reuse its visual intent, then add the named adapter and its task-specific references | Adapt expression without changing the accepted aesthetic. An unknown entry receives portable text. No assumed native Doubao Skill support or invented fields. |

These sets make a smaller compulsory body possible; they do not make files disappear from a continuing context. Exact file-count reduction is not the objective. For example, the added shared contract can increase a direct entry's file count while preventing a read of the much broader main body. Measure actual characters and observed reads after migration, then judge them alongside instruction preservation.

## Staged migration and acceptance

The user authorized source changes after this plan was written. The stages below preserve the intended acceptance sequence; source authorship is implemented, while actual assistant exercises remain pending. Use the existing repository and task record. Assign one writer per coupled file set. Do not run independent writers against the shared contract, main router, or design skill at the same time. The Primary owns the selected design and final acceptance; authoritative design-document revisions retain the project's authoring policy.

| Stage | Bounded changes | Acceptance evidence |
| --- | --- | --- |
| 1. Make shared policy reachable from every entry | Create C from the existing common rules. Update M and all 17 capability entries to read it explicitly. Replace full-main output-policy links. Keep specialist behavior and the old SOP intact for this stage. | Inspect the content diff for every preserved common rule. Verify direct links from all 18 entries, local link existence, and fences. Perform one main-entry and one direct-product prompt interaction with actual inputs, replies, and file reads. Both honor explicit language overrides, complete affirmative blocks, revision continuity, and inspection status without loading main solely for policy. |
| 2. Consolidate graphic ownership and remove compulsory detail | Move common G rules into D. Create O, X, and V from the existing detailed paragraphs. Update active callers in main, product, analysis, diagnosis, illustration, brand, stickers, and icons. Remove the old active G only after its material and callers are accounted for. | Review paragraph-to-owner preservation in the existing task record. Verify no active instruction points to retired G. Run the clear breakfast poster and original illustration poster through actual assistant entries. Their read records omit X and V for prompt-only creation and preserve graphic reasoning, full prompts, exact copy, and truthful status. Run a style-reference task to establish O is read when needed. |
| 3. Tighten conditional product and revision reads | Deduplicate P and E against C. Make E's trigger explicit. Change routine medium catalogue reads to conditional reads. Route a simple revision through current notes; reserve R for reported or observed misses. Move remaining main-only watermark, artifact, and adapter details to their existing owners as mapped above. | Run the vague bread dialogue through its actual follow-up, a background-only revision, a rejected-direction replacement, and a package miss. Save actual input and reply sequences plus read evidence. Confirm retained facts, no reopened settled questionnaire, no invented ingredient, no forced historical recipe, no unrequested redesign, and separate source-to-prompt and result deviations. A source conflict blocks only its dependent depiction. |
| 4. Record the accepted structure and delivery boundary | After the prior evidence is reviewed, revise `docs/architecture.md` and the index to describe the implemented topology. Measure the same representative file sets. Inspect the actual package's shared-resource inclusion if packaging is separately authorized. | Compare before and after character counts and observed read paths without claiming token or speed results. Confirm direct entries can resolve C in the environment actually tested. Distinguish source-file completion, installed-file availability, new-session discovery, and behavior. Deployment and installation remain separately authorized actions. |

The representative exercises cover different loading decisions. They are not a proposal to replace remediation with three tests. They need actual assistant requests and responses using the edited source. Record the run's available model and host provenance, the input, actual output, files read, and the evidence-based verdict. A handwritten ideal answer is design material, not run evidence. A missing transcript or read record remains an unverified outcome. Existing test mechanisms can be reused when available; do not create a large evaluation framework or an automatic runner for this migration.

The existing [ecommerce acceptance record](../work/ecommerce-workflow-20261003/acceptance-report.md) reports 13 added cases alongside 47 preserved cases, with 7 saved text judgments passing, 1 failing, and 5 unexecuted. It explicitly lacks independent per-case fresh-session traces and real product or result images. Its guided manual examples are not runs. Preserve the failed exact-label answer and the unexecuted cases. Reuse relevant inputs and failure criteria, not their saved answers as proof of the new instructions. This proposal has not replayed those evaluations.

Minimal later acceptance must include the exact-label dependency: when exact brand text is requested but unreadable, the assistant cannot silently substitute an unreadable-label delivery. It can continue independent layout, request usable evidence, and offer an explicitly described alternative for the user to choose. This follows an existing recorded text failure, not a new hypothetical gate. Image quality, package fidelity in generated pixels, and repeatability require separately authorized generation and inspection. None is claimed here.

## Expansion boundaries

Add a task reference when an existing entry carries substantial detail that only a current conditional branch needs. Add a discoverable skill only when users need to select a distinct capability with its own decisions and deliverable. Add a category reference only when a real product category has supported requirements that cannot remain concise in P. Do not pre-create food, cosmetics, appliances, or other empty domain trees.

Keep static prompts and revisions as the immediate product scope. Preserve the reusable subject and style descriptions as possible later Live or video references, without implementing Live or video production. Payment, membership, accounts, stores, web applications, publication systems, and new generation services are outside this migration. Existing native-artifact and tutorial capabilities remain available; their existence does not authorize development of new product systems.

Creative scope remains broad: realistic catalog views, use scenes, miniature worlds, scale changes, ingredient architecture when supported, fantasy, and anthropomorphism remain possible. Product truth constrains what the image implies about the sold item. It does not turn every approved fantasy into a documentary photograph.

No hard line or token gates, new schema, state machine, daemon, dependency service, approval ladder, or second task ledger is proposed. Stop the migration once the shared contract is reachable, the task reads are conditional, the preserved rules are accounted for, and the bounded behavior evidence supports the intended paths.

## Source implementation and pending acceptance

Proposal A was implemented in the maintained source checkout. The 18 public names remain unchanged. Every entry explicitly reads the new shared interaction contract unless unchanged content is already available. Main is a compact coordinator. Product truth stays in the product body. Graphic design contains the complete common process and directly selects observation, production, and review detail. Diagnosis reads review directly for graphic misses. Routine edits no longer automatically select diagnosis. Photography and illustration catalogues are conditional. Person-producing entries directly link existing person defaults.

The old graphic SOP was removed after its active callers were migrated. The four additional coupled callers were the reconstruction workflow, design domain reference, graphic source notes, and experimental-editorial template index. Their links and process cues changed; domain rows, recipe mechanisms, prompt scaffolds, and historical evidence were preserved. Qwen writing guidance and two prompt templates now name the shared output contract rather than main. These narrow caller changes were separately reviewed for scope by the Primary.

No new watermark reference, business entry, runtime loader, schema, state machine, rule gate, template, or evaluation framework was created. Existing card, sticker, icon, VI, tutorial, person-default, and historical-evidence contracts remain with their owners. The actual card renderer and assets were not changed. Model source-maintenance guidance moved from main into both existing adapters.

### Invariant ownership migration

C means the shared interaction contract, M the coordinator, P product art direction, D graphic design, O graphic observation, X graphic production, V graphic review, and R result diagnosis. Paragraph numbers below refer to non-heading paragraphs within the named section of the old `graphic-design-sop.md` at `d5df2ed`. These identify preserved reasoning, not just keywords.

| Old material | Current owner | Preserved constraint and reason |
| --- | --- | --- |
| Main aliases and workflow 1–2 | M and C | Existing public names, deliverable selection, explicit resource reads, confirmed choices, conditional capability selection, and dependent-only gaps. |
| Main workflow 3 | C, P, D, and M | Compact sourced notes, no forced template, no-match composition, user priority, product truth, graphic identity and meaning, and 3–5 anchors only for non-graphic prompts. |
| Main workflow 4 | M and existing Krea/Qwen adapters | Visual intent before adaptation; relevant primary-source snapshots with URL/date/revision/hash; actual-entry controls; producing versus target model; one intent across models. |
| Main workflow 5 | D, X, C, and person-producing entry links | Production selection, explicit tool constraints, provisional sketches, complete per-asset prompts, affirmative spatial relations, bidirectional fidelity check, and directly reachable person defaults. Reconstruction keeps its own counterexample procedure. |
| Main routing and watermark paragraphs | M and existing card/icon/tutorial/brand/sticker owners | Routing remains compact; card geometry, approved creature signature, lettering outlines and placement, no automatic icon watermark, article format, actual individual assets, and full-VI completeness remain at their existing owners. |
| Main output contract | C, D, X, and existing deliverable owners | Required languages and literal image text, separate complete blocks, affirmative construction, separate negative fields only when required, controls outside prose, portable Doubao limits, complete revisions, actual artifacts, and truthful inspection status. |
| SOP introduction paragraphs 1–4 | D introduction and source-note link; C continuity | Same graphic scope and stage order, understanding before tooling, compact notes without a new ledger or approvals, separate non-graphic procedures, and local-synthesis/source limits. |
| SOP Understand paragraphs 1–4 | D section 1 | Purpose and exact copy; connected subject form/action; facts versus interpretations including the crescent example; meaningful props and a concrete understanding account rather than title/palette/size alone. |
| SOP Observe paragraphs 1–6 | O, retained in full; D section 2 trigger | Inspect image before recipe, role separation, independent versions/directions, global continuity versus local interruptions, joins and layers, material limits, estimates, and source-grounded attention. |
| SOP Design paragraphs 1–3 | D section 3 and O, retained in full | Explain transformations, retain defining relations, use actual anatomy for opposed views, resolve fragments and coverage, preserve deliberate gaps, and integrate material finish without imposing aged paper. |
| SOP Design paragraphs 4–6 | D section 3 and O, retained in full | Meaningful crop and hammock example, marble-neck versus creature anatomy, provisional masks, exact title reflow, readable interleaving, and no decorative filler for missing copy. |
| SOP Design paragraphs 7–8 | D section 3 and O, retained in full | Whole meaning before coordinates, return to understanding/observation, no prompt-padding or model-blame substitute, resolved reasons without mandatory approvals or sketch count. |
| SOP Production paragraphs 1–5 | X, retained in full; D section 4 selection | Design-driven production, code/vector/model constraints, inspected provisional sketches and assets, actual alpha support, complete prompts or necessary composite assets, observable finish, and plan/asset/assembled-artifact distinction. |
| SOP Review paragraphs 1–5 | V, retained in full; D section 5 obligation | Identity before polish, source/result at equal visual height, intended viewing size, copy and factual checks, joins and shared material, source fidelity separate from submitted-prompt compliance, causal uncertainty, and whole-image verdict over local scores. |
| SOP Correct paragraphs 1–2 | V, retained in full; D section 5 and R | Repair the responsible stage, preserve successes, local editable fixes when design is intact, continue authorized work, and bounded diagnosis after two controlled misses. |
| SOP Correct paragraphs 3–5 | V, retained in full; C, D, and X delivery rules | Complete prompt path rather than forced asset-only output, actual finished preview/source/inspection, historical prompt and metadata preservation, and no inherited validation or repeatability claim. |
| SOP Carry paragraphs 1–2 | C continuity, D process, O closing | Compact notes carry intent/evidence/adaptation/path/review without a schema; inspect optional recipes and do not create persistent templates for every new subject. |
| Product/Ecommerce repeated rules | P and C; E conditional detail | P retains all product truths, source conflicts, realistic and fantasy ranges, fictional-scene boundaries, and exact-label dependency; C owns continuity; E handles vague choice, useful research, missing copy, and assistant handoff. |
| Analysis and diagnosis graphic restatements | O and V directly; original analysis checks and R attribution | Analysis-only use avoids creation; actual/reported misses use review without an automatic creation loop. Structural anchors and source-to-prompt versus output deviations remain distinct. |

### Evidence and limits

The baseline collector saved pinned Git-blob measurements in `work/progressive-disclosure-20261003/baseline.json`. The original tables above measured working-tree bytes including their stored newline characters. For example, main was 14,153 bytes in that snapshot and 14,096 bytes in its LF Git blob. Do not attribute newline conversion to architecture savings. Compare normalized LF text or another consistent convention for before and after counts.

Author self-checks cover frontmatter/public-name preservation, explicit contract reachability, person-reference triggers, local links, balanced fences, and absence of active retired-SOP references. Author checks passed for all 18 entry frontmatters and public names, all 18 explicit shared-contract cues, and all 17 person-producing entry links. An explicit 33-file owned-path check found 183 resolvable local links and balanced fences with no failures. No active Markdown under `skills/` names the retired SOP path. Old SOP Observe, Design, Production, Review, and Correct sections were compared with `d5df2ed` and are retained verbatim after newline normalization in O, X, and V. Fenced prompt content in the three coupled templates is unchanged. `git diff --check` returned no whitespace errors. These are author self-checks, not independent behavior evidence. Independent source review, representative assistant inputs/replies/read records, installed dependency availability, new-session discovery, and image behavior remain separate pending acceptance. No generation or visual inspection was performed during this migration. Existing failed and unexecuted evaluation cases remain unchanged.


The additional coupled-path allowance changed only these active instructions outside entry bodies and the new reading units:

| Path | Old clause | New clause |
| --- | --- | --- |
| `skills/oneirloom-visual-analysis/references/reconstruction-workflow.md` | Old SOP owns graphic process order; use SOP composition steps | Creation/redesign reads D; source analysis alone reads O; composition steps belong to the design method |
| `skills/oneirloom-style-design/references/styles.md` | Old SOP link and two SOP process cues | D link and design-process cues; domain checks unchanged |
| `skills/oneirloom-style-design/references/graphic-design-sources.md` | Old SOP link and source-limit/process references | D link and equivalent process references; original sources and limits unchanged |
| `skills/oneirloom-style-design/templates/experimental-editorial-posters/template.md` | Read `../../references/graphic-design-sop.md` | Read `../../SKILL.md`; recipe relations unchanged |
| `skills/oneirloom-model-qwen-image-2-1/references/writing.md` | Main requested-language contract | Direct link to C; enhancer contract unchanged |
| `skills/oneirloom-style-photography/templates/xiaohongshu-squat/template.md` | Main output contract and languages required by router | Direct link to C and languages required by shared contract; scaffold unchanged |
| `skills/oneirloom-style-design/templates/blind-box-comparison/template.md` | Router output contract | Direct link to C; accepted prompt blocks unchanged |

### Authored path manifest

The following 33 source Markdown files were authored or amended by this assignment. Paths are relative to the source checkout. External governance, Git index, LFS, and baseline-receipt changes are excluded.

```text
skills/oneirloom-brand-identity/SKILL.md
skills/oneirloom-camera-composition/SKILL.md
skills/oneirloom-character-sheet/SKILL.md
skills/oneirloom-color-light/SKILL.md
skills/oneirloom-expression-stickers/SKILL.md
skills/oneirloom-figure-art/SKILL.md
skills/oneirloom-icon-design/SKILL.md
skills/oneirloom-image-tutorial/SKILL.md
skills/oneirloom-model-krea-2/SKILL.md
skills/oneirloom-model-qwen-image-2-1/SKILL.md
skills/oneirloom-product-art-direction/SKILL.md
skills/oneirloom-prompt-card/SKILL.md
skills/oneirloom-result-diagnosis/SKILL.md
skills/oneirloom-style-design/SKILL.md
skills/oneirloom-style-illustration/SKILL.md
skills/oneirloom-style-photography/SKILL.md
skills/oneirloom-visual-analysis/SKILL.md
skills/oneirloom/SKILL.md
skills/oneirloom/references/interaction-contract.md
skills/oneirloom-product-art-direction/references/ecommerce-workflow.md
skills/oneirloom-style-design/references/graphic-observation.md
skills/oneirloom-style-design/references/graphic-production.md
skills/oneirloom-style-design/references/graphic-review.md
skills/oneirloom-visual-analysis/references/reconstruction-workflow.md
skills/oneirloom-style-design/references/styles.md
skills/oneirloom-style-design/references/graphic-design-sources.md
skills/oneirloom-style-design/templates/experimental-editorial-posters/template.md
skills/oneirloom-model-qwen-image-2-1/references/writing.md
skills/oneirloom-style-photography/templates/xiaohongshu-squat/template.md
skills/oneirloom-style-design/templates/blind-box-comparison/template.md
docs/architecture.md
docs/architecture-progressive-disclosure-proposal.md
PROJECT-FILES.md
```

Retired instruction: `skills/oneirloom-style-design/references/graphic-design-sop.md`.
