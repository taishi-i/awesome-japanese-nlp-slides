"""Load and validate ``data/curated.json``.

``data/curated.json`` is the single source of truth of this repository: the
README files and the search data bundled with the plugin are both generated
from it. Generator scripts read it through this module so that every output
goes through the same validation.

Run this module directly to validate the file without generating anything.
"""

from __future__ import annotations

import html
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "curated.json"

#: Fields every entry must carry. All of them end up in the generated output.
REQUIRED_FIELDS = ("title", "url", "author", "date", "source")

#: Slide hosts the list covers. Used to keep ``source`` values consistent.
KNOWN_SOURCES = ("speakerdeck", "docswell")

_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
# Ideographic and non-breaking spaces are matched by ``\s`` as well, but naming
# them keeps the intent obvious: scraped titles are full of both.
_SPACES = re.compile(r"[\s\u3000\xa0]+")
_FILE_EXTENSION = re.compile(r"\.(pdf|pptx?|key)$", re.IGNORECASE)

Section = dict[str, Any]
Entry = dict[str, Any]


def clean(text: str) -> str:
    """Return ``text`` ready for display in a Markdown document.

    Resolves HTML entities, collapses runs of whitespace, and strips the file
    extension that some presenters leave in their slide title.
    """
    text = unicodedata.normalize("NFC", html.unescape(text or ""))
    text = _SPACES.sub(" ", text).strip()
    return _FILE_EXTENSION.sub("", text)


def _check_entry(entry: Entry, where: str, seen_urls: dict[str, str]) -> list[str]:
    """Return the problems found in a single entry."""
    problems = []
    for field in REQUIRED_FIELDS:
        if not entry.get(field):
            problems.append(f"{where}: {field} is empty")

    source = entry.get("source")
    if source and source not in KNOWN_SOURCES:
        expected = "/".join(KNOWN_SOURCES)
        problems.append(f"{where}: source must be one of {expected} (got: {source})")

    date = entry.get("date")
    if date and not _DATE.fullmatch(date):
        problems.append(f"{where}: date must be YYYY-MM-DD (got: {date})")

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
            entry["url"] = html.unescape(entry["url"])
    return sections


def count(sections: list[Section]) -> int:
    """Return the total number of entries across ``sections``."""
    return sum(len(section["entries"]) for section in sections)


if __name__ == "__main__":
    loaded = load()
    print(f"ok: {count(loaded)} entries in {len(loaded)} sections")
