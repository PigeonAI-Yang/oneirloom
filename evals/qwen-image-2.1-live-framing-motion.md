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
