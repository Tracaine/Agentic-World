# Domain, State, Identity, and Persistence

Registry: `blueprint.json`  
Artifact: ART-005  
Status: accepted

## Stable IDs

Gate A creates opaque UUID/ULID-style project-owned IDs. Adapters never choose them.

| ID | Stable scope | Notes |
| --- | --- | --- |
| `AgentId` | character | Stable across process, provider, bot, and persona versions |
| `PrincipalId` | person/authorized actor | Minecraft UUID/username/session entity IDs are aliases |
| `WorldId` | intended world continuity | Stable through compatible server restarts |
| `WorldEpoch` | compatible history segment | Monotonic integer within WorldId; increment on incompatible reset/replacement/restore |
| `WorldSessionId` | one adapter connection | New on every connection/reconnection |
| `EventId` | one durable source event | Unique; adapter source keys dedupe into it |
| `ConversationId` | addressed dialogue sequence | May span reconnects only within the same epoch |
| `ModelRunId` | one cognition attempt | Never reused for a retry; Gate A has no automatic retry |
| `UtteranceId` | one accepted NPC utterance proposal | At most one submission attempt without definitive environment dedupe |
| `ActionId` | one action proposal/attempt | Links validation and immediate dispatch |
| `BehaviorId` | one long-running behavior lease | Links later progress and terminal events |
| `EncounterId` | one deterministic source-event grouping | Used for restart retrieval and acceptance evidence |

Authorization, participants, memories, relationships, actions, and behaviors use internal IDs. A username may help resolve an alias but is never stored as the owner field.

## Orthogonal state model

The former exclusive idle/cognition/action lifecycle is retired. Five independent state machines describe what is actually happening.

### Connection state

`OFFLINE | CONNECTING | SYNCING | READY | DISCONNECTED | FAULTED`

- `OFFLINE`: operator-intended absence of a client connection—before start or after clean shutdown. No player-return observation is possible.
- `CONNECTING`: a connection/authentication attempt is in progress.
- `SYNCING`: connected, but identity/world/epoch/presence/snapshot are not yet safe for cognition/action.
- `READY`: adapter is connected and synchronized. The character can still be `SUSPENDED` or `PAUSED`.
- `DISCONNECTED`: a previously expected connection is absent because of server/network/client failure. Five capped reconnect attempts run; after exhaustion the state remains `DISCONNECTED` for diagnosis. A disconnected client cannot detect return.
- `FAULTED`: configuration, compatibility, identity, epoch, or unrecoverable adapter failure requires operator action.

Legal transitions:

```text
OFFLINE --start--> CONNECTING --joined--> SYNCING --synced--> READY
CONNECTING/SYNCING/READY --link lost--> DISCONNECTED --retry--> CONNECTING
any non-OFFLINE --operator shutdown completed--> OFFLINE
CONNECTING/SYNCING/DISCONNECTED --unrecoverable--> FAULTED
FAULTED --operator repair and explicit retry--> CONNECTING
```

### Availability state

`ACTIVE | SUSPENDED | PAUSED`

- `ACTIVE`: connection is READY, authorized principal is observed present, operator has not paused, and store/profile are usable.
- `SUSPENDED`: presence is absent/unknown or connection is not READY. Entry immediately priority-stops cognition, planning, movement, actions, and behaviors. While a healthy connection remains READY, only authorized-principal presence observation, essential connection health, and priority safety/operator control continue.
- `PAUSED`: explicit operator pause. The connection may remain READY; presence may continue to be observed, but no cognition or physical behavior resumes until explicit operator resume and all ACTIVE preconditions hold.

Rules:

- authorized player leaves while READY → `SUSPENDED`, Mineflayer stays connected;
- same `PrincipalId` observed again while READY → resync snapshot → `ACTIVE` unless PAUSED;
- unexpected disconnect → `SUSPENDED` plus connection `DISCONNECTED`;
- operator pause → `PAUSED` regardless of presence;
- operator shutdown → priority stop, connection eventually `OFFLINE`; availability remains non-active and is reconstructed at next start;
- `SUSPENDED` wins over every cognition trigger.

### Component health

World adapter, model, store, and telemetry independently use:

`OK | DEGRADED | UNAVAILABLE | FAULTED`

Health changes do not overwrite connection or availability. A model outage can coexist with `READY/ACTIVE`; a store fault prevents entering ACTIVE; telemetry degradation cannot delay emergency stop.

### Cognition run

```text
QUEUED → ASSEMBLING_CONTEXT → CALLING_MODEL → PARSING_DECISION → COMPLETED
  └──────────────→ REJECTED_BUDGET | TIMED_OUT | CANCELLED | FAILED | INTERRUPTED
```

`LIM-GA-002` (`model_deadline_ms`) covers provider work. `COMPLETED` means a valid `ModelDecision` was accepted, not that an utterance delivered or behavior completed. Suspension cancels all nonterminal runs. Restart marks unfinished runs `INTERRUPTED`; they are never resumed.

### Action attempt

```text
PROPOSED → VALIDATING → REJECTED
                     └→ VALIDATED → DISPATCHING → DISPATCHED → ACTIVE
                                               ↘ UNKNOWN       ↘ COMPLETED
                                                                 FAILED
                                                                 INTERRUPTED
                                                                 CANCELLED
                                                                 TIMED_OUT
                                                                 UNKNOWN
```

`DISPATCHED` means the environment channel accepted the command. `ACTIVE` requires the capability's evidence, not merely a function return. `COMPLETED` requires the declared minimum terminal evidence. Failure to determine an externally visible outcome becomes `UNKNOWN`.

### Long-running behavior

```text
REQUESTED → DISPATCHING → ACTIVE → COMPLETED
                              ├→ FAILED
                              ├→ INTERRUPTED
                              ├→ CANCELLED
                              ├→ TIMED_OUT
                              └→ UNKNOWN
```

Follow dispatch immediately returns `started` plus stable `BehaviorId`/lease ID. Later typed `BehaviorEvent`s carry progress, re-evaluation, interruption, completion, timeout, cancellation, failure, or uncertainty. The decision actor is free after `started` and can process priority stop or later stimuli.

### Utterance delivery (not an action)

```text
PROPOSED → VALIDATED → SUBMITTING → DELIVERED
        ↘ REJECTED                 ↘ UNKNOWN
```

The runtime assigns `UtteranceId`, writes intent before submitting once, and records the environment result. Unless the environment offers definitive deduplication, `SUBMITTING` found after interruption becomes `UNKNOWN`; it is never replayed. Player input is recorded as an observed/delivered player utterance, not as an NPC delivery attempt.

## Gate-A data records

| DAT ID | Record | Gate-A role |
| --- | --- | --- |
| DAT-001 | `CharacterIdentityRecord` | AgentId, display name, persona-package ref/version/hash |
| DAT-002 | `AgentRuntimeState` | Orthogonal current projection and transition events |
| DAT-003 | `WorldSession` | adapter connection and exact compatibility record |
| DAT-004 | `DurableEvent` | complete source events for utterance/action/behavior/evidence/lifecycle/restart |
| DAT-005 | `PerceptionSnapshot` | in-memory bounded view with epoch, capture, expiry, omissions |
| DAT-010 | `ConversationUtterance` | player delivered utterance; NPC proposal and delivery state |
| DAT-011 | `ActionAttempt` | typed proposal, validation, dispatch, outcome, evidence refs |
| DAT-012 | `ModelRun` | request manifest, structured decision, timing, status, provider metadata |
| DAT-014 | `SchemaMetadata` | migration/checksum/application/binding record |
| DAT-015 | `PrincipalIdentity` | PrincipalId, authorization, time-bounded Minecraft aliases |
| DAT-016 | `WorldIdentity` | WorldId, epoch, fingerprint, compatibility decision |
| DAT-017 | `BehaviorRun` | BehaviorId, lease, progress/terminal event refs |
| DAT-018 | `EncounterRecord` | deterministic source-event grouping for recall |

DAT-006–009 and DAT-013 are registered but deferred: beliefs, model-authored episodic interpretations, relationships, goals/plans, and comprehensive operator audit.

## Closed durable event union

Every Gate-A event shares:

`EventId`, `kind`, `schemaVersion`, `occurredAt`, `observedAt`, `recordedAt`, `WorldId`, `WorldEpoch`, `WorldSessionId?`, `AgentId`, `PrincipalId?`, `ConversationId?`, `causedByEventId?`, and kind-specific typed body.

Kinds are:

- `player_utterance_delivered`;
- `npc_utterance_proposed`, `npc_utterance_validated`, `npc_utterance_delivery_result`;
- `model_run_started`, `model_decision_accepted`, `model_run_terminal`;
- `action_proposed`, `action_validation_result`, `action_dispatch_result`;
- `behavior_started`, `behavior_progress`, `behavior_terminal`;
- `capability_evidence_observed`;
- `presence_changed`, `connection_changed`, `availability_changed`, `component_health_changed`;
- `encounter_promoted`;
- `shutdown_started`, `shutdown_completed`, `restart_reconciled`, `offline_gap_recorded`.

Each kind fixes its body schema. There is no generic durable `payload`, `normalizedPayload`, `self`, or `evidence` object.

## Deterministic encounter promotion

Gate A promotes an `EncounterRecord` only when:

1. the authorized player explicitly asks the character to remember the interaction; or
2. the interaction is the designated acceptance encounter and its model decision caused the demonstrated action.

Promotion is deterministic code. It stores promotion reason, participants, world/epoch, conversation/action/behavior IDs, and the complete ordered source `EventId`s. It does not require salience scoring, reflection, summary, tags, or relationship implications.

Retrieval is FTS/structured search over source utterances and event fields. The model receives labelled source excerpts plus uncertainty, never a database-console dump. Natural recall must affect conversation or behavior. SQL visibility alone is not acceptance.

## SQLite decision and transaction wrapper

DEC-005 establishes:

- WRK-002 pins Node before WRK-004 begins;
- WRK-004 first evaluates built-in `node:sqlite` on that exact runtime;
- it must pass WAL, foreign-key, explicit transaction/rollback, busy-timeout, FTS, online backup, separate-path restore, interruption, and repeated-start tests;
- current primary evidence shows `node:sqlite` as release-candidate API in Node 24.18 and includes an online `backup()` function, but evidence is re-read and smoke-tested when work starts;
- if any Gate-A requirement fails, the named fallback is `better-sqlite3`, with Python 3 and Visual Studio Build Tools “Desktop development with C++” included in Windows preflight;
- an IDE agent may not install or adopt any binding silently; fallback requires a DEC-005 amendment with exact failed probes.

Core sees a project-owned synchronous transaction wrapper:

```text
StorePort.withTransaction(operation)
  begin immediate
  execute prepared statements only
  commit
  on any error: rollback and return typed StoreError
```

All writes go through one in-process writer queue. Transactions are short and never contain model calls, network calls, pathfinding, or waits for behavior completion.

## Minimal schema and durability

WRK-004 creates only tables needed for Gate A:

`agents`, `principals`, `principal_aliases`, `worlds`, `world_epochs`, `world_sessions`, `events`, `conversations`, `utterances`, `model_runs`, `action_attempts`, `behavior_runs`, `encounters`, `encounter_events`, and `schema_metadata`.

WAL and foreign keys are enabled. Unique constraints cover all stable IDs plus adapter source dedupe. Backup uses the selected binding's online backup API; restore always targets a separate path, passes integrity/migration checks, and is never tested over the live database. Reset requires the explicit world ID, a confirmation token printed by the command, a pre-reset backup, and a new epoch for incompatible history.

Comprehensive retention, deletion, audit, correction, and migration governance belong to WRK-008/016.

## Restart reconciliation

On startup:

1. doctor/store integrity and migrations pass before Mineflayer connects;
2. open a new `WorldSessionId`;
3. resolve `WorldId`/`WorldEpoch` and authorized `PrincipalId` aliases;
4. mark unfinished model runs `INTERRUPTED`;
5. mark unfinished utterance submissions `UNKNOWN` without retry;
6. mark dispatching/active actions or behaviors `INTERRUPTED` or `UNKNOWN` based on their last phase;
7. gather a fresh same-epoch snapshot;
8. attach `reconciled` evidence only where the capability rule permits it;
9. record one explicit offline gap with wall-clock endpoints and no subjective events;
10. enter READY, then ACTIVE or SUSPENDED from observed presence.

No action, plan, provider session, pathfinder goal, or Minecraft entity object is blindly resumed.
