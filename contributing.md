# Contributing

コントリビューションはいつでも歓迎します。

掲載したい資料があれば、[Issue](https://github.com/taishi-i/awesome-japanese-nlp-slides/issues)
または [Pull Request](https://github.com/taishi-i/awesome-japanese-nlp-slides/pulls) を送ってください。
日本語・英語のどちらでも構いません。

## 掲載の基準

このリストは「厳選リスト」です。日本語NLPに取り組む人が読んで得るものがある資料だけを載せます。
判断の基準は**中身**であって、ページ数でも新しさでも発表者の知名度でもありません。
1枚のポスターでも研究内容が詰まっていれば載せますし、7枚のLTでも導出や実測結果があれば載せます。

次のものは載せません。

- **中身のない資料** — 会社紹介、採用案内、イベント告知、アジェンダの反復だけで終わるもの。
  勉強会のスポンサー枠で発表された自社紹介スライドはここに当たります。
- **個人的なメモ・備忘録** — リンクと感想の羅列、資料自身が「特に有用な知見はない」と断っているもの。
- **単体で読めない断片** — 書籍の一部の節の数式だけを写したもの、前後の文脈なしでは追えない輪読の切れ端。
  章単位で自己完結している輪講資料は問題ありません。
- **教科書の要約止まりのもの** — 同じテーマをより深く扱った資料がすでにリストにある場合。
- **日本語NLPとの関連が薄いもの** — 生成AIを使った開発生産性の話、ツールの設定手順など、
  題材が言語処理そのものではないもの。ペイウォールの内側にある記事も載せません。
- **生成AIで量産された要約** — 一次情報を確認した形跡がなく、資料自身が内容の正確さを保証していないもの。

うまくいかなかった記録そのものは価値があります。落とすのは、何が原因でどうすればよいのかが
残っていないもの（「試したがだめでした」で終わるもの）です。

記事（`data/articles.json`）も同じ基準で判断します。加えて、出どころは企業の技術ブログや
開発者本人のブログ（Zenn・Qiita・note・はてなブログ、企業の `tech.*` ドメインなど）を優先し、
SEO・コンテンツマーケティング目的のページは避けてください。

## Pull Request を送る場合

編集するのは `data/curated.json` だけです。README（全言語）とプラグインの検索データは、
すべてここから生成されます。該当セクションの `entries` に 5 つのフィールドを追加してください。

```json
{
  "title": "スライドのタイトル",
  "url": "https://speakerdeck.com/example/slide",
  "author": "発表者名",
  "date": "2024-11-08",
  "source": "speakerdeck",
  "added": "2024-11-08"
}
```

- `date` は `YYYY-MM-DD`（README では `YYYY-MM` に丸めて表示されます）
- `source` は `speakerdeck` / `docswell` / `slideshare` のいずれか
- `added`（任意）はこのリストに追加した日（`YYYY-MM-DD`）。付けておくと、追加から7日間 README の「🎉 最近追加されたスライド」に掲載されます。省略した場合はそのまま通常の一覧にのみ載ります。

追加したら、次の 2 つを実行して生成物を更新してください。

```bash
python3 scripts/generate_readme.py      # README.md, index.md, docs/README.*.md
python3 scripts/build_plugin_data.py    # プラグインの slides.json / articles.json
```

`data/articles.json`（ブログ記事・Web ページの一覧）を編集した場合も同様に、
`generate_articles_readme.py` と `build_plugin_data.py` を実行してください。
`build_plugin_data.py` はプラグインの `search` スキルが使う検索データを
スライド・記事の両方について書き出します。

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

出力はあくまで下書きです。PR を出す前に、スライド本体に目を通し、
[掲載の基準](#掲載の基準)を満たしているか確認してください。スキルは検索結果のページから
タイトル・発表者・公開日を確認しますが、資料の中身が薄いかどうかまでは判断しきれません。
