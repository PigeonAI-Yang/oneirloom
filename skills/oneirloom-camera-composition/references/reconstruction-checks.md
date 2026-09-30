# Camera and composition reconstruction checks

Perspective-mapping checks for `oneirloom-camera-composition` in reference reconstruction. They run alongside the [`oneirloom-visual-analysis` reconstruction workflow](../../oneirloom-visual-analysis/references/reconstruction-workflow.md), steps 2–3.

## Map three projected scales

For reference reconstruction with strong perspective, map three projected scales before writing the prompt: the nearest foreground element, the subject's head/torso, and the largest background form. Record their apparent frame-width or frame-height shares, overlap, and edge crops, plus the camera's apparent proximity to the nearest element and the direction of its optical axis. Express the decisive relations as affirmative, visible geometry in the prompt; a low-angle label alone does not preserve foreground exaggeration.

Keep this scale map when changing medium, such as from illustration to realistic photography.

## Check frame proportions before blaming the aspect ratio

In result comparisons, check actual frame proportions before attributing a scale mismatch to aspect ratio.
