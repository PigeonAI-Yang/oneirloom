<div align="center">

<h1>Oneirloom · 织梦师</h1>

<p><strong>Turn imagination into images.</strong></p>

<p>An open-source collection of visual prompting skills for analyzing images, developing concepts, writing complete prompts, and refining generated results.</p>

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

The collection uses three layers: **one main skill, reusable method skills, and indexed templates**. Concrete recipes live with their prompts and example records instead of becoming separate skills.

## Use

1. Install the skill directories under `skills/` as siblings in the host's skill search root.
2. Ask for Oneirloom, "织梦师", or "织梦师Skill"; explicitly invoke `$oneirloom` when using the technical ID. Method skills remain available directly.
3. Give the requested image or tutorial goal and any model, reference, or result already available. Confirmed conversation settings are inherited.
4. The main skill selects methods. A method reads its template index only when a concrete recipe helps, then loads a matching template. Without a match, it composes from its reusable method.

For standalone image prompts, the default output is a complete Chinese prompt followed by an equivalent English prompt, with one pair per explicitly requested model. An explicit single-language request overrides this default. Parameters and reference-image inputs remain outside prompt text.

For tutorials, invoke `oneirloom-image-tutorial` or ask the main skill to write, expand, or polish an illustrated lesson. The requested article language and author voice govern the deliverable. Prose-only revisions reuse existing evidence.

## Three layers

| Layer | Contents |
| --- | --- |
| Main | [Oneirloom](skills/oneirloom/SKILL.md): context, routing, integration, output contract |
| Methods | Visual analysis; character sheets; expression stickers; icons; brand identity; figure art; camera/composition; color/light; photography; illustration; design; Krea 2; Qwen-Image-2.1; result diagnosis; tutorial writing |
| Templates | [Photography](skills/oneirloom-style-photography/templates/index.md), [character sheets](skills/oneirloom-character-sheet/templates/index.md), [illustration](skills/oneirloom-style-illustration/templates/index.md), and [design](skills/oneirloom-style-design/templates/index.md): selection, visual anchors, slots, prompt scaffolds, image paths and evidence |

Templates include crouching selfies, indoor full-length portraits, four-view plus four-expression cards, three-view cards, character wardrobe sheets, decorative rainy-night prints, halftone portrait cutouts, physical fuse-bead artworks, and portrait-to-blind-box comparison images.

A method directory includes its own template assets. Method skills remain usable without a matching template. Skill lookup uses exact names; Markdown links do not automatically invoke skills. For installation and ownership details, see the [architecture](docs/architecture.md).

## Specialist design methods

| Method | Scope | Templates |
| --- | --- | --- |
| [oneirloom-expression-stickers](skills/oneirloom-expression-stickers/SKILL.md) | Reaction intent, consistent character identity, and individual sticker delivery | [Head reactions, action gestures, caption reactions](skills/oneirloom-expression-stickers/templates/index.md) |
| [oneirloom-icon-design](skills/oneirloom-icon-design/SKILL.md) | UI icon families, app symbols, and native vector assets | [Outline UI, solid UI, app symbol](skills/oneirloom-icon-design/templates/index.md) |
| [oneirloom-brand-identity](skills/oneirloom-brand-identity/SKILL.md) | Coherent VI foundations, applications, guidelines, and asset handoff | [Wordmark, mascot, editorial systems](skills/oneirloom-brand-identity/templates/index.md) |

These methods reuse the graphic-design SOP within the existing three layers. Their nine recipes are researched starting points with no corresponding generated examples or end-to-end VI production tests. A requested SVG, asset set, or VI guideline uses its artifact contract; prompt-only work retains complete bilingual prompts. A contact sheet or brand board does not establish complete asset delivery.

## Example evidence

The [indoor full-length template](skills/oneirloom-style-photography/templates/indoor-full-length/template.md) contains an existing generated PNG and its exact submitted prompt and settings. The image was inspected during migration, with framing and foot-spacing limitations recorded. Its generalized scaffold has not been generated.

Other migrated templates explicitly distinguish missing image evidence from user-reported results. Adding an image path does not itself establish visual success.

The [character wardrobe sheet](skills/oneirloom-character-sheet/templates/wardrobe-sheet/template.md) contains an original illustrated reference, a user-provided realistic result, and the Chinese prompt delivered in the conversation. The result was inspected with turnaround and costume-portrait deviations. Its actual execution metadata is unknown, and the generalized scaffold has not been generated.

## Maintenance

Read [CONTRIBUTING.md](CONTRIBUTING.md) for adding templates and examples, and [model evidence](docs/model-evidence.md) for model-specific claims. This repository uses the MIT license; model and service terms remain separate.
