# Interfaces and Contract Policy

Registry: `blueprint.json`  
Artifact: ART-007  
Status: accepted

Until implementation exists, `contracts/platform-contracts.md` is the canonical reference schema. Once a contract is implemented, the code schema/type becomes authority and the Markdown is generated or reduced to design notes. Unknown vendor data may exist only inside an adapter before parsing.

## Interface index

| ID | Purpose | Key rule |
| --- | --- | --- |
| INT-001 | world observation stream | Closed event union; parse before core |
| INT-002 | bounded fresh self/world query | Snapshot includes world/epoch, omissions, capture, expiry |
| INT-003 | structured model decision | `LIM-GA-002` deadline; one optional utterance; at most one action |
| INT-004 | Gate-A action proposal | `follow_player | stop_behavior`; never speech |
| INT-005 | behavior/control dispatch | immediate `started`/rejected/failed/unknown; no duration wait |
| INT-006 | behavior/evidence event stream | progress and terminal outcomes arrive later |
| INT-007 | encounter retrieval / derived cognition seam | Gate A promotes deterministically; interpretations provenance-or-reject |
| INT-008 | domain store/transaction | binding-neutral; no network/model work in transaction |
| INT-009 | causal telemetry/health | four independent health axes and suppression reasons |
| INT-010 | local operator control | closed commands; no generic replacement/correction |
| INT-011 | utterance submission | exactly one runtime-owned attempt per UtteranceId |
| INT-012 | persona package read | local read-only ref/version/hash verification |

## Closed schema rules

Every union has a `kind` discriminator and a kind-fixed body. Critical contracts cannot contain:

- `Record<string, unknown>` after boundary parsing;
- a generic `payload`, `normalizedPayload`, `self`, `evidence`, or operator `replacement` field;
- an arbitrary capability name plus arguments map;
- model-selected AgentId, PrincipalId, WorldId, authorization, or evidence state;
- vendor SDK/Mineflayer/SQLite objects.

Extension fields are introduced through a contract version and explicit union member. Unknown event/capability kinds reject safely and emit telemetry.

## Model decision

The provider returns exactly one schema:

```ts
type ModelDecision = {
  kind: "model_decision";
  decisionVersion: 1;
  utterance?: UtteranceProposal;
  action?: FollowPlayerProposal | StopBehaviorProposal;
};
```

`UtteranceProposal` carries character text and a delivery intent, not a transport ID or authority. The runtime may accept utterance and reject action, or vice versa. Action dispatch never delays speech validation/submission. A behavior result is a later domain event; if interpretation is warranted it starts a later cognition run.

The model receives no general tool loop in Gate A. The simplest supported structured-output/strict-tool adapter may be used behind `ModelPort`; the OpenAI Agents SDK is allowed only when it materially reduces code. It is not a domain dependency and no SDK session is authoritative.

## Utterance delivery

`UtteranceProposal` is not `ActionRequest`. CMP-003:

1. validates model-run freshness, ACTIVE availability, authorized conversation, text length/syntax, and character ownership;
2. assigns stable `UtteranceId` and persists intent;
3. calls INT-011 once;
4. records `delivered`, `rejected`, or `unknown`;
5. never retries an unconfirmed send unless a future environment supplies definitive deduplication by the same ID.

The Gate-A Minecraft adapter cannot provide definitive chat deduplication, so one attempt is the hard rule.

## Asynchronous behavior protocol

1. parse and validate a typed action proposal;
2. assign `ActionId`, validate freshness/authorization/lease/deadline;
3. dispatch `BehaviorDispatchRequest`;
4. return immediately with `ImmediateDispatchResult`:
   - `started { behaviorId, leaseId, acknowledgedAt }`,
   - `rejected { reason }`,
   - `failed { reason }`, or
   - `unknown { reason }`;
5. release cognition and actor mailbox;
6. publish typed `BehaviorEvent`s later;
7. evaluate each event using capability-specific evidence;
8. trigger later cognition only for a designated meaningful terminal/restart event.

Stop, hazard, suspension, shutdown, and emergency stop use `ControlRequest` through the high-priority path. `stop_behavior` is idempotent for an already terminal or absent target.

## Gate-A capabilities and evidence

| Capability/control | Validation | Immediate result | Minimum evidence for state | Timeout |
| --- | --- | --- | --- | --- |
| `follow_player` | ACTIVE, READY, authorized visible principal, ≤16 blocks, fresh same-epoch snapshot, free lease, no digging/building | `started` + BehaviorId | `active`: client-observed path/movement toward same PrincipalId; terminal: client-observed distance/motion/path state or typed failure | 60 s, reevaluate every 1 s |
| `stop_behavior` | own BehaviorId or current own lease; any availability | dispatch ack or idempotent completed | client-observed goal cleared plus no controlled movement during observation window | `LIM-GA-007` |
| `emergency_stop` | local owner/safety path; no cognition | dispatch ack | same stop evidence; unknown if adapter link is gone | `LIM-GA-007` |
| optional diagnostic inspection | fixed query kind/radius/count | query result | fresh typed snapshot with omissions | only if SPIKE/WRK-002 needs it |

`dispatch_acknowledged`, `client_observed`, `server_confirmed`, and `reconciled` are named evidence kinds, not numbers. The threshold table explicitly lists acceptable evidence kinds for each transition. No generic comparator ranks them.

## Time budgets

Canonical values live only in `blueprint.json.limits` and are rendered to `generated/limits.md`.

- outer addressed-chat-to-submission p95: `LIM-GA-001`;
- inner ModelPort hard deadline: `LIM-GA-002`;
- explicit inner/outer margin: derived and checked from `LIM-GA-001` minus `LIM-GA-002`;
- validated action dispatch deadline: `LIM-GA-003`;
- utterance validation/submission deadline: `LIM-GA-004`;
- behavior reevaluation: `LIM-GA-005`;
- follow timeout: `LIM-GA-006`;
- priority control dispatch p95: `LIM-GA-007`.

The behavior may outlive cognition. FLW-002 never waits for terminal follow within the model run.

## Idempotency and retry

| Operation | Idempotency key | Gate-A retry rule |
| --- | --- | --- |
| normalize adapter event | adapter source key → EventId | duplicate returns existing event |
| model run | ModelRunId | no automatic retry; a new player message creates a new run |
| NPC utterance | UtteranceId | at most one attempt; unconfirmed is unknown |
| action validation/dispatch | ActionId | replay returns existing immediate result; no second dispatch |
| behavior stop | BehaviorId + control request ID | idempotent; may repeat safe control until deadline while connected |
| SQLite transaction | operation-specific durable ID | transaction rollback/re-run only before external dispatch |
| backup | explicit destination/checksum | new destination on retry |
| reset | WorldId + printed confirmation token | never implicit; pre-reset backup first |

## Operator contract

Gate-A commands are a closed union:

`status | pause | resume | stop_behavior | emergency_stop | shutdown | doctor | backup | restore | reset | collect_evidence`

Restore requires a source backup and separate target. Reset requires explicit WorldId, printed confirmation token, and fixture. There is no `correct_record` or generic `replacement` member in Gate A. WRK-008 may later introduce typed, record-specific correction contracts with version checks and audit.

## Compatibility

Major contract changes require new versioned schemas and updated fixtures. Minor optional additions must not change the meaning of existing states. Environment adapters may expose different internal evidence, but core receives only declared union members. A second real adapter may force contract revision; that revision is expected and preferable to freezing Minecraft vocabulary prematurely.
