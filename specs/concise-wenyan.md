# Concise Wenyan (简辞)

## Accepted intent

Apply the complete ASD-STE100 Issue 9 foundation before selecting the presentation language. Use concise Chinese with a substantial, readable literary register for reports and explanations addressed to the user. Write newly authored instructions addressed to models or agents in STE English. Preserve complete meaning while reducing unnecessary wording.

## Scope

The skill controls expression, not task authority or implementation workflow. Explicit task language and required formats take precedence. Preserve code, paths, identifiers, structured payloads, and quotations. A mixed response follows the language of each section's reader.

## Deliverables

- `SKILL.md`: self-contained English instructions and Chinese examples.
- `agents/openai.yaml`: display name 简辞 and an invocation prompt.
- `evals/`: saved scenarios, executor answers, and a bounded validation record.
- A verified personal Codex installation if no different installation already exists.

## Acceptance

- Chinese prose has clear literary phrasing without obscure words or decorative allusions.
- Actors, conditions, numbers, exceptions, causal relations, and uncertainty remain clear.
- Agent instructions are complete English instructions, even inside a Chinese report.
- Technical strings and exact quotations remain unchanged.
- Complex explanations retain necessary detail. English foundation sentences follow the applicable 20/25-word limits and descriptive paragraphs follow the six-sentence limit. There is no fixed total response limit or Chinese character quota.
- Format validation and realistic behavioral examples are recorded separately. No universal reliability or token reduction claim follows from a small evaluation.

## Accepted refinement (2026-10-06)

The user approved four improvements after reviewing related writing skills:

1. Explicitly protect negation, exclusivity, exceptions, units, and recommendation strength during compression. Check these against the source before sending.
2. Calibrate literary phrasing with short positive and negative examples. Keep semantic errors distinct from stylistic defects, and preserve the chosen substantial literary register without imposing character quotas.
3. Strengthen English model instructions: establish required context before steps, put conditions before actions, name failure branches, and briefly explain unfamiliar concepts only when the reader needs them. Do not merge distinct technical terms for cosmetic uniformity.
4. Evaluate semantic preservation and style in separate columns. Retain per-case evidence and interpretation limits. A semantic pass is required even when the prose sounds good; stylistic compliance cannot establish user preference without user feedback.

The preceding refinement did not add modes, dependencies, automatic authority, or fixed response-length limits. It is retained as historical scope. The following clarification supersedes its STE boundary.

## Complete foundation clarification (2026-10-06)

The user explicitly requires the complete STE foundation, with literary Chinese only as the human presentation layer. Implement all 53 rule checkpoints, the eight general recommendations at their proper advisory status, and Part 2 dictionary review of words, senses, parts of speech, forms, and usage notes.

Apply procedural, descriptive, and safety rules according to passage type. Preserve allowed exceptions, including simultaneous actions, long official technical names, and passive descriptions with unknown actors. Do not strengthen recommendations, invent actors, or change data to satisfy a surface rule.

The official Issue 9 source is downloaded to a private cache and verified by SHA-256. Publish an original rule-coverage ledger and a helper for source reading and exact dictionary-row lookup. Do not redistribute the official PDF or dictionary. PyMuPDF is needed only for the helper's PDF reading; another capable reader can provide equivalent official evidence.

Chinese rendering preserves the English foundation's semantics and structure, but is not labeled formally STE-compliant English. Required computer formats and verbatim strings remain exact. Missing source/dictionary verification is unresolved rather than successful compliance. Preserve historical evaluation versions. Verify the new source, synchronize the personal installation, and push to the authorized repository.
