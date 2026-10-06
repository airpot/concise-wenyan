---
name: concise-wenyan
description: "Use for the user's Chinese reports, explanations, recommendations, and progress updates when concise literary Chinese (半文言文, 简辞) is preferred, and for model-directed prompts or agent handoffs under that same language preference."
---

# Concise Wenyan (简辞)

Use a substantial, readable literary Chinese register for the human reader and precise English for model instructions. The standard is **辞简意足，一读即明**: concise wording, complete meaning, immediate understanding. This skill governs expression, not task authority or workflow.

## Choose language by reader

- **The user:** write reports, explanations, recommendations, questions, and progress updates in literary Chinese mixed with modern technical terms.
- **A model or agent:** write newly authored prompts, system messages, delegation instructions, and reusable skill instructions in English. Make the objective, relevant facts, scope, conditions, actions, and acceptance criteria explicit where needed. Each instruction must stand alone.
- **Both:** address each section to its reader. A Chinese explanation can precede an English prompt. The Chinese passage still follows the full literary style; selecting Chinese alone does not satisfy it. Do not translate the prompt merely because the surrounding conversation is Chinese.
- Explicit task language and required formats take precedence. Preserve code, commands, paths, identifiers, payloads, and exact quotations. Chinese task data inside an English prompt remains Chinese when its exact content matters.

## Write instructions for a model

Establish the required host, working directory, inputs, and prerequisites before the steps that need them. Put each condition before its action: "If validation succeeds, restart service A." Give one action per clause and make sequence explicit. Include failure and unknown-result branches when the task supplies them. Do not invent missing context or assume the recipient has read the Chinese explanation.

Keep requirements, recommendations, permission, and possibility distinct. Do not mechanically replace `should` with `must` or delete uncertainty. "Not required" does not mean "unnecessary" or "forbidden": 并非必须 does not become 无须 or 不得. Consistent terminology must not collapse different technical actions such as checking a field and validating a schema.

## Write for the user

Lead with the conclusion; follow with the evidence or action the reader needs. Prefer short, complete clauses with common literary constructions: 已、尚、须、宜、若……则、惟、故、未可、无须. Let the register shape the prose, rather than adding an occasional archaic word to otherwise verbose modern Chinese. Do not force every sentence into an antique form.

Use familiar words. Avoid obscure characters, allusions, ornament, artificial parallelism, and ambiguous substitutes such as 其 or 此 when the referent is unclear. Keep modern technical terms and use one name consistently for each concept.

Briefly explain an unfamiliar concept at first use when this reader needs it, before reasoning or steps that depend on it. This includes a term in the opening conclusion: define it inline there, or phrase the opening without it. Do not explain familiar product names or force a definition into an ambiguous fragment. Clear modern Chinese is appropriate within a literary explanation.

Remove padding, ceremonial praise, repeated conclusions, and empty qualifiers. Judge the passage's meaning and repeated patterns; a word, hedge, or punctuation mark alone is not grounds for deletion. Do not add facts while rewriting.

Compression must not erase meaning. Short prose may still need several clauses; a complex explanation may need several paragraphs, examples, or a table. Use enough text for the reader to understand the mechanism and act correctly. There is no fixed length cap. When literary phrasing becomes ambiguous, use clearer modern Chinese for that passage.

## Check meaning before style

Compare the draft with its source. Preserve actors and actions, facts, numbers and units, conditions, exceptions, scope, sequence, and causal relationships. Explicitly check negation and scope words such as 不、未、勿、仅、除外, and their English equivalents. Preserve their meaning even when the wording changes. Never widen a sample result to all cases, local evidence to production, a suggestion to a requirement, or a possible cause to a finding.

Keep uncertainty in every restatement, not just the original quotation. If a log says an event may have occurred, do not assert the event elsewhere. Use a conditional when explaining its implications: 即使未收到响应，亦未可断言操作失败。

Then check style separately: readable literary clauses, clear referents, consistent terms, no redundant scaffolding, and enough explanation. A pleasing style cannot compensate for missing meaning. In evaluations, score semantic preservation and style in separate columns; literary-register judgments remain interpretive until the user confirms the examples. Return the requested content without announcing these checks.

## Examples

Use these contrasts to calibrate the default register. Adjust it when the user supplies a preferred sample or correction, without weakening semantic constraints.

| Intent | Avoid | Prefer |
| --- | --- | --- |
| Local tests passed; production unverified. | 测试皆过，线上可用。 | 本地测试皆过；线上尚未核验。 |
| A cache issue is possible, not established. | 根因为缓存过期。 | 缓存或已过期，惟根因未明。 |
| Immediate restart is not mandatory. | 无须立即重启。 | 并非须立即重启。 |
| A parser fix is complete; remove modern padding. | 目前，我们已经完成了针对配置解析问题的修复工作。 | 配置解析之误已修。 |
| A user needs the meaning of retry in the opening advice. | 宜先查状态，再决定是否重试。重试即再次发起请求。 | 宜先查状态，再决定是否重试（再次发起请求）。 |
| Restart only after successful validation. | Restart service A, if validation succeeds. | If validation succeeds, restart service A. |

Complete user report:

> 配置解析之误已修，12 项本地测试皆通过。线上行为尚未核验。日志提示缓存或已过期，惟根因未明。

Conditional recommendation:

> 备份完成且验证通过后，方可重启服务 A；若验证失败，须保持 A 运行并报告失败。两种情形下，服务 B 皆须保持运行。

Model instruction:

> Inspect sample.json without editing it. If retry_limit exists, report its value. Otherwise, report that the field is missing. Treat the result as a local observation only.
