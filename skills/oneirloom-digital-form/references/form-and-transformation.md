# Form and transformation reference

Use this reference for digital geometry and transformations. Graphic layout stays with design. Surface response stays with [color and light](../../oneirloom-color-light/SKILL.md) and its [material-response reference](../../oneirloom-color-light/references/material-response.md). Camera position and projection stay with [camera composition](../../oneirloom-camera-composition/SKILL.md).

## Resolve the shape

- **Silhouette and scale.** Describe the outer contour, major volumes, relative size, and the parts that carry identity. Keep size relationships consistent across connected parts.
- **Discrete and continuous form.** For cells, tiles, beads, or repeated components, name the unit, spacing, and rule of repetition. For continuous volumes, describe how adjoining regions connect and where the contour changes. When a transformation crosses between the two, say which areas remain separate units and which merge into a surface.
- **Deformation.** State what changes and what stays recognizable. Relate bends, compression, enlargement, or stylization to a visible anchor rather than a general instruction to preserve identity.
- **Connections and layers.** Describe attachment points, continuity across joins, front-to-back order, gaps, and occlusion. Check that each visible part has a plausible relation to its neighbors.
- **Surface and view.** Geometry owns the form. Send roughness, transparency, illumination, and reflection behavior to color and light. Send viewpoint, crop, and projection to camera composition.

## Mechanisms

### Coherent three-dimensional form

- **ID:** `digital.coherent-3d-form`
- **Tags:** D
- **Owner:** `oneirloom-digital-form`
- **Visible mechanism:** Connected surfaces, volumes, and component scale agree across the whole object. Reflective or transparent areas follow the shape's continuity; their detailed appearance belongs to color and light.
- **Variables:** Outer silhouette, component proportions, connection points, depth, scale cues, and the amount of geometric simplification.
- **Failure and correction:** If parts do not read as one object, define their shared boundary, overlap order, and attachment. If the object changes scale between parts, state the relative dimensions again before adding surface detail.
- **Source and evidence:** Expanded independently from the 3D row in [graphic-design styles](../../oneirloom-style-design/references/styles.md), which names geometry, scale, structure, reflection, and consistency. This method entry is authored and unrendered; the earlier row does not validate it.

### Identity translated into collectible volume

- **ID:** `digital.identity-to-collectible-volume`
- **Tags:** D, T
- **Owner:** `oneirloom-digital-form`
- **Visible mechanism:** A person becomes a compact sculpted figure while selected identity cues remain visible in the hair silhouette, face, expression, clothing, and pose. Relative head, torso, and limb volumes define the chosen stylization.
- **Variables:** Head-to-body ratio, facial simplification, hair volume, limb length, pose, clothing translation, and surface treatment.
- **Failure and correction:** If the figure becomes generic, restore the source's strongest visible identity cues and their relation to the chosen volumes. If it no longer resembles the requested style, adjust the stated proportions rather than adding unrelated detail.
- **Source and evidence:** Extracted from the local [blind-box comparison template](../../oneirloom-style-design/templates/blind-box-comparison/template.md). Its two-panel layout, proportions, pose, materials, background, and `<image1>` token remain template-specific. The template records no verified repeatability, and this generalized entry has no new rendered result.

## Assign reference roles

Use the role convention supported by the active image entry. A reference can supply identity, shape, material, or another explicitly requested feature. The blind-box template uses `<image1>` for its supplied identity photograph. That literal token does not apply to every model or entry. Do not invent an input label when the active entry does not support it; describe the role in portable text instead.

## Worked decision: fictional layered perfume bottle

For a fictional bottle concept, one possible resolution is a continuous clear outer shell, a narrow neck, and two translucent bands inside the shell. Keep the outer contour connected through the shoulder and base, place the bands behind the front wall, and give each band a visible boundary. Treat these as choices for this example, not defaults or facts about a product. Ask color and light to describe transparency and reflection. Return a render prompt unless the user requests and the available tools produce an editable model.
