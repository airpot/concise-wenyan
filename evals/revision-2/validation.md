# Revision 2 validation

Date: 2026-10-06 (Asia/Shanghai).

## Scope and method

The refinement addresses explicit protection of negation and scope, literary calibration examples, context-first and condition-first English model instructions, and separate semantic/style evaluation. The five original scenarios recur unchanged; four new scenarios test scope and units, unfamiliar concepts, command context, and literary rewriting.

There are eighteen semantic criteria and nine style criteria. Fresh executors receive only the trial's skill and the scenarios. Independent evaluators receive only the scenarios, criteria, and actual answers. No scenario commands, production operations, or account actions are executed.

## Retained results

| Trial | Semantic pass | Semantic fail | Style pass | Style fail |
| --- | --- | --- | --- | --- |
| Initial skill baseline | 16 | 2 | 9 | 0 |
| First refinement | 17 | 1 | 9 | 0 |
| Before final style repair | 18 | 0 | 7 | 2 |
| Final refinement | 18 | 0 | 9 | 0 |

The final trial passed all eighteen semantic criteria and all nine style criteria. Full verdicts and quoted evidence are retained in `scores-final.json`. Source format, literal preservation, local Markdown links, and installation hashes were checked separately.

Baseline failures concern treating a tentative log event as established in a paraphrase, and replacing a prohibition on retry with a statement that retry is unnecessary. The first refinement still lost the log event's uncertainty. The semantic repair keeps uncertainty in every restatement, including text outside the preserved quote.

Editorial review also found that “not required” had become “unnecessary.” The first evaluator accepted that wording under the broad criterion. The source now explicitly distinguishes those meanings; the saved before/after answers retain this stricter editorial finding.

The later style evaluator rejected a largely modern Chinese clause in a mixed-language response, and a concept defined after its first mention. The skill now explicitly applies literary phrasing to the Chinese part of a mixed response and permits an inline first-use definition in the opening conclusion.

The after-modal-fix executor trial is retained, but its evaluator returned an acknowledgement after an input-path update rather than structured scores. Its text is saved in `evaluator-after-modal-fix.txt`; no criterion count is inferred from that acknowledgement.

## Evidence

- `baseline-skill.md` and `baseline.json`: exact initial skill and actual baseline responses.
- `forward-initial-skill.md`, `forward-initial.json`, and `scores-initial.json`: first refinement and its independent scores.
- `forward-after-modal-fix-skill.md` and `forward-after-modal-fix.json`: retained intermediate executor trial.
- `forward-before-style-fix-skill.md`, `forward-before-style-fix.json`, and `scores-before-style-fix.json`: semantic pass with two style failures.
- Root `SKILL.md`, `forward-final.json`, and `scores-final.json`: final source, complete answers, and independent final scores.
- `provenance.json`: source/input/output SHA-256 hashes and known executor IDs.

## Limits

These are single offline writing trials, not statistical performance tests or live execution. Literary style is subjective: the two evaluators applied different strictness to readable modern Chinese clauses. A passing style score is not evidence that the user has approved every sentence. Model versions were inherited and not identified by returned metadata. No token-saving or cross-product discovery claim is made. Historical initial evaluation files remain evidence for the original commit only.
