# STE foundation validation

Date: 2026-10-06 (Asia/Shanghai).

Source version: these behavioral results and manifest paths describe commit `2c0f6ddbce3369db0a1118e4f87a80f94bd1aa2a`. The later v0.1.0 publication adds version metadata and documentation only. The skill body and helper are unchanged. Resolve the manifest's source hashes against that evaluated commit, not subsequent release-metadata changes.

## Scope

The user requires the complete ASD-STE100 foundation with literary Chinese only as the presentation layer for humans. The implementation uses Issue 9 (2025-01-15), all 53 Part 1 rule identifiers, the eight general recommendations at their advisory status, and Part 2 vocabulary review. It is not an official certification or a guarantee of every generated response.

## Evidence recorded so far

- Official source obtained directly from ASD. SHA-256: `d1f4ea9e7cd6e46b47aa9057209f99e78c0e9cfc4e27a5b07895b05c1a166431`. The PDF and dictionary extracts are kept outside Git.
- The 53 distinct ledger identifiers match the identifiers in the official rule-summary pages. All eight general recommendations are included. Identifier coverage alone does not prove behavioral compliance.
- `baseline-skill.md` is the exact root skill from commit `5aefdce32564b7d158060b81e937a2e18b4e4001`. `baseline.json` contains fresh executor answers for the eight scenarios.
- Baseline answers use `test` as a verb, `wear` for clothing, and `above` for a numeric threshold. Official Part 2 entries restrict these uses. The procedural answer also retains complex verb forms and advisory `should` instead of a faithful approved reconstruction.
- The helper initially failed to import because it did not exist. After implementation, five tests passed. Later integration checks exposed wrapped headwords and lines that combine headword and meaning. A `MANDATORY` lookup test failed before the latter repair and passed after it. Absence, corrupt source, exact-headword matching, official rows, and section ranges are covered.
- The preliminary forward executor overlaps helper repairs. Its output is retained as `forward-provisional.json` and must not establish final-source verification.
- Independent source review found two material parser defects: merged table lines, and wrapped parenthesized headwords/prefixes. Both were repaired. `source-review-followup.json` confirms exact rows and adjacent excerpt boundaries for ADJUSTABLE, MANDATORY, provided (that), providing (that), and re-. No remaining material issues were reported within that review's scope.

## Baseline writing results

| Dimension | Pass | Fail | Unresolved |
| --- | --- | --- | --- |
| Meaning | 8 | 0 | 0 |
| Observable STE behavior | 3 | 5 | 0 |
| Presentation | 8 | 0 | 0 |

The baseline has five STE criterion failures despite retaining meaning and presentation. Detailed evidence is in `scores-baseline.json`. These are criterion-specific verdicts, not every-word dictionary certification.

## Writing trial and targeted repair

The eight-case writing executor used a frozen entrypoint and ledger from before the negative-condition clarification. They are retained as `forward-batch-skill.md` and `forward-batch-guide.md`. Its helper source is retained as `helper-forward-trial.py`. After that freeze, two narrow helper extensions added parenthesized headwords and the prefix entry. The published helper is verified separately by the integration tests and source-review follow-up. Do not describe the batch executor as having run against the later source byte-for-byte.

The frozen batch is retained as `forward-batch.json`, with its exact entrypoint in `forward-batch-skill.md`. Independent grading in `scores-batch.json` gave eight meaning passes, seven STE criterion passes, and eight presentation passes. The modality case still put an essential `unless` condition after a prohibition. The skill and rule 5.4 checkpoint were clarified to cover negative conditions and exceptions before prohibitions.

A fresh executor then ran only that failed case against the revised source. Its actual answer and source are in `forward-repair.json` and `forward-repair-skill.md`. Independent `scores-repair.json` passed all three criteria. This targeted repair used medium reasoning effort; the original eight-case executors used high effort. No statistical model comparison is implied.

| Final regression collection | Pass | Fail | Unresolved |
| --- | --- | --- | --- |
| Meaning | 8 | 0 | 0 |
| Observable STE behavior | 8 | 0 | 0 |
| Presentation | 8 | 0 | 0 |

`forward-final.json` and `scores-final.json` assemble seven unchanged batch cases and the independently graded repaired modality case. They are not a new single-run trial. No answers or verdicts were invented during assembly. The final helper has five passing tests, including real official dictionary rows, corrupt/missing source behavior, exact lookup, and all section ranges with all eight recommendations.

## Publication checks and limits

The entrypoint passes the skill-format validator. Local documentation links and the official 53-rule identifier set were checked. Runtime files are synchronized to the personal installation and compared by bytes. The manifest retains source and evidence hashes. Git checks, commit, and remote-head verification complete publication.

Every pass above applies to the stated scenario criterion. The evaluation does not audit every English word or prove that an unseen English draft behind Chinese output complied with every rule. Complete rule coverage, helper correctness, faithful output, and formal document compliance are distinct claims. Source review supports the published design and parser within its stated scope; it is not an official certification. No live scenario operation or account action occurred. No universal compliance, model reliability, or token reduction claim is made.
