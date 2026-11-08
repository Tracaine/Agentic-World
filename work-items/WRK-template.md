# WRK-NNN — Outcome

Classification: `required now | architectural seam only | deferred until after proof | speculative future capability`  
Registry: `blueprint.json`  
Status: `accepted | deferred`  
Canonical execution detail: this file

## Package outcome and boundary

State the single owner-visible outcome, exact prerequisites, exclusions, final package gate, and evidence directory. A package does not become complete from compilation or an agent narrative.

## Universal prompt policy

Copy this text into every micro-step prompt:

> Inspect the repository and prior checkpoint before editing; report `git status --short` and state the exact files you intend to change. Make only this bounded change, avoid unrelated refactors, and preserve contracts unless this step explicitly changes them. Run format, lint, typecheck, unit tests, relevant contract/integration tests, and the named smoke test. Report exact commands, exit codes, meaningful output, and omissions. Summarize behavior plainly. Stop rather than bypass, conceal, weaken, skip, or explain away a failure; compilation alone is not success. Produce pasteable evidence for a second agent.

## Micro-step N.1 — One objective

- **Objective:** one result only.
- **Prerequisites/prior checkpoint:** exact named artifact and passing command.
- **Exact files/modules:** exhaustive path list; no vague directory-only scope.
- **Paste-ready IDE-agent prompt:** include the universal policy plus the bounded request and explicit non-goals.
- **Exact commands:** ordered fenced command block.
- **Expected success output:** literal final lines/observable behavior.
- **Objective pass/fail:** binary assertions.
- **Common symptoms:** likely failures and what they mean.
- **Recovery/rollback:** restore only declared paths or discard disposable step; preserve prior checkpoint.
- **Stop condition:** exact point to return control.
- **Proving artifact/checkpoint:** `evidence/WRK-NNN/N.1.txt` plus every other exact evidence path named by this micro-step.

Repeat for each independent micro-step. Never write “implement adapter,” “wire runtime,” “add persistence,” or “verify correctness” without decomposing the exact behavior.

## Package gate

List ordered commands, required output, owner/manual action, and evidence manifest. Only this gate permits the status transition to `completed`; second-party reconciliation permits `verified`.
