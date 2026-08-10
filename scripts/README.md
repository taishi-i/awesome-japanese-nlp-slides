# scripts

The generation pipeline for the README files and the plugin's search data.

`data/curated.json` is the single source of truth of this repository. Both the
README in every language and the search data bundled with the plugin are
generated from it, so **the only file you edit when adding a slide deck is
`data/curated.json`**.

## Repository layout

```
.
├── README.md                     # generated, Japanese (never edit by hand)
├── docs/
│   ├── README.ja.md              # generated (same text as the root README.md)
│   └── README.en.md              # generated, English
├── images/
│   └── awesome-japanese-nlp-slides.png
├── data/
│   ├── curated.json              # ★ the single source of truth (the only file you edit)
│   └── locales/                  # ★ per-language wording (add a file to add a language)
│       ├── ja.json
│       └── en.json
├── scripts/
│   ├── slides.py                 # loads and validates curated.json (shared module)
│   ├── generate_readme.py        # curated.json + locales → the README of each language
│   └── build_plugin_data.py      # curated.json → the plugin's slides.json
└── plugins/awesome-japanese-nlp-slides/
    ├── .claude-plugin/plugin.json
    ├── data/slides.json          # generated (shipped inside the plugin)
    └── skills/search/SKILL.md
```

The material itself — title, URL, presenter, date — is the same in every
language, and `curated.json` is its only source. Only section names, blurbs and
the boilerplate around them need translating, which is why those live in
`data/locales/`.

## Running

Edit `data/curated.json`, then run these two commands to refresh everything.

```bash
python3 scripts/generate_readme.py      # README.md, docs/README.*.md
python3 scripts/build_plugin_data.py    # plugins/.../data/slides.json
```

To validate without generating anything, run the shared module directly.

```bash
python3 scripts/slides.py               # ok: 314 entries in 23 sections
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
        "source": "speakerdeck"
      }
    ]
  }
]
```

- All five fields are required.
- `date` is `YYYY-MM-DD`. The README rounds it to `YYYY-MM` for display.
- `source` is either `speakerdeck` or `docswell`.
- The order of `entries` is free: the README lists each section newest first.
  Keeping the file in that order too makes diffs easier to read.

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

## Adding and reordering sections

The order of the array in `curated.json` is the order of the table of contents
and of the sections in the README. After adding a section, add its translation
to `sections` in each `data/locales/*.json` — an untranslated section is
emitted in Japanese.

## Adding a language

Drop one more JSON file into `data/locales/` and run `generate_readme.py`. No
change to the scripts is needed. For simplified Chinese, for example, you would
add `data/locales/zh-hans.json`:

```json
{
  "lang": "zh-hans",
  "order": 3,
  "nav_label": "简体中文 (Chinese)",
  "outputs": ["docs/README.zh-hans.md"],
  "strings": { "...": "fill in every key found in en.json" },
  "sections": {
    "検索・RAG": { "section": "检索・RAG", "blurb": "..." }
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
- `sections` — **keyed by the Japanese section name**, with the translated
  `section` and `blurb`. The key must match the section name in `curated.json`
  exactly. Sections that do not match, or that are missing, are emitted in
  Japanese.

## Linting

The scripts are kept clean under [ruff](https://docs.astral.sh/ruff/). There is
no config file in the repository; run it with the rule set below.

```bash
uvx ruff check scripts/ --select E,W,F,I,UP,B,SIM,C4,RET,ARG,PTH,N,PL,TRY,EM,EXE,RUF --target-version py39
uvx ruff format --check scripts/ --target-version py39
```

The scripts carry no shebang line: they are always run as
`python3 scripts/<name>.py`, which never consults one.
