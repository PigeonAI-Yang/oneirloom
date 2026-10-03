# Hotel full-length mirror selfie

## Selection

Use for an upright full-length mirror selfie in a recognizable hotel room, with a handheld camera covering the face. The Chinese recipe name is "酒店镜面全身自拍". This is a standing selfie recipe; use the crouching template when the requested pose is a squat. Preserve the user's chosen recording device and face visibility when adapting the recipe.

## Visual anchors

- Use a vertical head-to-shoe frame. The source figure occupies about three quarters of the image height, slightly right of center, with generous wooden-wall space above the head and a small strip of floor below the shoes.
- Keep the torso upright and facing the mirror. The arm on image right holds the camera at face height, obscuring the central face; the other arm hangs beside the coat, with its hand concealed by folds. Keep the viewpoint near face height and gently downward, with upright background panel lines.
- In the accepted revision, the legs are long, parallel and fully extended. Each hip, knee and ankle aligns along its own straight axis in the frontal view, with forward-facing knees and shoe tips. Keep leg extension distinct from body volume.
- The current body preset has moderately full, rounded thighs, tapering smoothly toward small knees, followed by long slender calves and slim ankles. The widest part of each thigh is approximately 1.8 times the width of its calf, a small reduction from the earlier 2:1 prompt target. Keep natural volume through the middle thigh with a gentler outer contour. The lower body remains about sixty percent of overall height. These are requested stylized proportions, not measurements of the reference or universal anatomy rules. Keep the added volume local to the thighs while retaining the slim waist and light upper-body proportions.
- Preserve the greige coat's broad lapels, draped overlapping front panels, upper-thigh hem and hanging belt ends. The stockings below the hem remain sheer black, transmitting warm skin tones; the shoes remain glossy black pointed-toe stilettos.
- Keep the room readable: a large pale honey-colored wooden wall behind the person, bed and bedside cabinet on image left, light wood floor beneath the shoes. Warm light from above and toward image right illuminates the subject, with local bedside light and a floor shadow extending toward the lower left.

## Adjustable slots and scoped defaults

Resolve identity, hairstyle, device, face coverage, body proportions, clothes, hosiery, footwear, room and light from the current request. Use the router's person defaults when identity is unspecified. For reuse of this look, retain the moderately full thighs, slim calves, long straight legs, loose greige coat, sheer black tights, black patent pumps and warm wooden hotel room. Another requested build or outfit overrides this preset. The body ratios apply only when this preset is selected.

Keep the coat hem high enough for the requested thigh contour to remain visible. Describe thigh width separately from leg length and calf width. A general long-leg or slim-leg phrase does not specify the accepted proportions. Preserve the original arm and clothing relations while applying the explicitly revised straight-leg stance.

## Prompt scaffold

Resolve every slot and deliver the languages required by the router. The first archived prompt pair preserves the earlier delivered revision; use the second pair for the current slightly slimmer thighs. The current refinement and this adjustable scaffold have not been generation-tested.

```text
A realistic {aspect ratio, default 9:16} vertical full-body mirror selfie of {adult subject and appearance} in {recognizable hotel room}. Show the complete figure from head to shoes, slightly right of center, occupying about three quarters of the image height, with generous space above the head and a small strip of floor below the shoes. The viewpoint is near face height and angled gently downward, with upright wall-panel lines.

The torso faces the mirror and stays upright, with a level pelvis. The arm on image right bends upward and holds {device, default a small black camera} in front of the face, {requested face coverage, default covering the central face}. The other arm hangs naturally, with its hand concealed among the coat folds beside the waist. {Hair and visible accessories}.

{Body proportions, using the current preset when requested: a slim waist and light upper body, with moderately full thighs and gently rounded outer contours. Each thigh's widest part is approximately 1.8 times the width of its calf. The middle thighs retain natural volume and taper smoothly toward delicate knees. Long thighs and lower legs together account for about sixty percent of overall height. The calves are slender and taper toward slim ankles.} Both legs extend straight downward in parallel, with each hip, knee and ankle aligned along its own straight axis in the frontal view. Both knees are fully extended and face forward. The feet are close together with shoe tips pointing forward.

{Outfit, default a loose greige coat with broad lapels, draped overlapping front panels and uneven diagonal hems across the upper thighs. A small cream-white neckline shows inside the coat, and long belt ends hang beside the body, with the image-right end reaching close to the lower leg.} The thigh contours below the hem clearly show the chosen thigh-to-calf proportions. {Hosiery and footwear, default sheer black tights transmitting warm skin tones, with darker knee and side areas and narrow soft frontal highlights, plus glossy black pointed-toe stiletto pumps.}

{Room layout, default pale honey-colored wood panels behind the person, white bedding and a gray-beige upholstered headboard on image left, a wooden bedside cabinet with a dark tissue box, a black wall lamp and outlets, pale upper wall panels with warm concealed lighting, and a light wooden floor with part of a pale rug.} Warm light from above and toward image right illuminates the hair, coat and legs. Local bedside light provides fill, and the figure's floor shadow extends toward the lower left. Preserve the separate colors and material responses of the coat, bedding, tights and shoes. Keep hair, fabric folds, hosiery transparency and room details recognizable, with a real lifestyle-selfie texture.
```

## Examples and evidence

| ID | Role | Asset or record | Evidence status |
| --- | --- | --- | --- |
| reference-01 | User-provided source photograph for framing, clothing and room | [Original reference](images/reference-01.webp); [case record](example-01.json) | Inspected in the chat; copied unchanged. Its original thighs and stance are not evidence for the revised body preset. |
| delivered-01 | Complete revised prompt accepted by the user | [Chinese prompt](delivered-prompt-01-zh.txt); [English prompt](delivered-prompt-01-en.txt) | User reported a good result and requested template collection on 2026-09-30. No generated output was supplied or inspected, and the submitted language, model, entry and settings are unknown. |
| current-02 | Complete prompt with slightly slimmer thighs, following the user's refinement | [Current Chinese prompt](current-prompt-02-zh.txt); [Current English prompt](current-prompt-02-en.txt) | User subsequently reported excessive thigh volume and requested a small reduction on 2026-09-30. This prompt refinement has not been generated or accepted after testing. |

The first delivered prompt left the thighs too slim according to user feedback. The accepted revision strengthened the thigh-to-calf width contrast, retained thigh thickness through the middle section, lengthened both leg segments and replaced the earlier slight inward foot turn with a straight, forward-facing stance. Archive the revision as delivered rather than treating it as a verified execution receipt. No new image generation was performed during collection. User-reported satisfaction supports reuse of this recipe; it does not establish inspected image fidelity or repeatability.

The subsequent user correction requested slightly slimmer thighs. The current preset reduces the prompt's thigh-to-calf width target from 2:1 to 1.8:1 and softens the thigh-volume wording, while preserving leg length, straight alignment, calf and ankle proportions, clothing, framing and light. This is a prompt adjustment, not a measured ten-percent reduction in a generated image. Keep the earlier prompt pair and its feedback as historical evidence; the current pair remains untested.
