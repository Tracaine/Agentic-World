# Generated Numeric Limits

> Generated from `blueprint.json.limits`; do not hand edit. Code configuration and tests must use these names/IDs.

| ID | Name | Value | Scope | Meaning |
| --- | --- | --- | --- | --- |
| LIM-GA-001 | addressed_chat_outer_slo_ms | 8000 | Gate A | p95 from accepted stimulus to the one utterance submission attempt |
| LIM-GA-002 | model_deadline_ms | 6000 | Gate A | hard ModelPort deadline; leaves an explicit 2000 ms outer-SLO margin |
| LIM-GA-003 | action_dispatch_deadline_ms | 1000 | Gate A | maximum from validated proposal to immediate dispatch result |
| LIM-GA-004 | utterance_submission_deadline_ms | 1000 | Gate A | maximum for validation plus one environment submission attempt |
| LIM-GA-005 | follow_re_evaluation_interval_ms | 1000 | Gate A | deterministic target/hazard/lease recheck while active |
| LIM-GA-006 | follow_behavior_timeout_ms | 60000 | Gate A | terminal timeout independent of the cognition run |
| LIM-GA-007 | priority_control_dispatch_slo_ms | 250 | Gate A | p95 stop, suspension, shutdown, or emergency-stop dispatch |
| LIM-GA-008 | cognition_pending_queue_max | 2 | Gate A | pending runs per agent, excluding the active run |
| LIM-GA-009 | addressed_chat_coalesce_window_ms | 750 | Gate A | same-principal messages merge before a run starts |
| LIM-GA-010 | addressed_chat_trigger_cooldown_ms | 500 | Gate A | duplicate source events suppress; distinct later messages remain eligible |
| LIM-GA-011 | perception_radius_blocks | 16 | Gate A | maximum ordinary nearby entity/player scope |
| LIM-GA-012 | ordinary_event_soak_minutes | 15 | Gate A | ambient-noise test duration with no addressed chat |
| LIM-GA-013 | clean_shutdown_deadline_ms | 10000 | Gate A | after safety control; unfinished external outcomes become unknown/interrupted |
| LIM-GA-014 | defining_proof_consecutive_repetitions | 3 | Gate A | each repetition includes full Paper and runtime stop/restart |
| LIM-GA-015 | chat_character_max | 240 | Gate A | validated player-visible utterance length |
| LIM-GA-016 | model_automatic_retry_max | 0 | Gate A | a new player stimulus creates a new run; no hidden retry |
| LIM-GA-017 | automatic_reconnect_attempts_per_incident | 5 | Gate A | capped backoff 1s, 2s, 5s, 10s, 10s; remain DISCONNECTED after exhaustion |
| LIM-GA-018 | fts_required_top5_cases | 7 | Gate A | at least 7 of 8 fixed retrieval fixtures, with zero stale/prohibited top-3 results |
