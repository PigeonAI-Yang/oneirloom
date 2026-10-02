# Oneirloom (织梦师)

**Turn visual ideas into clear image prompts.**

Oneirloom is an open-source collection of 15 visual creation Agent Skills. It helps an AI assistant analyze reference images, write image prompts, plan product ads and character sheets, and revise prompts against generated results. Oneirloom provides creative methods and prompt instructions. It does not include an image-generation model or service.

[English project page](https://www.pigeonyang.top/en/skills/oneirloom/) · [Installation guide](https://www.pigeonyang.top/en/skills/oneirloom/install/) · [Safety guide](https://www.pigeonyang.top/en/skills/oneirloom/safety/) · [简体中文](README.md)

[Repository installation](docs/INSTALL.md) · [Host compatibility](docs/COMPATIBILITY.md) · [Safety and privacy](docs/SAFETY.md) · [Third-party notices](THIRD_PARTY_NOTICES.md) · [Submission guide](docs/SUBMISSION.md)

## Install in a Codex project

Copy all 15 sibling directories matching `skills/oneirloom*` into `.agents/skills/` at your Codex project root. Keep each directory intact, including its existing `SKILL.md` file and any `scripts/`, `references/`, `templates/`, or `assets/` folders.

Start a new chat and ask for Oneirloom or invoke `$oneirloom`. Uploading a ZIP to a regular chat does not install these skills. The host must support Agent Skills. Reference-image analysis also requires the host to pass images to the assistant.

Try: “Use Oneirloom to turn this visual idea into a complete image prompt.” Attach a reference for analysis, or provide a target and result image for diagnosis.

See the [installation guide](docs/INSTALL.md) and [host compatibility notes](docs/COMPATIBILITY.md) for other installation and runtime requirements.

## Install from the Codex marketplace

After this repository's marketplace is published, run:

~~~bash
codex plugin marketplace add PigeonAI-Yang/oneirloom --ref main
codex plugin add oneirloom@oneirloom-local
codex plugin list --marketplace oneirloom-local --json
~~~

These commands add and install this repository's marketplace. Publishing a repository marketplace does not mean that OpenAI has listed or approved Oneirloom in its official plugin directory. See the [installation guide](docs/INSTALL.md) for the steps and verification status.

## Skill collection

Oneirloom uses three layers: one main skill, reusable method skills, and indexed templates. The main skill routes a request and combines the selected methods. Concrete visual recipes live with their templates and evidence.

| Skill | Purpose |
| --- | --- |
| [oneirloom](skills/oneirloom/SKILL.md) | Main entry point, context handoff, routing, and complete delivery |
| [oneirloom-visual-analysis](skills/oneirloom-visual-analysis/SKILL.md) | Reference-image breakdown and visual relationships |
| [oneirloom-product-art-direction](skills/oneirloom-product-art-direction/SKILL.md) | Product-ad concepts and image stories |
| [oneirloom-camera-composition](skills/oneirloom-camera-composition/SKILL.md) | Framing, camera position, perspective, crop, and occlusion |
| [oneirloom-color-light](skills/oneirloom-color-light/SKILL.md) | Regional color, light direction, and material lighting |
| [oneirloom-character-sheet](skills/oneirloom-character-sheet/SKILL.md) | Character sheets, views, expressions, and clothing |
| [oneirloom-figure-art](skills/oneirloom-figure-art/SKILL.md) | Pose and occlusion for non-explicit adult figure art |
| [oneirloom-style-photography](skills/oneirloom-style-photography/SKILL.md) | Realistic photography, portraits, and cinematic images |
| [oneirloom-style-illustration](skills/oneirloom-style-illustration/SKILL.md) | Painting, print, collage, and narrative illustration |
| [oneirloom-style-design](skills/oneirloom-style-design/SKILL.md) | Posters, typography, packaging, products, and 3D images |
| [oneirloom-model-krea-2](skills/oneirloom-model-krea-2/SKILL.md) | Prompt and task adaptation for Krea 2 |
| [oneirloom-model-qwen-image-2-1](skills/oneirloom-model-qwen-image-2-1/SKILL.md) | Prompt and task adaptation for Qwen-Image-2.1 |
| [oneirloom-result-diagnosis](skills/oneirloom-result-diagnosis/SKILL.md) | Generation-result diagnosis and prompt revision |
| [oneirloom-image-tutorial](skills/oneirloom-image-tutorial/SKILL.md) | Writing and editing illustrated tutorials |
| [oneirloom-prompt-card](skills/oneirloom-prompt-card/SKILL.md) | A 3:4 share card with an existing image and complete prompt |

The [photography templates](skills/oneirloom-style-photography/templates/index.md), [character-sheet templates](skills/oneirloom-character-sheet/templates/index.md), [illustration templates](skills/oneirloom-style-illustration/templates/index.md), and [design templates](skills/oneirloom-style-design/templates/index.md) contain visual anchors, prompt scaffolds, image paths, and evidence.

Templates include crouching selfies, indoor full-length portraits, four-view plus four-expression cards, three-view cards, character wardrobe sheets, decorative rainy-night prints, halftone portrait cutouts, physical fuse-bead artworks, and portrait-to-blind-box comparison images.

A method directory may include its own template assets. A method skill works without a matching template. Skill lookup uses exact names. Markdown links do not invoke skills. See the [architecture](docs/architecture.md) for installation and ownership details.

## Examples and evidence

The [indoor full-length template](skills/oneirloom-style-photography/templates/indoor-full-length/template.md) contains an existing generated PNG and its exact submitted prompt and settings. The image was inspected during migration, with framing and foot-spacing limitations recorded. Its generalized scaffold has not been generated.

Other migrated templates distinguish missing image evidence from user-reported results. Adding an image path does not establish visual success.

The [character wardrobe sheet](skills/oneirloom-character-sheet/templates/wardrobe-sheet/template.md) contains an original illustrated reference, a user-provided realistic result, and the Chinese prompt delivered in the conversation. The result was inspected, with turnaround and costume-portrait deviations recorded. Its actual execution metadata is unknown, and its generalized scaffold has not been generated.

## Compatibility and optional rendering

A host must support Agent Skills to discover and invoke Oneirloom. Reference-image analysis also requires a host that can pass image inputs to the assistant. Image-generation availability, model behavior, and service fees depend on the tools you choose.

The optional prompt-card renderer turns an existing image and prompt into a 3:4 PNG. It requires local `Python`, `Pillow`, `Playwright`, and a Chromium-compatible browser. The host must permit local file execution. The repository does not bundle these runtime dependencies. The renderer does not generate images or require model or API credentials.

## Safety and privacy

Your host and selected image service process inputs under their own privacy terms. Before you upload a reference or result image, review those terms and confirm you have permission to share the material with that service. Review the image and its usage terms before publication. Publish only material that you have permission to share. Start paid generation only after you confirm the provider and cost.

Oneirloom provides methods and prompts. It does not include an image-generation model or service. Your selected host and provider control image processing, generation, and charges.

## Licenses

The MIT license covers project-owned skill instructions and code. It does not grant rights to third-party images or reference materials. The bundled official Qwen-Image-2.1 reference materials are identified in the package notice as governed by the Qwen Research License for non-commercial research and evaluation. Commercial use requires separate permission. Read [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) before reusing those materials.

## Further documentation

- [Installation guide](docs/INSTALL.md)
- [Host compatibility](docs/COMPATIBILITY.md)
- [Safety and privacy](docs/SAFETY.md)
- [Submission guide](docs/SUBMISSION.md)
- [Third-party notices](THIRD_PARTY_NOTICES.md)
- [Model evidence](docs/model-evidence.md)
- [Contributing guide](CONTRIBUTING.md)
