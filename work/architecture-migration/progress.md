# Three-layer skill migration

Goal: route requests through the main skill and reusable method skills into indexed prompt templates with local image evidence.

Status: source migration and structural acceptance complete. Work performed personally by the Primary.

Changes: 13 active skills (one router and 12 methods), six indexed templates, and one preserved historical generated example. Former squat, character-card-template, and halftone recipe skills were merged into their method owners. Conditional person guidance moved out of the router body. Existing user edits and tutorial/model work were preserved.

Ownership: an external halftone edit was detected and that branch was paused. The user confirmed other writing had ended before migration resumed. The latest four rule paragraphs were preserved verbatim. Its now-obsolete installed junction was removed after checking its exact target; the illustration junction exposes the migrated template.

Evidence: python scripts/check_skills.py passed. All local documentation links, template index membership, image-record paths, and the example image hash passed. Original character-card and rainy-night prompt blocks were preserved exactly. All 27 existing behavior cases were preserved; six new scenarios were added, not executed. All 13 installed entries and all template files read back identically through existing junctions. Existing indoor portrait inspected personally, with deviations recorded; actual submitted prompt and PNG preserved exactly.

Limits: no new image generation, no independent behavioral model run, and no fresh-session discovery test. Untested templates and the image-less user-reported rainy-night success remain labeled accurately.

Detailed evidence: acceptance.json. Original snapshots: before/ and halftone-after-external-edit.md. No commit, push, or publication performed.

## Dreamweaver namespace migration, 2026-09-30

Goal: rename the collection, source root, all active skill IDs and installed entries, and both remote repositories to Dreamweaver.

Result: source now resides at J:/PigeonYang/skills/dreamweaver. Main ID is dreamweaver; all 13 method IDs use dreamweaver-. Both GitHub repositories and remote/LFS URLs were updated, with separate rename-only commits based on each previous remote version. Existing uncommitted source changes were preserved and were not published. All 362 inventoried files remain; dirty status is identical after name mapping, apart from migration evidence. Linked managed worktree data and directory name were preserved, and its Git pointer was repaired.

Acceptance: native Codex 0.159.0 app-server skills/list in a fresh process discovered all 14 new IDs and no legacy IDs. Installed junction readback, frontmatter names, routes, and all active Markdown links passed. Both exported remote versions passed their existing checkers. Project and main-source chat paths in the app database read back as dreamweaver.

Remaining: the empty old source root is locked by a running Windows process and cannot yet be removed. The running desktop rewrote its legacy project JSON cache after a targeted update; its sidebar refresh remains unverified. The pre-existing local design-case index failure and unchanged historical image-record mismatch were retained. The generic quick validator lacks PyYAML; no dependency was installed. No image generation or behavioral prompt evaluation was performed.

Evidence: dreamweaver-rename-acceptance.json and dreamweaver-native-discovery.json. Archived before-state materials retain their historical names and bytes.

Follow-up: the user requested keeping the public repository and deleting the private repository. GitHub DELETE for PigeonAI-Yang/dreamweaver-private returned HTTP 403, "Must have admin rights to Repository", despite the earlier metadata showing admin=true. No retry, authentication change, or alternate deletion route was attempted. The online private repository remains. Local private remote and its LFS endpoint were removed; origin is the only remote and the default push and main tracking remote. Existing private commits remain reachable from local HEAD and no private content was published.

## Reference reconstruction workflow repair, 2026-09-30

Goal: make frame, main-limb geometry, garment construction, base color, transparency, and illumination explicit inspection steps before prompt writing. Adapt writing to each model and task using local official sources.

Evidence: the Primary described the supplied hosiery as nude and then pale gray-beige. The user confirmed highly sheer black hosiery and straight-kneed crossed legs. The generated comparison has bent knees. Existing general color and pose rules were read but were not applied sufficiently; material identity and joint states were not resolved before drafting. The earlier claim of fabric runs was not established by the reference.

Status: local workflow and model-writing assets updated. Main routing now requires the reconstruction workflow. The workflow checks frame and scale, each important limb and joint, garment construction, material identity, transparency and illuminated color, environment, light, and uncertain details before drafting. It defines portable writing order and a final source-to-prompt comparison. Camera and color methods include the confirmed failure mechanisms.

Official assets: two Krea hosted documentation sources and the two official Qwen prompt-enhancer system prompts were saved unchanged with provenance and hashes. Qwen's older documentation snapshots remain unchanged. Model adapters link to task-specific writing and distinguish enhancer contracts from image-model and active-entry capabilities.

Verification: changed-document links and six affected skill frontmatters passed. All four new source byte counts and hashes passed, and three older Qwen snapshots retained their recorded hashes. Changed skill documents and new official assets read back identically through the Codex junctions. The existing full checker still stops at the pre-existing design-template index failure. Its historical image hash gap was not re-investigated.

Behavioral evidence: the first fresh text-only worker used the wrong image path and returned without inspecting it. A fresh replacement opened the correct source and applied the installed workflow and both model adapters. Its prompts preserved highly sheer black hosiery and extended knees, but incorrectly described both forearms as resting on the railing. The Primary rejected that contact description, added an explicit hand-to-object tracing step, and personally integrated the actual skirt grip into the [corrected portable prompts](../prompt-cards/night-portrait-corrected.md). The final added contact instruction has not received another independent pass. The text-only check is limited evidence of instruction use, not proof of image fidelity.

Existing dirty work and historical images were preserved. No new image generation, active image-entry operation, language comparison, commit, push, or publication was performed. The updated sources are installed through existing junctions; a future image result remains unverified.


## Oneirloom rename and checker removal, 2026-09-30

Goal: use Oneirloom as the English name of the collection, including local source, skill IDs, installed entries, Git remotes, and GitHub repository. Remove the full skill checker at the user's explicit request.

Result: source is J:/PigeonYang/skills/oneirloom; the main invocation is $oneirloom and 13 method IDs use oneirloom-. All 14 installed junctions point to the renamed source. Native Codex skills/list in a fresh app-server process discovered exactly these 14 IDs and no Dreamweaver IDs. The public GitHub repository retains ID 1388440925 and is now PigeonAI-Yang/oneirloom. Public commits d54a6cef71f0e55679180276c75f06f6989fcb86 and 75b6f7a671a8a0bc8dc6b47d232657a6c26744d6 contain the rename and explicit checker removal. The public changes were made from the previous public version; existing private and uncommitted source content was not published.

The complete scripts/check_skills.py checker and documentation requiring it were removed locally and publicly. No full checker was run after that request. Before removal, file equivalence established preservation of all 377 source files, including the 39 original dirty entries; historical archives and image bytes were unchanged. The checker's pre-existing local failure was not repaired.

Project name and roots were updated through the native project/update entry and read back. Persisted chat working directories and Git origin metadata, trusted source path, and stored editor paths were migrated. The old source root is empty but remains locked by a running process. Current desktop sidebar refresh is unverified.

Evidence: oneirloom-rename-acceptance.json.
