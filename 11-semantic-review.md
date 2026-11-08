# Revision 2 Semantic-Consistency Report

Registry: `blueprint.json`  
Artifact: ART-018  
Status: accepted  
Review date: 2026-07-17

Structural validation is necessary but not semantic proof. This report records the patch audit categories requested by the owner. Automated results are refreshed before packaging.

## Audit summary

| Audit | Result | Evidence |
| --- | --- | --- |
| Timeout/budget | PASS | canonical `limits`; guard proves `LIM-GA-002` is inside `LIM-GA-001` by the configured margin, behavior is independent, and the retired race is absent |
| Lifecycle | PASS | separate connection, availability, component health, cognition, action, and behavior state machines; `DEGRADED` removed as agent state |
| Suspension | PASS | READY client remains connected; SUSPENDED stops cognition/behavior; return requires observed presence; disconnect/restart/shutdown tested separately |
| Speech | PASS | DEC-010/CMP-003/INT-011; one `ModelDecision.utterance?`; no `speak` physical action, `finalSpeech`, callback-send, fallback-send, or blind retry |
| Async behavior | PASS | immediate `started` + BehaviorId; later typed events; priority control lane; actor never awaits duration |
| Identity | PASS | AgentId, PrincipalId, WorldId, WorldEpoch, and causal IDs; Minecraft aliases map to PrincipalId; epoch rules cover restart/reset/restore |
| Evidence | PASS | named non-total evidence kinds; capability-specific thresholds; movement evidence not generalized to mutation |
| Persistence | PASS | complete Gate-A events and deterministic encounter precede summaries; SQLite moved after embodiment/model; source events retained |
| Dependency graph | PASS | SPIKE → WRK-001 → WRK-002 → WRK-003 → WRK-004 → WRK-005; WRK-004 depends on Node-pin WRK-002; no Gate-B leakage |
| Compatibility/version | PASS | no hard Minecraft commitment; dated provisional primary sources; progressive gates and fallbacks; exact pin is empirical |
| Provider | PASS | provider-neutral ModelPort; simplest supported structured output; Agents SDK optional/non-permanent |
| SQLite | PASS | DEC-005 names `node:sqlite` evaluation criteria and `better-sqlite3`/Windows native toolchain fallback; no silent default |
| AgentProfile ownership | PASS | DEC-011/QST-007: Parallax/Lattice persona package is authority; runtime stores identity/reference/hash only |
| Registry duplication | PASS | JSON owns registry/limits/graph/classification; work files own execution; generated views are checkable; one status/decision/runbook authority |
| Gate-A scope | PASS | follow/stop only; simple local operations; rich governance/items/multi-agent/portability deferred |

## Reconciled required items

- DEC-002: empirical version intersection replaces fixed Paper version.
- DEC-005: Node pin precedes storage; binding evaluation/fallback is explicit.
- DEC-007 and FLW-008: connected suspension, honest OFFLINE/DISCONNECTED semantics.
- FLW-002 step 9: terminal follow wait removed; later events are independent.
- REQ-101: coherent inner/outer/dispatch/control/behavior budgets.
- Docs 05/07/08: contracts, limits/stimulus operations, and tests recut.
- lifecycle diagrams: orthogonal axes replace IDLE/COGNIZING/ACTING/DEGRADED lifecycle.
- WRK-003 and full graph: model/action now precedes SQLite; WRK-004 depends on Node evidence.
- WRK-007/008: split into independent later deliverables with WRK-006/007/008/009/015/016.
- RSK-006: fixed fixtures, thresholds, cadence, semantic trigger, and compaction comparison defined.
- INV-013: provenance-or-reject and “provenance is not faithfulness” explicit.
- AgentProfile: external persona ownership resolved.
- JSON/Markdown: authority map plus generator/check mode added.

## Automated semantic checks

`architecture/tools/semantic_guard.py` checks:

- exact lifecycle axes/states and ban on exclusive `DEGRADED` lifecycle;
- model deadline/margin/outer SLO relation;
- single speech owner and banned competing speech tokens;
- Gate-A action union excludes speech/item/build/combat;
- stable identity list and WorldEpoch behavior;
- evidence kinds and thresholds for implemented capabilities;
- Gate-A work DAG, SPIKE prerequisite, and no deferred dependency leakage;
- WRK-004's dependency on WRK-002 Node evidence;
- compatibility-record fields, progressive gates, and fallbacks;
- resolved AgentProfile ownership;
- generated-view freshness;
- Gate-A SQLite tables and encounter promotion rules;
- no critical generic core contract maps/fields;
- canonical limit IDs instead of duplicated literals in active Gate-A prose/prompts;
- every SPIKE/WRK micro-step has all required fields, exact scoped/checkpoint paths, a PowerShell command block, and no unresolved placeholder or wildcard scope.

## Narrow manual checklist

Automation cannot settle these; reviewer signs each before implementation and before Gate A:

- [x] the abstraction language is Minecraft-first and does not imply demonstrated portability;
- [x] Gate-A scope is the least infrastructure needed for the live proof;
- [x] character profile ownership matches the owner's existing Parallax/Lattice design;
- [x] no later feature is presented as required for first play;
- [ ] exact dependency intersection is proven live (SPIKE-000/WRK-002 work, not blueprint evidence);
- [ ] first named persona fixture feels recognizably consistent to the owner;
- [ ] natural recall is conversational rather than a database recital;
- [ ] the `LIM-GA-014` consecutive live proofs pass and the owner says the experience is worth continuing.

Unchecked items are intentionally runtime/experience gates, not blueprint defects.

## Residual risks

- Current external documentation is provisional; the real intersection may change before implementation.
- Mineflayer chat may not offer definitive delivery confirmation/deduplication; the honest Gate-A response is one attempt plus `unknown`.
- Client-observed follow/stop evidence is adequate only for the narrow Gate-A movement proof.
- Structured/FTS retrieval may miss indirect recall; the fixed threshold determines whether WRK-007 moves up.
- `node:sqlite` API stability and Windows behavior must pass the selected runtime probes before it becomes load-bearing.
- Owner character-content approval remains open, but does not change architecture.

## Validation record

The packaged revision must contain fresh command output in `generated/validation-report.txt` for:

1. JSON parse;
2. strict structural guard;
3. semantic guard;
4. generated-view check;
5. banned-token/generic-contract scan;
6. package content inventory and a pre-report content-tree digest.

The report is evidence of blueprint consistency only; it does not claim runtime implementation or live Minecraft success. The final archive's SHA-256 is written beside the archive rather than inside it, because an archive cannot contain its own stable checksum.
