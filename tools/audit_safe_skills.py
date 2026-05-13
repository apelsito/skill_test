#!/usr/bin/env python3
"""Lightweight safety audit for local Codex skill fixtures."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


FAIL_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"ignore\s+all\s+previous\s+instructions",
        r"ignore\s+previous\s+instructions",
        r"exfiltrat",
        r"\bread\s+secrets?\b",
        r"\bsteal\b.*\b(secret|token|credential|password)s?\b",
        r"\bsend\b.*\b(secret|token|credential|password)s?\b",
        r"\bupload\b.*\b(secret|token|credential|password)s?\b",
        r"\bbypass\b.*\b(safety|policy|guardrail)s?\b",
        r"\bdisable\b.*\b(safety|policy|guardrail)s?\b",
        r"rm\s+-rf\s+[/~]",
        r"Remove-Item\s+.*-Recurse\s+.*-Force\s+.*(?:C:\\|/|~)",
        r"git\s+reset\s+--hard",
    ]
]

WARN_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"\bsubprocess\.",
        r"child_process",
        r"\bInvoke-WebRequest\b",
        r"\bInvoke-RestMethod\b",
        r"\brequests\.",
        r"\bfetch\s*\(",
        r"\bcurl\b",
        r"\bStart-Process\b",
        r"\beval\s*\(",
        r"\bexec\s*\(",
    ]
]

SENSITIVE_NAMES = {
    ".env",
    ".env.local",
    ".envrc",
    "id_rsa",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
}

SENSITIVE_SUFFIXES = {
    ".pem",
    ".p12",
    ".pfx",
    ".key",
}

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
    ".py",
    ".js",
    ".mjs",
    ".ts",
    ".tsx",
    ".jsx",
    ".toml",
    ".ps1",
    ".sh",
}


def is_sensitive_file(path: Path) -> bool:
    lower_name = path.name.lower()
    if lower_name in SENSITIVE_NAMES:
        return True
    if lower_name.startswith("secrets."):
        return True
    return path.suffix.lower() in SENSITIVE_SUFFIXES


def read_text(path: Path) -> str | None:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return None
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            return None


def frontmatter_fields(skill_md: Path) -> tuple[bool, bool]:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return False, False
    end = text.find("\n---", 3)
    if end == -1:
        return False, False
    frontmatter = text[3:end]
    has_name = re.search(r"(?m)^\s*name\s*:", frontmatter) is not None
    has_description = re.search(r"(?m)^\s*description\s*:", frontmatter) is not None
    return has_name, has_description


def audit(skills_dir: Path) -> dict:
    failures: list[dict] = []
    warnings: list[dict] = []
    skills: list[dict] = []

    if not skills_dir.exists():
        failures.append({"path": str(skills_dir), "issue": "skills directory missing"})
        return {"skills": skills, "failures": failures, "warnings": warnings}

    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        files = [path for path in skill_dir.rglob("*") if path.is_file()]
        skills.append({"name": skill_dir.name, "files": len(files)})

        if not skill_md.exists():
            failures.append({"path": str(skill_dir), "issue": "missing SKILL.md"})
            continue

        has_name, has_description = frontmatter_fields(skill_md)
        if not has_name:
            failures.append({"path": str(skill_md), "issue": "missing frontmatter name"})
        if not has_description:
            failures.append({"path": str(skill_md), "issue": "missing frontmatter description"})

        for path in files:
            rel = path.relative_to(skills_dir)
            if is_sensitive_file(path):
                failures.append({"path": str(rel), "issue": "sensitive file name"})
                continue

            text = read_text(path)
            if text is None:
                continue

            for pattern in FAIL_PATTERNS:
                match = pattern.search(text)
                if match:
                    failures.append(
                        {
                            "path": str(rel),
                            "issue": "blocked safety pattern",
                            "pattern": pattern.pattern,
                            "match": match.group(0)[:120],
                        }
                    )

            for pattern in WARN_PATTERNS:
                match = pattern.search(text)
                if match:
                    warnings.append(
                        {
                            "path": str(rel),
                            "issue": "review risky API or command",
                            "pattern": pattern.pattern,
                            "match": match.group(0)[:120],
                        }
                    )
                    break

    return {"skills": skills, "failures": failures, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", default="skills", type=Path)
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = parser.parse_args()

    report = audit(args.skills_dir)
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(f"Skills audited: {len(report['skills'])}")
        for item in report["skills"]:
            print(f"  - {item['name']}: {item['files']} files")
        print(f"Failures: {len(report['failures'])}")
        for item in report["failures"]:
            print(f"  FAIL {item['path']}: {item['issue']}")
            if "match" in item:
                print(f"       match: {item['match']}")
        print(f"Warnings: {len(report['warnings'])}")
        for item in report["warnings"][:20]:
            print(f"  WARN {item['path']}: {item['issue']} ({item['match']})")
        if len(report["warnings"]) > 20:
            print(f"  ... {len(report['warnings']) - 20} more warnings")

    return 1 if report["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
