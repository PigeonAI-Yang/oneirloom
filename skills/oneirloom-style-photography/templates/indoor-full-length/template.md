# Indoor full-length portrait

## Selection

Use for an upright head-to-shoe portrait in a readable interior. Do not select it for a close-up or impose the recorded bedroom on another requested setting.

## Visual anchors

Keep the whole person and footwear inside the frame, with visible floor support and natural perspective. Place the person and major room objects in explicit relative positions. Describe the light direction and material colors separately so the room remains readable.

## Adjustable slots

Set identity, clothes, pose, room, object arrangement, regional colors, and light from the brief or reference. The historical sample's age, ethnicity, hairstyle, black dress, bedroom, seed, and model belong to that example. They are not mandatory template defaults.

## Prompt scaffold

Resolve every slot and deliver the languages required by the router. This generalized scaffold was created during the architecture migration and has not been generation-tested.

```text
一张{画幅比例}的室内全身摄影人像，人物从头顶到鞋底完整入画，头顶与脚下留少量空间，人物位于{画面位置}。相机位于{相对人物的高度}，朝向{拍摄方向}，人物上下比例自然。场景为{室内环境}，{主要物件及其左右、前后位置}，人物站在{与物件的空间关系}。{人物身份与外观}，穿着{服装结构、材质、颜色和鞋履}。人物{站姿、双脚间距、手臂与双手位置}，头部{朝向}，目光{方向}，神态{表情}。{光源}从{方向}照入，{人物与环境中具体的明亮区和阴影区}。{肤色、衣服、家具和地面的区域色彩}，五官、头发与衣料细节清楚，背景家具保持可辨认的轮廓。
```

## Examples

| ID | Role | Image | Exact prompt and settings | Verification |
| --- | --- | --- | --- | --- |
| result-01 | Generated output, not an input reference | [Original PNG](images/result-01.webp) | [Archived run record](example-01.json) | Inspected during migration; complete framing and room layout are visible, but the feet are closer together than requested |

The record preserves the actual Chinese prompt and local Qwen execution settings. The image was copied without alteration from the existing tutorial evidence. It demonstrates that recorded prompt, not the generalized scaffold above. No new generation was performed.
