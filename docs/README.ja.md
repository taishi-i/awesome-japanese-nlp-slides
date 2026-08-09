# awesome-japanese-nlp-slides

![Awesome Japanese NLP Slides](../images/awesome-japanese-nlp-slides.png)

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-slides)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-slides/pulls)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

[日本語 (Japanese)](https://github.com/taishi-i/awesome-japanese-nlp-slides/blob/main/docs/README.ja.md) | [English](https://github.com/taishi-i/awesome-japanese-nlp-slides/blob/main/docs/README.en.md)

日本語の自然言語処理（NLP）に関する発表スライドを集めたキュレーションリストです。
学会チュートリアル、大学講義、OSS 開発者による技術解説、企業の実践事例などをトピック別に整理しています。

216 件の資料を 18 カテゴリに分類しています。

> [!NOTE]
> このリストは現在構築途中です。今後も資料を追加し、内容を拡張していきます。

## 🔍 Claude Code から検索する

このリストの資料 216 件を Claude Code から検索できるプラグインを用意しています。

```
/plugin marketplace add taishi-i/awesome-japanese-nlp-slides
/plugin install awesome-japanese-nlp-slides@awesome-japanese-nlp-slides
```

インストール後、`search` スキルにキーワードや自然文を渡すと、関連度順に最大 10 件と読む順の提案が返ります。

```
/awesome-japanese-nlp-slides:search 形態素解析
/awesome-japanese-nlp-slides:search 日本語LLMの事前学習
/awesome-japanese-nlp-slides:search RAG
/awesome-japanese-nlp-slides:search evaluation benchmark
```

> [!TIP]
> 日本語・英語のどちらでも検索できます。出力の言語はクエリの言語に合わせます。
> 「入門から順に読みたい」のように自然文で聞くと、読む順の提案も返ります。

## 目次

- [入門・全体像](#入門全体像)
- [学会チュートリアル](#学会チュートリアル)
- [大学講義・体系的な講義資料](#大学講義体系的な講義資料)
- [日本語の基礎解析（形態素解析・構文解析）](#日本語の基礎解析形態素解析構文解析)
- [単語・文の分散表現](#単語文の分散表現)
- [事前学習モデル・Transformer](#事前学習モデルtransformer)
- [大規模言語モデル（概論・動向）](#大規模言語モデル概論動向)
- [日本語LLMの開発（事前学習・コーパス構築）](#日本語llmの開発事前学習コーパス構築)
- [ファインチューニング・事後学習](#ファインチューニング事後学習)
- [評価・ベンチマーク](#評価ベンチマーク)
- [検索・RAG](#検索rag)
- [LLM アプリケーション開発・運用](#llm-アプリケーション開発運用)
- [情報抽出・固有表現・アノテーション](#情報抽出固有表現アノテーション)
- [質問応答・知識](#質問応答知識)
- [機械翻訳・音声・対話](#機械翻訳音声対話)
- [生成・要約・校正](#生成要約校正)
- [解釈性・分析・言語学的視点](#解釈性分析言語学的視点)
- [産業応用・実務事例](#産業応用実務事例)

## 入門・全体像

自然言語処理そのものを俯瞰したい人が最初に読む資料。

- [情報処理学会関西支部2024年度定期講演会「自然言語処理と大規模言語モデルの基礎」](https://speakerdeck.com/ksudoh/qing-bao-chu-li-xue-hui-guan-xi-zhi-bu-2024nian-du-ding-qi-jiang-yan-hui-zi-ran-yan-yu-chu-li-toda-gui-mo-yan-yu-moderunoji-chu) - Katsuhito Sudoh（2024-11）
- [ae-8. 自然言語処理（問答，要約，テキスト生成，単語の特徴ベクトル，単語の類似度）](https://www.docswell.com/s/6674398749/5M4Y2K-2023-01-29-132348) - kunihikokaneko（2023-01）
- [言葉の形を教えてくれる自然言語処理](https://speakerdeck.com/eumesy/natural-language-processing-tells-us-the-shape-of-language) - Sho Yokoi（2022-03）
- [深層学習による自然言語処理入門: word2vecからBERT, GPT-3まで](https://www.docswell.com/s/ydnjp/K3YMDZ-2021-07-21-152903) - Yahoo!デベロッパーネットワーク（2021-07）
- [実践！AllenNLPによるディープラーニングを用いた自然言語処理](https://speakerdeck.com/ikuyamada/shi-jian-allennlpniyorudeipuraninguwoyong-itazi-ran-yan-yu-chu-li) - Ikuya Yamada（2021-03）
- [最先端自然言語処理ライブラリの最適な選択と有用な利用方法 / pycon-jp-2020](https://speakerdeck.com/taishii/pycon-jp-2020) - taishi-i（2020-08）
- [Python による日本語自然言語処理 〜系列ラベリングによる実世界テキスト分析〜 / PyCon JP 2019](https://speakerdeck.com/taishii/pycon-jp-2019) - taishi-i（2019-09）
- [How Deep Learning Changes Natural Language Processing](https://speakerdeck.com/chokkan/how-deep-learning-changes-natural-language-processing) - Naoaki Okazaki（2018-09）

## 学会チュートリアル

言語処理学会・人工知能学会などのチュートリアル講演資料。

- [言語モデルの内部機序：解析と解釈](https://speakerdeck.com/eumesy/analysis_and_interpretation_of_language_models) - Sho Yokoi（2025-03）
- [最強DB講義 #35 大規模言語モデルに基づく検索モデル](https://speakerdeck.com/mpkato/zui-qiang-dbjiang-yi-number-35-da-gui-mo-yan-yu-moderuniji-dukujian-suo-moderu) - Makoto P. Kato（2024-11）
- [SSII2024 \[OS2\] 大規模言語モデルと基盤モデルの射程](https://speakerdeck.com/ssii/ssii2024-os2-otani) - 画像センシングシンポジウム（2024-06）
- [大規模言語モデルの開発](https://speakerdeck.com/chokkan/jsai2024-tutorial-llm) - Naoaki Okazaki（2024-05）
- [IBIS2023チュートリアル「大規模言語モデル活用技術の最前線」](https://speakerdeck.com/1never/ibis2023tiyutoriaru-da-gui-mo-yan-yu-moderuhuo-yong-ji-shu-nozui-qian-xian) - Michimasa Inaba（2023-10）
- [PAKDD2023 Tutorial 2: A Gentle Introduction to Technologies Behind Language Models and Recent Achievement in ChatGPT (Parts 3 and 4)](https://speakerdeck.com/kyoun/pakdd2023-tutorial) - Kyosuke Nishida（2023-05）
- [Part 5: Efforts for Responsible LLMs, PAKDD 2023 Tutorial 2: A Gentle Introduction to Technologies Behind Language Models and Recent Achievement in ChatGPT](https://speakerdeck.com/chokkan/efforts-for-responsible-llms-pakdd-2023-tutorial-2) - Naoaki Okazaki（2023-05）
- [NLPとVision-and-Languageの基礎・最新動向 (1) / DEIM Tutorial Part 1: NLP](https://speakerdeck.com/kyoun/deim-tutorial-part-1-nlp) - Kyosuke Nishida（2023-03）
- [NLPとVision-and-Languageの基礎・最新動向 (2) / DEIM Tutorial Part 2 Vision-and-Language](https://speakerdeck.com/kyoun/deim-tutorial-part-2-vision-and-language) - Kyosuke Nishida（2023-03）
- [自然言語処理とVision-and-Language / A Tutorial on NLP & Vision-and-Language](https://speakerdeck.com/kyoun/a-tutorial-on-nlp-and-vision-and-language) - Kyosuke Nishida（2022-06）
- [ゼロから始める転移学習](https://www.docswell.com/s/ydnjp/5L8XPZ-2022-04-27-133413) - Yahoo!デベロッパーネットワーク（2022-04）
- [最適輸送と自然言語処理](https://speakerdeck.com/eumesy/optimal-transport-for-natural-language-processing) - Sho Yokoi（2022-03）

## 大学講義・体系的な講義資料

大学の講義や、書籍の輪読会で使われた連続講義資料。

- [\[輪講\] Transformer（大規模言語モデル入門第２章）](https://speakerdeck.com/taro_nakasone/lun-jiang-transformer-da-gui-mo-yan-yu-moderuru-men-di-2zhang) - Taro Nakasone（2025-09）
- [2024Fall 大規模言語モデル(LLM)講座 Day9 : AI Safety ~ Hallucination ~ 講義資料](https://speakerdeck.com/tellterubouzu/matsuo-lab-llm-day9-hallucination-shimomura-241023) - 下村晃生（2024-10）
- [【大規模言語モデル入門】 1章](https://www.docswell.com/s/kyoto-kaira/5XEPV2-2024-10-10-215106) - 京都大学人工知能研究会KaiRA（2024-10）
- [ゼロから始める大規模言語モデル入門](https://speakerdeck.com/mathbullet/zerokarashi-meruda-gui-mo-yan-yu-moderuru-men) - 数理の弾丸（2024-05）
- [LLM Fine-Tuning (東大松尾研LLM講座 Day5資料)](https://speakerdeck.com/schulta/llm-fine-tuning-dong-da-song-wei-yan-llmjiang-zuo-day5zi-liao) - Shota Nakasuji（2023-09）
- [東京大学深層学習（Deep Learning基礎講座2022）深層学習と自然言語処理](https://speakerdeck.com/verypluming/dong-jing-da-xue-shen-ceng-xue-xi-deep-learningji-chu-jiang-zuo-2022-shen-ceng-xue-xi-tozi-ran-yan-yu-chu-li) - Hitomi Yanaka（2022-06）
- [nl-1. 形態素解析と構文解析](https://www.docswell.com/s/6674398749/ZNJ7E5-2021-12-16-141804) - kunihikokaneko（2021-12）
- [Word Embeddings](https://speakerdeck.com/chokkan/word-embeddings) - Naoaki Okazaki（2020-08）
- [Encoder Decoder Models](https://speakerdeck.com/chokkan/encoder-decoder-models) - Naoaki Okazaki（2020-08）
- [DNN for Structural Data](https://speakerdeck.com/chokkan/dnn-for-structural-data) - Naoaki Okazaki（2020-08）
- [Feedforward Neural Network (I): Binary Classification](https://speakerdeck.com/chokkan/feedforward-neural-network-i-binary-classification) - Naoaki Okazaki（2020-07）
- [Feedforward Neural Network (II): Multi-class Classification](https://speakerdeck.com/chokkan/feedforward-neural-network-ii-multi-class-classification) - Naoaki Okazaki（2020-07）
- [Convolutional Neural Network](https://speakerdeck.com/chokkan/convolutional-neural-network) - Naoaki Okazaki（2020-07）

## 日本語の基礎解析（形態素解析・構文解析）

日本語特有の前処理を担う解析器と辞書に関する資料。

- [係り受け解析を用いた法律文書中の略称規定の解析についての報告](https://speakerdeck.com/puripuri2100/xi-rishou-kejie-xi-woyong-itafa-lu-wen-shu-zhong-nolue-cheng-gui-ding-nojie-xi-nituitenobao-gao) - puripuri2100（2024-09）
- [Lucene/Elasticsearch の Character Filter でユニコード正規化するとトークンのオフセットがズレるバグへの Workaround - Search Engineering Tech Talk 2024 Spring](https://speakerdeck.com/kampersanda/elasticsearch-no-character-filter-deyunikodozheng-gui-hua-surutotokunnoohusetutogazurerubaguheno-workaround-search-engineering-tech-talk-2024-spring) - Shunsuke Kanda（2024-05）
- [\[NLP2023\] 最小コスト法に基づく形態素解析におけるCPU キャッシュの効率化](https://speakerdeck.com/legalontechnologies/nlp2023-vibrato) - LegalOn Technologies, Inc（2024-05）
- [\[DEIM2023\] 高速な形態素解析器Vibratoの紹介](https://speakerdeck.com/legalontechnologies/deim2023-introduction-to-vibrato-fast-morphological-analyzer) - LegalOn Technologies, Inc（2023-03）
- [KWJA：汎用言語モデルに基づく日本語解析器 / kyoto-waseda-japanese-analyzer](https://speakerdeck.com/nobug/kyoto-waseda-japanese-analyzer) - Nobuhiro Ueda（2022-09）
- [Sudachi Family近況報告 at WAP NLP Tech Talk #5](https://speakerdeck.com/waptech/sudachi-familyjin-kuang-bao-gao-at-wap-nlp-tech-talk-number-5) - WAP（2022-04）
- [オープンソースとしての形態素解析器Sudachi / WAP NLP Tech Talk #4](https://speakerdeck.com/sorami/wap-nlp-tech-talk-number-4) - Sorami Shiromizu（2021-11）
- [日本語形態素解析器 SudachiPy の 現状と今後について](https://speakerdeck.com/waptech/ri-ben-yu-xing-tai-su-jie-xi-qi-sudachipy-false-xian-zhuang-tojin-hou-nituite) - WAP（2021-07）
- [Sudachi辞書のつくり方](https://speakerdeck.com/waptech/sudachici-shu-falsetukurifang) - WAP（2020-12）
- [Lucene Kuromoji のコードを読む会 （辞書ビルダー編）](https://speakerdeck.com/mocobeta/lucene-kuromoji-nokodowodu-muhui-ci-shu-birudabian) - Tomoko Uchida（2019-10）
- [犬でもわかる Minimal Acyclic Subsequential Transducer / Introduction to Minimal Acyclic Subsequential Transducer](https://speakerdeck.com/takuyaa/introduction-to-minimal-acyclic-subsequential-transducer) - Takuya Asano（2019-06）
- [文字列正規化パタンの獲得と崩れ表記正規化に基づく日本語形態素解析](https://speakerdeck.com/atsumikan/wen-zi-lie-zheng-gui-hua-patanfalsehuo-de-tobeng-rebiao-ji-zheng-gui-hua-niji-dukuri-ben-yu-xing-tai-su-jie-xi) - Atsushi（2018-04）
- [JUMAN++で分かち書きをしたかった...](https://speakerdeck.com/nagomiso/juman-plus-plus-defen-katishu-kiwositakatuta-dot-dot-dot) - なごみそ（2017-05）
- [日本語の形態素解析](https://speakerdeck.com/yumeto/ri-ben-yu-falsexing-tai-su-jie-xi) - Yumeto Inaoka（2017-01）
- [Pythonで作って学ぶ形態素解析](https://speakerdeck.com/mocobeta/pythondezuo-tutexue-buxing-tai-su-jie-xi) - Tomoko Uchida（2015-10）

## 単語・文の分散表現

単語ベクトル、文埋め込み、埋め込み空間の性質に関する資料。

- [Zipf 白色化：タイプとトークンの区別がもたらす良質な埋め込み空間と損失関数](https://speakerdeck.com/eumesy/zipfian-whitening) - Sho Yokoi（2024-11）
- [NLP2024 招待論文セッション: 定義文を用いた文埋め込み構成法](https://speakerdeck.com/hpprc/nlp2024-zhao-dai-lun-wen-setusiyon-ding-yi-wen-woyong-itawen-mai-meip-migou-cheng-fa) - Hayato Tsukagoshi（2024-09）
- [\[輪講資料\] Matryoshka Representation Learning](https://speakerdeck.com/hpprc/lun-jiang-zi-liao-matryoshka-representation-learning) - Hayato Tsukagoshi（2024-08）
- [\[輪講資料\] Text Embeddings by Weakly-Supervised Contrastive Pre-training](https://speakerdeck.com/hpprc/lun-jiang-zi-liao-text-embeddings-by-weakly-supervised-contrastive-pre-training) - Hayato Tsukagoshi（2024-05）
- [意味変化分析に向けた単語埋め込みの時系列パターン分析](https://speakerdeck.com/rudorudo11/yi-wei-bian-hua-fen-xi-nixiang-ketadan-yu-mai-meip-minoshi-xi-lie-patanfen-xi) - hajime kiyama（2024-03）
- [\[輪講資料\] One Embedder, Any Task: Instruction-Finetuned Text Embeddings](https://speakerdeck.com/hpprc/one-embedder-any-task-instruction-finetuned-text-embeddings) - Hayato Tsukagoshi（2023-12）
- [埋め込み表現の意味適応による知識ベース語義曖昧性解消](https://speakerdeck.com/s_mizuki_nlp/mai-meip-mibiao-xian-noyi-wei-shi-ying-niyoruzhi-shi-besuyu-yi-ai-mei-xing-jie-xiao) - S（2023-05）
- [単語分散表現 chiVeの活用方法 at WAP NLP Tech Talk #5](https://speakerdeck.com/waptech/dan-yu-fen-san-biao-xian-chivefalsehuo-yong-fang-fa-at-wap-nlp-tech-talk-number-5) - WAP（2022-04）
- [事前学習モデル chiTra の活用方法 at WAP NLP Tech Talk #5](https://speakerdeck.com/waptech/shi-qian-xue-xi-moderu-chitra-falsehuo-yong-fang-fa-at-wap-nlp-tech-talk-number-5) - WAP（2022-04）
- [単語分散表現と事前学習モデル - chiVe \_ chiTra 利活用のための下準備 at WAP NLP Tech Talk #5](https://speakerdeck.com/waptech/dan-yu-fen-san-biao-xian-toshi-qian-xue-xi-moderu-chive-chitra-li-huo-yong-falsetamefalsexia-zhun-bei-at-wap-nlp-tech-talk-number-5) - WAP（2022-04）
- [chiVe: 製品利用可能な日本語単語ベクトル資源の実現へ向けて](https://speakerdeck.com/sorami/chive-zhi-pin-li-yong-ke-neng-nari-ben-yu-dan-yu-bekutoruzi-yuan-falseshi-xian-hexiang-kete) - Sorami Shiromizu（2020-09）
- [双曲空間への単語埋め込みと QAサービスでの自然言語処理を 用いた推薦システムについて](https://speakerdeck.com/ryusuketa/shuang-qu-kong-jian-hefalsedan-yu-mai-meip-mito-qasabisudefalsezi-ran-yan-yu-chu-li-wo-yong-itatui-jian-sisutemunituite) - Ryusuke_Tanaka（2019-04）
- [トピックモデルによる分散表現獲得手法の提案](https://speakerdeck.com/nzw0301/topitukumoderuniyorufen-san-biao-xian-huo-de-shou-fa-falseti-an) - Kento Nozawa（2016-03）
- [分散表現に基づく文書要約#yjdsw1](https://www.docswell.com/s/ydnjp/ZXVYMK-2015-12-21-134350) - Yahoo!デベロッパーネットワーク（2015-12）

## 事前学習モデル・Transformer

BERT 以降の事前学習モデルと Transformer の解説資料。

- [【初心者向け】まだ間に合う！ Hugging Face入門 -TransformersでAI推論&学習](https://speakerdeck.com/tkhresk/huggingfaceru-men) - Takahiro Esaki（2023-09）
- [Transformersによる自然言語処理の実践](https://www.docswell.com/s/flowlight0/5RX82N-2023-08-22-152738) - flowlight0（2023-08）
- [BERTによる自然言語処理を学ぼう!【 Live!人工知能 #26】 #Live人工知能](https://speakerdeck.com/yukinaga/bertniyoruzi-ran-yan-yu-chu-li-woxue-bou-live-ren-gong-zhi-neng-number-26-number-liveren-gong-zhi-neng) - yuky_az（2020-11）
- [事前学習済言語モデルの動向 (2) / Survey of Pretrained Language Models](https://speakerdeck.com/kyoun/survey-of-pretrained-language-models-f6319c84-a3bc-42ed-b7b9-05e2588b12c7) - Kyosuke Nishida（2020-02）
- [事前学習言語モデルの動向 / Survey of Pretrained Language Models](https://speakerdeck.com/kyoun/survey-of-pretrained-language-models) - Kyosuke Nishida（2019-11）
- [\[DL輪読会\]BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://www.docswell.com/s/DeepLearning2023/5Q8L7R-dlbert-pretraining-of-deep-bidirectional-transformers-for-language-understanding) - Deep Learning JP（2018-10）

## 大規模言語モデル（概論・動向）

LLM 全体を俯瞰する解説・招待講演。

- [AIはどのように考えて話すのか？ ― 言葉と知能の不思議](https://speakerdeck.com/chokkan/how-ai-thinks-and-responds) - Naoaki Okazaki（2026-07）
- [大規模言語モデル（LLM)について人文学研究者が知っておきたいこと](https://speakerdeck.com/yhkondo/da-gui-mo-yan-yu-moderu-llm-nituiteren-wen-xue-yan-jiu-zhe-gazhi-tuteokitaikoto) - Yasuhiro Kondo（2025-05）
- [大規模言語モデルとそのソフトウェア開発に向けた応用 (2024年版)](https://speakerdeck.com/kazato/da-gui-mo-yan-yu-moderutosonosohutoueakai-fa-nixiang-ketaying-yong-2024nian-ban) - Hiroshi Kazato（2024-12）
- [大規模言語モデル (LLM) の技術と最新動向](https://speakerdeck.com/ikuyamada/da-gui-mo-yan-yu-moderu-llm-noji-shu-tozui-xin-dong-xiang) - Ikuya Yamada（2024-06）
- [大規模言語モデルのインパクトと課題/oc2023](https://speakerdeck.com/mamoruk/oc2023-5b5c720d-f963-430e-b4a1-ab4b2df45b1b) - Mamoru Komachi（2024-05）
- [大規模言語モデルを作る、拡張する](https://speakerdeck.com/stillpedant/building-llm) - Masafumi Oyamada（2024-02）
- [大規模言語モデル入門 / LLM introduction (SES2023)](https://speakerdeck.com/kyoun/llm-introduction-ses2023) - Kyosuke Nishida（2023-08）
- [大規模言語モデルの驚異と脅威](https://speakerdeck.com/chokkan/20230327_riken_llm) - Naoaki Okazaki（2023-03）

## 日本語LLMの開発（事前学習・コーパス構築）

日本語 LLM を実際に構築した現場からの知見。

- [国産生成AI PLaMoを支える事後学習と推論最適化](https://speakerdeck.com/pfn/20260406_plamo_3_beta_posttrain_and_inference_opt) - Preferred Networks（2026-04）
- [2024-02-Tokyo-Tech-大規模言語モデルの事前学習知見](https://speakerdeck.com/fujiikazuki2000/2024-02-tokyo-tech-da-gui-mo-yan-yu-moderunoshi-qian-xue-xi-zhi-jian) - Kazuki Fujii（2025-12）
- [言語処理学会2024-継続事前学習による日本語に強い大規模言語モデルの構築](https://speakerdeck.com/fujiikazuki2000/yan-yu-chu-li-xue-hui-2024-ji-sok-shi-qian-xue-xi-niyoruri-ben-yu-niqiang-ida-gui-mo-yan-yu-moderunogou-zhu) - Kazuki Fujii（2025-12）
- [情報処理学会-全国大会2024-大規模言語モデルの分散並列学習](https://speakerdeck.com/fujiikazuki2000/qing-bao-chu-li-xue-hui-quan-guo-da-hui-2024-da-gui-mo-yan-yu-moderunofen-san-bing-lie-xue-xi) - Kazuki Fujii（2025-12）
- [AWS Summit Japan 2025 Amazon SageMaker HyperPodを利用した日本語LLM(Swallow)の構築 (CUS-02)](https://speakerdeck.com/fujiikazuki2000/aws-summit-japan-2025-amazon-sagemaker-hyperpodwoli-yong-sitari-ben-yu-llm-swallow-nogou-zhu-cus-02) - Kazuki Fujii（2025-12）
- [合成データパイプラインを利用したSwallowProjectに おけるLLM性能向上](https://speakerdeck.com/fujiikazuki2000/he-cheng-detapaipurainwoli-yong-sitaswallowprojectni-okerullmxing-neng-xiang-shang) - Kazuki Fujii（2025-08）
- [論文では語られないLLM開発において重要なこと Swallow Projectを通して](https://speakerdeck.com/fujiikazuki2000/lun-wen-dehayu-rarenaillmkai-fa-nioitezhong-yao-nakoto-swallow-projectwotong-site) - Kazuki Fujii（2025-07）
- [Swallowコーパスv2: 教育的な日本語ウェブコーパスの構築（NLP2025）](https://speakerdeck.com/aya_se/swallowkopasuv2-jiao-yu-de-nari-ben-yu-uebukopasunogou-zhu-nlp2025) - Kakeru Hattori（2025-03）
- [新聞記事からつくる 時事と社会に強い日本語LLM（NLP2025）](https://speakerdeck.com/aya_se/xin-wen-ji-shi-karatukuru-shi-shi-toshe-hui-niqiang-iri-ben-yu-llm-nlp2025) - Kakeru Hattori（2025-03）
- [LLMの事前学習のためのテキストデータの収集と構築](https://speakerdeck.com/butsugiri/llmnoshi-qian-xue-xi-notamenotekisutodetanoshou-ji-togou-zhu) - Shun Kiyono（2025-02）
- [PLaMo-100B-Instruct 国産大規模言語モデル構築における事後学習の取り組み](https://speakerdeck.com/pfn/plamo-100b-instruct-guo-chan-da-gui-mo-yan-yu-moderugou-zhu-niokerushi-hou-xue-xi-noqu-rizu-mi) - Preferred Networks（2024-12）
- [大規模言語モデル Tanuki-8x8Bの紹介と開発経緯など](https://www.docswell.com/s/KanHatakeyama/5YDDJE-2024-09-18-214202) - Kan Hatakeyama（2024-09）
- [LLMに日本語テキストを学習させる意義](https://speakerdeck.com/ksaito/llmniri-ben-yu-tekisutowoxue-xi-saseruyi-yi) - Koshiro Saito（2024-08）
- [Building an Effective Pre-training Corpus for Japanese LLM (TAI AAI #3)](https://speakerdeck.com/aya_se/building-an-effective-pre-training-corpus-for-japanese-llm-tai-aai-number-3) - Kakeru Hattori（2024-08）
- [大規模言語モデル (LLM)における低精度数値表現](https://speakerdeck.com/pfn/20240508-hpckenkyukai-pfn-llm) - Preferred Networks（2024-05）
- [大規模言語モデル開発の進捗まとめ(◯データ整備・△事前学習・△ファインチューニング)](https://www.docswell.com/s/KanHatakeyama/ZYW393-2024-04-08-112244) - Kan Hatakeyama（2024-04）
- [ICHIKARA-INSTRUCTION LLMのための日本語インストラクションの構築と 人間とGPT-4による評価で観察されたもの](https://speakerdeck.com/olachinkei/ichikara-instruction-llmnotamenori-ben-yu-insutorakusiyonnogou-zhu-to-ren-jian-togpt-4niyoruping-jia-deguan-cha-saretamono) - Keisuke Kamata（2024-03）
- [大規模言語モデル開発のための日本語 Instruction データセット作成の取り組み](https://speakerdeck.com/kunishou/da-gui-mo-yan-yu-moderukai-fa-notamenori-ben-yu-instruction-detasetutozuo-cheng-noqu-rizu-mi) - Shouhei Kuniyoshi（2024-03）
- [自然言語処理のための分散並列学習](https://speakerdeck.com/fujiikazuki2000/zi-ran-yan-yu-chu-li-notamenofen-san-bing-lie-xue-xi-3dd9cdf8-cc6d-4350-8141-89ce35b9d273) - Kazuki Fujii（2024-03）
- [言語間転移学習で大規模言語モデルを賢くする](https://speakerdeck.com/ikuyamada/yan-yu-jian-zhuan-yi-xue-xi-deda-gui-mo-yan-yu-moderuwoxian-kusuru) - Ikuya Yamada（2024-03）
- [東工大Swallowプロジェクトにおける大規模日本語Webコーパスの構築](https://speakerdeck.com/aya_se/data-centric-ai-swallow-corpus-56e2869a-f9bd-46cb-b030-1012235c37f7) - Kakeru Hattori（2024-02）

## ファインチューニング・事後学習

既存モデルを目的に合わせて調整する手法。

- [Go言語での実装を通して学ぶLLMファインチューニングの仕組み / fukuokago22-llm-peft](https://speakerdeck.com/monochromegane/fukuokago22-llm-peft) - monochromegane（2025-08）
- [論文読み会 SNLP2025 Learning Dynamics of LLM Finetuning. In: ICLR 2025](https://speakerdeck.com/s_mizuki_nlp/lun-wen-du-mihui-snlp2025-learning-dynamics-of-llm-finetuning-in-iclr-2025) - S（2025-08）
- [帳票構造化タスクにおけるLLMファインチューニングの性能評価](https://speakerdeck.com/yosukeyoshida/zhang-piao-gou-zao-hua-tasukuniokerullmhuaintiyuningunoxing-neng-ping-jia) - yosukeyoshida（2025-07）
- [ローカルLLMでファインチューニング](https://speakerdeck.com/knishioka/rokarullmdehuaintiyuningu) - 西岡 賢一郎 (Kenichiro Nishioka)（2025-06）
- [第13回 Data-Centric AI勉強会, LLMのファインチューニングデータ](https://speakerdeck.com/kajyuuen/di-13hui-data-centric-aimian-qiang-hui-llmnohuaintiyuningudeta) - Koga Kobayashi（2025-02）
- [LLMアプリケーションの Fine-tunningと蒸留を活用した改善](https://speakerdeck.com/pharma_x_tech/llmahurikesiyonno-fine-tunningtozheng-liu-wohuo-yong-sitagai-shan) - PharmaX（旧YOJO Technologies）開発チーム（2024-12）
- [\[輪講資料\] LoRA: Low-Rank Adaptation of Large Language Models](https://speakerdeck.com/hpprc/lun-jiang-zi-liao-lora-low-rank-adaptation-of-large-language-models) - Hayato Tsukagoshi（2023-04）

## 評価・ベンチマーク

日本語 LLM・NLP システムをどう測るか。

- [HAKARI-Bench - 実運用視点での情報検索モデル評価ベンチマーク](https://speakerdeck.com/hotchpotch/hakari-bench-shi-yun-yong-shi-dian-denoqing-bao-jian-suo-moderuping-jia-bentimaku) - Yuichi Tateno（2026-07）
- [医療 LLM ベンチマークの現在地：多面的評価 と日本ローカライズ](https://speakerdeck.com/analokmaus/yi-liao-llm-bentimakunoxian-zai-di-duo-mian-de-ping-jia-tori-ben-rokaraizu) - Hiroshi Y (RabotniKuma)（2026-06）
- [Japanese SimpleQA: 日本語における事実に基づいた回答能力の評価ベンチマーク](https://speakerdeck.com/pfn/20251216_japanese_simpleqa) - Preferred Networks（2025-12）
- [進化する大規模言語モデル評価: Swallowプロジェクトにおける実践と知見](https://speakerdeck.com/chokkan/swallow-evaluation-instruct-wandb-fullyconnected2025) - Naoaki Okazaki（2025-10）
- [J-RAGBench: 日本語RAGにおける Generator評価ベンチマークの構築](https://speakerdeck.com/koki_itai/j-ragbench-ri-ben-yu-ragniokeru-generatorping-jia-bentimakunogou-zhu) - Koki Itai（2025-09）
- [日本語が話せるオープンアクセス大規模言語モデルの評価](https://speakerdeck.com/nssv/ri-ben-yu-gahua-seruopunakusesuda-gui-mo-yan-yu-moderunoping-jia) - ノーザンシステムサービス | Northern System Services（2024-11）
- [日本語医療LLM評価ベンチマークの構築と性能分析](https://speakerdeck.com/fta98/ri-ben-yu-yi-liao-llmping-jia-bentimakunogou-zhu-toxing-neng-fen-xi) - Takuya Fukushima（2024-09）
- [JMED-LLM: 日本語医療LLM評価データセットの公開](https://speakerdeck.com/fta98/jmed-llm-ri-ben-yu-yi-liao-llmping-jia-detasetutonogong-kai) - Takuya Fukushima（2024-07）
- [Nejumi Leaderboard release 20240702](https://speakerdeck.com/olachinkei/nejumi-leaderboard-release-20240702) - Keisuke Kamata（2024-07）
- [LCTG Bench 日本語LLMの制御性ベンチマークの紹介](https://speakerdeck.com/olachinkei/lctg-bench-ri-ben-yu-llmnozhi-yu-xing-bentimakunoshao-jie) - Keisuke Kamata（2024-07）
- [Japanese\_MT-Bench\_を使った\_LLM\_モデルの評価](https://speakerdeck.com/olachinkei/japanese-mt-bench-woshi-tuta-llm-moterunoping-jia) - Keisuke Kamata（2024-01）
- [Jasterデータセットを使ったLLMモデルの評価](https://speakerdeck.com/olachinkei/jastertetasetutowoshi-tutallmmoterunoping-jia) - Keisuke Kamata（2024-01）
- [JGLUEの構築そして 日本語LLM評価のこれから](https://speakerdeck.com/olachinkei/jgluenogou-zhu-sosite-ri-ben-yu-llmping-jia-nokorekara) - Keisuke Kamata（2023-11）
- [llm-jp-eval 日本語大規模言語モデルの 自動評価ツールの開発に向けて](https://speakerdeck.com/olachinkei/llm-jp-eval-ri-ben-yu-da-gui-mo-yan-yu-moteruno-zi-dong-ping-jia-turunokai-fa-nixiang-kete) - Keisuke Kamata（2023-11）

## 検索・RAG

情報検索、ベクトル検索、検索拡張生成。

- [【Paper&Hacks Vol.89】RAGアプリハンズオン～LLM/Embedding選択～](https://www.docswell.com/s/matsuo-lab_llm/Z8NRJE-Paper&HacksVol.89) - 松尾研LLMコミュニティ（2026-08）
- [【Paper&Hacks Vol.80】RAGを測るモノサシを作ろう 〜 Ragas × LangSmithでRAG評価アプリ開発 〜](https://www.docswell.com/s/matsuo-lab_llm/KWRGP8-Paper&HacksVol.80) - 松尾研LLMコミュニティ（2026-08）
- [Retriever と Reranker、結局どうする？](https://speakerdeck.com/kazuaki/retriever-to-reranker-jie-ju-dousuru) - hkazuakey（2026-07）
- [AIエージェントのための検索](https://speakerdeck.com/takatorisatoshi/aiezientonotamenojian-suo) - takatori（2026-07）
- [【2026年版】 ベクトル検索とEmbedding最前線](https://speakerdeck.com/mocobeta/2026nian-ban-bekutorujian-suo-embeddingzui-qian-xian) - Tomoko Uchida（2026-06）
- [FessのAI検索モード：検索システムとLLMへの取り組み](https://speakerdeck.com/marevol/fessnoaijian-suo-modo-jian-suo-sisutemutollmhenoqu-rizu-mi) - Shinsuke Sugaya（2026-04）
- [検索設計から 推論設計への重心移動と Recall-First Retrieval](https://speakerdeck.com/po3rin/jian-suo-she-ji-kara-tui-lun-she-ji-henozhong-xin-yi-dong-to-recall-first-retrieval) - po3rin（2026-04）
- [MCPでつなぐElasticsearchとLLM - 深夜の障害対応を楽にしたい / Bridging Elasticsearch and LLMs with MCP](https://speakerdeck.com/sashimimochi/bridging-elasticsearch-and-llms-with-mcp) - Sashimimochi（2026-01）
- [オープンウェイトのLLMリランカーを契約書で評価する / searchtechjp](https://speakerdeck.com/sansan_randd/searchtechjp) - Sansan R&D（2026-01）
- [2026年はチャンキングを極める！](https://speakerdeck.com/shibuiwilliam/2026nian-hatiyankinguwoji-meru) - shibuiwilliam（2026-01）
- [Pythonで構築する全国市町村ナレッジグラフ: GraphRAGを用いた意味的地域検索への応用](https://speakerdeck.com/negi111111/pythondegou-zhu-suruquan-guo-shi-ting-cun-naretuzigurahu-graphragwoyong-itayi-wei-de-di-yu-jian-suo-henoying-yong) - negi111111（2025-11）
- [OpenProvence - クエリに関連しない文章削除モデル日本語版の作成と公開](https://speakerdeck.com/hotchpotch/openprovence-kueriniguan-lian-sinaiwen-zhang-xue-chu-moderuri-ben-yu-ban-nozuo-cheng-togong-kai) - Yuichi Tateno（2025-10）
- [Azure AI SearchでAgentic Retreival](https://speakerdeck.com/takatorisatoshi/azure-ai-searchdeagentic-retreival) - takatori（2025-10）
- [Temporal Knowledge Graphで作る！ 時間変化するナレッジを扱うAI Agentの世界](https://speakerdeck.com/po3rin/temporal-knowledge-graphdezuo-ru-shi-jian-bian-hua-surunaretuziwoxi-uai-agentnoshi-jie) - po3rin（2025-10）
- [実践マルチモーダル検索！](https://speakerdeck.com/shibuiwilliam/shi-jian-marutimodarujian-suo) - shibuiwilliam（2025-10）
- [「LINE MUSIC」におけるハイブリッド検索や略称抽出を用いた曖昧検索への挑戦 / Challenges in Ambiguous Search Using Hybrid Search and Abbreviation Extraction in "LINE MUSIC"](https://speakerdeck.com/lycorptech_jp/challenges-in-ambiguous-search-using-hybrid-search-and-abbreviation-extraction-in-line-music) - LINEヤフーTech (LY Corporation Tech)（2025-06）
- [ベクトルストア入門](https://www.docswell.com/s/hmatsu47/ZP2LY6-2025-01-19-235645) - hmatsu47(まつ)（2025-02）
- [LLMによるRAG評価用合成テストデータの生成](https://speakerdeck.com/licux/llmniyoruragping-jia-yong-he-cheng-tesutodetanosheng-cheng) - matsukada（2025-01）
- [LLMアプリをRagasで評価して、Langfuseで可視化しよう！](https://speakerdeck.com/minorun365/llmapuriworagasdeping-jia-site-langfusedeke-shi-hua-siyou) - みのるん（2024-10）
- [テキスト検索の原点：全文検索のしくみと活用ポイント](https://speakerdeck.com/segavvy/tekisutojian-suo-noyuan-dian-quan-wen-jian-suo-nosikumitohuo-yong-hointo) - segavvy（2024-01）
- [言語モデルを用いたQuery Categorizationへの取り組み / LM-based query categorization for query understanding](https://speakerdeck.com/pakio/lm-based-query-categorization-for-query-understanding) - Kazuma Arimura（2023-12）
- [ヤフーにおける機械学習検索ランキングの取り組み](https://speakerdeck.com/szdr/yahuniokeruji-jie-xue-xi-jian-suo-rankingufalsequ-rizu-mi) - sz_dr（2019-12）
- [Elasticsearch における類似度ベクトル検索のベストプラクティスを求めて/es-vector-search](https://speakerdeck.com/takahiko03/es-vector-search) - Takahiko Ito（2019-07）

## LLM アプリケーション開発・運用

プロダクトとして LLM を組み込み、運用するための知見。

- [LangfuseによるLLMOps基盤の構築と活用事例](https://speakerdeck.com/zozotech/llmops-platform-with-langfuse) - ZOZO Developers（2026-07）
- [複数プロダクト利用を前提としたセルフホストLangfuse導入事例 / shibuya\_AI\_4](https://speakerdeck.com/sansan_randd/shibuya-ai-4) - Sansan R&D（2026-02）
- [LLMアプリケーションの品質担保に向けた プラクティスと LLMオブザーバビリティツール](https://speakerdeck.com/olachinkei/llmapurikesiyonnopin-zhi-dan-bao-nixiang-keta-purakuteisuto-llmobuzababiriteituru) - Keisuke Kamata（2025-04）
- [AOAI Dev Day LLMシステム開発 Tips集](https://speakerdeck.com/hirosatogamo/aoai-dev-day-llmsisutemukai-fa-tipsji) - Hirosato Gamo（2024-07）
- [LangSmith入門―トレース／評価／プロンプト管理などを担うLLMアプリ開発プラットフォーム](https://speakerdeck.com/os1ma/langsmithru-men-toresu-slash-ping-jia-slash-puronputoguan-li-nadowodan-ullmapurikai-fa-puratutohuomu) - os1ma（2024-04）
- [いまこそ学ぶLLMベースのAIエージェント入門―基本的なしくみ／開発ツール／有名なOSSや論文の紹介](https://speakerdeck.com/os1ma/imakosoxue-bullmbesunoaiezientoru-men-ji-ben-de-nasikumi-slash-kai-fa-turu-slash-you-ming-naossyalun-wen-noshao-jie) - os1ma（2024-02）
- [LLM研究会\_社外公開版\_プロンプトを改善する15のヒント](https://speakerdeck.com/chiami_kayama/llmyan-jiu-hui-she-wai-gong-kai-ban-puronputowogai-shan-suru15nohinto) - C.Kayama（2023-10）
- [ChatGPT - LLMシステム開発大全](https://speakerdeck.com/hirosatogamo/chatgpt-azure-openai-da-quan) - Hirosato Gamo（2023-07）
- [プロンプトエンジニアリングから始めるLangChain入門](https://speakerdeck.com/os1ma/puronputoenziniaringukarashi-merulangchainru-men) - os1ma（2023-04）

## 情報抽出・固有表現・アノテーション

テキストから構造化情報を取り出す技術と、その学習データ。

- [BizDocVQA: 実世界ビジネス帳票に対する根拠付きVQAデータセットの提案](https://speakerdeck.com/icoxfog417/biz-doc-vqa-dataset) - Takahiro Kubo（2026-03）
- [メールから送信者情報を抽出するタスクの奥深さ / kyoto\_ai\_meetup\_1](https://speakerdeck.com/sansan_randd/kyoto-ai-meetup-1) - Sansan R&D（2026-02）
- [アノテーション作業書作成のGood Practice](https://speakerdeck.com/cierpa0905/anotesiyonzuo-ye-shu-zuo-cheng-nogood-practice) - Cierpa & Company（2025-10）
- [Large Vision Language Modelを用いた 文書画像データ化作業自動化の検証、運用 / shibuya\_AI](https://speakerdeck.com/sansan_randd/shibuya-ai) - Sansan R&D（2025-10）
- [AIの血肉となるアノテーションデータのために大事にしている事](https://speakerdeck.com/cyberagentdevelopers/ainoxie-rou-tonaruanotesiyondetanotamenida-shi-nisiteirushi) - CyberAgent（2024-11）
- [メールからの名刺情報抽出におけるLLM活用 / Use of LLM in extracting business card information from e-mails](https://speakerdeck.com/sansan_randd/use-of-llm-in-extracting-business-card-information-from-e-mails) - Sansan R&D（2024-11）
- [日本語エンティティリンキングのための行政機関ウェブ文書コーパスの構築 (CADEL)](https://speakerdeck.com/shigashiyama/cadel-at-ipsj-nl-260) - shigashiyama（2024-06）
- [ストックマークテックミートアップ#8 / Stockmark Tech MeetUp#8](https://speakerdeck.com/stockmark/stockmark-tech-meetup-number-8) - Stockmark（2024-02）
- [場所参照表現と位置情報を紐付けるジオコーディングの概観と発展に向けての考察 / 言語処理学会第29回年次大会(NLP2023)](https://speakerdeck.com/sorami/nlp2023) - Sorami Shiromizu（2023-03）
- [完全なアノテーションが得られない状況下での固有表現抽出](https://speakerdeck.com/kajyuuen/wan-quan-naafalsetesiyongade-rarenaizhuang-kuang-xia-defalsegu-you-biao-xian-chou-chu) - Koga Kobayashi（2019-09）
- [言語処理学会年次大会(NLP2019) F1-1 ウェブ検索クエリに対する周辺語を考慮した教師なしエンティティリンキング #nlp2019](https://www.docswell.com/s/ydnjp/5D7YDK-2019-03-18-150155) - Yahoo!デベロッパーネットワーク（2019-03）
- [専門用語抽出手法の研究と 抽出アプリケーションの開発](https://speakerdeck.com/kajyuuen/zhuan-men-yong-yu-chou-chu-shou-fa-falseyan-jiu-to-chou-chu-apurikesiyonfalsekai-fa) - Koga Kobayashi（2018-09）
- [述語項構造と照応関係のアノテーション](https://speakerdeck.com/kakubari/shu-yu-xiang-gou-zao-tozhao-ying-guan-xi-falseafalsetesiyon) - kakubari（2017-05）

## 質問応答・知識

知識を扱う言語モデルと質問応答システム。

- [知識強化言語モデルLUKE @ LUKEミートアップ](https://speakerdeck.com/ikuyamada/zhi-shi-qiang-hua-yan-yu-moderuluke-at-lukemitoatupu) - Ikuya Yamada（2025-01）
- [知識拡張型言語モデルLUKE](https://speakerdeck.com/ikuyamada/zhi-shi-kuo-zhang-xing-yan-yu-moderuluke) - Ikuya Yamada（2023-03）
- [最先端の質問応答技術の研究開発と迅速な実用化ーStudio Ousiaでの取り組みー](https://speakerdeck.com/ikuyamada/zui-xian-duan-nozhi-wen-ying-da-ji-shu-noyan-jiu-kai-fa-toxun-su-nashi-yong-hua-studio-ousiadenoqu-rizu-mi) - Ikuya Yamada（2023-03）
- [Efficient Passage Retrieval with Hashing for Open-domain Question Answering (ACL 2021)](https://speakerdeck.com/ikuyamada/efficient-passage-retrieval-with-hashing-for-open-domain-question-answering-acl-2021) - Ikuya Yamada（2022-05）
- [AutoGluon-Tabular を用いたアンサンブルによる日本語質問応答システムの構築 / AIO solution by AutoGluon-Tabular](https://speakerdeck.com/upura/aio-solution-by-autogluon-tabular) - Shotaro Ishihara（2021-03）
- [オープンドメイン質問応答技術の最新動向](https://speakerdeck.com/ikuyamada/opundomeinzhi-wen-ying-da-ji-shu-falsezui-xin-dong-xiang) - Ikuya Yamada（2021-03）
- [知識ベースの自然言語処理への活用](https://speakerdeck.com/ikuyamada/zhi-shi-besufalsezi-ran-yan-yu-chu-li-hefalsehuo-yong) - Ikuya Yamada（2021-03）

## 機械翻訳・音声・対話

翻訳、音声言語処理、対話システム。

- [古典日本語の現代語機械翻訳のための評価資源の整備](https://speakerdeck.com/shigashiyama/20260318-aamt) - shigashiyama（2026-03）
- [RAGで制御可能なFull-duplex音声対話システム](https://speakerdeck.com/mssmkmr/ragdezhi-yu-ke-neng-nafull-duplexyin-sheng-dui-hua-sisutemu) - Convergence Lab.（2025-11）
- [実運用で学んだ 音声対話システムの評価とテスト](https://speakerdeck.com/ymachida/shi-yun-yong-dexue-nda-yin-sheng-dui-hua-sisutemunoping-jia-totesuto) - Yuichiro Machida（2025-11）
- [自動同時音声翻訳技術の進展とこれからの展望（九州大学アジアウィーク2025 Webセミナー）](https://speakerdeck.com/ksudoh/zi-dong-tong-shi-yin-sheng-fan-yi-ji-shu-nojin-zhan-tokorekaranozhan-wang-jiu-zhou-da-xue-aziauiku2025-websemina) - Katsuhito Sudoh（2025-11）
- [PLaMo翻訳 〜もう不自然な機械翻訳とはサヨナラ!PLaMo翻訳が変革するビジネス〜](https://speakerdeck.com/pfn/20251014-plamo-translate-ceatec2025) - Preferred Networks（2025-10）
- [【輪講資料】Moshi: a speech-text foundation model for real-time dialogue](https://speakerdeck.com/hpprc/lun-jiang-zi-liao-moshi-a-speech-text-foundation-model-for-real-time-dialogue) - Hayato Tsukagoshi（2025-07）
- [イラストで学ぶ音声認識 改訂第2版 12. 音声対話システム](https://www.docswell.com/s/MasahiroAraki/K9V38Y-2025-06-05-141640) - 荒木 雅弘（2025-06）
- [大規模言語モデル時代の機械翻訳の展望](https://speakerdeck.com/shigashiyama/20241108-cs-llmmt) - shigashiyama（2024-11）
- [武蔵大学 AIの社会浸透研究会 第3回公開セミナー 大規模言語モデルがもたらす対話システム技術の変革](https://speakerdeck.com/mnakano/wu-zang-da-xue-ainoshe-hui-jin-tou-yan-jiu-hui-di-3hui-gong-kai-semina-da-gui-mo-yan-yu-moderugamotarasudui-hua-sisutemuji-shu-nobian-ge) - Mikio Nakano（2024-06）
- [【SIG-SLP 141 招待講演】 IWSLT Evaluation Campaign: Simultaneous Speech Translation](https://speakerdeck.com/ksudoh/sig-slp-141-zhao-dai-jiang-yan-iwslt-evaluation-campaign-simultaneous-speech-translation) - Katsuhito Sudoh（2022-03）
- [EMNLP2015読み会：Effective Approaches to Attention-based Neural Machine Translation](https://speakerdeck.com/tkng/emnlp2015du-mihui-effective-approaches-to-attention-based-neural-machine-translation) - tkng（2015-10）

## 生成・要約・校正

テキスト生成とその応用タスク。

- [日本語ニュース記事要約支援に向けたドメイン特化事前学習済みモデルの構築と活用 / t5-news-summarization](https://speakerdeck.com/upura/t5-news-summarization) - Shotaro Ishihara（2025-03）
- [NLP2025 WS Shared Task 文法誤り訂正部門 ehiMetrick](https://speakerdeck.com/sugiyamaseiji/nlp2025-ws-shared-task-wen-fa-wu-riding-zheng-bu-men-ehimetrick) - 杉山誠治（Sugiyama Seiji）（2025-03）
- [大規模言語モデルを用いた意味分析による辞書記述への応用](https://speakerdeck.com/yhkondo/da-gui-mo-yan-yu-moderuwoyong-itayi-wei-fen-xi-niyoruci-shu-ji-shu-henoying-yong) - Yasuhiro Kondo（2023-11）
- [LLMによる日本語ニュース記事の平易化 / Japanese News Articles Simplification via Large Language Models](https://speakerdeck.com/asahimrdc/japanese-news-articles-simplification-via-large-language-models) - Media R&D Center, The Asahi Shimbun（2023-04）
- [実践：日本語文章生成 Transformers ライブラリで学ぶ実装の守破離 / Introduction of Japanese Text Generation with Transformers](https://speakerdeck.com/upura/introduction-of-japanese-text-generation-with-transformers) - Shotaro Ishihara（2022-10）
- [日本語文法誤り訂正における事前学習済みモデルを用いたデータ増強](https://speakerdeck.com/hideyoshikato/ri-ben-yu-wen-fa-wu-riding-zheng-niokerushi-qian-xue-xi-ji-mimoderuwoyong-itadetazeng-qiang) - hideyoshikato（2021-03）
- [日本語文法誤り訂正における誤り傾向を考慮した擬似誤り生成](https://speakerdeck.com/youichiro/ri-ben-yu-wen-fa-wu-riding-zheng-niokeruwu-riqing-xiang-wokao-lu-sitani-si-wu-risheng-cheng) - youichiro（2020-06）
- [文献紹介：正誤情報と文法誤りパターンを考慮した単語分散表現を用いた文法誤り検出](https://speakerdeck.com/a1da4/wen-xian-shao-jie-zheng-wu-qing-bao-towen-fa-wu-ripatanwokao-lu-sitadan-yu-fen-san-biao-xian-woyong-itawen-fa-wu-rijian-chu) - Taichi Aida（2019-01）

## 解釈性・分析・言語学的視点

モデルの中身を覗き、言語の観点から評価する。

- [大規模言語モデルは誰を覚えているか / Who Do Large Language Models Memorize?](https://speakerdeck.com/upura/who-do-large-language-models-memorize) - Shotaro Ishihara（2026-06）
- [その LLM 制御、本当に信頼できますか？ / Can We Reliably Control LLMs?](https://speakerdeck.com/shunk031/can-we-reliably-control-llms) - Shunsuke KITADA（2026-04）
- [言語モデルから言語について語る際に押さえておきたいこと](https://speakerdeck.com/eumesy/before-talking-about-language-via-language-models) - Sho Yokoi（2026-03）
- [日本語新聞記事を用いた大規模言語モデルの暗記定量化 / LLMC2025](https://speakerdeck.com/upura/llmc2025) - Shotaro Ishihara（2025-08）
- [Semantic Shift Stability: 学習コーパス内の単語の意味変化を用いた事前学習済みモデルの時系列性能劣化の監査](https://speakerdeck.com/upura/semantic-shift-stability) - Shotaro Ishihara（2025-03）
- [コーパスを丸呑みしたモデルから言語の何がわかるか](https://speakerdeck.com/eumesy/what-can-language-models-swallowing-corpora-tell-us-about-language) - Sho Yokoi（2025-03）
- [大規模言語モデルのバイアス](https://speakerdeck.com/yukinobaba/bias-in-llms) - Yukino Baba（2024-09）
- [「確率的なオウム」にできること、またそれがなぜできるのかについて](https://speakerdeck.com/eumesy/language-models-as-modern-version-of-the-use-theory-of-meaning) - Sho Yokoi（2024-07）
- [『源氏物語』の引き歌をベクトル検索によって検出する方法](https://speakerdeck.com/yhkondo/yuan-shi-wu-yu-noyin-kige-wobekutorujian-suo-niyotutejian-chu-surufang-fa) - Yasuhiro Kondo（2024-06）
- [大規模言語モデルの持つ言語知識とコミュニケーション](https://speakerdeck.com/yhkondo/da-gui-mo-yan-yu-moderunochi-tuyan-yu-zhi-shi-tokomiyunikesiyon) - Yasuhiro Kondo（2024-05）
- [日本語研究から見たChatGPT](https://speakerdeck.com/yhkondo/ri-ben-yu-yan-jiu-karajian-tachatgpt) - Yasuhiro Kondo（2023-05）
- [構造を持った言語データと最適輸送](https://speakerdeck.com/eumesy/optimal-transport-for-structured-language-data) - Sho Yokoi（2022-09）
- [eccoによる言語モデルの可視化 (2022-01-28 NLP Hacks#1)](https://speakerdeck.com/hikomimo/ecconiyoruyan-yu-moderufalseke-shi-hua-2022-01-28-nlp-hacks-number-1) - Akira Sasaki（2022-02）
- [Is Attention Interpretable?](https://speakerdeck.com/chokkan/is-attention-interpretable) - Naoaki Okazaki（2019-09）

## 産業応用・実務事例

実サービス・実業務に NLP / LLM を組み込んだ事例。

- [つくって納得、つかって実感！ 大規模言語モデルことはじめ ver2.0](https://speakerdeck.com/recruitengineers/fy2026_bootcamp_kiryu) - Recruit（2026-08）
- [Kaggle自然言語処理コンペ向けローカルLLM活用入門](https://speakerdeck.com/k951286/kagglezi-ran-yan-yu-chu-li-konpexiang-kerokarullmhuo-yong-ru-men) - monnu（2025-02）
- [医療分野における大規模言語モデルの調査](https://www.docswell.com/s/5451263343/5WWLRJ-2025-01-17-204429) - 高橋浩（2025-01）
- [Argo Workflowsで構築するLLMを活用したコールセンターの自動要約プロダクトの立ち上げ / ai-argo-summarize](https://speakerdeck.com/cyberagentdevelopers/ai-argo-summarize) - CyberAgent（2024-10）
- [自社開発した大規模言語モデルをどうプロダクションに乗せて運用していくか〜インフラ編〜](https://speakerdeck.com/pfn/20240906-cloud-operator-days-2024-pfn) - Preferred Networks（2024-09）
- [LLMと共に進むSORACOMサポートの挑戦と効果【SORACOM Discovery 2024】](https://speakerdeck.com/soracom/soracom-discovery-2024-c-5) - SORACOM（ソラコム）（2024-07）
- [LIFULL AI Hub 100ミニッツ #1\_LLM（大規模言語モデル）の研究開発](https://www.docswell.com/s/LIFULL/ZNR31G-2023-12-28-170955) - 株式会社LIFULL（2023-12）
- [ELYZA\_LLMの現状・課題・展望に関する勉強会\_20230713](https://speakerdeck.com/elyza/llm-yan-yu-sheng-cheng-ai-noxian-zhuang-ke-ti-zhan-wang-niguan-surumian-qiang-hui-20230713-7578523c-9de2-43d5-b0cd-36fda5baff68) - 株式会社ELYZA（2023-08）
- [テキストマイニングを使って 今年1年のレビュー内容をふりかえってみた話](https://speakerdeck.com/cybozuinsideout/line_twm_221221_cybozu) - Cybozu（2022-12）
- [ESG評価に対する自然言語処理の活用Workshop](https://speakerdeck.com/icoxfog417/esgping-jia-nidui-suruzi-ran-yan-yu-chu-li-falsehuo-yong-workshop) - Takahiro Kubo（2022-06）
- [日本経済新聞社における自然言語処理の取り組み / yans2022 nikkei nlp](https://speakerdeck.com/upura/yans2022-nikkei-nlp) - Shotaro Ishihara（2022-03）
- [ハンドメイド作品を扱うECサイトに特化したBERTを用いた言語モデル構築に向けた取り組み/ipsj-NL250-05](https://speakerdeck.com/tossy/ipsj-nl250-05) - tossy（2021-09）
- [【Ltech#11】住まい探しにおける対話AIの自然言語解析技術](https://www.docswell.com/s/LIFULL/KPLVGZ-%E4%BD%8F%E3%81%BE%E3%81%84%E6%8E%A2%E3%81%97%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E5%AF%BE%E8%A9%B1AI%E3%81%AE%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E8%A7%A3%E6%9E%90%E6%8A%80%E8%A1%93) - 株式会社LIFULL（2020-10）

## ライセンス

[CC0 1.0 Universal](http://creativecommons.org/publicdomain/zero/1.0/)

> [!NOTE]
> CC0 が適用されるのはこのリスト自体です。リンク先の各スライドの著作権は、それぞれの発表者に帰属します。
