---
description: Search curated Japanese NLP presentation slides (Speaker Deck / Docswell / SlideShare) AND blog articles / web pages from awesome-japanese-nlp-slides. Accepts keywords or natural language questions in any language, and falls back to a web search when the list itself has nothing.
when_to_use: "Use whenever the user is looking for Japanese NLP material — slides, lecture materials, or blog articles / tech-blog posts: conference tutorials, university lectures, LLM development / pretraining, fine-tuning, evaluation and benchmarks, RAG and search, morphological analysis, embeddings, or industry case studies. Trigger phrases include '日本語LLMのスライド', '形態素解析の発表資料', 'RAG の講演資料', '〜の勉強に使える記事', 'チュートリアル資料が見たい', '〜についてのブログ記事', 'Japanese NLP slides', 'articles on Japanese LLM', 'blog posts about RAG', '日語 LLM 的投影片', '形態素分析的發表資料', '日语 LLM 的幻灯片', '日语自然语言处理的演讲资料'."
argument-hint: [query]
allowed-tools: Bash, WebSearch, WebFetch
---

Search the awesome-japanese-nlp-slides database (slides **and** articles) for: "$ARGUMENTS"

## Instructions

### Step 0 — Validate input

If `$ARGUMENTS` is empty or blank, **stop immediately** and output:

```
Usage: /awesome-japanese-nlp-slides:search <query>

Examples:
  /awesome-japanese-nlp-slides:search LLM pretraining
  /awesome-japanese-nlp-slides:search morphological analysis
  /awesome-japanese-nlp-slides:search RAG
  /awesome-japanese-nlp-slides:search evaluation benchmark
  /awesome-japanese-nlp-slides:search university lecture

Searches both slides and articles.

---

使い方: /awesome-japanese-nlp-slides:search <query>

クエリ例:
  /awesome-japanese-nlp-slides:search 日本語LLMの事前学習
  /awesome-japanese-nlp-slides:search 形態素解析
  /awesome-japanese-nlp-slides:search RAG
  /awesome-japanese-nlp-slides:search 評価 ベンチマーク
  /awesome-japanese-nlp-slides:search 大学講義

スライドと記事の両方を検索します。

---

用法: /awesome-japanese-nlp-slides:search <query>

查询示例 / 查詢範例:
  /awesome-japanese-nlp-slides:search 日语 LLM 的预训练
  /awesome-japanese-nlp-slides:search 形态素解析
  /awesome-japanese-nlp-slides:search RAG
  /awesome-japanese-nlp-slides:search 评测 基准测试
  /awesome-japanese-nlp-slides:search 大学课程

同时搜索幻灯片和文章 / 投影片與文章。
```

Do **not** proceed to Step 1 if `$ARGUMENTS` is empty.

### Step 1 — Interpret the query

The user's query is: "$ARGUMENTS"

The data (titles, section names, presenter/author names) is **mostly Japanese**, with English titles mixed in.
So build a keyword list that contains **both Japanese and English** terms — do not search with English alone.

**Keywords are always Japanese and English, whatever language the query is in.** A Chinese query has to
be translated into the Japanese term first before it can match anything: 预训练 → `事前学習`, 词向量 → `分散表現`,
问答 → `質問応答`, 语音识别 → `音声認識`, 检索增强生成 → `RAG`/`検索`. Never put a Chinese character form in
the keyword list: `形态素` matches nothing where `形態素` matches many entries, and neither `检索` nor `檢索`
matches anything against entries holding `検索`. Traditional forms occasionally coincide with the
Japanese spelling — translate rather than bet on the coincidence.

**Keyword rules:**
1. **Include the Japanese term and its English counterpart.** Substring match is used, so `形態素` catches 「形態素解析」「形態素解析器」, and `morpholog` catches "morphology"/"morphological".
2. **Add well-known tool / model names** when the query maps to a known domain — they often appear in titles.
3. **Aim for 4–8 keywords.** Fewer miss items; more inflates weak partial matches.

| Domain | Japanese keywords | English / tool names to add |
|---|---|---|
| 形態素解析・構文解析 | `形態素`, `係り受け`, `構文解析`, `解析器` | `morpholog`, `mecab`, `sudachi`, `juman`, `vibrato`, `kwja`, `ginza` |
| NLP ライブラリ・ツール開発 | `ライブラリ`, `実装`, `自作`, `高速化`, `辞書`, `トライ` | `library`, `oss`, `rust`, `vibrato`, `vaporetto`, `kagome`, `trie` |
| 辞書・かな漢字変換・日本語入力 | `かな漢字変換`, `日本語入力`, `辞書`, `換言` | `ime`, `mozc`, `skk`, `input method` |
| 分散表現・埋め込み | `分散表現`, `埋め込み`, `単語ベクトル` | `embed`, `vector`, `word2vec`, `chive`, `sbert` |
| 事前学習モデル・Transformer | `事前学習`, `言語モデル` | `bert`, `transformer`, `gpt`, `pretrain`, `huggingface` |
| LLM 開発・事前学習 | `事前学習`, `コーパス`, `構築`, `開発` | `llm`, `swallow`, `llm-jp`, `sarashina`, `plamo` |
| ファインチューニング・事後学習 | `ファインチューニング`, `事後学習`, `指示`, `蒸留` | `fine-tun`, `sft`, `rlhf`, `dpo`, `lora`, `peft` |
| 評価・ベンチマーク | `評価`, `ベンチマーク` | `eval`, `benchmark`, `jglue`, `llm-jp-eval`, `nejumi` |
| 全文検索・検索基盤 | `検索`, `全文検索`, `検索基盤`, `ランキング` | `search`, `elasticsearch`, `solr`, `lucene`, `rerank` |
| 検索・RAG | `検索拡張`, `情報検索`, `チャンキング` | `rag`, `retriev`, `embedding`, `ruri`, `graphrag` |
| LLM アプリ開発・運用 | `アプリ`, `運用`, `プロダクト`, `エージェント` | `agent`, `llmops`, `prompt`, `production` |
| AI エージェント・MCP | `エージェント`, `マルチエージェント`, `自律` | `agent`, `mcp`, `langchain`, `langgraph`, `react` |
| LLM の安全性・セキュリティ | `安全性`, `セキュリティ`, `脆弱性`, `防御`, `プロンプトインジェクション` | `safety`, `security`, `injection`, `guardrail`, `alignment` |
| 推論最適化・サービング | `推論`, `高速化`, `量子化`, `蒸留` | `infer`, `vllm`, `quantiz`, `distill`, `serving` |
| 正規化・表記ゆれ | `正規化`, `表記ゆれ`, `誤字`, `住所` | `normaliz`, `variant`, `typo` |
| 情報抽出・固有表現 | `固有表現`, `情報抽出`, `アノテーション` | `ner`, `entit`, `extract`, `annotat` |
| 文書処理・OCR | `文書`, `帳票`, `契約書`, `請求書` | `ocr`, `document`, `vlm`, `invoice` |
| 質問応答・知識 | `質問応答`, `知識` | `qa`, `question`, `knowledge` |
| 機械翻訳 | `翻訳`, `同時通訳` | `translat`, `nmt`, `mt` |
| テキスト分類・感情分析 | `分類`, `感情`, `評判`, `極性`, `検知` | `classif`, `sentiment`, `polarity`, `moderation`, `fasttext` |
| スパム・有害コンテンツ対策 | `スパム`, `有害`, `不適切`, `違反`, `監視`, `フェイク` | `spam`, `abuse`, `moderation`, `toxic`, `fake` |
| テキストマイニング・トピックモデル | `テキストマイニング`, `トピックモデル`, `可視化`, `計算社会科学` | `topic`, `lda`, `kh coder`, `wordcloud` |
| マルチモーダル・V&L | `マルチモーダル`, `画像`, `視覚`, `文書画像` | `vlm`, `vision`, `multimodal`, `vqa`, `clip` |
| 音声認識・音声処理 | `音声`, `音声認識`, `文字起こし`, `音声合成` | `speech`, `asr`, `tts`, `whisper`, `espnet` |
| 対話システム・音声対話 | `対話`, `音声対話`, `ボイスボット`, `チャットボット` | `dialog`, `spoken`, `voicebot`, `chatbot` |
| 生成・要約・校正 | `生成`, `要約`, `校正`, `文法誤り` | `generat`, `summar`, `correct`, `gec` |
| 解釈性・分析 | `解釈`, `分析`, `内部`, `言語学` | `interpret`, `analys`, `probing`, `attention` |
| 入門・チュートリアル | `入門`, `基礎`, `チュートリアル`, `講義` | `introduc`, `tutorial`, `lecture`, `basic` |
| 産業応用・事例 | `事例`, `実務`, `活用`, `導入` | `case`, `industr`, `production` |

**Section filter:** if the query clearly names a category, also note the matching section name so you can prefer it in Step 4. The 32 sections (shared by slides and articles) are:
入門・全体像 / 学会チュートリアル / 大学講義・体系的な講義資料 / 日本語の基礎解析（形態素解析・構文解析） / NLP ライブラリ・ツール開発 / 日本語テキストの正規化・表記ゆれ / 辞書・かな漢字変換・日本語入力 / 単語・文の分散表現 / 事前学習モデル・Transformer / 大規模言語モデル（概論・動向） / 日本語LLMの開発（事前学習・コーパス構築） / ファインチューニング・事後学習 / LLM の推論最適化・サービング / 評価・ベンチマーク / 全文検索・検索基盤 / 検索・RAG / LLM アプリケーション開発・運用 / AI エージェント・MCP / LLM の安全性・セキュリティ / テキスト分類・感情分析 / スパム・有害コンテンツ対策 / テキストマイニング・トピックモデル / 情報抽出・固有表現・アノテーション / 文書処理・OCR / 質問応答・知識 / 機械翻訳 / マルチモーダル・Vision-and-Language / 音声認識・音声処理 / 対話システム・音声対話 / 生成・要約・校正 / 解釈性・分析・言語学的視点 / 産業応用・実務事例

### Step 2 — Locate the data files

Both data files ship with the plugin. Resolve their paths via `${CLAUDE_PLUGIN_ROOT}` (Claude Code substitutes this inline in skill content), falling back to a scoped search only if the install is unusual:

```bash
SLIDES_PATH="${CLAUDE_PLUGIN_ROOT}/data/slides.json"
[ -f "$SLIDES_PATH" ] || SLIDES_PATH="$(find "${HOME}/.claude/plugins" -type f -name slides.json 2>/dev/null | grep "awesome-japanese-nlp-slides/" | head -1)"
echo "SLIDES_PATH=$SLIDES_PATH"

ARTICLES_PATH="${CLAUDE_PLUGIN_ROOT}/data/articles.json"
[ -f "$ARTICLES_PATH" ] || ARTICLES_PATH="$(find "${HOME}/.claude/plugins" -type f -name articles.json 2>/dev/null | grep "awesome-japanese-nlp-slides/" | head -1)"
echo "ARTICLES_PATH=$ARTICLES_PATH"
```

If `ARTICLES_PATH` resolves to nothing (an older install of the plugin, from before the articles list existed), proceed with slides only — do not fail the whole search over it. Use the resulting absolute paths in Step 3.

### Step 3 — Search and score via Bash

**Do NOT use the Read tool** on the data files — it would consume tens of thousands of tokens unnecessarily. Run the scoring in a single Bash call.

Each item in `slides.json` has:
- `t`: slide title
- `u`: Speaker Deck / Docswell / SlideShare URL
- `a`: author (presenter)
- `d`: publication date (`YYYY-MM-DD`)
- `s`: section name
- `src`: `speakerdeck`, `docswell` or `slideshare`

Each item in `articles.json` has the same shape **minus `src`** — articles are blog posts / web pages, not confined to a handful of known hosts:
- `t`: article title
- `u`: URL
- `a`: author
- `d`: publication date (`YYYY-MM-DD`)
- `s`: section name

Matching relies on the **title and section name only** (plus author, weighted lower), so cast a slightly wide keyword net.

Run the following, replacing the `keywords` list with your terms from Step 1:

```python
python3 << 'EOF'
import json
import unicodedata

with open("SLIDES_PATH") as f:      # absolute path from Step 2
    slides = json.load(f)

articles = []
try:
    with open("ARTICLES_PATH") as f:  # absolute path from Step 2, may be missing
        articles = json.load(f)
except FileNotFoundError:
    pass

keywords = ["keyword1", "keyword2", "keyword3"]  # from Step 1

def norm(s):
    # 全半角・大文字小文字の揺れを吸収する
    return unicodedata.normalize("NFKC", s or "").lower()

def score_items(items, kind):
    out = []
    for item in items:
        t, a, s = norm(item["t"]), norm(item["a"]), norm(item["s"])

        score = 0
        for kw in keywords:
            kw = norm(kw)
            if not kw:
                continue
            if kw in t: score += 10   # タイトル一致がいちばん強い
            if kw in s: score += 3    # セクション名
            if kw in a: score += 3    # 発表者名 / 著者名

        if score < 3:
            continue

        # 新しいものをやや優先する（LLM 系は陳腐化が速いため）
        year = int(item["d"][:4]) if item["d"] else 2018
        recency = max(0, min(6, (year - 2018) * 0.8))

        out.append((score + recency, score, kind, item))
    return out

results = score_items(slides, "slide") + score_items(articles, "article")

# スコア降順、同点なら新しいものを先に（安定ソートの二段掛け）
results.sort(key=lambda x: x[3]["d"] or "", reverse=True)
results.sort(key=lambda x: -x[0])

n_slides = sum(1 for r in results if r[2] == "slide")
n_articles = sum(1 for r in results if r[2] == "article")
print(f"total_slides={len(slides)} total_articles={len(articles)} matched={len(results)} ({n_slides} slides, {n_articles} articles)")
print()
for combined, score, kind, item in results[:24]:
    print(f"score={combined:.1f} text={score} kind={kind}")
    print(f"  t={item['t']}")
    print(f"  u={item['u']}")
    src = f"  src={item['src']}" if kind == "slide" else ""
    print(f"  a={item['a']}  d={item['d']}{src}")
    print(f"  s={item['s']}")
    print()
EOF
```

If `matched=0`, retry **once** with broader keywords (drop the most specific term, add the section name from Step 1). If it is still 0, skip Step 4 and go to **Step 4b** — the list has nothing, so search the web instead.

### Step 4 — Re-rank with your judgment

You now have up to 24 candidates, a mix of slides and articles. Produce a final ordered list of up to **10**.

Re-rank by:
1. **Semantic centrality** — judge from the title and section whether the item actually covers the query's core intent. Drop candidates that matched only on an incidental keyword.
2. **Section fit** — if Step 1 identified a section, prefer items from it.
3. **Depth vs. overview** — "入門/知りたい" → prefer 入門・全体像 and チュートリアル; "開発/実装したい" → prefer 開発・実務事例の資料.
4. **Recency** — for LLM-related queries strongly prefer recent material; for foundational topics (形態素解析, 分散表現) older material is still fine.
5. **Variety** — avoid returning five items from the same presenter/author unless they form a coherent series. There is no quota between slides and articles — rank purely on relevance and let the mix fall out naturally; a query the article list happens to cover deeply can legitimately return mostly (or only) articles, and vice versa.

Do not mechanically follow the Step 3 score — use it as a starting point.

### Step 4b — Fall back to the open web

**Only reached when Step 3 returned `matched=0` twice.** The list covers a lot but not everything, and it is
weakest at its recent edge — a query about something from the last few months can legitimately find nothing.
Rather than reporting an empty result, look for both slides and articles on the web.

**Slides.** Run **3–5 WebSearch queries** against the three hosts the list indexes. The material is Japanese, so the
queries must be **mostly Japanese** — an English-only query set finds almost nothing. Translate the query
into its Japanese term first (the same translation Step 1 already did for the keyword list):

- `<japanese-term> 資料 site:speakerdeck.com`
- `<japanese-term> スライド site:docswell.com`
- `<japanese-term> site:slideshare.net`
- `<japanese-term> 勉強会 発表資料` (wrap-up blog posts often link decks that search engines have not indexed yet)
- `<english-keyword> japanese site:speakerdeck.com` — one English query, worth it for research-flavoured topics

Use **one `site:` per query**. Never OR the host names together (`... docswell OR speakerdeck OR slideshare`):
without the operator the engine treats them as topic words and returns articles comparing slide-sharing
services instead of slides.

Keep only URLs shaped like an actual deck — `https://speakerdeck.com/<user>/<slug>`,
`https://www.docswell.com/s/<user>/<ID>-<slug>`, `https://www.slideshare.net/<user>/<slug>` — and discard
profile pages, embeds, PDF mirrors, and Qiita / Zenn / note.com / YouTube links (those are article territory,
handled below). Take **up to 5**.

**Articles.** Run **2–3 WebSearch queries** for blog posts / tech-blog articles. Unlike slides, articles aren't
confined to a handful of hosts, so do **not** use `site:`; instead point the query at the platforms individual
developers and companies actually write on:

- `<japanese-term> ブログ` or `<japanese-term> 技術ブログ`
- `<japanese-term> site:zenn.dev OR site:qiita.com` (one combined query is fine here — both are the same kind of platform, unlike the three distinct slide hosts above)
- `<japanese-term> hatenablog.com OR note.com`

Keep only URLs that look like an individual article (a Zenn/Qiita/note/hatenablog post, or a `/blog/`,
`/entry/`, `techblog.*`, `tech.*` path on a company site) — discard tag pages, category listings, and the
platform's own homepage. Take **up to 5**.

**For a narrow term, drop the padding, for both.** Words like `資料`, `ブログ` and `自然言語処理` let the engine
satisfy the query on the padding alone and quietly ignore the term you came for: `手話 自然言語処理 資料
site:speakerdeck.com` returns ten general-NLP decks with no mention of 手話, while the bare `手話
site:speakerdeck.com` returns decks that actually cover it. Query the term by itself first. If no result title
contains your term, that is the signal it was dropped — re-run bare before deciding there is nothing.

`WebFetch` the survivors (up to 8 calls in parallel across both kinds) to confirm each page exists and to read its real title, author and publication date:

```
WebFetch url="<candidate url>" prompt="Extract as JSON: title, author (presenter or author display name), published_date in YYYY-MM-DD form, and one-sentence English summary. Set is_nlp_related to true only if the content is about natural language processing, LLMs, speech/text processing or search. Null for anything unavailable."
```

Drop anything that 404s, comes back `is_nlp_related: false`, or whose summary shows it does not address the
query after all — `is_nlp_related` is true of almost everything in this field, so it cannot carry the
relevance judgment by itself. Then report in **Step 5's web-fallback format** — these results are unvetted and
must never be presented as part of the curated list.

If nothing survives on either side, say the query found nothing anywhere. Some topics genuinely have no
Japanese slide deck or article behind them, and "not found" is a useful, honest answer — better than five
respectable results that do not answer the question.

### Step 5 — Format the output

**Language detection rule (apply before writing any output):**

Judge the language of `$ARGUMENTS` yourself — you read it better than any character test. The rules below
resolve the cases where judgment is genuinely split.

1. **Hiragana or katakana present** → **Japanese**. Decisive: no other language uses them.
2. **No Han characters at all** → **English**. This is also the default whenever nothing else applies.
3. **Han characters only** (no kana) → Japanese and Chinese overlap here, so read the wording:
   - Japanese technical compounds and this list's own section names → **Japanese**
     (`形態素解析`, `事前学習`, `質問応答`, `情報抽出`, `全文検索`, `機械翻訳`).
   - Chinese wording and Chinese-only character forms → **Chinese**
     (`预训练`, `词向量`, `问答`, `語音辨識`, `檢索增強生成`, `幻灯片`, `投影片`).
   - Still ambiguous after reading it — a bare compound spelled identically in Japanese and traditional
     Chinese, such as `知識` or `文書` → **Japanese**, since the list itself is Japanese.
4. **Chinese → pick the script**, because the two editions are separate:
   - traditional-only forms (`語`, `檢`, `資`, `應`, `對`, `詞`, `處`, `實`) → **繁體中文**
   - simplified-only forms (`语`, `检`, `资`, `应`, `对`, `词`, `处`, `实`) → **简体中文**
   - neither appears, or both do → **简体中文**
   Match the query's script exactly in the reply; do not mix the two.

Apply the detected language to all headings and prose. Titles, presenter/author names and section names
are quoted **as they are stored** — always Japanese — and are never translated or converted between scripts.

Present the final re-ranked results, marking each one as a slide or an article so the two are never confused:

```
## Search results for "$ARGUMENTS"

*(Searched for: keyword1, keyword2, ...)*

Found N result(s): X slide(s), Y article(s).

### 1. 🖥️ [slide title](url)
**Slide** ・ **Presenter:** author ・ **Published:** YYYY-MM ・ **Host:** speakerdeck ・ **Section:** section name

### 2. 📝 [article title](url)
**Article** ・ **Author:** author ・ **Published:** YYYY-MM ・ **Section:** section name

### 3. ...
```

Report only the metadata returned in Step 3. Do **not** invent a description of an item's contents — you have not read the slide or article itself.

**Web-fallback format (only when you came from Step 4b).** Say up front that the list had nothing, and keep the
web findings visibly separate from the curated list — the reader must be able to tell the two apart at a glance,
and slides must stay visually distinct from articles within the fallback results too:

```
## Search results for "$ARGUMENTS"

The list has no slides or articles matching this query yet *(searched for: keyword1, keyword2, ...)*.

## Found on the web (not in the list)

These came from a web search and are **not curated** — they have not been reviewed for this list.

### 1. 🖥️ [slide title](url)
**Slide** ・ **Presenter:** author ・ **Published:** YYYY-MM ・ **Host:** speakerdeck

One sentence on what it covers, from the page itself.

### 2. 📝 [article title](url)
**Article** ・ **Author:** author ・ **Published:** YYYY-MM

One sentence on what it covers, from the page itself.

### 3. ...
```

Then close with the two next moves, in the detected language:

- nearby section names in the list that are worth browsing, plus alternate keywords to retry with;
- an offer to add the good ones: for slides, `/awesome-japanese-nlp-slides:find-new-slides $ARGUMENTS` produces
  entries ready to paste into `data/curated.json`; for articles, there is no equivalent discovery skill yet, so
  offer to paste an entry into `data/articles.json` by hand instead. Either way, contributions go to
  https://github.com/taishi-i/awesome-japanese-nlp-slides

If Step 4b also found nothing, drop the "Found on the web" block and report just those two next moves.

Whenever Step 4b ran, finish the reply with the `Sources:` section WebSearch requires, listing the result URLs
you actually used.

### Step 6 — Output a short reading-order suggestion

Skip this step entirely when you came from Step 4b — a reading order implies these items were vetted and
sequenced, which is exactly the claim the web fallback cannot make.

After the list, add a brief section (**in the detected language**) suggesting where to start. Slides and
articles can be freely mixed in the same reading order — order by how introductory vs. advanced the content
is, not by kind:

```
## Suggested reading order

1. 📝 [title](url) — why to start here (10–15 words)
2. 🖥️ [title](url) — what it adds next
3. 📝 [title](url) — for going deeper
```

**Rules:**
- Pick **2–4 items** from the final list and order them from introductory to advanced.
- Each reason should be a short phrase about what the reader gains — do not repeat the description verbatim.
- If the results are all at the same level (e.g. all case studies), replace the ordering with one sentence stating how they differ instead.
