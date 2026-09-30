# Vintage halftone portrait cutout

## Selection

Use for portrait edits in a black-and-white newspaper cutout collage style. Apply the rendering treatment to the supplied person image while preserving recognizable identity, facial and body geometry, expression, pose, crop, hairstyle, and accessories. Change only elements the user explicitly asks to change.

## Visual anchors

Render the portrait as crisp black and paper-white shapes with a regular circular halftone screen. Vary dot size and density with the source luminance so the face remains readable, especially around the eyes, nose, and mouth. Keep the dot pattern regular, with subtle aged print and paper texture confined to the cutout. Give the subject a natural cut-paper silhouette; a narrow off-white paper edge is optional.

Default to one isolated subject on a transparent canvas: only the cutout is visible, with the canvas empty and transparent outside its silhouette. Keep all paper and ink texture within the cutout. Add scenery, a backdrop, lettering, or a shadow only when explicitly requested. Treat transparency as the intended output state and verify the active entry's alpha support before claiming an RGBA result. For Qwen-Image-2.1, follow the entry-specific guidance in `oneirloom-model-qwen-image-2-1`.

Deliver a complete Chinese prompt followed by its equivalent English version in separate copyable blocks, with labels outside, unless the current request explicitly asks for one language. Use affirmative descriptions of the target image. For Qwen-Image-2.1, load `oneirloom-model-qwen-image-2-1` and use the active entry's confirmed ordered image labels, assigning identity and style roles to actual inputs. A text-only request must not invent reference-image labels.

## Adjustable slots

Use the supplied portrait as the identity and geometry source. Adjust dot scale, paper aging, and optional paper edge to the request. Preserve the default transparent canvas unless the user requests another background. Image inputs and alpha controls belong outside the prompt. If no portrait is supplied, obtain it for an edit or follow an explicit request to create a new subject.

## Prompt scaffold

Resolve all slots from the request and actual inputs. The scaffold is not a historical run prompt; deliver the equivalent English version when required by the router.

```text
将输入人像转换为复古黑白报纸网点剪纸拼贴。保留原图人物可辨认的身份、面部与身体几何结构、表情、姿态、取景范围、发型和配饰。以清晰的黑色与纸白色块塑造人物，用规则圆形网点表现明暗，网点大小与密度随原图亮度变化，眼睛、鼻子和嘴部保持清楚可读。采用{网点尺度与轻微旧印刷质感}，让纸张肌理与油墨纹理分布在人物剪影内部，人物外轮廓呈自然剪纸边缘{按需求补充窄米白纸边}。{背景目标，默认剪影外的画布为空且完全透明}，整幅呈现单个人物的完整剪纸图层。
```

## Examples

No source portrait or generated result is associated with this migrated template. The scaffold and alpha output are untested. Do not present a white-background image as verified transparency.
