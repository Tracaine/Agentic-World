# Runtime Flows

Registry: `blueprint.json`  
Artifact: ART-008  
Status: accepted

The registry owns the machine-readable step/failure arrays. This document explains the cross-flow timing and authority changes.

## FLW-001 — Start and synchronize

```text
OFFLINE
  └─ operator start → CONNECTING
       └─ Mineflayer joined → SYNCING
            ├─ store/profile/world/epoch/aliases/snapshot valid → READY
            │     ├─ authorized principal observed → ACTIVE
            │     └─ principal absent → SUSPENDED (client remains connected)
            └─ incompatible/unrecoverable → FAULTED
```

No model call or action occurs before READY + ACTIVE. A restart creates a new `WorldSessionId`; it keeps `WorldEpoch` only after compatibility checks.

## FLW-002 — Addressed conversation and action

```text
authorized addressed chat
  → closed perception + durable player utterance
  → trigger gate (ACTIVE, dedupe, cooldown, queue)
  → decision actor assembles labelled bounded context
  → ModelPort (hard `LIM-GA-002` deadline)
  → ModelDecision { utterance?, action? }
       ├─ utterance → CMP-003 assign/persist UtteranceId → one INT-011 attempt
       └─ action → CMP-005 validate → dispatch → started + BehaviorId
  → cognition completes; actor mailbox is free

later:
BehaviorEvent → evidence rule → active/progress/terminal durable event
              → optional new cognition only if designated for interpretation
```

Utterance and action are independent children of the same decision. A rejected follow does not force a valid utterance to disappear; an unknown chat send does not make follow untrue. Their causal links share the player `EventId` and `ModelRunId` but their state machines remain separate.

The old FLW-002 step 9—waiting for terminal follow inside the model/tool run—is retired. No tool callback, actor mailbox, or database transaction stays open for physical duration.

## FLW-003 — Honest failure

Failures are classified by phase:

- before validation: `rejected` with reason;
- after validation, before external dispatch: `failed` or `cancelled`; no world effect;
- external dispatch acknowledged: `dispatched`, not success;
- active behavior with evidence: `active`;
- terminal evidence meets capability threshold: `completed`, `failed`, `interrupted`, `cancelled`, or `timed_out`;
- external effect cannot be determined: `unknown`;
- later same-epoch evidence may add `reconciled` without rewriting the earlier uncertainty.

Logs and tests use those exact words. “Started successfully” is forbidden because it collapses dispatch and outcome.

## FLW-004 — Full stop, restart, and recall

1. Acceptance interaction is deterministically promoted to `EncounterId` with complete source events.
2. Owner invokes shutdown. Priority control stops behavior before the `LIM-GA-013` cleanup deadline.
3. Runtime flushes transactions and closes; Paper stops completely.
4. No runtime events are created while both are stopped.
5. Later, Paper and runtime start. New world session, identity/epoch resolution, and reconciliation run before ACTIVE.
6. Unfinished speech becomes unknown; unfinished behavior becomes interrupted/unknown according to phase.
7. Relevant encounter retrieval uses principal, world/epoch, conversation cues, and FTS/structured fields.
8. Source-labelled excerpts enter the model context. The character refers naturally to the prior experience with appropriate uncertainty.

Acceptance fails if recall appears only in SQL/logs, sounds like a database/operator console, invents an offline event, or confidently asserts a source-unsupported detail.

## FLW-005 — Model provider unavailable

Model health changes independently. Exceeding `LIM-GA-002`, refusal, or invalid output closes the run. No partial text is submitted, no automatic retry occurs, and no action is dispatched from malformed output. World presence and priority safety controls continue if the adapter/store remain healthy.

## FLW-007 — Development resumption

The fresh IDE agent must:

1. inspect the repository before planning edits;
2. run structural and semantic guards;
3. read `10-resume-state.md` plus the active micro-step's prior checkpoint;
4. compare claimed evidence to actual files/tests;
5. classify the micro-step `unstarted | partial | complete | contradicted`;
6. stop on contradiction rather than weaken checks;
7. execute one bounded step and attach pasteable command/output evidence.

Agent narrative is never the only proof.

## FLW-008 — Absence, return, disconnect, restart, and shutdown

These are separate scenarios and tests:

| Scenario | Connection | Availability | What continues | Resume condition |
| --- | --- | --- | --- | --- |
| Player leaves | READY | SUSPENDED | same-principal presence observation, connection health, priority control | READY adapter observes same PrincipalId; resync succeeds |
| Player returns | READY | SUSPENDED → ACTIVE | resync then normal triggers | fresh presence and snapshot |
| Unexpected link loss | DISCONNECTED | SUSPENDED | reconnect timer and local operator control | reconnect → SYNCING → READY, then fresh presence |
| Paper restart | DISCONNECTED → CONNECTING/SYNCING | SUSPENDED | local diagnostics/reconnect | compatible epoch and fresh snapshot |
| Operator pause | usually READY | PAUSED | presence/health and priority control | explicit resume plus ACTIVE preconditions |
| Operator shutdown | eventually OFFLINE | non-active | nothing after process exit | later explicit start; OFFLINE itself observes nothing |

On player absence, the runtime immediately cancels cognition and high-priority-stops movement/actions/behavior. There is no grace period that permits another model call. Chat, entity, proximity, behavior-result, and restart triggers are all suppressed while SUSPENDED.

## FLW-009 — Stop and emergency stop

Stop does not wait behind ordinary stimuli:

1. accept typed control request;
2. identify the current own BehaviorId/lease if any;
3. clear dynamic pathfinder goal and movement controls immediately;
4. return acknowledgement within the `LIM-GA-007` p95 target;
5. observe path/motion state;
6. emit interruption/completion evidence or unknown if disconnected;
7. release lease and cancel future re-evaluation.

Calling stop when nothing is active is an idempotent completed control result, not an error.

## FLW-010 — Compatibility spike

SPIKE-000 and WRK-002 advance only through progressive gates:

`preflight → authentication/join → presence → chat → position/entities → chunks/basic movement → pathfinding → follow/interrupt/stop → structured model decision/utterance → disconnect/reconnect/restart`

Each gate records exact version, URL, retrieval/test date, command, output, host, and fallback. Failure stops expansion. The allowed fallback order is:

1. simplest manual movement or narrower observation;
2. another verified dependency intersection;
3. narrowly scoped Paper-side assistance for observation/wake only.

Do not respond to protocol risk by building more cognition or persistence.

## FLW-011 — Reset/restore and epoch

Restore is verified to a separate path. Before using a restored/replaced world, compare intended continuity and fingerprint. A compatible continuation may retain `WorldEpoch`; an incompatible history allocates the next epoch. Old encounters remain historical but cannot validate the current environment. Any ambiguity stops startup rather than silently merging histories.
