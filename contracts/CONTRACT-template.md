# INT-NNN — Contract title

- Status: proposed
- From:
- To:
- Requirements:
- Owner:

## Purpose

## Invocation or transport

## Input

Define a project-owned closed discriminated union. Each `kind` fixes every field, constraint, default, and example. Unknown vendor data may appear only as the adapter parser's input and must not enter core. Do not use a generic map, generic payload/body, arbitrary capability arguments, or model-selected identity/authority.

## Preconditions and authorization

## Output

Define immediate dispatch separately from later behavior/evidence events when work is long-running. Include rejected, failed, interrupted, cancelled, timed-out, and unknown where applicable. `started` and dispatch acknowledgement are not success.

## Behavioral semantics

Define state effects, authority, ordering, idempotency, duplicate handling, and consistency.

## Timing and control

Reference canonical limit IDs from `blueprint.json`; do not create a new literal silently. Define deadline, retry count, rate limit, cancellation, priority-control behavior, backpressure, queue overflow, and stale-input behavior. State whether work may outlive cognition/actor processing.

## Authority and evidence

Name the authority for each status transition and the minimum capability-specific environment-derived evidence. Evidence kinds are not automatically totally ordered. Define unconfirmed/unknown and reconciliation without blind retry.

## Identity and idempotency

Name stable project IDs, transport alias mapping, idempotency key, duplicate behavior, world/epoch constraints, and restart handling. Models/adapters cannot choose authority IDs.

## Compatibility

Define versioning, migration, and independent deployment expectations.

## Observability

Define correlation, logs, metrics, traces, and audit evidence.

## Verification

Link VER items and executable contract checks.
