# Verification and Experiential Acceptance

Registry: `blueprint.json`  
Artifact: ART-010  
Status: accepted

## Evidence hierarchy

1. typed unit/property/state-machine test;
2. contract test against fakes;
3. local integration test against the selected real adapter/store;
4. causal log/evidence manifest;
5. live in-world observation/media;
6. owner experiential judgment.

Compilation is necessary but never sufficient. `blueprint_guard.py validate --strict` proves structure, not semantic consistency or runtime behavior.

## Required test layers

| Layer | Network | Primary purpose |
| --- | --- | --- |
| format/lint/typecheck | none | project hygiene and exhaustive unions |
| unit/property | none | state transitions, trigger policy, evidence rules, ID/epoch, validators |
| contract with fakes | none | port boundary, one speech owner, async behavior, failure semantics |
| SQLite integration | none | transactions, WAL, FTS, migrations, backup/restore/reset, reconciliation |
| Minecraft integration | local Paper only | real progressive embodiment and evidence |
| model live | OpenAI only when explicitly selected | one structured decision and utterance quality |
| end-to-end live | Paper + explicit OpenAI | defining proof and owner review |

Default `npm test` is network-free and uses fakes.

## State-machine matrix

Tests must cover independently:

- connection: OFFLINE start, connection success, sync, unexpected disconnect, capped reconnect, server restart, operator shutdown, fault/repair;
- availability: ACTIVE absence → SUSPENDED, observed return → ACTIVE, PAUSED/resume, disconnect-induced suspension;
- health: world/model/store/telemetry degradations in combination without a `DEGRADED` agent state;
- cognition: success, invalid output, refusal, timeout, cancellation, interruption, stale late output;
- utterance: rejected, delivered, unconfirmed unknown, crash in SUBMITTING, duplicate ID, restart—never more than one attempt;
- action: rejected, validated, dispatch failed, dispatch unknown, started/active, terminal states;
- behavior: progress, stop, hazard interruption, suspension, shutdown, timeout, disconnect, unknown, idempotent no-active stop;
- epoch: compatible restart retains epoch; incompatible reset/replacement/restore increments; old epoch cannot validate action.

## Experience regression suite v1

`tests/fixtures/experience/v1/` is fixed and versioned. It contains:

| Fixture | Invariant/pass condition |
| --- | --- |
| identity consistency | same AgentId/name/persona ref; no identity swap after restart |
| known-fact contradiction | character does not contradict fixed source fact without acknowledging conflict |
| invented memory/fabricated certainty | no event/detail absent from retrieved sources is asserted as certain |
| relevant-memory retrieval failure | required EncounterId appears in top five and affects output |
| valid-but-foolish action | policy may reject contextually foolish action even if schema-valid; no unsafe improvisation |
| duplicate speech | at most one environment submission attempt per UtteranceId across timeout/restart |
| interrupted behavior | later dialogue acknowledges interruption, not completion |
| suspended behavior | zero model/behavior activity until observed return/resync |
| restart behavior | offline gap is explicit; natural recall remains grounded |

Rerun after any meaningful prompt, persona, memory, model, retrieval, action-policy, or orchestration change. Store model/version/prompt/fixture hashes with results.

## Retrieval suite v1

The eight cases are:

1. exact wording;
2. paraphrase;
3. indirect reference;
4. participant lookup;
5. place/event lookup;
6. keyword-free “remember when” within conversational context;
7. competing similar encounters;
8. stale/superseded interpretation excluded in favor of source event/current record.

Pass threshold is `LIM-GA-018`; measure twice on a release candidate. If both runs miss after ordinary query/index tuning, open WRK-007 semantic retrieval. Do not add embeddings earlier simply because the seam exists.

## Compaction evaluation (Gate B)

Any proposed compacted interpretation is compared with the uncompacted event/encounter baseline on:

- source/provenance retention;
- invariant key-fact preservation;
- contradiction and fabricated-certainty rate;
- retrieval usefulness across the eight fixtures;
- behavioral/dialogue continuity;
- token reduction.

It may be adopted only if it reduces tokens materially without lowering required retrieval/continuity thresholds or increasing prohibited claims. The comparison report is evidence; “has provenance” is not a pass.

## Stimulus tests

- addressed authorized chat: accepted once;
- duplicate source: suppressed;
- burst inside `LIM-GA-009`: coalesced;
- `LIM-GA-010` cooldown semantics: deterministic;
- queue at `LIM-GA-008`: newest excess stimulus suppressed with reason;
- non-addressed/unauthorized chat: no cognition;
- `LIM-GA-012` ordinary movement/entity/proximity/chunk/time soak: zero calls;
- player absence with noise: zero calls, no active behavior;
- return: no call before READY presence + resync;
- operator controls: act without cognition.

Any model call during SUSPENDED or the ambient soak fails Gate A.

## Capability evidence tests

For each capability transition, fixtures list accepted and rejected evidence kinds. Required negative tests include:

- dispatch acknowledgement alone cannot complete follow;
- client movement evidence may establish follow active/completed within its defined rule;
- client movement evidence cannot prove an item transfer or ownership;
- stale/wrong-epoch observation rejects;
- path goal cleared without observation of motion yields interrupted or unknown according to the observation window, not invented completed;
- later reconciliation appends a resolution and does not erase the original unknown phase.

## Gate-A live acceptance

Each repetition begins from the previous verified checkpoint and includes:

1. doctor prints no `FAIL`;
2. Paper starts and bot reaches READY;
3. authorized player is mapped to the expected PrincipalId;
4. player addresses the named character;
5. one structured decision produces one player-visible utterance attempt;
6. conversation causes validated asynchronous follow;
7. visible follow evidence appears;
8. stop/emergency stop works through the priority path;
9. player leaves; bot remains connected, becomes SUSPENDED, and makes zero model calls/actions;
10. Paper and runtime are completely stopped;
11. later restart reconciles honestly in the same compatible epoch;
12. relevant encounter is retrieved and naturally affects dialogue/behavior;
13. character avoids fabricated certainty and operator-console language;
14. evidence bundle validates machine-checkably;
15. owner rates the experience.

Run the entire sequence for the exact consecutive count in `LIM-GA-014`, each with a full Paper + runtime stop and later restart. Any failed repetition resets the consecutive count after the defect is corrected.

## Machine-checkable evidence manifest

Each run writes `evidence/gate-a/<run-id>/manifest.json` with:

- exact compatibility record hash;
- AgentId, authorized PrincipalId, WorldId, start/end WorldEpoch;
- required source EventIds;
- ConversationId, ModelRunId, UtteranceId and submission-attempt count;
- ActionId, BehaviorId, dispatch/active/terminal statuses and accepted evidence IDs;
- suspension interval and model-call count during it;
- process/server stop and restart timestamps;
- EncounterId, retrieval rank, source IDs supplied to recall run;
- tests/commands and exit codes;
- redaction scan result;
- links to logs/media;
- owner rubric result.

Automated verifier fails missing IDs, attempt count >1, absence calls >0, wrong epoch, absent evidence, failed tests, or retrieval below threshold.

## Owner experiential rubric

All are required:

- the character is recognizably consistent rather than generic;
- it refers naturally to currently perceived circumstances;
- its dialogue sounds like a character, not an operator console or database;
- memory is used conversationally and relevantly;
- it does not claim certainty beyond its sources;
- follow/stop behavior is coherent after interruption and restart;
- the owner answers **yes** to: “Is this live result worth continuing into Gate B?”

Machine evidence cannot substitute for this judgment; subjective approval cannot substitute for machine evidence.

## Structural and semantic checks

Before WRK-001 creates `package.json`, run the bundle-owned checks:

```powershell
python -m json.tool architecture\blueprint.json | Out-Null
python architecture\tools\semantic_guard.py architecture\blueprint.json
python architecture\tools\render_blueprint.py --check
```

From WRK-001 onward, run `npm run architecture:validate`; its package script wraps these checks and the scaffold's structural validation. The strict external blueprint guard result for the distributed revision is recorded in `generated/validation-report.txt`. The manual residual checklist in `11-semantic-review.md` covers meaning that cannot be reliably automated.
