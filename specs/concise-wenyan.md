# Concise Wenyan (简辞)

## Accepted intent

Use concise Chinese with a substantial, readable literary register for reports and explanations addressed to the user. Write newly authored instructions addressed to models or agents in English. Preserve complete meaning while reducing unnecessary wording.

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
- Complex explanations retain necessary detail. There is no fixed sentence or response length cap.
- Format validation and realistic behavioral examples are recorded separately. No universal reliability or token reduction claim follows from a small evaluation.
