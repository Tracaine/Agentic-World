# Generated Registry View

> Generated from `blueprint.json`; do not hand edit.

Blueprint revision: 2  
Project status: approved

## Requirements

| ID | Status | Priority | Summary | Acceptance | Work | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | accepted | P0 | Keep core policy independent of Minecraft/provider implementations without claiming demonstrated portability | Core imports no Mineflayer/OpenAI/SQLite implementation; fakes prove boundaries, not world portability. | WRK-001 | VER-001 |
| REQ-002 | accepted | P0 | Connect one stable named NPC to the empirically selected private Paper world | The same AgentId completes join, player-detection, disconnect, reconnect, and restart smoke gates using a dated compatibility record. | WRK-002 | VER-002 |
| REQ-003 | accepted | P0 | Produce a limited structured agent-scoped nearby perception | Only typed self, authorized-player, addressed-chat, bounded entity, position, connection, and behavior evidence enters core; suppressed observations carry reasons. | WRK-002 | VER-003 |
| REQ-004 | accepted | P0 | Hold an in-character conversation through one runtime-owned utterance-delivery path | One accepted addressed chat yields at most one player-visible submission attempt for its UtteranceId; unconfirmed delivery is unknown and is not retried. | WRK-003 | VER-004 |
| REQ-005 | accepted | P0 | Expose only typed validated Gate-A action and control capabilities | Gate A permits follow_player and stop_behavior plus emergency stop; no speech, raw commands, item mutation, building, crafting, or combat enters the physical action union. | WRK-003 | VER-005 |
| REQ-006 | accepted | P0 | Preserve causal conversation-to-action-to-evidence linkage | The acceptance request, model decision, ActionId, BehaviorId, behavior events, and capability-appropriate evidence share one causal chain; started is never success. | WRK-003, WRK-005 | VER-006 |
| REQ-007 | accepted | P0 | Persist event-grounded continuity across full shutdown and restart | Complete source events and one deterministic encounter survive restart and naturally affect later dialogue or behavior. | WRK-004 | VER-007 |
| REQ-008 | accepted | P0 | Separate world facts, bounded observations, subjective beliefs, source events, and model interpretations | Contracts and context label every epistemic category; a summary cannot replace or prove its source event. | WRK-001, WRK-004 | VER-008 |
| REQ-009 | accepted | P0 | Represent dispatch, activity, completion, failure, interruption, cancellation, timeout, and uncertainty honestly | Fault tests distinguish all states and never generalize movement evidence to authoritative mutation. | WRK-001, WRK-003, WRK-004 | VER-009 |
| REQ-010 | accepted | P0 | Suspend cognition and embodiment while the authorized player is absent without disconnecting a healthy client | Absence enters SUSPENDED, cancels cognition and behavior, retains only presence/connection/safety control, makes zero model calls, and resumes only after observed return. | WRK-003 | VER-010 |
| REQ-011 | accepted | P0 | Use deterministic trigger, safety, presence, queue, and behavior logic | Ambient events and routine movement make zero model calls; only Gate-A designated stimuli enqueue cognition. | WRK-001, WRK-003 | VER-011 |
| REQ-012 | deferred | P1 | Scale through a two-agent gate toward 8-10 separate characters | After Gate A, two-agent isolation passes before any 8-10-character load claim. | WRK-010, WRK-011 | VER-012 |
| REQ-013 | deferred | P1 | Enforce per-character knowledge and memory visibility boundaries | Post-proof two-agent fixtures prove private records do not cross without an explicit transmission event. | WRK-010 | VER-013 |
| REQ-014 | deferred | P1 | Maintain separate relationship belief goal intention and plan state per character | Post-proof schemas and behavior tests demonstrate independent, directional, versioned state. | WRK-015 | VER-014 |
| REQ-015 | accepted | P0 | Emit a minimal causal evidence trail across the Gate-A loop | An export joins principal/world/epoch/event/conversation/model/utterance/action/behavior/evidence IDs with redaction. | WRK-001, WRK-004, WRK-005 | VER-015 |
| REQ-016 | accepted | P0 | Provide owner-safe local diagnosis stop backup restore reset and evidence commands | Package scripts emit PASS/WARN/FAIL and perform safeguarded local operations; authenticated service and corrections remain deferred. | WRK-001, WRK-004 | VER-016 |
| REQ-017 | accepted | P0 | Provide minimal Gate-A migration integrity and safe backup/restore | Empty, repeat, backup, separate-path restore, integrity, and safeguarded reset checks pass; governance/deletion breadth is deferred. | WRK-004 | VER-017 |
| REQ-018 | accepted | P0 | Recover predictably from model adapter process restart and stale-behavior failures | Recovery tests yield typed interruption/unknown/reconciliation outcomes and never claim a disconnected client detects player return. | WRK-003, WRK-004 | VER-018 |
| REQ-019 | accepted | P0 | Maintain evidence-based resumption and bounded IDE-agent micro-steps | Every active package has exact files, prompt, commands, output, pass/fail, recovery, stop condition, and checkpoint evidence. | WRK-001 | VER-019 |
| REQ-020 | deferred | P1 | Add authoritative item and inventory mutations only after the defining proof | Post-proof capability-specific ownership, transfer, crash, and reconciliation tests pass. | WRK-012 | VER-020 |
| REQ-021 | deferred | P2 | Preserve an optional safe seam for LSL-inspired action tags or emotes | Any future notation is threat-modeled and compiles to existing typed capability/control boundaries without becoming a script executor. | WRK-013 | VER-021 |
| REQ-101 | accepted | P0 | Meet coherent Gate-A cognition response dispatch and control budgets | Canonical LIM-GA-001 through LIM-GA-007 separate outer response, model, dispatch, utterance, behavior, reevaluation, and priority-control budgets; the semantic guard verifies their required relationships. | WRK-003, WRK-005 | VER-101 |
| REQ-102 | deferred | P1 | Bound 8-10-agent concurrency and idle model calls | Post-proof capacity limits are set from measured two-agent behavior before ten-agent testing. | WRK-011 | VER-102 |
| REQ-103 | deferred | P1 | Enforce multi-level model cost and concurrency budgets | Post-proof run/session/daily budgets pass deterministic exhaustion tests; Gate A uses one timeout, stimulus suppression, and provider-side spend protection. | WRK-009 | VER-103 |
| REQ-104 | accepted | P0 | Meet Gate-A durability shutdown restart and restore targets | Committed events survive full stop, safety control precedes the LIM-GA-013 shutdown deadline, and a verified backup restores to a separate path. | WRK-004, WRK-005 | VER-104 |
| REQ-105 | accepted | P0 | Prevent secret private-context command-channel and accidental network exposure | Checks find no credentials in logs/prompts/data, no slash-command route, and no unapproved public listener. | WRK-001, WRK-002, WRK-003 | VER-105 |
| REQ-106 | accepted | P0 | Keep the default automated suite deterministic and network-free | Default tests pass twice with fakes, network denied, and zero live world/model calls. | WRK-001 | VER-106 |
| REQ-107 | deferred | P1 | Demonstrate portability only with a second materially different real environment adapter | No portability claim appears before the second real adapter passes revised conformance without freezing Minecraft-shaped abstractions. | WRK-014 | VER-107 |
| REQ-108 | accepted | P0 | Suppress uncontrolled Gate-A cognition stimuli | Only addressed authorized-player chat and designated result/restart events trigger; overflow/coalescing/suspension reasons are observable; absence produces zero calls. | WRK-003 | VER-108 |
| REQ-109 | accepted | P0 | Promote only deterministic Gate-A encounters | Promotion occurs only on an explicit remember request or the designated acceptance interaction that caused the demonstrated action. | WRK-004 | VER-109 |
| REQ-110 | accepted | P0 | Pass Gate A through the LIM-GA-014 consecutive machine-evidenced live repetitions and owner experiential approval | The LIM-GA-014 consecutive full meet-act-suspend-stop-restart-recall runs pass, and the owner records that the live character is worth continuing. | WRK-005 | VER-110 |
| REQ-111 | accepted | P0 | Use stable internal principal world epoch and causal identities | Authorization, participants, memory, action ownership, and restart records use internal IDs; Minecraft aliases map to PrincipalId; incompatible reset increments WorldEpoch. | WRK-001, WRK-004 | VER-111 |

## Invariants

| ID | Status | Summary | Enforcement | Verification |
| --- | --- | --- | --- | --- |
| INV-001 | accepted | Paper/Minecraft is authority for physical state; Mineflayer is an observation and command channel | Typed observation/evidence contracts and restart reconciliation | VER-201 |
| INV-002 | accepted | Model narration and utterance text cannot mutate physical state | Separate UtteranceProposal and ActionRequest unions; no narration executor | VER-202 |
| INV-003 | accepted | Action status advances only on the minimum environment-derived evidence required by that capability | CapabilityEvidence union and per-capability evidence threshold table | VER-203 |
| INV-004 | accepted | Every model run belongs to exactly one agent and scoped context | Per-agent actor, runtime-issued IDs, context schema | VER-204 |
| INV-005 | accepted | Private knowledge crosses agents only through explicit transmission | Viewer-aware visibility queries and source provenance | VER-205 |
| INV-006 | accepted | One agent has at most one exclusive long-running physical behavior lease | BehaviorId lease and high-priority control path | VER-206 |
| INV-007 | accepted | Duplicate event utterance action and behavior IDs cannot duplicate records or effects | Stable IDs, unique keys, one utterance attempt, idempotent lookup, and non-blind retry | VER-207 |
| INV-008 | accepted | Gate-A schema changes are ordered transactional and recorded; broad migration governance is deferred | Minimal migration ledger/checksum and WRK-004 tests | VER-208 |
| INV-009 | accepted | Models receive no raw commands code filesystem credentials or open network | Closed tool catalogue, no sandbox tools, dependency checks | VER-209 |
| INV-010 | accepted | Agent Principal World and WorldEpoch identities remain stable across transport sessions | Internal IDs and explicit alias/epoch mapping | VER-210 |
| INV-011 | accepted | SUSPENDED overrides every cognition trigger and permits no model call or physical behavior | Availability gate, abort signals, priority stop, and suppression telemetry | VER-211 |
| INV-012 | accepted | Dependency health is independent of agent connection and availability state | Four health axes; DEGRADED is never an exclusive lifecycle state | VER-212 |
| INV-013 | accepted | Derived interpretations require visible source-event provenance or are rejected; provenance does not prove faithfulness | Foreign-key/source visibility checks, source retention, contradiction and continuity fixtures | VER-213 |
| INV-014 | deferred | Comprehensive operator correction is deferred and may never falsify physical state | Future typed correction ADR and audit; no generic Gate-A replacement contract | VER-214 |
| INV-015 | deferred | World portability is not demonstrated until a second materially different real adapter passes a revised suite | WRK-014 gate; Gate A uses boundary fakes only | VER-215 |
| INV-016 | accepted | The runtime has exactly one player-visible utterance validation and submission owner | CMP-003 plus INT-011; no speak action, finalSpeech, tool callback, or blind retry | VER-216 |
| INV-017 | accepted | The actor serializes decisions and state mutation but never waits for physical behavior duration | Immediate dispatch result and later BehaviorEvent stream | VER-217 |
| INV-018 | accepted | No runtime means no subjective elapsed time or invented offline event | Restart gap marker and explicit unknown interval | VER-218 |

## Decisions

| ID | Status | Summary |
| --- | --- | --- |
| DEC-001 | accepted | Use a Minecraft-first modular monolith with revisable provider/environment seams |
| DEC-002 | accepted | Empirically select and pin the newest smoke-tested stable Paper/Mineflayer/pathfinder/Java/Node intersection |
| DEC-003 | accepted | Use strict TypeScript on an empirically pinned Node LTS with npm Zod and Vitest |
| DEC-004 | accepted | Keep provider-neutral ModelPort and use the simplest supported OpenAI structured-output adapter for Gate A |
| DEC-005 | accepted | Use SQLite WAL after Node is pinned; prefer verified node:sqlite and use named native fallback only if its Gate-A probes fail |
| DEC-006 | accepted | Use a per-agent decision actor plus independent asynchronous behavior leases and global cognition backpressure |
| DEC-007 | accepted | Keep a healthy Mineflayer client connected but enter SUSPENDED whenever the authorized player is absent |
| DEC-008 | accepted | Use loopback-isolated offline authentication only for local proof |
| DEC-009 | accepted | Use deterministic logic for routine embodiment and models only for designated cognitive stimuli |
| DEC-010 | accepted | Treat speech as a one-attempt runtime delivery workflow, never a physical ActionRequest |
| DEC-011 | accepted | Parallax/Lattice persona packages own authored character profile; Agentic-World owns only runtime identity and a versioned profile reference |
| DEC-012 | accepted | Prove continuity from complete durable events and deterministic encounters before model-authored memory |

## Questions

| ID | Status | Blocking | Summary | Resolution |
| --- | --- | --- | --- | --- |
| QST-001 | resolved | True | Which embodiment model boundary and absence behavior define the first proof? | Mineflayer embodiment; provider-neutral OpenAI-first structured adapter; healthy connected suspension while absent |
| QST-002 | open | False | What is the first NPC's canonical identity voice history values and starting relationship? | — |
| QST-003 | deferred | False | What do the owner's LSL scripts and action tags mean and what authority may they have? | — |
| QST-004 | deferred | False | Should durable memory or conversation retention differ from local defaults? | — |
| QST-005 | deferred | False | What should continue compress or pause while the owner is absent in a later phase? | — |
| QST-006 | open | False | Will the bot later join a LAN or remote authenticated server with a dedicated account? | — |
| QST-007 | resolved | True | Where is authored AgentProfile authority? | User-owned Parallax/Lattice persona package is authoritative; Agentic-World stores AgentId plus profile reference/version/hash and reads compiled context through INT-012. |

## Risks

| ID | Status | Summary | Trigger | Mitigation |
| --- | --- | --- | --- | --- |
| RSK-001 | active | Paper Mineflayer pathfinder Java or Node drift breaks progressive embodiment | Any gate after join fails or integration resumes after dependency/time drift | Re-read primary sources, record exact versions, and pass every SPIKE-000/WRK-002 progressive gate before cognition or persistence. |
| RSK-002 | active | Model proposes invalid unsafe or impossible action | Validation rejection rate exceeds ten percent | Untrusted typed proposals, closed catalogue, preconditions, limits, and observed results. |
| RSK-003 | active | Crash or disconnect after dispatch leaves an action or utterance outcome uncertain | Restart finds SUBMITTING, DISPATCHING, DISPATCHED, or ACTIVE without terminal evidence | Pre-dispatch durable intent, typed unknown state, capability-specific reconciliation, one utterance attempt, and no blind retry. |
| RSK-004 | active | Model-authored interpretation becomes a false durable memory | Interpretation lacks visible sources, contradicts invariant facts, or claims certainty beyond evidence | Persist source events first; deterministic encounter promotion; provenance-or-reject; contradiction/invention fixtures; summaries never replace sources. |
| RSK-005 | active | Provider latency or failure breaks conversational cadence | REQ-101 fails in two consecutive live samples or model health becomes unavailable | LIM-GA-002 remains inside LIM-GA-001, LIM-GA-016 controls retries, context is bounded, and failures are explicit. |
| RSK-006 | active | Prompt/history growth or retrieval failure erodes continuity | A release candidate misses the threshold twice after query/index tuning | Gate A uses the fixed retrieval/continuity suite and LIM-GA-018; compaction and semantic retrieval remain measured Gate-B mitigations. |
| RSK-007 | active | SQLite binding friction or contention delays proof | WRK-004 probe fails or write busy errors appear in Gate A | Pin Node first; prefer node:sqlite only after WAL/transaction/FTS/backup probes; explicit better-sqlite3 fallback/toolchain; short transactions. |
| RSK-008 | active | Private knowledge leaks between characters | VER-013 or VER-205 fails | Viewer-scoped queries, visibility labels, context manifests, adversarial two-agent gate. |
| RSK-009 | active | Offline-mode development server becomes network-exposed | Port reachable from another device/context | Loopback bind, firewall/LAN probe, authenticated online mode before shared hosting. |
| RSK-010 | active | Blueprint and code drift after interrupted sessions | Declared paths contracts or statuses disagree with repository evidence | One implementation-status file, generated registry views, micro-step checkpoints, strict structural validation, and semantic guard. |
| RSK-011 | active | Ambient stimuli or population growth creates uncontrolled model calls | Any call occurs while suspended or during the ordinary-event soak | Closed Gate-A trigger allowlist, coalescing, pending queue two, suppression telemetry, absence and ambient soak tests. |
| RSK-012 | active | LSL or action tags become an alternate unvalidated action channel | Any notation bypasses ActionGateway | Keep QST-003 deferred and require compilation into INT-004 plus threat model. |
| RSK-013 | active | Competing speech paths duplicate player-visible dialogue | More than one submission attempt for an UtteranceId | DEC-010, one CMP-003 delivery owner, UtteranceId, one attempt, semantic guard banned tokens, duplicate-speech regression. |
| RSK-014 | active | Lifecycle coupling falsely claims a disconnected client can detect player return | Any return transition lacks a READY presence observation | Orthogonal connection/availability states; keep healthy client connected during absence; separate disconnect tests. |
| RSK-015 | active | World restore or reset contaminates memories across incompatible history | World fingerprint changes without an explicit epoch decision | Stable WorldId, monotonic WorldEpoch, epoch-scoped events/encounters, reset confirmation and tests. |

## Components

| ID | Status | Summary | Requirements |
| --- | --- | --- | --- |
| CMP-001 | accepted | Minecraft World Adapter | REQ-002, REQ-003, REQ-009, REQ-010, REQ-018 |
| CMP-002 | accepted | Perception Normalizer | REQ-003, REQ-008, REQ-108 |
| CMP-003 | accepted | Agent Runtime Core and sole utterance-delivery owner | REQ-001, REQ-004, REQ-006, REQ-010, REQ-011, REQ-015, REQ-018, REQ-110 |
| CMP-004 | accepted | Model Gateway | REQ-004, REQ-011, REQ-101, REQ-105 |
| CMP-005 | accepted | Action and Behavior Coordinator | REQ-005, REQ-006, REQ-009, REQ-018, REQ-101 |
| CMP-006 | accepted | State Store | REQ-007, REQ-016, REQ-017, REQ-104, REQ-111 |
| CMP-007 | accepted | Continuity, Memory, and Belief Service | REQ-007, REQ-008, REQ-109 |
| CMP-008 | accepted | Stimulus, Scheduler, and Budget Policy | REQ-010, REQ-011, REQ-108 |
| CMP-009 | accepted | Causal Logs and Minimal Health | REQ-015, REQ-016, REQ-101, REQ-105 |
| CMP-010 | accepted | Local Operator Command Surface | REQ-016, REQ-018, REQ-019 |
| CMP-011 | accepted | Persona Package Adapter | REQ-004, REQ-111 |

## Interfaces

| ID | Status | Summary | From | To | Contract |
| --- | --- | --- | --- | --- | --- |
| INT-001 | accepted | Typed world observation stream | CMP-001 | CMP-002 | WorldObservation union v2 in ART-017 |
| INT-002 | accepted | Bounded fresh self/world query | CMP-003, CMP-005 | CMP-001 | WorldQueryRequest and WorldSnapshot union v2 in ART-017 |
| INT-003 | accepted | Bounded structured model decision | CMP-003 | CMP-004 | CognitionRequest ModelDecision and ModelRunResult v2 in ART-017 |
| INT-004 | accepted | Typed Gate-A action proposal | CMP-003 | CMP-005 | GateAActionProposal ActionRequest and validation result v2 in ART-017 |
| INT-005 | accepted | Validated behavior/control dispatch | CMP-005 | CMP-001 | BehaviorDispatchRequest ControlRequest and ImmediateDispatchResult v2 in ART-017 |
| INT-006 | accepted | Asynchronous behavior and capability evidence events | CMP-001 | CMP-005 | BehaviorEvent and CapabilityEvidence unions v2 in ART-017 |
| INT-007 | accepted | Scoped encounter retrieval and derived cognition seam | CMP-003, CMP-010 | CMP-007 | EncounterQuery EncounterBundle and DerivedInterpretationProposal v2 in ART-017 |
| INT-008 | accepted | Domain store and transaction port | CMP-003, CMP-005, CMP-007, CMP-010 | CMP-006 | GateAStorePort TransactionPort and StoreError v2 in ART-017 |
| INT-009 | accepted | Redacted causal telemetry and component health | CMP-001, CMP-002, CMP-003, CMP-004, CMP-005, CMP-006, CMP-007, CMP-008, CMP-010, CMP-011 | CMP-009 | CausalSignal and ComponentHealth v2 in ART-017 |
| INT-010 | accepted | Typed local operator control | CMP-010 | CMP-003, CMP-005, CMP-006 | OperatorCommand and OperatorResult closed unions v2 in ART-017 |
| INT-011 | accepted | One-attempt player-visible utterance submission | CMP-003 | CMP-001 | ValidatedUtterance and UtteranceSubmissionResult v2 in ART-017 |
| INT-012 | accepted | Versioned persona package read | CMP-003 | CMP-011 | PersonaPackageRequest and CompiledPersonaContext v1 in ART-017 |

## Data

| ID | Status | Summary | Owner | Persistence |
| --- | --- | --- | --- | --- |
| DAT-001 | accepted | CharacterIdentityRecord: stable AgentId, display name, and Parallax/Lattice profile ref/version/hash | CMP-003 | SQLite durable in Gate A |
| DAT-002 | accepted | AgentRuntimeState: orthogonal connection, availability, component health, and active run/action/behavior IDs | CMP-003 | In-memory through WRK-003; durable transition events in WRK-004 |
| DAT-003 | accepted | WorldSession: adapter connection interval and compatibility record | CMP-001 | SQLite durable in Gate A |
| DAT-004 | accepted | DurableEvent: complete typed player/NPC utterance, action, dispatch, behavior, evidence, lifecycle, and restart source event | CMP-002 | SQLite durable append-only in Gate A |
| DAT-005 | accepted | PerceptionSnapshot: bounded expiring self/world view | CMP-002 | In-memory Gate A; optional rebuildable persistence later |
| DAT-006 | accepted | BeliefRecord: subjective sourced proposition | CMP-007 | Architectural seam only until Gate B |
| DAT-007 | accepted | EpisodicMemory: replaceable model-authored interpretation over source events | CMP-007 | Deferred Gate-B SQLite record |
| DAT-008 | accepted | RelationshipRecord: directional sourced social interpretation | CMP-007 | Deferred Gate-B SQLite record |
| DAT-009 | accepted | GoalPlanRecord: goals intentions and plans | CMP-003 | Deferred Gate-B SQLite record |
| DAT-010 | accepted | ConversationUtterance: delivered player chat and NPC utterance proposal/delivery state | CMP-003 | SQLite durable in Gate A |
| DAT-011 | accepted | ActionAttempt: typed proposal validation dispatch and evidence-linked outcome | CMP-005 | SQLite durable in Gate A |
| DAT-012 | accepted | ModelRun: bounded provider execution and structured ModelDecision | CMP-004 | SQLite durable metadata in Gate A |
| DAT-013 | accepted | OperatorAudit: comprehensive operator governance record | CMP-010 | Deferred Gate B |
| DAT-014 | accepted | SchemaMetadata: migration ID checksum application and SQLite binding record | CMP-006 | SQLite durable in Gate A |
| DAT-015 | accepted | PrincipalIdentity: durable PrincipalId plus authorized roles and Minecraft UUID/username/session-entity aliases | CMP-006 | SQLite durable in Gate A |
| DAT-016 | accepted | WorldIdentity: stable WorldId and monotonic WorldEpoch | CMP-006 | SQLite durable in Gate A |
| DAT-017 | accepted | BehaviorRun: long-running follow lease and asynchronous event lifecycle | CMP-005 | SQLite durable in Gate A |
| DAT-018 | accepted | EncounterRecord: deterministic grouping of complete source events for recall | CMP-007 | SQLite durable plus rebuildable FTS in Gate A |

## Flows

| ID | Status | Summary |
| --- | --- | --- |
| FLW-001 | accepted | Start, connect, synchronize, and become ACTIVE or SUSPENDED |
| FLW-002 | accepted | Addressed chat produces one model decision, one utterance attempt, and optional asynchronous action |
| FLW-003 | accepted | Fail, interrupt, or remain uncertain honestly |
| FLW-004 | accepted | Shutdown, restart, retrieve, and use event-grounded continuity |
| FLW-005 | accepted | Model provider degrades without corrupting embodiment |
| FLW-006 | accepted | Preserve future multi-agent knowledge boundaries |
| FLW-007 | accepted | Resume development from evidence |
| FLW-008 | accepted | Suspend on absence and resume only from observed return |
| FLW-009 | accepted | High-priority stop and emergency stop |
| FLW-010 | accepted | Run progressive compatibility spike and production pin |
| FLW-011 | accepted | Reset, restore, and advance WorldEpoch safely |

## Verifications

| ID | Status | Summary | Target | Method | Evidence |
| --- | --- | --- | --- | --- | --- |
| VER-001 | accepted | Verify Minecraft-first dependency seams without portability overclaim | REQ-001 | Static import boundary plus fake port contract tests; scan claims | Boundary report and zero Gate-A portability assertions |
| VER-002 | accepted | Verify empirical NPC compatibility gates | REQ-002 | SPIKE-000 and WRK-002 progressive live smoke | Dated compatibility record and logs beyond join |
| VER-003 | accepted | Verify bounded closed-union perception | REQ-003 | Fixture/property tests and ambient suppression soak | Accepted/rejected counts with reasons |
| VER-004 | accepted | Verify one in-character utterance delivery path | REQ-004 | Fake/live conversation and duplicate-attempt fault tests | UtteranceId trace with at most one attempt |
| VER-005 | accepted | Verify Gate-A action/control union | REQ-005 | Schema exhaustiveness and adversarial validation | No speech/item/build/combat member; rejects recorded |
| VER-006 | accepted | Verify causal asynchronous conversation-action loop | REQ-006 | Live follow/stop plus trace join | Decision, ActionId, BehaviorId and later evidence chain |
| VER-007 | accepted | Verify event-grounded restart continuity | REQ-007 | Full server/runtime stop, restart, retrieval, and live dialogue | Source events, encounter query, and owner-rated natural recall |
| VER-008 | accepted | Verify epistemic type separation | REQ-008 | Type/schema/context snapshot tests | Separate fact/observation/belief/event/interpretation sections |
| VER-009 | accepted | Verify honest action behavior and utterance uncertainty | REQ-009 | Phase-by-phase fault matrix | Distinct dispatched/active/terminal/unknown records |
| VER-010 | accepted | Verify connected absence suspension | REQ-010 | Presence leave/return, disconnect, restart, and shutdown tests | Zero absence calls; return only from READY observation |
| VER-011 | accepted | Verify deterministic Gate-A gating | REQ-011 | Ambient movement/entity/proximity soak | Zero model calls and suppression reasons |
| VER-012 | accepted | Verify deliberate two-then-ten scale | REQ-012 | Deferred Gate-B load gate | Two-agent evidence precedes ten-agent evidence |
| VER-013 | accepted | Verify per-agent knowledge boundaries | REQ-013 | Deferred adversarial two-agent fixtures | No unauthorized retrieval |
| VER-014 | accepted | Verify separate rich character state | REQ-014 | Deferred schema/behavior suite | Independent directional state |
| VER-015 | accepted | Verify causal log completeness | REQ-015 | Export one defining trace and validate required IDs | Machine-readable manifest plus human-readable timeline |
| VER-016 | accepted | Verify owner-safe Gate-A command surface | REQ-016 | Command integration tests on temporary paths | PASS/WARN/FAIL doctor and safe operation transcripts |
| VER-017 | accepted | Verify minimal migrations backup restore and reset | REQ-017 | Empty/repeat/integrity/backup/separate-restore/reset tests | Checksums and original-data preservation |
| VER-018 | accepted | Verify bounded recovery | REQ-018 | Model timeout, link loss, process stop, stale behavior, restart tests | Typed terminal/unknown/reconciled outcomes |
| VER-019 | accepted | Verify micro-step project resumption | REQ-019 | Fresh-agent handoff drill | Exact next command selected from artifacts |
| VER-020 | accepted | Verify authoritative item capabilities | REQ-020 | Deferred Gate-B mutation suite | Capability-specific ownership/transfer evidence |
| VER-021 | deferred | Verify action tags cannot bypass boundaries | REQ-021 | Deferred threat model and fake dispatch | No script executor or alternate authority |
| VER-101 | accepted | Verify coherent time budgets | REQ-101 | Fake-clock unit tests and live p95 sample | 6000 < 8000 with 2000 margin; dispatch/control SLOs |
| VER-102 | accepted | Verify future capacity/backpressure | REQ-102 | Deferred measured load suite | Limits selected after two-agent evidence |
| VER-103 | accepted | Verify future multi-level budgets | REQ-103 | Deferred deterministic exhaustion suite | Run/session/daily gates |
| VER-104 | accepted | Verify Gate-A durability shutdown restart and restore | REQ-104 | Kill/clean stop/restart/restore on temp copy | No fabricated completion and verified integrity |
| VER-105 | accepted | Verify secrets command and network boundaries | REQ-105 | Static scans, redaction fixtures, listener probe | Zero leaked credential or raw command route |
| VER-106 | accepted | Verify deterministic network-free defaults | REQ-106 | Run default suite twice with network blocked | Identical pass with zero external calls |
| VER-107 | accepted | Verify second real adapter before portability claim | REQ-107 | Deferred WRK-014 conformance and claim review | Second materially different adapter evidence |
| VER-201 | accepted | Verify world physical authority | INV-001 | Reject external physical write and reconcile stale projection | tests/contract/world-authority |
| VER-202 | accepted | Verify narration has no world authority | INV-002 | Inject action-like tags and claims into speech | tests/contract/narration-authority |
| VER-203 | accepted | Verify capability-specific evidence thresholds | INV-003 | Evidence matrix tests | Movement accepts client_observed; authoritative mutation does not |
| VER-204 | accepted | Verify one-agent run scope | INV-004 | Cross-wire agent and run IDs | tests/unit/context-isolation |
| VER-205 | accepted | Verify explicit knowledge transmission | INV-005 | Query B for A-private fact before and after speech transmission | evidence/WRK-010/knowledge-boundary-report.json |
| VER-206 | accepted | Verify one exclusive behavior lease | INV-006 | Concurrency/preemption tests | No overlapping exclusive behavior; stop bypasses queue |
| VER-207 | accepted | Verify event utterance action and behavior idempotency | INV-007 | Duplicate/restart injection | No duplicate records, speech attempts, or effects |
| VER-208 | accepted | Verify migration immutability | INV-008 | Change applied checksum and restart | evidence/WRK-003/migration-test-report.txt |
| VER-209 | accepted | Verify forbidden model capabilities are absent | INV-009 | Prompt and schema tests for console shell file network and credentials | evidence/WRK-008/security-report.txt |
| VER-210 | accepted | Verify stable Agent/Principal/World/Epoch identity | INV-010 | Alias/restart/reset/restore fixtures | Internal IDs and epoch behavior match contracts |
| VER-211 | accepted | Verify SUSPENDED suppression | INV-011 | Absence and noisy-world soak | Zero cognition/model/behavior activity |
| VER-212 | accepted | Verify orthogonal health and lifecycle | INV-012 | State-model transition tests | Dependency degradation never becomes exclusive agent state |
| VER-213 | accepted | Verify provenance-or-reject continuity discipline | INV-013 | Unsourced/invisible/contradictory fixture tests | Rejects plus retained complete sources |
| VER-214 | accepted | Verify future typed operator correction | INV-014 | Deferred Gate-B correction suite | No generic replacement contract |
| VER-215 | accepted | Verify deferred portability conformance | INV-015 | Deferred second-adapter review | No Gate-A toy-adapter proof claim |
| VER-108 | accepted | Verify Gate-A stimulus suppression | REQ-108 | Addressed/non-addressed, duplicate, coalescing, cooldown, overflow, ambient, and suspended tests | Trigger/suppression reason counts and zero forbidden calls |
| VER-109 | accepted | Verify deterministic encounter promotion | REQ-109 | Explicit-remember, designated-acceptance, and ordinary-chat fixtures | Only two eligible reasons create EncounterRecord |
| VER-110 | accepted | Verify the LIM-GA-014 consecutive defining live proofs and owner judgment | REQ-110 | LIM-GA-014 full meet-act-suspend-stop-restart-recall repetitions | One verified manifest, machine check set, media index, and signed owner experiential rubric per required repetition |
| VER-111 | accepted | Verify principal and world epoch semantics | REQ-111 | UUID/username/session alias plus compatible/incompatible restart/reset/restore matrix | Stable PrincipalId/WorldId and monotonic epoch report |
| VER-216 | accepted | Verify single speech ownership | INV-016 | Static banned-path scan and duplicate fault suite | Only INT-011 submits and each UtteranceId has <=1 attempt |
| VER-217 | accepted | Verify actor never awaits behavior duration | INV-017 | Fake long follow while processing stop and later addressed chat | Immediate started result, free mailbox, and priority stop latency |
| VER-218 | accepted | Verify no invented offline time or events | INV-018 | Clock-gap restart fixtures | Explicit offline gap with no subjective elapsed-time event |
