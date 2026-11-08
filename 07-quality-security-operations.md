# Quality, Security, Stimulus Policy, and Operations

Registry: `blueprint.json`  
Artifact: ART-009  
Status: accepted

## Canonical Gate-A limits

Numeric values live only in `blueprint.json.limits`; [`generated/limits.md`](generated/limits.md) is generated. Contracts, work prompts, tests, and hand-maintained prose reference limit IDs or configuration keys, not copied literals.

Key relationships:

- `LIM-GA-002` is strictly inside `LIM-GA-001`, with the exact derived margin checked by the semantic guard;
- action and utterance dispatch use `LIM-GA-003` and `LIM-GA-004`;
- `LIM-GA-006` may outlive cognition and is re-evaluated on `LIM-GA-005`;
- priority stop/suspension/shutdown/emergency dispatch uses `LIM-GA-007`;
- pending cognition, retry, and proof repetition limits are `LIM-GA-008`, `LIM-GA-016`, and `LIM-GA-014`.

The semantic guard fails if the inner deadline is not lower than the outer SLO, the margin differs, speech attempts exceed one, or Gate-A work depends on deferred work.

## Gate-A cognition triggers

While `ACTIVE`, only these may enqueue cognition:

1. addressed chat from the authorized `PrincipalId`;
2. a behavior terminal event explicitly marked `needs_interpretation=true` by deterministic policy;
3. a restart/encounter-retrieval event explicitly marked `needs_recall_response=true` for the acceptance flow.

Operator control acts without cognition. Everything else is ignored or processed deterministically.

### Suppression/coalescing policy

| Stimulus | ACTIVE behavior | SUSPENDED/PAUSED behavior | Telemetry reason |
| --- | --- | --- | --- |
| duplicate source event | suppress | suppress | `duplicate_source_event` |
| same-principal addressed messages within `LIM-GA-009` before start | coalesce in arrival order | suppress | `coalesced_addressed_chat` / `availability_blocked` |
| addressed event during `LIM-GA-010` duplicate cooldown | coalesce if same source burst; otherwise queue | suppress | `cooldown_coalesced` / `availability_blocked` |
| pending queue below `LIM-GA-008` | enqueue | suppress | `trigger_accepted` / `availability_blocked` |
| pending queue at `LIM-GA-008` | suppress newest; preserve active and earlier pending; never evict priority control | suppress | `cognition_queue_full` |
| ordinary movement/entity/proximity/block/time/chunk/inventory noise | no cognition | no cognition | `not_cognitive_gate_a` |
| non-addressed or unauthorized chat | no cognition | no cognition | `not_addressed` / `unauthorized_principal` |
| behavior progress | deterministic state update only | stop/cancel only | `progress_not_cognitive` |
| designated terminal/restart event | enqueue if policy says interpretation needed | defer/drop according to kind; never call model | `trigger_accepted` / `availability_blocked` |

Suppression telemetry includes `EventId`, kind, agent, principal when allowed, connection, availability, reason, queue depth, and timestamp. It does not include secrets or unrelated chat.

### Required soak tests

- `LIM-GA-012` of ordinary player/NPC movement, entity updates, proximity changes, chunks, time, and ambient noise while ACTIVE: zero model calls;
- authorized player absence with ordinary noise: zero model calls and zero active behavior;
- addressed burst exceeding the queue: bounded calls and explicit suppression counts;
- return: no model call until fresh presence and resync make availability ACTIVE;
- unexpected disconnect: no claim of detecting return before reconnect/sync.

Before Gate-B autonomous idle, define salience thresholds, per-event cooldowns, per-player budgets, and measured acceptance limits in a new decision. Gate A supplies no default autonomous wake.

## Package-script command surface

The production scaffold must expose one stable owner-facing surface. The exact scripts become available by the work package listed.

| Command | Available after | Purpose | Required final line |
| --- | --- | --- | --- |
| `npm run aw:doctor` | WRK-001, expanded WRK-002/004 | Node, Java, Paper, auth, DB/migrations, credentials | `PASS: doctor complete` or `FAIL: ...`; missing model key is `WARN` |
| `npm run architecture:validate` | WRK-001 | strict structural guard, semantic audit, and generated-view freshness | `PASS: blueprint validation complete` |
| `npm run aw:install` | WRK-002 | install exact lockfile and verify compatibility record | `PASS: pinned dependencies installed` |
| `npm run aw:secrets:init` | WRK-003 | create the ignored local secrets template without printing values | `PASS: local secrets template ready` |
| `npm run aw:server:start` | WRK-002 | start a managed Paper child, record its exact PID, and return after readiness | `PASS: Paper ready` |
| `npm run aw:server:stop` | WRK-002 | request clean Paper shutdown and verify the process stopped | `PASS: Paper stopped cleanly` |
| `npm run aw:app:start` | WRK-002/003 | start a managed agent child, record its exact PID, and return after readiness | `PASS: agent READY/ACTIVE` or `PASS: agent READY/SUSPENDED` |
| `npm run aw:stop` | WRK-003 | stop active behavior | `PASS: behavior stopped` or `PASS: no active behavior` |
| `npm run aw:emergency-stop` | WRK-002 diagnostic, production-coordinated in WRK-003 | priority safety stop independent of cognition | `PASS: emergency stop dispatched` plus evidence state |
| `npm run aw:shutdown` | WRK-003/004 | priority stop, flush, close safely | `PASS: runtime OFFLINE` |
| `npm run aw:smoke` | WRK-002 onward | current checkpoint smoke | `PASS: <checkpoint> smoke` |
| `npm run aw:health` | WRK-003 | print connection, availability, four health axes, active IDs | `PASS/WARN/FAIL` per component |
| `npm run aw:db:backup -- --to .\data\backups\pre-play.sqlite` | WRK-004 | online backup and integrity check; another explicit file may be supplied | `PASS: backup verified` plus checksum |
| `npm run aw:db:restore -- --from .\data\backups\pre-play.sqlite --to .\data\restore-check.sqlite` | WRK-004 | restore only to a separate path and verify | `PASS: restore verified` |
| `npm run aw:reset -- --fixture gate-a --prepare` | WRK-004 | resolve configured WorldId, pre-backup, and print one exact confirmation command | `READY: copy and run the confirmation command above` |
| `npm run aw:evidence -- --run latest` | WRK-001 onward | collect the latest redacted causal bundle; an explicit run ID may be supplied | `PASS: evidence written` plus exact path |

Commands may print raw traces after the human-readable diagnosis, never instead of it. A command exits nonzero on `FAIL`. No script installs software or chooses a SQLite binding silently.

## Doctor output contract

Example:

```text
PASS: Node <exact> matches compatibility record
PASS: Java <exact> matches selected Paper build
PASS: Paper artifact checksum verified
PASS: Mineflayer authentication configured for this private target
PASS: database opens; migrations current; integrity_check=ok
WARN: model API key absent; fake and deterministic checks remain available
PASS: logs and data directories are writable
PASS: doctor complete
```

Doctor never prints credentials. A missing model key is a warning until a live model step; then that step stops rather than fabricating success.

## Security baseline

- Paper/offline-mode development, if selected, binds to loopback/private host only; no public listener.
- Shared/LAN/WAN use waits for QST-006 and online authenticated mode.
- `OPENAI_API_KEY` is process environment or an ignored local secrets file documented in the runbook; never `.env.example` with a real value.
- The model sees no raw command, code execution, filesystem, network, credential, other-agent private context, or operator tool.
- NPC text beginning `/`, containing newline/control codes, or exceeding 240 characters rejects.
- Pathfinder configuration disables digging, block placement, towers, combat, and item use for Gate A.
- Evidence exports redact credential-shaped values and unrelated private context.
- Backup/restore/reset use explicit paths under configured data roots; broad paths, globs, and unresolved environment variables reject.

## Minimal Gate-A operations vs Gate B

Gate A includes diagnosis, safe stop, clean shutdown, causal logs, evidence export, checkpoint recovery, online backup, separate-path restore, and safeguarded local reset. Gate B owns authenticated operator transport, comprehensive audit/deletion/correction, retention governance, exhaustive crash recovery, generalized readiness, remote operations, and production hardening.

## Observability

Every causal signal uses stable IDs where applicable:

`AgentId`, `PrincipalId`, `WorldId`, `WorldEpoch`, `WorldSessionId`, `EventId`, `ConversationId`, `ModelRunId`, `UtteranceId`, `ActionId`, `BehaviorId`, `EncounterId`.

Required signal families:

- state transition with previous/current/reason;
- cognition trigger accepted/suppressed;
- model run start/terminal/latency;
- utterance validation/submission result and attempt count;
- action validation/immediate dispatch;
- behavior progress/terminal;
- evidence observed/accepted/rejected with capability reason;
- store migration/backup/restore/reset integrity;
- startup/reconciliation/offline gap;
- independent component health.

Logs must let a second agent reconstruct “what happened and why” without reading source or hidden reasoning.
