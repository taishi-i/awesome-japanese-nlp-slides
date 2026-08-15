# Contributing

コントリビューションはいつでも歓迎します。

掲載したい資料があれば、[Issue](https://github.com/taishi-i/awesome-japanese-nlp-slides/issues)
または [Pull Request](https://github.com/taishi-i/awesome-japanese-nlp-slides/pulls) を送ってください。
日本語・英語のどちらでも構いません。

## Pull Request を送る場合

編集するのは `data/curated.json` だけです。README（全言語）とプラグインの検索データは、
すべてここから生成されます。該当セクションの `entries` に 5 つのフィールドを追加してください。

```json
{
  "title": "スライドのタイトル",
  "url": "https://speakerdeck.com/example/slide",
  "author": "発表者名",
  "date": "2024-11-08",
  "source": "speakerdeck"
}
```

- `date` は `YYYY-MM-DD`（README では `YYYY-MM` に丸めて表示されます）
- `source` は `speakerdeck` / `docswell` / `slideshare` のいずれか

追加したら、次の 2 つを実行して生成物を更新してください。

```bash
python3 scripts/generate_readme.py      # README.md, docs/README.*.md
python3 scripts/build_plugin_data.py    # プラグインの slides.json
```

生成の仕組みや、セクション・言語の追加方法は [`scripts/README.md`](scripts/README.md) に詳しく書いてあります。

## 追加する資料を探す

このリポジトリのプラグインには、まだ収録されていないスライドを探す `find-new-slides` スキルがあります。
分野を渡すと Speaker Deck・Docswell・SlideShare を検索し、収録済みのものを除外したうえで、
各スライドのタイトル・発表者・公開日をページ本体で確認し、上の形式の JSON をセクションごとに出力します。

```
/plugin marketplace add taishi-i/awesome-japanese-nlp-slides
/plugin install awesome-japanese-nlp-slides@awesome-japanese-nlp-slides
```

```
/awesome-japanese-nlp-slides:find-new-slides RAG
/awesome-japanese-nlp-slides:find-new-slides 音声認識
/awesome-japanese-nlp-slides:find-new-slides            # 分野を指定しない場合は最近公開されたものを探す
```

出力はあくまで下書きです。PR を出す前に、スライド本体に目を通してください。
