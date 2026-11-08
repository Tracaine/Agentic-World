#!/usr/bin/env python3
"""Render deterministic Markdown views from the canonical blueprint registry."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ARCH = Path(__file__).resolve().parents[1]
DEFAULT_BLUEPRINT = ARCH / "blueprint.json"
GENERATED = ARCH / "generated"


def cell(value: object) -> str:
    if value is None:
        return "—"
    if isinstance(value, list):
        return ", ".join(str(item) for item in value) or "—"
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend("| " + " | ".join(cell(value) for value in row) + " |" for row in rows)
    return "\n".join(lines)


def registry_view(data: dict) -> str:
    sections = [
        "# Generated Registry View",
        "",
        "> Generated from `blueprint.json`; do not hand edit.",
        "",
        f"Blueprint revision: {data['revision']}  ",
        f"Project status: {data['status']}",
    ]
    specs = [
        ("Requirements", "requirements", ["ID", "Status", "Priority", "Summary", "Acceptance", "Work", "Verification"]),
        ("Invariants", "invariants", ["ID", "Status", "Summary", "Enforcement", "Verification"]),
        ("Decisions", "decisions", ["ID", "Status", "Summary"]),
        ("Questions", "questions", ["ID", "Status", "Blocking", "Summary", "Resolution"]),
        ("Risks", "risks", ["ID", "Status", "Summary", "Trigger", "Mitigation"]),
        ("Components", "components", ["ID", "Status", "Summary", "Requirements"]),
        ("Interfaces", "interfaces", ["ID", "Status", "Summary", "From", "To", "Contract"]),
        ("Data", "data_entities", ["ID", "Status", "Summary", "Owner", "Persistence"]),
        ("Flows", "flows", ["ID", "Status", "Summary"]),
        ("Verifications", "verifications", ["ID", "Status", "Summary", "Target", "Method", "Evidence"]),
    ]
    for title, key, headers in specs:
        rows: list[list[object]] = []
        for item in data["registries"][key]:
            if key == "requirements":
                rows.append([item["id"], item["status"], item.get("priority"), item["summary"], item.get("acceptance"), item.get("implemented_by"), item.get("verified_by")])
            elif key == "invariants":
                rows.append([item["id"], item["status"], item["summary"], item.get("enforcement"), item.get("verified_by")])
            elif key == "questions":
                rows.append([item["id"], item["status"], item.get("blocking", False), item["summary"], item.get("resolution")])
            elif key == "risks":
                rows.append([item["id"], item["status"], item["summary"], item.get("trigger"), item.get("mitigation")])
            elif key == "components":
                rows.append([item["id"], item["status"], item["summary"], item.get("requirements")])
            elif key == "interfaces":
                rows.append([item["id"], item["status"], item["summary"], item.get("from"), item.get("to"), item.get("contract")])
            elif key == "data_entities":
                rows.append([item["id"], item["status"], item["summary"], item.get("owner"), item.get("persistence")])
            elif key == "verifications":
                rows.append([item["id"], item["status"], item["summary"], item.get("target"), item.get("method"), item.get("evidence")])
            else:
                rows.append([item["id"], item["status"], item["summary"]])
        sections.extend(["", f"## {title}", "", table(headers, rows)])
    return "\n".join(sections) + "\n"


def limits_view(data: dict) -> str:
    rows = [[item["id"], item["name"], item["value"], item["scope"], item["meaning"]] for item in data["limits"]]
    return "\n".join([
        "# Generated Numeric Limits",
        "",
        "> Generated from `blueprint.json.limits`; do not hand edit. Code configuration and tests must use these names/IDs.",
        "",
        table(["ID", "Name", "Value", "Scope", "Meaning"], rows),
        "",
    ])


def features_view(data: dict) -> str:
    groups = ["required now", "architectural seam only", "deferred until after proof", "speculative future capability"]
    parts = ["# Generated Feature Classification", "", "> Generated from `blueprint.json.feature_classification`; do not hand edit."]
    for group in groups:
        parts.extend(["", f"## {group}", ""])
        parts.extend(f"- {item['feature']}" for item in data["feature_classification"] if item["class"] == group)
    return "\n".join(parts) + "\n"


def work_view(data: dict) -> str:
    rows = [[item["id"], item["status"], item.get("classification"), item["summary"], item.get("depends_on"), item["artifact"]] for item in data["registries"]["work_items"]]
    spike = data["spikes"][0]
    parts = [
        "# Generated Work Index",
        "",
        "> Generated from `blueprint.json`; do not hand edit. Execution details live only in the referenced work file.",
        "",
        "## Step Zero",
        "",
        f"- **{spike['id']}** — {spike['summary']} (`{spike['artifact']}`)",
        "",
        "## Work packages",
        "",
        table(["ID", "Status", "Class", "Outcome", "Depends on", "Canonical work file"], rows),
        "",
        "## Gate-A chain",
        "",
        "`SPIKE-000 → WRK-001 → WRK-002 → WRK-003 → WRK-004 → WRK-005`",
        "",
    ]
    return "\n".join(parts)


def render(data: dict) -> dict[Path, str]:
    return {
        GENERATED / "registry.md": registry_view(data),
        GENERATED / "limits.md": limits_view(data),
        GENERATED / "feature-classification.md": features_view(data),
        GENERATED / "work-index.md": work_view(data),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blueprint", type=Path, default=DEFAULT_BLUEPRINT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.blueprint.read_text(encoding="utf-8"))
    outputs = render(data)
    if args.check:
        stale = [str(path.relative_to(ARCH)) for path, expected in outputs.items() if not path.exists() or path.read_text(encoding="utf-8") != expected]
        if stale:
            print("FAIL: generated views stale: " + ", ".join(stale))
            return 1
        print("PASS: generated views match blueprint.json")
        return 0
    GENERATED.mkdir(parents=True, exist_ok=True)
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"PASS: rendered {path.relative_to(ARCH)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
