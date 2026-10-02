# Compatibility and verification status

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

The final documentation update changes only status documents and their source-manifest hashes. The package retains 117 entries. All skill files, scripts, plugin manifests, icons, and images remain byte-identical to the previously tested package, so the native installation evidence remains applicable to those files. No additional installation or image-generation test is claimed.

The package has not been submitted to or approved by the OpenAI plugin directory.
