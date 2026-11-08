# Context, Authority, and Invariants

Registry: `blueprint.json`  
Artifact: ART-004  
Status: accepted

## System boundary

```text
Authorized player ──Minecraft chat/movement──> Paper/Minecraft
                                                │ authority for physical state
                                                ▼
                                      Mineflayer adapter (CMP-001)
                                      observations / commands only
                                                │ typed boundary
                                                ▼
┌──────────────────────── Agentic-World modular monolith ────────────────────────┐
│ CMP-002 perception     CMP-003 decision actor + sole speech owner             │
│ CMP-004 ModelPort      CMP-005 action/behavior coordinator                    │
│ CMP-006 StorePort      CMP-007 encounter/retrieval                            │
│ CMP-008 trigger gate   CMP-009 logs/health   CMP-010 local controls           │
│ CMP-011 persona-package reader                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
       │ structured request                │ transactions            │ read-only
       ▼                                   ▼                         ▼
OpenAI adapter/provider                  SQLite                  Parallax/Lattice
proposal authority only          durable local evidence       persona authority
```

The box is a modular monolith, not a set of network services. Ports are project-owned TypeScript contracts. Adapters parse unknown vendor data before it enters core logic.

## Authority ladder

1. **World fact:** Paper/Minecraft physical state, observed through an adapter with stated evidence limitations.
2. **Observation:** bounded, time-stamped, agent-scoped, possibly partial Mineflayer view.
3. **Durable source event:** a complete structured record of an eligible utterance, decision, action, dispatch, behavior, evidence, lifecycle, or restart event.
4. **Deterministic encounter:** a runtime-created grouping of source events under one of two Gate-A promotion rules.
5. **Belief or interpretation:** subjective, provenance-backed, replaceable, possibly wrong.
6. **Narration/utterance:** character expression, not evidence that anything happened.

No upward conversion is implicit. A model summary with perfect provenance can still misstate its sources. INV-013 therefore means **provenance or reject**, not “provenance equals truth.”

## Trust boundaries

| Boundary | Untrusted input | Required parse/validation | Forbidden pass-through |
| --- | --- | --- | --- |
| Mineflayer → core | packets, entities, usernames, session IDs, chat | closed `WorldObservation` union, bounds, alias mapping, epoch, dedupe | vendor objects or generic payload maps |
| Model provider → core | response text/tool data/refusal/usage | closed `ModelDecision`, one optional utterance, at most one Gate-A action | arbitrary tools, identity IDs, raw code, `finalSpeech` |
| Core → world | action/control/utterance request | runtime IDs, authorization, freshness, lease, deadline, length/syntax | raw commands, model-generated slash command, provider payload |
| Persona package → core | compiled context file | schema, reference, version, hash, size | mutation or provider session state |
| Local operator → core | package-script arguments | closed command union, exact target, confirmation where destructive | generic replacement or SQL fragment |
| SQLite → runtime | persisted records | schema version, constraints, WorldId/Epoch, integrity | rows from incompatible epoch as current truth |

## Invariant groups

The authoritative invariant registry and enforcement links are generated in `generated/registry.md`.

### Authority and evidence

- INV-001: Paper/Minecraft owns physical truth; Mineflayer is a channel.
- INV-002: narration/utterance cannot mutate physical state.
- INV-003: each capability declares minimum environment-derived evidence.
- INV-013: derived cognition keeps visible source provenance or is rejected; provenance is not faithfulness.

`EvidenceState` labels are not a universal total order:

- `unknown` — the runtime cannot determine whether the external effect occurred;
- `dispatch_acknowledged` — the adapter accepted the request, not proof of the intended effect;
- `client_observed` — the Mineflayer client observed a capability-relevant condition;
- `server_confirmed` — the environment supplied an authoritative confirmation for that capability;
- `reconciled` — a later observation resolved an earlier uncertain attempt under that capability's rule.

For Gate-A `follow_player`, a sequence of fresh client positions and active path state can establish `active`; distance/velocity plus cleared path controls can establish `completed` or `interrupted`. For `stop_behavior`, cleared path goal and no movement after the observation window can suffice. Those rules cannot be reused for ownership, item transfer, container mutation, crafting, or building.

### Identity and continuity

- INV-007: stable IDs prevent duplicate event, utterance, action, or behavior records/effects.
- INV-010: `AgentId`, `PrincipalId`, `WorldId`, and `WorldEpoch` outlive transport sessions.
- INV-018: an offline interval creates no subjective elapsed time or invented event.

Minecraft UUID, username, and session entity ID are aliases for a durable `PrincipalId`. UUID is preferred when authenticated; username is a configured alias for the local offline proof; session entity ID is presence evidence only and never authorization authority.

`WorldId` names the intended world continuity. `WorldEpoch` starts at 1. Compatible full stops/restarts keep it. An incompatible world replacement, reset, or restore allocates the next integer before new events. Old events remain queryable as history but cannot validate current actions or be described as current-world fact.

### Concurrency and suspension

- INV-006: one exclusive behavior lease per agent.
- INV-011: `SUSPENDED` overrides every cognitive trigger and physical behavior.
- INV-012: component health is independent of connection/availability.
- INV-016: exactly one player-visible utterance submission owner.
- INV-017: the actor serializes decisions/mutations, never physical duration.

The high-priority control path is separate from the ordinary actor mailbox. Stop, hazard, suspension, shutdown, and emergency stop can preempt an active behavior even while a provider call or ordinary event is pending.

### Deferred invariants

INV-014 (typed comprehensive operator correction) and INV-015 (second-real-adapter portability conformance) remain registered as `deferred`. Gate A contains neither a generic correction object nor a toy portability proof.

## Allowed dependency direction

```text
domain types
   ↑
application policy / actors / evidence rules
   ↑
project-owned ports
   ↑
Mineflayer / OpenAI / SQLite / persona / log adapters
   ↑
bootstrap and package-script command surface
```

Core packages never import Mineflayer, an OpenAI SDK, a SQLite binding, or persona-package filesystem code. Gate-A fakes implement ports to keep tests deterministic; they are not marketed as environments.

## Health axes

World adapter, model provider, store, and telemetry each report independently:

`OK | DEGRADED | UNAVAILABLE | FAULTED`

`DEGRADED` is never an agent lifecycle state. Examples:

- world `UNAVAILABLE` plus connection `DISCONNECTED` and availability `SUSPENDED`;
- model `UNAVAILABLE` while connection remains `READY` and deterministic presence remains healthy;
- telemetry `DEGRADED` while priority stop continues;
- store `FAULTED` prevents readiness and live cognition.

## Portability claim rule

Boundary independence is testable at Gate A; environment portability is not. Any statement that the system “can replace Minecraft without core changes” must be phrased as a future intent until WRK-014 supplies a second real adapter and records which abstractions had to change. The second adapter may revise contracts; Gate A must not freeze Minecraft's entity, inventory, or pathfinding model into a supposedly generic capability catalogue.
