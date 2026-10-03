---
name: vpd-style-halftone-cutout
description: Turn a supplied portrait into an isolated vintage black-and-white halftone newspaper paper-cut collage while preserving the person's identity and framing.
---

# Vintage halftone cutout portraits

Use for portrait edits in a black-and-white newspaper cutout collage style. Apply the rendering treatment to the supplied person image while preserving recognizable identity, facial and body geometry, expression, pose, crop, hairstyle, and accessories. Change only elements the user explicitly asks to change.

Render the portrait as crisp black and paper-white shapes with a regular circular halftone screen. Vary dot size and density with the source luminance so the face remains readable, especially around the eyes, nose, and mouth. Keep the dot pattern regular, with subtle aged print and paper texture confined to the cutout. Give the subject a natural cut-paper silhouette; a narrow off-white paper edge is optional.

Default to one isolated subject on a transparent canvas: only the cutout is visible, with the canvas empty and transparent outside its silhouette. Keep all paper and ink texture within the cutout. Add scenery, a backdrop, lettering, or a shadow only when explicitly requested. Treat transparency as the intended output state and verify the active entry's alpha support before claiming an RGBA result. For Qwen-Image-2.1, follow the entry-specific guidance in `vpd-model-qwen-image-2-1`.

Deliver a complete Chinese prompt followed by its equivalent English version in separate copyable blocks, with labels outside, unless the current request explicitly asks for one language. Use affirmative descriptions of the target image. For Qwen-Image-2.1, load `vpd-model-qwen-image-2-1` and use the active entry's confirmed ordered image labels, assigning identity and style roles to actual inputs. A text-only request must not invent reference-image labels.
