# Qwen-Image-2.1 official documentation archive

Retrieved 2026-09-29 UTC. The files below are unmodified source snapshots. Their SHA-256 values identify the saved bytes. No model weights or example media are included.

| Local snapshot | Official source | Source revision | SHA-256 |
| --- | --- | --- | --- |
| [Hugging Face model card](hf-model-card.md) | [Qwen/Qwen-Image-2.1 card](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/790c92633540aa0cb11d9abf19eb46d861714758/README.md) | `790c92633540aa0cb11d9abf19eb46d861714758` | `ee79e9dccc074f71fed40bf1cd74f35928b2f4e03a992ec193c437907308289f` |
| [QwenLM release README](github-readme.md) | [QwenLM/Qwen-Image-2.1 README](https://github.com/QwenLM/Qwen-Image-2.1/blob/fb7ae1d1f9611cd91524d03c53c5246b36ac8577/README.md) | `fb7ae1d1f9611cd91524d03c53c5246b36ac8577` | `6aabfdd57e0f597d5485b9ed137dd772508fb353e2bc89db9e8baaf4433732be` |
| [Prompt-rewriter README](prompt_rewrite/README.md) | [QwenLM prompt_rewrite README](https://github.com/QwenLM/Qwen-Image-2.1/blob/fb7ae1d1f9611cd91524d03c53c5246b36ac8577/prompt_rewrite/README.md) | `fb7ae1d1f9611cd91524d03c53c5246b36ac8577` | `b33b7db6f498edacb0df3712e9e49a1aec2f56488ccd4127d4b96f71eb7c03d2` |
| [License](LICENSE) | [QwenLM repository license](https://github.com/QwenLM/Qwen-Image-2.1/blob/fb7ae1d1f9611cd91524d03c53c5246b36ac8577/LICENSE) | `fb7ae1d1f9611cd91524d03c53c5246b36ac8577` | `8dc973f024ff95966bea25866efa443fd16776dcb1001e681e3d467ea572b28d` |

The `prompt_rewrite/README.md` path preserves the release README's relative directory link. The earlier [flat snapshot](prompt-rewrite-readme.md) remains as a byte-identical compatibility copy. The archived source documents have not been rewritten.

The model card and QwenLM release README cover text-to-image, image-conditioned editing, up to 10 reference images, local edits guided by circles, painted annotations, or masks, and native RGBA. The release README includes Diffusers examples for generation, single-image editing, multiple references, and transparent output.

The prompt-rewriter README describes two separate fine-tuned Qwen3.5-VL checkpoints, one for text-to-image and one for editing. It accepts prompts in any language. Its text-to-image checkpoint returns a detailed English prompt. Its edit schema uses ordered `input_images` and labels references as `<image1>`, `<image2>`, and so on. Those labels belong to the companion prompt-rewriter contract; they are not Qwen-Image-2.1 pipeline input syntax or proof of support in another entry.

## Read only the source needed for the task

- For model scope and metadata, read the model card.
- For inference inputs, editing examples, reference images, or RGBA prompts, read the QwenLM release README.
- For the companion prompt rewriter's input and output contract, read the prompt-rewriter README.
- Read `LICENSE` when license terms matter. It contains the Qwen Research License Agreement released 2026-09-20.

These are model and open-source pipeline facts. The active local entry was not identified or tested during this archive task. Do not infer its upload fields, reference order, image limit, mask controls, or alpha output from these documents. The workspace's `<image1>` label convention belongs to a local edit entry and is not a Qwen model requirement; confirm the active route before applying it.

The archived Qwen sources do not provide a front-facing, flat-foot squat recipe or guarantee that result. They do not establish that English prompts outperform Chinese. Treat these as unverified prompt or output questions, not official specifications.

## Prompt-enhancer instructions retrieved 2026-09-30

The following unchanged text snapshots were retrieved from the official Qwen checkpoint repositories. Dates use Asia/Shanghai. The [enhancer source manifest](pe-sources.json) records pinned retrieval URLs, revisions, byte counts, and hashes. The older release snapshots above remain unchanged.

| Local snapshot | Official source revision | SHA-256 |
| --- | --- | --- |
| [T2I system prompt](pe-t2i-system-prompt.txt) | [Qwen-Image-2.1-PE-T2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I/blob/f3ed7985c788ad75b3ab7223e0c4c51e2a43545b/system_prompt.txt) | `a77c9a06c59b120741141d9514b95682bb8761d02bec49ca61def7b2b3d9fb99` |
| [I2I system prompt](pe-i2i-system-prompt.txt) | [Qwen-Image-2.1-PE-I2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I/blob/72927bc08afc99b7888ceb7d7d51a12db3700bbd/system_prompt.txt) | `e378fea686a1431581ba4c654d332ae96adad633f144ae738ec8ce9c4fd66439` |

Read T2I for inventory and finished-image writing order. Read I2I for operation-first editing, preservation, language decisions, and reference roles. Their exact schemas belong to the separate enhancer checkpoints. They do not prove the active image entry supports those fields or that an image-model language performs better. The [local writing guide](../writing.md) applies the relevant distinctions without replacing Oneirloom's user-facing output contract.

The official Qwen blog link was found at [Qwen-Image-2.1: Compact, Efficient, and Unified Image Creation](https://qwen.ai/blog?id=qwen-image-2.1). The browser open timed out, and a direct HTML request returned only the generic Qwen page shell without the article text. No blog snapshot was saved; the capability claims above rely on the archived model card and release README. This was a page-fetch limitation, not an access denial.
