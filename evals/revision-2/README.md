# Revision 2 evaluation

Use the saved initial skill as the baseline and the revised root `SKILL.md` as the forward instructions. The original five scenarios recur unchanged, with four additional cases for scope, unfamiliar concepts, English execution order, and literary calibration.

Fresh executors receive only the respective skill and `scenarios.json`. Keep `criteria.json`, specifications, prior results, and intended answers outside executor inputs. Scenario instructions are simulated; do not execute their commands or mutate external systems.

A separate evaluator reads the scenarios, criteria, and complete actual answers. Score each criterion as `pass`, `fail`, or `not_assessable`, with a concrete quotation or omission. Report semantic and style scores separately. Literary-register judgments are interpretive, not word-count tests; do not manufacture baseline failures or claim that passing proves the user's preference.

Retain raw answers, scores, exact source hashes, and known executor IDs. Do not infer general reliability or token savings from these single trials. The earlier fifteen-criterion evaluation remains historical evidence for commit `a4f94483532d804435128889d1f9a03cc5a0a4a8`, not proof about this revision.
