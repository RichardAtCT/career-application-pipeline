#!/usr/bin/env python3
"""Lightweight validation for a Career Application Pipeline workspace."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

REQUIRED = [
    "config.yaml",
    "cv/parsed-profile.yaml",
    "cv/search-criteria.yaml",
    "cv/cv-feedback.md",
    "tracker.csv",
    "source-inventory.yaml",
    "applications",
    "roles/raw",
    "roles/staged",
    "roles/verified",
]

TRACKER_HEADERS = [
    "role_id", "date_seen", "last_seen", "company", "role_title", "location", "remote_policy",
    "source_url", "application_url", "score", "status", "next_action", "follow_up_date",
    "application_pack_path", "notes",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate expected workspace files.")
    parser.add_argument("workspace")
    args = parser.parse_args()
    ws = Path(args.workspace).expanduser().resolve()

    errors = []
    for rel in REQUIRED:
        if not (ws / rel).exists():
            errors.append(f"missing: {rel}")

    tracker = ws / "tracker.csv"
    if tracker.exists():
        with tracker.open(newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader, [])
        if headers != TRACKER_HEADERS:
            errors.append(f"tracker headers differ: {headers}")

    if errors:
        print("Workspace validation failed:")
        for e in errors:
            print(f"- {e}")
        return 1

    print(f"Workspace validation passed: {ws}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
