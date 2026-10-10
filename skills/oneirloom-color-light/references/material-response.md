# Material response

Use this reference when a surface needs to read through its visible response to light. It covers appearance across image media, not object construction. Keep stated product properties tied to user or source evidence.

Separate a material's supported base identity from the scene's illumination. Describe how direct light, reflected environmental color, transmission, shadow, and highlights affect its visible appearance. Keep cues local to the relevant regions; an overall warm or cool impression does not tint every material or shadow.

For transparent-fabric reconstruction, keep evidence-specific checks in [evidence checks](evidence-checks.md). This reference does not replace them.

## Selected mechanism entries

These locally identified entries record useful visual variables and correction cues. They are authored guidance, not claims that a particular material or image result has been tested.

### MR-01. Base color and reflected illumination

- **ID:** `MR-01`
- **Tags:** `base-color`, `illumination`, `regional-consistency`
- **Owner:** `oneirloom-color-light`
- **Variables:** supported base hue; key and fill light; nearby reflected color; lit and shadowed regions.
- **Failure:** a bright patch is mistaken for the material's identity, or a global tint erases distinct regional colors.
- **Correction:** name the base identity and illumination separately, compare lit planes with shadows, and revise only the affected regional cue while preserving colors that already read correctly.
- **Provenance:** generalizes the regional comparison rule in [evidence checks](evidence-checks.md) and the material-response scope in the [visual-capability expansion plan](../../../docs/visual-capability-expansion-plan.md) §5.
- **Unrendered state:** written guidance only; no new image was rendered to validate it.

### MR-02. Roughness, highlights, and reflectivity

- **ID:** `MR-02`
- **Tags:** `roughness`, `highlight-shape`, `reflectivity`
- **Owner:** `oneirloom-color-light`
- **Variables:** surface roughness; highlight width and edge softness; reflection strength and clarity; visible reflected surroundings.
- **Failure:** surfaces with different finishes receive the same highlight treatment, or reflections do not correspond to the surrounding scene.
- **Correction:** use broader, softer highlights and weaker environmental reflections for a diffuse finish; use more defined highlights and clearer reflections for a polished finish when supported by the intended or observed appearance. Keep the cue about appearance rather than asserting an unverified product specification.
- **Provenance:** newly organized material-response guidance scoped by the [visual-capability expansion plan](../../../docs/visual-capability-expansion-plan.md) §5; no prior rendering is attributed to this entry.
- **Unrendered state:** written guidance only; no new image was rendered to validate it.

### MR-03. Transmission, thickness, and scale

- **ID:** `MR-03`
- **Tags:** `transmission`, `thickness`, `scale`
- **Owner:** `oneirloom-color-light`
- **Variables:** visible transmission; supported boundary or edge cues; apparent thickness; texture size relative to the object and nearby scale references.
- **Failure:** a surface is called transparent without describing what is visibly transmitted, or texture and thickness cues make the object read at an inconsistent scale.
- **Correction:** state what can be seen through or at the material boundary only when supported; relate texture size and visible thickness to the object's boundaries and nearby scale cues.
- **Provenance:** newly organized material-response guidance scoped by the [visual-capability expansion plan](../../../docs/visual-capability-expansion-plan.md) §5. Transparent-fabric evidence remains in [evidence checks](evidence-checks.md).
- **Unrendered state:** written guidance only; no new image was rendered to validate it.
