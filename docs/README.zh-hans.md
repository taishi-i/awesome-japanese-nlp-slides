# awesome-japanese-nlp-slides

![Awesome Japanese NLP Slides](../images/awesome-japanese-nlp-slides.png)

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-slides)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-slides/pulls)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

[日本語 (Japanese)](https://github.com/taishi-i/awesome-japanese-nlp-slides/blob/main/docs/README.ja.md) | [English](https://github.com/taishi-i/awesome-japanese-nlp-slides/blob/main/docs/README.en.md) | [繁體中文 (Chinese)](https://github.com/taishi-i/awesome-japanese-nlp-slides/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese)](https://github.com/taishi-i/awesome-japanese-nlp-slides/blob/main/docs/README.zh-hans.md)

这是一份精选列表，收录了日语自然语言处理（NLP）相关的演示幻灯片。
按主题整理了学会的教程演讲、大学课程、OSS 开发者的技术讲解，以及企业的实践案例。

共收录 437 份资料，分为 26 个分类。

幻灯片标题保留发表时的原文，因此绝大多数为日语。

> [!NOTE]
> 本列表仍在建设中，今后会持续新增资料并扩充内容。

## 🔍 从 Claude Code 搜索

我们提供了插件，让你可以从 Claude Code 搜索本列表收录的 437 份资料。

```
/plugin marketplace add taishi-i/awesome-japanese-nlp-slides
/plugin install awesome-japanese-nlp-slides@awesome-japanese-nlp-slides
```

安装后，把关键词或自然语句交给 `search` 技能，就会按相关度返回最多 10 条结果，以及建议的阅读顺序。

```
/awesome-japanese-nlp-slides:search 形态素解析
/awesome-japanese-nlp-slides:search 日语 LLM 的预训练
/awesome-japanese-nlp-slides:search RAG
/awesome-japanese-nlp-slides:search evaluation benchmark
```

> [!TIP]
> 日语、英语、中文均可搜索。输出的语言会跟随查询所使用的语言，用简体中文查询就会得到简体中文的回复。
> 也可以用自然语句提问，例如「我想从入门开始依次阅读」，这样还会得到建议的阅读顺序。

## 目录

- [入门・全貌](#入门全貌)
- [学会教程演讲](#学会教程演讲)
- [大学课程・系统性讲义资料](#大学课程系统性讲义资料)
- [日语的基础分析（形态素分析・句法分析）](#日语的基础分析形态素分析句法分析)
- [日语文本的规范化・写法差异](#日语文本的规范化写法差异)
- [词与句的分布式表示](#词与句的分布式表示)
- [预训练模型・Transformer](#预训练模型transformer)
- [大语言模型（概论・趋势）](#大语言模型概论趋势)
- [日语 LLM 的开发（预训练・语料库构建）](#日语-llm-的开发预训练语料库构建)
- [微调・后训练](#微调后训练)
- [LLM 的推理优化・服务部署](#llm-的推理优化服务部署)
- [评测・基准测试](#评测基准测试)
- [全文检索・搜索基础设施](#全文检索搜索基础设施)
- [检索・RAG](#检索rag)
- [LLM 应用开发・运维](#llm-应用开发运维)
- [文本分类・情感分析](#文本分类情感分析)
- [信息抽取・命名实体・标注](#信息抽取命名实体标注)
- [文档处理・OCR](#文档处理ocr)
- [问答・知识](#问答知识)
- [机器翻译](#机器翻译)
- [多模态・视觉与语言](#多模态视觉与语言)
- [语音识别・语音处理](#语音识别语音处理)
- [对话系统・语音对话](#对话系统语音对话)
- [生成・摘要・校对](#生成摘要校对)
- [可解释性・分析・语言学观点](#可解释性分析语言学观点)
- [产业应用・实务案例](#产业应用实务案例)

## 入门・全貌

想纵观自然语言处理全貌的人，最先该读的资料。

- [情報処理学会関西支部2024年度定期講演会「自然言語処理と大規模言語モデルの基礎」](https://speakerdeck.com/ksudoh/qing-bao-chu-li-xue-hui-guan-xi-zhi-bu-2024nian-du-ding-qi-jiang-yan-hui-zi-ran-yan-yu-chu-li-toda-gui-mo-yan-yu-moderunoji-chu) - Katsuhito Sudoh（2024-11）
- [ae-8. 自然言語処理（問答，要約，テキスト生成，単語の特徴ベクトル，単語の類似度）](https://www.docswell.com/s/6674398749/5M4Y2K-2023-01-29-132348) - kunihikokaneko（2023-01）
- [言葉の形を教えてくれる自然言語処理](https://speakerdeck.com/eumesy/natural-language-processing-tells-us-the-shape-of-language) - Sho Yokoi（2022-03）
- [深層学習による自然言語処理入門: word2vecからBERT, GPT-3まで](https://www.docswell.com/s/ydnjp/K3YMDZ-2021-07-21-152903) - Yahoo!デベロッパーネットワーク（2021-07）
- [実践！AllenNLPによるディープラーニングを用いた自然言語処理](https://speakerdeck.com/ikuyamada/shi-jian-allennlpniyorudeipuraninguwoyong-itazi-ran-yan-yu-chu-li) - Ikuya Yamada（2021-03）
- [自然言語処理の最新技術動向紹介](https://www.docswell.com/s/ydnjp/5D79LK-2020-12-24-130254) - Yahoo!デベロッパーネットワーク（2020-12）
- [最先端自然言語処理ライブラリの最適な選択と有用な利用方法 / pycon-jp-2020](https://speakerdeck.com/taishii/pycon-jp-2020) - taishi-i（2020-08）
- [Python による日本語自然言語処理 〜系列ラベリングによる実世界テキスト分析〜 / PyCon JP 2019](https://speakerdeck.com/taishii/pycon-jp-2019) - taishi-i（2019-09）
- [How Deep Learning Changes Natural Language Processing](https://speakerdeck.com/chokkan/how-deep-learning-changes-natural-language-processing) - Naoaki Okazaki（2018-09）
- [深層学習による自然言語処理の研究動向](https://www.slideshare.net/stairlab/ss-61806151) - STAIR Lab, Chiba Institute of Technology（2016-04）
- [深層学習時代の自然言語処理](https://www.slideshare.net/unnonouno/ss-43844132) - Yuya Unno（2015-01）
- [Deep Learningと自然言語処理](https://www.slideshare.net/pfi/deep-learning-42997311) - Preferred Networks（2014-12）

## 学会教程演讲

语言处理学会、人工智能学会等学会的教程演讲资料。

- [言語モデルの内部機序：解析と解釈](https://speakerdeck.com/eumesy/analysis_and_interpretation_of_language_models) - Sho Yokoi（2025-03）
- [最強DB講義 #35 大規模言語モデルに基づく検索モデル](https://speakerdeck.com/mpkato/zui-qiang-dbjiang-yi-number-35-da-gui-mo-yan-yu-moderuniji-dukujian-suo-moderu) - Makoto P. Kato（2024-11）
- [言語と数理の交差点：テキストの埋め込みと構造のモデル化 (IBIS 2024 チュートリアル)](https://speakerdeck.com/yukiar/yan-yu-toshu-li-nojiao-chai-dian-tekisutonomai-meip-mitogou-zao-nomoderuhua-ibis-2024-tiyutoriaru) - Yuki Arase（2024-11）
- [SSII2024 \[OS2\] 大規模言語モデルと基盤モデルの射程](https://speakerdeck.com/ssii/ssii2024-os2-otani) - 画像センシングシンポジウム（2024-06）
- [大規模言語モデルの開発](https://speakerdeck.com/chokkan/jsai2024-tutorial-llm) - Naoaki Okazaki（2024-05）
- [IBIS2023チュートリアル「大規模言語モデル活用技術の最前線」](https://speakerdeck.com/1never/ibis2023tiyutoriaru-da-gui-mo-yan-yu-moderuhuo-yong-ji-shu-nozui-qian-xian) - Michimasa Inaba（2023-10）
- [Part 5: Efforts for Responsible LLMs, PAKDD 2023 Tutorial 2: A Gentle Introduction to Technologies Behind Language Models and Recent Achievement in ChatGPT](https://speakerdeck.com/chokkan/efforts-for-responsible-llms-pakdd-2023-tutorial-2) - Naoaki Okazaki（2023-05）
- [PAKDD2023 Tutorial 2: A Gentle Introduction to Technologies Behind Language Models and Recent Achievement in ChatGPT (Parts 3 and 4)](https://speakerdeck.com/kyoun/pakdd2023-tutorial) - Kyosuke Nishida（2023-05）
- [NLPとVision-and-Languageの基礎・最新動向 (2) / DEIM Tutorial Part 2 Vision-and-Language](https://speakerdeck.com/kyoun/deim-tutorial-part-2-vision-and-language) - Kyosuke Nishida（2023-03）
- [NLPとVision-and-Languageの基礎・最新動向 (1) / DEIM Tutorial Part 1: NLP](https://speakerdeck.com/kyoun/deim-tutorial-part-1-nlp) - Kyosuke Nishida（2023-03）
- [自然言語処理とVision-and-Language / A Tutorial on NLP & Vision-and-Language](https://speakerdeck.com/kyoun/a-tutorial-on-nlp-and-vision-and-language) - Kyosuke Nishida（2022-06）
- [ゼロから始める転移学習](https://www.docswell.com/s/ydnjp/5L8XPZ-2022-04-27-133413) - Yahoo!デベロッパーネットワーク（2022-04）
- [最適輸送と自然言語処理](https://speakerdeck.com/eumesy/optimal-transport-for-natural-language-processing) - Sho Yokoi（2022-03）
- [\[最新版\] JSAI2018 チュートリアル「"深層学習時代の" ゼロから始める自然言語処理」](https://www.slideshare.net/yukiarase/jsai2018-101054060) - Yuki Arase（2018-06）
- [NLP2017 NMT Tutorial](https://www.slideshare.net/ToshiakiNakazawa/nlp2017-nmt-tutorial) - Toshiaki Nakazawa（2017-03）
- [ゼロから始める自然言語処理 【FIT2016チュートリアル】](https://www.slideshare.net/yukiarase/fit2016-66043779) - Yuki Arase（2016-09）

## 大学课程・系统性讲义资料

大学课程，以及书籍读书会所使用的系列讲义资料。

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

## 日语的基础分析（形态素分析・句法分析）

负责日语特有预处理的分析器与词典相关资料。

- [日本語のポップアップ辞書アプリに向けて形態素解析システムの設計・実装・運用](https://speakerdeck.com/noheartpen/i2-b3-ri-ben-yu-nopotupuatupuci-shu-apurinixiang-ketexing-tai-su-jie-xi-sisutemunoshe-ji-shi-zhuang-yun-yong) - John Qing（2025-04）
- [係り受け解析を用いた法律文書中の略称規定の解析についての報告](https://speakerdeck.com/puripuri2100/xi-rishou-kejie-xi-woyong-itafa-lu-wen-shu-zhong-nolue-cheng-gui-ding-nojie-xi-nituitenobao-gao) - puripuri2100（2024-09）
- [\[NLP2023\] 最小コスト法に基づく形態素解析におけるCPU キャッシュの効率化](https://speakerdeck.com/legalontechnologies/nlp2023-vibrato) - LegalOn Technologies, Inc（2024-05）
- [\[DEIM2023\] 高速な形態素解析器Vibratoの紹介](https://speakerdeck.com/legalontechnologies/deim2023-introduction-to-vibrato-fast-morphological-analyzer) - LegalOn Technologies, Inc（2023-03）
- [KWJA：汎用言語モデルに基づく日本語解析器 / kyoto-waseda-japanese-analyzer](https://speakerdeck.com/nobug/kyoto-waseda-japanese-analyzer) - Nobuhiro Ueda（2022-09）
- [Sudachi Family近況報告 at WAP NLP Tech Talk #5](https://speakerdeck.com/waptech/sudachi-familyjin-kuang-bao-gao-at-wap-nlp-tech-talk-number-5) - WAP（2022-04）
- [Sudachi近況報告 at WAP NLP Tech Talk #4](https://speakerdeck.com/waptech/sudachijin-kuang-bao-gao-at-wap-nlp-tech-talk-number-4) - WAP（2021-11）
- [オープンソースとしての形態素解析器Sudachi / WAP NLP Tech Talk #4](https://speakerdeck.com/sorami/wap-nlp-tech-talk-number-4) - Sorami Shiromizu（2021-11）
- [日本語形態素解析器 SudachiPy の 現状と今後について](https://speakerdeck.com/waptech/ri-ben-yu-xing-tai-su-jie-xi-qi-sudachipy-false-xian-zhuang-tojin-hou-nituite) - WAP（2021-07）
- [Sudachi辞書のつくり方](https://speakerdeck.com/waptech/sudachici-shu-falsetukurifang) - WAP（2020-12）
- [Lucene Kuromoji のコードを読む会 （辞書ビルダー編）](https://speakerdeck.com/mocobeta/lucene-kuromoji-nokodowodu-muhui-ci-shu-birudabian) - Tomoko Uchida（2019-10）
- [犬でもわかる Minimal Acyclic Subsequential Transducer / Introduction to Minimal Acyclic Subsequential Transducer](https://speakerdeck.com/takuyaa/introduction-to-minimal-acyclic-subsequential-transducer) - Takuya Asano（2019-06）
- [形態素解析器をフルスクラッチで作る話](https://speakerdeck.com/namachan10777/xing-tai-su-jie-xi-qi-wohurusukuratutidezuo-ruhua) - Nakano Masaki（2019-05）
- [NLP2019 松田寛 - GiNZA](https://www.slideshare.net/MegagonLabs/nlp2019-ginza-139011245) - Megagon Labs（2019-03）
- [Javaでつくる本格形態素解析器](https://www.slideshare.net/WorksApplications/java-82794239) - Works Applications（2017-11）
- [AWS APIGateway + Python Lambda + NEologdで作るサーバレス日本語形態素解析API](https://speakerdeck.com/satorukadowaki/aws-apigateway-plus-python-lambda-plus-neologddezuo-rusabaresuri-ben-yu-xing-tai-su-jie-xi-api) - Satoru Kadowaki（2017-09）
- [形態素解析](https://www.slideshare.net/WorksApplications/ss-78025845) - Works Applications（2017-06）
- [JUMAN++で分かち書きをしたかった...](https://speakerdeck.com/nagomiso/juman-plus-plus-defen-katishu-kiwositakatuta-dot-dot-dot) - なごみそ（2017-05）
- [日本語の形態素解析](https://speakerdeck.com/yumeto/ri-ben-yu-falsexing-tai-su-jie-xi) - Yumeto Inaoka（2017-01）
- [第17回Lucene/Solr勉強会 #SolrJP – Apache Lucene Solrによる形態素解析の課題とN-bestの提案](https://www.docswell.com/s/ydnjp/Z9YVX5-2015-10-28-154003) - Yahoo!デベロッパーネットワーク（2015-10）
- [Pythonで作って学ぶ形態素解析](https://speakerdeck.com/mocobeta/pythondezuo-tutexue-buxing-tai-su-jie-xi) - Tomoko Uchida（2015-10）
- [1binary 自己完結型の 形態素解析器 kagome を 作ってみた話](https://speakerdeck.com/ikawaha/1binary-zi-ji-wan-jie-xing-false-xing-tai-su-jie-xi-qi-kagome-wo-zuo-tutemitahua) - ikawaha（2015-06）
- [形態素解析器 MeCab の新語・固有表現辞書 mecab-ipadic-NEologd のご紹介](https://www.slideshare.net/overlast/mecab-ipadicneologdtokyordf-46497035) - Toshinori Sato（2015-03）
- [形態素解析の過去・現在・未来](https://www.slideshare.net/pfi/ss-9805912) - Preferred Networks（2011-10）
- [統計的係り受け解析入門](https://speakerdeck.com/unnonouno/tong-ji-de-xi-rishou-kejie-xi-ru-men) - Yuya Unno（2010-11）

## 日语文本的规范化・写法差异

全角半角、异体字、地址与专有名词的写法差异等，统一日语文本所需的实务知识。

- [POI検索システムにおける 誤字・脱字との戦い](https://speakerdeck.com/tstomoki/poijian-suo-sisutemuniokeru-wu-zi-tuo-zi-tonozhan-i) - Tomoki Saito（2025-11）
- [Rustの住所正規化ライブラリをPythonから触る / PythonFukuoka\_Session\_2](https://speakerdeck.com/sansan_randd/pythonfukuoka-session-2) - Sansan R&D（2025-09）
- [Tech Kitchen #31 - グローバル版でMeCab辞書も管理したい](https://speakerdeck.com/ksh/tech-kitchen-number-31-gurobaruban-demecabci-shu-moguan-li-sitai) - k-ush（2025-04）
- [Lucene/Elasticsearch の Character Filter でユニコード正規化するとトークンのオフセットがズレるバグへの Workaround - Search Engineering Tech Talk 2024 Spring](https://speakerdeck.com/kampersanda/elasticsearch-no-character-filter-deyunikodozheng-gui-hua-surutotokunnoohusetutogazurerubaguheno-workaround-search-engineering-tech-talk-2024-spring) - Shunsuke Kanda（2024-05）
- [文字列正規化パタンの獲得と崩れ表記正規化に基づく日本語形態素解析](https://speakerdeck.com/atsumikan/wen-zi-lie-zheng-gui-hua-patanfalsehuo-de-tobeng-rebiao-ji-zheng-gui-hua-niji-dukuri-ben-yu-xing-tai-su-jie-xi) - Atsushi（2018-04）
- [日本語の表記ゆれ 解決方法の検討と実装](https://speakerdeck.com/takahiko03/ri-ben-yu-falsebiao-ji-yure-jie-jue-fang-fa-falsejian-tao-toshi-zhuang) - Takahiko Ito（2017-11）
- [日本語解析システム「雪だるま」における表記ゆれの拡張とまとめあげ](https://speakerdeck.com/nishiyama/ri-ben-yu-jie-xi-sisutemu-xue-daruma-niokerubiao-ji-yurefalsekuo-zhang-tomatomeage) - nishi-k（2016-08）

## 词与句的分布式表示

词向量、句子嵌入，以及嵌入空间性质的相关资料。

- [Zipf 白色化：タイプとトークンの区別がもたらす良質な埋め込み空間と損失関数](https://speakerdeck.com/eumesy/zipfian-whitening) - Sho Yokoi（2024-11）
- [NLP2024 招待論文セッション: 定義文を用いた文埋め込み構成法](https://speakerdeck.com/hpprc/nlp2024-zhao-dai-lun-wen-setusiyon-ding-yi-wen-woyong-itawen-mai-meip-migou-cheng-fa) - Hayato Tsukagoshi（2024-09）
- [\[輪講資料\] Matryoshka Representation Learning](https://speakerdeck.com/hpprc/lun-jiang-zi-liao-matryoshka-representation-learning) - Hayato Tsukagoshi（2024-08）
- [\[輪講資料\] Text Embeddings by Weakly-Supervised Contrastive Pre-training](https://speakerdeck.com/hpprc/lun-jiang-zi-liao-text-embeddings-by-weakly-supervised-contrastive-pre-training) - Hayato Tsukagoshi（2024-05）
- [意味変化分析に向けた単語埋め込みの時系列パターン分析](https://speakerdeck.com/rudorudo11/yi-wei-bian-hua-fen-xi-nixiang-ketadan-yu-mai-meip-minoshi-xi-lie-patanfen-xi) - hajime kiyama（2024-03）
- [オープンな日本語埋め込みモデルの選択肢 / Exploring Publicly Available Japanese Embedding Models](https://speakerdeck.com/nttcom/exploring-publicly-available-japanese-embedding-models) - NTT docomo Business（2024-01）
- [\[輪講資料\] One Embedder, Any Task: Instruction-Finetuned Text Embeddings](https://speakerdeck.com/hpprc/one-embedder-any-task-instruction-finetuned-text-embeddings) - Hayato Tsukagoshi（2023-12）
- [埋め込み表現の意味適応による知識ベース語義曖昧性解消](https://speakerdeck.com/s_mizuki_nlp/mai-meip-mibiao-xian-noyi-wei-shi-ying-niyoruzhi-shi-besuyu-yi-ai-mei-xing-jie-xiao) - S（2023-05）
- [単語分散表現と事前学習モデル - chiVe \_ chiTra 利活用のための下準備 at WAP NLP Tech Talk #5](https://speakerdeck.com/waptech/dan-yu-fen-san-biao-xian-toshi-qian-xue-xi-moderu-chive-chitra-li-huo-yong-falsetamefalsexia-zhun-bei-at-wap-nlp-tech-talk-number-5) - WAP（2022-04）
- [単語分散表現 chiVeの活用方法 at WAP NLP Tech Talk #5](https://speakerdeck.com/waptech/dan-yu-fen-san-biao-xian-chivefalsehuo-yong-fang-fa-at-wap-nlp-tech-talk-number-5) - WAP（2022-04）
- [事前学習モデル chiTra の活用方法 at WAP NLP Tech Talk #5](https://speakerdeck.com/waptech/shi-qian-xue-xi-moderu-chitra-falsehuo-yong-fang-fa-at-wap-nlp-tech-talk-number-5) - WAP（2022-04）
- [chiVe\_実用的な日本語単語ベクトル実現にむけて\_20201208](https://speakerdeck.com/waptech/chive-shi-yong-de-nari-ben-yu-dan-yu-bekutorushi-xian-nimukete-20201208) - WAP（2020-12）
- [chiVe: 製品利用可能な日本語単語ベクトル資源の実現へ向けて](https://speakerdeck.com/sorami/chive-zhi-pin-li-yong-ke-neng-nari-ben-yu-dan-yu-bekutoruzi-yuan-falseshi-xian-hexiang-kete) - Sorami Shiromizu（2020-09）
- [双曲空間への単語埋め込みと QAサービスでの自然言語処理を 用いた推薦システムについて](https://speakerdeck.com/ryusuketa/shuang-qu-kong-jian-hefalsedan-yu-mai-meip-mito-qasabisudefalsezi-ran-yan-yu-chu-li-wo-yong-itatui-jian-sisutemunituite) - Ryusuke_Tanaka（2019-04）
- [トピックモデルによる分散表現獲得手法の提案](https://speakerdeck.com/nzw0301/topitukumoderuniyorufen-san-biao-xian-huo-de-shou-fa-falseti-an) - Kento Nozawa（2016-03）
- [分散表現に基づく文書要約#yjdsw1](https://www.docswell.com/s/ydnjp/ZXVYMK-2015-12-21-134350) - Yahoo!デベロッパーネットワーク（2015-12）
- [単語の分散表現と構成性の計算モデルの発展](https://www.slideshare.net/naoakiokazaki/20150530-jsai2015) - Naoaki Okazaki（2015-05）

## 预训练模型・Transformer

BERT 之后的预训练模型，以及 Transformer 的讲解资料。

- [PyTorchによるGPT-2モデルのフルスクラッチ実装と内部構造の解説](https://speakerdeck.com/sennsann99/pytorchniyorugpt-2moderunohurusukuratutishi-zhuang-tonei-bu-gou-zao-nojie-shuo) - Chigen SEN（2026-03）
- [非情報系研究者へ送る Transformer入門](https://speakerdeck.com/rishiyama/fei-qing-bao-xi-yan-jiu-zhe-hesong-ru-transformerru-men) - Ryo Ishiyama（2026-03）
- [大規模言語モデルを支える頭脳：Transformerを30分でつかむ](https://speakerdeck.com/rhagihara0844/da-gui-mo-yan-yu-moderuwozhi-erutou-noy-transformerwo30fen-detukamu) - r-hagihara-max（2025-08）
- [Transformerによるテキストベクトル化を解説](https://speakerdeck.com/payanotty/transformerniyorutekisutobekutoruhua-wojie-shuo) - payanotty（2024-01）
- [【初心者向け】まだ間に合う！ Hugging Face入門 -TransformersでAI推論&学習](https://speakerdeck.com/tkhresk/huggingfaceru-men) - Takahiro Esaki（2023-09）
- [Transformersによる自然言語処理の実践](https://www.docswell.com/s/flowlight0/5RX82N-2023-08-22-152738) - flowlight0（2023-08）
- [Transformer / Vision and Languageの基礎](https://speakerdeck.com/sgnm/vision-and-languagenoji-chu) - Masanori Suganuma（2022-10）
- [BERTによる自然言語処理を学ぼう!【 Live!人工知能 #26】 #Live人工知能](https://speakerdeck.com/yukinaga/bertniyoruzi-ran-yan-yu-chu-li-woxue-bou-live-ren-gong-zhi-neng-number-26-number-liveren-gong-zhi-neng) - yuky_az（2020-11）
- [事前学習済言語モデルの動向 (2) / Survey of Pretrained Language Models](https://speakerdeck.com/kyoun/survey-of-pretrained-language-models-f6319c84-a3bc-42ed-b7b9-05e2588b12c7) - Kyosuke Nishida（2020-02）
- [事前学習言語モデルの動向 / Survey of Pretrained Language Models](https://speakerdeck.com/kyoun/survey-of-pretrained-language-models) - Kyosuke Nishida（2019-11）
- [BERTology のススメ](https://www.slideshare.net/haradatm/bertology-177275003) - University of Tsukuba（2019-09）
- [\[DL輪読会\]BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://www.docswell.com/s/DeepLearning2023/5Q8L7R-dlbert-pretraining-of-deep-bidirectional-transformers-for-language-understanding) - Deep Learning JP（2018-10）

## 大语言模型（概论・趋势）

纵观 LLM 全貌的讲解与特邀演讲。

- [AIはどのように考えて話すのか？ ― 言葉と知能の不思議](https://speakerdeck.com/chokkan/how-ai-thinks-and-responds) - Naoaki Okazaki（2026-07）
- [大規模言語モデル（LLM)について人文学研究者が知っておきたいこと](https://speakerdeck.com/yhkondo/da-gui-mo-yan-yu-moderu-llm-nituiteren-wen-xue-yan-jiu-zhe-gazhi-tuteokitaikoto) - Yasuhiro Kondo（2025-05）
- [大規模言語モデルとそのソフトウェア開発に向けた応用 (2024年版)](https://speakerdeck.com/kazato/da-gui-mo-yan-yu-moderutosonosohutoueakai-fa-nixiang-ketaying-yong-2024nian-ban) - Hiroshi Kazato（2024-12）
- [大規模言語モデル (LLM) の技術と最新動向](https://speakerdeck.com/ikuyamada/da-gui-mo-yan-yu-moderu-llm-noji-shu-tozui-xin-dong-xiang) - Ikuya Yamada（2024-06）
- [大規模言語モデルのインパクトと課題/oc2023](https://speakerdeck.com/mamoruk/oc2023-5b5c720d-f963-430e-b4a1-ab4b2df45b1b) - Mamoru Komachi（2024-05）
- [LLMの現在](https://speakerdeck.com/pfn/llm-no-genzai-imos) - Preferred Networks（2024-03）
- [大規模言語モデルを作る、拡張する](https://speakerdeck.com/stillpedant/building-llm) - Masafumi Oyamada（2024-02）
- [大規模言語モデル入門 / LLM introduction (SES2023)](https://speakerdeck.com/kyoun/llm-introduction-ses2023) - Kyosuke Nishida（2023-08）
- [大規模言語モデルの驚異と脅威](https://speakerdeck.com/chokkan/20230327_riken_llm) - Naoaki Okazaki（2023-03）

## 日语 LLM 的开发（预训练・语料库构建）

来自实际打造日语 LLM 的一线经验。

- [AIエージェント時代のLLM-jpモデルのあるべき姿](https://speakerdeck.com/k141303/aiezientoshi-dai-nollm-jpmoderunoarubekizi) - Kouta Nakayama（2026-04）
- [2024-02-Tokyo-Tech-大規模言語モデルの事前学習知見](https://speakerdeck.com/fujiikazuki2000/2024-02-tokyo-tech-da-gui-mo-yan-yu-moderunoshi-qian-xue-xi-zhi-jian) - Kazuki Fujii（2025-12）
- [言語処理学会2024-継続事前学習による日本語に強い大規模言語モデルの構築](https://speakerdeck.com/fujiikazuki2000/yan-yu-chu-li-xue-hui-2024-ji-sok-shi-qian-xue-xi-niyoruri-ben-yu-niqiang-ida-gui-mo-yan-yu-moderunogou-zhu) - Kazuki Fujii（2025-12）
- [情報処理学会-全国大会2024-大規模言語モデルの分散並列学習](https://speakerdeck.com/fujiikazuki2000/qing-bao-chu-li-xue-hui-quan-guo-da-hui-2024-da-gui-mo-yan-yu-moderunofen-san-bing-lie-xue-xi) - Kazuki Fujii（2025-12）
- [AWS Summit Japan 2025 Amazon SageMaker HyperPodを利用した日本語LLM(Swallow)の構築 (CUS-02)](https://speakerdeck.com/fujiikazuki2000/aws-summit-japan-2025-amazon-sagemaker-hyperpodwoli-yong-sitari-ben-yu-llm-swallow-nogou-zhu-cus-02) - Kazuki Fujii（2025-12）
- [LLM-jp-3 and beyond: Training Large Language Models](https://speakerdeck.com/odashi/llm-jp-3-and-beyond-training-large-language-models) - Yusuke Oda（2025-10）
- [合成データパイプラインを利用したSwallowProjectに おけるLLM性能向上](https://speakerdeck.com/fujiikazuki2000/he-cheng-detapaipurainwoli-yong-sitaswallowprojectni-okerullmxing-neng-xiang-shang) - Kazuki Fujii（2025-08）
- [論文では語られないLLM開発において重要なこと Swallow Projectを通して](https://speakerdeck.com/fujiikazuki2000/lun-wen-dehayu-rarenaillmkai-fa-nioitezhong-yao-nakoto-swallow-projectwotong-site) - Kazuki Fujii（2025-07）
- [新聞記事からつくる 時事と社会に強い日本語LLM（NLP2025）](https://speakerdeck.com/aya_se/xin-wen-ji-shi-karatukuru-shi-shi-toshe-hui-niqiang-iri-ben-yu-llm-nlp2025) - Kakeru Hattori（2025-03）
- [Swallowコーパスv2: 教育的な日本語ウェブコーパスの構築（NLP2025）](https://speakerdeck.com/aya_se/swallowkopasuv2-jiao-yu-de-nari-ben-yu-uebukopasunogou-zhu-nlp2025) - Kakeru Hattori（2025-03）
- [LLMの事前学習のためのテキストデータの収集と構築](https://speakerdeck.com/butsugiri/llmnoshi-qian-xue-xi-notamenotekisutodetanoshou-ji-togou-zhu) - Shun Kiyono（2025-02）
- [PLaMo-100B-Instruct 国産大規模言語モデル構築における事後学習の取り組み](https://speakerdeck.com/pfn/plamo-100b-instruct-guo-chan-da-gui-mo-yan-yu-moderugou-zhu-niokerushi-hou-xue-xi-noqu-rizu-mi) - Preferred Networks（2024-12）
- [松尾研LLM開発プロジェクト “Tanuki” 開発報告会 Vol.1](https://www.docswell.com/s/matsuo-lab_llm/51R2L4-2024-9-10-Tanuki%E9%96%8B%E7%99%BA%E5%A0%B1%E5%91%8A%E4%BC%9A-vol1) - 松尾研LLMコミュニティ（2024-11）
- [大規模言語モデル Tanuki-8x8Bの紹介と開発経緯など](https://www.docswell.com/s/KanHatakeyama/5YDDJE-2024-09-18-214202) - Kan Hatakeyama（2024-09）
- [LLMに日本語テキストを学習させる意義](https://speakerdeck.com/ksaito/llmniri-ben-yu-tekisutowoxue-xi-saseruyi-yi) - Koshiro Saito（2024-08）
- [Building an Effective Pre-training Corpus for Japanese LLM (TAI AAI #3)](https://speakerdeck.com/aya_se/building-an-effective-pre-training-corpus-for-japanese-llm-tai-aai-number-3) - Kakeru Hattori（2024-08）
- [LLM開発・活用の舞台裏@2024.04.25](https://speakerdeck.com/stockmark/llmkai-fa-huo-yong-nowu-tai-li-at-2024-dot-04-dot-25-slash-behind-the-scene-of-development-and-utilize-llm) - Stockmark（2024-04）
- [大規模言語モデル開発の進捗まとめ(◯データ整備・△事前学習・△ファインチューニング)](https://www.docswell.com/s/KanHatakeyama/ZYW393-2024-04-08-112244) - Kan Hatakeyama（2024-04）
- [ICHIKARA-INSTRUCTION LLMのための日本語インストラクションの構築と 人間とGPT-4による評価で観察されたもの](https://speakerdeck.com/olachinkei/ichikara-instruction-llmnotamenori-ben-yu-insutorakusiyonnogou-zhu-to-ren-jian-togpt-4niyoruping-jia-deguan-cha-saretamono) - Keisuke Kamata（2024-03）
- [大規模言語モデル開発のための日本語 Instruction データセット作成の取り組み](https://speakerdeck.com/kunishou/da-gui-mo-yan-yu-moderukai-fa-notamenori-ben-yu-instruction-detasetutozuo-cheng-noqu-rizu-mi) - Shouhei Kuniyoshi（2024-03）
- [言語間転移学習で大規模言語モデルを賢くする](https://speakerdeck.com/ikuyamada/yan-yu-jian-zhuan-yi-xue-xi-deda-gui-mo-yan-yu-moderuwoxian-kusuru) - Ikuya Yamada（2024-03）
- [自然言語処理のための分散並列学習](https://speakerdeck.com/fujiikazuki2000/zi-ran-yan-yu-chu-li-notamenofen-san-bing-lie-xue-xi-3dd9cdf8-cc6d-4350-8141-89ce35b9d273) - Kazuki Fujii（2024-03）
- [東工大Swallowプロジェクトにおける大規模日本語Webコーパスの構築](https://speakerdeck.com/aya_se/data-centric-ai-swallow-corpus-56e2869a-f9bd-46cb-b030-1012235c37f7) - Kakeru Hattori（2024-02）
- [Stability AI Japanにおける大規模言語モデルの研究開発](https://speakerdeck.com/iwiwi/stability-ai-japanniokeruda-gui-mo-yan-yu-moderunoyan-jiu-kai-fa) - Takuya Akiba（2023-09）
- [大規模日本語ブログコーパスにおける言語モデルの構築と評価](https://www.slideshare.net/techblogyahoo/nlp2011-okuno-slide) - Yahoo!デベロッパーネットワーク（2011-03）

## 微调・后训练

按照目的调整已有模型的各种方法。

- [PLaMo 3.0 Primeの事後学習](https://speakerdeck.com/pfn/20260730_pfn_llm_1_post_training) - Preferred Networks（2026-07）
- [PLaMoの事後学習を支える技術 / PFN LLMセミナー](https://speakerdeck.com/pfn/20251001-pfn-llm-seminar-post-training) - Preferred Networks（2025-10）
- [Function calling機能をPLaMo2に実装するには / PFN LLMセミナー](https://speakerdeck.com/pfn/20251001-pfn-llm-seminar-infopt-function-calling) - Preferred Networks（2025-10）
- [Go言語での実装を通して学ぶLLMファインチューニングの仕組み / fukuokago22-llm-peft](https://speakerdeck.com/monochromegane/fukuokago22-llm-peft) - monochromegane（2025-08）
- [論文読み会 SNLP2025 Learning Dynamics of LLM Finetuning. In: ICLR 2025](https://speakerdeck.com/s_mizuki_nlp/lun-wen-du-mihui-snlp2025-learning-dynamics-of-llm-finetuning-in-iclr-2025) - S（2025-08）
- [ローカルLLMでファインチューニング](https://speakerdeck.com/knishioka/rokarullmdehuaintiyuningu) - 西岡 賢一郎 (Kenichiro Nishioka)（2025-06）
- [第13回 Data-Centric AI勉強会, LLMのファインチューニングデータ](https://speakerdeck.com/kajyuuen/di-13hui-data-centric-aimian-qiang-hui-llmnohuaintiyuningudeta) - Koga Kobayashi（2025-02）
- [LLMアプリケーションの Fine-tunningと蒸留を活用した改善](https://speakerdeck.com/pharma_x_tech/llmahurikesiyonno-fine-tunningtozheng-liu-wohuo-yong-sitagai-shan) - PharmaX（旧YOJO Technologies）開発チーム（2024-12）
- [\[輪講資料\] LoRA: Low-Rank Adaptation of Large Language Models](https://speakerdeck.com/hpprc/lun-jiang-zi-liao-lora-low-rank-adaptation-of-large-language-models) - Hayato Tsukagoshi（2023-04）

## LLM 的推理优化・服务部署

让训练好的模型跑得更快、更省的量化、蒸馏与推理基础设施。

- [国産生成AI PLaMoを支える事後学習と推論最適化](https://speakerdeck.com/pfn/20260406_plamo_3_beta_posttrain_and_inference_opt) - Preferred Networks（2026-04）
- [契約書からの情報抽出を行うLLMのスループットを、バッチ処理を用いて最大40%改善した話](https://speakerdeck.com/sansantech/20260326-3) - SansanTech（2026-03）
- [量子化 × ファインチューニングはどの組み合わせから試すべき？](https://speakerdeck.com/sinchir0/liang-zi-hua-x-huaintiyuninkuhatonozu-mihe-wasekarashi-suheki) - sin chir0（2025-11）
- [NLPコロキウム20251022\_超効率化への挑戦: LLM 1bit量子化のロードマップ](https://speakerdeck.com/yumaichikawa/nlpkorokiumu20251022-chao-xiao-lu-hua-henotiao-zhan-llm-1bitliang-zi-hua-norodomatupu) - Yuma Ichikawa（2025-10）
- [PLaMo2シリーズのvLLM実装 / PFN LLM セミナー](https://speakerdeck.com/pfn/20251001-pfn-llm-seminar-plamo-on-vllm) - Preferred Networks（2025-10）
- [リソース制限環境下でのローカルLLM構築術](https://speakerdeck.com/koukimiura/risosuzhi-xian-huan-jing-xia-denorokarullmgou-zhu-shu) - kouki.miura（2025-07）
- [Deploying PLaMo 2 with vLLM: A Practical Guide / vLLM roundup Community Meetup Tokyo](https://speakerdeck.com/pfn/vllm-roundup-community-meetup-tokyo) - Preferred Networks（2025-06）
- [関東Kaggler会LT: 人狼コンペとLLM量子化について](https://speakerdeck.com/nejumi/guan-dong-kagglerhui-lt-ren-lang-konpetollmliang-zi-hua-nituite) - YuyaYAMAMOTO（2025-02）
- [OpenAIの蒸留機能(Model Distillation)を使用して運用中のLLMのコストを削減する取り組み](https://speakerdeck.com/pharma_x_tech/openainozheng-liu-ji-neng-model-distillation-woshi-yong-siteyun-yong-zhong-nollmnokosutowoxue-jian-suruqu-rizu-mi) - PharmaX（旧YOJO Technologies）開発チーム（2024-12）
- [LLMを「速く」「安く」 動かすには / CloudNative Days Winter 2024](https://speakerdeck.com/pfn/cloudnative-days-2024-lean-and-swift-llm-deployment) - Preferred Networks（2024-11）
- [大規模言語モデル (LLM)における低精度数値表現](https://speakerdeck.com/pfn/20240508-hpckenkyukai-pfn-llm) - Preferred Networks（2024-05）

## 评测・基准测试

该如何衡量日语 LLM 与 NLP 系统。

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
- [Auto-evaluation of ranking model by LLM](https://speakerdeck.com/legalontechnologies/auto-evaluation-of-ranking-model-by-llm) - LegalOn Technologies, Inc（2023-10）

## 全文检索・搜索基础设施

搜索引擎与日语分析器、查询理解、排序改善的实务案例。

- [Retriever と Reranker、結局どうする？](https://speakerdeck.com/kazuaki/retriever-to-reranker-jie-ju-dousuru) - hkazuakey（2026-07）
- [AIエージェントのための検索](https://speakerdeck.com/takatorisatoshi/aiezientonotamenojian-suo) - takatori（2026-07）
- [【2026年版】 ベクトル検索とEmbedding最前線](https://speakerdeck.com/mocobeta/2026nian-ban-bekutorujian-suo-embeddingzui-qian-xian) - Tomoko Uchida（2026-06）
- [検索リランキングを事業成果につなげる 評価・改善戦略](https://speakerdeck.com/masakick07/jian-suo-rirankinguwoshi-ye-cheng-guo-nitunageru-ping-jia-gai-shan-zhan-lue) - 田代真生（2026-05）
- [検索設計から 推論設計への重心移動と Recall-First Retrieval](https://speakerdeck.com/po3rin/jian-suo-she-ji-kara-tui-lun-she-ji-henozhong-xin-yi-dong-to-recall-first-retrieval) - po3rin（2026-04）
- [Percolatorを廃止し、マルチ検索サービスへ刷新した話 / Search Engineering Tech Talk 2026 Spring](https://speakerdeck.com/visional_engineering_and_design/search-engineering-tech-talk-2026-spring) - Visional Engineering ＆ Design（2026-04）
- [FessのAI検索モード：検索システムとLLMへの取り組み](https://speakerdeck.com/marevol/fessnoaijian-suo-modo-jian-suo-sisutemutollmhenoqu-rizu-mi) - Shinsuke Sugaya（2026-04）
- [ビズリーチにおける検索・推薦の取り組み / DEIM2026](https://speakerdeck.com/visional_engineering_and_design/deim2026) - Visional Engineering ＆ Design（2026-03）
- [MCPでつなぐElasticsearchとLLM - 深夜の障害対応を楽にしたい / Bridging Elasticsearch and LLMs with MCP](https://speakerdeck.com/sashimimochi/bridging-elasticsearch-and-llms-with-mcp) - Sashimimochi（2026-01）
- [オープンウェイトのLLMリランカーを契約書で評価する / searchtechjp](https://speakerdeck.com/sansan_randd/searchtechjp) - Sansan R&D（2026-01）
- [LegalOn Assistantの契約書検索](https://speakerdeck.com/legalontechnologies/legalonassistant-contractsearch) - LegalOn Technologies, Inc（2025-12）
- [実践マルチモーダル検索！](https://speakerdeck.com/shibuiwilliam/shi-jian-marutimodarujian-suo) - shibuiwilliam（2025-10）
- [社内版ビズリーチ LLMとセマンティックサーチによる新たな人材検索の挑戦 / Search Engineering MEET UP\_2-2](https://speakerdeck.com/visional_engineering_and_design/search-engineering-meet-up-2-2) - Visional Engineering ＆ Design（2025-10）
- [「LINE MUSIC」におけるハイブリッド検索や略称抽出を用いた曖昧検索への挑戦 / Challenges in Ambiguous Search Using Hybrid Search and Abbreviation Extraction in "LINE MUSIC"](https://speakerdeck.com/lycorptech_jp/challenges-in-ambiguous-search-using-hybrid-search-and-abbreviation-extraction-in-line-music) - LINEヤフーTech (LY Corporation Tech)（2025-06）
- [Two-Tower モデルで実現する 検索リランキング / Shibuya\_AI\_2](https://speakerdeck.com/visional_engineering_and_design/shibuya-ai-2) - Visional Engineering ＆ Design（2025-06）
- [ベクトルストア入門](https://www.docswell.com/s/hmatsu47/ZP2LY6-2025-01-19-235645) - hmatsu47(まつ)（2025-02）
- [テキスト検索の原点：全文検索のしくみと活用ポイント](https://speakerdeck.com/segavvy/tekisutojian-suo-noyuan-dian-quan-wen-jian-suo-nosikumitohuo-yong-hointo) - segavvy（2024-01）
- [言語モデルを用いたQuery Categorizationへの取り組み / LM-based query categorization for query understanding](https://speakerdeck.com/pakio/lm-based-query-categorization-for-query-understanding) - Kazuma Arimura（2023-12）
- [レガシーSolrの Elasticseach移行 Cybozu Tech Meetup #14](https://speakerdeck.com/yokotaso/regasisolrfalse-elasticseachyi-xing-cybozu-tech-meetup-number-14) - tomoya yokota（2021-07）
- [ウェブ検索クエリのための部分一致文字列に対するエンティティ名称予測モデルの提案](https://www.docswell.com/s/ydnjp/5GM2L5-2021-03-22-155332) - Yahoo!デベロッパーネットワーク（2021-03）
- [ヤフーにおける機械学習検索ランキングの取り組み](https://speakerdeck.com/szdr/yahuniokeruji-jie-xue-xi-jian-suo-rankingufalsequ-rizu-mi) - sz_dr（2019-12）
- [Elasticsearch における類似度ベクトル検索のベストプラクティスを求めて/es-vector-search](https://speakerdeck.com/takahiko03/es-vector-search) - Takahiko Ito（2019-07）
- [社内ドキュメント検索システム構築のノウハウ](https://speakerdeck.com/marevol/she-nei-dokiyumentojian-suo-sisutemugou-zhu-falsefalseuhau) - Shinsuke Sugaya（2019-04）
- [実践！Elasticsearch + Sudachi を用いた全文検索エンジン](https://www.slideshare.net/ssuser7eadbf/elasticsearch-sudachi) - S. T.（2019-04）
- [「いい検索」を考える](https://speakerdeck.com/rtechkouhou/iijian-suo-wokao-eru) - Recruit Technologies（2019-02）
- [日本最大級の求人検索エンジン「スタンバイ」を支える技術](https://speakerdeck.com/marevol/ri-ben-zui-da-ji-falseqiu-ren-jian-suo-enzin-sutanbai-wozhi-eruji-shu) - Shinsuke Sugaya（2018-05）
- [Solrで日本語全文検索システムの構築と応用](https://www.slideshare.net/syutahashimoto/solr-79837656) - Syuta Hashimoto（2017-09）
- [全文検索システムFessを用いた 検索システム構築入門](https://speakerdeck.com/marevol/quan-wen-jian-suo-sisutemufesswoyong-ita-jian-suo-sisutemugou-zhu-ru-men) - Shinsuke Sugaya（2017-01）
- [Elasticsearchベースの全文検索システムFess](https://www.slideshare.net/slideshow/elasticsearchfess/63500978) - Shinsuke Sugaya（2016-06）
- [リクルート流Elasticsearchの使い方](https://www.slideshare.net/recruitcojp/elasticsearch-56355817) - Recruit Technologies（2015-12）
- [Luceneと日本語の検索](https://speakerdeck.com/johtani/lucenetori-ben-yu-falsejian-suo) - Jun Ohtani（2014-12）
- [SQLiteで高速全文検索〜日本語編〜](https://speakerdeck.com/shoby/sqlitedegao-su-quan-wen-jian-suo-ri-ben-yu-bian) - shoby（2014-08）
- [SolrとElasticsearchを比べてみよう](https://www.slideshare.net/shinsuke/solr-vses2014) - Shinsuke Sugaya（2014-05）

## 检索・RAG

检索增强生成（RAG）的设计、改善与评测。

- [【Paper&Hacks Vol.89】RAGアプリハンズオン～LLM/Embedding選択～](https://www.docswell.com/s/matsuo-lab_llm/Z8NRJE-Paper&HacksVol.89) - 松尾研LLMコミュニティ（2026-08）
- [【Paper&Hacks Vol.80】RAGを測るモノサシを作ろう 〜 Ragas × LangSmithでRAG評価アプリ開発 〜](https://www.docswell.com/s/matsuo-lab_llm/KWRGP8-Paper&HacksVol.80) - 松尾研LLMコミュニティ（2026-08）
- [2026年はチャンキングを極める！](https://speakerdeck.com/shibuiwilliam/2026nian-hatiyankinguwoji-meru) - shibuiwilliam（2026-01）
- [LegalドメインにおけるRAG精度改善フロー](https://speakerdeck.com/legalontechnologies/legaldomain-rag-accuracyimprovement-flow) - LegalOn Technologies, Inc（2025-12）
- [Pythonで構築する全国市町村ナレッジグラフ: GraphRAGを用いた意味的地域検索への応用](https://speakerdeck.com/negi111111/pythondegou-zhu-suruquan-guo-shi-ting-cun-naretuzigurahu-graphragwoyong-itayi-wei-de-di-yu-jian-suo-henoying-yong) - negi111111（2025-11）
- [OpenProvence - クエリに関連しない文章削除モデル日本語版の作成と公開](https://speakerdeck.com/hotchpotch/openprovence-kueriniguan-lian-sinaiwen-zhang-xue-chu-moderuri-ben-yu-ban-nozuo-cheng-togong-kai) - Yuichi Tateno（2025-10）
- [Azure AI SearchでAgentic Retreival](https://speakerdeck.com/takatorisatoshi/azure-ai-searchdeagentic-retreival) - takatori（2025-10）
- [Temporal Knowledge Graphで作る！ 時間変化するナレッジを扱うAI Agentの世界](https://speakerdeck.com/po3rin/temporal-knowledge-graphdezuo-ru-shi-jian-bian-hua-surunaretuziwoxi-uai-agentnoshi-jie) - po3rin（2025-10）
- [【検索勉強会2024春】RAG改善からみたクエリ・ドキュメント理解とリランキング](https://speakerdeck.com/mzntaka0/jian-suo-mian-qiang-hui-2024chun-raggai-shan-karamitakueridokiyumentoli-jie-torirankingu) - mzntaka0（2025-09）
- [Ask! NIKKEI RAG検索技術の深層](https://speakerdeck.com/hotchpotch/ask-nikkei-ragjian-suo-ji-shu-noshen-ceng) - Yuichi Tateno（2025-02）
- [LLMによるRAG評価用合成テストデータの生成](https://speakerdeck.com/licux/llmniyoruragping-jia-yong-he-cheng-tesutodetanosheng-cheng) - matsukada（2025-01）
- [LLMアプリをRagasで評価して、Langfuseで可視化しよう！](https://speakerdeck.com/minorun365/llmapuriworagasdeping-jia-site-langfusedeke-shi-hua-siyou) - みのるん（2024-10）
- [実務におけるRAG 〜学びと現場のノウハウ〜](https://www.docswell.com/s/hoxo-m_inc/K4V3MW-rag) - 株式会社ホクソエム（2024-07）

## LLM 应用开发・运维

把 LLM 放进产品并持续运维所需的知识。

- [PLaMo 3.0 Primeの構造化出力サポート](https://speakerdeck.com/pfn/20260730_pfn_llm_2_structured_output) - Preferred Networks（2026-07）
- [LangfuseによるLLMOps基盤の構築と活用事例](https://speakerdeck.com/zozotech/llmops-platform-with-langfuse) - ZOZO Developers（2026-07）
- [SQL/ID抽出タスクから考える 実践的なハルシネーション対策](https://speakerdeck.com/nearme_tech/safe-llm-usage-in-development) - NearMe（2026-05）
- [複数プロダクト利用を前提としたセルフホストLangfuse導入事例 / shibuya\_AI\_4](https://speakerdeck.com/sansan_randd/shibuya-ai-4) - Sansan R&D（2026-02）
- [LLMアプリの品質保証](https://speakerdeck.com/cybozuinsideout/llm-app-qa-study-session) - Cybozu（2026-02）
- [LLMアプリケーション開発におけるセキュリティリスクと対策 / LLM Application Security](https://speakerdeck.com/flatt_security/llm-application-security) - GMO Flatt Security（2025-09）
- [企業の生成AIガバナンスにおけるエージェントとセキュリティ](https://speakerdeck.com/lycorptech_jp/enterprise-ai-governance-agent-security) - LINEヤフーTech (LY Corporation Tech)（2025-09）
- [LLMアプリケーションの品質担保に向けた プラクティスと LLMオブザーバビリティツール](https://speakerdeck.com/olachinkei/llmapurikesiyonnopin-zhi-dan-bao-nixiang-keta-purakuteisuto-llmobuzababiriteituru) - Keisuke Kamata（2025-04）
- [【DeNA × AI Day】 LLMの事業適用を加速させるLLMOps](https://www.docswell.com/s/DeNA_Tech/5EX9M6-aiday-specific-1630) - DeNA_Tech（2025-02）
- [LLMアプリケーションの評価と継続的改善](https://speakerdeck.com/pharma_x_tech/llmapurikesiyonnoping-jia-toji-sok-de-gai-shan) - PharmaX（旧YOJO Technologies）開発チーム（2024-11）
- [AOAI Dev Day LLMシステム開発 Tips集](https://speakerdeck.com/hirosatogamo/aoai-dev-day-llmsisutemukai-fa-tipsji) - Hirosato Gamo（2024-07）
- [AIアプリケーションの落とし穴](https://speakerdeck.com/yusukejustinnakajima/aiapurikesiyonnoluo-tosixue) - YusukeJustinNakajima（2024-05）
- [LangSmith入門―トレース／評価／プロンプト管理などを担うLLMアプリ開発プラットフォーム](https://speakerdeck.com/os1ma/langsmithru-men-toresu-slash-ping-jia-slash-puronputoguan-li-nadowodan-ullmapurikai-fa-puratutohuomu) - os1ma（2024-04）
- [いまこそ学ぶLLMベースのAIエージェント入門―基本的なしくみ／開発ツール／有名なOSSや論文の紹介](https://speakerdeck.com/os1ma/imakosoxue-bullmbesunoaiezientoru-men-ji-ben-de-nasikumi-slash-kai-fa-turu-slash-you-ming-naossyalun-wen-noshao-jie) - os1ma（2024-02）
- [LLMの出⼒制御問題とSansan Labsにおける「Output Parsers」の活⽤ / LLM Output Control Issues and the Use of "Output Parsers" in Sansan Labs](https://speakerdeck.com/sansan_randd/llm-output-control-issues-and-the-use-of-output-parsers-in-sansan-labs) - Sansan R&D（2023-11）
- [LLM研究会\_社外公開版\_プロンプトを改善する15のヒント](https://speakerdeck.com/chiami_kayama/llmyan-jiu-hui-she-wai-gong-kai-ban-puronputowogai-shan-suru15nohinto) - C.Kayama（2023-10）
- [ChatGPT - LLMシステム開発大全](https://speakerdeck.com/hirosatogamo/chatgpt-azure-openai-da-quan) - Hirosato Gamo（2023-07）
- [プロンプトエンジニアリングから始めるLangChain入門](https://speakerdeck.com/os1ma/puronputoenziniaringukarashi-merulangchainru-men) - os1ma（2023-04）

## 文本分类・情感分析

把文档和评论归入标签的分类任务，以及内容审核等实务应用。

- [LLMを用いた擬似ラベルデータセットによる記事分類タスクの精度改善/yans2025](https://speakerdeck.com/nikkei_engineer_recruiting/yans2025) - 日本経済新聞社 エンジニア採用事務局（2025-10）
- [OPENREC.tv におけるLLMを活用した監視効率化](https://speakerdeck.com/clom/openrec-dot-tv-niokerullmwohuo-yong-sitajian-shi-xiao-lu-hua) - Kento Nomiyama（2024-10）
- [ChatGPTを活用した悪意のあるコメント抽出AI開発の可能性](https://www.docswell.com/s/KunihiroSugiyama/524D39-2024-04-16-110104) - Kunihiro Sugiyama（2024-04）
- [gpt-3.5-turboのFine-tuningによる分類タスク改善の試み](https://speakerdeck.com/nyosu/gpt-3-dot-5-turbonofine-tuningniyorufen-lei-tasukugai-shan-noshi-mi-527dddc7-3c18-4c10-9842-de4c312886a1) - Nyosu（2023-08）
- [NLP2023 分類タスクにおける不確実性の高い文章の傾向調査](https://speakerdeck.com/masatoto/nlp2023-fen-lei-tasukuniokerubu-que-shi-xing-nogao-iwen-zhang-noqing-xiang-diao-cha) - masatoto（2023-03）
- [Pocochaにおける規約違反検知のための機械学習の活用【DeNA TechCon 2021 Autumn】/techcon2021autumn-08](https://speakerdeck.com/dena_tech/techcon2021autumn-08) - DeNA_Tech（2021-09）
- [【Ltech#15】Well-beingを測る「LIFE WILL」開発の舞台裏](https://www.docswell.com/s/LIFULL/ZY9YPK-Well-being%E3%82%92%E6%B8%AC%E3%82%8B%E3%80%8CLIFEWILL%E3%80%8D%E9%96%8B%E7%99%BA%E3%81%AE%E8%88%9E%E5%8F%B0%E8%A3%8F) - 株式会社LIFULL（2021-03）
- [感情分析に使う極性辞書を生成してみる](https://speakerdeck.com/kanto/gan-qing-fen-xi-nishi-uji-xing-ci-shu-wosheng-cheng-sitemiru) - g-k（2020-06）
- [Neural Architecture Searchを用いて出品違反検知モデリングを高速化したお話](https://speakerdeck.com/dkumazaw/neural-architecture-searchwoyong-itechu-pin-wei-fan-jian-zhi-moderinguwogao-su-hua-sitaohua) - Daiki Kumazawa（2019-05）
- [MeCabとKerasを使ったテキスト分類](https://speakerdeck.com/itagakim/mecabtokeraswoshi-tutatekisutofen-lei) - masa-ita（2019-02）
- [要望分析のための投稿テキストのカテゴリ分類支援 / Assisting Text Classification for Request Post Analysis](https://speakerdeck.com/sansandsoc/assisting-text-classification-for-request-post-analysis) - Sansan DSOC（2019-02）
- [複数言語複数タスクを扱う発話意図推定モデリングのための敵対的学習の検討](https://speakerdeck.com/ryomasumura/fu-shu-yan-yu-fu-shu-tasukuwoxi-ufa-hua-yi-tu-tui-ding-moderingufalsetamefalsedi-dui-de-xue-xi-falsejian-tao) - Ryo Masumura（2018-12）
- [Percolatorを用いたカテゴリ分類](https://speakerdeck.com/tarao/percolatorwoyong-itakategorifen-lei) - INA Lintaro（2018-08）
- [fastTextでテキスト情報から レシピ分類器を作った話](https://speakerdeck.com/atlimited/fasttextdetekisutoqing-bao-kara-resipifen-lei-qi-wozuo-tutahua) - Yusuke Takagi（2017-05）
- [TFUG#3 RettyにおけるDeep Learningの自然言語処理への応用事例](https://speakerdeck.com/bokeneko/tfug-number-3-rettyniokerudeep-learningfalsezi-ran-yan-yu-chu-li-hefalseying-yong-shi-li) - bokeneko（2017-02）
- [ニューラルネットワークでニュース記事を自動分類してみた](https://speakerdeck.com/tsurubee/niyurarunetutowakuteniyusuji-shi-wozi-dong-fen-lei-sitemita) - tsurubee（2017-01）
- [Pythonで動かして学ぶ機械学習入門第二回 評判分析](https://speakerdeck.com/diracdiego/pythondedong-kasitexue-buji-jie-xue-xi-ru-men-di-er-hui-ping-pan-fen-xi) - yoppe（2016-09）
- [CNNによるテキスト分類](https://speakerdeck.com/tkengo/cnnniyorutekisutofen-lei) - けんご（2016-03）

## 信息抽取・命名实体・标注

从文本取出结构化信息的技术，以及支撑它的训练数据。

- [メールから送信者情報を抽出するタスクの奥深さ / kyoto\_ai\_meetup\_1](https://speakerdeck.com/sansan_randd/kyoto-ai-meetup-1) - Sansan R&D（2026-02）
- [アノテーション作業書作成のGood Practice](https://speakerdeck.com/cierpa0905/anotesiyonzuo-ye-shu-zuo-cheng-nogood-practice) - Cierpa & Company（2025-10）
- [AI Frontiers Revealed: Transforming LINE Shopping TW with LLM-Driven Product Attribute Extraction](https://speakerdeck.com/lycorptech_jp/ai-frontiers-revealed-transforming-line-shopping-tw-with-llm-driven-product-attribute-extraction) - LINEヤフーTech (LY Corporation Tech)（2025-07）
- [診断前の病歴テキストを対象としたLLMによるエンティティリンキング精度検証](https://speakerdeck.com/hagino3000/zhen-duan-qian-nobing-li-tekisutowodui-xiang-tositallmniyoruenteiteirinkinkujing-du-jian-zheng) - Takashi Nishibayashi（2025-05）
- [AIの血肉となるアノテーションデータのために大事にしている事](https://speakerdeck.com/cyberagentdevelopers/ainoxie-rou-tonaruanotesiyondetanotamenida-shi-nisiteirushi) - CyberAgent（2024-11）
- [メールからの名刺情報抽出におけるLLM活用 / Use of LLM in extracting business card information from e-mails](https://speakerdeck.com/sansan_randd/use-of-llm-in-extracting-business-card-information-from-e-mails) - Sansan R&D（2024-11）
- [日本語エンティティリンキングのための行政機関ウェブ文書コーパスの構築 (CADEL)](https://speakerdeck.com/shigashiyama/cadel-at-ipsj-nl-260) - shigashiyama（2024-06）
- [ストックマークテックミートアップ#8 / Stockmark Tech MeetUp#8](https://speakerdeck.com/stockmark/stockmark-tech-meetup-number-8) - Stockmark（2024-02）
- [場所参照表現と位置情報を紐付けるジオコーディングの概観と発展に向けての考察 / 言語処理学会第29回年次大会(NLP2023)](https://speakerdeck.com/sorami/nlp2023) - Sorami Shiromizu（2023-03）
- [継続して改善する固有表現抽出 / Continuous improvement of named entity extraction](https://speakerdeck.com/sansanbuildersbox/continuous-improvement-of-named-entity-extraction) - Sansan（2021-11）
- [jel: japanese entity linker](https://speakerdeck.com/izuna385/jel-japanese-entity-linker) - izuna385（2021-09）
- [実務で使う固有表現抽出 / Practical Use of Named Entity Recognition](https://speakerdeck.com/sansandsoc/practical-use-of-named-entity-recognition) - Sansan DSOC（2020-10）
- [ニュース配信における固有表現抽出の取り組み / Extraction of Unique Expressions in News Distribution](https://speakerdeck.com/sansandsoc/extraction-of-unique-expressions-in-news-distribution) - Sansan DSOC（2020-09）
- [株式会社ABEJA\_アノテーションにおける運用上のノウハウの紹介](https://speakerdeck.com/gokiritani/zhu-shi-hui-she-abeja-afalsetesiyonniokeruyun-yong-shang-falsefalseuhaufalseshao-jie) - Go（2020-04）
- [多言語統語・意味情報コーパスParallel Meaning Bank日本語版の構築](https://www.slideshare.net/slideshow/parallel-meaning-bank/230689876) - Hitomi Yanaka（2020-03）
- [自然言語処理向け データアノテーションとそのユースケース](https://www.slideshare.net/DeepLearningLab/ss-180667732) - Deep Learning Lab（ディープラーニング・ラボ）（2019-10）
- [完全なアノテーションが得られない状況下での固有表現抽出](https://speakerdeck.com/kajyuuen/wan-quan-naafalsetesiyongade-rarenaizhuang-kuang-xia-defalsegu-you-biao-xian-chou-chu) - Koga Kobayashi（2019-09）
- [ニューラル固有表現抽出 / Neural Named Entity Recognition](https://speakerdeck.com/himkt/neural-named-entity-recognition) - himkt（2019-03）
- [言語処理学会年次大会(NLP2019) F1-1 ウェブ検索クエリに対する周辺語を考慮した教師なしエンティティリンキング #nlp2019](https://www.docswell.com/s/ydnjp/5D7YDK-2019-03-18-150155) - Yahoo!デベロッパーネットワーク（2019-03）
- [ニューラル固有表現抽出器を実装してみる / PyNER](https://speakerdeck.com/himkt/pyner) - himkt（2018-12）
- [専門用語抽出手法の研究と 抽出アプリケーションの開発](https://speakerdeck.com/kajyuuen/zhuan-men-yong-yu-chou-chu-shou-fa-falseyan-jiu-to-chou-chu-apurikesiyonfalsekai-fa) - Koga Kobayashi（2018-09）
- [Solr から使う OpenNLP の日本語固有表現抽出](https://www.slideshare.net/KojiSekiguchi/solr-opennlp-106671440) - Koji Sekiguchi（2018-07）
- [述語項構造と照応関係のアノテーション](https://speakerdeck.com/kakubari/shu-yu-xiang-gou-zao-tozhao-ying-guan-xi-falseafalsetesiyon) - kakubari（2017-05）
- [クックパッド特売情報における自然言語処理 〜固有表現抽出を利用した検索システム〜](https://www.slideshare.net/abicky/ss-52441786) - Takeshi Arabiki（2015-09）
- [株式会社ブレインパッド\_テクニカルナレッジ共有会#10 「ブートストラップ法による自然言語処理」白井尊昭](https://speakerdeck.com/brainpad/zhu-shi-hui-she-bureinpatudo-tekunikarunaretuzigong-you-hui-number-10-butosutoratupufa-niyoruzi-ran-yan-yu-chu-li-bai-jing-zun-zhao) - brainpad-inc（2014-09）
- [言語資源と付き合う](https://www.slideshare.net/unnonouno/ss-13236436) - Yuya Unno（2012-06）

## 文档处理・OCR

把表单、合同、名片等真实世界的文档转成数据的技术。

- [BizDocVQA: 実世界ビジネス帳票に対する根拠付きVQAデータセットの提案](https://speakerdeck.com/icoxfog417/biz-doc-vqa-dataset) - Takahiro Kubo（2026-03）
- [Large Vision Language Modelを用いた 文書画像データ化作業自動化の検証、運用 / shibuya\_AI](https://speakerdeck.com/sansan_randd/shibuya-ai) - Sansan R&D（2025-10）
- [帳票構造化タスクにおけるLLMファインチューニングの性能評価](https://speakerdeck.com/yosukeyoshida/zhang-piao-gou-zao-hua-tasukuniokerullmhuaintiyuningunoxing-neng-ping-jia) - yosukeyoshida（2025-07）
- [ビジネス文書に特化した基盤モデル開発 / SaaSxML\_Session\_2](https://speakerdeck.com/sansan_randd/saasxml-session-2) - Sansan R&D（2025-07）
- [文書画像のデータ化における VLM活用 / Use of VLM in document image data conversion](https://speakerdeck.com/sansan_randd/use-of-vlm-in-document-image-data-conversion) - Sansan R&D（2024-11）
- [FiftyOneを用いたOCRモデルの比較 / Comparing OCR Models using FiftyOne](https://speakerdeck.com/moneyforward/comparing-ocr-models-using-fiftyone) - Money Forward, Inc.（2024-09）
- [【DeNATechCon2024】未来医療の革新 AIを活用した医療情報の効率的構造化](https://www.docswell.com/s/DeNA_Tech/KYW4GP-2024-02-29-090538) - DeNA_Tech（2024-02）
- [LLM時代におけるAI-OCR機能の開発戦略 / layerx-bakuraku-ocr-llm-lt-2024](https://speakerdeck.com/yuya4/layerx-bakuraku-ocr-llm-lt-2024) - Yuya Matsumura（2024-01）
- [Contract One における契約書解析技術の開発 / Development of Contract Analysis Technology in Contract One](https://speakerdeck.com/sansan_randd/development-of-contract-analysis-technology-in-contract-one) - Sansan R&D（2023-12）
- [バクラクのAI-OCR機能の体験を支える良質なデータセット作成の仕組み / data-centric-ai-bakuraku-dataset](https://speakerdeck.com/yuya4/data-centric-ai-bakuraku-dataset) - Yuya Matsumura（2023-06）
- [LayerXにおける機械学習を活用した請求書OCR機能に関する取り組み / deim2023-layerx-ai-ocr](https://speakerdeck.com/yuya4/deim2023-layerx-ai-ocr) - Yuya Matsumura（2023-03）

## 问答・知识

处理知识的语言模型与问答系统。

- [An Open and Reproducible Deep Research Agent for Long-Form Question Answering](https://speakerdeck.com/ikuyamada/an-open-and-reproducible-deep-research-agent-for-long-form-question-answering) - Ikuya Yamada（2025-12）
- [知識強化言語モデルLUKE @ LUKEミートアップ](https://speakerdeck.com/ikuyamada/zhi-shi-qiang-hua-yan-yu-moderuluke-at-lukemitoatupu) - Ikuya Yamada（2025-01）
- [知識拡張型言語モデルLUKE](https://speakerdeck.com/ikuyamada/zhi-shi-kuo-zhang-xing-yan-yu-moderuluke) - Ikuya Yamada（2023-03）
- [最先端の質問応答技術の研究開発と迅速な実用化ーStudio Ousiaでの取り組みー](https://speakerdeck.com/ikuyamada/zui-xian-duan-nozhi-wen-ying-da-ji-shu-noyan-jiu-kai-fa-toxun-su-nashi-yong-hua-studio-ousiadenoqu-rizu-mi) - Ikuya Yamada（2023-03）
- [Elasticsearchによる質問応答～NLP機械学習モデルの利用～](https://speakerdeck.com/shin_higuchi/elasticsearchniyoruzhi-wen-ying-da-nlpji-jie-xue-xi-moderunoli-yong) - 樋口慎（2022-08）
- [Efficient Passage Retrieval with Hashing for Open-domain Question Answering (ACL 2021)](https://speakerdeck.com/ikuyamada/efficient-passage-retrieval-with-hashing-for-open-domain-question-answering-acl-2021) - Ikuya Yamada（2022-05）
- [加藤拓真, 宮脇峻平, 第二回AI王最終報告会 - DPR ベースラインによる オープンドメイン質問応答の取り組み (2022)](https://speakerdeck.com/smiyawaki0820/jia-teng-tuo-zhen-gong-xie-jun-ping-di-er-hui-aiwang-zui-zhong-bao-gao-hui-dpr-besurainniyoru-opundomeinzhi-wen-ying-da-falsequ-rizu-mi-2022) - Shumpei Miyawaki（2022-03）
- [AutoGluon-Tabular を用いたアンサンブルによる日本語質問応答システムの構築 / AIO solution by AutoGluon-Tabular](https://speakerdeck.com/upura/aio-solution-by-autogluon-tabular) - Shotaro Ishihara（2021-03）
- [知識ベースの自然言語処理への活用](https://speakerdeck.com/ikuyamada/zhi-shi-besufalsezi-ran-yan-yu-chu-li-hefalsehuo-yong) - Ikuya Yamada（2021-03）
- [オープンドメイン質問応答技術の最新動向](https://speakerdeck.com/ikuyamada/opundomeinzhi-wen-ying-da-ji-shu-falsezui-xin-dong-xiang) - Ikuya Yamada（2021-03）

## 机器翻译

翻译模型的研究开发，以及翻译服务的实现。

- [plamo-3-translateの開発](https://speakerdeck.com/pfn/20260730_pfn_llm_3_plamo-3-translate) - Preferred Networks（2026-07）
- [古典日本語の現代語機械翻訳のための評価資源の整備](https://speakerdeck.com/shigashiyama/20260318-aamt) - shigashiyama（2026-03）
- [自動同時音声翻訳技術の進展とこれからの展望（九州大学アジアウィーク2025 Webセミナー）](https://speakerdeck.com/ksudoh/zi-dong-tong-shi-yin-sheng-fan-yi-ji-shu-nojin-zhan-tokorekaranozhan-wang-jiu-zhou-da-xue-aziauiku2025-websemina) - Katsuhito Sudoh（2025-11）
- [PLaMo翻訳 〜もう不自然な機械翻訳とはサヨナラ!PLaMo翻訳が変革するビジネス〜](https://speakerdeck.com/pfn/20251014-plamo-translate-ceatec2025) - Preferred Networks（2025-10）
- [大規模言語モデル時代の機械翻訳の展望](https://speakerdeck.com/shigashiyama/20241108-cs-llmmt) - shigashiyama（2024-11）
- [機械翻訳をローカルマシンで( ArgosTranslate/LibreTranslate )](https://speakerdeck.com/matoken/libretranslate) - Kenichiro MATOHARA（2022-12）
- [機械翻訳とエンコーダデコーダモデル](https://speakerdeck.com/kyaonn/ji-jie-fan-yi-toenkodadekodamoderu) - Kyao（2022-05）
- [【SIG-SLP 141 招待講演】 IWSLT Evaluation Campaign: Simultaneous Speech Translation](https://speakerdeck.com/ksudoh/sig-slp-141-zhao-dai-jiang-yan-iwslt-evaluation-campaign-simultaneous-speech-translation) - Katsuhito Sudoh（2022-03）
- [AWSを活用した機械翻訳のためのGPU並列処理環境の構築/aso](https://speakerdeck.com/stockmark/aso) - Stockmark（2021-06）
- [機械翻訳コンペティション参加報告](https://speakerdeck.com/butsugiri/ji-jie-fan-yi-konpeteisiyoncan-jia-bao-gao) - Shun Kiyono（2021-02）
- [「機械翻訳」Chapter 2 機械翻訳の自動評価と統計的検定](https://speakerdeck.com/sei88888/ji-jie-fan-yi-chapter-2-ji-jie-fan-yi-falsezi-dong-ping-jia-totong-ji-de-jian-ding) - Seitaro Shinagawa（2020-08）
- [大規模な論文対訳データを利用した高精度な中日、英日ニューラル機械翻訳の開発](https://www.slideshare.net/ToshiakiNakazawa/ss-83451641) - Toshiaki Nakazawa（2017-12）
- [ニューラル機械翻訳の動向@IBIS2017](https://www.slideshare.net/slideshow/ibis2017/81833961) - Toshiaki Nakazawa（2017-11）
- [EMNLP2015読み会：Effective Approaches to Attention-based Neural Machine Translation](https://speakerdeck.com/tkng/emnlp2015du-mihui-effective-approaches-to-attention-based-neural-machine-translation) - tkng（2015-10）
- [機械翻訳の今昔物語](https://www.slideshare.net/hirsoshnakagawa3/ss-39911667) - Hiroshi Nakagawa（2014-10）

## 多模态・视觉与语言

连接图像与语言的模型研究开发，以及把 VLM 装进产品的实践案例。

- [FAXが現役の業界でマルチモーダルAIプロダクトを作る](https://speakerdeck.com/kakehashi/building-multimodal-ai-products) - KAKEHASHI（2026-03）
- [【Gen-AX】20260115開催\_マルチモーダルAI技術勉強会TL会登壇\_CTO 木田](https://speakerdeck.com/genax/gen-ax-20260115kai-cui-marutimodaruaiji-shu-mian-qiang-hui-tlhui-deng-tan-cto-mu-tian) - Gen-AX株式会社（2026-01）
- [Qwen3-VL入門：推論・物体検出・SFTまで](https://speakerdeck.com/bekku/qwen3-vlru-men-tui-lun-wu-ti-jian-chu-sftmade) - bekku_zer（2025-12）
- [言語だけじゃない！Qwen VLモデルの実力 The Power of Qwen VL:Beyond Language](https://speakerdeck.com/sawanochika/yan-yu-dakeziyanai-qwen-vlmoderunoshi-li-the-power-of-qwen-vl-beyond-language) - Sawa（2025-05）
- [VLMを用いた表の質問応答:画像とテキスト入力の性能比較-](https://speakerdeck.com/eida/vlmwoyong-itabiao-nozhi-wen-ying-da-hua-xiang-totekisutoru-li-noxing-neng-bi-jiao) - eida（2025-04）
- [2025-04-24 "Manga AI Understanding & Localization" Furukawa Arata (CyberAgent, Inc)](https://speakerdeck.com/ornew/2025-04-24-cyberagent-inc-manga-ai-understanding-and-localization) - Arata Furukawa（2025-04）
- [大規模日本語VLM Asagi-VLMにおける合成データセットの構築とモデル実装](https://speakerdeck.com/kuehara/da-gui-mo-ri-ben-yu-vlm-asagi-vlmniokeruhe-cheng-detasetutonogou-zhu-tomoderushi-zhuang) - Kohei Uehara（2025-03）
- [マルチモーダルLLM 実践的活用と課題](https://speakerdeck.com/sakaguchikou/marutimodarullm-shi-jian-de-huo-yong-toke-ti) - SakaguchiKou（2024-12）
- [Large Vision Language Model (LVLM) に関する最新知見まとめ (Part 1)](https://speakerdeck.com/onely7/large-vision-language-model-lvlm-niguan-suruzui-xin-zhi-jian-matome-part-1) - Daiki Shiono（2024-11）
- [【Pycon mini 東海 2024】Google Colaboratoryで試すVLM](https://speakerdeck.com/kazuhitotakahashi/pycon-mini-dong-hai-2024-google-colaboratorydeshi-suvlm) - 高橋かずひと（2024-11）
- [マルチモーダル AI 実装の課題と解決策 / Developer X Summit](https://speakerdeck.com/upura/developer-x-summit) - Shotaro Ishihara（2024-11）
- [マルチモーダルRAGやってみた](https://speakerdeck.com/tanimon/marutimodaruragyatutemita) - tanimon（2024-10）
- [大規模言語モデルを用いた日本語視覚言語モデルの評価方法とベースラインモデルの提案 【MIRU 2024】](https://speakerdeck.com/kentosasaki/da-gui-mo-yan-yu-moderuwoyong-itari-ben-yu-shi-jue-yan-yu-moderunoping-jia-fang-fa-tobesurainmoderunoti-an-miru-2024-c2e6ec07-bd66-4a2f-866d-bf3a2fd72ef5) - Kento Sasaki（2024-08）
- [大規模言語モデルによる視覚・言語の融合/Large Vision Language Models](https://speakerdeck.com/ryotatanaka/large-vision-language-models) - Ryota Tanaka（2024-07）
- [【Gemini本発売記念】npaka による マルチモーダルとローカルLLMの現在と未来](https://speakerdeck.com/npaka/geminiben-fa-mai-ji-nian-npaka-niyoru-marutimodarutorokarullmnoxian-zai-towei-lai) - npaka（2024-06）
- [日本語Vision-Languageモデルの学習と評価ベンチマークの構築](https://speakerdeck.com/yuyamaguchi/ri-ben-yu-vision-languagemoderunoxue-xi-toping-jia-bentimakunogou-zhu) - Yu Yamaguchi（2024-06）
- [マルチモーダルLLMがもたらすビジネス革新と技術解説](https://speakerdeck.com/elith/marutimodarullmgamotarasubizinesuge-xin-toji-shu-jie-shuo) - Elith（2024-03）
- [マルチモーダル生成AIの最前線～アプリケーションと考えるべきリスク～](https://speakerdeck.com/yusukejustinnakajima/marutimodarusheng-cheng-ainozui-qian-xian-apurikesiyontokao-erubekirisuku) - YusukeJustinNakajima（2024-02）
- [テキストからの実世界理解に向けて](https://speakerdeck.com/shuheikurita/tekisutokaranoshi-shi-jie-li-jie-nixiang-kete) - Shuhei Kurita（2023-10）
- [⼤規模⾔語モデルとVision-and-Language](https://speakerdeck.com/kosuken/gui-mo-yu-moderutovision-and-language) - Kosuke Nishida（2023-10）
- [SSII2023 \[OS1\] GPT-4とVision-and-Languageの未来](https://speakerdeck.com/ssii/ssii2023-os1-04) - 画像センシングシンポジウム（2023-06）
- [Vision and Languageの現状と展望（GPT-4）](https://speakerdeck.com/sgnm/vision-and-languagenoxian-zhuang-tozhan-wang-gpt-4) - Masanori Suganuma（2023-03）
- [文書画像に対する質問応答技術の最新動向/ Recent Trends in Document Visual Question Answering](https://speakerdeck.com/ryotatanaka/recent-trends-in-document-visual-question-answering) - Ryota Tanaka（2022-03）
- [Vision and Language とその先へ](https://speakerdeck.com/yushiku/vision-and-language-tosofalsexian-he) - Yoshitaka Ushiku（2022-02）
- [言語と視覚に基づく質問応答の最新動向 / Recent Trends in Vision-and-Language Studies for QA](https://speakerdeck.com/kyoun/recent-trends-in-vision-and-language-studies-for-qa) - Kyosuke Nishida（2021-03）
- [事前学習言語モデルを用いたVision & Languageの動向 / A Survey of Pre-trained Language Models for Vision & Language](https://speakerdeck.com/kyoun/a-survey-of-pre-trained-language-models-for-vision-and-language) - Kyosuke Nishida（2019-11）
- [Deep Learning による視覚×言語融合の最前線](https://speakerdeck.com/yushiku/deep-learning-niyorushi-jue-xyan-yu-rong-he-falsezui-qian-xian) - Yoshitaka Ushiku（2017-03）

## 语音识别・语音处理

把语音转换为文本的语音识别，以及作为其基础的语音处理与语音基础模型。

- [会議AIエージェントに話者認識AIを乗せる難しさと重要性](https://speakerdeck.com/nishikainc/hui-yi-aiezientonihua-zhe-ren-shi-aiwocheng-serunan-sisatozhong-yao-xing) - Nishika-Inc（2026-08）
- [ASRは精度だけでは足りない − 専門用語の誤認識にどう向き合うか](https://speakerdeck.com/nishikainc/asrhajing-du-dakedehazu-rinai-zhuan-men-yong-yu-nowu-ren-shi-nidouxiang-kihe-uka) - Nishika-Inc（2026-08）
- [文字起こし基盤の信頼性](https://speakerdeck.com/abnoumaru/wen-zi-qi-kosiji-pan-noxin-lai-xing) - abnoumaru（2026-07）
- [軽量音声認識OSS Parapper](https://speakerdeck.com/nadare881/qing-liang-yin-sheng-ren-shi-oss-parapper) - nadare（2026-06）
- [パソコンで使える日本語AI音声入力の比較（2026年3月版）](https://speakerdeck.com/frievea/pasokondeshi-eruri-ben-yu-aiyin-sheng-ru-li-nobi-jiao-2026nian-3yue-ban) - Frieve-A（2026-03）
- [Gemini APIで音声文字起こし-実装の工夫と課題解決](https://speakerdeck.com/tkikuchi/gemini-apideyin-sheng-wen-zi-qi-kosi-shi-zhuang-nogong-fu-toke-ti-jie-jue) - t-kikuchi（2026-01）
- [LLMが読唇術？視覚音声認識最前線](https://www.docswell.com/s/hiroga/ZPG7JQ-2025-10-21-VSR-LLM) - Hiroaki Ogasawara（2025-10）
- [音声感情認識技術の進展と展望](https://speakerdeck.com/nagase/yin-sheng-gan-qing-ren-shi-ji-shu-nojin-zhan-tozhan-wang) - Ryotaro Nagase（2025-10）
- [Interspeech2025読み会](https://speakerdeck.com/ksudoh/interspeech2025du-mihui) - Katsuhito Sudoh（2025-09）
- [音素BERTと音声基盤モデルを用いた自動韻律アノテーションの検討](https://speakerdeck.com/hyama5/yin-su-berttoyin-sheng-ji-pan-moderuwoyong-itazi-dong-yun-lu-anotesiyonnojian-tao) - hyama5（2025-09）
- [LINEヤフーの音声AIがもたらす未来：ASR/TTSと対話技術の新たな可能性 / LY Corporation's Speech AI Vision: Towards Realtime Spoken Dialogue through Advanced ASR and TTS](https://speakerdeck.com/lycorptech_jp/ly-corporations-speech-ai-vision-towards-realtime-spoken-dialogue-through-advanced-asr-and-tts) - LINEヤフーTech (LY Corporation Tech)（2025-07）
- [イラストで学ぶ音声認識 改訂第2版 11. 事前学習モデルによる音声認識](https://www.docswell.com/s/MasahiroAraki/5G1DX4-2025-06-05-141601) - 荒木 雅弘（2025-06）
- [イラストで学ぶ音声認識 改訂第2版 10. End-to-End の音声認識](https://www.docswell.com/s/MasahiroAraki/Z1R6JE-2025-06-05-141518) - 荒木 雅弘（2025-06）
- [深層学習による音声処理～物理なき音声のモデル化～](https://www.docswell.com/s/akinori-ito/56V8JW-2025-03-16-213358) - Akinori Ito（2025-03）
- [AWS 音声基盤モデル トーク解析AI MiiTelの音声処理について](https://speakerdeck.com/ken57/aws-yin-sheng-ji-pan-moderu-tokujie-xi-ai-miitelnoyin-sheng-chu-li-nituite) - Ken57（2025-01）
- [LINEヤフー株式会社における音声言語情報処理AI研究開発@SP/SLP研究会 2024.10.22](https://speakerdeck.com/lycorptech_jp/20241105a) - LINEヤフーTech (LY Corporation Tech)（2024-11）
- [LLMと音声基盤モデルを用いた音声認識](https://speakerdeck.com/spiralai/llmtoyin-sheng-ji-pan-moderuwoyong-itayin-sheng-ren-shi) - Spiral.AI（2024-09）
- [音声処理ツールキットESPnetの現在と未来](https://speakerdeck.com/kanbayashi1125/yin-sheng-chu-li-turukitutoespnetnoxian-zai-towei-lai) - Tomoki Hayashi（2024-03）
- [【Pythonで学ぶ音声認識】第7章：End-to-Endモデルによる連続音声認識（7.4節）](https://www.docswell.com/s/kyoto-kaira/5M18X6-2023-12-28-143451) - 京都大学人工知能研究会KaiRA（2023-12）
- [【Pythonで学ぶ音声認識】第7章：End-to-Endモデルによる連続音声認識（7.1～7.3節）](https://www.docswell.com/s/kyoto-kaira/Z4Q7VJ-2023-12-28-143239) - 京都大学人工知能研究会KaiRA（2023-12）
- [LINE CLOVAの音声認識技術](https://speakerdeck.com/line_developers/speech-recognition-technology-of-line-clova) - LINE Developers（2023-06）
- [音声認識と音声合成の超入門](https://speakerdeck.com/tam17aki/yin-sheng-ren-shi-toyin-sheng-he-cheng-nochao-ru-men) - Akira Tamamori（2023-06）
- [Self-Conditioned CTCとその発展](https://speakerdeck.com/line_developers/self-conditioned-ctc-and-its-development) - LINE Developers（2023-06）
- [デジタルツインと電話応対における音声合成と音声認識](https://speakerdeck.com/cyberagentdevelopers/dezitarutuintodian-hua-ying-dui-niokeruyin-sheng-he-cheng-toyin-sheng-ren-shi) - CyberAgent（2022-07）
- [JTubeSpeech: 音声認識と話者照合のために YouTube から構築される日本語音声コーパス](https://www.slideshare.net/ShinnosukeTakamichi/jtubespeech-youtube) - Shinnosuke Takamichi（2022-03）
- [音声領域におけるLINEの研究開発](https://speakerdeck.com/line_developers/line-research-and-development-in-the-voice-field) - LINE Developers（2022-03）
- [Introduction of LINE's Speech Recognition efforts](https://speakerdeck.com/line_developers/introduction-of-lines-speech-recognition-efforts) - LINE Developers（2021-06）
- [サイバーエージェントの音声研究開発の取り組み | CA BASE NEXT](https://speakerdeck.com/cyberagentdevelopers/saibaezientofalseyin-sheng-yan-jiu-kai-fa-falsequ-rizu-mi-ca-base-next) - CyberAgent（2021-05）
- [ここまで来た＆これから来る音声合成 (明治大学 先端メディアコロキウム)](https://www.slideshare.net/ShinnosukeTakamichi/ss-241884248) - Shinnosuke Takamichi（2021-01）
- [音声情報処理に便利な (Python) パッケージやソフトウェア](https://speakerdeck.com/tam17aki/yin-sheng-qing-bao-chu-li-nibian-li-na-python-patukeziyasohutouea) - Akira Tamamori（2020-12）
- [ヤフー音声認識YJVOICEにおけるディープラーニングの実用化](https://www.docswell.com/s/ydnjp/KM2JLK-2017-08-01-143133) - Yahoo!デベロッパーネットワーク（2017-08）
- [音声認識と深層学習](https://www.slideshare.net/pfi/ss-50580059) - Preferred Networks（2015-07）

## 对话系统・语音对话

语音与文本的对话系统，以及语音机器人的实际运维。

- [会話AIロボットRomiにおける自然な会話のためのアーキテクチャ設計](https://speakerdeck.com/mixi_engineers/architecture-design-for-natural-conversations-in-the-conversational-ai-robot-romi) - MIXI ENGINEERS（2026-04）
- [音声対話モデル2025-26](https://www.docswell.com/s/yuAbe/Z8W7GY-2026-01-29-120501) - 阿部雄斗（2026-01）
- [実運用で学んだ 音声対話システムの評価とテスト](https://speakerdeck.com/ymachida/shi-yun-yong-dexue-nda-yin-sheng-dui-hua-sisutemunoping-jia-totesuto) - Yuichiro Machida（2025-11）
- [RAGで制御可能なFull-duplex音声対話システム](https://speakerdeck.com/mssmkmr/ragdezhi-yu-ke-neng-nafull-duplexyin-sheng-dui-hua-sisutemu) - Convergence Lab.（2025-11）
- [【輪講資料】Moshi: a speech-text foundation model for real-time dialogue](https://speakerdeck.com/hpprc/lun-jiang-zi-liao-moshi-a-speech-text-foundation-model-for-real-time-dialogue) - Hayato Tsukagoshi（2025-07）
- [イラストで学ぶ音声認識 改訂第2版 12. 音声対話システム](https://www.docswell.com/s/MasahiroAraki/K9V38Y-2025-06-05-141640) - 荒木 雅弘（2025-06）
- [リクルートやNRIデジタルとの成功事例に学ぶ、 IVRyのAI音声対話／音声解析ソリューションが 変革するコールセンターの未来](https://speakerdeck.com/miyashino/call-center-crm-demo-and-conference-20241122) - Shinobu Miyahara（2024-11）
- [武蔵大学 AIの社会浸透研究会 第3回公開セミナー 大規模言語モデルがもたらす対話システム技術の変革](https://speakerdeck.com/mnakano/wu-zang-da-xue-ainoshe-hui-jin-tou-yan-jiu-hui-di-3hui-gong-kai-semina-da-gui-mo-yan-yu-moderugamotarasudui-hua-sisutemuji-shu-nobian-ge) - Mikio Nakano（2024-06）
- [マルチモーダル対話システム](https://speakerdeck.com/sei88888/marutimodarudui-hua-sisutemu) - Seitaro Shinagawa（2024-06）
- [ボイスボット事業における研究開発と産学連携](https://speakerdeck.com/cyberagentdevelopers/boisubotutoshi-ye-niokeruyan-jiu-kai-fa-tochan-xue-lian-xi) - CyberAgent（2022-07）
- [マルチモーダル対話システムのスゝメ](https://www.slideshare.net/slideshow/ss-62714701/62714701) - Takahiro Kubo（2016-06）
- [対話システム, 南泰浩](https://www.slideshare.net/iilab/723-50838179) - KIT Cognitive Interaction Design（2015-07）

## 生成・摘要・校对

文本生成及其应用任务。

- [日本語ニュース記事要約支援に向けたドメイン特化事前学習済みモデルの構築と活用 / t5-news-summarization](https://speakerdeck.com/upura/t5-news-summarization) - Shotaro Ishihara（2025-03）
- [NLP2025 WS Shared Task 文法誤り訂正部門 ehiMetrick](https://speakerdeck.com/sugiyamaseiji/nlp2025-ws-shared-task-wen-fa-wu-riding-zheng-bu-men-ehimetrick) - 杉山誠治（Sugiyama Seiji）（2025-03）
- [ABEMA NEWSにおける映像データを活用した記事生成AI 〜記事制作者に寄り添ったソリューションにするまで〜](https://speakerdeck.com/cyberagentdevelopers/abema-newsniokeruying-xiang-detawohuo-yong-sitaji-shi-sheng-cheng-ai-ji-shi-zhi-zuo-zhe-niji-ritian-tutasoriyusiyonnisurumade) - CyberAgent（2024-11）
- [大規模言語モデルを用いた意味分析による辞書記述への応用](https://speakerdeck.com/yhkondo/da-gui-mo-yan-yu-moderuwoyong-itayi-wei-fen-xi-niyoruci-shu-ji-shu-henoying-yong) - Yasuhiro Kondo（2023-11）
- [LLMによる日本語ニュース記事の平易化 / Japanese News Articles Simplification via Large Language Models](https://speakerdeck.com/asahimrdc/japanese-news-articles-simplification-via-large-language-models) - Media R&D Center, The Asahi Shimbun（2023-04）
- [実践：日本語文章生成 Transformers ライブラリで学ぶ実装の守破離 / Introduction of Japanese Text Generation with Transformers](https://speakerdeck.com/upura/introduction-of-japanese-text-generation-with-transformers) - Shotaro Ishihara（2022-10）
- [自然言語処理を用いた効果的な広告テキストの自動生成【CADC2022】](https://speakerdeck.com/cyberagentdevelopers/zi-ran-yan-yu-chu-li-woyong-itaxiao-guo-de-naguang-gao-tekisutofalsezi-dong-sheng-cheng-cadc2022) - CyberAgent（2022-03）
- [日本語文法誤り訂正における事前学習済みモデルを用いたデータ増強](https://speakerdeck.com/hideyoshikato/ri-ben-yu-wen-fa-wu-riding-zheng-niokerushi-qian-xue-xi-ji-mimoderuwoyong-itadetazeng-qiang) - hideyoshikato（2021-03）
- [日本語文法誤り訂正における誤り傾向を考慮した擬似誤り生成](https://speakerdeck.com/youichiro/ri-ben-yu-wen-fa-wu-riding-zheng-niokeruwu-riqing-xiang-wokao-lu-sitani-si-wu-risheng-cheng) - youichiro（2020-06）
- [文献紹介：正誤情報と文法誤りパターンを考慮した単語分散表現を用いた文法誤り検出](https://speakerdeck.com/a1da4/wen-xian-shao-jie-zheng-wu-qing-bao-towen-fa-wu-ripatanwokao-lu-sitadan-yu-fen-san-biao-xian-woyong-itawen-fa-wu-rijian-chu) - Taichi Aida（2019-01）
- [日本語の語彙平易化システムおよび評価セットの構築](https://www.slideshare.net/moguranosenshi/ss-47551205) - Tomoyuki Kajiwara（2015-04）

## 可解释性・分析・语言学观点

窥看模型的内部，并从语言的角度加以评估。

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

## 产业应用・实务案例

把 NLP／LLM 集成进实际服务与实际业务的案例。

- [つくって納得、つかって実感！ 大規模言語モデルことはじめ ver2.0](https://speakerdeck.com/recruitengineers/fy2026_bootcamp_kiryu) - Recruit（2026-08）
- [LocalLLMで機密データを匿名化したい](https://speakerdeck.com/cyberagentdevelopers/localllmdeji-mi-detawoni-ming-hua-sitai) - CyberAgent（2026-05）
- [キャリアアシスタントにおけるLLMの不確実性を制御するアプローチ](https://speakerdeck.com/recruitengineers/recruittc2026-06-2-ikegamikenshin) - Recruit（2026-02）
- [LLM のプロダクト導入における開発の裏側と技術的挑戦](https://speakerdeck.com/recruitengineers/recruittc2026-05-1-ueyamaayaka) - Recruit（2026-02）
- [日本語テキストと音楽の対照学習の技術とその応用](https://speakerdeck.com/lycorptech_jp/20260126a) - LINEヤフーTech (LY Corporation Tech)（2026-01）
- [Kaggle自然言語処理コンペ向けローカルLLM活用入門](https://speakerdeck.com/k951286/kagglezi-ran-yan-yu-chu-li-konpexiang-kerokarullmhuo-yong-ru-men) - monnu（2025-02）
- [医療分野における大規模言語モデルの調査](https://www.docswell.com/s/5451263343/5WWLRJ-2025-01-17-204429) - 高橋浩（2025-01）
- [Argo Workflowsで構築するLLMを活用したコールセンターの自動要約プロダクトの立ち上げ / ai-argo-summarize](https://speakerdeck.com/cyberagentdevelopers/ai-argo-summarize) - CyberAgent（2024-10）
- [自然言語処理を役立てるのはなぜ難しいのか](https://speakerdeck.com/pfn/20241015_todai_nlp_unno_lecture) - Preferred Networks（2024-10）
- [自社開発した大規模言語モデルをどうプロダクションに乗せて運用していくか〜インフラ編〜](https://speakerdeck.com/pfn/20240906-cloud-operator-days-2024-pfn) - Preferred Networks（2024-09）
- [履歴書サービスでのLLMを使った機能の事例](https://speakerdeck.com/morizyun/lu-li-shu-sabisudenollmwoshi-tutaji-neng-noshi-li) - morizyun（2024-07）
- [LLMと共に進むSORACOMサポートの挑戦と効果【SORACOM Discovery 2024】](https://speakerdeck.com/soracom/soracom-discovery-2024-c-5) - SORACOM（ソラコム）（2024-07）
- [LLMを用いた住まい探しにおけるユーザ価値観の推定](https://www.docswell.com/s/LIFULL/KYW3N4-2024-03-29-160847) - 株式会社LIFULL（2024-03）
- [LLMに医療知識をつけるには](https://speakerdeck.com/elith/llmniyi-liao-zhi-shi-wotukeruniha) - Elith（2024-03）
- [LIFULL AI Hub 100ミニッツ #1\_LLM（大規模言語モデル）の研究開発](https://www.docswell.com/s/LIFULL/ZNR31G-2023-12-28-170955) - 株式会社LIFULL（2023-12）
- [ELYZA\_LLMの現状・課題・展望に関する勉強会\_20230713](https://speakerdeck.com/elyza/llm-yan-yu-sheng-cheng-ai-noxian-zhuang-ke-ti-zhan-wang-niguan-surumian-qiang-hui-20230713-7578523c-9de2-43d5-b0cd-36fda5baff68) - 株式会社ELYZA（2023-08）
- [テキストマイニングを使って 今年1年のレビュー内容をふりかえってみた話](https://speakerdeck.com/cybozuinsideout/line_twm_221221_cybozu) - Cybozu（2022-12）
- [ESG評価に対する自然言語処理の活用Workshop](https://speakerdeck.com/icoxfog417/esgping-jia-nidui-suruzi-ran-yan-yu-chu-li-falsehuo-yong-workshop) - Takahiro Kubo（2022-06）
- [日本経済新聞社における自然言語処理の取り組み / yans2022 nikkei nlp](https://speakerdeck.com/upura/yans2022-nikkei-nlp) - Shotaro Ishihara（2022-03）
- [ハンドメイド作品を扱うECサイトに特化したBERTを用いた言語モデル構築に向けた取り組み/ipsj-NL250-05](https://speakerdeck.com/tossy/ipsj-nl250-05) - tossy（2021-09）
- [自然言語処理の基礎と応用 〜 料理と医療を題材として 〜 /JADI2021](https://speakerdeck.com/junharashima/jadi2021) - j.harashima（2021-09）
- [企業で3年間言語処理と働いて思ったこと #NLP2021 #NLP2021WS4](https://www.docswell.com/s/ydnjp/Z1M3RK-2021-03-24-155120) - Yahoo!デベロッパーネットワーク（2021-03）
- [【Ltech#11】住まい探しにおける対話AIの自然言語解析技術](https://www.docswell.com/s/LIFULL/KPLVGZ-%E4%BD%8F%E3%81%BE%E3%81%84%E6%8E%A2%E3%81%97%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E5%AF%BE%E8%A9%B1AI%E3%81%AE%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E8%A7%A3%E6%9E%90%E6%8A%80%E8%A1%93) - 株式会社LIFULL（2020-10）
- [#devsumi 自然言語処理・機械学習によるファクトチェック業務の支援](https://speakerdeck.com/komiya_atsushi/number-devsumi-zi-ran-yan-yu-chu-li-ji-jie-xue-xi-niyoruhuakutotietukuye-wu-falsezhi-yuan) - KOMIYA Atsushi（2018-02）
- [リクルート式 自然言語処理技術の適応事例紹介](https://www.slideshare.net/recruitcojp/ss-66242894) - Recruit Technologies（2016-09）
- [企業における自然言語処理技術の活用の現場（情報処理学会東海支部主催講演会@名古屋大学）](https://www.slideshare.net/unnonouno/20141022-ipsj-tokai) - Yuya Unno（2014-10）

## 许可协议

[CC0 1.0 Universal](http://creativecommons.org/publicdomain/zero/1.0/)

> [!NOTE]
> CC0 适用的对象是本列表本身。各份幻灯片的著作权，归属于各自的发表者。
