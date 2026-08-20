"""Generate the articles list for every language from ``data/articles.json``.

This is the companion to ``generate_readme.py``: it produces the same kind of
document, but for web pages and blog posts instead of slide decks. It shares
the section names and their translations with the slide list — see
``data/locales/*.json``'s ``sections`` key — and each locale's own
``articles.strings`` for the boilerplate specific to this document.

Input:  data/articles.json, data/locales/*.json
Output: the files listed under each locale's ``articles.outputs``
        (docs/ARTICLES.ja.md, docs/ARTICLES.en.md, ...)
"""

from __future__ import annotations

from datetime import date
from typing import Any

import articles
import generate_readme as slides_readme
from articles import Section
from generate_readme import BLOB_URL, anchor, escape, load_locales

Locale = dict[str, Any]


def nav_line(locales: list[Locale]) -> str:
    """Return the language switcher for the articles doc, mirroring the slide list's."""
    return " | ".join(
        f"[{locale['nav_label']}]({BLOB_URL}/{locale['articles']['outputs'][-1]})"
        for locale in locales
        if "articles" in locale
    )


def _intro(strings: dict[str, str], nav: str, total: int, sections: int) -> list[str]:
    """Return the logo, badges, language switcher, backlink and opening notes."""
    main_readme = f"{BLOB_URL}/README.md"
    lines = [
        "# awesome-japanese-nlp-slides — Articles",
        "",
        f"![{strings['logo_alt']}]({'../'}images/awesome-japanese-nlp-slides.png)",
        "",
        nav,
        "",
        strings["back_to_main"].format(link=main_readme),
        "",
        *(line.format(link=main_readme) for line in strings["intro"]),
        "",
        strings["count"].format(total=total, sections=sections),
        "",
    ]
    if strings.get("titles_note"):
        lines += [strings["titles_note"], ""]
    return [*lines, "> [!NOTE]", f"> {strings['wip_note']}", ""]


def _latest_additions(
    strings: dict[str, str], sections: list[Section], name_of: Any, today: date
) -> list[str]:
    """Return the section listing articles added in the last 7 days, grouped by section.

    Empty when nothing qualifies, so a quiet week leaves no trace.
    """
    groups = [
        (name_of(section), recent)
        for section in sections
        if (
            recent := sorted(
                (e for e in section["entries"] if articles.is_recent(e, today)),
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


def render(locale: Locale, sections: list[Section], nav: str, today: date) -> str:
    """Return the articles doc text for one language."""
    strings = locale["articles"]["strings"]
    translations = locale.get("sections", {})
    total = articles.count(sections)

    def name_of(section: Section) -> str:
        name = section["section"]
        return translations.get(name, {}).get("section", name)

    # Article blurbs are only authored in Japanese (data/articles.json); other
    # locales fall back to it, same as an unmatched slide section would.
    def blurb_of(section: Section) -> str:
        return section["blurb"]

    lines = [
        *_intro(strings, nav, total, len(sections)),
        *_latest_additions(strings, sections, name_of, today),
        *_body(strings, sections, name_of, blurb_of),
        f"## {strings['license_heading']}",
        "",
        f"[CC0 1.0 Universal]({slides_readme.LICENSE_URL})",
        "",
        "> [!NOTE]",
        f"> {strings['license_note']}",
    ]
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    sections = articles.load()
    locales = load_locales()
    locales_with_articles = [locale for locale in locales if "articles" in locale]
    nav = nav_line(locales_with_articles)
    today = date.today()

    for locale in locales_with_articles:
        for relative in locale["articles"]["outputs"]:
            out = articles.ROOT / relative
            out.parent.mkdir(parents=True, exist_ok=True)
            body = render(locale, sections, nav, today)
            out.write_text(body, encoding="utf-8")
            print(f"wrote {relative}: {locale['lang']}, {len(body.splitlines())} lines")

    print(
        f"{articles.count(sections)} entries, {len(sections)} sections, "
        f"{len(locales_with_articles)} locales"
    )


if __name__ == "__main__":
    main()
