# 0.3.0-preview source implementation

## Goal and acceptance

Freeze the current local source state first, then implement the approved [visual-capability expansion plan](../../docs/visual-capability-expansion-plan.md) as a 0.3.0-preview outcome: source foundations, reviewed old-knowledge ownership and migration, and targeted source-guided text walkthroughs.

Acceptance evidence covers the recorded pre-change checkpoint; the 22-skill source tree with all 19 checkpoint entries retained; the approved visual routes and methods; byte-preserving migration of reviewed fuse-bead material; and ten actual local source-guided text cases exercising the planned routes and examples. The two exercise reports record the initial outputs, criteria, corrections, source reads, and limits.

The five visual cases initially met 4/5 case criteria; case 1 failed because its English prompt omitted the empty-street/no-people requirement. A manual, unblinded correction run corrected cases 1 and 2, carried cases 3–5 forward unchanged, and brought the visual result to 5/5 cases and 14/14 current criteria. Case 2 only had an unrequested English translation removed; its original criteria already passed. The five continuity cases (6–10) passed all 20 listed criteria. Overall, the current text criteria pass for 10/10 cases and 34/34 criteria. Initial responses and the case-1 failure remain preserved in the reports. The correction did not change source guidance. These source-guided text observations do not prove automatic routing or behavior in a fresh installed session.

This scope adds no fixed catalogue quota, full external-catalog migration gate, image-quality threshold, package build, or installation requirement. Image generation and inspection, installation, packaging, release, and publication remain outside this local-source and text-walkthrough outcome.

## Ownership and limits

- Baseline: branch codex/oneirloom-0.3.0-preview, commit 3c15c394b6feff57c7a2193f8d524e2475b90148, checkpoint tag checkpoint/pre-0.3.0-preview-20261010.
- Goal and final acceptance owner: /root. Primary accepted the local source and text-walkthrough outcome on 2026-10-11 after reviewing the actual changes and recorded responses.
- Completed source owners: /root/build_three_visual_methods_030, /root/add_owned_domain_knowledge_030, and /root/integrate_030_routes_and_migration.
- Completed text-evidence owners: /root/exercise_visual_routes_030, /root/exercise_continuity_routes_030, and /root/correct_text_exercise_delivery_030.
- Acceptance-record update owner: /root/finalize_030_acceptance_record (complete). No child assignment or next assessment remains running; /root retains final acceptance.
- Stop: no user Stop was received during this assignment.
- The pre-change local commit and tag were authorized only to freeze the checkpoint. All 0.3.0-preview changes remain uncommitted. No push, package build, installation, release, deployment, full test suite, network request, or image operation was performed for this source outcome.

## Source result

The local 0.3.0-preview source tree contains 22 skills: all 19 checkpoint entries plus craft construction, digital form, and space conception. It is a development source preview with no corresponding package and remains uninstalled. The frozen v0.2.0-preview.1 package and unchanged SOURCE-MANIFEST.json remain an 18-skill package. New method guidance is text only and does not establish image quality, native model files, engineering feasibility, or new-session behavior.

The main route sends physical construction, digital form, spatial layout, composed graphics, real products, and fashion styling to their respective owners. The family index is optional for formed scenes with open direction; clear watercolor and settled edits proceed directly. Family notes identify partial foundation coverage. The design template index points to craft construction for fuse-bead recipes.

The fuse-bead directory moved from skills/oneirloom-style-design/templates/fuse-bead/ to skills/oneirloom-craft-construction/templates/fuse-bead/. The current template adds one 550-byte mapping paragraph outside the prompts. The four migrated image-path files (two .png paths stored as Git LFS pointer files and two actual WebP files) and two migrated JSON records match their pre-move hashes. The appended evidence in the [migration record](migration-preservation-0.3.0-preview.json) records the pointer OIDs and declared payload sizes, stored-file hashes, and the fact that the PNG payloads were not hydrated or downloaded. These hashes establish preservation of the pointer files and WebP files, not verification of hydrated PNG payload bytes. Both original fuse-bead prompt blocks and both blind-box prompt blocks match their archived Base64 and SHA-256 exactly. Active relative image and input_image fields resolve after the move. Historical publication_encoding.image values remain in the byte-identical JSON records.

[docs/image-compression.json](../../docs/image-compression.json) is Git-clean and its CRLF-normalized working-tree SHA-256 matches the baseline Git blob. The raw worktree SHA differs because the checkout uses CRLF while the Git blob uses LF; no file edit is present.

## Verification

- quick_validate.py passed for all 17 changed or new SKILL directories in the source implementation.
- The recorded seven-document JSON parse passed for the plugin, marketplace, frozen manifest, image-compression record, moved records, and migration record.
- Local-path link closure passed for 43 changed/new Markdown files: 427 local paths and 0 missing targets. Anchors were not checked.
- The current source has 22 skill entries; all 19 checkpoint paths still exist. All ten family codes are present once.
- The plugin version is 0.3.0-preview; the marketplace label is oneirloom-0-3-0-preview / Oneirloom 0.3.0 Preview.
- The source exercise reports contain ten actual source-guided text cases: the corrected visual run passed 5/5 cases and the continuity run passed 5/5. The visual correction was manual and unblinded; the reports preserve the initial output and initial case-1 failure. No source instructions changed during correction.
- Current hashes match all 23 unique source instruction paths recorded by the exercise reports.
- The current branch is codex/oneirloom-0.3.0-preview at the checkpoint commit. The checkpoint tag still targets that commit, and the frozen v0.2.0-preview.1 tag object and target commit match the checkpoint receipt.
- All 90 excluded local files recorded in the checkpoint manifest exist with matching byte lengths and SHA-256: 86 ComfyUI outputs and four README badge PNGs.
- The SVG exercise record reports successful XML and source-contract checks. The SVG was not rendered or visually inspected.
- git -c core.autocrlf=false -c core.whitespace=cr-at-eol diff --check passed for the source implementation's then-checked paths. Current acceptance-record edits receive their own targeted checks.
- Full migration preservation measurements are in the [migration record](migration-preservation-0.3.0-preview.json). Actual responses and source reads are in the [visual exercise report](text-exercises-visual-0.3.0-preview.md) and [continuity exercise report](text-exercises-continuity-0.3.0-preview.md).

## Remaining evidence limits

No fresh installed session, automatic invocation route, image generation, or image-quality review was observed. The SVG has source-level XML and contract evidence but no render inspection. Installation, packaging, release, deployment, and publication remain unverified. Primary acceptance is complete for this local-source and text-walkthrough outcome. Further runtime or image evidence would be separate future work, not a new completion gate for this outcome.

## Publication preparation

On 2026-10-11, the user authorized updating the version record, cleaning current project and publication wording, and committing and pushing the source after review. At this preparation checkpoint, the candidate is staged for Primary review; no source commit or push has been made. The local pre-change checkpoint tag and commit remain intact. Remote readback is pending the later push; its receipt belongs at the ignored `.local-only/remote-push-0.3.0-preview.json`. Historical verification results above were not rewritten. The prepared version record is [0.3.0-preview source record](../../docs/releases/0.3.0-preview.md).
