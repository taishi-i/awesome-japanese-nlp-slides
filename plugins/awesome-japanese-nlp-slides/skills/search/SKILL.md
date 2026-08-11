---
description: Search curated Japanese NLP presentation slides and lecture materials (Speaker Deck / Docswell / SlideShare) from awesome-japanese-nlp-slides. Accepts keywords or natural language questions in any language.
when_to_use: "Use whenever the user is looking for Japanese NLP slides, lecture materials, or talks: conference tutorials, university lectures, LLM development / pretraining, fine-tuning, evaluation and benchmarks, RAG and search, morphological analysis, embeddings, or industry case studies. Trigger phrases include '日本語LLMのスライド', '形態素解析の発表資料', 'RAG の講演資料', '〜の勉強に使えるスライド', 'チュートリアル資料が見たい', 'Japanese NLP slides', 'lecture materials on Japanese LLM', '日語 LLM 的投影片', '形態素分析的發表資料', '日语 LLM 的幻灯片', '日语自然语言处理的演讲资料'."
argument-hint: [query]
allowed-tools: Bash
---

Search the awesome-japanese-nlp-slides database for: "$ARGUMENTS"

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

Please pass the keyword(s) you want to search for as the argument.

---

使い方: /awesome-japanese-nlp-slides:search <query>

クエリ例:
  /awesome-japanese-nlp-slides:search 日本語LLMの事前学習
  /awesome-japanese-nlp-slides:search 形態素解析
  /awesome-japanese-nlp-slides:search RAG
  /awesome-japanese-nlp-slides:search 評価 ベンチマーク
  /awesome-japanese-nlp-slides:search 大学講義

検索したいキーワードを引数に指定してください。

---

用法: /awesome-japanese-nlp-slides:search <query>

查询示例 / 查詢範例:
  /awesome-japanese-nlp-slides:search 日语 LLM 的预训练
  /awesome-japanese-nlp-slides:search 形态素解析
  /awesome-japanese-nlp-slides:search RAG
  /awesome-japanese-nlp-slides:search 评测 基准测试
  /awesome-japanese-nlp-slides:search 大学课程

请把想搜索的关键词作为参数传入。
```

Do **not** proceed to Step 1 if `$ARGUMENTS` is empty.

### Step 1 — Interpret the query

The user's query is: "$ARGUMENTS"

The data (titles, section names, presenter names) is **mostly Japanese**, with English titles mixed in.
So build a keyword list that contains **both Japanese and English** terms — do not search with English alone.

**Keywords are always Japanese and English, whatever language the query is in.** A Chinese query has to
be translated into the Japanese term before it can match anything: 预训练 → `事前学習`, 词向量 → `分散表現`,
问答 → `質問応答`, 语音识别 → `音声認識`, 检索增强生成 → `RAG`/`検索`. Never put a Chinese character form in
the keyword list: `形态素` matches nothing where `形態素` matches 27 decks, and neither `检索` nor `檢索`
matches anything against the 52 decks holding `検索`. Traditional forms occasionally coincide with the
Japanese spelling — translate rather than bet on the coincidence.

**Keyword rules:**
1. **Include the Japanese term and its English counterpart.** Substring match is used, so `形態素` catches 「形態素解析」「形態素解析器」, and `morpholog` catches "morphology"/"morphological".
2. **Add well-known tool / model names** when the query maps to a known domain — they often appear in slide titles.
3. **Aim for 4–8 keywords.** Fewer miss items; more inflates weak partial matches.

| Domain | Japanese keywords | English / tool names to add |
|---|---|---|
| 形態素解析・構文解析 | `形態素`, `係り受け`, `構文解析`, `解析器` | `morpholog`, `mecab`, `sudachi`, `juman`, `vibrato`, `kwja`, `ginza` |
| 分散表現・埋め込み | `分散表現`, `埋め込み`, `単語ベクトル` | `embed`, `vector`, `word2vec`, `chive`, `sbert` |
| 事前学習モデル・Transformer | `事前学習`, `言語モデル` | `bert`, `transformer`, `gpt`, `pretrain`, `huggingface` |
| LLM 開発・事前学習 | `事前学習`, `コーパス`, `構築`, `開発` | `llm`, `swallow`, `llm-jp`, `sarashina`, `plamo` |
| ファインチューニング・事後学習 | `ファインチューニング`, `事後学習`, `指示`, `蒸留` | `fine-tun`, `sft`, `rlhf`, `dpo`, `lora`, `peft` |
| 評価・ベンチマーク | `評価`, `ベンチマーク` | `eval`, `benchmark`, `jglue`, `llm-jp-eval`, `nejumi` |
| 全文検索・検索基盤 | `検索`, `全文検索`, `検索基盤`, `ランキング` | `search`, `elasticsearch`, `solr`, `lucene`, `rerank` |
| 検索・RAG | `検索拡張`, `情報検索`, `チャンキング` | `rag`, `retriev`, `embedding`, `ruri`, `graphrag` |
| LLM アプリ開発・運用 | `アプリ`, `運用`, `プロダクト`, `エージェント` | `agent`, `llmops`, `prompt`, `production` |
| 推論最適化・サービング | `推論`, `高速化`, `量子化`, `蒸留` | `infer`, `vllm`, `quantiz`, `distill`, `serving` |
| 正規化・表記ゆれ | `正規化`, `表記ゆれ`, `誤字`, `住所` | `normaliz`, `variant`, `typo` |
| 情報抽出・固有表現 | `固有表現`, `情報抽出`, `アノテーション` | `ner`, `entit`, `extract`, `annotat` |
| 文書処理・OCR | `文書`, `帳票`, `契約書`, `請求書` | `ocr`, `document`, `vlm`, `invoice` |
| 質問応答・知識 | `質問応答`, `知識` | `qa`, `question`, `knowledge` |
| 機械翻訳 | `翻訳`, `同時通訳` | `translat`, `nmt`, `mt` |
| テキスト分類・感情分析 | `分類`, `感情`, `評判`, `極性`, `検知` | `classif`, `sentiment`, `polarity`, `moderation`, `fasttext` |
| マルチモーダル・V&L | `マルチモーダル`, `画像`, `視覚`, `文書画像` | `vlm`, `vision`, `multimodal`, `vqa`, `clip` |
| 音声認識・音声処理 | `音声`, `音声認識`, `文字起こし`, `音声合成` | `speech`, `asr`, `tts`, `whisper`, `espnet` |
| 対話システム・音声対話 | `対話`, `音声対話`, `ボイスボット`, `チャットボット` | `dialog`, `spoken`, `voicebot`, `chatbot` |
| 生成・要約・校正 | `生成`, `要約`, `校正`, `文法誤り` | `generat`, `summar`, `correct`, `gec` |
| 解釈性・分析 | `解釈`, `分析`, `内部`, `言語学` | `interpret`, `analys`, `probing`, `attention` |
| 入門・チュートリアル | `入門`, `基礎`, `チュートリアル`, `講義` | `introduc`, `tutorial`, `lecture`, `basic` |
| 産業応用・事例 | `事例`, `実務`, `活用`, `導入` | `case`, `industr`, `production` |

**Section filter:** if the query clearly names a category, also note the matching section name so you can prefer it in Step 4. The 26 sections are:
入門・全体像 / 学会チュートリアル / 大学講義・体系的な講義資料 / 日本語の基礎解析（形態素解析・構文解析） / 日本語テキストの正規化・表記ゆれ / 単語・文の分散表現 / 事前学習モデル・Transformer / 大規模言語モデル（概論・動向） / 日本語LLMの開発（事前学習・コーパス構築） / ファインチューニング・事後学習 / LLM の推論最適化・サービング / 評価・ベンチマーク / 全文検索・検索基盤 / 検索・RAG / LLM アプリケーション開発・運用 / テキスト分類・感情分析 / 情報抽出・固有表現・アノテーション / 文書処理・OCR / 質問応答・知識 / 機械翻訳 / マルチモーダル・Vision-and-Language / 音声認識・音声処理 / 対話システム・音声対話 / 生成・要約・校正 / 解釈性・分析・言語学的視点 / 産業応用・実務事例

### Step 2 — Locate the data file

The data file ships with the plugin. Resolve its path via `${CLAUDE_PLUGIN_ROOT}` (Claude Code substitutes this inline in skill content), falling back to a scoped search only if the install is unusual:

```bash
SLIDES_PATH="${CLAUDE_PLUGIN_ROOT}/data/slides.json"
[ -f "$SLIDES_PATH" ] || SLIDES_PATH="$(find "${HOME}/.claude/plugins" -type f -name slides.json 2>/dev/null | grep "awesome-japanese-nlp-slides/" | head -1)"
echo "SLIDES_PATH=$SLIDES_PATH"
```

Use the resulting absolute `SLIDES_PATH` in Step 3.

### Step 3 — Search and score via Bash

**Do NOT use the Read tool** on the data file — it would consume ~30K tokens unnecessarily. Run the scoring in a single Bash call.

Each item in the JSON array has:
- `t`: slide title
- `u`: Speaker Deck / Docswell / SlideShare URL
- `a`: author (presenter)
- `d`: publication date (`YYYY-MM-DD`)
- `s`: section name
- `src`: `speakerdeck`, `docswell` or `slideshare`

Matching relies on the **title and section name only**, so cast a slightly wide keyword net.

Run the following, replacing the `keywords` list with your terms from Step 1:

```python
python3 << 'EOF'
import json
import unicodedata

with open("SLIDES_PATH") as f:    # absolute path from Step 2
    slides = json.load(f)

keywords = ["keyword1", "keyword2", "keyword3"]  # from Step 1

def norm(s):
    # 全半角・大文字小文字の揺れを吸収する
    return unicodedata.normalize("NFKC", s or "").lower()

results = []
for item in slides:
    t, a, s = norm(item["t"]), norm(item["a"]), norm(item["s"])

    score = 0
    for kw in keywords:
        kw = norm(kw)
        if not kw:
            continue
        if kw in t: score += 10   # タイトル一致がいちばん強い
        if kw in s: score += 3    # セクション名
        if kw in a: score += 3    # 発表者名

    if score < 3:
        continue

    # 新しい資料をやや優先する（LLM 系は陳腐化が速いため）
    year = int(item["d"][:4]) if item["d"] else 2018
    recency = max(0, min(6, (year - 2018) * 0.8))

    results.append((score + recency, score, item))

# スコア降順、同点なら新しい資料を先に（安定ソートの二段掛け）
results.sort(key=lambda x: x[2]["d"] or "", reverse=True)
results.sort(key=lambda x: -x[0])

print(f"total={len(slides)} matched={len(results)}")
print()
for combined, score, item in results[:20]:
    print(f"score={combined:.1f} text={score}")
    print(f"  t={item['t']}")
    print(f"  u={item['u']}")
    print(f"  a={item['a']}  d={item['d']}  src={item['src']}")
    print(f"  s={item['s']}")
    print()
EOF
```

If `matched=0`, retry **once** with broader keywords (drop the most specific term, add the section name from Step 1). If it is still 0, go to Step 5 and report no results.

### Step 4 — Re-rank with your judgment

You now have up to 20 candidates. Produce a final ordered list of up to **10**.

Re-rank by:
1. **Semantic centrality** — judge from the title and section whether the slide actually covers the query's core intent. Drop candidates that matched only on an incidental keyword.
2. **Section fit** — if Step 1 identified a section, prefer slides from it.
3. **Depth vs. overview** — "入門/知りたい" → prefer 入門・全体像 and チュートリアル; "開発/実装したい" → prefer 開発・実務事例の資料.
4. **Recency** — for LLM-related queries strongly prefer recent slides; for foundational topics (形態素解析, 分散表現) older material is still fine.
5. **Variety** — avoid returning five slides from the same presenter unless they form a coherent series.

Do not mechanically follow the Step 3 score — use it as a starting point.

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

Apply the detected language to all headings and prose. Slide titles, presenter names and section names
are quoted **as they are stored** — always Japanese — and are never translated or converted between scripts.

Present the final re-ranked results:

```
## Search results for "$ARGUMENTS"

*(Searched for: keyword1, keyword2, ...)*

Found N slide(s).

### 1. [slide title](url)
**Presenter:** author ・ **Published:** YYYY-MM ・ **Section:** section name

### 2. ...
```

Report only the metadata returned in Step 3. Do **not** invent a description of a slide's contents — you have not seen the slide itself.

If there are no results, suggest alternate keywords, list a few nearby section names, and link to:
https://github.com/taishi-i/awesome-japanese-nlp-slides

### Step 6 — Output a short reading-order suggestion

After the list, add a brief section (**in the detected language**) suggesting where to start:

```
## Suggested reading order

1. [slide title](url) — why to start here (10–15 words)
2. [slide title](url) — what it adds next
3. [slide title](url) — for going deeper
```

**Rules:**
- Pick **2–4 slides** from the final list and order them from introductory to advanced.
- Each reason should be a short phrase about what the reader gains — do not repeat the description verbatim.
- If the results are all at the same level (e.g. all case studies), replace the ordering with one sentence stating how they differ instead.
