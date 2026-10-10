<div align="center">

<h1>Oneirloom · 织梦师</h1>

<p><strong>Turn imagination into images.</strong></p>

<!-- project-metadata:source-summary:start -->
<p>An open-source collection of 22 free visual creation skills. Work with your AI assistant to explore ideas, analyze references, design images, and refine the results—from product visuals, photography and illustration to characters, branding, crafts, digital art, and spatial concepts.</p>
<!-- project-metadata:source-summary:end -->

<!-- project-metadata:package-badge:start -->
<p align="center"><a href="https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.2.0-preview.1/oneirloom-0.2.0-preview.1.zip">Download skills (18 skills)</a> · <a href="https://github.com/PigeonAI-Yang/oneirloom/releases/tag/v0.2.0-preview.1">Release notes</a></p>
<!-- project-metadata:package-badge:end -->

<p>
  <a href="https://github.com/PigeonAI-Yang/oneirloom/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/PigeonAI-Yang/oneirloom?style=flat-square&amp;logo=github" /></a>
  <a href="https://github.com/PigeonAI-Yang/oneirloom/forks"><img alt="GitHub forks" src="https://img.shields.io/github/forks/PigeonAI-Yang/oneirloom?style=flat-square&amp;logo=github" /></a>
  <a href="https://github.com/PigeonAI-Yang/oneirloom/watchers"><img alt="GitHub watchers" src="https://img.shields.io/github/watchers/PigeonAI-Yang/oneirloom?style=flat-square&amp;logo=github" /></a>
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" /></a>
</p>

<p>
  <a href="https://www.pigeonyang.top/en/skills/oneirloom/"><img alt="Website" src="https://img.shields.io/badge/Website-Oneirloom-7c3aed?style=flat-square" /></a>
  <a href="#example-evidence"><img alt="Examples" src="https://img.shields.io/badge/Examples-Browse-f59e0b?style=flat-square" /></a>
  <a href="https://github.com/PigeonAI-Yang/oneirloom/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/PigeonAI-Yang/oneirloom?style=flat-square&amp;logo=github" /></a>
  <a href="https://github.com/PigeonAI-Yang"><img alt="GitHub followers" src="https://img.shields.io/github/followers/PigeonAI-Yang?style=flat-square&amp;logo=github&amp;label=Follow%20author" /></a>
  <a href="https://x.com/KimbomArtist"><img alt="X KimbomArtist" src="https://img.shields.io/badge/X-KimbomArtist-000000?style=flat-square&amp;logo=x&amp;logoColor=white" /></a>
  <a href="https://www.xiaohongshu.com/user/profile/689af6b90000000019016082"><img alt="Xiaohongshu Dibo" src="https://img.shields.io/badge/%E5%B0%8F%E7%BA%A2%E4%B9%A6-Dibo-ff2442?style=flat-square&amp;logo=xiaohongshu&amp;logoColor=white" /></a>
</p>

<p>
  <a href="#use">Use</a> · <a href="#example-evidence">Examples</a> · <a href="#three-layers">Skills</a> · <a href="README.md">中文</a> | <a href="README.en.md">English</a> · <a href="https://www.pigeonyang.top/en/skills/oneirloom/">Website</a>
</p>
</div>

<p align="center">
  <a href="docs/assets/product-page/01-hero-oneirloom-v4.webp"><img src="docs/assets/product-page/01-hero-oneirloom-v4.webp" alt="Oneirloom hero image featuring Dream Cocoon, portraits, a folklore illustration, and product advertising." /></a>
</p>

Oneirloom is the public name of this collection, also called "织梦师", "织梦师Skill", or "Oneirloom Skill". The main technical skill ID is `oneirloom`; method IDs use the `oneirloom-` prefix.

Turn visual requests, references, and generation misses into complete image prompts, or develop illustrated image-generation tutorials.

The collection uses three layers: **one main skill, reusable method skills, and indexed templates**. Concrete recipes live with their prompts and example records instead of becoming separate skills. See the skill directory below for the available entries.

<!-- project-metadata:guidance-heading:start -->
## Guidance in the frozen 0.2.0-preview.1 package
<!-- project-metadata:guidance-heading:end -->

- For a clear brief, work within the constraints you provide. For an open brief, inspect the references and available material, ask only necessary questions, then offer two or three reasoned directions.
- For product campaigns, preserve confirmed facts and make no claims about unknown ingredients. A fantasy concept can change the product's scale or surroundings without inventing product facts.
- For local revisions, keep the other confirmed requirements. When you provide a real result image, use visible deviations to write a complete, specific revision prompt. Without a result image, do not claim the result was inspected.

<!-- project-metadata:guidance-current-status:start -->
These instructions belong to the frozen 0.2.0-preview.1 package. The 0.3.0-preview source remains a development preview with no corresponding package; its new-session behavior and generated image quality have not been verified. See the dated [0.2.0-preview.1 publication record](docs/releases/0.2.0-preview.1-publication.md) for its account checks.
<!-- project-metadata:guidance-current-status:end -->

## Use the frozen package

<!-- project-metadata:install-intro:start -->
The frozen `0.2.0-preview.1` package has **18 free skills** and does not contain the 0.3.0-preview source changes. Download the publisher-built ZIP from the [fixed package URL](https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.2.0-preview.1/oneirloom-0.2.0-preview.1.zip) and verify it with [SHA256SUMS.txt](https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.2.0-preview.1/SHA256SUMS.txt). Do not use GitHub's generated source archive as the inspected installation package. See [installation and rollback](docs/INSTALL.md), [frozen-package publication status](docs/releases/0.2.0-preview.1-publication.md), and [prepublication compatibility and verification records](docs/COMPATIBILITY.md).
<!-- project-metadata:install-intro:end -->

The `main` branch is for development. Use a confirmed versioned package for installation; contributors need Git LFS to fetch the complete source images. The core skills require no Go runtime or local image model. Generation tools and optional card-rendering dependencies are separate. Public prompt cards are unbranded by default; an authorized local watermark is optional.

<!-- project-metadata:install-copy:start -->
1. Follow the installation guide to copy all 18 directories in the frozen package under `skills/` as siblings into a new project's `.agents/skills/`. Preserve the exact prior installation and package hash before an upgrade.
<!-- project-metadata:install-copy:end -->
2. Ask for Oneirloom, "织梦师", or "织梦师Skill"; explicitly invoke `$oneirloom` when using the technical ID. Method skills remain available directly.
3. Give the requested image or tutorial goal and any model, reference, or result already available. Confirmed conversation settings are inherited.
4. The main skill selects methods. A method reads its template index only when a concrete recipe helps, then loads a matching template. Without a match, it composes from its reusable method.

For standalone image prompts, the default output is a complete Chinese prompt followed by an equivalent English prompt, with one pair per explicitly requested model. An explicit single-language request overrides this default. Parameters and reference-image inputs remain outside prompt text.

For tutorials, invoke `oneirloom-image-tutorial` or ask the main skill to write, expand, or polish an illustrated lesson. The requested article language and author voice govern the deliverable. Prose-only revisions reuse existing evidence.

## Three layers

| Layer | Contents |
| --- | --- |
| Main | [Oneirloom](skills/oneirloom/SKILL.md): context, routing, integration, output contract |
<!-- project-metadata:methods-summary:start -->
| Methods | Dream weaving; Visual analysis; Product art direction; Camera and composition; Color and light; Character sheets; Expression stickers; Icon design; Brand identity; Artistic figure; Photography; Illustration; Graphic design; Craft construction; Digital form; Space conception; Krea 2 adapter; Qwen-Image-2.1 adapter; Result diagnosis; Image tutorials; Prompt cards |
<!-- project-metadata:methods-summary:end -->
| Templates | [Photography](skills/oneirloom-style-photography/templates/index.md), [character sheets](skills/oneirloom-character-sheet/templates/index.md), [illustration](skills/oneirloom-style-illustration/templates/index.md), [design](skills/oneirloom-style-design/templates/index.md), and [craft construction](skills/oneirloom-craft-construction/templates/index.md): selection, visual anchors, slots, prompt scaffolds, image paths and evidence |

<!-- project-metadata:skill-directory:start -->
## Skill directory

This table lists all 22 skills in the `0.3.0-preview` source tree.

| Skill | Purpose |
| --- | --- |
| [oneirloom](skills/oneirloom/SKILL.md) | Request routing, conversation context, and complete delivery. |
| [oneirloom-dream-weaving](skills/oneirloom-dream-weaving/SKILL.md) | Develop feelings, memories, and fragments into a drawable scene. |
| [oneirloom-visual-analysis](skills/oneirloom-visual-analysis/SKILL.md) | Reference-image analysis and visual relationships. |
| [oneirloom-product-art-direction](skills/oneirloom-product-art-direction/SKILL.md) | Product-ad concepts and visual storytelling. |
| [oneirloom-camera-composition](skills/oneirloom-camera-composition/SKILL.md) | Shot size, camera position, perspective, crops, and occlusion. |
| [oneirloom-color-light](skills/oneirloom-color-light/SKILL.md) | Color regions, light direction, and material response. |
| [oneirloom-character-sheet](skills/oneirloom-character-sheet/SKILL.md) | Character, multi-view, expression, and wardrobe sheets. |
| [oneirloom-expression-stickers](skills/oneirloom-expression-stickers/SKILL.md) | Sticker reactions, consistent characters, and individual sticker files. |
| [oneirloom-icon-design](skills/oneirloom-icon-design/SKILL.md) | UI icon families, app symbols, and native vector assets. |
| [oneirloom-brand-identity](skills/oneirloom-brand-identity/SKILL.md) | VI foundations, applications, guidelines, and asset handoff. |
| [oneirloom-figure-art](skills/oneirloom-figure-art/SKILL.md) | Poses and coverage for non-explicit adult figure art. |
| [oneirloom-style-photography](skills/oneirloom-style-photography/SKILL.md) | Realistic photography, lifestyle portraits, and film-still imagery. |
| [oneirloom-style-illustration](skills/oneirloom-style-illustration/SKILL.md) | Painting, print, collage, and narrative illustration. |
| [oneirloom-style-design](skills/oneirloom-style-design/SKILL.md) | Posters, typography, ads, and packaging graphics. |
| [oneirloom-craft-construction](skills/oneirloom-craft-construction/SKILL.md) | Units, joins, layers, and supports in crafts such as fuse beads. |
| [oneirloom-digital-form](skills/oneirloom-digital-form/SKILL.md) | Digital volume, deformation, connections, and visual transformation. |
| [oneirloom-space-conception](skills/oneirloom-space-conception/SKILL.md) | Spatial relations for rooms, sets, and environments. |
| [oneirloom-model-krea-2](skills/oneirloom-model-krea-2/SKILL.md) | Krea 2 prompts and entry-point adaptation. |
| [oneirloom-model-qwen-image-2-1](skills/oneirloom-model-qwen-image-2-1/SKILL.md) | Qwen-Image-2.1 prompts and task adaptation. |
| [oneirloom-result-diagnosis](skills/oneirloom-result-diagnosis/SKILL.md) | Analyze generation misses and revise prompts. |
| [oneirloom-image-tutorial](skills/oneirloom-image-tutorial/SKILL.md) | Write, expand, and polish illustrated tutorials. |
| [oneirloom-prompt-card](skills/oneirloom-prompt-card/SKILL.md) | 3:4 share cards for images and complete prompts. |
<!-- project-metadata:skill-directory:end -->

Templates include crouching selfies, indoor full-length portraits, four-view plus four-expression cards, three-view cards, character wardrobe sheets, decorative rainy-night prints, halftone portrait cutouts, physical fuse-bead artworks, and portrait-to-blind-box comparison images.

A method directory includes its own template assets. Method skills remain usable without a matching template. Skill lookup uses exact names; Markdown links do not automatically invoke skills. For installation and ownership details, see the [architecture](docs/architecture.md).

## Specialist design methods

| Method | Scope | Templates |
| --- | --- | --- |
| [oneirloom-expression-stickers](skills/oneirloom-expression-stickers/SKILL.md) | Reaction intent, consistent character identity, and individual sticker delivery | [Head reactions, action gestures, caption reactions](skills/oneirloom-expression-stickers/templates/index.md) |
| [oneirloom-icon-design](skills/oneirloom-icon-design/SKILL.md) | UI icon families, app symbols, and native vector assets | [Outline UI, solid UI, app symbol](skills/oneirloom-icon-design/templates/index.md) |
| [oneirloom-brand-identity](skills/oneirloom-brand-identity/SKILL.md) | Coherent VI foundations, applications, guidelines, and asset handoff | [Wordmark, mascot, editorial systems](skills/oneirloom-brand-identity/templates/index.md) |

These three specialist methods reuse the graphic-design process within the existing layers. They contain nine researched starter templates, not nine templates in total. The expression-sticker method also has 14 extension templates, and its offline browser check passed. The nine starter templates have no matching generated examples. New character/VI image generation and complete VI production remain unaccepted. A requested SVG, asset set, or VI guideline uses its artifact contract; prompt-only work retains complete bilingual prompts. A contact sheet or brand board does not establish complete asset delivery.

## Example evidence

The [indoor full-length template](skills/oneirloom-style-photography/templates/indoor-full-length/template.md) contains an existing generated PNG and its exact submitted prompt and settings. The image was inspected during migration, with framing and foot-spacing limitations recorded. Its generalized scaffold has not been generated.

Other migrated templates explicitly distinguish missing image evidence from user-reported results. Adding an image path does not itself establish visual success.

The [character wardrobe sheet](skills/oneirloom-character-sheet/templates/wardrobe-sheet/template.md) contains an original illustrated reference, a user-provided realistic result, and the Chinese prompt delivered in the conversation. The result was inspected with turnaround and costume-portrait deviations. Its actual execution metadata is unknown, and the generalized scaffold has not been generated.

## Maintenance

Read [CONTRIBUTING.md](CONTRIBUTING.md) for adding templates and examples, and [model evidence](docs/model-evidence.md) for model-specific claims. This repository uses the MIT license; model and service terms remain separate.
