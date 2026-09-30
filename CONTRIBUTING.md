# Maintenance

- Keep instructions and rule updates in English. Prompt scaffolds, exact historical prompts, and requested in-image text may use their task language.
- Keep the main skill focused on task routing and the shared output contract. Add a method skill only for a distinct reusable decision process, and update its route.
- Add a concrete scene, pose, card layout, or style recipe under its owning method's `templates/<id>/template.md`. Add one entry to that method's `templates/index.md`. Do not add a new skill or router row for every template.
- Follow the [template ownership and format](docs/architecture.md#template-ownership-and-format). Preserve defining relations, identify adjustable slots, and keep defaults scoped to the recipe. No match must remain a valid path through the method.
- For a generated example, store the actual image, exact submitted prompt, known model/entry and relevant settings, plus inspected observations or an accurate uninspected status. Keep paths relative and assets inside the template directory. Missing images stay missing; do not substitute an unrelated illustration or claim user-reported success was inspected.
- When changing a scaffold, preserve historical example prompts. Add a new generation record only after an actual run. Preserve image integrity; record any processing separately.
- Keep model facts specific to version, entry, and task. Distinguish official documentation, local observations, hypotheses, and unknowns. Include official URLs and verification dates for model facts. A model capability does not establish the controls exposed by every third-party entry.
- Promote language or length preferences only with controlled evidence. Krea hosted creativity controls are not interchangeable with RAW weights.
- Delivered prompts are complete and affirmative by default. Requested negative prompts stay separate. Literal in-image text such as "NO SIGNAL" is not an exclusion instruction.
- Refresh official sources only when changing model facts. Architecture-only migration does not require new online model research or image generation.
