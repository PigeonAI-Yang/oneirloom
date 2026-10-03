---
name: vpd-color-light
description: 把色彩、明度、对比、光向、材质受光和空气感转成区域明确的图像提示词。用于修正偏灰、偏冷、过曝、光色错位或“鲜活梦幻”等抽象氛围。
---

# 色彩与光线

1. 分区域标注主体、背景、天空、云、暗部和高光。分别描述色相、明度、饱和度；整图一个“低饱和”标签会抹平冷暖关系。
2. 明确光源方向、软硬、环境补光、阴影深浅、色彩反射和材质响应。`柔光`控制边缘，`亮`控制明度，`发光`可来自局部晕染；三者不可互换。
3. 将氛围和色彩机制分开。“鲜活”可通过区域色相区分、暖色中间调、动作与表情建立；“梦幻”也可在深色场景中由发光体和空间层次产生。
4. 描述暗部支点与亮部过渡。例如黑发保持深色体积，皮肤中间调暖亮，云层亮处呈奶油杏桃色。避免全局调色命令与矛盾的明暗要求。

最小修正：当天空、肤色一起偏青时，只改区域色彩句，固定人物、构图、服装与裁切；下一轮检验区域是否分开。

For reference reconstruction and color correction, compare the source and result by large visual regions. Distinguish a material's underlying base hue from its visible color under the scene's illumination. Match the observed colors of skin, light fabrics, colored surfaces, and shadows; preserve the material's identity without restoring its neutral-light appearance. A cool or warm overall impression is not an instruction to tint every region. When color alone misses, revise regional color wording while preserving the matched pose, wardrobe, objects, and framing.

For portrait reference reconstruction, infer the dominant light direction and elevation from visible evidence. Compare lit planes with cast shadows, preserve the observed key/fill relationship, and compare subject exposure with the nearby background. If the user specifies an overhead stage key, keep it dominant without naming an unsupported fixture; do not replace broad colored illumination shown in the source with neutral frontal fill or uniform warm skin. Distinguish a material's base hue from its apparent color under light, and broad colored illumination from a rim highlight. Use regional color notes to inspect the source and result, then condense them into a few supported prompt cues for light direction, relative key/fill, exposure, and decisive highlights and shadows across the subject and surroundings. Retain distinctive source colors and user-requested hues, including regional color when supported. Do not turn every region into an independent color instruction or add unexplained patches. If a result looks separately lit, check frontal brightness, key/fill balance, colored illumination, and background exposure before adding rim light.
