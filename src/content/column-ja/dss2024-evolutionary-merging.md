---
title: "Can One Merged LLM Handle 15 Sentiment Tasks?"
subtitle: "Multi-Stage Evolutionary Model Merging with Meta Data Driven Curriculum Learning for Sentiment-Specialized Large Language Modeling"
date: "2026-11-27"
excerpt: "タスクごとに作った 15 個の感情分析エキスパート LLM を、進化的アルゴリズムで 1 つにマージし、さらに易しいタスクから順に例を見せる推論時カリキュラムを加えました。IEEE DSS 2024 で Best Paper Award を受けた論文の解説です。"
readingMinutes: 11
showImage: false
image: "/column-images/dss2024-evolutionary-merging/framework.png"
imageAlt: "MEM-MCL の全体図。SFT フェーズでタスクごとのエキスパートモデルを作り、MEM フェーズで進化的アルゴリズムにより段階的にマージし、MCL フェーズで難易度順のカリキュラムを使って推論する。"
authors:
  - name: "井下 敬翔"
    url: "/about/"
    affiliation: "関西大学"
  - name: "Xiaokang Zhou"
    affiliation: "Kansai University / RIKEN Center for AIP"
  - name: "Akira Kawai"
    affiliation: "Shiga University / Japan Safety Society Research Center"
tldr: "感情分析には、ポジ・ネガの分類から、アスペクトごとの感情抽出、皮肉やヘイトの判定まで、性質の違うタスクがたくさんあります。この研究では Llama 2 を LoRA でタスクごとに指示チューニングして 15 個のエキスパートを作り、それらを 3 グループ内で、次にグループ間で、進化的アルゴリズムを使って 2 段階でマージしました（MEM）。マージの重みは、各エキスパートが間違えた「弱いデータ」での成績で選びます。さらに、タスクのメタ情報（クラス数・データの多様さ・タスクの複雑さ・主観性）から難易度を数え、易しい順に例を並べて推論させるカリキュラム（MCL）を加えました。1 つにまとめたモデルは、15 タスク中 10 タスクで元の Llama 2 を上回り、6 タスクではタスク専用のエキスパートも上回りました。MCL を加えると 15 タスク中 9 タスクで MEM より高くなりました。一方で、易しい SC タスクでは MCL によってむしろ下がるなど、効果はタスクによって分かれています。"
links:
  - label: "Paper (IEEE DSS 2024)"
    url: "https://doi.org/10.1109/dss64273.2024.00018"
citation: |
  @inproceedings{inoshita2024memmcl,
    title     = {Multi-Stage Evolutionary Model Merging with Meta Data Driven
                 Curriculum Learning for Sentiment-Specialized Large Language Modeling},
    author    = {Inoshita, Keito and Zhou, Xiaokang and Kawai, Akira},
    booktitle = {Proceedings of the 10th IEEE DSS},
    pages     = {58--65},
    year      = {2024},
    doi       = {10.1109/dss64273.2024.00018}
  }
---

<div class="teaser">
<div>

Merge

15 個のエキスパートを **進化的アルゴリズムで 2 段階マージ**。1 つのモデルが、15 タスク中 10 タスクで元の Llama 2 を上回る。

</div>
<div>

Order

タスクのメタ情報から **難易度スコア** を計算し、易しい順に例を見せて推論する。MEM との比較で 15 タスク中 9 タスクが上昇。

</div>
<div>

Limits

効果は一様ではない。**易しい SC タスクでは MCL で下がり**、MAST-Hate などでは元の Llama 2 に届かない。

</div>
</div>

この論文は、2024 年 12 月の第 10 回 IEEE DSS で発表し、Best Paper Award を受けました。

## 感情分析は 1 つのタスクではない

感情分析と一口に言っても、中身はさまざまです。文全体のポジ・ネガを当てる分類（Sentiment Classification, SC）、文中の対象ごとに感情を結びつけるアスペクトベース感情分析（ABSA）、11 や 28 の細かい感情、ヘイト・攻撃性・皮肉を判定する主観的テキストの分析（MAST）は、必要な読み取り方がかなり違います。

従来の手法は、たいてい 1 つのタスクに特化していました。実際の現場では複数のタスクを同時に扱うことが多く、タスクごとに別のモデルを持つのは運用面で重荷です。LLM は 1 つで多くのタスクをこなせますが、感情分析では専用モデルほどの精度が出ないことが知られています。

そこでこの研究では、2 つの問いを立てました。

1. タスクごとに作った専用モデルを **1 つのモデルにまとめても、精度を保てるか**。
2. タスクそのものの **メタ情報（クラス数や主観性など）を使って学ばせる順番を決める** と、精度は上がるか。

## MEM-MCL の仕組み

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/framework-1600.webp" alt="MEM-MCL framework overview" />
  <figcaption><strong>Figure 1.</strong> MEM-MCL の全体図（論文の Fig. 1）。左から、エキスパートを作る SFT フェーズ、進化的にマージする MEM フェーズ、難易度順のカリキュラムで推論する MCL フェーズです。</figcaption>
</figure>

MEM-MCL は 3 つのフェーズで動きます。

1. **SFT フェーズ**：15 個の感情分析タスクそれぞれについて、指示文・入力文（ABSA ではアスペクトやカテゴリも）からプロンプトを作り、Llama 2 に LoRA を付けて指示チューニングします。これでタスク専用のエキスパートが 15 個できます。
2. **MEM フェーズ（Multi-stage Evolutionary Model Merging）**：エキスパートを SC・ABSA・MAST の 3 グループに分け、まずグループ内で、次にグループ間でマージします。マージは重み付きの和で、その重みを進化的アルゴリズムで探します。
3. **MCL フェーズ（Meta data driven Curriculum Learning）**：タスクの難易度をメタ情報から計算し、易しいタスクから難しいタスクの順に指示・入力・出力を並べてプロンプトに入れ、推論させます。

### 弱いデータで重みを選ぶ

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/mem-mechanism-1600.webp" alt="Mechanism of MEM" />
  <figcaption><strong>Figure 2.</strong> MEM の仕組み（論文の Fig. 4）。15 個のエキスパートをメタ情報で 3 グループに分け、1 段目の進化的マージでグループごとのモデルを作り、2 段目で最終モデルにまとめます。</figcaption>
</figure>

MEM の特徴は、重みの良し悪しを測るデータの選び方です。まず各エキスパートに自分の学習データを推論させ、**間違えた事例を「弱いデータ」として取り出します**。進化的アルゴリズムは、重みベクトルの集団を作り、交叉・突然変異でばらつかせ、その重みでマージしたモデルが弱いデータでどれだけ正解するかを適合度にして、良い個体を次の世代に残します。苦手な事例で成績が良くなる重みを選ぶことで、エキスパートどうしが弱点を補い合うことを狙っています。

主なハイパーパラメータは以下のとおりです。

| フェーズ | 設定 | 値 |
|---|---|---|
| SFT | バッチサイズ / マイクロバッチ | 64 / 4 |
| SFT | 学習率 / 最大エポック / weight decay | 3e-4 / 10 / 0.1 |
| SFT | LoRA r / α / dropout | 4 / 16 / 0.05 |
| マージ | 世代数 / 初期集団サイズ | 10 / 20 |
| マージ | 交叉点 / 突然変異確率 | ランダム / 0.1 |

### メタ情報から難易度を数える

MCL では、各タスクの難易度を次の式で数えます。

**Score = 1.0 × C + 0.5 × V + 2.0 × Z + 5.0 × S**

C はクラス数、V はデータの多様さ、Z はタスクの複雑さ、S は主観性の有無です。重みは先行研究にもとづいて決めており、主観性（皮肉やヘイトの判定など）に最も大きい 5.0 を与えています。

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/difficulty-1600.webp" alt="Task difficulty scores" />
  <figcaption><strong>Figure 3.</strong> 15 タスクの難易度スコアと順位（論文の Table III）。上から順にカリキュラムで提示します。28 感情分類が最も難しく、2 値の文単位分類が最も易しい扱いです。順位は Table III のとおりで、SC-5class（8）が ABSA-TSD（6.5）より先に来るなど、スコアの大小と一致しない箇所があります。</figcaption>
</figure>

## 実験の設定

<div class="setup">

**Setup**

- ベースモデル：Llama 2（7B）、LoRA による指示チューニング
- タスク：SC 4 種、ABSA 6 種（ATSA・ACSA・TSD・ASD・ASTE・ASQP）、MAST 5 種（11 クラス・28 クラス・Hate・Offensive・Irony）の計 15 種
- テスト：各タスク最大 500 件をランダムに抽出
- 指標：タスクに応じて Accuracy、Micro-F1、Macro-F1（いずれも % 表示）

</div>

| グループ | タスク | 学習 | テスト | 指標 |
|---|---|---|---|---|
| SC | 2class-sen / 2class-doc / 3class / 5class | 6000 / 3000 / 3000 / 15000 | 各 500 | Accuracy |
| ABSA | ATSA / ACSA | 1600 / 3000 | 421 / 400 | Accuracy |
| ABSA | TSD / ASD / ASTE / ASQP | 1600 / 1500 / 1500 / 1500 | 421 / 400 / 500 / 500 | Micro-F1 |
| MAST | 11class / 28class | 5000 / 10000 | 各 500 | Accuracy |
| MAST | Hate / Offensive / Irony | 9000 / 3000 / 3000 | 各 500 | Macro-F1 |

論文の Fig. 7・Fig. 8 は数値の入っていない棒グラフなので、この記事の図は、それらの棒に対応する著者の集計表の値で描き直しています。

## 実験 1：1 つにまとめても精度を保てるか

<p class="experiment-label">Experiment 1</p>

元の Llama 2（Base）、タスクごとのエキスパート（Expert）、MEM でマージした 1 つのモデル（MEM）を 15 タスクで比べました。

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/mem-vs-base-expert-1600.webp" alt="Base vs expert vs MEM" />
  <figcaption><strong>Figure 4.</strong> 15 タスクでのスコア（論文の Fig. 7 に対応）。灰色が元の Llama 2、青がタスク専用のエキスパート、金色が 1 つにマージした MEM です。</figcaption>
</figure>

MEM は 15 タスク中 10 タスクで Base を上回りました。差が大きいのは ATSA（18.76 → 67.22）、SC-2class-doc（47.4 → 94.8）、SC-3class（36.8 → 87.6）です。

エキスパートとの比較では、MEM が上回ったのは ATSA（61.52 → 67.22）、ACSA、ASQP、SC-3class、MAST-Hate、MAST-Irony の 6 タスクでした。SC-2class-doc（95.2 と 94.8）や ASTE（25.2 と 24.8）のように差がごく小さいタスクもあります。各タスクに特化したモデルと、15 タスクを 1 つで受け持つモデルが、多くのタスクで近い水準にあることがわかります。

一方で、MEM が Base を下回るタスクもあります。MAST-Hate（38.04 → 25.34）、MAST-Irony（63.29 → 59.94）、ABSA-TSD、SC-5class、SC-2class-sen です。MAST-Hate はエキスパート自体も 19.13 と Base より低く、指示チューニングの段階で難しかったタスクです。

## 実験 2：易しい順に見せると精度は上がるか

<p class="experiment-label">Experiment 2</p>

MCL の効果を見るため、3 つの条件を比べました。MEM だけ（MEM）、MEM にタスクの例を順番を決めずに見せる条件（Unstructured）、MEM に難易度順で見せる条件（MEM-MCL）です。

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/mcl-comparison-1600.webp" alt="MEM vs unstructured vs MEM-MCL" />
  <figcaption><strong>Figure 5.</strong> 15 タスクでのスコア（論文の Fig. 8 に対応）。灰色が MEM、薄い色が順番を決めずに見せた条件、金色が難易度順の MEM-MCL です。</figcaption>
</figure>

MEM-MCL は 15 タスク中 9 タスクで MEM を上回りました。大きく上がったのは ACSA（9.25 → 19.5）と ASD（20.5 → 28.75）、MAST-Hate（25.34 → 38.04）、MAST-Offensive（22.29 → 41.73）です。順番を決めない条件との比較では、9 タスクで MEM-MCL が上回り、特に ATSA（55.34 → 67.93）と MAST-Irony（52.3 → 60.17）で差がつきました。

ただし、すべてのタスクで効いたわけではありません。ASD では順番を決めない条件（31.5）のほうが MEM-MCL（28.75）より高く、MAST-Hate では両者が同じ 38.04 でした。

## 実験 3：どのタスクで効き、どこで下がったか

<p class="experiment-label">Experiment 3</p>

MEM から MEM-MCL への変化を、カリキュラムの順（易しい順）に並べ直しました。

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/mcl-delta-1600.webp" alt="Change from MEM to MEM-MCL" />
  <figcaption><strong>Figure 6.</strong> MEM-MCL と MEM の差（ポイント）。タスクは難易度の順位順で、上ほど易しいタスクです。最も易しい SC の 3 タスクではいずれも下がっています。</figcaption>
</figure>

最も易しい 3 タスク（SC-2class-sen、SC-2class-doc、SC-3class）では、MCL によってスコアが 3.2〜7.4 ポイント下がりました。論文でも、SC グループでは MEM のほうが MEM-MCL より良いタスクがあり、MCL の効果はタスクによって限られると述べています。上がったのは、中位の ABSA と MAST-Hate・MAST-Offensive が中心でした。

最後に、15 タスクでの勝ち数をまとめます。

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/win-counts-1600.webp" alt="Win counts over 15 tasks" />
  <figcaption><strong>Figure 7.</strong> 15 タスクのうち、左側のモデルのスコアが高かったタスクの数。MAST-Hate の同点（38.04）は勝ちに数えていません。</figcaption>
</figure>

## わかったこと・わかっていないこと

この研究でわかったのは次の点です。

- タスクごとに作った 15 個のエキスパートを、弱いデータを使った進化的マージで 1 つにまとめると、多くのタスクで元の LLM を上回り、エキスパートに近い水準を保てた。
- タスクのメタ情報から難易度を数え、易しい順に例を見せる推論時カリキュラムは、15 タスク中 9 タスクで精度を上げた。

一方で、論文自身が挙げている課題もあります。

- MAST-Hate のようにラベルの偏りが大きいタスクでは、7B の小さなモデルが出力形式をうまく守れないことがあった。モデルの大きさとタスクの複雑さの両方が原因と考えられる。
- マージの効果は一様ではなく、Base を下回るタスクが残った。複雑なタスクや主観的なタスクでは、マージの重みづけやアルゴリズムの調整が足りない可能性がある。
- 難易度スコアの重み（1.0・0.5・2.0・5.0）は先行研究にもとづく経験的な設定で、最適化はしていない。

また、テストは各タスク最大 500 件で、論文には複数シードでのばらつきや統計的検定は示されていません。差が小さいタスクの勝ち負けは、慎重に読む必要があります。

今後は、進化的アルゴリズムの最適化と、カリキュラムの重みを各タスクの成績に応じて自動で決める仕組みに取り組む予定です。
