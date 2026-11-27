---
title: "Can a CNN Catch Sarcasm by Looking at Several Scales at Once?"
subtitle: "Multi-Scale Convolutional Fusion with Contrastive Feature Alignment for Imbalanced Data Classification"
date: "2026-11-27"
excerpt: "字面と本音が逆になる皮肉の検出に向けて、膨張率の違う畳み込みで複数のスケールを同時に見る MSCF と、対照学習でクラスを引き離す CFA を組み合わせました。NLDB 2025 で Best Paper Award を受賞した論文の解説です。"
readingMinutes: 10
showImage: false
image: "/column-images/nldb2025-multiscale-fusion/architecture.png"
imageAlt: "MSCF-CFA の全体図。RoBERTa の埋め込みを MF-CNN で局所特徴にし、MSCF で複数スケールの依存関係を融合し、CFA で対照学習によって特徴を整えてから分類する。"
authors:
  - name: "井下 敬翔"
    url: "/about/"
    affiliation: "関西大学"
  - name: "Takato Ueno"
    affiliation: "Shiga University"
  - name: "Xiaokang Zhou"
    affiliation: "Kansai University / RIKEN Center"
tldr: "皮肉は字面と意図が逆になるため、感情分析や意見マイニングの精度を下げます。この論文では、複数サイズのフィルタを使う MF-CNN を土台に、膨張率 1・2・4 の畳み込みを並列に走らせる MSCF、特徴空間を広げて対照学習でクラスを引き離す CFA、少数クラスを重くする重み付き交差エントロピー（WCE）を組み合わせた MSCF-CFA を提案しました。3,834 文の皮肉検出データで F1 79.37% となり、比較した 6 手法（最良は RoBERTa+DBLoss の 75.14%）をすべての指標で上回りました。部品を外すと F1 は 0.6〜1.7 ポイント下がり、WCE を外したときの低下が最も大きくなりました。"
links:
  - label: "Paper (NLDB 2025)"
    url: "https://doi.org/10.1007/978-3-031-97141-9_1"
citation: |
  @inproceedings{inoshita2025mscfcfa,
    title     = {Multi-Scale Convolutional Fusion with Contrastive Feature Alignment
                 for Imbalanced Data Classification},
    author    = {Inoshita, Keito and Ueno, Takato and Zhou, Xiaokang},
    booktitle = {Natural Language Processing and Information Systems (NLDB 2025)},
    series    = {Lecture Notes in Computer Science},
    volume    = {15836},
    year      = {2025},
    doi       = {10.1007/978-3-031-97141-9_1}
  }
---

<div class="teaser">
<div>

Compare

F1 は **79.37%**。比較した 6 手法の最良（RoBERTa+DBLoss、75.14%）を 4.23 ポイント上回りました。

</div>
<div>

Ablate

MSCF・CFA・WCE は **どれを外しても下がる**。最も大きいのは WCE で、F1 は 77.66% まで低下。

</div>
<div>

Visualize

PCA で見ると、MF-CNN → MSCF → CFA と進むにつれて **皮肉と非皮肉が両端へ分かれていきます**。

</div>
</div>

## 皮肉はなぜ難しいのか

SNS やレビューサイトの投稿を自動で分析する技術は、マーケティングや社会動向の把握に欠かせなくなっています。その中で皮肉は厄介な存在です。「なんて素晴らしい天気だ！」という文は、悪天候への不満を表していることがあります。**字面と意図が逆になる**ため、通常の文分類ではそのまま誤分類につながります。

皮肉検出では、局所的な表現の抽出が得意な CNN が RNN より高い精度を示してきました。中でも、サイズの違う複数のフィルタで n-gram 特徴をとる Multi-Filter CNN（MF-CNN）はよく使われます。ただし論文では、MF-CNN に次の 3 つの限界があると整理しました。

1. 使うカーネルサイズが限られるため、**離れた語どうしの関係や複数スケールの依存関係**をとらえにくい。
2. 同じクラスの特徴が十分に集まらず、違うクラスの特徴が十分に離れないため、**特徴の識別力が弱い**。
3. 皮肉の文は相対的に少ないことが多く、**クラス不均衡**のもとでは多数クラスに偏りやすい。

この 3 つに 1 つずつ対応する部品を足したのが MSCF-CFA です。

## MSCF-CFA の仕組み

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/architecture-1600.webp" alt="MSCF-CFA framework overview" />
  <figcaption><strong>Figure 1.</strong> MSCF-CFA の全体図（論文の Figure 1）。左から、RoBERTa による埋め込み、MF-CNN による局所特徴の抽出、MSCF による複数スケールの融合、CFA による特徴の整列と分類です。</figcaption>
</figure>

処理は 4 段階です。

1. **埋め込み**：文をトークンに分け、事前学習済みの RoBERTa で 768 次元のベクトル列（系列長 128）にします。
2. **MF-CNN**：フィルタサイズ 2・3・4 の 2 次元畳み込み（各 100 フィルタ）で bigram や trigram 相当の特徴をとり、max pooling でまとめて 256 次元にします。
3. **MSCF（Multi-Scale Convolutional Fusion）**：膨張率（dilation）1・2・4 の 1 次元畳み込みを並列に走らせ、結果をつないで線形変換します。残差接続と Layer Normalization を入れ、このブロックを 2 段重ねます。
4. **CFA（Contrastive Feature Alignment）**：特徴を 4 つの特徴空間に広げ（Feature Expansion）、平均プーリングでまとめてから 64 次元に射影します。この射影に対して、同じクラスを近づけ違うクラスを遠ざける対照損失（温度 τ = 0.7）をかけます。

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/mscf.png" alt="Mechanism of MSCF" />
  <figcaption><strong>Figure 2.</strong> MSCF の構造（論文の Figure 2）。膨張率の違う枝ごとに、とびとびの位置を見る畳み込みをかけ、短い範囲から長い範囲までの依存関係を同時にとらえます。</figcaption>
</figure>

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/cfa.png" alt="Mechanism of CFA" />
  <figcaption><strong>Figure 3.</strong> CFA の構造（論文の Figure 3）。特徴を複数の空間に広げてから平均し、低次元に射影したうえで対照学習をかけます。</figcaption>
</figure>

最後に分類器でクラスを予測します。損失は、クラスの出現頻度の逆数で重みをつけた交差エントロピー（WCE）と対照損失の和で、対照損失の重み α は 0.1 です。WCE は少数クラスの損失を大きくして、多数クラスへの偏りをおさえる役割をもちます。

## 実験 1：既存手法との比較

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- データ：皮肉検出データセット（3,834 文、「皮肉」「非皮肉」の 2 値ラベル）、学習 80%・テスト 20%
- 埋め込み：事前学習済み RoBERTa（768 次元）
- 比較：MF-CNN、BiLSTM、Transformer、DualCL（対照学習）、RoBERTa+DBLoss（不均衡向けの損失）、MHA-BiLSTM（皮肉検出向け）
- 学習：バッチサイズ 64、100 エポック、学習率 1e-4
- 評価：Accuracy、Precision、Recall、F1

</div>

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/main-results-1600.webp" alt="F1 of all models" />
  <figcaption><strong>Figure 4.</strong> テストセットでの F1。灰色が土台の MF-CNN、青が比較手法の中で最良の RoBERTa+DBLoss です。横軸は 65% から始めています。</figcaption>
</figure>

| モデル | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| MF-CNN | 74.84 | 75.88 | 74.88 | 74.60 |
| BiLSTM | 71.58 | 71.82 | 71.60 | 71.51 |
| Transformer | 74.45 | 75.10 | 74.41 | 74.26 |
| DualCL | 69.49 | 69.61 | 69.51 | 69.45 |
| RoBERTa+DBLoss | 75.23 | 75.53 | 75.21 | 75.14 |
| MHA-BiLSTM | 73.66 | 73.98 | 73.69 | 73.59 |
| **MSCF-CFA** | **79.40** | **79.58** | **79.42** | **79.37** |

MSCF-CFA は 4 つの指標すべてで最も高くなりました。比較手法で最良の RoBERTa+DBLoss（Accuracy 75.23%）とは Accuracy で 4.17 ポイントの差です。土台の MF-CNN も 74.84% で、BiLSTM（71.58%）や Transformer（74.45%）を上回っており、局所的な特徴をとる CNN がこのタスクに向いていることがわかります。

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/metrics-1600.webp" alt="Four metrics for three models" />
  <figcaption><strong>Figure 5.</strong> 土台の MF-CNN、最良の比較手法、MSCF-CFA の 4 指標。Precision だけが高くなるような偏りはなく、4 指標がそろって上がっています。</figcaption>
</figure>

学習曲線も比べました（論文の Figure 4）。構造が単純な MF-CNN は損失が最も早く下がりますが、MSCF-CFA は立ち上がりがやや遅いかわりに、40 エポック前後で収束し、最終的な損失は他のモデルより低くなりました。

## 実験 2：特徴は段階ごとにどう変わるか

<p class="experiment-label">Experiment 2</p>

各部品が特徴をどう変えるかを見るため、MF-CNN の後、MSCF の後、CFA の後の特徴をそれぞれ PCA で 2 次元に落としました。

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/pca-1600.webp" alt="PCA of features after each module" />
  <figcaption><strong>Figure 6.</strong> 各段階の特徴の PCA（論文の Figure 5）。(a) MF-CNN の後、(b) MSCF の後、(c) CFA の後。Label 1 が皮肉、Label 0 が非皮肉です。</figcaption>
</figure>

- **(a) MF-CNN の後**：皮肉の点は右に寄る傾向がありますが、非皮肉と大きく重なっています。
- **(b) MSCF の後**：皮肉は右へ、非皮肉は左へ移り、重なりが減ります。ただし中央にはまだどちらとも言えない点が残ります。
- **(c) CFA の後**：2 つのクラスが特徴空間の両端に分かれ、中央の曖昧な点が目に見えて減ります。

特徴空間を広げて対照学習をかける CFA が、クラスの分離を強めていることを示唆する結果です。ただし (c) でも中央に残る点はあり、これは後で述べる限界につながります。

## 実験 3：どの部品が効いているか

<p class="experiment-label">Experiment 3</p>

MSCF、CFA、WCE をそれぞれ外したモデルを作り、性能を比べました。

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/ablation-1600.webp" alt="Ablation study" />
  <figcaption><strong>Figure 7.</strong> 部品を 1 つずつ外したときの F1。括弧内は完全版からの差です。横軸は 76% から始めています。</figcaption>
</figure>

| モデル | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| MSCF-CFA | 79.40 | 79.58 | 79.42 | 79.37 |
| w/o MSCF | 78.75 | 78.83 | 78.76 | 78.74 |
| w/o CFA | 78.75 | 78.84 | 78.74 | 78.73 |
| w/o WCE | 77.71 | 77.91 | 77.69 | 77.66 |

MSCF または CFA を外すと、F1 は約 0.6 ポイント下がりました。WCE を外したときの低下は 1.71 ポイントで、3 つの中で最も大きくなりました。どの部品も性能に寄与しており、とくに損失の重みづけがクラスのバランスに大きく効いていることがわかります。

## わかったこと・わかっていないこと

この研究でわかったのは次の点です。

- 複数サイズのフィルタ（MF-CNN）に、膨張率の違う畳み込み（MSCF）と対照学習による特徴の整列（CFA）を重ねると、皮肉検出の精度が比較手法を上回った。
- 段階ごとの PCA では、MSCF と CFA を通るたびにクラスの分離がはっきりしていった。
- MSCF・CFA・WCE はいずれも性能に寄与し、WCE の寄与が最も大きかった。

一方で、限界もあります。CFA の後の PCA でも曖昧な点が残っており、より深い文の理解や補足情報が必要な例があります。皮肉検出のラベル付きデータは少なく、注釈のぶれも課題です。複数スケールの畳み込みと特徴空間の拡張でパラメータが増えるため、計算資源の限られた環境では使いにくくなります。また、評価は 1 つのデータセットの 1 回の分割で行っており、複数シードでのばらつきは報告していません。

今後は、入力文を補う方法、弱教師あり・自己教師あり学習によるデータの拡充、蒸留・量子化・枝刈りによる軽量化に取り組む予定です。

この論文は NLDB 2025 で Best Paper Award を受賞しました。
