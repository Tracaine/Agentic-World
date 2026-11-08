# Agentic World Platform — Revision 2 Charter

Registry: `blueprint.json`  
Artifact: ART-002  
Status: accepted  
Blueprint revision: 2

## Product outcome

Build one recognizably consistent AI character who inhabits a private Minecraft world, converses with the authorized player, visibly follows because of that conversation, suspends safely when the player leaves, and later recalls the grounded encounter after both Paper and the agent runtime have been completely stopped and restarted.

Minecraft is the first proof body. This is a **Minecraft-first modular monolith with revisable provider and environment seams**, not a demonstrated portable-world platform. Gate A does not build a toy world adapter or a generic capability registry to manufacture a portability claim. Demonstrated portability begins only at WRK-014, after a second materially different real adapter exists.

The defining proof is:

> meet → authorized player speaks → visible validated action caused by the conversation → safe absence suspension → completely stop server and agent runtime → restart later → natural grounded recall and consistent behavior

Gate A passes only after the exact consecutive repetition count in `LIM-GA-014` and the owner's judgment that the live result is worth continuing.

## Step-Zero rule

SPIKE-000 comes before load-bearing production work. It lives on a disposable branch or under `spikes/SPIKE-000`, proves the real dependency intersection and experiential loop with the least code possible, and is then discarded. Production retains only its version record, commands, results, failures, and adapter decisions. A successful bot join is not enough; follow, interruption, stop, structured model output, and restart must also pass.

## Gate A

Gate A requires only:

- one named Mineflayer NPC and one authorized `PrincipalId`;
- addressed English text chat;
- bounded typed perception;
- one structured `ModelDecision` with optional utterance and at most one action proposal;
- exactly one runtime-owned player-visible utterance path;
- asynchronous `follow_player`, `stop_behavior`, and emergency stop;
- zero model activity while the player is absent;
- minimal SQLite identities, events, conversations, model runs, actions, behaviors, evidence, and one deterministic encounter;
- honest shutdown, restart, reconciliation, retrieval, and natural recall;
- simple local diagnosis, logs, backup/restore, reset, and evidence collection;
- machine evidence plus owner experiential approval.

`move_near`, `inspect_surroundings`, and read-only inventory inspection are optional only when an empirical compatibility problem makes them the shortest diagnostic route. Crafting, building, combat, item exchange, autonomous plans, rich relationships, and multi-agent behavior cannot block Gate A.

## Authority and evidence

- Paper/Minecraft settles physical state. Mineflayer is a client observation and command channel.
- Model output is a proposal. It never settles delivery, action success, memory truth, identity, or permission.
- `started` means a long-running behavior was accepted and dispatched; it is not success.
- Each capability declares its minimum acceptable environment-derived evidence. Client-observed movement can complete Gate-A follow/stop; it says nothing about ownership, containers, or item transfer.
- Unconfirmed speech or action remains `unknown`. The runtime does not guess or blindly retry.
- Complete source events, deterministic encounters, and model-authored interpretations are distinct. Provenance makes an interpretation auditable; it does not make it faithful.

## Character profile ownership

DEC-011 resolves the former `AgentProfile` ambiguity. User-owned Parallax/Lattice persona packages own authored identity, voice, relationship model, style, examples, and compiled persona context. Agentic-World owns only a stable `AgentId`, display name, and a versioned profile reference/hash needed to load one compiled context through `ProfileSourcePort`. It does not silently create a competing profile database or mutate the external package.

QST-002 remains a non-architectural content choice: the final name and characterization of the first fixture. A temporary named persona-package fixture may support engineering, but the owner must approve it before the live experiential gate.

## Actors

| Actor ID | Actor | Gate-A authority | Prohibited inference |
| --- | --- | --- | --- |
| ACT-001 | Authorized player | Ordinary Minecraft play and addressed chat | Username or session entity ID alone is not durable authorization |
| ACT-002 | Owner/operator | Local start, status, pause, stop, emergency stop, shutdown, backup, restore, reset, evidence | No generic database replacement or physical-state correction |
| ACT-003 | Character runtime | Assemble scoped context, request one decision, validate/deliver speech, dispatch typed behavior | Cannot execute raw commands, invent success, or act while suspended |
| ACT-004 | Paper/Minecraft | Physical world authority | Cannot author character belief or memory |
| ACT-005 | Model provider | Propose one bounded decision | Cannot deliver speech, mutate the world, or establish fact |
| ACT-006 | IDE implementation agent | Execute one declared micro-step and report evidence | Cannot weaken tests, hide failure, or refactor unrelated scope |
| ACT-007 | Parallax/Lattice persona package | Authored character-profile authority | Does not own runtime/world state |

## Scope classes

The authoritative four-way classification is `blueprint.json.feature_classification`; `generated/feature-classification.md` is generated from it.

1. **required now** — indispensable to the defining proof;
2. **architectural seam only** — a narrow replaceable boundary used now without building the future implementation;
3. **deferred until after proof** — preserved Gate-B intent that cannot block first play;
4. **speculative future capability** — recorded idea with no current contract or delivery commitment.

## Non-goals for Gate A

- demonstrated world portability;
- a generic capability marketplace or toy world adapter;
- authenticated remote operator service or comprehensive audit/deletion/correction;
- exhaustive mutation crash recovery or migration governance;
- embeddings, compaction, reflection, autonomous salience, goals, plans, schedules, or rich relationship simulation;
- multiple characters or 8–10-character load tests;
- authoritative item/inventory/container mutation;
- voice, observer dashboard, complex building, public hosting, original graphics, or autonomous civilization.

## Product constraints

- The owner must never need to inspect source code to determine whether a step passed.
- Every active step must name exact files, commands, expected output, pass/fail rules, rollback, stop condition, and proving artifact.
- Every stage remains runnable and preserves the previous checkpoint.
- No model call occurs merely because the world ticked, an entity moved, or time passed.
- No runtime means no subjective elapsed time and no invented offline event.
- Compatibility evidence is provisional whenever read; primary sources and smoke gates are re-run after time or dependency drift.
- Secrets never enter prompts, logs, SQLite, commits, screenshots, or evidence bundles.

## Gate-B direction

Gate B preserves the larger vision: derived memory and belief, relationships, goals, plans, reflection, scheduling, two then 8–10 characters, richer budgets and observability, authenticated operations, authoritative inventory workflows, a second real adapter, and portability assessment. Those are real future directions, not Gate-A prerequisites.

LSL-inspired scripting/action tags remain on the radar under QST-003 and WRK-013. They may later offer compact emote or minor-action notation, but they must compile to existing typed boundaries; they never become an alternate script executor or authority channel.

## Architecture questions

No material architecture question currently blocks SPIKE-000 or Gate A. QST-002 is a character-content approval; QST-003–006 are explicitly later decisions. QST-007 is resolved by DEC-011.
