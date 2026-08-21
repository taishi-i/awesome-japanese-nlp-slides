"""Generate the search data bundled with the plugin.

The plugin is distributed with git-subdir, so only what lives under
plugins/awesome-japanese-nlp-slides/ ships to users. The search data is
therefore written into the plugin rather than referenced from data/.

Input:  data/curated.json, data/articles.json
Output: plugins/awesome-japanese-nlp-slides/data/slides.json
        plugins/awesome-japanese-nlp-slides/data/articles.json
"""

from __future__ import annotations

import json

import articles
import slides
from slides import ROOT

PLUGIN_DATA = ROOT / "plugins" / "awesome-japanese-nlp-slides" / "data"
SLIDES_OUT = PLUGIN_DATA / "slides.json"
ARTICLES_OUT = PLUGIN_DATA / "articles.json"


def _write(path, records, label) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}: {len(records)} {label}")


def main() -> None:
    sections = slides.load()

    # Keys are single letters: the whole file is read into the model's context
    # every time the search skill runs.
    slide_records = [
        {
            "t": entry["title"],
            "u": entry["url"],
            "a": entry["author"],
            "d": entry["date"],  # YYYY-MM-DD
            "s": section["section"],
            "src": entry["source"],  # speakerdeck / docswell / slideshare
        }
        for section in sections
        for entry in section["entries"]
    ]
    _write(SLIDES_OUT, slide_records, f"slides, {len(sections)} sections")

    article_sections = articles.load()
    article_records = [
        {
            "t": entry["title"],
            "u": entry["url"],
            "a": entry["author"],
            "d": entry["date"],  # YYYY-MM-DD
            "s": section["section"],
            # No ``src``: unlike slides, articles aren't confined to a
            # handful of known hosts, so there is no host field to carry.
        }
        for section in article_sections
        for entry in section["entries"]
    ]
    _write(ARTICLES_OUT, article_records, f"articles, {len(article_sections)} sections")


if __name__ == "__main__":
    main()
