---
license: other
license_name: qwen-research
license_link: LICENSE
pipeline_tag: text-to-image
tags:
  - diffusers
  - qwen
  - image-generation
  - image-editing
  - rgba
---

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/image2.1/logo.png" width="400"/>
</p>
<p align="center">
    🤖 <a href="https://modelscope.cn/models/Qwen/Qwen-Image-2.1">ModelScope</a>&nbsp;&nbsp;|
    &nbsp;&nbsp;🤗 <a href="https://huggingface.co/Qwen/Qwen-Image-2.1">HuggingFace</a>&nbsp;&nbsp;|
    &nbsp;&nbsp;📑 <a href="https://qwen.ai/blog?id=qwen-image-2.1">Blog</a>&nbsp;&nbsp;|
    &nbsp;&nbsp;🖥️ <a href="https://huggingface.co/spaces/Qwen/Qwen-Image-2.1">Demo</a>&nbsp;&nbsp;|
    &nbsp;&nbsp;🫨 <a href="https://discord.gg/BEYSk3pkSu">Discord</a>&nbsp;&nbsp;|
    &nbsp;&nbsp;💬 <a href="https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/assets/qr.png">WeChat</a>
</p>

## Introduction

We are excited to open-source **Qwen-Image-2.1**, a unified text-to-image generation and image editing model in the Qwen family. With just **7B parameters in its visual generation component** (32 Single-Stream DiT layers), Qwen-Image-2.1 balances generation quality, inference efficiency, and versatility.

Four key improvements define this release:

- **Compact and Efficient** — A lightweight architecture with mixed-granularity attention and prefix KV cache reuse delivers strong image quality at low computational cost.
- **Native Transparency, Unified Creation and Editing** — Generate regular or transparent (RGBA) images from text, edit transparent layers, and extract subjects from photographs—all in one model.
- **Versatile Editing** — Support up to **10 reference images**, specify local edits via circles, painted annotations, or separate masks, and preserve identity for people and products.
- **Realistic Textures and Refined Aesthetics** — Improved typography, portrait lighting, and fine details for more visually compelling results.

<p align="center">
    <img src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen-Image/image2.1/images/example-01.png" width="100%"/>
</p>

For more details, see the [GitHub repo](https://github.com/QwenLM/Qwen-Image-2.1) and [Blog](https://qwen.ai/blog?id=qwen-image-2.1).

## Quick Start

### Installation

```bash
pip install torch>=2.4.0
pip install transformers>=5.17
pip install git+https://github.com/huggingface/diffusers
pip install accelerate pillow
```

### Text-to-Image

```python
import torch
from diffusers import QwenImage21Pipeline

pipe = QwenImage21Pipeline.from_pretrained(
    "Qwen/Qwen-Image-2.1", torch_dtype=torch.bfloat16
).to("cuda")

image = pipe(
    prompt="A neon shop sign that reads \"QWEN IMAGE 2.1\", rainy night, reflections on wet pavement",
    width=2048, height=2048,
    num_inference_steps=40,
    generator=torch.Generator("cuda").manual_seed(42),
).images[0]

image.save("t2i_example.png")
```

### Image Editing

```python
import torch
from PIL import Image
from diffusers import QwenImage21Pipeline

pipe = QwenImage21Pipeline.from_pretrained(
    "Qwen/Qwen-Image-2.1", torch_dtype=torch.bfloat16
).to("cuda")

input_image = Image.open("input.png")

image = pipe(
    prompt="Change the background to a sunset beach",
    image=input_image,
    num_inference_steps=40,
    generator=torch.Generator("cuda").manual_seed(42),
).images[0]

image.save("edit_example.png")
```

### Transparent Image Generation (RGBA)

Use the recommended prompt format for transparent images:

```python
image = pipe(
    prompt="This is an RGBA image with transparency. A cute cartoon dragon sticker. The image has alpha channel and the background is transparent.",
    width=2048, height=2048,
    num_inference_steps=40,
    generator=torch.Generator("cuda").manual_seed(42),
).images[0]

image.save("transparent_example.png")
```

### Supported Aspect Ratios

```python
aspect_ratios = {
    "1:1":  (2048, 2048),
    "4:3":  (2400, 1792),
    "3:4":  (1792, 2400),
    "3:2":  (2528, 1696),
    "2:3":  (1696, 2528),
    "16:9": (2752, 1536),
    "9:16": (1536, 2752),
}
```

### Memory Optimization

```python
pipe = QwenImage21Pipeline.from_pretrained(
    "Qwen/Qwen-Image-2.1", torch_dtype=torch.bfloat16
)
pipe.enable_model_cpu_offload()
```

## Showcase

<p align="center">
<img src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen-Image/image2.1/images/example-04.png" width="30%"/>
<img src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen-Image/image2.1/images/example-05.png" width="30%"/>
<img src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen-Image/image2.1/images/example-06.png" width="30%"/>
</p>
<p align="center"><em>Native transparent image generation</em></p>

<p align="center">
<img src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen-Image/image2.1/images/example-15.png" width="100%"/>
</p>
<p align="center"><em>Group photograph generated from six portrait references</em></p>

<p align="center">
<img src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen-Image/image2.1/images/example-43.png" width="48%"/>
<img src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen-Image/image2.1/images/example-44.png" width="48%"/>
</p>
<p align="center"><em>Text rendering</em></p>

## License

This model is licensed under the [Qwen Research License Agreement](./LICENSE).
