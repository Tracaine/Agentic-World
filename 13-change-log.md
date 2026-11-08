# Blueprint Revision 2 — ID Change and Coverage Log

Registry: `blueprint.json`  
Artifact: ART-034  
Patch date: 2026-07-17

This is the coverage map used before and during the patch. IDs are preserved when their concern survives. “Recast” means the approved revision changed an unimplemented planning slot; the former meaning is named and moved rather than silently erased.

## Requirements

| IDs | Disposition |
| --- | --- |
| REQ-001 | altered: boundary independence retained; toy-adapter portability acceptance retired; proof moved to REQ-107/WRK-014 |
| REQ-002–003 | altered: hard version removed; progressive real embodiment and closed bounded perception moved to WRK-002 |
| REQ-004 | altered: single runtime utterance owner, one attempt, unknown-on-unconfirmed |
| REQ-005–006 | altered: Gate-A union narrowed to follow/stop; asynchronous causal action/evidence |
| REQ-007–008 | altered: complete source events and deterministic encounter precede interpretations |
| REQ-009 | altered: explicit dispatched/active/terminal/unknown distinctions and capability evidence |
| REQ-010 | altered: healthy client remains connected during SUSPENDED; no grace-period cognition |
| REQ-011 | altered: closed deterministic Gate-A triggers and routine behavior |
| REQ-012–014 | moved to Gate B: multi-agent scale, knowledge boundaries, rich per-character state |
| REQ-015 | narrowed: minimal causal proof logs rather than generalized trace infrastructure |
| REQ-016–017 | narrowed: local diagnosis/control/backup/restore/reset now; governance/deletion/correction later |
| REQ-018–019 | altered: honest bounded recovery plus literal micro-step resumption evidence |
| REQ-020 | moved to WRK-012 after proof; authoritative item/inventory workflows excluded from Gate A |
| REQ-021 | preserved as speculative seam; LSL/action tags remain deferred under QST-003/WRK-013 |
| REQ-101 | corrected: canonical `LIM-GA-001`–`LIM-GA-007` separate cognition, dispatch, behavior, and priority-control budgets |
| REQ-102–103 | moved to Gate B: population and multi-level budgets |
| REQ-104–106 | narrowed to Gate-A durability/shutdown/security/deterministic suite |
| REQ-107 | altered and deferred: only a second materially different real adapter can prove portability |
| REQ-108 | added: stimulus suppression/coalescing/queue/absence proof |
| REQ-109 | added: deterministic encounter promotion |
| REQ-110 | added: `LIM-GA-014` consecutive live proofs plus owner judgment |
| REQ-111 | added: stable principal/world/epoch/causal identities |

## Invariants

| IDs | Disposition |
| --- | --- |
| INV-001–002 | clarified: Paper authority, Mineflayer channel, utterance/narration non-authority |
| INV-003 | corrected: capability-minimum environment evidence replaces universal adapter/server confirmation |
| INV-004–005 | preserved; full multi-agent visibility verification deferred with Gate B |
| INV-006 | altered: exclusive behavior lease, not an actor held in ACTING |
| INV-007 | expanded to event/utterance/action/behavior idempotency |
| INV-008 | narrowed: minimal migration integrity now; governance later |
| INV-009 | preserved: no raw model commands/code/files/network/credentials |
| INV-010 | expanded: Agent/Principal/World/Epoch identity |
| INV-011 | strengthened: SUSPENDED overrides all cognition/behavior triggers |
| INV-012 | corrected: dependency health is orthogonal; DEGRADED is not lifecycle |
| INV-013 | corrected: provenance-or-reject; provenance is not proof of faithfulness |
| INV-014–015 | moved to Gate B: typed correction and real-adapter conformance |
| INV-016 | added: exactly one speech owner/path |
| INV-017 | added: actor never waits for physical duration |
| INV-018 | added explicitly: no runtime means no subjective time/offline events |

## Decisions

| ID | Disposition |
| --- | --- |
| DEC-001 | altered: Minecraft-first revisable seams; no Gate-A portability claim |
| DEC-002 | superseded fixed Paper/Java version with empirical intersection and progressive gates |
| DEC-003 | altered: exact Node pinned by WRK-002 before storage |
| DEC-004 | superseded mandatory Agents SDK with simplest supported structured ModelPort adapter; SDK optional |
| DEC-005 | resolved: node:sqlite probes after Node pin; better-sqlite3 named fallback/toolchain; no silent choice |
| DEC-006 | superseded duration-holding actor/tool loop with async behavior leases and priority control |
| DEC-007 | superseded “suspend and disconnect” with connected suspension and honest OFFLINE/DISCONNECTED |
| DEC-008 | preserved with empirical auth option and strict local/private boundary |
| DEC-009 | strengthened: closed Gate-A cognitive trigger policy |
| DEC-010 | added: one-attempt speech workflow separate from actions |
| DEC-011 | added: Parallax/Lattice persona-package ownership |
| DEC-012 | added: event-grounded deterministic continuity |

## Assumptions and questions

| IDs | Disposition |
| --- | --- |
| ASM-001–002, ASM-004–007 | preserved, validation moved to SPIKE-000/WRK-002 where relevant |
| ASM-003 | narrowed to explicit live model steps and safe credential warning/stop |
| ASM-008 | altered to named external persona-package fixture |
| QST-001 | resolution updated to connected suspension |
| QST-002 | preserved as non-blocking character-content approval |
| QST-003 | preserved: LSL/action-tag meaning/authority deferred |
| QST-004–006 | preserved and moved to Gate-B/nonlocal decision points |
| QST-007 | added/resolved from prior Parallax/Lattice material; removes AgentProfile blocker |

## Risks

| IDs | Disposition |
| --- | --- |
| RSK-001 | altered: progressive protocol/embodiment gates and time/drift recheck |
| RSK-002 | preserved: invalid model proposal bounded by closed validation |
| RSK-003 | expanded: uncertain utterance/action/behavior after dispatch/restart |
| RSK-004 | altered: source events + deterministic encounter; summaries never replace sources |
| RSK-005 | corrected coherent model/outer budgets and zero retry |
| RSK-006 | defined with versioned fixtures, `LIM-GA-018`, and measured compaction |
| RSK-007 | altered: binding/toolchain friction plus SQLite probe criteria |
| RSK-008–009 | preserved for later multi-agent/privacy/network scope |
| RSK-010 | expanded: one status source, generated views, semantic guard |
| RSK-011 | altered: Gate-A ambient/absence stimulus storm risk |
| RSK-012 | preserved: action tags cannot bypass typed boundary |
| RSK-013 | added: duplicate speech paths |
| RSK-014 | added: dishonest disconnected return detection |
| RSK-015 | added: world epoch contamination |

## Components and interfaces

| IDs | Disposition |
| --- | --- |
| CMP-001–002 | altered: adapter is channel/parser boundary; no speech policy or generic objects |
| CMP-003 | altered: orthogonal coordinator and sole utterance owner |
| CMP-004 | altered: one structured decision; no duration-holding callback |
| CMP-005 | altered: action/behavior coordinator with priority control/evidence rules |
| CMP-006 | narrowed to Gate-A store/ops; binding independent |
| CMP-007 | narrowed to deterministic encounter/retrieval; derived cognition later |
| CMP-008 | altered to stimulus gate/queue/coalescing/suspension policy |
| CMP-009 | narrowed to causal logs, doctor, and independent health |
| CMP-010 | narrowed to closed local commands; generic correction removed |
| CMP-011 | added: read-only Parallax/Lattice persona-package adapter |
| INT-001–002 | closed typed observation/snapshot schemas |
| INT-003 | corrected to one `ModelDecision` |
| INT-004 | physical action proposals only; speech removed |
| INT-005–006 | corrected to immediate dispatch plus asynchronous behavior/evidence events |
| INT-007 | altered to deterministic encounter retrieval plus Gate-B interpretation seam |
| INT-008–009 | narrowed store and causal telemetry contracts |
| INT-010 | generic replacement/correction removed from Gate A |
| INT-011 | added: one-attempt utterance submission |
| INT-012 | added: persona package read |

## Data and state

| IDs | Disposition |
| --- | --- |
| DAT-001 | recast from internally owned AgentProfile to runtime identity + external profile reference/hash |
| DAT-002 | corrected to orthogonal state projection |
| DAT-003–005 | altered for session/epoch, complete events, and in-memory bounded snapshot |
| DAT-006–009 | preserved but deferred: belief, model-authored memory, relationship, goal/plan |
| DAT-010 | expanded to player-delivered and NPC proposal/delivery lifecycle |
| DAT-011 | expanded to dispatch/active/terminal/unknown action lifecycle |
| DAT-012 | narrowed to one structured model decision/run metadata |
| DAT-013 | preserved but deferred comprehensive operator audit |
| DAT-014 | narrowed Gate-A migration/binding record |
| DAT-015 | added: PrincipalIdentity and Minecraft aliases |
| DAT-016 | added: WorldId/WorldEpoch |
| DAT-017 | added: BehaviorRun |
| DAT-018 | added: deterministic EncounterRecord |

## Flows and verification

| IDs | Disposition |
| --- | --- |
| FLW-001 | corrected startup to orthogonal connection/availability |
| FLW-002 | corrected step 9: no terminal follow wait; speech/action independent; later events |
| FLW-003–005 | altered for typed uncertainty, event-grounded restart, independent model health |
| FLW-006 | preserved and deferred multi-agent visibility |
| FLW-007 | expanded evidence-based micro-step resume |
| FLW-008 | superseded disconnect-on-absence with connected suspension; separate return/disconnect/restart/shutdown |
| FLW-009 | recast as high-priority stop/emergency stop |
| FLW-010 | recast as progressive compatibility spike/pin |
| FLW-011 | added: safe reset/restore/epoch |
| VER-001–021 | corresponding functional verifications altered/deferred with their requirements |
| VER-101–107 | quality verifications corrected; portability/budgets deferred as appropriate |
| VER-201–215 | invariant tests updated for evidence/state/identity; correction/conformance deferred |
| VER-108–111 | added: suppression, encounter promotion, repeated proof, epoch identity |
| VER-216–218 | added: one speech owner, nonblocking behavior actor, no offline invention |

## Work packages

| ID | Disposition |
| --- | --- |
| SPIKE-000 | added before production; disposable compatibility/feasibility proof, including a separate owner-approved exact Node/Java install/verify step |
| WRK-001 | altered: thin contracts/fakes/in-memory causal loop; no portability toy adapter |
| WRK-002 | expanded: production version pin plus presence/chat/perception/movement/stop |
| WRK-003 | recast from persistence to model decision, one utterance, async follow/stop/suspension; now depends on WRK-002 |
| WRK-004 | recast from world adapter to minimal SQLite continuity; old world work moved to WRK-002; now depends on Node pin and WRK-003 |
| WRK-005 | recast from conversation-only to the `LIM-GA-014` repeated defining proofs; old conversation work moved to WRK-003 |
| WRK-006 | recast from action loop to versioned experience regression hardening |
| WRK-007 | narrowed/split: measured derived memory/compaction/semantic retrieval only |
| WRK-008 | narrowed/split: authenticated operator/audit/deletion/correction only |
| WRK-009 | recast from defining proof (moved to WRK-005) to generalized readiness/observability/budgets |
| WRK-010–011 | preserved, deferred second-character then 8–10 scale |
| WRK-012 | preserved, broadened authoritative item/inventory/container workflow, deferred |
| WRK-013 | preserved speculative LSL/action-tag/emote design |
| WRK-014 | added: second real adapter/portability assessment |
| WRK-015 | added: rich social cognition/goals/plans/scheduling split |
| WRK-016 | added: exhaustive mutation recovery/migration governance split |

## Artifacts and drafting

- ART-001–018 retained; meanings updated in place where affected.
- ART-019–031 retained as stable work-file artifact IDs; summaries updated to recut package meanings.
- ART-032–042 added for SPIKE, Windows runbook, change log, Gate map, generator, semantic guard, generated views/validation record, and WRK-014–016.
- Docs 00–11 updated in place; Docs 12–14 and the generated validation record added.
- `blueprint.json` is the only registry/limit/graph/classification authority.
- `generated/*.md` is generated and checked, never hand-maintained.
- `generated/validation-report.txt` records the final structural/semantic/package audit; the archive checksum remains a sibling file.
- `10-resume-state.md` is the only implementation-status authority.
- `decisions/accepted-decisions.md` is the only decision-rationale authority.
- `12-golden-path-windows.md` is the only owner golden-path runbook.
- work files alone own micro-step files/prompts/commands/pass/fail/recovery/checkpoints.

No affected ID was silently deleted. Superseded meanings and their destinations are recorded above.
