# Oneirloom project directory index

This index describes resource directories and their purposes. Keep individual file lists in the relevant directory's own documentation.

## Directory map

```text
docs/assets/dream-cocoon/ (mascot references and character asset cards)
├── logo-icons/ (color/background variants and icon sizes)
└── logo-actions/ (pose and expression icon variants)
tools/
└── comfyui/ (local one-click generation tool and API workflow)
skills/
├── oneirloom/ (main visual-workflow router and shared references)
│   └── references/visual-families/ (ten-family index and foundation notes)
├── oneirloom-dream-weaving/ (local inspiration-development skill and dialogue examples)
├── oneirloom-craft-construction/ (craft method, construction reference, and fuse-bead recipe)
├── oneirloom-digital-form/ (digital form method and transformation mechanisms)
├── oneirloom-space-conception/ (spatial layout method and relation checks)
├── oneirloom-color-light/references/material-response.md (shared surface-response guidance)
├── oneirloom-style-photography/references/still-frame-staging.md (static cinematic staging)
├── oneirloom-character-sheet/references/fashion-styling.md (conditional outfit coordination)
├── oneirloom-expression-stickers/ (sticker skill and templates)
└── oneirloom-product-art-direction/references/ (product cases and ecommerce collaboration examples)
output/
├── comfyui/ (locally retrieved ComfyUI results)
├── dream-cocoon-asset-cards-20261001/ (mascot asset cards)
├── oneirloom-plugin-icon-0.1.2/ (selected plugin icon and complete candidate package)
└── oneirloom-stickers-20261003/ (selected sticker pack and offline browsing)
work/
├── readme-launch/badges-20261003/ (README desktop/mobile previews and verification receipt)
├── sticker-pack-templates-20261002/ (sticker browser and file-placement verification)
├── ecommerce-workflow-20261003/ (structural checks and text-only ecommerce exercises)
├── dream-weaving-20261010/ (source checks, text trials, handoff repair and prompt delivery)
├── visual-families-20261010/ (family foundation checks, 0.3.0-preview source and migration records, text exercises, and SVG source fixture)
└── progressive-disclosure-20261003/ (source migration and pending behavior verification receipts)
```

## Resource groups

| Group | Directories |
| --- | --- |
| Architecture and migration | [Active architecture](docs/architecture.md), [approved progressive-disclosure migration and pending acceptance](docs/architecture-progressive-disclosure-proposal.md), [approved visual-capability design and source implementation](docs/visual-capability-expansion-plan.md), [Pre-0.3.0 source checkpoint](docs/checkpoints/pre-0.3.0-preview-20261010.md) |
| Visual-family discovery | [Ten-family index and foundation notes](skills/oneirloom/references/visual-families/index.md), [Scope change and targeted checks](work/visual-families-20261010/checks.md), [0.3.0-preview source implementation](work/visual-families-20261010/implementation-0.3.0-preview.md), [Migration preservation record](work/visual-families-20261010/migration-preservation-0.3.0-preview.json), [Visual text exercise report](work/visual-families-20261010/text-exercises-visual-0.3.0-preview.md), [Visual text exercise data](work/visual-families-20261010/text-exercises-visual-0.3.0-preview.json), [Continuity text exercise report](work/visual-families-20261010/text-exercises-continuity-0.3.0-preview.md), [Continuity text exercise data](work/visual-families-20261010/text-exercises-continuity-0.3.0-preview.json), and [SVG source fixture](work/visual-families-20261010/fixture-arrow.svg) |
| Shared visual knowledge | [Material response](skills/oneirloom-color-light/references/material-response.md), [Still-frame staging](skills/oneirloom-style-photography/references/still-frame-staging.md), [Fashion styling](skills/oneirloom-character-sheet/references/fashion-styling.md), [Craft construction](skills/oneirloom-craft-construction/references/construction.md), [Digital form](skills/oneirloom-digital-form/references/form-and-transformation.md), and [Spatial relations](skills/oneirloom-space-conception/references/spatial-relations.md) |
| Mascot source and delivery | [Mascot source](docs/assets/dream-cocoon/), [Asset-card delivery](output/dream-cocoon-asset-cards-20261001/) |
| Local image generation | [ComfyUI one-click tool and usage](tools/comfyui/README.md), [Retrieved images](output/comfyui/) |
| Icon variants and plugin package | [Color variants](docs/assets/dream-cocoon/logo-icons/), [Pose variants](docs/assets/dream-cocoon/logo-actions/), [Plugin package](output/oneirloom-plugin-icon-0.1.2/) |
| Sticker skill and delivery | [Sticker skill](skills/oneirloom-expression-stickers/), [Sticker delivery](output/oneirloom-stickers-20261003/) |
| Dream-weaving trial | [Local skill](skills/oneirloom-dream-weaving/), [Dialogue examples](skills/oneirloom-dream-weaving/references/dialogue-examples.md), [Case definitions](evals/dream-weaving-cases.json), [Source checks and text trials](work/dream-weaving-20261010/) |
| Ecommerce collaboration | [Workflow guidance](skills/oneirloom-product-art-direction/references/ecommerce-workflow.md), [Chinese text-fixture examples](skills/oneirloom-product-art-direction/references/ecommerce-examples.md) |
| Progressive-disclosure instructions | [Shared interaction contract](skills/oneirloom/references/interaction-contract.md), [graphic design and conditional references](skills/oneirloom-style-design/) |
| Local 0.3.0-preview source | 22 source skills, including three new methods; development source preview with no corresponding package. See the [source record](docs/releases/0.3.0-preview.md). The 18-skill `v0.2.0-preview.1` package remains frozen. |
| Free 18-skill preview | [Release notes and current publication status](docs/releases/0.2.0-preview.1-publication.md), [versioned installation and rollback](docs/INSTALL.md), [verification status](docs/COMPATIBILITY.md) |
| Verification records | [Sticker verification](work/sticker-pack-templates-20261002/), [Ecommerce checks and text exercises](work/ecommerce-workflow-20261003/), [Progressive-disclosure verification](work/progressive-disclosure-20261003/), [Independent structure receipt](work/progressive-disclosure-20261003/structure-checks.json), [Actual text answers](work/progressive-disclosure-20261003/actual-answers.md), [Acceptance report](work/progressive-disclosure-20261003/acceptance-report.md), [Closure behavior checks](work/progressive-disclosure-20261003/closure-behavior-checks.json), [Closure actual answers](work/progressive-disclosure-20261003/closure-actual-answers.md), [Closure acceptance report](work/progressive-disclosure-20261003/closure-acceptance-report.md) |

Plugin 0.1.2 is a validated local candidate using the selected purple rounded icon. Installation, publication, and the connected Sites plugin icon update have not been performed.

The sticker delivery contains 14 templates and 156 selected PNG entries. Platform import and acceptance are unverified.

Oneirloom brand VI source and delivery directories listed above are local-private and must not be published. Completed image cases and showcase imagery are a separate category and remain publishable, including finished images containing branding. Website asset exceptions are explicit and minimal in `.gitignore`.
The HTML layout previews in `work/prompt-cards/green-lane/` remain local and are excluded from Git tracking; the prompt and rendered PNG files remain tracked.
[Local delivery provenance](../../deliveries/oneirloom-0.2.0-preview.1/CASE-PROVENANCE.json)
