---
name: concise-wenyan
description: "Use when Chinese reports, explanations, recommendations, or progress updates need concise literary Chinese, or related model instructions need English, with the complete ASD-STE100 foundation."
---

# Concise Wenyan (简辞)

Use the complete ASD-STE100 Issue 9 foundation. Use literary Chinese for the human reader. Use STE English for model instructions. Preserve the syntax of computer inputs.

The objective is **辞简意足，一读即明**. Meaning comes first. This skill controls expression. It does not give authority to do a task.

## Load the foundation

Read [the complete implementation reference](references/ste-issue9.md). It covers all 53 rules, the eight general recommendations, and dictionary review.

Use the official standard as the authority. The implementation reference does not replace the standard or its dictionary.

Read the applicable official sections and the dictionary introduction. Review vocabulary against Part 2. Reuse verified reference evidence for the same issue and sense.

Use [the reference helper](scripts/ste_reference.py) for source access:

```text
python scripts/ste_reference.py fetch
python scripts/ste_reference.py section dictionary-intro
python scripts/ste_reference.py section 5
python scripts/ste_reference.py lookup test wear above should
```

Run these commands from the skill directory. The helper keeps the official source in a local cache. It does not certify sentences.

If source evidence is unavailable, use another reader for the official PDF. If verification remains incomplete, report that limitation. Do not claim complete compliance.

## Build the English foundation

Identify the reader, passage type, facts, conditions, and required format. Separate procedures, descriptions, safety instructions, and protected material.

Prepare an English content draft. Apply every relevant STE rule before you select the output language. Do not publish this intermediate draft unless the task requires it.

- Check dictionary approval, part of speech, meaning, forms, and restrictions for each authored English word.
- For technical terms, check the applicable noun or verb category. Do not use technical terminology as a general exemption.
- Use the permitted verb constructions. Use active clauses. Use passive description only when its actor is unknown.
- Keep ordinary noun groups within three words. Introduce longer official names before an explicit shorter form or justified grouping.
- Keep procedural and safety sentences within 20 STE words. Keep descriptive sentences and note sentences within 25 STE words.
- Keep each descriptive paragraph within six sentences and one topic. Use the official word-count conventions.
- Put conditions before commands. Give one sequential instruction per sentence. Preserve simultaneous actions as simultaneous.
- Put negative conditions and exceptions before prohibitions too. Do not leave an `unless` condition after its command.
- Give notes as information only. Put an action in its work step or applicable safety instruction.
- For a supplied hazard, preserve its risk level, avoidance action, and consequence. Do not invent hazards.
- Retain necessary grammar and clear connections. Do not use contractions, semicolons, or new phrasal-verb meanings in STE prose.

Complete the rule review with the reference ledger. For an audit, record evidence for every rule and dictionary use. Give a reason for each inapplicable rule. Mark missing evidence as unresolved.

## Select the presentation

**Human reader:** Render the reviewed content as readable literary Chinese. Preserve modern technical terms. Use common constructions such as 已、尚、须、宜、若……则、惟、未可.

**Model or agent:** Output the reviewed English. Establish the host, directory, inputs, and prerequisites before the steps that need them. Each instruction must stand alone.

**Computer:** Preserve code, commands, paths, identifiers, payloads, labels, and required quotations. Their protocol controls their syntax. Do not translate Chinese keys or data.

**Mixed readers:** Select the language for each passage. Apply the full literary style to each Chinese passage. Keep model instructions in English.

An explicit task language or required format takes precedence. If an audit is requested, disclose any resulting STE deviation.

English vocabulary, inflections, articles, punctuation, and word counts apply to the English foundation. They do not become Chinese character limits. Chinese punctuation is permitted in the human rendering.

## Check meaning and presentation

Compare both drafts with the source. Preserve actors, actions, quantities, units, sequence, causality, conditions, exceptions, negation, and scope.

Keep uncertainty in every restatement. Do not turn a possible cause into a finding. Do not extend local evidence to production.

Keep advice, obligation, permission, and possibility distinct. A dictionary alternative does not permit a change in meaning.

Do not replace advisory `should` with binding `must`. Reconstruct the advice with approved wording. “Not required” does not mean “unnecessary” or “forbidden.”

Make Chinese referents clear. Explain an unfamiliar concept at first use when the reader needs it, including in the opening conclusion.

Remove padding and decorative allusions. Do not delete necessary relations to imitate ancient prose. If a literary phrase is ambiguous, use clearer Chinese.

Assess meaning, STE foundation, and presentation separately. A style pass cannot repair a semantic failure. Chinese rendering is not formally STE English.

Return the requested content without routine audit commentary. Report a material verification gap when it affects the task or a compliance claim.

## Calibration

| Source meaning | Incorrect rendering | Faithful rendering |
| --- | --- | --- |
| Local tests pass. Production is unverified. | 测试皆过，线上可用。 | 本地测试皆过。线上尚未核验。 |
| The cause is possible. | 根因为缓存过期。 | 缓存或已过期，惟根因未明。 |
| Immediate restart is not mandatory. | 无须立即重启。 | 并非须立即重启。 |
| A parser repair is complete. | 目前已完成针对解析器问题的修复工作。 | 解析器之误已修。 |

Model example:

> If the version is 2, do the local test. If the test fails, stop the procedure. Keep the existing file.

Keep the version condition, test meaning, failure branch, and file boundary when you render this example for a human reader.
