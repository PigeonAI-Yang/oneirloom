# Compatibility and verification status

<!-- project-metadata:current-status:start -->
## Current source and package status

The current `0.3.0-preview` source contains 22 skills and remains a development preview without a matching package.
The published frozen `0.2.0-preview.1` package contains 18 skills. See the [source record](https://github.com/PigeonAI-Yang/oneirloom/blob/main/docs/releases/0.3.0-preview.md) and [publication record](https://github.com/PigeonAI-Yang/oneirloom/blob/main/docs/releases/0.2.0-preview.1-publication.md).
The candidate table below preserves prepublication checks. Its pending items describe that earlier review, not current package availability.
<!-- project-metadata:current-status:end -->

## Historical 0.1.1 results

The table and website observations in this section describe the earlier 15-skill delivery. They do not verify 0.2.0-preview.1. The archived 0.1.1 packages contain private brand watermarks and are not public rollback downloads. The later 0.1.2 icon candidate was locally validated but was not installed or published.

| Surface or feature | Evidence and limits | Status |
| --- | --- | --- |
| Codex CLI plugin commands | Codex CLI 0.153.0 exposed marketplace, add, and list commands. Local package and published-source candidates were installed. The exact `PigeonAI-Yang/oneirloom --ref main` GitHub shorthand was not run. | Local routes passed; direct GitHub shorthand untested. |
| Corrected native Codex plugin install | The corrected local 0.1.1 candidate was installed and enabled. Its ZIP contained 117 entries; all 117 ZIP, extracted-package, and installed-cache hashes and sizes matched. Eight Git LFS objects were hydrated, with no pointer files in the ZIP, extracted package, or cache. All 25 source and installed-cache raster images decoded. | Passed on Codex CLI 0.153.0 for the corrected local marketplace candidate. |
| Published-source native install | A Git LFS clone of public commit `463e68f1a4965b7bedba68d2946b93cb743874bb` was copied into a local marketplace wrapper using `./plugin`. All 343 source files matched the installed cache byte for byte. All 25 package raster images decoded, and eight LFS payloads matched their object IDs and sizes. The test restored the existing 15 plugins and three marketplaces. | Passed on Codex CLI 0.153.0; the separate wrapper name preserved the existing installation. |
| Native skill discovery | `skills/list` returned all 15 Oneirloom skills at the exact installed cache paths with zero candidate-specific errors. The same runtime reported 15 unrelated global errors, which are not attributed to this candidate. | Passed for both corrected local and published-source candidates on Codex CLI 0.153.0. |
| Codex project skill copy | The documented project path is `.agents/skills/<skill-folder>/`, with all 15 sibling directories kept intact. A manual copy was not separately exercised. | Layout documented; manual copy untested. |
| ChatGPT desktop, web, and mobile | This package has not been installed or invoked on those surfaces. | Unverified. |
| Claude, Cursor, and other agents | A shared skill format does not establish each host's import path, discovery behavior, tools, or policy compatibility. | Unverified; do not infer support. |
| Reference-image analysis | Requires an agent host that accepts image input and can inspect it. | Host-dependent; no cross-host test. |
| Krea 2 and Qwen-Image-2.1 guidance | The adapters provide prompt-writing and task guidance. They include no model weights, service credentials, or generation service. | Prompt guidance only; no image-generation test or quality guarantee. |
| Optional prompt-card renderer | A synthetic local PNG rendered with Python 3.11.16, Pillow 12.3.0, Playwright 1.61.0, and Microsoft Edge in headless mode. The process exited 0 and produced a 2700×3600 PNG that was visually inspected. | Passed for this local sample; this is not an image-generation test. |

The homepage and privacy-policy destinations are [the English project page](https://www.pigeonyang.top/en/skills/oneirloom/) and [the English safety page](https://www.pigeonyang.top/en/skills/oneirloom/safety/). On 2026-10-02, live checks passed for all six Chinese and English product, installation, and safety pages, plus the gallery homepage. Browser checks covered widths of 1440, 390, and 360 pixels. Mobile checks used Edge emulation, not a physical phone. The published website commit is `452535448e43c9f4efc2a3b4f0cdc261fd62b80f`.

The final 0.1.1 documentation update changed only status documents and their source-manifest hashes. That package retained 117 entries. All skill files, scripts, plugin manifests, icons, and images remained byte-identical to its previously tested package, so the historical native installation evidence remained applicable to those files. This statement does not apply to the 0.2.0-preview.1 candidate. No additional installation or image-generation test was claimed for that documentation update.

The package has not been submitted to or approved by the OpenAI plugin directory.

## 0.2.0-preview.1 prepublication evidence

This section records the 18-skill package before publication. At that point, the separate versioned package was still pending publication. The package is now published; see the [publication record](releases/0.2.0-preview.1-publication.md), [installation guide](INSTALL.md), and [release notes](releases/0.2.0-preview.1.md). The candidate started from base commit `f8059e1a8b512d3af0302f4212521a82cade964c` plus working-tree changes. The bundled `SOURCE-MANIFEST.json` must identify the actual source snapshot; the base commit alone is insufficient.

| Check | Available evidence and limits | Candidate status |
| --- | --- | --- |
| Prompt-delivery behavior | Latest scoped closure coverage combines 12 passing C1 cases with one corrected C2 rerun. The first C1 batch had one failure among 13 cases. The other 12 cases were not rerun on C2. These native-child receipts record source reads, not installed-skill discovery. | Historical source-level evidence; no full current-candidate rerun claimed. |
| Execution model attribution | The closure receipts requested `gpt-6-luna` at `max`. The server response model was not observed. | Requested model known; actual server model unknown. |
| ZIP inventory, hashes, and private-asset exclusion | The proposed ZIP requires 18 skills, schema-version-2 source provenance, actual image payloads, and no private mascot, logo, or standalone watermark assets. Eight known LFS objects need hydration during preparation. | Fresh candidate package checks pending. |
| New-project skill installation | Planned checks copy the packaged skills into an empty project's `.agents/skills/`, disable plugins and old global skill paths for the test, and audit actual reads. This is isolation inside the existing user environment, not a clean operating-system test. | Pending. |
| Native Codex plugin installation | The proposed isolated marketplace is `oneirloom-0-2-0-preview-1` with source `./`. The existing `oneirloom-local` installation is separate. | Pending; historical 0.1.1 installation is not evidence for this candidate. |
| Prompt cards | Public cards default to no watermark. An authorized local PNG can be supplied through `--watermark`. Fixed image and prompt regions remain one third and two thirds. | Fresh unbranded and supplied-watermark renderer checks pending. |
| Image generation and visual quality | No generated-image outcome is established by prompt checks, packaging, skill discovery, or local card rendering. | No new generation or pixel-level quality proof. |
| Other hosts | Historical ChatGPT, Claude, Cursor, and other-host limits remain unchanged. | Unverified. |

Fresh results must name the exact package hash and tested source snapshot before replacing a pending status. Keep unexecuted checks and unknown runtime fields explicit. Candidate preparation does not establish release approval, publication, repeatability, or OpenAI directory acceptance.
