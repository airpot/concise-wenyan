# 简辞 · concise-wenyan

一项 agent 写作技能：**对人以文言简述，对模型以英语明令。** 辞简意足，一读即明。

向用户汇报、解释或建议时，以常见文言组织短句，现代术语守原。事实、条件、数字、例外与不确定性皆须保留。复杂事项仍须详述，篇幅随理解所需而定。

向模型或另一 agent 下令时，用明确英语。若同一答复兼有汇报与任务指令，则各依读者选用语言。代码、命令、路径、结构化数据与原文引述保持原样。

## 示例

向用户汇报：

> 配置解析之误已修，12 项本地测试皆通过。线上行为尚未核验。日志提示缓存或已过期，惟根因未明。

向模型下令：

> Inspect sample.json without editing it. If retry_limit exists, report its value. Otherwise, report that the field is missing. Treat the result as a local observation only.

## 安装

先取仓库：

```text
git clone https://github.com/airpot/concise-wenyan.git
```

将 `concise-wenyan` 完整目录置于所用 agent 的技能目录。个人 Codex 可置于 `~/.codex/skills/concise-wenyan`，Claude Code 可置于 `~/.claude/skills/concise-wenyan`。其他 agent 须依其技能发现机制安置。

至少保留根目录 [SKILL.md](SKILL.md)；Codex 的界面元数据另见 [agents/openai.yaml](agents/openai.yaml)。当前会话若尚未识别，可刷新技能发现或新开会话再试。

## 调用

```text
Use $concise-wenyan for this report. Preserve every fact, condition, and uncertainty.
```

亦可用于混合输出：

```text
Use $concise-wenyan. Explain the result to me, then write a self-contained instruction for another AI to verify it.
```

技能保留正常自动选择；须明确使用时，以 `$concise-wenyan` 调用。具体任务所指定的语言与格式优先。

## 验证

本次修订补齐四处：否定与范围逐项核对；文言正反样例校准；英语指令前置背景与条件；语义、文风分栏评估。陌生概念须于读者需要时首次简释，既有术语不可为求整齐而混同。

新版评估复用五组原有样例，另增四组；十八项语义标准、九项语体标准皆通过。此前未通过的样例及修正过程亦保留，完整记录见 [本次评估](evals/revision-2/validation.md)。语体通过仅表明样例符合所列标准，仍须依用户反馈校准。

初版以五组离线文字样例、十五项标准评估。无技能基线通过十三项；加载技能后十五项皆通过。两处基线缺口皆为向模型下令仍用中文。

初版样例与完整答复留存于 [历史评估](evals/validation.md)。此为小规模文字检验；文言语感部分依判断，尚无跨模型可靠性或 token 节省量测。

## 设计依据

借鉴 [asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) 的表达纪律：短句、术语一致、条件明确、语义不失。此处另为中文文言语体设计，未宣称符合 ASD-STE100 英语标准。

需求与验收范围见 [specs/concise-wenyan.md](specs/concise-wenyan.md)。
