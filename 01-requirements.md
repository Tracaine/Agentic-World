# Requirements, Assumptions, Questions, and Risks

Registry: `blueprint.json`  
Artifact: ART-003  
Status: accepted  
Blueprint revision: 2

`blueprint.json` is the only hand-maintained requirement registry. Do not copy acceptance text into this file. Run `python architecture/tools/render_blueprint.py` to rebuild `generated/registry.md`, which contains the current ID, status, priority, acceptance, owner, verification, and work-package mappings.

## Gate-A requirement groups

| Outcome | Requirement IDs | Meaning |
| --- | --- | --- |
| Embodiment | REQ-002, REQ-003 | One named bot joins the empirically selected stack, recognizes the authorized principal, and exposes a bounded typed view |
| Conversation | REQ-004, REQ-101 | One model decision and one runtime-owned utterance attempt meet coherent time budgets |
| Action | REQ-005, REQ-006, REQ-009 | Typed asynchronous follow/stop, causal IDs, capability evidence, and honest terminal/unknown states |
| Absence and triggers | REQ-010, REQ-011, REQ-108 | Connected suspension, closed trigger allowlist, queue bounds, and zero absence/ambient calls |
| Continuity | REQ-007, REQ-008, REQ-109, REQ-111 | Stable identity and epoch, complete source events, deterministic encounter, grounded retrieval |
| Owner operation | REQ-015–019, REQ-104–106 | Causal logs, safe local operations, bounded recovery, resumability, secrets, and deterministic tests |
| Proof gate | REQ-110 | `LIM-GA-014` consecutive full repetitions plus owner experiential approval |

## Explicitly deferred requirements

- REQ-012–014: multi-character scale, knowledge isolation, and rich character state;
- REQ-020: authoritative item and inventory mutations;
- REQ-021: LSL/action-tag semantics;
- REQ-102–103: population backpressure and multi-level budgets;
- REQ-107: demonstrated portability with a second real adapter.

They remain requirements in the registry so the vision is preserved. Their `deferred` status prevents strict validation from treating them as Gate-A obligations.

## Assumptions

| ID | Assumption | Validation point | Failure response |
| --- | --- | --- | --- |
| ASM-001 | Owner can run Java Edition and a private Paper server | SPIKE-000 preflight | Move Paper to another private owner-controlled host or revisit first environment |
| ASM-002 | Windows host has sufficient Java/Node/RAM resources | SPIKE-000 doctor | Reduce Paper allocation before changing architecture |
| ASM-003 | A funded OpenAI API credential is available for live structured-call steps | SPIKE-000 model gate | Continue fake/deterministic work; stop live model gate with `WARN`, never bypass credentials |
| ASM-004 | Gate A has one authorized player and one NPC | Charter | Reopen attention/authorization design if false |
| ASM-005 | Gate A uses English text chat | Character acceptance | Localization/voice stays later |
| ASM-006 | Reference world has no incompatible anti-cheat/gameplay plugin | SPIKE-000 clean-server test | Remove plugin or record narrow compatibility work |
| ASM-007 | Gate-A data remains on an owner-controlled local machine | Deployment check | Reopen encryption, consent, retention, and operator security |
| ASM-008 | A temporary named persona-package fixture may support engineering | Before WRK-003 live step | Owner supplies/approves the fixture; architecture remains unchanged |

No unvalidated assumption is architecture-shaping. If one becomes architecture-shaping, stop and promote it to a question/decision before editing load-bearing contracts.

## Questions

| ID | Status | Decision point | Effect |
| --- | --- | --- | --- |
| QST-001 | resolved | complete | Mineflayer, OpenAI-first provider adapter, and connected absence suspension |
| QST-002 | open, non-blocking | before live WRK-003 review | First character's canonical name, voice, history, values, and relationship starting point |
| QST-003 | deferred | before WRK-013 | Meaning and authority of the owner's LSL scripts/action tags |
| QST-004 | deferred | Gate-B data governance | Retention/deletion preferences beyond safe local Gate-A defaults |
| QST-005 | deferred | before unattended life | What may continue while the player is absent in a later phase |
| QST-006 | open, later | before LAN/WAN deployment | Dedicated authenticated bot account and hosting topology |
| QST-007 | resolved | complete | Parallax/Lattice owns authored persona; Agentic-World stores a reference/hash |

There is no unresolved Gate-A architecture blocker. QST-002 is a content/experience choice, not a schema-ownership question.

## Highest Gate-A risks

| ID | Trigger | Required response |
| --- | --- | --- |
| RSK-001 | Any embodiment gate after join fails or dependencies drift | Stop platform work; re-read primary sources and use a recorded version/fallback intersection |
| RSK-003 | Restart finds utterance/action/behavior in an externally uncertain phase | Record `unknown`, reconcile where the capability permits, never blindly retry |
| RSK-004 | A summary lacks/contradicts visible source events | Reject it; retain the complete events; do not promote it as memory |
| RSK-005 | Model misses deadline or outer SLO | Record typed failure; no hidden retry; diagnose provider/contract separately from world |
| RSK-006 | Fixed continuity/retrieval suite misses its threshold twice | Prioritize measured semantic retrieval in Gate B; do not claim compaction is already a mitigation |
| RSK-007 | Selected SQLite binding fails WAL/transaction/FTS/backup probes | Use the named fallback only after an explicit DEC-005 update and toolchain preflight |
| RSK-010 | Registry, docs, code, or checkpoint disagree | Stop; run both guards; reconcile evidence before continuing |
| RSK-011 | Ambient/suspended activity causes any model call | Gate A fails; inspect trigger and suppression telemetry |
| RSK-013 | An UtteranceId has more than one submission attempt | Gate A fails; remove competing speech path/retry |
| RSK-014 | A disconnected client is credited with detecting return | Lifecycle test fails; return requires a READY adapter presence observation |
| RSK-015 | Reset/restore changes history without a new epoch | Stop startup; repair WorldId/WorldEpoch mapping before new events |

## Risk RSK-006: defined continuity evidence

Gate A uses a fixed, versioned suite in `tests/fixtures/continuity/v1/` with:

- invariant identity facts and relationship starting facts;
- prohibited certainty, invented-event, and contradictory claims;
- required and prohibited encounter IDs for each query;
- eight retrieval cases: exact wording, paraphrase, indirect reference, participant, place/event, keyword-free “remember when,” competing similar encounters, and stale/superseded interpretation;
- behavioral fixtures for duplicate speech, foolish-but-valid action, interrupted behavior, suspension, and restart.

Structured/FTS retrieval must meet `LIM-GA-018`. Failing that threshold twice after ordinary query/index tuning triggers WRK-007 semantic-retrieval work. Embeddings remain a local/hosted port seam until then.

Compaction is not a Gate-A guarantee. WRK-007 may adopt it only after comparing provenance retention, key-fact preservation, contradictions, retrieval usefulness, behavioral continuity, and token reduction against the uncompacted source-event baseline.

## Change control

Any new Gate-A capability, model trigger, retry, timeout, queue, numeric limit, or persistence record must update `blueprint.json`, its owning contract/decision, a verification, and the semantic guard where automatable. Architecture-shaping changes require a decision amendment and owner confirmation. Implementation convenience is not an acceptance criterion.
