# awesome-japanese-nlp-slides — Articles

![Awesome Japanese NLP Slides](../images/awesome-japanese-nlp-slides.png)

[日本語 (Japanese)](https://github.com/taishi-i/awesome-japanese-nlp-slides/blob/main/docs/ARTICLES.ja.md) | [English](https://github.com/taishi-i/awesome-japanese-nlp-slides/blob/main/docs/ARTICLES.en.md) | [繁體中文 (Chinese)](https://github.com/taishi-i/awesome-japanese-nlp-slides/blob/main/docs/ARTICLES.zh-hant.md) | [简体中文 (Chinese)](https://github.com/taishi-i/awesome-japanese-nlp-slides/blob/main/docs/ARTICLES.zh-hans.md)

← Back to the [slide list](https://github.com/taishi-i/awesome-japanese-nlp-slides/blob/main/README.md)

A curated list of web pages and blog posts on Japanese natural language processing (NLP), written by companies and individual developers.
Organized under the same 32 topics as the [slide list](https://github.com/taishi-i/awesome-japanese-nlp-slides/blob/main/README.md).

115 articles across 32 categories.

Article titles are kept as published, so most of them are in Japanese.

> [!NOTE]
> This list is still a work in progress. More material will be added over time.

## Contents

- [Getting Started / Big Picture](#getting-started--big-picture)
- [Conference Tutorials](#conference-tutorials)
- [University Lectures & Course Materials](#university-lectures--course-materials)
- [Japanese Text Analysis (Morphological & Syntactic)](#japanese-text-analysis-morphological--syntactic)
- [NLP Library & Tool Development](#nlp-library--tool-development)
- [Japanese Text Normalization & Spelling Variants](#japanese-text-normalization--spelling-variants)
- [Dictionaries, Kana-Kanji Conversion & Japanese Input (IME)](#dictionaries-kana-kanji-conversion--japanese-input-ime)
- [Word & Sentence Embeddings](#word--sentence-embeddings)
- [Pretrained Models & Transformers](#pretrained-models--transformers)
- [Large Language Models (Overview & Trends)](#large-language-models-overview--trends)
- [Building Japanese LLMs (Pretraining & Corpus Construction)](#building-japanese-llms-pretraining--corpus-construction)
- [Fine-tuning & Post-training](#fine-tuning--post-training)
- [LLM Inference Optimization & Serving](#llm-inference-optimization--serving)
- [Evaluation & Benchmarks](#evaluation--benchmarks)
- [Full-text Search & Search Infrastructure](#full-text-search--search-infrastructure)
- [Search & RAG](#search--rag)
- [LLM Application Development & Operations](#llm-application-development--operations)
- [AI Agents & MCP](#ai-agents--mcp)
- [LLM Safety & Security](#llm-safety--security)
- [Text Classification & Sentiment Analysis](#text-classification--sentiment-analysis)
- [Spam & Harmful Content Countermeasures](#spam--harmful-content-countermeasures)
- [Text Mining & Topic Models](#text-mining--topic-models)
- [Information Extraction, NER & Annotation](#information-extraction-ner--annotation)
- [Document AI & OCR](#document-ai--ocr)
- [Question Answering & Knowledge](#question-answering--knowledge)
- [Machine Translation](#machine-translation)
- [Multimodal & Vision-and-Language](#multimodal--vision-and-language)
- [Speech Recognition & Speech Processing](#speech-recognition--speech-processing)
- [Dialogue Systems & Spoken Dialogue](#dialogue-systems--spoken-dialogue)
- [Generation, Summarization & Proofreading](#generation-summarization--proofreading)
- [Interpretability, Analysis & Linguistic Perspectives](#interpretability-analysis--linguistic-perspectives)
- [Industry Applications & Case Studies](#industry-applications--case-studies)

## Getting Started / Big Picture

自然言語処理そのものを俯瞰したい人が最初に読む記事。

- [自然言語処理入門: 機械学習を用いた自然言語処理モデルの構築](https://qiita.com/iitachi_tdse/items/5b5e2edea040cd2a1575) - いいたっち（@iitachi_tdse） (2022-12)

## Conference Tutorials

言語処理学会などの参加報告記事。チュートリアルの雰囲気が伝わる。

- [言語処理学会 (NLP2026) 参加報告](https://future-architect.github.io/articles/20260420a/) - 田中裕真（フューチャー株式会社） (2026-04)
- [言語処理学会第 32 回年次大会（NLP2026）参加報告](https://hack.nikkei.com/blog/nlp2026/) - 白井穂乃, 中村礼音, 大村和正（日本経済新聞社） (2026-03)
- [NLP2025 参加報告](https://tech.gunosy.io/entry/NLP2025) - 森田, 大城, 井口（株式会社Gunosy） (2025-04)
- [NLP2025に参加してきました](https://moneyforward-dev.jp/entry/2025/03/21/160205) - 山岸（株式会社マネーフォワード） (2025-03)

## University Lectures & Course Materials

大学の演習課題や講義に取り組んだ記録。体系的に学べる教材への入口。

- [言語処理100本ノック ー第1章ー](https://leadinge.co.jp/rd/2021/10/25/1339/) - K.Y（株式会社リーディング・エッジ社） (2021-10)
- [言語処理100本ノック2020を打った話](https://trap.jp/post/1120/) - YumizSui（東京科学大学デジタル創作同好会traP） (2020-09)
- [まとめ: 言語処理100本ノックで学べることと成果](https://qiita.com/FukuharaYohei/items/6f0af3c4e270d8af2d99) - FukuharaYohei (2020-03)

## Japanese Text Analysis (Morphological & Syntactic)

形態素解析・係り受け解析の仕組みを手を動かして理解する記事。

- [テキスト分析の大通り#04: 形態素解析(Sudachi編)](https://note.com/yssymmt/n/n1da058b57cab) - yssymmt (2022-10)
- [形態素解析に触れる ～ 日本語処理の入口を理解する ～](https://note.com/1in9mu/n/n28df7e4879bb) - lingmu (2022-05)
- [自然言語処理入門 Vol.2 係り受け解析/構文解析](https://leadinge.co.jp/rd/2021/05/10/696/) - M.H（株式会社リーディング・エッジ社） (2021-05)
- [自然言語処理の形態素解析について調べたまとめ](https://zenn.dev/megane_otoko/articles/008_morphological_analysis) - koji (2020-11)
- [形態素解析器比較 Sudachi vs Mecab+Neologd](https://tdual.hatenablog.com/entry/2020/07/13/162151) - tdualdir (2020-07)
- [係り受けに基づく日本語単語埋め込みを用いた係り受け解析](https://tech-blog.lapras.com/techBlogs/dependency-parsing-using-japanese-word-embedding-based-on-dependency) - R&Dチーム（LAPRAS株式会社） (2019-11)

## NLP Library & Tool Development

形態素解析器や検索ツールなど、NLPライブラリ本体の実装記事。

- [速度の高みを目指す：高速な単語分割器 Vaporetto の技術解説](https://tech.legalforce.co.jp/entry/2021/09/28/180844) - 赤部（LegalOn Technologies） (2021-09)
- [Rustによる自然言語処理ツールの実装: 形態素解析器「sudachi.rs」](https://qiita.com/sorami/items/7934fec2074c493c0f7d) - sorami (2019-12)

## Japanese Text Normalization & Spelling Variants

neologdnや独自の正規化処理など、表記ゆれ対策の実装記事。

- [住所正規化のデモ機能を作ったので、日本のヤバい住所を入力してみた](https://zenn.dev/sikkim/articles/bc86fbcac3a9fd) - TAKAHASHI Taro (2023-09)
- [日本語テキストの前処理：neologdn、大文字小文字、Unicode正規化](https://tuttieee.hatenablog.com/entry/ja-nlp-preprocess) - tuttieee (2019-12)
- [pythonによる日本語前処理備忘録](https://datumstudio.jp/blog/python%E3%81%AB%E3%82%88%E3%82%8B%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%89%8D%E5%87%A6%E7%90%86%E5%82%99%E5%BF%98%E9%8C%B2/) - 安達（DATUM STUDIO株式会社） (2018-10)
- [自然言語処理における前処理の種類とその威力](https://qiita.com/Hironsan/items/2466fe0f344115aff177) - Hironsan (2017-04)

## Dictionaries, Kana-Kanji Conversion & Japanese Input (IME)

IMEやかな漢字変換エンジンの自作記録。

- [自作 macOS IME「RomKana」開発記](https://zenn.dev/toshinao/articles/1cffb713b1c670) - toshinao (2026-06)
- [IMEなしの日本語サジェスト実装メモ：実務で使える4つのTips（+番外編1つ）](https://qiita.com/Rapls/items/868df2f859df470d86e9) - Rapls (2026-05)
- [Swift：【IME自作プロジェクト】かな漢字変換ライブラリ作成中](https://qiita.com/Kyome/items/5ae009a2e8e15c5ff6bf) - Kyome (2018-10)

## Word & Sentence Embeddings

単語埋め込み・分散表現の仕組みと活用の解説記事。

- [Sentence-Transformersで日本語文埋め込みを理解する：可視化からクラスタリングまで](https://zenn.dev/dxc_ai_driven/articles/22069126393a7d) - Adrian Tam（DXC AI-Driven） (2025-09)
- [テキスト埋め込みモデルPLaMo-Embedding-1Bの開発](https://tech.preferred.jp/ja/blog/plamo-embedding-1b/) - Kaito Suzuki（Preferred Networks） (2025-04)
- [単語埋め込みを単語埋め込みに埋め込む -前編-](https://buildersbox.corp-sansan.com/entry/2019/03/30/110000) - 荒居（Sansan株式会社） (2019-03)
- [なぜ自然言語処理にとって単語の分散表現は重要なのか？](https://qiita.com/Hironsan/items/a58636f946dd51f670b0) - Hironsan (2017-03)

## Pretrained Models & Transformers

BERTとTransformerの仕組みを図解・実装で理解する記事。

- [TransformerのSelf AttentionのQKVを直感的に解説する](https://qiita.com/kenmatsu4/items/1b3853a3314ab66eb2a3) - kenmatsu4（まつけん） (2026-05)
- [【図解】BERTの仕組みと進化の流れ：Attention・Transformerから理解する](https://zenn.dev/stockdatalab/articles/20250614_tech_nlpbert) - 情報収集ラボ (2025-06)
- [第1回：Transformerとは何か？ Attention Is All You Needについて調べてみた。](https://zenn.dev/tech_taka/articles/4c0e632897b2e8) - tech_taka (2025-04)
- [Transformerの文章生成の仕組みを理解する](https://future-architect.github.io/articles/20250226a/) - 森友雅（フューチャー株式会社） (2025-02)
- [BERTモデルとファインチューニング](https://zenn.dev/yosuke00/articles/9d9d405e164198) - Yosuke00 (2023-01)
- [深層学習界の大前提Transformerの論文解説！](https://qiita.com/omiita/items/07e69aef6c156d23c538) - @omiita（オミータ） (2019-12)

## Large Language Models (Overview & Trends)

LLMの全体像や最新動向を追った記事・まとめ。

- [2026年4月のLLMアップデートラッシュを振り返る](https://qiita.com/camcam/items/af76ca0b9ffe5eae1bf1) - camcam (2026-05)
- [日本特有の知識に特化した大規模言語モデルの学習および評価](https://zenn.dev/elyza/articles/9e46b79371fc0e) - Daisuke Oba（ELYZA株式会社） (2024-11)
- [ChatGPT（とその周辺）の技術](https://zenn.dev/zenkigen_tech/articles/2023-05-kurihara) - masakuri（株式会社ZENKIGEN） (2023-06)
- [話題爆発中のAI「ChatGPT」の仕組みにせまる！](https://qiita.com/omiita/items/c355bc4c26eca2817324) - @omiita（オミータ） (2022-12)

## Building Japanese LLMs (Pretraining & Corpus Construction)

日本語LLMを実際に開発したチームの知見と、事前学習の技術記事まとめ。

- [Llama-3-Swallow: 日本語に強い継続事前学習モデル](https://zenn.dev/tokyotech_lm/articles/f65989d76baf2c) - Kazuki Fujii（東京科学大学 岡崎研究室） (2024-07)
- [継続事前学習による金融ドメイン特化LLMの構築の検証](https://tech.preferred.jp/ja/blog/qfin-llm-continual-pretraining/) - Masanori Hirano（Preferred Networks） (2024-04)
- [日本語LLM の学習に関する技術記事まとめ](https://note.com/npaka/n/n23e2a05cb650) - npaka (2024-02)
- [Swallow: LLaMA-2 日本語継続事前学習モデル](https://zenn.dev/tokyotech_lm/articles/d6cb3a8fdfc907) - Kazuki Fujii（東京科学大学 岡崎研究室） (2023-12)

## Fine-tuning & Post-training

LoRAなどを使ったファインチューニングの入門・実践記事。

- [LLM 事後学習 (SFT / RLHF / DPO / RLVR / GRPO / 自己蒸留) を教師信号から眺める](https://zenn.dev/shunk031/articles/llm-post-training-overview) - しゅんけー, Ph.D. (2026-06)
- [LLMファインチューニング入門──RAGと使い分けるための基礎からLoRA実装まで【2026】](https://zenn.dev/karaagedesu/articles/edf46190f70b1d) - karaagedesu (2026-05)
- [大規模言語モデルのファインチューニングを理解するための丁寧な入門ガイド](https://zenn.dev/nakano_teppei/articles/fe4ae4748ecb5d) - 中野哲平 (2025-11)

## LLM Inference Optimization & Serving

vLLMや量子化を使った推論高速化の実践記事。

- [LLMの量子化手法と実装方法について](https://www.skygroup.jp/tech-blog/article/2117/) - Sky株式会社 (2026-02)
- [「量子化済みLLM+LoRA」 vs 「量子化なしLLM+LoRA」、RPSとlatencyはどう変わるか？](https://buildersbox.corp-sansan.com/entry/2025/12/22/100000) - 齋藤慎一朗（Sansan株式会社） (2025-12)
- [vLLMを利用したLLM推論高速化テクニック](https://acro-engineer.hatenablog.com/entry/2024/12/24/120000) - tereka114（株式会社アクロクエストテクノロジー） (2024-12)
- [TanukiモデルのAWQ、GPTQ、GGUF量子化について](https://zenn.dev/matsuolab/articles/2857bf0feeeb5d) - Aratako（松尾研究室） (2024-09)

## Evaluation & Benchmarks

JGLUEなど日本語LLMの評価手法・ベンチマークの解説記事。

- [事前学習LLMの評価における既存LLMの活用](https://tech.preferred.jp/ja/blog/llm-eval-by-answer-matching/) - Hiroaki Mikami（Preferred Networks） (2025-09)
- [LLMの精度ってどう測るの？評価指標を調べてみた](https://tech.smarthr.jp/entry/2025/08/05/192115) - mizunao（株式会社SmartHR） (2025-08)
- [大規模言語モデル（LLM）における日本語評価の概観](https://tech.algomatic.jp/entry/2024/02/29/153905) - なべ（Algomatic） (2024-02)
- [日本語LLMのベンチマーク：「JGLUE」と「Rakuda Benchmark」](https://note.com/bakushu/n/n545a97ea43d1) - Baku (2023-08)

## Full-text Search & Search Infrastructure

Elasticsearchなど検索基盤を日本語向けにチューニングする記事。

- [全文検索を日本語向けにチューニングする](https://linkers.hatenablog.com/entry/2024/02/02/073000) - jesus_isao（株式会社Linkers） (2024-02)
- [Elasticsearchで社内ナレッジを全文検索するためにやったこと](https://qiita.com/s-itou/items/f5f85ae16b8143db6a9c) - s-itou (2023-12)
- [検索のランキング処理を改善するポイント（『機械学習による検索ランキング改善ガイド』を執筆しました）](https://techblog.lycorp.co.jp/ja/20231113a) - 真鍋知博（LINEヤフー株式会社） (2023-11)
- [Elasticsearchで日本語検索を扱うためのマッピング定義](https://techblog.zozo.com/entry/elasticsearch-mapping-config-for-japanese-search) - vasilyjp（株式会社ZOZO） (2021-11)

## Search & RAG

RAGの仕組みをゼロから実装して学ぶ記事。

- [「手作り RAG システム」で RAG の仕組みを学び直す](https://zenn.dev/google_cloud_jp/articles/e699bda0a298d6) - Etsuji Nakai（Google Cloud Japan） (2025-12)
- [RAGをゼロから実装して仕組みを学ぶ【2025年版】](https://zenn.dev/knowledgesense/articles/2619c6e5918d08) - Atsushi Kadowaki（株式会社KnowledgeSense） (2025-11)
- [Elasticsearchのハイブリッド検索を用いて高精度なRAGを簡単に実現する](https://acro-engineer.hatenablog.com/entry/2024/12/17/120000) - shin0higuchi（株式会社アクロクエストテクノロジー） (2024-12)

## LLM Application Development & Operations

プロンプトの設計・管理など、LLMプロダクト開発の実務記事。

- [LLMアプリケーション開発におけるプロンプトの取得と管理](https://tech-blog.rakus.co.jp/entry/20260129/llm) - TKDS（株式会社ラクス） (2026-01)
- [LLMOpsを実運用する――プロンプト管理・評価・ツール選定の実際](https://zenn.dev/shintaroamaike/articles/ba975609780e3a) - ShintaroAmaike (2024-12)
- [LLMプロダクト開発のことはじめ #02 ~ よい応答を得るためのプロンプト制約](https://tech.algomatic.jp/entry/column/llm-product/02) - 宮脇（Algomatic） (2024-08)
- [プロンプト技術を高めるテクニック集【入門編】](https://zenn.dev/knowledgesense/articles/7504b1c6bbba84) - Atsushi Kadowaki（株式会社KnowledgeSense） (2024-03)

## AI Agents & MCP

LangGraphやMCPを使ったAIエージェント実装の記事。

- [LangGraphでシンプルな「AIエージェント」を作ってみた](https://www.skygroup.jp/tech-blog/article/2320/) - Sky株式会社 (2026-04)
- [MCP と LangGraph で構築：Human-in-the-Loop 対応の AI エージェントを作る](https://qiita.com/raid50/items/69ff348e57cbb764b015) - raid50 (2025-12)
- [AIエージェント開発への探求 - パート1：アーキテクチャの理解と実装アプローチ](https://techblog.lycorp.co.jp/ja/20250609a) - Nguyễn Trọng Phúc（LINEヤフー株式会社） (2025-06)

## LLM Safety & Security

プロンプトインジェクションなどLLM特有の脅威と対策の記事。

- [【LLMセキュリティ】間接的プロンプトインジェクションの脅威と対策](https://tech.akariinc.co.jp/entry/2026/01/29/190549) - soichiro_sugimoto（株式会社AKARI） (2026-01)
- [プロンプトインジェクション対策: 様々な攻撃パターンから学ぶセキュリティのリスク](https://blog.flatt.tech/entry/prompt_injection) - 石川（GMOフラットセキュリティ株式会社） (2025-05)

## Text Classification & Sentiment Analysis

テキスト分類・感情分析モデルの実装記事。

- [BERTモデルを使った日本語テキスト感情分析プログラムの実装](https://qiita.com/kiyotaman/items/736d5d0e47dbfd419244) - kiyotaman（清田史和） (2024-10)
- [Hugging Faceを使って事前学習モデルを日本語の感情分析用にファインチューニングしてみた](https://dev.classmethod.jp/articles/huggingface-jp-text-classification/) - nokomoro3（クラスメソッド株式会社） (2022-09)
- [ポジティブ？ネガティブ？ツイートの感情分析にBERTを活用した事例紹介 〜 学習データのラベル偏りに対する取り組み](https://techblog.yahoo.co.jp/entry/2021051730150930/) - 山城颯太（ヤフー株式会社） (2021-05)
- [機械学習によるテキスト分類（入門）](https://tech.unifa-e.com/entry/2020/03/23/092121) - ユニファ株式会社 (2020-03)
- [教師なしで作る評価分析器](https://hironsan.hatenablog.com/entry/2018/09/14/095519) - Hironsan (2018-09)

## Spam & Harmful Content Countermeasures

不適切な投稿・コメントを検知する仕組みの開発記事。

- [小学生向けチャットシステムで必要なNGワード検出方法のメモ](https://zenn.dev/appleworld/articles/b4f3e96bf90948) - T.H is ぺんぐぃん (2025-09)
- [ChatGPTを支える技術 コンテンツモデレーションの紹介](https://blog.brainpad.co.jp/entry/2023/05/26/153230) - 米川（株式会社ブレインパッド） (2023-05)
- [大規模深層学習モデルによるYahoo!ニュース「不適切コメント」対策](https://techblog.yahoo.co.jp/entry/2021041930133238/) - 清水徹（ヤフー株式会社） (2021-04)

## Text Mining & Topic Models

トピックモデルなどテキストマイニング手法の実践記事。

- [テキストマイニングへの道03――トピックモデルとの格闘1](https://hunihunisaito.hatenablog.com/entry/2023/02/21/000000) - hunihunisaito (2023-02)
- [近年の本格ミステリを可視化する【テキストマイニング】](https://qiita.com/masaka_programming/items/4d871f90c5876a3bcb38) - masaka_programming (2022-09)
- [\[R\] トピックモデル(LDA)を用いた大量文書の教師なし分類](https://qiita.com/YM_DSKR/items/017a5dddeb56fcdf1054) - YM_DSKR (2019-02)

## Information Extraction, NER & Annotation

固有表現抽出（NER）のデータセットと実装の記事。

- [【自然言語処理】アノテーションがぐっと楽になる！ お助けツールprodigyについて](https://note.com/asahi_ictrad/n/n2201dad206bd) - 朝日新聞社メディア研究開発センター（杉野かおり） (2021-07)
- [Transformersを用いた固有表現抽出のtips](https://tech.mntsq.co.jp/entry/2020/12/16/160006) - 稲村和樹（株式会社MNTSQ） (2020-12)
- [Wikipediaを用いた日本語の固有表現抽出データセットの公開](https://tech.stockmark.co.jp/blog/202012_ner_dataset/) - Stockmark株式会社 (2020-12)
- [固有表現抽出のアノテーションデータについて](https://kzinmr.hatenablog.com/entry/2020/10/06/162659) - kzinmr（稲村和樹） (2020-10)
- [spaCy + GiNZAを使って固有表現抽出とカスタムモデルの学習をしてみる](https://www.mof-mof.co.jp/tech-blog/spacy-ner/) - mofmof-inc（株式会社もふもふ） (2020-03)
- [ディープラーニングで作る固有表現認識器](https://hironsan.hatenablog.com/entry/deep-named-entity-recognition_1) - Hironsan (2018-05)

## Document AI & OCR

帳票・請求書などをAI-OCRやLLMでデータ化する記事。

- [請求書読み取りにおけるOCRとLLMの最適な役割分担 - LLMに何をさせるべきか](https://zenn.dev/edash_tech_blog/articles/346c03c39c80a9) - ikeda（株式会社e-dash） (2025-11)
- [LLMによる文書解析の性能を比較したリーダーボード](https://hironsan.hatenablog.com/entry/intelligent-document-processing-leaderboard) - Hironsan (2025-10)
- [AIによる契約書の自動レビュー機能を作ってみた](https://zenn.dev/minedia/articles/ai-legal-review) - Matsukura Yuki（株式会社マインディア） (2024-09)
- [非定型 AI-OCR 作ってみた 〜 AI 時代の開発戦略を添えて](https://zenn.dev/simpleform/articles/20231202-02-empowering-ocr-with-llm) - 小間（株式会社SimpleForm） (2023-12)

## Question Answering & Knowledge

知識グラフを使った質問応答・推論の実装記事。

- [オントロジー駆動でGraphRAGを構築してみた](https://techblog.insightedge.jp/entry/ontology-graph-rag) - 齊藤（Insight Edge株式会社） (2026-08)
- [社内用語集を気軽に質問できるSlackBotを作ってみた (RAGの応用アプリ)](https://tech-blog.abeja.asia/entry/in-house-jargon-slackbot-with-rag-202402) - y034112（株式会社ABEJA） (2024-02)
- [知識グラフ上での推論のためのモデルQuery2Boxを試す](https://recruit.group.gmo/engineer/jisedai/blog/kg_inference/) - S.S.（GMOインターネットグループ） (2022-04)

## Machine Translation

機械翻訳モデルの開発・自作の記事。

- [特化型大規模言語モデル『PLaMo翻訳』を公開しました](https://tech.preferred.jp/ja/blog/plamo-translate/) - Kentaro Imajo（Preferred Networks） (2025-05)
- [ニューラル機械翻訳モデルを自作してみる](https://lab.astamuse.co.jp/entry/neural-machine-translation) - astamuse株式会社 (2020-12)

## Multimodal & Vision-and-Language

画像と言語を組み合わせるVLM（視覚言語モデル）の解説記事。

- [高性能な日本語マルチモーダル基盤モデル「clip-japanese-base-v2」の公開](https://techblog.lycorp.co.jp/ja/20251218a) - 岡田俊太郎ほか（LINEヤフー株式会社） (2025-12)
- [CLIPで画像とテキストを理解する：ゼロショット分類を実装してみた](https://zenn.dev/madaozaku/articles/5dd0d828ea151b) - madaozaku (2025-10)
- [【ローカルVLM】マルチモーダル・モデルは便利すぎる件【OpenWebUI】](https://note.com/catap_art3d/n/nba533680f191) - Catapp-Art3D (2025-05)
- [うさぎでもわかる日本発の大規模視覚言語モデル「NABLA-VL」](https://zenn.dev/taku_sid/articles/20250423_nabla_vlm) - taku_sid (2025-04)

## Speech Recognition & Speech Processing

Whisperなど音声認識モデルの検証・活用記事。

- [SwiftUIで作るオンデバイス話者分離アプリ - 営業商談の音声メモを端末内で完結](https://zenn.dev/okamyuji/articles/swiftui-offline-speaker-diarization) - okamyuji (2025-12)
- [Whisper による音声認識の最先端〜8年越しのASR](https://zenn.dev/simpleform/articles/20231206-02-automatic-speech-recognition-whisper) - 小間（株式会社SimpleForm） (2023-12)
- [Whisperの音声認識精度および認識速度の検証](https://tech.revcomm.co.jp/investigate-whisper-asr) - wataru-nakata（株式会社RevComm） (2022-11)
- [話者の顔ランドマークを用いた音声分離](https://tech.preferred.jp/ja/blog/speech_separation_with_face_landmark/) - Motoki Sato（Preferred Networks） (2019-10)

## Dialogue Systems & Spoken Dialogue

音声対話AIの開発・評価に関する実務記事。

- [音声対話システムの自動評価フレームワーク「VociMetrics」](https://developers.cyberagent.co.jp/blog/archives/61458/) - ohira_yoshiki（株式会社サイバーエージェント） (2025-12)
- [リアルタイム音声対話AI開発の取り組み紹介（Tech-Verse 2025）](https://techblog.lycorp.co.jp/ja/20250903a) - 三宅純平, 木下泰輝（LINEヤフー株式会社） (2025-09)
- [初心者に捧げる対話システムの作り方](https://qiita.com/Hironsan/items/0373339388f460cebb08) - Hironsan (2016-08)

## Generation, Summarization & Proofreading

文章生成・要約・校正を自動化する実装記事。

- [AIによる文章要約と重複チェックの開発](https://tech.makeshop.co.jp/entry/2024/10/07/180251) - tech-makeshop-mori（GMOメイクショップ株式会社） (2024-10)
- [大自然言語時代のための、文章要約](https://qiita.com/icoxfog417/items/d06651db10e27220c819) - icoxfog417 (2017-10)
- [Qiita:Team + Hubot + textlintで文章校正を自動で実行する](https://techblog.zozo.com/entry/auto_sentence_proofreading_of_posts) - vasilyjp（株式会社ZOZO） (2017-05)

## Interpretability, Analysis & Linguistic Perspectives

LLMの内部表現を解析・解釈する記事。

- [ＬＬＭの内部表現を理解する解析と解釈](https://note.com/makokon/n/n4f795b8dafec) - makokon (2026-04)
- [言語処理学会第31回年次大会（NLP2025）に行ってきました](https://zenn.dev/finatext/articles/nlp-2025-report) - Ryotaro（Finatextホールディングス） (2025-04)
- [ChatGPT先生に教わりながら「Transformerの肝」である「注意機構（Attention機構）」を可視化する](https://developer.mamezou-tech.com/blogs/2023/03/26/using-transformer-03/) - shuichi-takatsu（株式会社豆蔵） (2023-03)
- [【self attention】簡単に予測理由を可視化できる文書分類モデルを実装する](https://qiita.com/itok_msi/items/ad95425b6773985ef959) - itok_msi（k ito） (2018-02)

## Industry Applications & Case Studies

企業の現場でLLM・NLPを活用した実務事例の記事。

- [AI駆動開発の効果、どう測る？データで見えた生産性向上と、その先の課題](https://techblog.spiderplus.co.jp/entry/2026/07/24/120000) - spiderplus（株式会社スパイダープラス） (2026-07)
- [AI/機械学習によるカスタマーサポートの回答予測 ── 試行錯誤の歴史](https://tech.smarthr.jp/entry/2025/03/05/145917) - kano（株式会社SmartHR） (2025-03)
- [with 生成AIで営業生産性を倍増させる、LayerXの内製プロダクト Sales Portalの現在地](https://note.com/numashi_biz/n/n0161bb02f485) - numashi（株式会社LayerX） (2025-02)

## License

[CC0 1.0 Universal](http://creativecommons.org/publicdomain/zero/1.0/)

> [!NOTE]
> CC0 applies to this list itself. The copyright of each linked article belongs to its respective author or company.
