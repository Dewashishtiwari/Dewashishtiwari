#!/usr/bin/env python3
"""Validate local profile assets and configuration."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
LOCAL_LINK = re.compile(r"""(?:src|href)=["'](\.?\.?/[^#?"']+)""")
ACTION_USE = re.compile(r"^\s*uses:\s*[^@\s]+@([^\s#]+)", re.MULTILINE)
IMMUTABLE_SHA = re.compile(r"^[0-9a-f]{40}$")
PLACEHOLDER = "YOUR_GITHUB_USERNAME"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail when the GitHub username placeholder remains.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    config = json.loads((ROOT / "profile.json").read_text(encoding="utf-8"))

    if args.strict and PLACEHOLDER in readme:
        errors.append(
            "GitHub username is not configured. Run the configure_profile.py script."
        )
    if args.strict and config.get("github_username") == PLACEHOLDER:
        errors.append("profile.json still contains the username placeholder.")

    for raw_path in LOCAL_LINK.findall(readme):
        clean = raw_path.split("#", 1)[0]
        target = (ROOT / clean).resolve()
        if ROOT not in target.parents and target != ROOT:
            errors.append(f"Local path escapes repository: {raw_path}")
        elif not target.exists():
            errors.append(f"Missing local asset: {raw_path}")

    for svg in sorted(ROOT.rglob("*.svg")):
        try:
            ET.parse(svg)
        except ET.ParseError as exc:
            errors.append(f"Invalid SVG {svg.relative_to(ROOT)}: {exc}")

    for workflow in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
        workflow_text = workflow.read_text(encoding="utf-8")
        for action_ref in ACTION_USE.findall(workflow_text):
            if not IMMUTABLE_SHA.fullmatch(action_ref):
                errors.append(
                    "Workflow action is not pinned to an immutable commit: "
                    f"{workflow.relative_to(ROOT)} uses @{action_ref}"
                )
        if "contents: write" in workflow_text and "schedule:" in workflow_text:
            errors.append(
                f"Write-enabled workflow must be manual-only: {workflow.relative_to(ROOT)}"
            )

    required_files = [
        "README.md",
        "SETUP_GUIDE.md",
        ".github/workflows/snake.yml",
        ".github/workflows/profile-3d.yml",
        ".github/workflows/profile-quality.yml",
    ]
    for relative in required_files:
        if not (ROOT / relative).exists():
            errors.append(f"Missing required file: {relative}")

    if errors:
        print("\n".join(f"ERROR: {item}" for item in errors), file=sys.stderr)
        return 1

    print("Profile validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
