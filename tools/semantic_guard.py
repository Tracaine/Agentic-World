#!/usr/bin/env python3
"""Lightweight semantic audit for revision-2 Agentic-World blueprint invariants."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

from render_blueprint import render


ARCH = Path(__file__).resolve().parents[1]


class Audit:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)

    def finish(self) -> int:
        if self.errors:
            for error in self.errors:
                print(f"FAIL: {error}")
            print(f"FAIL: semantic guard found {len(self.errors)} issue(s)")
            return 1
        print("PASS: semantic guard found 0 issues")
        return 0


def by_id(items: list[dict]) -> dict[str, dict]:
    return {item["id"]: item for item in items}


def check_dag(audit: Audit, work: dict[str, dict]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(item_id: str) -> None:
        if item_id in visited:
            return
        if item_id in visiting:
            audit.require(False, f"work dependency cycle reaches {item_id}")
            return
        visiting.add(item_id)
        for dependency in work[item_id].get("depends_on", []):
            audit.require(dependency in work, f"{item_id} depends on missing {dependency}")
            if dependency in work:
                visit(dependency)
        visiting.remove(item_id)
        visited.add(item_id)

    for item_id in work:
        visit(item_id)


def check_work_recipes(audit: Audit) -> None:
    """Reject micro-steps that are not independently executable by an IDE agent."""
    required_markers = {
        "objective": "- **Objective:**",
        "prerequisites": "- **Prerequisites/prior checkpoint:**",
        "files": "- **Exact files/modules:**",
        "prompt": "- **Paste-ready IDE-agent prompt:**",
    }
    alternate_markers = {
        "commands": ("- **Commands:**", "- **Exact commands:**"),
        "expected": ("- **Expected:**", "- **Expected success output:**"),
        "pass_fail": ("- **Pass/fail:**", "- **Objective pass/fail:**"),
        "symptoms": ("- **Symptoms:**", "- **Common symptoms:**"),
        "recovery": ("- **Recovery:**", "- **Recovery/rollback:**"),
        "stop": ("- **Stop:**", "- **Stop condition:**"),
        "checkpoint": ("- **Checkpoint:**", "- **Proving artifact/checkpoint:**"),
    }
    ambiguous_scope = re.compile(
        r"<[^>]+>|/\*|\*\.[A-Za-z0-9]+|\bresume state\b|\bnew numbered migration\b|"
        r"\bone named\b|\btyped repository/migration additions\b|\bexplicitly approved `src/ports/` revisions\b",
        flags=re.IGNORECASE,
    )
    heading = re.compile(r"^## ((?:S0|\d+)\.\d+[A-Z]?)\b.*$", flags=re.MULTILINE)

    paths = [ARCH / "work-items" / "SPIKE-000.md", *sorted((ARCH / "work-items").glob("WRK-[0-9][0-9][0-9].md"))]
    for path in paths:
        body = path.read_text(encoding="utf-8")
        matches = list(heading.finditer(body))
        audit.require(bool(matches), f"{path.name} has no executable micro-step")
        for index, match in enumerate(matches):
            step_id = match.group(1)
            end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
            section = body[match.start():end]
            for label, marker in required_markers.items():
                audit.require(marker in section, f"{path.name} {step_id} missing {label}")
            for label, markers in alternate_markers.items():
                audit.require(any(marker in section for marker in markers), f"{path.name} {step_id} missing {label}")
            files_line = next((line for line in section.splitlines() if line.startswith("- **Exact files/modules:**")), "")
            audit.require(bool(files_line), f"{path.name} {step_id} has no exact file line")
            audit.require(ambiguous_scope.search(files_line) is None, f"{path.name} {step_id} has ambiguous file scope: {files_line}")
            audit.require("architecture/10-resume-state.md" in files_line, f"{path.name} {step_id} does not name the resume-state checkpoint")
            command_start = section.find("```powershell")
            command_end = section.find("```", command_start + len("```powershell")) if command_start >= 0 else -1
            audit.require(command_start >= 0 and command_end > command_start, f"{path.name} {step_id} lacks a PowerShell command block")
            if command_start >= 0 and command_end > command_start:
                commands = section[command_start:command_end]
                audit.require(re.search(r"<[^>]+>", commands) is None, f"{path.name} {step_id} command contains an unresolved placeholder")
            checkpoint_line = next(
                (
                    line
                    for line in section.splitlines()
                    if line.startswith("- **Checkpoint:**") or line.startswith("- **Proving artifact/checkpoint:**")
                ),
                "",
            )
            audit.require(re.search(r"`[^`]+/[^`]+`", checkpoint_line) is not None, f"{path.name} {step_id} checkpoint lacks an exact repository-relative evidence path")
            audit.require("resume state" not in checkpoint_line.lower(), f"{path.name} {step_id} checkpoint names vague resume state instead of architecture/10-resume-state.md")
            scoped_paths = set(re.findall(r"`([^`]+/[^`]+)`", files_line))
            checkpoint_paths = set(re.findall(r"`([^`]+/[^`]+)`", checkpoint_line))
            for checkpoint_path in checkpoint_paths:
                audit.require(checkpoint_path in scoped_paths, f"{path.name} {step_id} checkpoint path is absent from exact file scope: {checkpoint_path}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("blueprint", nargs="?", type=Path, default=ARCH / "blueprint.json")
    args = parser.parse_args()
    audit = Audit()
    data = json.loads(args.blueprint.read_text(encoding="utf-8"))
    registries = data["registries"]
    requirements = by_id(registries["requirements"])
    decisions = by_id(registries["decisions"])
    questions = by_id(registries["questions"])
    components = by_id(registries["components"])
    interfaces = by_id(registries["interfaces"])
    entities = by_id(registries["data_entities"])
    work = by_id(registries["work_items"])
    limits = {item["name"]: item["value"] for item in data["limits"]}
    audit.require(len(limits) == len(data["limits"]), "canonical limit names are not unique")
    audit.require(len({item["id"] for item in data["limits"]}) == len(data["limits"]), "canonical limit IDs are not unique")

    # Generated registry views must be byte-for-byte current.
    stale_views = [str(path.relative_to(ARCH)) for path, expected in render(data).items() if not path.exists() or path.read_text(encoding="utf-8") != expected]
    audit.require(not stale_views, "generated views are stale: " + ", ".join(stale_views))

    # Timeout and budget coherence.
    required_limits = {
        "addressed_chat_outer_slo_ms",
        "model_deadline_ms",
        "action_dispatch_deadline_ms",
        "utterance_submission_deadline_ms",
        "follow_re_evaluation_interval_ms",
        "follow_behavior_timeout_ms",
        "priority_control_dispatch_slo_ms",
        "cognition_pending_queue_max",
        "addressed_chat_coalesce_window_ms",
        "addressed_chat_trigger_cooldown_ms",
        "model_automatic_retry_max",
        "defining_proof_consecutive_repetitions",
    }
    audit.require(required_limits.issubset(limits), "canonical Gate-A limit set is incomplete")
    if required_limits.issubset(limits):
        audit.require(limits["model_deadline_ms"] < limits["addressed_chat_outer_slo_ms"], "model deadline must be inside outer response SLO")
        audit.require(limits["addressed_chat_outer_slo_ms"] - limits["model_deadline_ms"] == 2000, "model/outer SLO margin must be explicit 2000 ms")
        audit.require(limits["follow_behavior_timeout_ms"] > limits["model_deadline_ms"], "follow behavior must be able to outlive cognition")
        audit.require(limits["action_dispatch_deadline_ms"] < limits["model_deadline_ms"], "dispatch deadline must not contain behavior duration")
        audit.require(limits["model_automatic_retry_max"] == 0, "Gate A automatic model retry must be zero")
        audit.require(limits["cognition_pending_queue_max"] == 2, "Gate A pending queue must be exactly two")
        audit.require(limits["defining_proof_consecutive_repetitions"] == 3, "Gate A proof repetition count must be three")

    # Closed contracts, lifecycle, speech, and evidence.
    contract_path = ARCH / "contracts" / "platform-contracts.md"
    contract = contract_path.read_text(encoding="utf-8")
    for required in [
        '"OFFLINE"', '"CONNECTING"', '"SYNCING"', '"READY"', '"DISCONNECTED"', '"FAULTED"',
        '"ACTIVE"', '"SUSPENDED"', '"PAUSED"',
        "ComponentHealthState", "CognitionRequest", "ModelDecision", "UtteranceProposal",
        "ImmediateDispatchResult", "BehaviorEvent", "CapabilityEvidence", "PrincipalId", "WorldId", "WorldEpoch",
    ]:
        audit.require(required in contract, f"contract missing {required}")
    for banned in ["Record<string, unknown>", "normalizedPayload", "finalSpeech", 'kind: "speak"', "replacement:"]:
        audit.require(banned not in contract, f"critical contract contains banned generic/competing field {banned}")
    audit.require(contract.count("export interface UtteranceSubmissionPort") == 1, "contract must declare exactly one utterance submission port")
    audit.require("attemptNumber: 1" in contract, "utterance contract must fix the Gate-A attempt number at one")
    action_section = contract.split("export type ActionRequest =", 1)[1].split("export type ActionRejectionReason", 1)[0]
    audit.require("utterance" not in action_section.lower(), "physical ActionRequest union must not contain utterance delivery")
    audit.require('kind: "started"' in contract and "BehaviorId" in contract, "behavior dispatch must return started plus stable BehaviorId")
    audit.require("dispatch_acknowledged" in contract and "client_observed" in contract and "server_confirmed" in contract and "reconciled" in contract and 'kind: "unknown"' in contract, "typed evidence states are incomplete")
    audit.require("GateAEvidenceRule" in contract and "`dispatch_acknowledged` alone cannot complete" in contract, "capability evidence thresholds are not explicit")
    audit.require("payload:" not in contract and "self:" not in contract, "critical contracts retain a generic payload/self field")

    # One speech owner across registry.
    audit.require("sole utterance" in components["CMP-003"]["summary"].lower(), "CMP-003 must be the sole utterance owner")
    audit.require(interfaces["INT-011"]["from"] == "CMP-003", "INT-011 must originate only from CMP-003")
    audit.require("speech" in decisions["DEC-010"]["summary"].lower(), "DEC-010 speech decision missing")
    audit.require("speech" not in interfaces["INT-004"]["contract"].lower(), "INT-004 contract must not own speech")

    # Identity, profile ownership, and persistence.
    for entity_id in ["DAT-015", "DAT-016", "DAT-017", "DAT-018"]:
        audit.require(entity_id in entities, f"missing Gate-A data entity {entity_id}")
    audit.require("Parallax/Lattice" in decisions["DEC-011"]["summary"], "external persona ownership not resolved")
    audit.require(questions["QST-007"]["status"] == "resolved", "AgentProfile ownership remains unresolved")
    audit.require("personaPackageRef" in contract and "ProfileSourcePort" in contract, "profile reference/read port missing")
    gate_a_tables = {"agents", "principals", "principal_aliases", "worlds", "world_epochs", "world_sessions", "events", "conversations", "utterances", "model_runs", "action_attempts", "behavior_runs", "encounters", "encounter_events", "schema_metadata"}
    state_doc = (ARCH / "03-domain-state-data.md").read_text(encoding="utf-8")
    audit.require(all(f"`{name}`" in state_doc for name in gate_a_tables), "minimal Gate-A SQLite table catalogue is incomplete")
    audit.require(contract.count("explicit_remember_request") >= 2 and contract.count("designated_acceptance_action") >= 2, "encounter promotion rules must contain exactly the two named reasons in contract shapes")

    # Compatibility and version evidence.
    compatibility = data["compatibility_policy"]
    exact_rule = "Select and pin the newest smoke-tested stable intersection of Paper, Mineflayer, mineflayer-pathfinder, Java, and Node. Falling back to another verified combination requires no architecture review."
    audit.require(compatibility["rule"] == exact_rule, "compatibility rule differs from approved wording")
    required_record_fields = {"component", "exact_version", "source_url", "retrieved_at", "tested_at", "command", "result", "host_os", "fallback_used"}
    audit.require(required_record_fields.issubset(compatibility["record_fields"]), "compatibility record schema is incomplete")
    audit.require(len(compatibility["progressive_gates"]) >= 8, "progressive compatibility gates are incomplete")
    audit.require(len(compatibility["fallbacks"]) == 3, "each critical compatibility gate needs the three approved fallback classes")
    audit.require("node:sqlite" in decisions["DEC-005"]["summary"] and "better-sqlite3" in " ".join(decisions["DEC-005"]["alternatives"]), "DEC-005 binding and named fallback are unresolved")

    # Work dependency and Gate-A leakage.
    check_dag(audit, work)
    expected_gate_chain = {
        "WRK-001": [],
        "WRK-002": ["WRK-001"],
        "WRK-003": ["WRK-001", "WRK-002"],
        "WRK-004": ["WRK-002", "WRK-003"],
        "WRK-005": ["WRK-004"],
    }
    for item_id, dependencies in expected_gate_chain.items():
        audit.require(work[item_id].get("depends_on") == dependencies, f"{item_id} Gate-A dependencies differ from approved graph")
        audit.require(work[item_id].get("classification") == "required now", f"{item_id} must be required now")
        for req_id in work[item_id].get("requirements", []):
            audit.require(requirements[req_id]["status"] != "deferred", f"{item_id} leaks deferred requirement {req_id} into Gate A")
    audit.require("WRK-002" in work["WRK-004"]["depends_on"], "WRK-004 SQLite work must depend on WRK-002 Node pin")
    audit.require(data["spikes"][0]["id"] == "SPIKE-000" and len(data["spikes"][0]["gates"]) >= 9, "SPIKE-000 is missing or incomplete")
    check_work_recipes(audit)

    # Scope classification and source authorities.
    valid_classes = {"required now", "architectural seam only", "deferred until after proof", "speculative future capability"}
    audit.require({item["class"] for item in data["feature_classification"]} == valid_classes, "feature classification must use all and only four approved classes")
    for key in ["registry_work_graph_limits_and_classification", "implementation_status", "decision_rationale", "owner_runbook", "work_execution_details", "generated_views"]:
        audit.require(key in data["source_of_truth"], f"source-of-truth map missing {key}")
    audit.require(requirements["REQ-107"]["status"] == "deferred" and "WRK-014" in requirements["REQ-107"]["implemented_by"], "portability proof must be deferred to WRK-014")

    # Scan the most conflict-prone documents for retired duration/lifecycle phrases.
    conflict_docs = "\n".join((ARCH / name).read_text(encoding="utf-8") for name in [
        "03-domain-state-data.md", "05-interfaces-and-contracts.md", "06-runtime-flows.md", "07-quality-security-operations.md", "08-verification.md"
    ])
    for pattern in [r"IDLE\s*[↔<]", r"COGNIZING\s*[↔<]", r"ACTING\s*[↔<]", r"movement defaults? 20", r"follow.*30\s*s"]:
        audit.require(re.search(pattern, conflict_docs, flags=re.IGNORECASE) is None, f"retired lifecycle/time wording remains: {pattern}")

    # Active hand-maintained prose and Gate-A prompts must reference limit IDs,
    # not duplicate numeric values from blueprint.json.limits.
    limit_reference_docs = [
        "03-domain-state-data.md", "04-components-and-topology.md", "05-interfaces-and-contracts.md",
        "06-runtime-flows.md", "07-quality-security-operations.md", "08-verification.md",
        "work-items/WRK-001.md", "work-items/WRK-002.md", "work-items/WRK-003.md", "work-items/WRK-004.md",
    ]
    limit_reference_text = "\n".join((ARCH / name).read_text(encoding="utf-8") for name in limit_reference_docs)
    for literal in ["6000 ms", "8000 ms", "2000 ms", "1000 ms", "60000 ms", "250 ms", "750 ms", "500 ms", "15-minute", "15 minutes", "16-block", "10-second"]:
        audit.require(literal.lower() not in limit_reference_text.lower(), f"hand-maintained Gate-A prose duplicates canonical numeric limit: {literal}")

    return audit.finish()


if __name__ == "__main__":
    sys.exit(main())
