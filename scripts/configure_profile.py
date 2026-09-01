#!/usr/bin/env python3
"""Configure the profile repository with a GitHub username."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "profile.json"
USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Replace the GitHub username placeholder throughout the profile."
    )
    parser.add_argument("--username", required=True, help="Your exact GitHub login")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    username = args.username.strip()
    if not USERNAME_PATTERN.fullmatch(username):
        raise SystemExit(
            "Invalid GitHub username. Use 1-39 letters, numbers or single hyphens; "
            "do not begin or end with a hyphen."
        )

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    old_username = config.get("github_username", "YOUR_GITHUB_USERNAME")
    if old_username == username:
        print(f"Profile is already configured for {username}.")
        return 0

    targets = [
        ROOT / "README.md",
        ROOT / "SETUP_GUIDE.md",
        ROOT / "REPOSITORY_ROADMAP.md",
        ROOT / ".github" / "workflows" / "metrics.yml",
    ]
    for path in targets:
        text = path.read_text(encoding="utf-8")
        text = text.replace("YOUR_GITHUB_USERNAME", username)
        if old_username and old_username != "YOUR_GITHUB_USERNAME":
            text = text.replace(old_username, username)
        path.write_text(text, encoding="utf-8")

    config["github_username"] = username
    CONFIG_PATH.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    print(f"Configured profile for github.com/{username}")
    print(f"Create the public repository: {username}/{username}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

