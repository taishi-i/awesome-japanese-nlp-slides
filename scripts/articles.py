"""Load and validate ``data/articles.json``.

``data/articles.json`` is the single source of truth for the companion list of
web pages and blog posts (as opposed to ``data/curated.json``, which holds the
slide decks). It reuses the same 32 section names as ``curated.json`` — see
``scripts/slides.py`` — so a section's translated name comes from the very
same ``data/locales/*.json`` entries; only the blurb in ``articles.json``
itself (Japanese) is specific to this list.

Run this module directly to validate the file without generating anything.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

from slides import ROOT, clean

SRC = ROOT / "data" / "articles.json"

#: Fields every entry must carry. Unlike curated.json, there is no ``source``
#: field: articles are not confined to a handful of known platforms.
REQUIRED_FIELDS = ("title", "url", "author", "date")

#: Optional: the date (YYYY-MM-DD) the entry was added to this list. Entries
#: added within the last 7 days show up in the "latest additions" section;
#: omit it and the entry is simply never featured there.
ADDED_FIELD = "added"

#: How many days an entry stays in the "latest additions" section.
LATEST_WINDOW_DAYS = 7

_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")

Section = dict[str, Any]
Entry = dict[str, Any]


def _check_entry(entry: Entry, where: str, seen_urls: dict[str, str]) -> list[str]:
    """Return the problems found in a single entry."""
    problems = []
    for field in REQUIRED_FIELDS:
        if not entry.get(field):
            problems.append(f"{where}: {field} is empty")

    date_value = entry.get("date")
    if date_value and not _DATE.fullmatch(date_value):
        problems.append(f"{where}: date must be YYYY-MM-DD (got: {date_value})")

    added = entry.get(ADDED_FIELD)
    if added and not _DATE.fullmatch(added):
        problems.append(f"{where}: added must be YYYY-MM-DD (got: {added})")

    url = entry.get("url")
    if url in seen_urls:
        problems.append(f"{where}: duplicate URL, already used by {seen_urls[url]}")
    elif url:
        seen_urls[url] = where

    return problems


def _check(sections: list[Section]) -> list[str]:
    """Return every problem found in the whole file, in document order."""
    problems: list[str] = []
    seen_sections: dict[str, int] = {}
    seen_urls: dict[str, str] = {}

    for index, section in enumerate(sections):
        name = section.get("section")
        where = f"[{index}] {name or '(section missing)'}"

        for key in ("section", "blurb", "entries"):
            if not section.get(key):
                problems.append(f"{where}: {key} is missing")

        if name in seen_sections:
            problems.append(
                f"{where}: section name already used by [{seen_sections[name]}]"
            )
        seen_sections[name] = index

        for position, entry in enumerate(section.get("entries") or []):
            title = str(entry.get("title"))[:40]
            at = f"{where} entries[{position}] {title}"
            problems += _check_entry(entry, at, seen_urls)

    return problems


def load(path: Path = SRC) -> list[Section]:
    """Return the validated sections of ``path``.

    Exits with status 1 after reporting every problem it found, so that a bad
    edit can never reach the generated files.
    """
    sections: list[Section] = json.loads(path.read_text(encoding="utf-8"))

    problems = _check(sections)
    if problems:
        name = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        print(f"{name} has {len(problems)} problem(s):", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        sys.exit(1)

    # Absorb the formatting noise once, here, so the generators never have to.
    for section in sections:
        for entry in section["entries"]:
            entry["title"] = clean(entry["title"])
            entry["author"] = clean(entry["author"])
    return sections


def count(sections: list[Section]) -> int:
    """Return the total number of entries across ``sections``."""
    return sum(len(section["entries"]) for section in sections)


def is_recent(entry: Entry, today: date, days: int = LATEST_WINDOW_DAYS) -> bool:
    """Return whether ``entry`` was added within the last ``days`` days of ``today``.

    Same semantics as ``slides.is_recent``: no ``added`` field, or one in the
    future, is never recent.
    """
    added = entry.get(ADDED_FIELD)
    if not added:
        return False
    try:
        added_date = date.fromisoformat(added)
    except ValueError:
        return False
    age = (today - added_date).days
    return 0 <= age < days


if __name__ == "__main__":
    loaded = load()
    print(f"ok: {count(loaded)} entries in {len(loaded)} sections")
