---
name: oneirloom-result-diagnosis
description: 对比目标图、提示词与生成结果，找出构图、光色、主体、文字或表现形式的主要偏差，并输出保留成功部分的完整修正提示词。用于“跑偏了”“不像”“只改颜色”等迭代任务。
---

# Result diagnosis

对比目标、提示词与生成结果，找出主要偏差，交付保留成功部分的完整修正提示词。诊断时区分产生样本的模型/入口与期望的目标模型。

## When to use

- “跑偏了”“不像”“只改颜色”等结果迭代任务
- 已有生成结果与既定目标，需要判断主要偏差并修订提示词
- 反推、摄影、设计等方法的修正轮失准后转入本技能

## Workflow

1. 记录用户请求的改动、已确认的目标值、观察到的偏差、已经成功的画面部分、拟改的主要维度与验收标准。观察不可见时只基于用户描述，不假装看过结果。
   - For reference reconstruction, read `oneirloom-visual-analysis` and its reconstruction workflow. Compare source, complete submitted prompt when available, and result against the same mandatory structural anchors: held-object direction, visible grip, body-relative covering span, and garment coverage, openings, connectors, and layers. Check hosiery separately from shoes. Distinguish structural misses from aesthetic preferences; hidden details remain unknown.
2. 判断偏差来源是提示词语义、参考图用途、模型入口、画幅裁切还是生成随机性。若已有源图且用户只改局部，优先使用编辑任务与蒙版／参考通道（入口确认后），不要反复全文生成。
   - Attribute a miss only as far as the evidence permits. Without the actual submitted prompt, analysis, integration, and generation attribution remains unresolved; missing execution metadata leaves execution-specific causes unknown. The visible mismatch alone cannot locate the failed stage. When the submitted prompt is available, classify each relation separately: source-to-prompt omission or semantic mismatch, versus a clearly stated requirement not followed by the output. These can coexist in one result. For example, covering a skirt beside the hip mismatches a target of concealing the thigh-root region; a stated instep opening that appears filled is an output deviation, not a missing instruction. Execution-specific causes and which skill revision produced the prompt still require provenance; do not claim a patch was exercised without that evidence.
3. 修订：Treat the failed result as evidence of a miss, not as a replacement target. Preserve successful relations grounded in the source or user intent. Compare the revised prompt with the previously confirmed target specification for scale, crop, occlusion, and prominence; state any necessary coupled changes explicitly and preserve all other successful relations. Change only the requested main dimension when possible. Run the workflow's counterexample check on the complete revision in each delivered language; naming the missing prop or clothing category alone is insufficient.
   - Check for globally scoped body-size terms when local fullness spills over. Revise those terms instead of layering negative "not fat" commands. Keep requested local fullness, the face and other features, camera, and framing intact.
4. 连续两轮受控修改仍不能解决同一关键偏差时，检查模型、参考通道、提示词增强、画幅和可控设置，不继续堆近义形容词。
5. 景别边界连续失准时，核对画幅比例、主体占比、姿势与其他构图要求是否冲突。若边界必须精确，按当前入口能力使用裁切、编辑或参考控制；合适时可在生成后裁切。区分模型直接生成的构图与后期裁切，不把后者记作提示词命中。

## Output and handoff

Return the complete revision as concrete affirmative target states under the main skill's output contract. Replace abstract warnings, negated failed variants, and 'keep correct/consistent' with the intended visible shape, placement, coverage boundary, opening, connector, layering, or material. Keep counterexample tests and error/acceptance lists internal unless requested; requested diagnosis remains outside copyable generation prose. Explicitly requested or entry-required negative prompts use a separate field or block. Preserve matched source relations and leave hidden construction unknown.

交付整合后的完整修正提示词，而非补丁。内部记录示例：`目标=天空与肤色冷暖分离；偏差=两者均偏青；修改=区域色彩句；保留=姿势、肩脸遮挡、服装；验收=暖肤与冷天分立且构图稳定`。不把一次偶然样本宣称为模型通则。
