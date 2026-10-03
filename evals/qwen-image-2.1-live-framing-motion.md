# Qwen-Image-2.1 local framing and motion observations

- Date: 2026-09-26
- Entry: local ComfyUI workflow on port 8188
- Model stack: Qwen-Image-2.1 int8, Qwen3-VL int8, and VAE
- Controlled settings: seed `568747609386335`, 40 steps, CFG 1, Euler, simple scheduler
- Evidence level: observed local outputs; this is evidence about these runs, not a general claim about Qwen-Image-2.1
- Output directory: `ComfyUI/output/`. The first row is a pre-existing history record; the other five runs were submitted for this check.

| Run history | Canvas and controlled prompt change | Output | Observation |
| --- | --- | --- | --- |
| `ff7562e8-783d-4a56-9f04-4d8eb3505bf4` | Existing 1024×1920 baseline with the original text prompt | `Qwen21_official_00047_.png` | The result looked different from the supplied image despite the same text prompt. |
| `2e6c1442-4ed0-4d41-9340-0cf29e8c271e` | 1024×1920; explicit head-to-waist crop | `VPD_Qwen21_frame_test_00001_.png` | Still thigh-up and static. |
| `17d1054f-dd40-49bf-abf0-3596298dc382` | 1024×1280; same crop prompt | `VPD_Qwen21_frame_4x5_test_00001_.png` | Still thigh-up and static. |
| `c524f99a-1b41-4472-b050-5b224d54b3ab` | 1024×1280; closer camera and larger subject occupancy | `VPD_Qwen21_close_frame_test_00001_.png` | Still below the waist and static. |
| `5289d9e8-f3a6-4461-b414-cb7e475846b8` | 1024×1024; same closer prompt | `VPD_Qwen21_close_square_test_00001_.png` | Somewhat closer, but still below the waist and static. |
| `246d7b76-4a8e-4f1d-bc2d-177d50a1864f` | 1024×1024; moving-step and head-turn prompt | `VPD_Qwen21_motion_square_test_00001_.png` | Hair, jacket, and arm motion were visible, but the torso/head turn relation was not reliable; framing remained below the waist. |

These runs support checking canvas geometry and competing composition constraints after repeated crop misses, and describing torso and head orientation separately for motion. They do not establish a universal model limitation. No output images are copied into this repository.

## Reference-path follow-up

The next runs used the same local Qwen-Image-2.1 checkpoint. The text-only run kept 40 steps. The reference runs used an existing successful image-edit graph with 25 steps and CFG 1, so their visual differences from the text-only run do not isolate the effect of the reference image. The supplied image stayed unchanged; `ImageCrop` prepared a square reference before generation.

| Run history | Input and change | Output | Observation |
| --- | --- | --- | --- |
| `a9129d90-9d84-47bd-9483-18eb4021c4a4` | Text only; shorter pose and crop prompt at 1024×1024 | `VPD_Qwen21_compact_pose_crop_00001_.png` | Torso and head directions differed more clearly, but the jacket covered the dress and the frame extended below the waist. |
| `51b08a94-4759-4752-a6c5-e00594df918c` | Supplied image cropped to 1024×1024 at y=250; reference also supplied the sampler latent | `VPD_Qwen21_ref_edit_pose_waist_00001.png` | Face, outfit, and light stayed close to the supplied image; pose changed little. |
| `479b922e-4a7f-4088-90b7-311d428b3e33` | Same reference; empty sampler latent | `VPD_Qwen21_ref_t2i_motion_crop_00001.png` | Appearance stayed close to the supplied image, while the requested step and turn remained weak. |
| `2deacac7-bae3-471c-81e8-39210c4a5638` | Crop-only preview at y=100; no model generation | `VPD_reference_crop_preview_00001_.png` | The preview contains the upper body and less of the dress below the waist. |
| `a0c3cfd3-003c-4c34-9c47-aca04c9bc11c` | Reference crop moved to y=100; empty sampler latent | `VPD_Qwen21_ref_t2i_crop_y100_00001.png` | Appearance remained close to the supplied image and framing moved closer to the waist; pose stayed nearly static. |
| `96daa15c-4811-4b70-bbac-133bfaef600e` | Added a second reference for torso and head direction | `VPD_Qwen21_two_refs_pose_waist_00001.png` | The turn was clearer, but the jacket hid the dress and the rendering became harsher. |

This follow-up shows a tradeoff in these local runs: the appearance reference retained the original look and pose, while a second pose reference changed both pose and styling. It does not prove that the model always behaves this way or that the reference routes are equivalent to a pose control model.
