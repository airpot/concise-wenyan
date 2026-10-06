# Complete STE foundation: Issue 9

## Authority and source access

The authority is [ASD-STE100 Issue 9, dated 2025-01-15](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf), including Part 1 and Part 2. This document contains original implementation checkpoints, not the standard's full text. Read the official explanations and exceptions when applying a checkpoint. Do not substitute this ledger or model memory for the official dictionary.

Use the complete foundation for every passage covered by this skill. During the first use in a session, read this ledger and the official dictionary introduction. Read all applicable official rule sections. Reuse reference evidence already read for the same pinned issue, but assess the applicability and vocabulary of each new draft. All rules remain in scope even when a particular passage has no relevant safety instruction or procedure.

Commands are relative to this skill's directory:

```text
python scripts/ste_reference.py fetch
python scripts/ste_reference.py section dictionary-intro
python scripts/ste_reference.py section 5
python scripts/ste_reference.py lookup test wear above should
```

The helper needs Python. Section reading and dictionary lookup also need PyMuPDF. If it is unavailable, use an existing PDF reader that can show the official pages, or install PyMuPDF when dependency installation is authorized. `fetch` uses the Python standard library and checks the source SHA-256. The source stays in `~/.cache/concise-wenyan/`, outside the skill and Git repository. Use `--cache PATH` before the subcommand to select another cache.

A source mismatch, missing reader, absent source, or ambiguous extraction is unresolved. Never infer approval from an absent search result, an example, or a synonym in the alternatives column. The helper retrieves evidence. It does not parse a sentence, resolve meaning, count STE words, or certify compliance.

## Applicability and outcomes

Classify each passage as procedural, descriptive, or a safety instruction. Classify notes as descriptive. A mixed response can contain several types. Apply all shared rules and the appropriate type-specific rules. For a formal review, use `pass`, `fail`, `not applicable` with a reason, or `unresolved` with missing evidence for each rule. A complete review requires all 53 rule IDs and dictionary checks. Do not turn an unresolved result into a pass.

Use the English foundation's limits: procedures and safety instructions have 20 words per sentence. Descriptions and informational notes have 25 words per sentence. Descriptive paragraphs have no more than six sentences. These are sentence and paragraph limits, not a limit on the answer's total length. Divide a complex answer into enough sentences and paragraphs to retain its meaning.

## Part 1: 53 implementation checkpoints

### 1. Vocabulary (shared)

| ID | Check in the English foundation |
| --- | --- |
| 1.1 | Account for each word as a dictionary-approved use, valid technical noun, or valid technical verb. |
| 1.2 | Verify the dictionary part of speech for the actual use. Approval as a noun does not approve a verb. |
| 1.3 | Verify the actual sense, including restricted contexts, rather than general English meanings. |
| 1.4 | Verify the permitted inflections and adjective forms. |
| 1.5 | Identify a valid technical-noun category for each domain term. |
| 1.6 | Justify non-dictionary words as technical nouns or components of such nouns, except separately valid technical verbs. |
| 1.7 | Do not use a technical noun as a verb merely because ordinary English permits it. A separately justified technical verb needs its own category. |
| 1.8 | Use established terminology from the project's, industry's, or subject's glossary. |
| 1.9 | If a new term is necessary, select a short, understandable name. |
| 1.10 | Exclude slang and region-specific or insider-only jargon from technical terminology. |
| 1.11 | Keep the same noun for the same item throughout the text. |
| 1.12 | Justify each technical verb under an allowed category. Prefer an approved verb when it accurately expresses the same action. |
| 1.13 | Do not use technical-verb status as noun approval. Assess a noun separately. |
| 1.14 | Use American spelling unless an applicable official directive requires another spelling. |

### 2. Noun groups (shared)

| ID | Check |
| --- | --- |
| 2.1 | Keep ordinary noun groups within three words. |
| 2.2 | Introduce a longer official technical noun in full, then define a shorter form or clarify related units with justified hyphens. Do not silently alter an official name. |

### 3. Verb construction (shared, with the descriptive exception)

| ID | Check |
| --- | --- |
| 3.1 | Use the dictionary's listed verb forms. |
| 3.2 | Use infinitives, imperatives, simple present/past/future, and adjectival past participles. Reconstruct perfect and progressive forms. |
| 3.3 | Assess past participles as adjectives, rather than allowing an unapproved compound tense. |
| 3.4 | Remove complex auxiliary constructions. Retain permitted simple-future and modal constructions only as the official rules and entries allow. |
| 3.5 | Restrict an `-ing` form to a technical noun or a modifier within one. Do not apply this restriction to protected literal strings. |
| 3.6 | Prefer active clauses. A passive descriptive clause is allowed only when its actor is unknown. Never invent an actor to satisfy the rule. |
| 3.7 | Name an action with an approved verb instead of obscuring it in a nominal construction. Respect nouns such as `test` whose verb use is unapproved. |

### 4. Sentence clarity (shared)

| ID | Check |
| --- | --- |
| 4.1 | Make sentence structure short and unambiguous. |
| 4.2 | Retain necessary grammatical words and expand contractions. Brevity does not justify telegram English. |
| 4.3 | Use a vertical list when complex content otherwise obscures structure. |
| 4.4 | State logical connections between related sentences. |
| 4.5 | Supply articles or demonstratives where grammar requires them. Respect proper names and identifiers instead of inserting articles mechanically. |

### 5. Procedures

| ID | Check |
| --- | --- |
| 5.1 | Count each procedural sentence using section 8. Keep it within 20 words, including safety instructions. Informational notes use the descriptive limit. |
| 5.2 | Put one sequential instruction in a sentence. Multiple simultaneous actions can share a sentence when simultaneity is explicit. |
| 5.3 | Give work steps in the imperative. Do not convert a supplied recommendation into an obligation. |
| 5.4 | Put a necessary condition before its command and separate the two with a comma. This includes negative conditions and exceptions before prohibitions. Reconstruct an action-first `unless` clause without reversing its scope. |
| 5.5 | Keep notes informational. Move a required action into the procedure or the appropriate safety instruction. |

### 6. Descriptions, reports, and informational notes

| ID | Check |
| --- | --- |
| 6.1 | Introduce information in a sequence the reader can follow. Descriptive passages report information rather than issuing imperative work steps. |
| 6.2 | Use stable key terms and explicit connecting phrases to show structure. |
| 6.3 | Count descriptive sentences using section 8 and keep each within 25 words. |
| 6.4 | Group related information into paragraphs. |
| 6.5 | Keep one topic in each paragraph. |
| 6.6 | Keep each descriptive paragraph within six sentences. |

### 7. Safety instructions, when the supplied task contains a hazard

| ID | Check |
| --- | --- |
| 7.1 | Use a signal word that matches the risk. A warning concerns injury/death; a caution concerns damage to objects. Respect documented domain-specific equivalents. |
| 7.2 | Start with the precise command or condition needed to avoid the hazard. |
| 7.3 | State the hazard or consequence clearly. Do not invent hazards or weaken an existing risk level. |

### 8. Punctuation and STE word count

| ID | Check |
| --- | --- |
| 8.1 | Use standard English punctuation without semicolons in authored STE prose. Code and required verbatim strings are preserved separately. |
| 8.2 | Hyphenate directly related word units only when that grouping makes their relation clear. |
| 8.3 | Use parentheses for references, item/work-step identifiers, abbreviations, number forms, explanations, or alternatives. Do not hide missing context in them. |
| 8.4 | At a vertical-list introduction, treat its colon as a sentence boundary for counting. This does not license arbitrary colon splitting elsewhere. |
| 8.5 | Count a parenthesized text group as one STE word. |
| 8.6 | Count a number, number-plus-unit, abbreviation, alphanumeric identifier, quotation, title/heading/label, or proper-name unit as one, as the official examples specify. |
| 8.7 | Count a hyphenated group as one. Do not fabricate hyphens to evade the limits. |

### 9. Writing practice (shared)

| ID | Check |
| --- | --- |
| 9.1 | Reconstruct the sentence when replacing individual words cannot retain clear, correct meaning. |
| 9.2 | Recheck approved meanings and contextual restrictions in the actual sentence. |
| 9.3 | Do not combine approved words into a new phrasal-verb meaning. Use an explicitly approved restricted phrase or a separately justified technical verb only in its valid context. |
| 9.4 | Use consistent wording for the same action and meaning, not stylistic synonym variation. |

## General recommendations: separate from the 53 rules

Consider these eight recommendations without relabeling them as mandatory numbered rules:

- GR-1: Include `that` when it makes the clause boundary clear.
- GR-2: Resolve the intended meaning of `with`; state the actual primary action.
- GR-3: Replace a pronoun with its noun when the referent is ambiguous.
- GR-4: Give an explicit referent for `this`, including its causal context.
- GR-5: Check apparent cognates against English meaning.
- GR-6: Prefer clear English over Latin abbreviations.
- GR-7: Use inclusive language that avoids unjustified exclusions.
- GR-8: Assess possessive forms carefully; use an explicit relationship when needed for clarity.

Read the official section 9 for the full context of these recommendations.

## Technical terminology: category justification

Part 1 allows technical nouns in 22 categories. Record which category supports a project term; the category does not waive grammar or permit an unrelated verb sense.

1. Design and parts identification.
2. Vehicles, machines, and their locations.
3. Tools, support equipment, components, and locations.
4. Materials, consumables, and unwanted substances.
5. Facilities, infrastructure, and logistics.
6. Systems, circuits, configurations, functions, and components.
7. Mathematics, science, engineering, and formulas.
8. Navigation and geography.
9. Numbers, measurement units, time, and symbols.
10. Fixed quoted text and labels.
11. Roles, people, groups, organizations, and geopolitical names.
12. Anatomical terms.
13. Personal items, food, and beverages.
14. Medical terminology.
15. Documents, document components, standards, and guidelines.
16. Environmental and operational conditions.
17. Color terms, with the standard's restrictions on their forms.
18. Damage and defect terminology.
19. Computing, information, and communication technology.
20. Civil and military operations and support.
21. Law and regulation.
22. Animals, plants, and other organisms.

Technical verbs have four category groups: manufacturing; computer processes/applications; specified subject-field processes; and legal/regulatory text. Consult the official examples and restrictions. A computing action such as schema validation needs a real computing meaning, not a blanket exemption for every word in an AI prompt. A term can have independently justified noun and verb uses. Neither use automatically approves the other.

## Part 2: vocabulary review

The dictionary is a required part of the foundation, not an optional style aid. Check the actual use of every authored English word. For an approved entry, check its part of speech, approved sense, listed forms, and usage notes. For an unapproved entry, assess the proposed alternatives in context. If a replacement changes the sense, reconstruct the sentence. A technical term needs a category and a domain meaning. Inflected words need a verified base entry and an allowed form.

Keep a reusable reviewed word inventory for the same issue, including word/base form, part of speech, sense, forms or restriction, and page evidence. Reuse it only for the same sense and context. New or changed uses need review. Do not ship the official dictionary or a copied word inventory in this repository.

Pay particular attention to uses that look ordinary but are restricted: `test` as a verb, `wear` for clothing, and `above` for a numeric threshold. The official entries resolve these cases. Do not infer allowed meanings from the everyday language model prior.

Do not replace advisory `should` with binding `must` merely because a dictionary alternative lists `MUST`. Use a construction that explicitly describes a recommendation. Likewise, distinguish permission from possibility, `not required` from `unnecessary` or `forbidden`, and confirmed failure from a timeout. If no faithful approved construction is available, keep meaning and report the unresolved conflict.

## Chinese presentation and protected material

Apply the English-specific morphology, vocabulary, articles, punctuation, and word counts to the English foundation. Preserve the foundation's propositions, actor, force, branch structure, order, terminology mapping, quantities, and evidence in the Chinese rendering. Chinese is not formally STE English. Do not pretend that Chinese characters are STE words or that Chinese grammatical particles are dictionary-approved English.

Prefer readable literary clauses for the human text. Necessary grammatical relations must remain explicit even if literary Chinese usually permits their omission. Chinese punctuation and brief inline definitions are allowed. If a literary phrase obscures a prerequisite, actor, exception, or uncertainty, make that passage clearer.

Protected commands, code, paths, JSON, UI labels, quotations, and required literal data retain their syntax and spelling. Mark their boundary and review the surrounding authored prose. Protection is not a way to quote an entire newly authored instruction to evade the rules. An explicit task language or required format overrides the default rendering; record any resulting STE deviation honestly if a review is requested.

## Evidence and truthful claims

Separate three checks: meaning, STE foundation, and presentation. A format validator proves only skill format. A short sentence is not proof of dictionary compliance. The lookup helper is not a grammar checker. A full audit needs per-rule evidence, vocabulary evidence, and a review of technical correctness. Never describe a Chinese rendering as formally STE-compliant English, or a small evaluation as universal compliance or official certification.
