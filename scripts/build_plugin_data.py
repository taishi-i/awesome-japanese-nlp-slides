"""Generate the search data bundled with the plugin from ``data/curated.json``.

The plugin is distributed with git-subdir, so only what lives under
plugins/awesome-japanese-nlp-slides/ ships to users. The search data is
therefore written into the plugin rather than referenced from data/.

Input:  data/curated.json
Output: plugins/awesome-japanese-nlp-slides/data/slides.json
"""

from __future__ import annotations

import json

import slides
from slides import ROOT

OUT = ROOT / "plugins" / "awesome-japanese-nlp-slides" / "data" / "slides.json"


def main() -> None:
    sections = slides.load()

    # Keys are single letters: the whole file is read into the model's context
    # every time the search skill runs.
    records = [
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

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(records, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )
    print(
        f"wrote {OUT.relative_to(ROOT)}: {len(records)} slides, "
        f"{len(sections)} sections"
    )


if __name__ == "__main__":
    main()
