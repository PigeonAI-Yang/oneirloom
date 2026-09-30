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
2. 判断偏差来源是提示词语义、参考图用途、模型入口、画幅裁切还是生成随机性。若已有源图且用户只改局部，优先使用编辑任务与蒙版／参考通道（入口确认后），不要反复全文生成。
3. 修订：Treat the failed result as evidence of a miss, not as a replacement target. Preserve successful relations grounded in the source or user intent. Compare the revised prompt with the previously confirmed target specification for scale, crop, occlusion, and prominence; state any necessary coupled changes explicitly and preserve all other successful relations. Change only the requested main dimension when possible.
   - Check for globally scoped body-size terms when local fullness spills over. Revise those terms instead of layering negative "not fat" commands. Keep requested local fullness, the face and other features, camera, and framing intact.
4. 连续两轮受控修改仍不能解决同一关键偏差时，检查模型、参考通道、提示词增强、画幅和可控设置，不继续堆近义形容词。
5. 景别边界连续失准时，核对画幅比例、主体占比、姿势与其他构图要求是否冲突。若边界必须精确，按当前入口能力使用裁切、编辑或参考控制；合适时可在生成后裁切。区分模型直接生成的构图与后期裁切，不把后者记作提示词命中。

## Output and handoff

交付整合后的完整修正提示词，而非补丁。内部记录示例：`目标=天空与肤色冷暖分离；偏差=两者均偏青；修改=区域色彩句；保留=姿势、肩脸遮挡、服装；验收=暖肤与冷天分立且构图稳定`。不把一次偶然样本宣称为模型通则。
