# scripts

The generation pipeline for the README files, the articles list, and the
plugin's search data.

`data/curated.json` is the single source of truth for the **slide decks**.
Both the README in every language and the search data bundled with the plugin
are generated from it, so **the only file you edit when adding a slide deck is
`data/curated.json`**. `data/articles.json` is the same idea for the companion
list of **web pages and blog posts** — see [Articles](#articles-blog-posts-and-web-pages)
below.

## Repository layout

```
.
├── README.md                     # generated, Japanese (never edit by hand)
├── _config.yml                   # GitHub Pages: the Jekyll theme of the site
├── docs/
│   ├── README.ja.md              # generated (same text as the root README.md)
│   ├── README.en.md              # generated, English
│   ├── README.zh-hant.md         # generated, traditional Chinese
│   ├── README.zh-hans.md         # generated, simplified Chinese
│   ├── ARTICLES.ja.md            # generated, the articles list (Japanese)
│   ├── ARTICLES.en.md            # generated, English
│   ├── ARTICLES.zh-hant.md       # generated, traditional Chinese
│   └── ARTICLES.zh-hans.md       # generated, simplified Chinese
├── images/
│   └── awesome-japanese-nlp-slides.png
├── data/
│   ├── curated.json              # ★ slide decks: the source of truth (the only file you edit)
│   ├── articles.json             # ★ web pages / blog posts: the source of truth
│   └── locales/                  # ★ per-language wording (add a file to add a language)
│       ├── ja.json
│       ├── en.json
│       ├── zh-hant.json
│       └── zh-hans.json
├── scripts/
│   ├── slides.py                    # loads and validates curated.json (shared module)
│   ├── articles.py                  # loads and validates articles.json (shared module)
│   ├── generate_readme.py           # curated.json + locales → the README of each language
│   ├── generate_articles_readme.py  # articles.json + locales → the articles list
│   └── build_plugin_data.py         # curated.json + articles.json → the plugin's slides.json / articles.json
└── plugins/awesome-japanese-nlp-slides/
    ├── .claude-plugin/plugin.json
    ├── data/
    │   ├── slides.json           # generated (shipped inside the plugin)
    │   └── articles.json         # generated (shipped inside the plugin)
    └── skills/
        ├── search/SKILL.md           # search slides + articles; falls back to the web when it misses
        └── find-new-slides/SKILL.md  # find decks the list does not have yet
```

The material itself — title, URL, presenter, date — is the same in every
language, and `curated.json` (or `articles.json`) is its only source. Only
section names, blurbs and the boilerplate around them need translating, which
is why those live in `data/locales/`. Both lists share the same 32 section
names, so a section's translated name is written once and reused by both.

## Running

Edit `data/curated.json`, then run these to refresh the slide list and the
plugin's search data.

```bash
python3 scripts/generate_readme.py      # README.md, docs/README.*.md
python3 scripts/build_plugin_data.py    # plugins/.../data/slides.json + articles.json
```

Edit `data/articles.json`, then run these to refresh the articles list and the
plugin's search data.

```bash
python3 scripts/generate_articles_readme.py   # docs/ARTICLES.*.md
python3 scripts/build_plugin_data.py          # plugins/.../data/slides.json + articles.json
```

`generate_readme.py` also links to the articles list (the "🌐" line near the
top of the README), so re-run it after changing `articles.json` too if you
want that entry count to catch up.

`build_plugin_data.py` writes both `plugins/.../data/slides.json` and
`plugins/.../data/articles.json` in one run regardless of which of the two
source files changed — it is cheap to run after either edit, and the
plugin's `search` skill reads both files together (see below), so it is
easiest to just always run it after touching either `curated.json` or
`articles.json`.

To validate without generating anything, run the shared modules directly.

```bash
python3 scripts/slides.py               # ok: 604 entries in 32 sections
python3 scripts/articles.py             # ok: 64 entries in 32 sections
```

There are no dependencies — the Python 3 standard library is enough (3.9 or
later).

## Adding and removing material

Edit the `entries` of the relevant section in `data/curated.json` and run the
two commands above. That refreshes both the README in every language and the
plugin's search data.

```json
[
  {
    "section": "検索・RAG",
    "blurb": "The single sentence that opens the section.",
    "entries": [
      {
        "title": "大規模言語モデル時代の機械翻訳の展望",
        "url": "https://speakerdeck.com/example/slide",
        "author": "発表者名",
        "date": "2024-11-08",
        "source": "speakerdeck",
        "added": "2024-11-08"
      }
    ]
  }
]
```

- All five fields (`title`, `url`, `author`, `date`, `source`) are required.
- `date` is `YYYY-MM-DD`. The README rounds it to `YYYY-MM` for display.
- `source` is one of `speakerdeck`, `docswell` or `slideshare`.
- `added` is optional: the `YYYY-MM-DD` date the entry was added to this list
  (not the deck's own `date`). Set it and the entry shows up in the README's
  "🎉 The latest additions" section for 7 days from that date, then drops out
  on its own — nothing to clean up later. Leave it out and the entry is never
  featured there, which is also what a pre-existing entry does implicitly.
- The order of `entries` is free: the README lists each section newest first.
  Keeping the file in that order too makes diffs easier to read.

### Finding material to add

The plugin's `find-new-slides` skill does the legwork: give it a topic and it
searches Speaker Deck, Docswell and SlideShare, drops everything already in the
list, confirms each deck's title, presenter and publication date against its own
page, and prints entry objects in exactly the shape above, grouped by the
section they belong in.

```
/awesome-japanese-nlp-slides:find-new-slides RAG
/awesome-japanese-nlp-slides:find-new-slides 音声認識
/awesome-japanese-nlp-slides:find-new-slides            # no topic: whatever is newest
```

Paste the blocks it emits into the matching sections of `curated.json`, then run
the two commands above. Its output is a starting point, not a merge — read each
deck before you commit it.

Both scripts validate the file through `scripts/slides.py` before writing
anything. A missing field, a malformed date, a duplicate URL or a duplicate
section name stops the run with the offending location, exit status 1, and the
generated files untouched.

```
$ python3 scripts/generate_readme.py
data/curated.json has 2 problem(s):
  [13] 検索・RAG entries[0] 大規模言語モデル時代の機械翻訳の展望: date is empty
  [13] 検索・RAG entries[3] RAG の実践: duplicate URL, already used by [2] 大学講義... entries[1]
```

## GitHub Pages

The site is served from the **root of `main`**, and `_config.yml` sets
`jekyll-theme-cayman` as its theme. There is no landing page to maintain:
`jekyll-readme-index` — one of the plugins GitHub Pages enables by default and
cannot disable — publishes `README.md` as the index of a site that has no index
file of its own. The site is therefore whatever `generate_readme.py` last
wrote, with no extra output and no extra step.

Serving from the root also keeps `images/` inside the site, so the relative
link to the logo resolves from the repository, from `docs/`, and from the
published site alike.

## Adding and reordering sections

The order of the array in `curated.json` is the order of the table of contents
and of the sections in the README. After adding a section, add its translation
to `sections` in each `data/locales/*.json` — an untranslated section is
emitted in Japanese.

## Articles (blog posts and web pages)

`data/articles.json` is the same shape as `curated.json` — a list of the same
32 sections, each with a `blurb` and `entries` — except an entry has no
`source` field (articles aren't confined to three known platforms the way
slides are):

```json
[
  {
    "section": "検索・RAG",
    "blurb": "The single sentence that opens the section.",
    "entries": [
      {
        "title": "RAGをゼロから実装して仕組みを学ぶ",
        "url": "https://example.com/blog/rag-from-scratch",
        "author": "著者名 or 企業名",
        "date": "2025-11-18",
        "added": "2025-11-20"
      }
    ]
  }
]
```

- `title`, `url`, `author` and `date` are required; `added` is optional and
  works exactly like it does in `curated.json` (see above) — it puts the entry
  in the "🎉 latest additions" section of the articles list for 7 days.
- The section names must match `curated.json` **character for character**.
  `generate_articles_readme.py` reuses the slide list's own translated section
  names from `data/locales/*.json`'s `sections` key, so a section gets its
  translated heading in the articles list for free — only the `blurb` in
  `articles.json` is specific to this list, and it is only ever authored in
  Japanese; other languages fall back to it, same as an untranslated slide
  section would.
- Because articles can come from anywhere, prefer a real company tech blog or
  an individual developer's own blog (Zenn, Qiita, note, hatenablog, a company
  `tech.*` subdomain, ...) over SEO/content-marketing pages — the bar is the
  same "would a Japanese NLP engineer actually want to read this" judgment
  used for slides.
- Each language's `data/locales/*.json` needs its own `articles` block (with
  `outputs` and its own `strings`) for `generate_articles_readme.py` to write
  that language's file — see `ja.json` for a filled-in example. A locale
  without one is simply skipped by the articles generator (the slide README
  still gets generated normally).

## Adding a language

Drop one more JSON file into `data/locales/` and run `generate_readme.py` and
`generate_articles_readme.py`. No change to the scripts is needed. For
simplified Chinese, for example, you would add `data/locales/zh-hans.json`:

```json
{
  "lang": "zh-hans",
  "order": 3,
  "nav_label": "简体中文 (Chinese)",
  "outputs": ["docs/README.zh-hans.md"],
  "strings": { "...": "fill in every key found in en.json" },
  "sections": {
    "検索・RAG": { "section": "检索・RAG", "blurb": "..." }
  },
  "articles": {
    "outputs": ["docs/ARTICLES.zh-hans.md"],
    "strings": { "...": "fill in every key found in en.json's articles.strings" }
  }
}
```

- `order` — the position in the language switcher line.
- `outputs` — where to write. List several paths to emit the same text to each
  of them (Japanese goes to both the root `README.md` and `docs/README.ja.md`).
  The relative link to the logo gets its `../` prefixes from the depth of the
  output path.
- `strings` — the boilerplate of the README. Copy every key from `en.json` and
  translate it. `{total}` and `{sections}` are replaced with the number of
  decks and of categories. `titles_note` — the remark that titles are kept in
  their original language — is optional; omit the key and the line is skipped.
  `articles_pointer` is optional too: omit it and the README simply has no
  link to the articles list in that language.
- `sections` — **keyed by the Japanese section name**, with the translated
  `section` and `blurb`. The key must match the section name in `curated.json`
  exactly. Sections that do not match, or that are missing, are emitted in
  Japanese. Reused as-is by the articles list for its section headings.
- `articles` — optional; add it once the language should also get an articles
  list. `outputs` and `strings` work exactly like the top-level keys above,
  just for `docs/ARTICLES.<lang>.md` instead of the README.

## Linting

The scripts are kept clean under [ruff](https://docs.astral.sh/ruff/). There is
no config file in the repository; run it with the rule set below.

```bash
uvx ruff check scripts/ --select E,W,F,I,UP,B,SIM,C4,RET,ARG,PTH,N,PL,TRY,EM,EXE,RUF --target-version py39
uvx ruff format --check scripts/ --target-version py39
```

The scripts carry no shebang line: they are always run as
`python3 scripts/<name>.py`, which never consults one.
