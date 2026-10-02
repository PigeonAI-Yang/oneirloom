# Compatibility and verification status

| Surface or feature | Evidence and limits | Status |
| --- | --- | --- |
| Codex CLI plugin commands | Codex CLI 0.153.0 exposed marketplace, add, and list commands. A local marketplace candidate was added and installed. The GitHub repository commands in the installation guide remain to be checked after marketplace publication. | Local CLI and candidate path checked; published repository route pending. |
| Corrected native Codex plugin install | The corrected local 0.1.1 candidate was installed and enabled. Its ZIP contained 117 entries; all 117 ZIP, extracted-package, and installed-cache hashes and sizes matched. Eight Git LFS objects were hydrated, with no pointer files in the ZIP, extracted package, or cache. All 25 source and installed-cache raster images decoded. | Passed on Codex CLI 0.153.0 for the local marketplace candidate; the GitHub repository install route remains unchecked. |
| Native skill discovery | `skills/list` returned all 15 Oneirloom skills at the exact installed cache paths with zero candidate-specific errors. The same runtime reported 15 unrelated global errors, which are not attributed to this candidate. | Passed for the corrected candidate on Codex CLI 0.153.0. |
| Codex project skill copy | The documented project path is `.agents/skills/<skill-folder>/`, with all 15 sibling directories kept intact. A manual copy was not separately exercised. | Layout documented; manual copy untested. |
| ChatGPT desktop, web, and mobile | This package has not been installed or invoked on those surfaces. | Unverified. |
| Claude, Cursor, and other agents | A shared skill format does not establish each host's import path, discovery behavior, tools, or policy compatibility. | Unverified; do not infer support. |
| Reference-image analysis | Requires an agent host that accepts image input and can inspect it. | Host-dependent; no cross-host test. |
| Krea 2 and Qwen-Image-2.1 guidance | The adapters provide prompt-writing and task guidance. They include no model weights, service credentials, or generation service. | Prompt guidance only; no image-generation test or quality guarantee. |
| Optional prompt-card renderer | A synthetic local PNG rendered with Python 3.11.16, Pillow 12.3.0, Playwright 1.61.0, and Microsoft Edge in headless mode. The process exited 0 and produced a 2700×3600 PNG that was visually inspected. | Passed for this local sample; this is not an image-generation test. |

The homepage and privacy-policy destinations are `https://www.pigeonyang.top/en/skills/oneirloom/` and `https://www.pigeonyang.top/en/skills/oneirloom/safety/`. Their live reachability and content have not been verified. The package has not been submitted to or approved by the OpenAI plugin directory.
