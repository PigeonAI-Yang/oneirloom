<!-- project-metadata:package-title:start -->
# Install Oneirloom 0.2.0-preview.1
<!-- project-metadata:package-title:end -->

<!-- project-metadata:current-package-status:start -->
This guide installs the published frozen package `0.2.0-preview.1`, which contains 18 sibling skills.
The current `0.3.0-preview` source contains 22 skills and remains a development preview with no matching package.
See the [source record](https://github.com/PigeonAI-Yang/oneirloom/blob/main/docs/releases/0.3.0-preview.md) and the [frozen-package publication record](https://github.com/PigeonAI-Yang/oneirloom/blob/main/docs/releases/0.2.0-preview.1-publication.md).
<!-- project-metadata:current-package-status:end -->

<!-- project-metadata:package-obtain:start -->
## Obtain and check the frozen package

Download the publisher-built [oneirloom-0.2.0-preview.1.zip](https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.2.0-preview.1/oneirloom-0.2.0-preview.1.zip) and its [SHA256SUMS.txt](https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.2.0-preview.1/SHA256SUMS.txt).
Compare the downloaded ZIP with its exact filename in the checksum file before extraction.
<!-- project-metadata:package-obtain:end -->

<!-- project-metadata:package-hash-command:start -->
1. Compare the ZIP's SHA-256 with the exact filename in `SHA256SUMS.txt`. In PowerShell, run `Get-FileHash -Algorithm SHA256 -LiteralPath './oneirloom-0.2.0-preview.1.zip'` in the download directory.
<!-- project-metadata:package-hash-command:end -->
2. Extract the ZIP into a new directory. Find the package root containing `skills/` and `SOURCE-MANIFEST.json`.
<!-- project-metadata:manifest-count:start -->
3. Check that the manifest records package version `0.2.0-preview.1` and the 18 skill IDs listed below. Keep the ZIP, `SHA256SUMS.txt`, and manifest together with your installation record.
<!-- project-metadata:manifest-count:end -->

The manifest uses schema version 2. It records the package name and version, `skillIds`, hashes and sizes in `packagedFilesExceptThisManifest`, and `sourceSnapshot` provenance. The snapshot includes the base commit, dirty working-tree state, skill-content fingerprint, and LFS payload provenance. The ZIP checksum covers the manifest too. A base commit alone does not identify this candidate's uncommitted source content.

Use the built ZIP rather than GitHub's automatically generated source ZIP. The development checkout has eight known Git LFS pointers that require hydration before packaging. A release payload must contain the actual image bytes. Do not install pointer text as an image or treat a source archive as the checked release package.

## Install in a new Codex project

<!-- project-metadata:install-copy:start -->
Start with an empty project so existing skills do not need to be overwritten. Copy all 18 directories inside the package's `skills/` into the project's `.agents/skills/`, retaining every directory name and its internal files. Do not put the collection inside one extra `oneirloom/` directory.
<!-- project-metadata:install-copy:end -->

The candidate's skill IDs are:

```text
oneirloom
oneirloom-brand-identity
oneirloom-camera-composition
oneirloom-character-sheet
oneirloom-color-light
oneirloom-expression-stickers
oneirloom-figure-art
oneirloom-icon-design
oneirloom-image-tutorial
oneirloom-model-krea-2
oneirloom-model-qwen-image-2-1
oneirloom-product-art-direction
oneirloom-prompt-card
oneirloom-result-diagnosis
oneirloom-style-design
oneirloom-style-illustration
oneirloom-style-photography
oneirloom-visual-analysis
```

Open a new chat in that project and check that the host discovers these skills from the project path. Invoke `$oneirloom` with a real request, or name a method directly. Confirm that the assistant reads the candidate's skill and shared interaction contract. An already open chat may retain older instructions. A global skill or plugin with the same ID can also obscure which copy ran, so record the actual paths used.

Uploading the ZIP to an ordinary chat does not install skills. Hosts other than Codex require their own supported installation path; compatibility has not been established for them.

## Optionally register an isolated Codex marketplace

Use this route only with a host that exposes the relevant plugin commands. Inspect the extracted `.agents/plugins/marketplace.json` first. The candidate marketplace must be named `oneirloom-0-2-0-preview-1`, with the plugin source `./` inside that marketplace root. Keep an existing `oneirloom-local` registration and its installed copy unchanged.

Replace the example with the absolute extracted package root:

```sh
codex plugin marketplace add /absolute/path/to/extracted-package
codex plugin add oneirloom@oneirloom-0-2-0-preview-1
codex plugin list --marketplace oneirloom-0-2-0-preview-1 --json
```

This candidate's native plugin installation is pending verification. The older 0.1.1 local-marketplace result does not prove these commands install the new package. Confirm the installed version and file hashes, then use a new chat to check discovery and invocation. Do not register `main` as a substitute for this versioned candidate.

## Preserve a rollback before upgrading

Before replacing an existing installation, back up its exact Oneirloom directories, local edits, manifest, and known working package. Record the package hash, installed file hashes, version, and successful invocation. If no verified backup or package exists, record **rollback baseline absent**. There is no supplied, publicly redistributable, verified rollback package: historical 0.1.1 archives contain private watermark assets and must not be republished.

Compare the candidate's explicit `skillIds` with the previous installation's inventory. Replace only the Oneirloom directories owned by that installation. Preserve unrelated skills and edits of unknown origin. Do not use a wildcard to delete every `oneirloom*` directory, and do not delete `.agents/skills/` itself.

To revert, remove only the candidate-owned directories identified by its inventory, after preserving edits made since installation. Restore the exact previous backup or verified package. Restore the previous inventory as a unit: a known 15-skill installation must not retain the three candidate-only methods. Do not assume an arbitrary older tag is a tested rollback. If you used the isolated marketplace, remove only `oneirloom@oneirloom-0-2-0-preview-1` when that is the intended candidate, leaving other registrations intact. Refresh the host in a new chat and repeat the previously successful request.

## Use optional tools

The core collection is Markdown. It requires no Go runtime, model weights, service credentials, or bundled generation server. Image analysis requires a host that can inspect images. Image generation uses a separately available tool or service and may incur a fee. Model instructions do not establish active-entry support; see [model evidence](model-evidence.md).

The optional prompt-card renderer requires local Python, Pillow, Playwright, and a Chromium-compatible browser, plus access to its input and output paths. These dependencies are not bundled. Cards are unbranded by default. An explicitly supplied, authorized local PNG can be passed with `--watermark`; no private brand asset is required or included. See the [prompt-card skill](../skills/oneirloom-prompt-card/SKILL.md).

## Historical installation evidence and license

The 0.1.1 package had 15 skills from snapshot `8d195d4fc9404d5da71733c861fd947aa109d4f1`. Codex CLI 0.153.0 installed the corrected local package and a complete public clone through separate local marketplace wrappers. The published-clone check matched 343 files, decoded 25 raster images, verified eight LFS payloads, and discovered all 15 skills. The exact GitHub shorthand `PigeonAI-Yang/oneirloom --ref main` was not tested. These are historical observations, not current candidate results or a stable rollback promise. Full limits remain in [compatibility](COMPATIBILITY.md).

Read the [MIT license](../LICENSE), [third-party notices](../THIRD_PARTY_NOTICES.md), and [safety and privacy guidance](SAFETY.md). Bundled Qwen-Image-2.1 references retain their separate Qwen Research License and attribution requirements. This candidate has not been submitted to or approved by the OpenAI plugin directory.
