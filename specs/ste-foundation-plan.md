# STE foundation revision

## Accepted design

The user clarified that the complete ASD-STE100 rules are the foundation. Literary Chinese is only the presentation layer for human readers. This clarification supersedes the earlier design that borrowed selected writing principles.

Use Issue 9 (2025-01-15). Apply all 53 rules in Part 1, the eight general recommendations, and Part 2's approved vocabulary, senses, parts of speech, forms, and usage notes. Classify procedural, descriptive, and safety passages separately. Assess applicability instead of pretending every rule applies to every passage.

Construct a meaning-preserving English content plan and apply the applicable STE rules. Output that English for models. For human readers, render its propositions as readable literary Chinese and check them again. English word limits and inflections govern the English foundation; they are not Chinese character limits. Preserve executable syntax, identifiers, required quotations, and user-specified formats.

The official standard is the authority. Publish original implementation guidance and source references, not a redistributed dictionary or PDF. A helper obtains the verified official PDF in a local cache and retrieves rule sections and dictionary rows. Missing evidence is unresolved, never a compliance pass. No checker is represented as an official certification.

## Implementation plan

- [x] Preserve the preceding skill and run fresh baseline writing scenarios before changing its instructions.
- [x] Add tests for exact dictionary lookup, source integrity, section ranges, and unavailable references. Observe missing-helper failures.
- [x] Implement `scripts/ste_reference.py`: verified fetch, local cache, section reading, and dictionary lookup with page evidence.
- [x] Add `references/ste-issue9.md`: all 53 identifiers, applicability, technical terminology categories, general recommendations, and dictionary review procedure.
- [x] Revise `SKILL.md`, interface metadata, README, and accepted specification to implement the two layers.
- [x] Run the same writing scenarios against the revised skill; review semantics, STE behavior, and literary style separately. Retain failures and repair them.
- [x] Verify source hashes, reference coverage, helper tests, format, links, and installation equivalence. Commit and push to the existing remote.

## Verification scope

Structural coverage means every official rule identifier has an implementation checkpoint. Behavioral samples do not prove universal STE compliance. Dictionary lookup reports original evidence and does not infer grammar or certify a sentence. Source downloads and dictionary extracts remain outside Git. Historical evaluations continue to describe their original source versions.
