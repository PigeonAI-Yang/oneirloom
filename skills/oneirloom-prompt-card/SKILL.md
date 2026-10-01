---
name: oneirloom-prompt-card
description: "Create a 3:4 vertical card from an existing image and complete prompt. Crop the image to fill the upper third, and typeset the prompt in the lower two thirds. Use for image-and-prompt collages, prompt cards, or Oneirloom prompt sharing layouts."
---

# Image and prompt card

把已有成品图与完整提示词排成一张可分享卡片的渲染技能。本技能只渲染既有内容；写作新提示词仍归摄影与设计方法。

## When to use

Use this Oneirloom child skill when the user asks to combine an existing image and prompt into one shareable graphic. Recognize requests for a prompt card or an image paired with its prompt. This skill renders existing content; the photography and design methods remain responsible for writing new image prompts.

## Fixed layout

- The output is one 3:4 portrait PNG. Use a 1800 by 2400 logical canvas and render at 1.5 scale for a 2700 by 3600 PNG.
- The image region is the full-width upper third, from the top edge to exactly one third of the total height. Fill it with a proportional `object-fit: cover` crop. Crop the image to fit this region, retaining an identifiable focal point. For a mirror selfie, prioritize the face, camera and upper outfit when the wide crop cannot include the whole body.
- The prompt region is the full-width lower two thirds. Place any modest title and all text padding inside this region. Typeset the complete selected prompt here. Keep the region split fixed while fitting the text.
- Use a plain light text background, dark type and clear paragraph spacing. Keep decorative labels subordinate to the prompt. Preserve the source image's colors and geometry apart from the proportional crop and the signature overlay below.

## Approved signature

- Default to the approved [woven creature signature with white lettering and black outlines](assets/oneirloom-woven-signature-white-black-outline.png). The lettering reads "织梦师" with "Oneirloom Skill" beneath it. The creature sits behind the overlapping Chinese lettering, with blue threads woven into the strokes. Both language lines and the long calligraphic flourishes have black outlines. Use this packaged transparent PNG without redrawing it.
- Prefer this white-letter version on both light and dark backgrounds. Switch to another version only when the user requests it or inspection shows a specific readability problem. If black lettering is requested, use white outlines around its Chinese text, English caption, and flourishes. The current black-letter gray-background preview is not a transparent watermark asset. The older text-only [white](assets/oneirloom-signature.png) and [black](assets/oneirloom-signature-black.png) assets remain available for explicit requests.
- Set the watermark width to 20 percent of the card width and preserve its native aspect ratio. The packaged square asset is 360 by 360 logical pixels on the 1800 by 2400 canvas. Keep the top and right margins at 36 logical pixels, both equal to 2 percent of the card width. The final export uses a 540 by 540 watermark and 54-pixel margins.
- Use 90 percent opacity. The black outlines provide contrast without an added shadow. Keep the surrounding background transparent, with no panel or border. The complete overlay stays inside the image region and does not enter the prompt region.
- The renderer applies these defaults automatically. Keep the approved design and placement unless the user explicitly requests a change. Inspect the actual output for readability and subject overlap; report any unresolved conflict with the fixed placement.

## Workflow

1. Select the latest confirmed image and prompt from the conversation. A new attachment replaces the previous picture for the card unless its role is explicitly different. When the user refers to a known template, use its current prompt rather than a superseded archive. Use the requested language; otherwise use the complete Chinese version for a Chinese conversation.
2. Inspect the image and choose the crop position. Read the actual prompt file. Preserve its wording, paragraph order and values, including any generation aspect ratio. Card composition does not authorize rewriting or shortening the prompt. An output image paired with a prompt does not establish which exact prompt or model generated it.
3. Render with [scripts/render_card.py](scripts/render_card.py) using local HTML, Playwright and an available Chromium browser. The renderer adds the approved signature automatically. Copy the original image and exact signature PNG into the output folder and keep editable HTML and prompt text beside the card. Rendering requires the existing Python Playwright and Pillow packages; use an installed browser executable when available.
4. Check the actual rendered geometry: 3:4 canvas, cropped upper image region exactly one third high, lower text region exactly two thirds high, every prompt paragraph inside that lower region, and rendered prompt text equal to the selected source. Verify the signature's upper-right position, proportional size, margins, opacity and source hash. Fit the font within the text region; an inability to fit the complete text is a gap to report, not permission to shorten it or enlarge the image region.
5. Inspect the PNG for crop focus, signature readability and subject overlap, legible text, paragraph order and clipping. Fix the crop or text fitting within the fixed split when required. Deliver the PNG inline with a clickable file link. State material omissions or unverified outcomes only when present.

## Renderer

```powershell
python '<skill directory>/scripts/render_card.py' --image '<source image>' --prompt '<current prompt text file>' --output '<new output directory>' --title '<short title>' --image-y 6 --browser 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
```

`--image-y` sets vertical `object-position` as a percentage from 0 to 100. Choose it from the inspected image; 6 is the crop used for the current hotel-selfie case, not a universal portrait setting. Horizontal positioning stays centered. Omit `--browser` to use Playwright's installed Chromium. Output folders must be new so previous versions remain intact.

The renderer saves `prompt-card-3x4.png`, `card.html`, `photo` with the original extension, the default watermark as `watermark.png`, `prompt.txt` and `render-checks.json`. The HTML references the archived signature so the output folder remains self-contained. The checks record the actual geometry, signature placement, selected version, sampled background brightness, source-image hash and signature hash. Background brightness is diagnostic and does not trigger a color switch. These checks do not prove visual quality until the PNG is inspected.
