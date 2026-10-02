#!/usr/bin/env python3
"""Deterministic scorer for StackAI Claude Code readiness assessments."""

import argparse
import json
import sys
from pathlib import Path

DIMENSIONS = [
    "business_objective",
    "system_access",
    "asset_ownership",
    "internal_owner",
    "dev_test_rollback",
    "permissions_governance",
    "security",
    "ongoing_support",
]

def status_for(score: int) -> str:
    if score >= 13:
        return "ready_for_pilot"
    if score >= 9:
        return "ready_after_limited_preparation"
    if score >= 5:
        return "preparation_required"
    return "start_with_mapping"

def validate_and_score(data: dict) -> dict:
    scores = data.get("scores")
    if not isinstance(scores, dict):
        raise ValueError("Missing 'scores' object.")

    missing = [d for d in DIMENSIONS if d not in scores]
    if missing:
        raise ValueError("Missing score dimensions: " + ", ".join(missing))

    for key in DIMENSIONS:
        value = scores[key]
        if not isinstance(value, int) or value not in (0, 1, 2):
            raise ValueError(f"{key} must be an integer 0, 1, or 2.")

    total = sum(scores[d] for d in DIMENSIONS)
    data["total_score"] = total
    data["readiness_status"] = status_for(total)
    return data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to assessment JSON")
    parser.add_argument("-o", "--output", help="Optional output JSON path")
    args = parser.parse_args()

    path = Path(args.input)
    data = json.loads(path.read_text(encoding="utf-8"))
    result = validate_and_score(data)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)

    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)