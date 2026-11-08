# Components and Topology

Registry: `blueprint.json`  
Artifact: ART-006  
Status: accepted

## Reference topology

Gate A is one local TypeScript process plus Paper:

```text
Windows host
├─ Paper Java process
│  └─ private/loopback world
├─ Agentic-World Node process (modular monolith)
│  ├─ core domain + application
│  ├─ Mineflayer adapter
│  ├─ OpenAI adapter behind ModelPort
│  ├─ SQLite adapter behind StorePort
│  ├─ local persona-package reader
│  └─ local logs / package-script controls
├─ data/agentic-world.sqlite
├─ data/backups/
├─ logs/
└─ evidence/
```

No broker, container orchestrator, microservice mesh, remote admin API, metrics stack, vector database, or custom dashboard is required.

## Component ownership

| ID | Component | Owns now | Explicitly does not own |
| --- | --- | --- | --- |
| CMP-001 | Minecraft World Adapter | connection, queries, physical dispatch, observations/evidence, raw chat-send method | cognition, speech policy/dedupe, memory, success invention |
| CMP-002 | Perception Normalizer | closed observation parsing, identity alias mapping, bounds/dedupe | wake policy, belief, omniscience |
| CMP-003 | Agent Runtime Core | decision actor, orthogonal state coordination, context, **sole utterance workflow**, causal loop | vendor APIs, physical duration, a second speech path |
| CMP-004 | Model Gateway | provider adaptation, one structured decision, deadline/refusal/usage | tool callback that waits for follow, speech submission, world mutation |
| CMP-005 | Action/Behavior Coordinator | validation, leases, immediate dispatch, behavior events, evidence rules, priority control | speech or raw commands |
| CMP-006 | State Store | transaction wrapper, minimal SQLite, integrity, backup/restore/reset | domain decisions, implicit binding choice |
| CMP-007 | Continuity/Memory | deterministic encounter and retrieval; later interpretations | Gate-A autonomous salience, world truth |
| CMP-008 | Stimulus/Scheduler | trigger allowlist, suspension gate, coalescing, queue, cooldowns, behavior timers | prose or physical execution |
| CMP-009 | Logs/Health | causal logs, four health axes, doctor/evidence export | domain mutation, enterprise telemetry |
| CMP-010 | Local Operator Surface | local typed control and safe data commands | generic replacement, public service, raw SQL |
| CMP-011 | Persona Package Adapter | read/verify one compiled Parallax/Lattice persona artifact | profile mutation or runtime state |

The full responsibility/prohibition mapping is canonical in `blueprint.json` and generated in `generated/registry.md`.

## Decision actor and asynchronous work

The per-agent actor owns ordering for:

- accepting/suppressing stimuli;
- availability and attention state mutation;
- context assembly;
- starting/cancelling a model run;
- accepting one `ModelDecision`;
- assigning stable IDs;
- initiating independent utterance and action workflows;
- applying later behavior results when they require state interpretation.

It does **not** hold its mailbox while:

- Mineflayer follows a player;
- pathfinding recalculates;
- a behavior waits for timeout;
- a stop observation window completes;
- SQLite backup copies pages.

Long-running work publishes typed later events. The actor handles them as new stimuli only if the Gate-A trigger policy designates them meaningful.

## Priority control lane

```text
operator/player safety signal
          │
          ▼
high-priority ControlRequest queue (not ordinary cognition mailbox)
          │
          ▼
CMP-005 cancels lease + CMP-001 clears path/movement
          │
          ▼
ImmediateDispatchResult, then capability evidence/BehaviorEvent
```

Sources are `stop_behavior`, `emergency_stop`, hazard policy, suspension entry, shutdown, or connection failure. A provider call cannot block this path. Dispatch uses `LIM-GA-007` (`priority_control_dispatch_slo_ms`); adapter confirmation may arrive later and is recorded separately.

## Speech lane

```text
ModelDecision.utterance?
       │
       ▼
CMP-003 validate text/identity/state ──reject──> durable rejected result
       │
       ├─ assign and persist UtteranceId/intention
       ▼
INT-011 exactly one submission attempt
       │
       ├─ confirmed delivered
       └─ rejected / unknown (no blind retry)
```

There is no `speak` physical action, model tool callback, `finalSpeech`, post-run fallback-send, or action retry route. The adapter exposes a send mechanism but owns neither delivery policy nor idempotency.

## Dependency rules

- `src/core/domain` imports only project-owned types.
- `src/core/application` imports domain and port interfaces.
- `src/ports` imports domain types and Zod schemas.
- `src/adapters/*` imports ports plus its vendor/library.
- `src/bootstrap` selects adapters and configuration.
- adapters never import one another;
- model adapter never imports Mineflayer or SQLite adapter;
- core never imports vendor SDKs;
- tests/fakes may implement ports but cannot be cited as environment-portability proof.

WRK-001 enforces these with an import-boundary test.

## Failure isolation

| Failure | Connection | Availability | Health | Immediate policy |
| --- | --- | --- | --- | --- |
| Model timeout | unchanged | usually ACTIVE | model DEGRADED/UNAVAILABLE | fail run; no retry; keep deterministic safety/presence |
| Mineflayer disconnect | DISCONNECTED | SUSPENDED | world UNAVAILABLE | priority stop; capped reconnect; no return detection |
| Paper restart | DISCONNECTED then CONNECTING/SYNCING | SUSPENDED | world transitions | new session; same epoch only if compatible; reconcile |
| Store integrity failure | may remain OFFLINE/SYNCING | SUSPENDED | store FAULTED | prevent READY; preserve data; restore only to separate path |
| Telemetry failure | unchanged | unchanged | telemetry DEGRADED | count/drop permitted debug only; priority control continues |
| Persona missing/hash mismatch | READY possible | SUSPENDED | model path UNAVAILABLE | no live cognition; deterministic controls remain |

## Future extraction rule

Components are logical boundaries inside one process. Network extraction is allowed only after measured need and a new decision. Environment replacement may revise the ports. The architecture intentionally avoids a frozen, supposedly universal action registry based on Minecraft concepts.
