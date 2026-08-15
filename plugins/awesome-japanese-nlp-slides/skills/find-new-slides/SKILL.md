---
description: Find Japanese NLP presentation slides on Speaker Deck / Docswell / SlideShare that are NOT yet in awesome-japanese-nlp-slides. Give it a topic and it searches the web, filters out everything already listed, and emits entries ready to paste into data/curated.json.
when_to_use: "Use only when the user explicitly wants to discover Japanese NLP slides that are NOT yet in awesome-japanese-nlp-slides, or to prepare a contribution to the list. Trigger phrases include 'リストに無い新しいスライド', 'awesome-japanese-nlp-slides に追加できそうな資料', '最近公開された日本語NLPのスライド', '〜の新しい発表資料を探して', 'curated.json に追加する候補', 'find unlisted Japanese NLP slides', 'new slides to contribute'. For searching what is already in the list, use the search skill instead."
argument-hint: [topic]
allowed-tools: Bash, WebSearch, WebFetch
---

Find Japanese NLP presentation slides about "$ARGUMENTS" that are not already in the awesome-japanese-nlp-slides list.

## Instructions

### Preamble — Establish the current date

Before anything else, run this once and remember the values — every step that mentions a year or today's date refers to them:

```bash
echo "TODAY=$(date +%F)"
echo "YEAR_NOW=$(date +%Y)"
echo "YEAR_PREV=$(($(date +%Y) - 1))"
```

Substitute these wherever this skill writes `${YEAR_NOW}` or `${YEAR_PREV}`. **Do not hardcode years** — the value of this list is that it stays current.

### Step 0 — Handle empty input

If `$ARGUMENTS` is empty or blank, treat it as a **sweep for the most recent Japanese NLP slides across every topic**:

- **Topic label** for the output heading: "最近公開された日本語NLPスライド" (Japanese) / "Recent Japanese NLP slides" (English)
- **Search queries for Step 4**: drop the topic term and lean entirely on recency —
  - `自然言語処理 発表資料 ${YEAR_NOW} site:speakerdeck.com`
  - `LLM 勉強会 資料 ${YEAR_NOW} site:speakerdeck.com`
  - `日本語 LLM スライド ${YEAR_NOW}`
  - `NLP 論文読み会 資料 ${YEAR_NOW} site:speakerdeck.com`
  - `言語処理学会 ${YEAR_NOW} 発表資料`
  - `自然言語処理 ${YEAR_NOW} site:docswell.com`
- **Target section**: none — assign each survivor its own section in Step 7.

Then continue from Step 1 with those defaults.

### Step 1 — Interpret the topic and pick the target section

The user's topic is: "$ARGUMENTS"

The material is **Japanese slide decks**, so the search queries have to be **Japanese**. An English-only query set finds almost nothing: the titles, the slide hosts' metadata and the surrounding blog posts are all Japanese. Translate the topic into the Japanese term first, then optionally add one English query.

The table below is the list's own 32 sections. Use it twice: pick the search phrases here in Step 1, and reuse the same row's cues to assign a section in Step 7. Pick **1–3 rows** — the one the topic names plus any obvious neighbour.

| Section (use this exact name in the output) | Japanese search phrases | Assignment cues |
|---|---|---|
| 入門・全体像 | `自然言語処理 入門`, `NLP 全体像`, `ざっくり わかる 自然言語処理` | overview, 入門, ざっくり, 全体像, no single technique |
| 学会チュートリアル | `言語処理学会 チュートリアル`, `NLP チュートリアル 資料`, `NLP${YEAR_NOW} チュートリアル` | NLP20xx / 言語処理学会 / ACL / EMNLP tutorial slot |
| 大学講義・体系的な講義資料 | `自然言語処理 講義資料`, `大学 講義 自然言語処理`, `授業資料 NLP` | 講義, 授業, 第N回, 全N回, a university course |
| 日本語の基礎解析（形態素解析・構文解析） | `形態素解析 資料`, `係り受け解析 スライド`, `構文解析 発表` | 形態素, 係り受け, 構文解析, MeCab/Sudachi/JUMAN/KWJA |
| NLP ライブラリ・ツール開発 | `形態素解析器 自作`, `NLP ライブラリ 開発 資料`, `Rust 形態素解析` | 自作した, 実装, 高速化, OSS library internals |
| 日本語テキストの正規化・表記ゆれ | `表記ゆれ 正規化 資料`, `日本語 正規化 スライド`, `住所 正規化` | 正規化, 表記ゆれ, 誤字, 住所, NEologdn |
| 辞書・かな漢字変換・日本語入力 | `かな漢字変換 資料`, `日本語入力 スライド`, `IME 開発 発表` | IME, かな漢字変換, SKK, Mozc, 辞書構築, 換言 |
| 単語・文の分散表現 | `分散表現 資料`, `文埋め込み スライド`, `word2vec 発表` | 分散表現, 埋め込み, ベクトル, word2vec/SBERT |
| 事前学習モデル・Transformer | `BERT 解説 資料`, `Transformer 論文読み`, `事前学習モデル スライド` | BERT, Transformer, attention 機構, 事前学習モデルの解説 |
| 大規模言語モデル（概論・動向） | `大規模言語モデル 解説`, `LLM 概論 資料`, `LLM 動向 ${YEAR_NOW}` | LLM の概観・動向・サーベイ、特定の開発事例ではない |
| 日本語LLMの開発（事前学習・コーパス構築） | `日本語LLM 事前学習 資料`, `LLM コーパス 構築 発表`, `Swallow 開発` | 事前学習を回した話, コーパス構築, Swallow/LLM-jp/PLaMo |
| ファインチューニング・事後学習 | `ファインチューニング 資料`, `事後学習 スライド`, `LoRA 発表` | SFT, RLHF, DPO, LoRA, 蒸留, 指示チューニング |
| LLM の推論最適化・サービング | `LLM 推論 高速化 資料`, `vLLM 発表`, `量子化 スライド` | 推論高速化, 量子化, サービング, vLLM, GPU |
| 評価・ベンチマーク | `LLM 評価 資料`, `ベンチマーク 発表`, `llm-jp-eval スライド` | 評価, ベンチマーク, リーダーボード, JGLUE/Nejumi |
| 全文検索・検索基盤 | `全文検索 資料`, `検索基盤 スライド`, `Elasticsearch 発表` | 全文検索エンジン, 検索基盤, ランキング, Solr/Lucene/Vespa |
| 検索・RAG | `RAG 資料`, `検索拡張生成 スライド`, `チャンキング 発表` | RAG, リトリーバル, リランカー, チャンク分割 |
| LLM アプリケーション開発・運用 | `LLM アプリ 開発 資料`, `LLMOps スライド`, `プロンプト 設計 発表` | プロダクト投入, 運用, LLMOps, プロンプト設計 |
| AI エージェント・MCP | `AI エージェント 資料`, `MCP 解説 スライド`, `マルチエージェント 発表` | エージェント, MCP, LangGraph, 自律, ツール利用 |
| LLM の安全性・セキュリティ | `プロンプトインジェクション 資料`, `LLM セキュリティ スライド`, `AI 安全性 発表` | 安全性, セキュリティ, 脆弱性, 攻撃と防御, ガードレール |
| テキスト分類・感情分析 | `感情分析 資料`, `テキスト分類 スライド`, `評判分析 発表` | 分類, 感情, 極性, 評判, fastText |
| スパム・有害コンテンツ対策 | `スパム対策 資料`, `違反検知 スライド`, `有害コンテンツ 発表` | スパム, 荒らし, 違反投稿, 不適切検知, フェイク |
| テキストマイニング・トピックモデル | `テキストマイニング 資料`, `トピックモデル スライド`, `KH Coder 発表` | テキストマイニング, LDA, トピックモデル, 計算社会科学 |
| 情報抽出・固有表現・アノテーション | `固有表現抽出 資料`, `情報抽出 スライド`, `アノテーション 発表` | NER, 情報抽出, 関係抽出, アノテーション設計 |
| 文書処理・OCR | `OCR 資料`, `帳票 読み取り スライド`, `文書画像 発表` | OCR, 帳票, 請求書, 契約書, 文書画像 |
| 質問応答・知識 | `質問応答 資料`, `知識グラフ スライド`, `QA システム 発表` | 質問応答, QA, 知識グラフ, ナレッジベース |
| 機械翻訳 | `機械翻訳 資料`, `同時通訳 スライド`, `翻訳モデル 発表` | 機械翻訳, NMT, 同時通訳, 対訳 |
| マルチモーダル・Vision-and-Language | `Vision and Language 資料`, `マルチモーダル スライド`, `VLM 発表` | 画像 × 言語, VLM, CLIP, VQA, 動画 |
| 音声認識・音声処理 | `音声認識 資料`, `文字起こし スライド`, `音声合成 発表` | ASR, TTS, Whisper, ESPnet, 話者分離 |
| 対話システム・音声対話 | `対話システム 資料`, `音声対話 スライド`, `チャットボット 発表` | 対話システム, ボイスボット, 音声対話, コールセンター |
| 生成・要約・校正 | `要約 資料`, `文法誤り訂正 スライド`, `校正 発表` | 要約, 生成, 校正, GEC, 見出し生成 |
| 解釈性・分析・言語学的視点 | `言語モデル 解釈性 資料`, `内部表現 分析 スライド`, `計量言語学 発表` | 解釈性, probing, 内部表現の分析, 言語学的考察 |
| 産業応用・実務事例 | `自然言語処理 事例 資料`, `LLM 導入 事例 スライド`, `NLP 業務 活用 発表` | 社内導入, 業務活用, 事例紹介, ビジネス成果 |

If the topic matches no row, translate it literally into Japanese and append `資料` / `スライド` / `発表` to build the queries, then assign the closest section in Step 7.

### Step 2 — Locate the existing data file

Same resolution as the `search` skill:

```bash
SLIDES_PATH="${CLAUDE_PLUGIN_ROOT}/data/slides.json"
[ -f "$SLIDES_PATH" ] || SLIDES_PATH="$(find "${HOME}/.claude/plugins" -type f -name slides.json 2>/dev/null | grep "awesome-japanese-nlp-slides/" | head -1)"
echo "SLIDES_PATH=$SLIDES_PATH"
```

### Step 3 — Build the existing-URL set

The plugin's `slides.json` is generated from `data/curated.json`, so an installed copy can lag the repository by a few commits. When the run happens inside a checkout of the repo, merge `curated.json` in as well so freshly added decks are not reported as new.

```bash
EXISTING_URLS_FILE=$(mktemp -t awesome_ja_nlp_slides_urls.XXXXXX)
```

```python
python3 << 'EOF'
import json
import os
import re

SLIDES_PATH = "SLIDES_PATH"           # from Step 2
OUTPUT_PATH = "EXISTING_URLS_FILE"    # from the mktemp above


def canon(url):
    """Normalise a slide URL the way Step 5 compares them."""
    url = (url or "").strip().lower()
    url = url.split("?")[0].split("#")[0].rstrip("/")
    url = re.sub(r"^http://", "https://", url)
    url = re.sub(r"^https://www\.speakerdeck\.com", "https://speakerdeck.com", url)
    url = re.sub(r"^https://(docswell|slideshare)\.", r"https://www.\1.", url)
    return url


urls = set()
with open(SLIDES_PATH) as f:
    for item in json.load(f):
        urls.add(canon(item["u"]))
count_plugin = len(urls)

# Walk up looking for the repo's data/curated.json (present only in a checkout).
path = os.path.abspath(os.path.dirname(SLIDES_PATH))
for _ in range(6):
    path = os.path.dirname(path)
    curated = os.path.join(path, "data", "curated.json")
    if os.path.exists(curated):
        with open(curated) as f:
            for section in json.load(f):
                for entry in section["entries"]:
                    urls.add(canon(entry["url"]))
        print(f"Supplemented {len(urls) - count_plugin} URLs from {curated}")
        break

with open(OUTPUT_PATH, "w") as f:
    f.write("\n".join(sorted(urls)))
print(f"Loaded {len(urls)} existing slide URLs ({count_plugin} from the plugin) -> {OUTPUT_PATH}")
EOF
```

Clean the temp file up when the skill finishes (`rm -f "$EXISTING_URLS_FILE"`).

### Step 4 — Discover candidates via WebSearch

Run **6–9 WebSearch queries** built from the phrases picked in Step 1. Rules:

1. **At least two thirds of the queries must be Japanese.** This is the single biggest factor in whether anything is found.
2. **Cover all three hosts, one `site:` per query.** Speaker Deck holds most of the list, but Docswell and SlideShare are where a lot of corporate and academic material lives.
   - `<japanese-phrase> site:speakerdeck.com`
   - `<japanese-phrase> site:docswell.com`
   - `<japanese-phrase> site:slideshare.net`

   Never OR the hosts into one query (`... docswell OR speakerdeck OR slideshare`). Without the `site:`
   operator the engine reads the host names as topic words and returns articles *about* slide-sharing
   services instead of slides. One host per query, `site:` every time.
3. **Add recency.** Two or three queries should carry `${YEAR_NOW}` or `${YEAR_PREV}` — the list is weakest at its recent edge.
4. **Search around the events too**, since slides are announced in wrap-up blog posts before search engines index the deck itself:
   - `<japanese-phrase> 勉強会 資料 ${YEAR_NOW}`
   - `<japanese-phrase> 登壇 資料`
   - `言語処理学会 ${YEAR_NOW} <japanese-phrase> 発表資料`
5. One English query is worth including for research-flavoured topics: `<english-keyword> japanese site:speakerdeck.com`.

**Keep a narrow topic undiluted — this is the rule that decides whether a rare topic finds anything.**
Padding a specific term with generic ones (`自然言語処理`, `NLP`, `LLM`, `資料`) lets the engine satisfy the
query on the padding alone and silently drop the term you care about. Measured on the same topic:

| Query | Result |
|---|---|
| `手話 自然言語処理 資料 site:speakerdeck.com` | ten popular general-NLP decks, **not one mentioning 手話** |
| `手話 site:speakerdeck.com` | decks that actually cover 手話 |

So for a narrow topic, query the **term by itself** plus `site:`, and only then widen. The tell that the term
was dropped is a result set whose titles do not contain it anywhere — when you see that, re-run with the bare
term before concluding anything. The generic phrases in the Step 1 table are for broad topics that need
narrowing, not for narrow ones that need protecting.

From every result — the result URLs *and* the URLs quoted inside wrap-up pages — extract anything matching a slide-deck shape:

| Host | Shape | `source` value |
|---|---|---|
| Speaker Deck | `https://speakerdeck.com/<user>/<slug>` | `speakerdeck` |
| Docswell | `https://www.docswell.com/s/<user>/<ID>-<slug>` | `docswell` |
| SlideShare | `https://www.slideshare.net/<user>/<slug>` or `https://www.slideshare.net/slideshow/<slug>/<id>` | `slideshare` |

Ignore user/profile pages (`https://speakerdeck.com/<user>` with no slug), player/embed URLs, PDF mirrors, YouTube, Qiita, Zenn and note.com — this list indexes slide decks on those three hosts only. Normalise each URL exactly as `canon()` in Step 3 does, and collect them into a candidate set tagged with its `source`.

### Step 5 — Filter against the existing list

Drop every candidate whose normalised URL appears in `$EXISTING_URLS_FILE`, then deduplicate the remainder.

Then **drop everything that is not actually about the topic.** This is the filter that matters most, because
of how the search engine behaves on a narrow term: asked for `手話 自然言語処理 資料 site:speakerdeck.com`
it quietly discards `手話` and returns ten popular general-NLP decks — real, well-known, genuinely
NLP-related, and none of them about sign language. Half of them were already in this list; the other half
would sail through every other check in this skill and be reported as "new 手話 slides".

So judge each candidate's title against the topic and drop the ones that only share the general field. A deck
earns its place by covering the topic, not by being a good deck.

Report the count you dropped as "already listed: N". If **everything** was dropped, the topic is already well
covered; if the survivors are all off-topic, the honest answer is that nothing was found. Say so in Step 8 —
a short "nothing found" is worth more than a list of decks the reader has to re-check by hand, and it is the
correct answer for a topic the Japanese NLP community has not presented on.

If more than 20 candidates survive, prioritise those that appeared in several result sets and those whose title clearly matches the topic.

### Step 6 — Enrich the candidates via WebFetch

`curated.json` requires five fields per entry and **rejects a missing or malformed one**, so every candidate has to be confirmed against its own page — never guess a date from a search snippet.

Cap at **10–15** candidates and issue up to **5 WebFetch calls in parallel** (one message, multiple tool calls):

```
WebFetch url="<candidate url>" prompt="Extract as JSON: title (the deck's title exactly as displayed, in its original language), author (the presenter's display name exactly as shown on the page), published_date in YYYY-MM-DD form, slide_count, and topic_summary (one sentence, English). Also return is_nlp_related: true only if the deck is about natural language processing, LLMs, speech/text processing or search. If any field is unavailable, set it to null."
```

Then drop a candidate when:

- the page 404s, redirects to a profile, or is private;
- `is_nlp_related` is false — a keyword can match a deck that only mentions NLP in passing;
- `topic_summary` shows the deck is not really about the topic, even though the title looked close. This is
  the second chance to catch what Step 5 is guarding against: `is_nlp_related` is true for most of this
  list, so it is nearly useless as a relevance test on its own;
- the deck is **not in Japanese and not from the Japanese-speaking community**. The list's scope is NLP/LLM material presented to a Japanese audience: a general LLM survey given in Japanese belongs, an English-only deck by an unrelated author does not;
- `published_date` is null. Put these in the "要確認" bucket in Step 8 instead of discarding them silently — the date usually just needs a human to look at the page.

Normalise the two fields that `scripts/slides.py` cleans up on load, so the output can be pasted verbatim:

- **title** — collapse runs of whitespace, and strip a trailing `.pdf` / `.pptx` / `.key` if the presenter left one in.
- **author** — the platform display name as-is (`Preferred Networks`, `Naoaki Okazaki`, `himkt`). Do not romanise it, translate it, or replace it with an account ID.
- **date** — `YYYY-MM-DD`, the date the deck was published, not the date of the event.

### Step 7 — Assign a section

Give every survivor exactly one of the **32 section names** from the Step 1 table, using that row's cues. Rules:

- The name must match `curated.json` **character for character** — the generators key their translations off it, and a typo silently creates a duplicate section.
- Prefer the specific section over the generic one: a deck about running a pretraining job goes to 日本語LLMの開発（事前学習・コーパス構築）, not 大規模言語モデル（概論・動向）.
- A company case study whose substance is one technique goes to that technique's section; 産業応用・実務事例 is for decks whose subject *is* the rollout.
- A university lecture series goes to 大学講義・体系的な講義資料 whatever it covers.

### Step 8 — Output

**Language detection:** if `$ARGUMENTS` contains any Japanese character, or is empty, write the prose in **Japanese**; otherwise in **English**. Titles, author names and section names are always quoted exactly as stored — never translated.

Lead with the paste-ready JSON, grouped by section. These are **entry objects to append to the `entries` array of an existing section** in `data/curated.json` — not new section objects.

````
## "$ARGUMENTS" の追加候補

未収録のスライド **N 件** を見つけました（検索した候補 M 件のうち、収録済み K 件を除外）。

*(検索クエリ: query1, query2, ...)*

### `検索・RAG` に追加

```json
{
  "title": "スライドのタイトル",
  "url": "https://speakerdeck.com/user/slug",
  "author": "発表者名",
  "date": "2025-06-14",
  "source": "speakerdeck"
},
```

- [スライドのタイトル](https://speakerdeck.com/user/slug) — 発表者名（2025-06）・全 42 枚 / どんな内容かの一文

### `評価・ベンチマーク` に追加

...

---

### 要確認（公開日が取得できなかったもの）

- [タイトル](url) — 発表者名 / ページを開いて公開日を確認してください

### 反映手順

1. 上の JSON を `data/curated.json` の該当セクションの `entries` に貼り付ける
2. `python3 scripts/slides.py` で検証する
3. `python3 scripts/generate_readme.py` と `python3 scripts/build_plugin_data.py` を実行する
````

**Rules for the output:**

- The JSON block is the deliverable — keep the five keys in the order `title`, `url`, `author`, `date`, `source` to match the file, and leave the trailing comma so the block splices into an existing array.
- The bullet under each JSON block is for the human reading the result: presenter, `YYYY-MM`, slide count when known, and one sentence on the content **drawn from the WebFetch summary**. Never invent a description you did not read.
- Order the entries within a section newest first, matching how `curated.json` is kept.
- Do not print the "要確認" block or the "反映手順" block when they are empty.
- If nothing survived, say so and offer next moves:

  ```
  ## "$ARGUMENTS" の追加候補

  未収録のスライドは見つかりませんでした（収録済み K 件を検索結果から除外）。

  - 別のキーワードで再試行: `<提案するクエリ>`
  - 収録済みの資料は `/awesome-japanese-nlp-slides:search $ARGUMENTS` で確認できます
  ```

### Step 9 — Sources

Append the `Sources:` section that WebSearch requires, listing the result URLs you actually used, then clean up: `rm -f "$EXISTING_URLS_FILE"`
