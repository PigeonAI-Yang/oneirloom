# Qwen-Image-2.1 task map

Read [task-specific writing](writing.md) for prompt order, edit wording, and the distinction between image-model inputs and the companion enhancers' contracts.

| Task | Prompt focus | Official model-level documentation | Verify in the active entry and output |
| --- | --- | --- | --- |
| Text-to-image | Describe the target scene, subject relationships, lighting, and medium. | The model card and QwenLM README show text-to-image inference with Diffusers. | Confirm the active route, supported sizes, and exposed generation controls. |
| Single-image edit | State the requested change and the content that must stay intact. | The QwenLM README shows image-conditioned editing through the pipeline's `image` input. | Confirm the upload field and inspect whether unrelated regions remain intact. |
| Multiple references | Assign each reference a role, such as identity, pose, color, or style. | The QwenLM README says the model supports up to 10 references and passes a list to the `image` input. | Confirm the active entry's image limit, order, and input syntax. |
| Local edit | Name the changed region, its boundary, and the content to preserve. | Qwen's documentation describes circles, painted annotations, and separate masks. | Confirm which region controls the active entry exposes and inspect the edit boundary. |
| RGBA | Describe a transparent background and the complete subject outline. | Qwen documents native RGBA generation and gives a recommended prompt format. | Inspect the output file for an alpha channel; wording alone does not prove the entry returned transparency. |

These sources describe model-level capabilities and Diffusers examples. They do not establish that a third-party UI or API exposes the same inputs. Read the [official archive index](official/README.md) for source revisions, hashes, and task-specific reading guidance.

Qwen's prompt-rewriting companion uses separate fine-tuned Qwen3.5-VL checkpoints for text-to-image and editing. Its text-to-image profile returns a detailed English prompt and accepts input in any language. This companion is separate from the image model and does not establish that English prompts outperform Chinese. The archived Qwen sources do not give a front-facing, flat-foot squat recipe or guarantee that output. Do not present either as an official model specification.
