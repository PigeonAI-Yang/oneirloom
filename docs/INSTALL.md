# Install Oneirloom 0.1.1

The package contains 15 sibling skill folders with their references, templates, scripts, and assets. Keep each folder intact. Oneirloom prepares prompts; image generation requires a separately available model or tool.

## Codex CLI plugin installation

The repository marketplace is public. These GitHub shorthand commands are documented but have not been directly tested:

```sh
codex plugin marketplace add PigeonAI-Yang/oneirloom --ref main
codex plugin add oneirloom@oneirloom-local
codex plugin list --marketplace oneirloom-local --json
```

Codex CLI 0.153.0 installed and enabled both the corrected local package and a complete clone of the published repository through a local marketplace wrapper. The public-clone test matched all 343 source files to the installed cache, decoded all 25 package raster images, verified eight LFS payloads, and discovered all 15 skills with zero candidate-specific errors. It used a separate test marketplace name to preserve existing installations. The GitHub shorthand above remains untested. See [compatibility](COMPATIBILITY.md) for the scope of these checks.

If `oneirloom-local` already exists, inspect its source before adding this marketplace. Preserve the existing installation and local edits. Refresh the host after installation, then ask: "Use Oneirloom to turn this visual idea into a complete image prompt." Remove this plugin with `codex plugin remove oneirloom@oneirloom-local` only when that is the installation you intend to remove.

## Fetch the complete source

For a manual install or a local marketplace, install Git LFS, then fetch the image payloads:

```sh
git lfs install
git clone https://github.com/PigeonAI-Yang/oneirloom.git
cd oneirloom
git lfs pull
git lfs fsck
git lfs ls-files
```

Check that `git lfs fsck` passes. In `git lfs ls-files`, `*` marks a complete working-tree payload and `-` marks a pointer. The published-source check hydrated and verified eight objects. Do not copy pointer files as images. GitHub-generated source ZIPs may contain pointers; use a Git LFS clone or the publisher-built `oneirloom-0.1.1.zip`, whose 25 raster images have been decoded and checked.

To use the cloned repository as a local marketplace, replace the example path with its absolute location:

```sh
codex plugin marketplace add /absolute/path/to/oneirloom
codex plugin add oneirloom@oneirloom-local
codex plugin list --marketplace oneirloom-local --json
```

The repository declares the marketplace name `oneirloom-local`. Its local plugin source is `./`, within the marketplace root. The verified public-clone test copied the full repository into a separate wrapper with source `./plugin`; it did not exercise the GitHub shorthand or change an existing `oneirloom-local` installation.

## Manual skill installation

In a Codex project, copy each folder inside `skills/` to `.agents/skills/<skill-folder>/` under the project root. Preserve folder names and all internal files. Review existing destinations and preserve local edits before merging. A generic chat window that only receives a ZIP does not install skills; use a host's supported plugin or skill installation flow.

## Compatibility and optional helpers

The main workflow uses Markdown skill instructions. Reference-image analysis requires a host that can pass images to the assistant. Krea 2 and Qwen-Image-2.1 provide prompt-writing guidance; image generation requires a separately chosen tool or service and may incur a fee.

The optional prompt-card renderer uses local Python, Pillow, Playwright, and a Chromium-compatible browser, with permission to read local inputs and write the output folder. These runtime dependencies are not bundled. A local renderer check passed; it used a synthetic image and did not generate an image with an AI model. See [compatibility](COMPATIBILITY.md) for versions and results.

## Version, license, and removal

Version 0.1.1 packages the 15-skill snapshot `8d195d4fc9404d5da71733c861fd947aa109d4f1`. The bundled Qwen-Image-2.1 reference materials have a separate Qwen Research License and required attribution; see [third-party notices](../THIRD_PARTY_NOTICES.md) before reuse. The OpenAI plugin-directory submission has not been made. See [safety and privacy](https://www.pigeonyang.top/skills/oneirloom/safety/) for data-handling guidance.

For a manual install, remove only the skill folders copied from this package, after preserving any edits. Do not delete an entire skills directory that contains unrelated skills.
