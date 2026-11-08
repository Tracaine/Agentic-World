# Accepted Decisions and Revision History

Registry: `blueprint.json`  
Artifact: ART-016  
Blueprint revision: 2

The registry owns current status/summary. This log owns rationale, alternatives, consequences, and revision disposition.

## DEC-001 — Minecraft-first modular monolith with revisable seams

Use one local TypeScript modular monolith with project-owned world, model, store, clock, telemetry, and profile ports. Gate A proves dependency boundaries with fakes; it does not claim environment portability. No toy environment or generic capability registry is built to support a marketing claim. WRK-014 is the first point at which portability can be assessed against a second materially different real adapter, and contract revision is allowed.

Revision 1's phrase “portable modular monolith” and toy-adapter acceptance were superseded because they overstated evidence and risked freezing Minecraft-shaped abstractions.

## DEC-002 — Empirical compatibility intersection

At SPIKE-000 and WRK-002, select and pin the newest smoke-tested stable intersection of Paper, Mineflayer, mineflayer-pathfinder, Java, and Node. Falling back to another verified combination requires no architecture review. Documentation is provisional at read time; re-read primary sources and rerun the progressive gates after time or dependency drift.

Progressive proof is authentication/join, presence, chat, position/entities, chunks/basic movement, pathfinding, follow/interrupt/stop, disconnect/reconnect/restart, then later inventory. Join alone does not retire protocol risk.

Revision 1's Paper 1.21.11/Java 21 commitment is retired as an architecture decision. It may still become the empirical result, but the blueprint does not assume it.

## DEC-003 — Strict TypeScript on pinned Node LTS

Use strict TypeScript, npm lockfile, Zod boundary schemas, and Vitest. The exact Node LTS is selected in WRK-002 and becomes a prerequisite for WRK-004. This avoids an implicit storage-runtime assumption.

## DEC-004 — Provider-neutral ModelPort; simplest supported structured adapter

Core consumes one `ModelDecision`. The OpenAI adapter uses the simplest currently supported strict structured-output/tool-call mechanism verified when WRK-003 begins. The Responses API may be used directly. The Agents SDK is optional and non-permanent, used only if it materially reduces Gate-A code. Provider sessions, tools, traces, IDs, and aliases are not domain authority.

Revision 1's mandatory Agents SDK choice is narrowed. It created a callback shape that encouraged awaiting physical actions and was unnecessary for one decision.

## DEC-005 — SQLite after Node pin; node:sqlite preferred when verified

Use local SQLite WAL behind a project-owned transaction wrapper. After WRK-002 pins Node, WRK-004 evaluates `node:sqlite` for:

- availability/stability on that exact LTS;
- WAL, foreign keys, busy timeout, explicit transaction/rollback;
- FTS used by the eight-case retrieval suite;
- online backup and separate-path restore;
- interruption/repeated-start behavior on clean Windows.

Use it if all pass. Otherwise the named fallback is `better-sqlite3`; its preflight must include Python 3 and Visual Studio Build Tools with Desktop C++ workload. An IDE agent may not silently choose or install a binding. Fallback requires a dated DEC-005 amendment identifying failed probes and exact versions/toolchain.

As provisional evidence read 2026-07-17, Node 24.18 is LTS, `node:sqlite` is documented as release candidate, and its API includes `backup()`. These facts are not a production pin.

## DEC-006 — Decision actor plus asynchronous behavior leases

The per-agent actor serializes stimuli, decisions, and state mutation. It never represents physical duration. `follow_player` validation/dispatch immediately returns `started` with stable `BehaviorId`/lease ID. Later events report progress/terminal outcomes. Stop, hazard, suspension, shutdown, and emergency stop use a high-priority lane that cannot wait behind the mailbox or provider call.

Revision 1's in-model action callback and exclusive `ACTING` lifecycle are superseded.

## DEC-007 — Connected suspension on player absence

When the authorized player leaves, keep a healthy Mineflayer client connected, set availability `SUSPENDED`, and cancel cognition, plans, movement, actions, behaviors, and model calls. Continue only same-principal presence observation, essential connection health, and priority safety/operator control. Resume after the connected adapter observes return and resync succeeds.

Use `OFFLINE` for operator-intended no connection and `DISCONNECTED` for unexpected link loss. A disconnected client cannot detect return. Full disconnect is operator shutdown, server/network failure, or a future Paper-side wake design.

Revision 1's “suspend and disconnect while absent” is superseded.

## DEC-008 — Private proof authentication

For a strictly local/loopback proof, an explicitly configured offline-mode Paper/Mineflayer account remains permitted. The world must not be reachable from untrusted LAN/WAN. Shared hosting waits for QST-006 and authenticated online mode. The empirical spike may instead choose a dedicated Microsoft-authenticated account if it is lower friction for the owner's actual environment.

## DEC-009 — Models only for designated cognitive work

Deterministic code handles presence, connection, safety, queueing, cooldowns, behavior timers, evidence rules, encounter promotion, and routine movement. Gate-A cognition wakes only for authorized addressed chat and explicitly designated terminal/restart meaning events. Autonomous idle, ambient salience, relationships, goals, plans, and scheduling wait for measured Gate-B policy.

## DEC-010 — One-attempt utterance workflow

Player-visible NPC speech is not an `ActionRequest`. One `ModelDecision` contains optional `UtteranceProposal`. CMP-003 alone validates it, assigns/persists `UtteranceId`, and makes at most one environment submission attempt. Without definitive environment deduplication, unconfirmed delivery becomes `unknown` and is never blindly retried.

Competing `speak` action/tool, `finalSpeech`, same-run tool callback, post-run fallback, and reconnect retry paths are retired.

## DEC-011 — External persona-package ownership

The owner's existing Parallax/Lattice architecture keeps companion identity in user-owned persona packages outside the runtime system prompt. Agentic-World therefore stores `CharacterIdentityRecord` with AgentId, display name, profile reference, version, and hash, and reads a bounded compiled context through `ProfileSourcePort`. It never duplicates or mutates the full authored profile.

Revision 1 `AgentProfile` as a load-bearing internal database record is retired. QST-007 is resolved; QST-002 remains only the first fixture's content.

## DEC-012 — Source events and deterministic encounter first

Gate A persists complete structured source events. It promotes an encounter only for an explicit player remember request or the designated acceptance interaction that caused the demonstrated action. Retrieval must naturally affect later dialogue/behavior.

Model-authored summaries, salience, tags, beliefs, and relationship implications are replaceable interpretations. They never replace source events and provenance never guarantees faithfulness. Autonomous significance scoring, reflection, compaction, and semantic retrieval are measured Gate-B options.

## Reversal costs

| Decision | Reversal cost before Gate A | After durable data exists |
| --- | --- | --- |
| DEC-001 topology | low | medium if boundaries are violated |
| DEC-002 version intersection | low; update record/lockfile | low-medium; rerun embodiment/reconciliation |
| DEC-004 provider adapter | low behind ModelPort | medium if prompts/evals shift |
| DEC-005 binding | low before WRK-004 | medium; transaction and backup regression required |
| DEC-007 absence policy | low in tests | medium; changes product semantics and continuity evidence |
| DEC-010 speech | high if competing paths return | high; duplicate delivery histories become ambiguous |
| DEC-011 profile ownership | low before persistence | high if two profile authorities diverge |
| DEC-012 continuity source | low before data | high; summaries alone cannot reconstruct lost events |
