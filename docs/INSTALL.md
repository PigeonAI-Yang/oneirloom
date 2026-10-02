# Install Oneirloom 0.1.1

The package contains 15 sibling skill folders with their references, templates, scripts, and assets. Keep each folder intact. Oneirloom prepares prompts; image generation requires a separately available model or tool.

## Codex CLI plugin installation

After this repository's marketplace is published, add and install it with the Codex CLI:

```sh
codex plugin marketplace add PigeonAI-Yang/oneirloom --ref main
codex plugin add oneirloom@oneirloom-local
codex plugin list --marketplace oneirloom-local --json
```

These instructions target the GitHub-hosted marketplace; that repository installation route still needs a direct check. The corrected local 0.1.1 candidate was installed and checked with Codex CLI 0.153.0: its ZIP contained 117 entries, all 25 raster images decoded, and all 117 ZIP, extracted-package, and installed-cache hashes and sizes matched. Eight Git LFS objects were hydrated, with no pointer files left in the package. `skills/list` discovered all 15 skills with zero candidate-specific errors. This verifies the corrected package through a local marketplace candidate, not the public repository route or OpenAI's plugin directory. See [compatibility](COMPATIBILITY.md) for the evidence and remaining limits. Refresh the host after installation, then ask: “Use Oneirloom to turn this visual idea into a complete image prompt.” Remove it with `codex plugin remove oneirloom@oneirloom-local`.

## Manual skill installation

In a Codex project, copy each folder inside `skills/` to `.agents/skills/<skill-folder>/` under the project root. Preserve folder names and all internal files. Review existing destinations and preserve local edits before merging. A generic chat window that only receives a ZIP does not install skills; use a host's supported plugin or skill installation flow.

## Compatibility and optional helpers

The main workflow uses Markdown skill instructions. Reference-image analysis requires a host that can pass images to the assistant. Krea 2 and Qwen-Image-2.1 provide prompt-writing guidance; image generation requires a separately chosen tool or service and may incur a fee.

The optional prompt-card renderer uses local Python, Pillow, Playwright, and a Chromium-compatible browser, with permission to read local inputs and write the output folder. These runtime dependencies are not bundled. A local renderer check passed; it used a synthetic image and did not generate an image with an AI model. See [compatibility](COMPATIBILITY.md) for versions and results.

## Version, license, and removal

Version 0.1.1 packages the 15-skill snapshot `8d195d4fc9404d5da71733c861fd947aa109d4f1`. The bundled Qwen-Image-2.1 reference materials have a separate Qwen Research License and required attribution; see [third-party notices](../THIRD_PARTY_NOTICES.md) before reuse. The OpenAI plugin-directory submission has not been made. See [safety and privacy](https://www.pigeonyang.top/skills/oneirloom/safety/) for data-handling guidance.

For a manual install, remove only the skill folders copied from this package, after preserving any edits. Do not delete an entire skills directory that contains unrelated skills.
