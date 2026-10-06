# Complete-foundation evaluation

Run the eight offline scenarios against the preceding skill and the revised skill. Give executors only the skill, referenced source resources, and scenarios. Do not give them criteria, expected answers, or previous outputs. Keep all scenario operations hypothetical.

Assess each response separately for semantic preservation, observable STE behavior, and presentation using `criteria.json`. Review English vocabulary against the official source where required. Chinese outputs require a separate meaning/presentation assessment; visible Chinese alone cannot establish that an unseen English content draft complied with every rule.

Record the executor's actual outputs, failed trials, material repairs, source hashes, model identifier when available, and the limits of each check. An evaluator must not infer a dictionary pass from short prose. Complete rule coverage is a separate structural check, not a statistical result or a formal compliance certificate.

The official source is held outside the repository. Dictionary excerpts and bulk execution logs stay in the private cache or `.git/ste-eval/`. The repository retains the original implementation guide, writing scenarios, answers, judgments, and validation record.
