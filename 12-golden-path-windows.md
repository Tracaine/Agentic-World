# Clean Windows Golden Path

Registry: `blueprint.json`  
Artifact: ART-033  
Status: accepted target runbook

This is the owner-facing path after WRK-005 implementation. It contains no hand-edited version placeholders: `config/compatibility.lock.json`, produced by SPIKE-000 and verified in WRK-002, contains every exact version, URL, checksum, and test date. The bootstrap script reads that file and either installs/verifies exactly those versions or stops with a copyable command. Until WRK-002 produces that record, this runbook is a specification—not a claim that the runtime exists.

## What you need

- Windows 11 x64 with PowerShell 7 and `winget`;
- Git;
- a Minecraft Java Edition account for the human player;
- either the compatibility record's dedicated Microsoft-authenticated bot account or the explicitly loopback-only offline bot fixture;
- an OpenAI API project key with a small provider-side spend limit for the live steps;
- enough free disk/RAM reported by `aw:doctor`;
- the repository at a simple path such as `C:\agentic-world`.

Do not expose an offline-mode Paper server to LAN/WAN. Do not paste the API key into a command line, commit, chat, screenshot, or log.

## Canonical locations

| Purpose | Path |
| --- | --- |
| exact dependency/runtime record | `config\compatibility.lock.json` |
| local runtime config | `config\runtime.local.json` |
| named character identity/profile reference | `config\characters\gate-a.json` |
| compiled Parallax/Lattice persona artifact | path referenced by `gate-a.json` |
| ignored, ACL-limited secrets | `.secrets\local.env` |
| Paper server | `dev\paper\` |
| Paper properties | `dev\paper\server.properties` |
| Paper config | `dev\paper\config\paper-global.yml` |
| SQLite | `data\agentic-world.sqlite` |
| backups | `data\backups\` |
| logs | `logs\` |
| proof evidence | `evidence\gate-a\` |

## 1. Open a clean PowerShell

```powershell
Set-Location C:\agentic-world
git status --short
```

Expected: no unexpected output. If files are listed, stop and ask the IDE agent to reconcile them; do not delete or overwrite them.

## 2. Install and verify exact prerequisites

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\windows\bootstrap.ps1 -Compatibility .\config\compatibility.lock.json
```

Expected ending:

```text
PASS: Git <exact> available
PASS: Node <exact> matches compatibility record
PASS: Java <exact> matches selected Paper build
PASS: Windows bootstrap complete
```

If the script prints an installation command, copy that exact line into an elevated PowerShell, close/reopen PowerShell, and rerun the bootstrap. Do not substitute a “close enough” Java/Node version.

## 3. Install the locked project and Paper artifact

```powershell
npm run aw:install
```

Expected ending:

```text
PASS: npm lockfile installed
PASS: Paper artifact checksum verified
PASS: pinned dependencies installed
```

Failure rules:

- lockfile drift, checksum mismatch, unsupported Node, or native build prompt = `FAIL`; stop;
- the command may not silently switch SQLite bindings;
- rerun primary-source/compatibility smoke work rather than deleting the lockfile.

## 4. Configure secrets safely

```powershell
npm run aw:secrets:init
```

The command prompts without echo, writes only `.secrets\local.env`, applies an owner-only Windows ACL, verifies `.gitignore`, and prints variable names but never values.

Expected ending:

```text
PASS: OPENAI_API_KEY stored without echo
PASS: secret file is ignored and owner-readable only
```

For a deterministic/fake checkpoint, choosing “skip model key” is allowed and doctor reports `WARN`. A live model step stops until the key exists.

## 5. Validate configuration and environment

```powershell
npm run aw:doctor
```

Required final result: `PASS: doctor complete` and no `FAIL`. A missing API key may be `WARN` only before the live model step. Doctor must report Node, Java, Paper, Mineflayer authentication, database/migrations, persona artifact/hash, credentials, network binding, and writable data/log paths.

## 6. Create a safe pre-play backup

```powershell
npm run aw:db:backup -- --to .\data\backups\pre-play.sqlite
```

Expected: `PASS: backup verified <sha256>`. The destination must not be the live database.

## 7. Start Paper, then the agent

Use two PowerShell windows.

Window A:

```powershell
Set-Location C:\agentic-world
npm run aw:server:start
```

Wait for `PASS: Paper ready`.

Window B:

```powershell
Set-Location C:\agentic-world
npm run aw:app:start
```

Expected before the player joins:

```text
PASS: connection READY
PASS: availability SUSPENDED (authorized player absent)
```

## 8. Join and check presence

Start Minecraft Java using the version in `compatibility.lock.json`. Join the private server address printed by `aw:doctor` (the local reference is `localhost`).

In Window C:

```powershell
Set-Location C:\agentic-world
npm run aw:health
```

Expected:

```text
PASS: connection READY
PASS: availability ACTIVE
PASS: authorized PrincipalId <redacted-short-id> present
PASS: world/model/store/telemetry health usable
```

If the username appears but PrincipalId is wrong or unmapped, stop. Do not “fix” authorization by weakening the identity check.

## 9. Run the live encounter

First print the exact owner prompts generated from the configured character profile:

```powershell
npm run aw:smoke -- --case owner-prompts
```

Expected output includes two lines beginning `CHAT 1:` and `CHAT 2:`. Copy the text after `CHAT 1:` into Minecraft chat. Its meaning is:

```text
the configured character name, followed by “please follow me.”
```

Expected in-world behavior:

- exactly one NPC reply appears;
- the NPC begins following within the configured dispatch/behavior window;
- moving a short safe distance produces visible follow;
- no digging, placing, combat, item use, or slash command occurs.

Then copy the text after `CHAT 2:`. Its meaning is:

```text
the configured character name, followed by “stop here.”
```

Expected: stop is dispatched through the priority-capable control route and movement ceases. Also test the independent owner control once:

```powershell
npm run aw:emergency-stop
```

Expected: `PASS: emergency stop dispatched` followed by `client_observed`/`server_confirmed` or an honest `unknown`; never a guessed success.

## 10. Prove absence suspension

Leave the Minecraft server. Keep Paper and the agent running for the configured absence observation.

```powershell
npm run aw:health
npm run aw:smoke -- --case absence
```

Required:

```text
PASS: connection READY
PASS: availability SUSPENDED
PASS: active cognition 0
PASS: active behavior 0
PASS: model calls during absence 0
```

If connection is OFFLINE/DISCONNECTED solely because the player left, Gate A fails. If the client disconnected for a real network/server reason, it must not claim it observed return.

## 11. Shut down everything completely

Window B:

```powershell
npm run aw:shutdown
```

Expected: `PASS: runtime OFFLINE` within the shutdown deadline after priority stop.

Window A:

```powershell
npm run aw:server:stop
```

Expected: `PASS: Paper stopped cleanly`.

Verify no runtime/server process is active:

```powershell
npm run aw:health
```

Expected: `PASS: runtime OFFLINE` and `PASS: Paper offline`. Leave both stopped long enough to make the later return experientially distinct. No offline event should be invented.

## 12. Restart later and recall naturally

Repeat Step 7, join Minecraft, and wait for ACTIVE. Print the exact recall prompt:

```powershell
npm run aw:smoke -- --case owner-prompts
```

Copy the line beginning `RECALL:` into Minecraft chat. Its meaning is:

```text
the configured character name, followed by a natural question about what happened when you met last time.
```

Pass behavior:

- the character naturally refers to the prior conversation/follow/stop experience;
- it does not quote table/ID/database terminology;
- it does not invent an offline activity or uncertain detail;
- its behavior and voice remain recognizably consistent.

## 13. Collect and verify evidence

```powershell
npm run aw:evidence -- --run latest
npm run aw:smoke -- --case gate-a-manifest
```

Expected:

```text
PASS: evidence written .\evidence\gate-a\<run-id>
PASS: utterance submission attempts 1
PASS: model calls during absence 0
PASS: encounter retrieval threshold met
PASS: Gate-A manifest valid
```

Record the owner experiential rubric in the generated review file. Repeat the entire encounter/stop/absence/full-stop/restart/recall flow until `npm run aw:smoke -- --case gate-a-manifest` reports the `LIM-GA-014` consecutive count is met. A failure resets the consecutive count after repair.

## Backup, restore, and reset

### Verify a restore without touching live data

```powershell
npm run aw:shutdown
npm run aw:db:restore -- --from .\data\backups\pre-play.sqlite --to .\data\restore-check.sqlite
```

Expected: `PASS: restore verified`; live `data\agentic-world.sqlite` remains unchanged.

### Safeguarded reset

First request a token:

```powershell
npm run aw:reset -- --fixture gate-a --prepare
```

The script resolves and prints the configured WorldId, verifies that it is not a broad filesystem target, creates a backup, and prints one exact confirmation command containing a one-time token. Copy that command verbatim. Expected final output is `PASS: reset complete; WorldEpoch=` followed by the new number. Never use broad paths or delete the data directory manually.

## Troubleshooting

| Symptom | Diagnosis command | Required response |
| --- | --- | --- |
| `FAIL: Node/Java mismatch` | `npm run aw:doctor` | run exact bootstrap command; do not edit lock record |
| Paper ready but bot cannot join | `npm run aw:smoke -- --case auth-join` | return to compatibility gate; verify auth/version/listener |
| bot joins but player is not authorized | `npm run aw:smoke -- --case principal-map` | repair alias/config; never authorize by session entity ID alone |
| chat duplicates | `npm run aw:smoke -- --case duplicate-speech` | stop Gate A; remove competing owner/retry before live use |
| follow never starts | `npm run aw:smoke -- --case pathfinding` | inspect chunks/movement/pathfinder gate; use recorded fallback |
| stop is slow | `npm run aw:smoke -- --case priority-stop` | verify high-priority lane; provider/mailbox must not block it |
| model calls while absent | `npm run aw:smoke -- --case absence` | Gate A fails; inspect suppression reason telemetry |
| restart claims completed action without evidence | `npm run aw:smoke -- --case reconciliation` | change state to unknown/interrupted and repair evidence rule |
| recall is missing | `npm run aw:smoke -- --case retrieval-v1` | inspect event/encounter promotion and top-five ranking |
| recall sounds like SQL/logs or invents certainty | experience fixture/report | fix context/prompt/retrieval; SQL visibility is not acceptance |
| database integrity/restore fails | `npm run aw:doctor` | preserve original; stop; restore only to a new path |

When a command says `FAIL`, paste its exact output to the next IDE agent. Do not rerun with a weaker flag, delete state, or declare success because another check passed.
