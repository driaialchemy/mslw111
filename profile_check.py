"""Smoke check for the GitHub profile README repository."""

from __future__ import annotations

from pathlib import Path


REQUIRED_TERMS = ("AI", "data", "prompt")


def validate_profile_readme(path: Path = Path("README.md")) -> list[str]:
    problems: list[str] = []

    if not path.exists():
        return [f"{path} is missing"]

    text = path.read_text(encoding="utf-8")
    if not text.strip():
        problems.append(f"{path} is empty")

    lower_text = text.lower()
    missing_terms = [term for term in REQUIRED_TERMS if term.lower() not in lower_text]
    if missing_terms:
        problems.append("README is missing profile terms: " + ", ".join(missing_terms))

    return problems


def main() -> int:
    problems = validate_profile_readme()
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}")
        return 1

    print("Profile README smoke check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
