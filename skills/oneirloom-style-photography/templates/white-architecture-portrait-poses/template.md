# White-architecture portrait poses

## Selection

Use this set for the four outdoor portrait poses accepted by the user on 2026-10-01. Select one variant for a single image. Use all four only when a series is requested. Select by pose and camera geometry; the white architecture, outfit and subject appearance can be replaced from the current brief.

| Variant | Select when | Accepted output | Exact submitted Chinese prompt | Generation record |
| --- | --- | --- | --- | --- |
| 01: Overhead forward lean | The subject reaches forward and looks up at a steeply elevated camera | [Full image](images/result-01.png) | [Prompt](submitted-prompt-01-zh.txt) | [Record](example-01.json) |
| 02: Low-angle side seat | The subject sits sideways with bent knees and lifts the chin | [Full image](images/result-02.png) | [Prompt](submitted-prompt-02-zh.txt) | [Record](example-02.json) |
| 03: Front stair seat with drink | An asymmetrical seated portrait has a raised knee and a drink between the feet | [Full image](images/result-03.png) | [Prompt](submitted-prompt-03-zh.txt) | [Record](example-03.json) |
| 04: Wall lean with raised leg | One leg supports the body while the other bends across it against a wall | [Full image](images/result-04.png) | [Prompt](submitted-prompt-04-zh.txt) | [Record](example-04.json) |

The linked images are generated outputs, not the earlier photographic references. Inspect the selected full image before adapting its pose. Cropped prompt cards do not show enough of the legs to establish their geometry.

## Shared visual anchors

- Keep the chosen camera position distinct from the other variants. Variant 01 uses steep downward viewing. Variants 02 and 04 use upward viewing. Variant 03 places the camera farther back and slightly below the face for a complete seated view.
- Preserve each leg's knee state, direction, depth order and visible support. A bent or overlapping leg does not establish that a foot touches a wall. Keep observed support separate from inferred support.
- Keep the face and both shoes inside a full-body composition unless the user requests another crop. Resolve person scale and environmental space from the selected example rather than using one occupancy ratio for the whole set.
- When reusing the accepted styling, keep fair skin with a soft rosy undertone across the face, arms and legs. Cheeks and joints have subtle pink coloration, highlights approach white, and shadows remain light pink-gray. Sunlit warmth and wet reflections affect local appearance; they do not change the skin base to tan or golden brown. Another requested complexion overrides this scoped default.
- Preserve regional colors when this look is selected: granular cool gray-white architecture, blue-gray shadows, dark hair, muted reddish-brown fabric, faded gray-blue denim and caramel-brown footwear. Sky appears in variants 02, 03 and 04; variant 01 has only a small sand area above the walls.

## Pose and camera anchors

### 01: Overhead forward lean

Place the camera in front of and well above the subject, pointing steeply downward. The face and shoulders are nearer than the hips and feet. The torso leans forward, while the hips recede toward image right. Both arms reach toward image left and leave the frame; keep hand contact unspecified where the hands are cropped. The head lifts toward the lens with direct eye contact. Both legs remain separated with slightly bent knees, and both feet rest on the stairs below. A curved wall occupies the left foreground. Hair spreads to image right and falls toward the shorts.

### 02: Low-angle side seat

Place the camera low near the stairs, pointing upward. The hips visibly rest on the right-side seat. The torso is side-on toward image left, with the chest lifted, neck extended and chin raised toward the upper left. Both knees are bent. The near thigh runs from the right-side hip toward the central knee; the near lower leg extends toward the lower left. The far leg sits behind it, with its lower leg partly obscured. Both sandals rest on the lower steps in the accepted output. One hand hangs between the legs. Preserve the near/far size difference seen in the output without forcing the historical prompt's two-to-one head/foot width target.

### 03: Front stair seat with drink

Use enough camera distance for the complete seated figure, both shoes, the drink and recognizable stairs. The accepted output has a mostly frontal torso and a gently tilted head looking toward the lens. Both knees are bent and open asymmetrically. The image-right knee is raised closer to the chest; its lower leg descends toward the lower right. The image-left knee opens outward and its lower leg descends toward the lower left. Both feet rest on the lower step. One forearm crosses the body toward the image-left knee; the other hand reaches downward over the lid of an upright drink between the feet. Preserve this observed pose when reusing the accepted result rather than restoring the earlier prompt's tucked-back foot.

### 04: Wall lean with raised leg

Place the camera near ground level with an upward view. The back and hip lie against the right-side wall. The support leg extends to the ground, with its sandal sole and heel visibly supported. The other knee bends outward toward image left; its lower leg folds diagonally back to image right across the support leg. The raised sandal remains higher than the grounded sandal, beside the wall. Keep its wall contact unspecified unless requested. The visible arm hangs beside the wall with relaxed fingers. The head tilts toward image left while the face looks toward the lens. An arch and sky remain visible beside and above the figure.

## Adjustable slots and scoped defaults

Resolve identity, adult age, face, hairstyle, complexion, build, outfit, accessories, footwear, setting, light, drink and visible text from the current request. Follow the main skill's person defaults when unspecified. Keep requested thigh volume separate from face, torso, arm and calf size.

For reuse of this particular look, the styling preset is long dark hair, fair rosy skin, muted reddish-brown halter fabric, distressed denim shorts, gold jewelry and chain details, caramel thong sandals and burgundy toenails. The accepted tops differ: variants 01 and 03 show a cropped swim top; variants 02 and 04 show fabric extending toward the waist. Preserve the selected garment boundaries rather than forcing one top construction across all four images.

White curved walls, stairs, blue sky and hard sunlight are setting defaults for this set. They are not required for using the poses elsewhere. The drink and its literal `COFF` lettering belong to variant 03 when that prop is selected. Embedded seeds and sampling values belong to the historical runs, not to new tasks.

## Complete prompt scaffolds

Choose one scaffold, resolve every slot and deliver the languages required by the main skill. These scaffolds describe the accepted visible poses. They are new reusable prompts and have not been generation-tested. For the historical wording, use the exact submitted prompt files without modifying them.

### 01 scaffold

```text
A realistic {aspect ratio, default 3:4} outdoor full-body fashion portrait of {adult subject and appearance} among {curved walls and stairs}. The camera is in front of and well above the subject, looking steeply downward. Show the head through both shoes. The face and shoulders are near the lens, the hips recede toward image right, and the legs extend toward the bottom with natural overhead foreshortening. A curved wall occupies the left foreground.

The torso leans forward, both arms reach toward image left and continue beyond the frame, and both hands are outside the crop. The subject lifts the face toward the lens with direct eye contact and {expression}. Both knees are slightly bent, the legs remain separated, and both feet rest on the stairs. {Hair, default long dark hair spreading toward image right and falling toward the shorts}.

{Outfit construction, colors and coverage}. {Accessories and footwear}. {Complexion, default fair skin with a soft rosy undertone, pink cheeks and joints, near-white highlights and pale pink-gray shadows}. {Light direction, default diagonal sunlight from above, with clear local reflections and edged cast shadows}. {Wall, stair and ground colors and textures}. Keep the skin texture, hair strands, clothing and surrounding architecture clearly resolved.
```

### 02 scaffold

```text
A realistic {aspect ratio, default 3:4} outdoor full-body fashion portrait of {adult subject and appearance}, sitting sideways on the edge of {raised seat}. The camera is low near the steps, looking upward. The hips rest on the seat at image right, the head is in the upper-right area, and the bent legs extend toward the lower left and center. Keep the near sandal visibly larger than the far sandal while retaining the complete head and both shoes. {Surrounding architecture and upper sky} remain recognizable.

The torso faces image left, the chest lifts, the neck extends and the chin rises toward the upper left. The eyes look upward with {expression}. Both knees are bent. The near thigh extends from the right-side hip toward the central knee, and the near lower leg descends toward the lower left. The far leg remains behind it, with a partly obscured lower leg. Both sandals rest on lower steps. The arms descend beside the body, with one relaxed hand visible between the legs. {Hair}.

{Outfit construction, colors and coverage}. {Accessories and footwear}. {Complexion, default fair rosy skin with near-white highlights and pale pink-gray shadows}. {Directional light and cast shadows}. {Regional architecture, sky and fabric colors}. Keep the figure and rough setting clearly resolved with natural photographic detail.
```

### 03 scaffold

```text
A realistic {aspect ratio, default 3:4} outdoor environmental full-body portrait of {adult subject and appearance}, sitting on {stairs}. Use a camera slightly below the face, with a mild upward angle and enough distance for the full seated figure, both shoes and the surrounding steps. Leave recognizable wall and sky above and beside the subject and a strip of stair below the shoes.

The hips rest on an upper step and the torso faces mostly forward. The head tilts gently while the eyes look toward the lens with {expression}. Both knees are bent and open asymmetrically. The image-right knee is raised toward the chest, its lower leg descends toward the lower right, and the other lower leg descends toward the lower left. Both feet rest on the lower step. One forearm crosses toward the image-left knee, with relaxed fingers beside it. The other hand reaches downward over the lid of {an upright drink between the feet, including requested visible lettering}. {Hair}.

{Outfit construction, colors and coverage}. {Accessories and footwear}. {Complexion, default fair skin with soft pink coloration, near-white highlights and pale pink-gray shadows}. {Light direction and local reflections}. {Regional wall, stair, sky and clothing colors}. Preserve the drink's scale beside the legs, clear stair geometry and natural skin and fabric detail.
```

### 04 scaffold

```text
A realistic {aspect ratio, default 3:4} outdoor full-body fashion portrait of {adult subject and appearance}, leaning against {wall}. The camera is near ground level and points upward, with enough distance to include the complete head and both shoes. Place the subject in the right half, with {an architectural opening and sky or the requested surrounding environment} visible beside and above the figure. Leave space above the head and below the grounded shoe.

The upper back and hip rest against the right-side wall. One leg extends downward as the support leg, with the sandal sole and heel on the ground. The other knee bends outward toward image left, and its lower leg folds diagonally toward image right across the support leg. The raised sandal remains above the grounded sandal beside the wall. The visible arm hangs along the wall with relaxed fingers. The head tilts toward image left, and the face looks toward the lens with {expression}. {Hair, default long dark hair lifted toward image left by the wind}.

{Outfit construction, colors and coverage}. {Accessories and footwear}. {Complexion, default fair rosy skin with near-white highlights and pale pink-gray shadows}. {Light direction and cast shadows}. {Regional wall, sky, ground and clothing colors and textures}. Keep the leg overlap, visible foot support and complete architectural setting clear.
```

## Examples and evidence

The user supplied four generated PNGs and accepted this pose set on 2026-10-01. Each original PNG is archived byte-for-byte with its embedded ComfyUI prompt graph and workflow. The exact submitted Chinese prompts, local checkpoint filenames and sampling settings were extracted from those PNGs. All four outputs are 1248 by 1664, with a recorded 3:4 resolution selector.

The embedded loader names identify a local Qwen-Image-2.1 quantized checkpoint, a Qwen3-VL text encoder and a Qwen image VAE. This is evidence of the recorded local workflow, not of an official hosted entry, unchanged upstream weights or repeatability. The `Qwen21_official` save prefix does not establish those claims.

Variant 02's historical prompt requests 3:5, but its recorded resolution selector and output use 3:4. Variant 03's accepted output differs from its historical wording in torso tilt and far-foot placement. Keep these differences in the example records; do not edit the old prompts to erase them.

The four original outputs have been visually inspected, and user acceptance applies to the pose set. No new generation was performed while collecting it. Exact reference matching, new subject or wardrobe adaptations, the reusable scaffolds and cross-session automatic selection have not been tested.
