# SPIKE-000 — Disposable Compatibility and Experiential Feasibility

Classification: `required now`  
Registry entry: `blueprint.json.spikes[0]`  
Status: required before WRK-001  
Location: disposable branch or `spikes/SPIKE-000/`; never copied wholesale into `src/`

## Outcome and boundary

With minimum disposable code, prove the real Windows/Paper/Mineflayer/pathfinder/OpenAI stack can join, map the authorized player, exchange deterministic chat, see positions/chunks, move, follow, stop immediately, produce one strict structured decision with one utterance, and survive disconnect/reconnect/full restart. Retain only compatibility evidence, failures, and adapter decisions.

Do not design production domain models, SQLite, memory, generic ports, a toy environment, dashboards, or polished character behavior.

Every prompt below already contains the mandatory IDE-agent policy. Execute one micro-step per task and stop at its checkpoint.

## S0.1 — Clean-machine preflight and disposable boundary

- **Objective:** establish a safe disposable location and record whether Windows, Git, PowerShell, Node, Java, Minecraft ownership, and credentials are available—without installing or changing versions.
- **Prerequisites/prior checkpoint:** blueprint structural/semantic/generated checks pass; `git status --short` has no unexplained changes.
- **Exact files/modules:** `spikes/SPIKE-000/README.md`, `spikes/SPIKE-000/evidence/preflight.txt`, `spikes/SPIKE-000/.gitignore`, `architecture/10-resume-state.md`.
- **Paste-ready IDE-agent prompt:**

  > Inspect the repository and prior checkpoint before editing; report `git status --short` and state the exact files you intend to change. Make only this bounded change, avoid unrelated refactors, and preserve contracts. Run all named checks and report exact commands, exit codes, meaningful output, and omissions. Stop rather than bypass, conceal, weaken, skip, install software, or explain away a failure; compilation alone is not success. Create only the SPIKE-000 disposable boundary and a redacted preflight record. Do not install Node/Java, download Paper, create production code, or expose credentials. Summarize behavior plainly and produce pasteable evidence for a second agent.

- **Exact commands:**

  ```powershell
  git status --short
  $PSVersionTable.PSVersion
  git --version
  node --version
  npm --version
  java -version
  winget --version
  python architecture\tools\semantic_guard.py architecture\blueprint.json
  ```

  Missing `node` or `java` is recorded as `WARN`, not hidden. Do not install in this step.
- **Expected success output:** semantic guard prints `PASS`; `preflight.txt` ends `PASS: S0.1 preflight recorded` and uses `PASS/WARN/FAIL` per prerequisite without secret values.
- **Objective pass/fail:** pass when disposable paths exist, the record names host OS/architecture and each prerequisite state, and production `src/`, `config/`, `package.json` are untouched. Fail on any secret value, install/change, unexplained worktree edit, or missing record.
- **Common symptoms:** command-not-found Node/Java = expected `WARN`; PowerShell <7 = `WARN` plus exact bootstrap need; dirty worktree = stop for reconciliation.
- **Recovery/rollback:** delete/discard only the new disposable branch/directory through normal Git tooling after preserving `preflight.txt`; never reset the repository.
- **Stop condition:** stop after S0.1 evidence and resume-state entry; do not choose versions.
- **Proving artifact/checkpoint:** `spikes/SPIKE-000/evidence/preflight.txt` and `architecture/10-resume-state.md`, both naming commands and exit codes.

## S0.2 — Primary-source record and candidate intersection

- **Objective:** read current primary sources and record one candidate plus one fallback version intersection; install nothing.
- **Prerequisites/prior checkpoint:** S0.1 artifact exists and semantic guard passes.
- **Exact files/modules:** `spikes/SPIKE-000/compatibility-candidates.json`, `spikes/SPIKE-000/evidence/source-read.txt`, `spikes/SPIKE-000/check-record.ps1`, `architecture/10-resume-state.md`.
- **Paste-ready IDE-agent prompt:**

  > Inspect the repository and S0.1 evidence first; report `git status --short` and exact intended files. Make only this bounded compatibility-record change; avoid unrelated refactors and do not install or pin production dependencies. Re-read official Paper requirements/download documentation, the official Mineflayer and mineflayer-pathfinder repositories, Node release and node:sqlite documentation, and official OpenAI model/structured-output documentation. Record exact URLs, retrieval time, candidate versions, fallback versions, rationale, commands, and unknowns. Add a validator that fails a missing required field. Run the named checks and report exact commands/results. Stop rather than guess, use secondary claims as authority, bypass missing evidence, or declare join compatibility from documentation alone. Produce pasteable evidence for a second agent.

- **Exact commands:**

  ```powershell
  $Mineflayer = Invoke-RestMethod https://registry.npmjs.org/mineflayer/latest
  $Pathfinder = Invoke-RestMethod https://registry.npmjs.org/mineflayer-pathfinder/latest
  $Mineflayer | Select-Object name,version,engines | ConvertTo-Json -Depth 5
  $Pathfinder | Select-Object name,version,peerDependencies | ConvertTo-Json -Depth 5
  pwsh -NoProfile -File .\spikes\SPIKE-000\check-record.ps1 -Path .\spikes\SPIKE-000\compatibility-candidates.json
  python architecture\tools\semantic_guard.py architecture\blueprint.json
  ```

- **Expected success output:** `PASS: compatibility candidate record complete`; record contains component, exact version, source URL, retrieved/tested dates (tested may be `pending`), command, result `not-tested`, host, and fallback.
- **Objective pass/fail:** pass only with all approved record fields, official URLs, candidate and fallback, and no “verified compatible” claim. Fail on a hard architecture edit or missing source/date.
- **Common symptoms:** docs disagree with package metadata = record discrepancy and choose neither until smoke; current Paper requires newer Java than older Minecraft = candidate intersection must use per-version table.
- **Recovery/rollback:** amend only candidate record; preserve source-read evidence. No production rollback should be necessary.
- **Stop condition:** stop before installing candidate versions.
- **Proving artifact/checkpoint:** validated `spikes/SPIKE-000/compatibility-candidates.json` and `spikes/SPIKE-000/evidence/source-read.txt`.

## S0.2A — Install and verify the selected host prerequisites

- **Objective:** install exactly the owner-approved candidate Node and Java runtimes on the clean Windows host, then verify their versions before any project package or Paper install.
- **Prerequisites/prior checkpoint:** S0.2 candidate and fallback records validate; the owner approves the candidate and authorizes the recorded system installations.
- **Exact files/modules:** `spikes/SPIKE-000/scripts/install-prerequisites.ps1`, `spikes/SPIKE-000/compatibility-candidates.json`, `spikes/SPIKE-000/evidence/prerequisites-install.txt`, `architecture/10-resume-state.md`.
- **Paste-ready IDE-agent prompt:**

  > Inspect the repository, S0.2 evidence, current installed versions, and exact candidate record; report the worktree and listed files. Create only a PowerShell prerequisite installer with `-Plan`, `-Apply`, and `-Verify` modes. It must read exact Node/Java versions, package IDs, official source URLs, and checksums from the candidate record; `-Plan` performs no mutation and prints the exact commands, `-Apply` requires owner confirmation and refuses unrecorded versions, and `-Verify` proves the installed versions. Do not install npm packages, Paper, a database binding, or production code. Do not silently substitute a version or package manager. Run plan first, ask the owner to approve the visible system change, then apply/verify. Report exact commands, exits, and redacted output. Stop if an exact package is unavailable and return to the recorded fallback rather than improvising.
- **Exact commands:**

  ```powershell
  pwsh -NoProfile -ExecutionPolicy Bypass -File .\spikes\SPIKE-000\scripts\install-prerequisites.ps1 -Record .\spikes\SPIKE-000\compatibility-candidates.json -Plan
  pwsh -NoProfile -ExecutionPolicy Bypass -File .\spikes\SPIKE-000\scripts\install-prerequisites.ps1 -Record .\spikes\SPIKE-000\compatibility-candidates.json -Apply
  pwsh -NoProfile -ExecutionPolicy Bypass -File .\spikes\SPIKE-000\scripts\install-prerequisites.ps1 -Record .\spikes\SPIKE-000\compatibility-candidates.json -Verify
  ```
- **Expected success output:** plan names exact official package/version commands without changing the host; apply records owner confirmation; verify ends `PASS: selected Node and Java prerequisites match candidate record`.
- **Objective pass/fail:** installed Node and Java outputs exactly match the candidate record and the evidence contains commands/source/checksum/date with no secrets. Any silent fallback, unexpected package, or version mismatch fails.
- **Common symptoms:** recorded version absent from `winget` = stop and use the record's official installer/checksum or fallback through a revised S0.2 record; terminal still sees old PATH = reopen PowerShell and run `-Verify`; elevation refused = stop without partial success.
- **Recovery/rollback:** use only the exact uninstall command printed in `-Plan` for a package installed by this step; preserve evidence and do not remove a pre-existing runtime.
- **Stop condition:** stop after version verification; do not install project packages or start Paper.
- **Proving artifact/checkpoint:** `spikes/SPIKE-000/evidence/prerequisites-install.txt` and `architecture/10-resume-state.md`, containing owner approval, exact versions, and command exits.

## S0.3 — Candidate install, Paper start, authentication, and join

- **Objective:** install only inside the disposable spike, start one loopback/private Paper instance, and prove bot authentication/join/spawn.
- **Prerequisites/prior checkpoint:** S0.2A verifies exact Node/Java; owner has accepted the candidate and authentication mode.
- **Exact files/modules:** `spikes/SPIKE-000/package.json`, `spikes/SPIKE-000/package-lock.json`, `spikes/SPIKE-000/paper/paper.jar`, `spikes/SPIKE-000/paper/eula.txt`, `spikes/SPIKE-000/paper/server.properties`, `spikes/SPIKE-000/src/join.mjs`, `spikes/SPIKE-000/scripts/start-paper.ps1`, `spikes/SPIKE-000/scripts/stop-paper.ps1`, `spikes/SPIKE-000/evidence/join.txt`, `spikes/SPIKE-000/compatibility-candidates.json`, `architecture/10-resume-state.md`.
- **Paste-ready IDE-agent prompt:**

  > Inspect the repo, S0.2 record, and worktree first; state exact files. Install only exact candidate packages in `spikes/SPIKE-000`, download only the exact recorded Paper artifact/checksum, and bind the disposable server to the approved private interface. Add the smallest join/spawn/clean-disconnect script and deterministic start/stop scripts. Do not add production ports, cognition, persistence, or copy spike code elsewhere. Run format/syntax checks and the exact join smoke. Report commands, exit codes, selected versions, listener address, and meaningful output. Stop rather than change versions silently, expose offline mode, disable authentication safeguards, or call join alone a complete compatibility proof.

- **Exact commands:**

  ```powershell
  Set-Location .\spikes\SPIKE-000
  npm ci
  pwsh -NoProfile -File .\scripts\start-paper.ps1
  node .\src\join.mjs --once
  pwsh -NoProfile -File .\scripts\stop-paper.ps1
  pwsh -NoProfile -File .\check-record.ps1 -Path .\compatibility-candidates.json
  ```

- **Expected success output:** `PASS: Paper ready on approved private address`; `PASS: bot authenticated, joined, spawned, and disconnected cleanly`; `PASS: Paper stopped cleanly`.
- **Objective pass/fail:** three consecutive join/spawn/clean-disconnect cycles pass on the same exact versions and listener is not unapproved public. Join failure or version drift fails.
- **Common symptoms:** protocol mismatch = try recorded fallback in a new subdirectory and update result; login rejected = repair selected auth, never weaken server exposure; chunk timeout after spawn = S0.5 issue, not yet a join failure if spawn event is complete.
- **Recovery/rollback:** stop Paper; discard the failed candidate install directory; preserve logs and create a new candidate record entry. Do not delete the prior record.
- **Stop condition:** stop after three join cycles; do not add presence/chat.
- **Proving artifact/checkpoint:** `spikes/SPIKE-000/evidence/join.txt` with versions, listener probe, three timestamps/results, and redacted logs.

## S0.4 — Authorized-player detection and deterministic chat

- **Objective:** map the configured Minecraft identity to a spike-local principal fixture and exchange deterministic, non-model chat once.
- **Prerequisites/prior checkpoint:** S0.3 three-cycle join checkpoint; human can join the private server.
- **Exact files/modules:** `spikes/SPIKE-000/src/presence-chat.mjs`, `spikes/SPIKE-000/config.local.example.json`, ignored `spikes/SPIKE-000/config.local.json`, `spikes/SPIKE-000/evidence/presence-chat.txt`, `architecture/10-resume-state.md`.
- **Paste-ready IDE-agent prompt:**

  > Inspect S0.3 evidence and repo first; state exact files. Add the smallest disposable script that observes player join/leave, maps the configured UUID or offline username to a spike-local principal label, ignores session entity ID as authorization, recognizes addressed chat, and sends one deterministic reply. Do not call a model, create production identity types, or accept non-addressed/unauthorized chat. Run syntax and live smoke with the owner. Report exact commands/events with identifiers redacted. Stop rather than loosen authorization or treat any nearby player as authorized.

- **Exact commands:**

  ```powershell
  Set-Location .\spikes\SPIKE-000
  pwsh -NoProfile -File .\scripts\start-paper.ps1
  # Owner joins, sends exactly: SpikeBot, ping; then leaves.
  node .\src\presence-chat.mjs
  pwsh -NoProfile -File .\scripts\stop-paper.ps1
  ```

  `presence-chat.mjs` prints `READY: owner action required`, waits for the listed join/chat/leave sequence, emits its PASS/FAIL result, and exits. If it does not exit, use `Ctrl+C`, run the listed stop command, and mark the step failed.
- **Expected success output:** `PASS: authorized player present`; one in-game `pong`; `PASS: addressed chat observed once`; `PASS: authorized player absent`; no response to non-addressed/unauthorized fixture.
- **Objective pass/fail:** exact one deterministic reply and correct presence transitions. Duplicate response, wrong identity, or response to ambient chat fails.
- **Common symptoms:** username seen but entity absent = wait for spawn/entity event and record; offline UUID unstable = use configured offline username only within loopback proof; duplicate chat events = dedupe by source signature in spike and record adapter behavior.
- **Recovery/rollback:** stop processes; revert only S0.4 files or fix disposable dedupe; keep S0.3 checkpoint intact.
- **Stop condition:** stop after presence/chat evidence; no movement/model.
- **Proving artifact/checkpoint:** `spikes/SPIKE-000/evidence/presence-chat.txt` with one reply and enter/leave events.

## S0.5 — Chunks, position, basic movement, pathfinding, follow, and immediate stop

- **Objective:** prove progressive embodiment through dynamic follow and immediate stop without digging/building.
- **Prerequisites/prior checkpoint:** S0.4 presence/chat passes; safe flat test area is loaded.
- **Exact files/modules:** `spikes/SPIKE-000/src/movement.mjs`, `spikes/SPIKE-000/evidence/movement.txt`, `spikes/SPIKE-000/compatibility-candidates.json`, `architecture/10-resume-state.md`.
- **Paste-ready IDE-agent prompt:**

  > Inspect S0.4 evidence and exact candidate versions first; state files. Extend only the disposable spike with sequential checks for agent/player position, chunk availability, one simple control-state movement, one pathfinder near-goal, dynamic `GoalFollow`, interruption, and forced immediate stop. Configure pathfinder with digging, block placement, towers, combat, and item use disabled. Log start/final positions and path events. Do not build production action abstractions or await follow indefinitely. Run each gate in order and stop on the first failure; record the approved fallback rather than hiding it. Report commands, exit codes, output, and owner-visible behavior.

- **Exact commands:**

  ```powershell
  Set-Location .\spikes\SPIKE-000
  pwsh -NoProfile -File .\scripts\start-paper.ps1
  # Owner joins the recorded private server and waits for the script's authorized-presence PASS.
  node .\src\movement.mjs --gate positions
  node .\src\movement.mjs --gate chunks
  node .\src\movement.mjs --gate basic
  node .\src\movement.mjs --gate path-near
  node .\src\movement.mjs --gate follow-stop
  pwsh -NoProfile -File .\scripts\stop-paper.ps1
  ```

- **Expected success output:** each gate ends `PASS`; follow logs movement toward the authorized player; stop logs goal cleared and zero controlled movement in its observation window.
- **Objective pass/fail:** every gate passes on exact versions; owner sees follow and immediate stop; forbidden pathfinder abilities remain false. A timeout/no-path after join fails the relevant gate and does not retire protocol risk.
- **Common symptoms:** unloaded chunks = pause/diagnose before pathfinding; `noPath` = try flat area/simpler movement; stop waits until next node = use documented goal clearing for emergency stop and record behavior.
- **Recovery/rollback:** stop bot/server; preserve failed gate log; use simpler movement or recorded fallback intersection. Do not expand cognition.
- **Stop condition:** stop after follow/interrupt/stop evidence; no model call.
- **Proving artifact/checkpoint:** `spikes/SPIKE-000/evidence/movement.txt` and `spikes/SPIKE-000/compatibility-candidates.json` with every progressive result.

## S0.6 — One structured model decision and one utterance

- **Objective:** prove one current supported OpenAI structured call can return the smallest decision containing one utterance; submit it once through the disposable chat path.
- **Prerequisites/prior checkpoint:** S0.5 passes; safe API credential is available; official OpenAI docs/model catalogue re-read and recorded that day.
- **Exact files/modules:** `spikes/SPIKE-000/src/model-decision.mjs`, `spikes/SPIKE-000/src/model-schema.mjs`, `spikes/SPIKE-000/evidence/model.txt`, `spikes/SPIKE-000/config.local.example.json`, ignored `spikes/SPIKE-000/config.local.json`, `spikes/SPIKE-000/compatibility-candidates.json`, `architecture/10-resume-state.md`.
- **Paste-ready IDE-agent prompt:**

  > Inspect S0.5 evidence, `LIM-GA-002`, current official OpenAI documentation, repo, and worktree first; state exact files. Add the simplest disposable OpenAI adapter that requests one strict structured object `{ utterance?: { text, intent } }`, with no tools/actions, no retries, the canonical model deadline, and redacted logs. Use the currently supported model recorded in the candidate file; do not hard-code it into architecture or use Agents SDK unless direct structured parsing cannot satisfy the one call. Validate text and make exactly one Mineflayer chat attempt. Do not log the key or full provider request. Run schema/fake failure checks before one explicit live call. Stop rather than retry, switch models silently, send partial text, or claim delivery without evidence.

- **Exact commands:**

  ```powershell
  Set-Location .\spikes\SPIKE-000
  node .\src\model-decision.mjs --fake valid
  node .\src\model-decision.mjs --fake invalid
  node .\src\model-decision.mjs --fake timeout
  pwsh -NoProfile -File .\scripts\start-paper.ps1
  # Owner joins the recorded private server and waits for authorized-presence PASS.
  node .\src\model-decision.mjs --live-once
  pwsh -NoProfile -File .\scripts\stop-paper.ps1
  ```

- **Expected success output:** fake cases classify correctly; live output says `PASS: one structured decision parsed`; Minecraft shows one utterance; log says `PASS: utterance submission attempts=1` with no credential.
- **Objective pass/fail:** valid schema within `LIM-GA-002` or typed timeout, one attempt, no action/tool. Duplicate, partial-send, secret, hidden retry, or unrecorded model/version fails.
- **Common symptoms:** unsupported schema keyword = simplify schema and record; first-schema latency >deadline = prewarm only as an explicit spike observation, never extend outer architecture silently; missing key = `WARN` and stop live gate.
- **Recovery/rollback:** stop server; preserve redacted failure; keep movement checkpoint. Change candidate model/adapter only with updated official source record.
- **Stop condition:** stop after one live utterance attempt; no production code or persistence.
- **Proving artifact/checkpoint:** `spikes/SPIKE-000/evidence/model.txt` with schema hash, model/SDK versions, latency, attempt count, result, and redaction check.

## S0.7 — Disconnect, reconnect, and complete restart

- **Objective:** characterize and prove client disconnect/reconnect and full Paper+spike restart on the candidate intersection.
- **Prerequisites/prior checkpoint:** S0.6 passes.
- **Exact files/modules:** `spikes/SPIKE-000/src/reconnect.mjs`, `spikes/SPIKE-000/scripts/restart-scenario.ps1`, `spikes/SPIKE-000/evidence/restart.txt`, `spikes/SPIKE-000/compatibility-candidates.json`, `architecture/10-resume-state.md`.
- **Paste-ready IDE-agent prompt:**

  > Inspect all prior spike evidence first; state exact files. Add only a disposable reconnect harness plus one PowerShell scenario driver that starts the recorded Paper process, starts the bot, waits for READY, stops Paper to cause real link loss, verifies DISCONNECTED, restarts Paper, verifies CONNECTING→SYNCING→READY, then stops both. Its fresh-process mode must start Paper and a new bot process, verify READY, and stop both. Demonstrate that a disconnected client makes no player-return claim. Use the canonical capped reconnect configuration and print explicit states. Do not add persistence, memory, production lifecycle code, or manual timing steps. Run the exact scenarios and report timestamps/exit codes. Stop rather than label reconnect as continuous observation or hide a failed restart.

- **Exact commands:**

  ```powershell
  Set-Location .\spikes\SPIKE-000
  pwsh -NoProfile -File .\scripts\restart-scenario.ps1 -Scenario ServerInterruption
  pwsh -NoProfile -File .\scripts\restart-scenario.ps1 -Scenario FreshProcess
  ```

- **Expected success output:** explicit READY → DISCONNECTED → CONNECTING → SYNCING → READY for recoverable interruption; fresh-process join passes; no return observation while disconnected.
- **Objective pass/fail:** both scenarios pass with exact versions and state evidence. Infinite retry, false presence claim, or failure to stop cleanly fails.
- **Common symptoms:** reconnect library stale state = recreate client and record adapter decision; Paper takes longer = doctor/readiness issue, not permission to invent READY.
- **Recovery/rollback:** stop processes; preserve logs; use fallback intersection if restart remains red.
- **Stop condition:** stop after restart evidence.
- **Proving artifact/checkpoint:** `spikes/SPIKE-000/evidence/restart.txt` and `spikes/SPIKE-000/compatibility-candidates.json` with completed progressive gates.

## S0.8 — Freeze findings and discard spike code

- **Objective:** produce the production-consumable compatibility result and adapter decisions, then make the spike disposable.
- **Prerequisites/prior checkpoint:** S0.1–S0.7, including S0.2A, all pass or every failed candidate was replaced by an explicitly accepted fallback that reran the affected gates; no unresolved red embodiment gate.
- **Exact files/modules:** read-only `spikes/SPIKE-000/check-record.ps1`, `evidence/SPIKE-000/compatibility-result.json`, `evidence/SPIKE-000/adapter-decisions.md`, `evidence/SPIKE-000/checksums.txt`, `architecture/10-resume-state.md`; no production source.
- **Paste-ready IDE-agent prompt:**

  > Inspect every spike artifact and repository first; state exact files. Consolidate only exact versions, official URLs, retrieval/test dates, commands/results, host, selected authentication, progressive gates, failures/fallbacks, model adapter choice, pathfinder stop behavior, and SQLite/Node facts into production-consumable evidence. Run the record validator and checksum files. Do not copy spike source, package dependencies, prompts, or ad hoc abstractions into production. Mark WRK-001 as next only if all required gates are green. Report exact commands/results and stop.

- **Exact commands:**

  ```powershell
  pwsh -NoProfile -File .\spikes\SPIKE-000\check-record.ps1 -Path .\evidence\SPIKE-000\compatibility-result.json
  python architecture\tools\semantic_guard.py architecture\blueprint.json
  python architecture\tools\render_blueprint.py --check
  Get-FileHash .\evidence\SPIKE-000\compatibility-result.json -Algorithm SHA256
  ```

- **Expected success output:** `PASS: compatibility candidate record complete`; all progressive gates `pass`; checksum recorded; resume state names WRK-001 step 1.1.
- **Objective pass/fail:** pass only if production retained evidence/decisions—not spike code—and every red gate is resolved. Fail if any spike source appears under `src/` or unresolved gate is softened.
- **Common symptoms:** desire to reuse “working” spike = extract behavior requirements, then reimplement behind WRK-001 contracts; version record missing test date = return to relevant gate.
- **Recovery/rollback:** remove only accidentally copied production files; keep spike evidence. Preserve the disposable branch until a second agent validates checksums, then discard normally.
- **Stop condition:** stop before WRK-001 implementation.
- **Proving artifact/checkpoint:** `evidence/SPIKE-000/compatibility-result.json`, `evidence/SPIKE-000/adapter-decisions.md`, `evidence/SPIKE-000/checksums.txt`, and `architecture/10-resume-state.md`.

## Spike gate

SPIKE-000 passes only when every progressive gate through full restart is green on one exact intersection, the structured model step makes one utterance attempt, and a second agent verifies that production contains only evidence/decisions. Otherwise embodiment remains the blocker and WRK-001 does not start.
