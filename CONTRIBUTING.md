# 维护规则

- Keep the main skill concise. Add a method skill for a distinct medium or model and update the main skill's routing table.
- 一个模型档案对应**精确版本 + 入口 + 任务模式**。将 `official_documented`、`observed_local`、`hypothesis`、`unknown` 分开写；官方事实附 URL 和核验日期，观察附入口、参考图、设置、结果及对照。
- 只在同条件对照后把“某语言／长度更好”提升为经验。不能把 Krea 托管控件当作开放权重接口，也不能将模型支持能力直接当作第三方界面能力。
- 示例以独立完整提示词结束；默认不输出负面词和正文排除句。输出的实际画内文字（如海报上的“NO SIGNAL”）不属于排除指令。
- When changing model facts, revisit official sources and update the verification date.
