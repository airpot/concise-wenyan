# 简辞 · concise-wenyan

**以完整 STE 规则及词典为底层，对人作文言，对模型用英语；代码与数据守原。** 辞简意足，一读即明。

先据 ASD-STE100 Issue 9 整理英语内容，核对所适用的写作规则及词典用法，再按读者表达。向人汇报、解释或建议时，转为可读文言。向模型或另一 agent 下令时，输出经核对的 STE 英语。事实、否定、范围、条件、数字、例外及不确定性皆须保全。

## 完整底层

底层涵盖 Part 1 的五十三条规则、八项一般建议，以及 Part 2 对词性、词义、词形和受限用法的规定。一般建议仍属建议，不能冒作强制规则。程序、安全指令、描述及备注各依其适用条文核验。

英语程序与安全指令每句至多二十个 STE 词；描述及备注每句至多二十五词，描述每段至多六句。复杂事项可分句分段详述，全文无固定上限。文言依已核对的内容转换，不机械套用英文词数，亦不称中文为正式 STE 英语。

完整核对项及查阅法见 [底层参考](references/ste-issue9.md)。权威依据为 [官方 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)，非本仓库的摘要。官方 PDF 及词典缓存于个人机器，不随仓库再发布。

## 安装

```text
git clone https://github.com/airpot/concise-wenyan.git
```

将整个目录置于 agent 的技能目录。个人 Codex 可置于 `~/.codex/skills/concise-wenyan`，Claude Code 可置于 `~/.claude/skills/concise-wenyan`。其他 agent 依其技能发现机制安置。

运行时须保留 `SKILL.md`、`references/` 与 `scripts/`，不能仅复制入口文件。Codex 的界面元数据另见 [agents/openai.yaml](agents/openai.yaml)。

首次取官方原文，在技能目录运行：

```text
python scripts/ste_reference.py fetch
```

取件仅用 Python 标准库，核对固定 SHA-256，默认缓存于 `~/.cache/concise-wenyan/`。规则与词典查阅另需 PyMuPDF：

```text
python -m pip install PyMuPDF
python scripts/ste_reference.py section dictionary-intro
python scripts/ste_reference.py section 5
python scripts/ste_reference.py lookup test wear above should
```

亦可用其他 PDF 阅读工具查官方原页。原文缺失、哈希不符或词典核对未成，须明示未核验，不能报为完全符合。查询工具仅取原页证据，不自动判定句子合规。

## 调用

```text
Use $concise-wenyan. Apply the complete STE foundation and dictionary. Report the result to me in literary Chinese.
```

混合输出：

```text
Use $concise-wenyan. Explain the result in literary Chinese. Then write an English instruction for another AI. Apply the complete STE foundation.
```

自动选择仍保留；欲明确使用，以 `$concise-wenyan` 调用。任务指定语言与格式优先。命令、代码、路径、JSON 键及原文引述守原，不能一概英译。

## 验证

本次改为完整 STE 底层，规则覆盖、工具测试及离线文字评估见 [本次记录](evals/ste-foundation/validation.md)。语义、STE 用法与表达分别核验，词典查询与技能格式检查均不能代替完整合规审查。

[初版评估](evals/validation.md) 与 [此前修订评估](evals/revision-2/validation.md) 均属历史版本。本次不以其通过项数证明新底层。小样本亦不证明跨模型可靠性、普遍合规或 token 节省。

## 设计依据

初以 [asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) 为参照。用户现已明确要求完整规则为底层，故新版直接以官方标准及词典为准。

需求见 [规格](specs/concise-wenyan.md)，修订与验收步骤见 [实施计划](specs/ste-foundation-plan.md)。
