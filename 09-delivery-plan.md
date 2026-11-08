# Delivery Plan: Step Zero to Experiential Proof

Registry: `blueprint.json`  
Artifact: ART-011  
Status: accepted

## Critical path

```text
SPIKE-000 disposable feasibility/compatibility record
      │
      ▼
WRK-001 thin contracts + fakes + in-memory causal loop
      │
      ▼
WRK-002 real stack pin + join/presence/chat/perception/movement/stop
      │
      ▼
WRK-003 one decision + one utterance + async follow/stop/suspension
      │
      ▼
WRK-004 minimal SQLite events/encounter + shutdown/restart/retrieval/ops
      │
      ▼
WRK-005 three live full proofs + owner judgment
      │
      └──────── Gate A passed; Gate B packages may begin
```

Visible sequence:

`preflight → server → bot join → player detection → deterministic chat → manual movement/stop → structured model decision → one utterance → async follow/stop → persist encounter → restart/retrieve → repeated proof`

No milestone requires infrastructure beyond its visible behavior.

## Checkpoint discipline

Every micro-step:

- begins from a named, passing prior checkpoint;
- changes one objective and the exact listed files/modules;
- includes a paste-ready bounded IDE-agent prompt;
- runs format, lint, typecheck, unit, relevant contract/integration/smoke checks;
- states expected human-readable success output and objective failure conditions;
- stops on concealed/weakened/bypassed failure;
- leaves recovery/rollback instructions and a proving artifact;
- updates only `10-resume-state.md` for implementation status.

Do not combine unrelated steps to “save time.” Optional sophistication never blocks the next visible behavior.

## Gate-A package outcomes

| Package | New visible capability | Prior checkpoint preserved | Gate |
| --- | --- | --- | --- |
| SPIKE-000 | proves the selected external stack can do the whole thin loop | disposable; production untouched | every progressive gate recorded or fallback chosen |
| WRK-001 | network-free fake player message → decision → utterance/action proposal → async result | strict blueprint checks | closed contracts/state/IDs and deterministic tests |
| WRK-002 | real bot joins, sees authorized player, deterministic chat, moves, stops | fake loop still passes | exact compatibility record and progressive smoke |
| WRK-003 | real addressed model decision, one utterance, async follow/stop, connected suspension | deterministic chat/manual movement still work | single-speech, timeout, trigger, priority-control tests |
| WRK-004 | encounter survives full stop/restart and is retrieved; owner-safe data commands | WRK-003 still runs with in-memory fake store tests | SQLite probes, integrity, backup/restore/reset/reconciliation |
| WRK-005 | repeatable live defining experience | complete automated suite | `LIM-GA-014` consecutive proofs plus owner yes/no |

## Empirical dependency gates

SPIKE-000 records provisional choices; WRK-002 pins production exact versions. WRK-004 cannot begin until the selected Node version is recorded because DEC-005's SQLite choice depends on that runtime. This removes the former implicit WRK-003 SQLite/Node prerequisite.

At any later integration resume after time/dependency drift:

1. re-read the primary sources in `blueprint.json.compatibility_policy`;
2. rerun progressive gates from authentication through the first affected capability;
3. date and hash the updated record;
4. use another verified intersection without architecture review when needed;
5. stop platform expansion if embodiment is red.

## Gate-B independent deliverables

The former WRK-007/008 breadth is split:

- WRK-006 — versioned experience/continuity regression hardening;
- WRK-007 — measured derived memory, compaction, and semantic retrieval;
- WRK-008 — authenticated operator service, audit, retention/deletion, typed correction;
- WRK-009 — generalized readiness, observability, and multi-level budgets;
- WRK-010 — second character and isolation/interaction;
- WRK-011 — deliberate 8–10-character scale;
- WRK-012 — authoritative item/inventory/container/transfer workflows;
- WRK-013 — speculative LSL/action-tag/emote design;
- WRK-014 — second real environment adapter and portability assessment;
- WRK-015 — rich beliefs, relationships, goals, plans, reflection, scheduling;
- WRK-016 — exhaustive mutation crash recovery and migration governance.

None is a Gate-A dependency. Their exact graph is generated in `generated/work-index.md`.

## Universal IDE-agent instruction block

Every micro-step prompt includes this verbatim policy:

> Inspect the repository and the prior checkpoint before editing. State the exact files you intend to change. Make only the requested bounded change; avoid unrelated refactors and preserve existing contracts unless this step explicitly changes them. Run format, lint, typecheck, unit tests, relevant contract/integration tests, and the named smoke test. Report exact commands, exit codes, meaningful output, and anything omitted. Summarize the resulting behavior in plain language. Stop rather than bypass, conceal, weaken, skip, or explain away a failure. Compilation alone is not success. Produce evidence that can be pasted unchanged to a second agent for review.

## Package completion rule

A work package becomes `completed` only after every micro-step checkpoint exists and the package gate passes. It becomes `verified` only after a second agent or owner reconciles those artifacts. Registry status is never changed merely because an IDE agent says it is done.

## Recovery rule

If a step fails:

1. preserve the previous checkpoint;
2. capture the exact command/output;
3. revert only the step's declared files or discard its disposable branch/directory;
4. classify the failure as environment, dependency, contract, behavior, evidence, or owner-experience;
5. apply only the documented fallback or stop for a new decision;
6. never rebuild the entire project unless the prior checkpoint itself is independently proven corrupt.
