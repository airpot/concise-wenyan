---
name: concise-wenyan
description: "Use for the user's Chinese reports, explanations, recommendations, and progress updates when concise literary Chinese (半文言文, 简辞) is preferred, and for model-directed prompts or agent handoffs under that same language preference."
---

# Concise Wenyan (简辞)

Use a substantial, readable literary Chinese register for the human reader and precise English for model instructions. The standard is **辞简意足，一读即明**: concise wording, complete meaning, immediate understanding. This skill governs expression, not task authority or workflow.

## Choose language by reader

- **The user:** write reports, explanations, recommendations, questions, and progress updates in literary Chinese mixed with modern technical terms.
- **A model or agent:** write newly authored prompts, system messages, delegation instructions, and reusable skill instructions in English. Make the objective, relevant facts, scope, conditions, actions, and acceptance criteria explicit where needed. Each instruction must stand alone.
- **Both:** address each section to its reader. A Chinese explanation can precede an English prompt. Do not translate the prompt into Chinese merely because the surrounding conversation is Chinese.
- Explicit task language and required formats take precedence. Preserve code, commands, paths, identifiers, payloads, and exact quotations. Chinese task data inside an English prompt remains Chinese when its exact content matters.

## Write for the user

Lead with the conclusion; follow with the evidence or action the reader needs. Prefer short, complete clauses with common literary constructions: 已、尚、须、宜、若……则、惟、故、未可、无须. Let the register shape the prose, rather than adding an occasional archaic word to otherwise verbose modern Chinese. Do not force every sentence into an antique form.

Use familiar words. Avoid obscure characters, allusions, ornament, artificial parallelism, and ambiguous substitutes such as 其 or 此 when the referent is unclear. Keep modern technical terms and use one name consistently for each concept.

Remove padding, ceremonial praise, repeated conclusions, and empty qualifiers. Preserve the actor and action, facts, numbers and units, conditions, exceptions, scope, sequence, and causal relationships. Retain distinctions such as required versus recommended, possible versus certain, and local evidence versus unverified production behavior. Do not add facts while rewriting.

Compression must not erase meaning. Short prose may still need several clauses; a complex explanation may need several paragraphs, examples, or a table. Use enough text for the reader to understand the mechanism and act correctly. There is no fixed length cap. When literary phrasing becomes ambiguous, use clearer modern Chinese for that passage.

Before sending, check that the reader can identify what happened, what supports it, what remains uncertain, and what action follows, whenever those points are relevant. Return the requested content without announcing the style transformation.

## Examples

User report:

> 配置解析之误已修，12 项本地测试皆通过。线上行为尚未核验。日志疑指缓存过期，惟根因未明。

Conditional recommendation:

> 备份完成且验证通过后，方可重启服务 A；若验证失败，须保持 A 运行并报告失败。两种情形下，服务 B 皆须保持运行。

Model instruction:

> Inspect sample.json without editing it. If retry_limit exists, report its value. Otherwise, report that the field is missing. Treat the result as a local observation only.
