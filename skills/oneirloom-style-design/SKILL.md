---
name: oneirloom-style-design
description: Compose prompts for posters, text layouts, products, packaging, 3D renders, and physical craft mockups. For creative ads based on a supplied product image, use product art direction before choosing a style or template.
---

# Graphic, product, and 3D design

平面、产品与三维设计类提示词的方法技能。本技能是判断规则库，按清单检查；具体设计配方在 templates。

## When to use

- 海报、文字版式、产品、包装、3D 渲染、实体工艺样机
- 基于实物产品图的创意广告：先走 [product art direction](../oneirloom-product-art-direction/SKILL.md)，再选表现手法或模板

## Method checklist

- 先识别用途和验收重点：海报是文字层级、对齐、留白和元素顺序；产品是完整轮廓、标识位置、材质和使用场景；三维是几何、表面、反射、灯光和空间关系。
- 画内文字用引号逐字提供，说明位置、大小和排版层级；“NO SIGNAL”等文本内容应原样保留。文字准确性依赖具体模型与入口，重要文字应在生成后核验。
- 产品标志不能仅靠艺术风格词控制。不要给海报无端增加景深和人物皮肤细节，也不要把三维材质写成不相容的真实摄影材质。

## Templates and references

- 按输出品类读取 [设计风格表](references/styles.md)。
- 其他可复用的产品、海报、版式、材质或工艺构造：读 [template index](templates/index.md)，只读匹配的模板。内容参考与构图或材质处理分开；适配呈现方式时保留主体的身份与结构，包括产品包装与文字。无匹配模板时按上面的方法自组。
- 先检查示例图再描述其效果；风格参考图不证明库存提示词生成过它。

## Output and handoff

交付完整提示词；画内文字保持逐字，重要文字提醒生成后核验。基于产品图的广告交付后，按 product art direction 的结果检查回看。生成结果偏差时转 `oneirloom-result-diagnosis`。
