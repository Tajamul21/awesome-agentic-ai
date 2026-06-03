#!/usr/bin/env python3
"""Lightweight metadata validator for Awesome Agentic AI Systems."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
URL_RE = re.compile(r"^https?://")


def load_yaml(path: Path) -> Any:
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(
            "PyYAML is required for full validation. Install with: pip install pyyaml"
        ) from exc
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_list_file(path: Path, required_keys: set[str]) -> int:
    data = load_yaml(path)
    require(isinstance(data, list), f"{path.name}: expected a list at top level")
    seen_titles: set[str] = set()
    for idx, item in enumerate(data, start=1):
        require(isinstance(item, dict), f"{path.name}:{idx}: expected mapping")
        missing = required_keys - set(item)
        require(not missing, f"{path.name}:{idx}: missing keys {sorted(missing)}")
        title = str(item.get("title", item.get("name", item.get("problem", "")))).strip()
        require(title, f"{path.name}:{idx}: empty title/name")
        key = title.lower()
        require(key not in seen_titles, f"{path.name}:{idx}: duplicate entry {title!r}")
        seen_titles.add(key)
        year = item.get("year")
        if year is not None:
            require(isinstance(year, int), f"{path.name}:{idx}: year must be integer")
            require(2019 <= year <= 2026, f"{path.name}:{idx}: suspicious year {year}")
        url = item.get("url") or item.get("paper_url")
        if url:
            require(bool(URL_RE.match(str(url))), f"{path.name}:{idx}: invalid URL {url!r}")
    return len(data)


def main() -> int:
    counts = {
        "papers": check_list_file(DATA / "papers.yaml", {"title", "year", "category"}),
        "benchmarks": check_list_file(DATA / "benchmarks.yaml", {"name", "year", "domain"}),
        "frameworks": check_list_file(DATA / "frameworks.yaml", {"name", "category"}),
        "open_problems": check_list_file(DATA / "open_problems.yaml", {"problem", "why"}),
    }
    for name, count in counts.items():
        print(f"OK: {name}: {count} entries")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
