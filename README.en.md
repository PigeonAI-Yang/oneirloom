<div align="center">

<h1>Oneirloom · 织梦师</h1>

<p><strong>Turn imagination into images.</strong></p>

<p>The source tree contains 22 visual-creation Agent Skills: the 19 existing entries plus methods for craft construction, digital form, and space conception. Craft construction owns the fuse-bead recipe. The 0.3.0-preview source is a development preview with no corresponding package; the released package remains frozen at 0.2.0-preview.1 with 18 skills. <a href="docs/releases/0.3.0-preview.md">Read the source record</a>.</p>

<p align="center"><a href="https://github.com/PigeonAI-Yang/oneirloom/releases/tag/v0.2.0-preview.1">Frozen released version: 0.2.0-preview.1 (18 skills)</a> · <a href="https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.2.0-preview.1/oneirloom-0.2.0-preview.1.zip">Download the frozen package (18 skills)</a></p>

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

The collection uses three layers: **one main skill, reusable method skills, and indexed templates**. Concrete recipes live with their prompts and example records instead of becoming separate skills. The directory below lists all 22 skills in the 0.3.0-preview source tree.

## Guidance in the frozen 0.2.0-preview.1 package

- For a clear brief, work within the constraints you provide. For an open brief, inspect the references and available material, ask only necessary questions, then offer two or three reasoned directions.
- For product campaigns, preserve confirmed facts and make no claims about unknown ingredients. A fantasy concept can change the product's scale or surroundings without inventing product facts.
- For local revisions, keep the other confirmed requirements. When you provide a real result image, use visible deviations to write a complete, specific revision prompt. Without a result image, do not claim the result was inspected.

These instructions belong to the frozen 0.2.0-preview.1 package. The 0.3.0-preview source remains a development preview with no corresponding package; its new-session behavior and generated image quality have not been verified. See the dated [0.2.0 publication record](docs/releases/0.2.0-preview.1-publication.md) for its account checks.

## Use the frozen package

The frozen `0.2.0-preview.1` package has **18 free skills** and does not contain the 0.3.0-preview source changes. Download the publisher-built ZIP from the [fixed package URL](https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.2.0-preview.1/oneirloom-0.2.0-preview.1.zip) and verify it with [SHA256SUMS.txt](https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.2.0-preview.1/SHA256SUMS.txt). Do not use GitHub's generated source archive as the inspected installation package. See [installation and rollback](docs/INSTALL.md), [frozen-package publication status](docs/releases/0.2.0-preview.1-publication.md), and [prepublication compatibility and verification records](docs/COMPATIBILITY.md).

The `main` branch is for development. Use a confirmed versioned package for installation; contributors need Git LFS to fetch the complete source images. The core skills require no Go runtime or local image model. Generation tools and optional card-rendering dependencies are separate. Public prompt cards are unbranded by default; an authorized local watermark is optional.

1. Follow the installation guide to copy all 18 directories in the frozen package under `skills/` as siblings into a new project's `.agents/skills/`. Preserve the exact prior installation and package hash before an upgrade.
2. Ask for Oneirloom, "织梦师", or "织梦师Skill"; explicitly invoke `$oneirloom` when using the technical ID. Method skills remain available directly.
3. Give the requested image or tutorial goal and any model, reference, or result already available. Confirmed conversation settings are inherited.
4. The main skill selects methods. A method reads its template index only when a concrete recipe helps, then loads a matching template. Without a match, it composes from its reusable method.

For standalone image prompts, the default output is a complete Chinese prompt followed by an equivalent English prompt, with one pair per explicitly requested model. An explicit single-language request overrides this default. Parameters and reference-image inputs remain outside prompt text.

For tutorials, invoke `oneirloom-image-tutorial` or ask the main skill to write, expand, or polish an illustrated lesson. The requested article language and author voice govern the deliverable. Prose-only revisions reuse existing evidence.

## Three layers

| Layer | Contents |
| --- | --- |
| Main | [Oneirloom](skills/oneirloom/SKILL.md): context, routing, integration, output contract |
| Methods | Dream weaving; visual analysis; character sheets; product art direction; expression stickers; icons; brand identity; figure art; camera/composition; color/light; photography; illustration; graphic design; craft construction; digital form; space conception; Krea 2; Qwen-Image-2.1; result diagnosis; prompt cards; tutorial writing |
| Templates | [Photography](skills/oneirloom-style-photography/templates/index.md), [character sheets](skills/oneirloom-character-sheet/templates/index.md), [illustration](skills/oneirloom-style-illustration/templates/index.md), [design](skills/oneirloom-style-design/templates/index.md), and [craft construction](skills/oneirloom-craft-construction/templates/index.md): selection, visual anchors, slots, prompt scaffolds, image paths and evidence |

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
