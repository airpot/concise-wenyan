# Concise Wenyan validation

Date: 2026-10-06 (Asia/Shanghai).

## Checked artifact

- Source: `SKILL.md` (unchanged from the original workspace skill).
- SHA-256: `7724ef3890c81dc6388bbee1af5838bf6b7571c0bb54f6978c10aa129f8be2e2`.
- Personal installation checked at creation: `~/.codex/skills/concise-wenyan`.
- Both installed files match their source SHA-256 hashes.
- The skill validator passed for source and installation. UI metadata, scenario IDs, exact path, command, JSON, and log quote checks also passed.
- File hashes and evaluation inputs are recorded in `provenance.json`.

## Written-response evaluation

Five scenarios have three criteria each. Fresh executors received the same scenarios; the forward executor also received the skill. A separate evaluator read the requests, criteria, and actual answers. It did not receive the skill or proposed conclusions.

| Mode | Pass | Fail | Not assessable |
| --- | --- | --- | --- |
| Without the skill | 13 | 2 | 0 |
| With the skill | 15 | 0 | 0 |

The two baseline failures concern Chinese instructions addressed to another AI, including instructions embedded in a Chinese explanation. The baseline already preserved the tested facts and conditions. No semantic-preservation improvement is inferred from those already-passing criteria.

Complete responses are retained in `baseline.json` and `forward.json`. Criterion scores and quoted evidence are in `scores.json`.

Executor IDs: baseline `01a10f49-692f-7a42-a7c0-a5f75d89317c`; forward `01a10f4a-93a0-7cc0-a4fa-fed586d6ac4e`; evaluator `01a10f4b-5974-72c1-adfb-fd11087963ad`. Each used the inherited model; the returned tool metadata did not identify the exact model version.

## Limits

These are single offline written-response trials, not live task execution or cross-agent runtime tests. Two scenarios closely resemble examples in the skill; three test variations not shown in those examples. Literary register is partly subjective, and the evaluator accepted light literary phrasing in the baseline. There is no measured token saving, statistical reliability claim, or discovery test in every agent product. The installation retains normal automatic skill selection; it does not force loading on every turn.

Refresh skill discovery or open a new session if the personal installation is not yet listed. Invoke `$concise-wenyan` to request the style explicitly.
