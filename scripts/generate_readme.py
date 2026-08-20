"""Generate the awesome-list README for every language from ``data/curated.json``.

Input:  data/curated.json, data/locales/*.json
Output: the files listed under ``outputs`` in each locale
        (README.md, docs/README.ja.md, docs/README.en.md, ...)

Adding a language only takes one more JSON file in data/locales/.
"""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Any, NamedTuple

import articles
import slides
from slides import ROOT, Section

LOCALE_DIR = ROOT / "data" / "locales"

REPO_SLUG = "taishi-i/awesome-japanese-nlp-slides"
REPO_URL = f"https://github.com/{REPO_SLUG}"
BLOB_URL = f"{REPO_URL}/blob/main"

AWESOME_BADGE = (
    "https://cdn.rawgit.com/sindresorhus/awesome/"
    "d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"
)
PRS_BADGE = "https://img.shields.io/badge/PRs-welcome-brightgreen"
LICENSE_BADGE = "https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg"
LICENSE_URL = "http://creativecommons.org/publicdomain/zero/1.0/"

LOGO = "images/awesome-japanese-nlp-slides.png"

# The Zenn article introducing the search plugin/skill. The title is kept in
# Japanese in every language's README, same as deck titles (see titles_note).
ZENN_ARTICLE_URL = "https://zenn.dev/taishii/articles/523e4ffc13387d"
ZENN_ARTICLE_TITLE = (
    "日本語NLPの発表スライド560件を整理し、Claude Codeから検索するスキル"
)

Locale = dict[str, Any]


class RunInfo(NamedTuple):
    """The values that stay the same across every output file of a run."""

    nav: str
    today: date
    total_articles: int


_NON_ANCHOR = re.compile(r"[^\w\- ]", re.UNICODE)
_MARKDOWN = re.compile(r"([\[\]*_`])")


def anchor(text: str) -> str:
    """Return the heading anchor GitHub derives from ``text``."""
    return _NON_ANCHOR.sub("", text).strip().lower().replace(" ", "-")


def escape(text: str) -> str:
    """Escape the Markdown punctuation in ``text`` so titles survive as written."""
    return _MARKDOWN.sub(r"\\\1", text)


def load_locales() -> list[Locale]:
    """Return every data/locales/*.json, sorted by its ``order``."""
    locales = [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(LOCALE_DIR.glob("*.json"))
    ]
    return sorted(locales, key=lambda locale: locale["order"])


def nav_line(locales: list[Locale]) -> str:
    """Return the language switcher, using absolute URLs so docs/ can use it too.

    Each link points at the last of the locale's ``outputs`` (the copy under
    docs/). The root README.md and docs/README.ja.md hold the same text, so
    every language stays reachable from docs/.
    """
    return " | ".join(
        f"[{locale['nav_label']}]({BLOB_URL}/{locale['outputs'][-1]})"
        for locale in locales
    )


def _intro(
    strings: dict[str, str], nav: str, total: int, sections: int, depth: int
) -> list[str]:
    """Return the logo, badges, language switcher and opening notes."""
    lines = [
        "# awesome-japanese-nlp-slides",
        "",
        f"![{strings['logo_alt']}]({'../' * depth}{LOGO})",
        "",
        f"[![Awesome]({AWESOME_BADGE})]({REPO_URL})",
        f"[![PRs]({PRS_BADGE})]({REPO_URL}/pulls)",
        f"[![License: CC0-1.0]({LICENSE_BADGE})]({LICENSE_URL})",
        "",
        nav,
        "",
        *strings["intro"],
        "",
        strings["count"].format(total=total, sections=sections),
        "",
    ]
    # Titles are always kept in their original language, which is worth saying
    # in the translated editions.
    if strings.get("titles_note"):
        lines += [strings["titles_note"], ""]
    return [*lines, "> [!NOTE]", f"> {strings['wip_note']}", ""]


def _latest_additions(
    strings: dict[str, str], sections: list[Section], name_of: Any, today: date
) -> list[str]:
    """Return the section listing decks added in the last 7 days, grouped by section.

    Empty when nothing qualifies, so a quiet week leaves no trace in the
    README rather than an empty heading.
    """
    groups = [
        (name_of(section), recent)
        for section in sections
        if (
            recent := sorted(
                (e for e in section["entries"] if slides.is_recent(e, today)),
                key=lambda e: e["added"],
                reverse=True,
            )
        )
    ]
    if not groups:
        return []

    lines = [f"## {strings['latest_heading']}", "", strings["latest_intro"], ""]
    for name, entries in groups:
        lines.append(f"**{name}**")
        lines += [
            strings["entry"].format(
                title=escape(entry["title"]),
                url=entry["url"],
                author=entry["author"] or strings["unknown_author"],
                ym=entry["date"][:7] if entry["date"] else strings["unknown_date"],
            )
            for entry in entries
        ]
        lines.append("")
    lines.append(strings["latest_updated"].format(date=today.isoformat()))
    lines.append("")
    return lines


def _plugin(strings: dict[str, str], total: int) -> list[str]:
    """Return the section describing the Claude Code plugin."""
    return [
        f"## {strings['plugin_heading']}",
        "",
        strings["plugin_intro"].format(total=total),
        "",
        "```",
        f"/plugin marketplace add {REPO_SLUG}",
        "/plugin install awesome-japanese-nlp-slides@awesome-japanese-nlp-slides",
        "```",
        "",
        strings["plugin_usage"],
        "",
        "```",
        *(
            f"/awesome-japanese-nlp-slides:search {q}"
            for q in strings["search_examples"]
        ),
        "```",
        "",
        "> [!TIP]",
        *(f"> {line}" for line in strings["plugin_tip"]),
        "",
        *_plugin_article(strings),
    ]


def _plugin_article(strings: dict[str, str]) -> list[str]:
    """Return the further-reading link to the Zenn article, if the locale has one."""
    if not strings.get("plugin_article"):
        return []
    link = f"[{escape(ZENN_ARTICLE_TITLE)}]({ZENN_ARTICLE_URL})"
    return [strings["plugin_article"].format(link=link), ""]


def _articles_pointer(
    strings: dict[str, str], locale: Locale, total_articles: int
) -> list[str]:
    """Return the one-line pointer to this locale's companion articles doc.

    Skipped for a locale with no ``articles`` block (or when there is
    nothing to point to yet), and skipped when the locale's strings have no
    ``articles_pointer`` key, so both are opt-in per language.
    """
    has_pointer = "articles" in locale and "articles_pointer" in strings
    if not total_articles or not has_pointer:
        return []
    link = f"{BLOB_URL}/{locale['articles']['outputs'][-1]}"
    return [strings["articles_pointer"].format(link=link, total=total_articles), ""]


def _body(
    strings: dict[str, str], sections: list[Section], name_of: Any, blurb_of: Any
) -> list[str]:
    """Return the table of contents followed by one block per section."""
    lines = [f"## {strings['toc_heading']}", ""]
    lines += [f"- [{name_of(s)}](#{anchor(name_of(s))})" for s in sections]
    lines.append("")

    for section in sections:
        lines += [f"## {name_of(section)}", "", blurb_of(section), ""]
        newest_first = sorted(section["entries"], key=lambda e: e["date"], reverse=True)
        lines += [
            strings["entry"].format(
                title=escape(entry["title"]),
                url=entry["url"],
                author=entry["author"] or strings["unknown_author"],
                ym=entry["date"][:7] if entry["date"] else strings["unknown_date"],
            )
            for entry in newest_first
        ]
        lines.append("")
    return lines


def render(locale: Locale, sections: list[Section], depth: int, run: RunInfo) -> str:
    """Return the README text for one language.

    ``depth`` is how deep the output file sits, used to adjust the relative
    link to the logo. ``run`` carries the values shared by every output file
    of this run: the language switcher, today's date (which decides which
    entries are recent enough for the "latest additions" section), and the
    size of the companion articles list (0 skips the pointer to it).
    """
    strings = locale["strings"]
    translations = locale.get("sections", {})
    total = slides.count(sections)

    def name_of(section: Section) -> str:
        name = section["section"]
        return translations.get(name, {}).get("section", name)

    def blurb_of(section: Section) -> str:
        return translations.get(section["section"], {}).get("blurb", section["blurb"])

    lines = [
        *_intro(strings, run.nav, total, len(sections), depth),
        *_plugin(strings, total),
        *_articles_pointer(strings, locale, run.total_articles),
        *_latest_additions(strings, sections, name_of, run.today),
        *_body(strings, sections, name_of, blurb_of),
        f"## {strings['license_heading']}",
        "",
        f"[CC0 1.0 Universal]({LICENSE_URL})",
        "",
        "> [!NOTE]",
        f"> {strings['license_note']}",
    ]
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    sections = slides.load()
    total_articles = articles.count(articles.load()) if articles.SRC.exists() else 0
    locales = load_locales()
    run = RunInfo(
        nav=nav_line(locales), today=date.today(), total_articles=total_articles
    )

    for locale in locales:
        for relative in locale["outputs"]:
            out = ROOT / relative
            out.parent.mkdir(parents=True, exist_ok=True)
            # How many directories deep the file sits, for the logo's relative link.
            depth = len(Path(relative).parts) - 1
            body = render(locale, sections, depth, run)
            out.write_text(body, encoding="utf-8")
            print(f"wrote {relative}: {locale['lang']}, {len(body.splitlines())} lines")

    print(
        f"{slides.count(sections)} entries, {len(sections)} sections, "
        f"{len(locales)} locales"
    )


if __name__ == "__main__":
    main()
