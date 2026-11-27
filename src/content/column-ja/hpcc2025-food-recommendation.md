---
title: "Can Lifestyle Cues from Images and Nutrition Improve Food Recommendation?"
subtitle: "GNN-Enhanced Multimodal Fusion with Contrastive Learning for Smart Health Oriented Food Recommendation System"
date: "2026-11-27"
excerpt: "料理の画像・栄養・材料・調理手順から「どんな生活に合う料理か」を読み取り、グラフニューラルネットワークで利用者と結びつける食品推薦モデル GNNMF-CL を作りました。IEEE HPCC 2025 で Best Paper Award を受賞した論文の解説です。"
readingMinutes: 10
showImage: false
image: "/column-images/hpcc2025-food-recommendation/architecture.png"
imageAlt: "GNNMF-CL の全体図。画像・栄養・材料・調理手順から 3 種類の特徴を取り出し、HGT で利用者ノードと料理ノードを結んで推薦スコアを出す。"
authors:
  - name: "Ryutaro Matsuoka"
    affiliation: "Shiga University"
  - name: "井下 敬翔"
    url: "/about/"
    affiliation: "関西大学"
  - name: "Xiaokang Zhou"
    affiliation: "Kansai University / RIKEN Center for AIP"
  - name: "Zhigao Zheng"
    affiliation: "Wuhan University"
  - name: "Akira Kawai"
    affiliation: "Shiga University"
  - name: "Katsutoshi Yada"
    affiliation: "Kansai University"
tldr: "料理を選ぶときには、見た目や材料だけでなく「減量中」「忙しい」といった生活上の目標も効いています。GNNMF-CL は、VLM が画像から書いた説明文と栄養データを対照学習でそろえて「ライフスタイル特徴」を作り、材料と調理手順の関係を HAN で「味の好み特徴」に、画像を ResNet-50 で「見た目特徴」にして、HGT で利用者と料理のグラフに統合します。AllRecipes では AUC 0.7148、Recall@10 0.1297 で比較手法を上回りました。一方で NDCG@10 は 0.0247 で、HAFR（0.0455）より低く、上位の並び順には課題が残りました。IEEE HPCC 2025 で Best Paper Award を受賞しています。"
citation: |
  @inproceedings{matsuoka2025gnnmfcl,
    title     = {{GNN}-Enhanced Multimodal Fusion with Contrastive Learning for
                 Smart Health Oriented Food Recommendation System},
    author    = {Matsuoka, Ryutaro and Inoshita, Keito and Zhou, Xiaokang and
                 Zheng, Zhigao and Kawai, Akira and Yada, Katsutoshi},
    booktitle = {Proceedings of the IEEE International Conference on High
                 Performance Computing and Communications (HPCC)},
    pages     = {864--871},
    year      = {2025},
    month     = aug
  }
---

<div class="teaser">
<div>

Lifestyle

VLM が書いた料理の説明文と栄養データを **対照学習でそろえ**、「どんな生活に合う料理か」を表す特徴を作る。

</div>
<div>

Fuse

見た目・ライフスタイル・味の好みの 3 特徴を **HGT で利用者と料理のグラフに統合**する。

</div>
<div>

Result

AllRecipes で **AUC 0.7148**（HAFR 0.6435）、**Recall@10 0.1297**。ただし NDCG@10 は HAFR より低い。

</div>
</div>

## 料理は生活に合わせて選ばれる

推薦システムは、購入履歴や属性だけを使う方式から、画像・テキストなど複数の情報源を使う方式へ移ってきました。食品推薦でも、料理の画像やカロリーを使う研究はありました。しかし、材料・調理手順・栄養を組み合わせて、それが利用者の好みにどう効くかを扱った研究は多くありません。

材料は料理どうしで部分的に重なり、同じ材料でも「茹でる」か「焼く」かで受け取られ方が変わります。さらに、料理の選び方は**生活上の目標**に強く左右されます。体重を管理したい人は低カロリーの料理を、忙しい人は効率よく栄養をとれる料理を選びやすく、妊娠中の人や持病のある人は避けたい材料があります。

この研究では、これまで推薦に使われてきた特徴に加えて、料理から**ライフスタイルに関わる特徴**を取り出し、利用者の健康目標や食事制限に合った料理を推薦することを目指しました。

## GNNMF-CL の仕組み

<figure>
  <img src="/column-images/hpcc2025-food-recommendation/architecture-1600.webp" alt="GNNMF-CL architecture" />
  <figcaption><strong>Figure 1.</strong> GNNMF-CL の全体図（論文の Fig. 1）。左の 4 つの入力から 3 種類の特徴を作り、中央の HGT で料理ノードと利用者ノードを結んで、右で推薦確率を計算します。</figcaption>
</figure>

入力は、料理の画像・栄養データ・材料リスト・調理手順と、利用者の情報です。これを 5 つのモジュールで処理します。

| モジュール | 入力 | 使う手法 | 出力 |
|---|---|---|---|
| 見た目特徴 | 画像 | ResNet-50（Food-101 で微調整） | 見た目特徴 |
| ライフスタイル特徴 | 画像・栄養 | VLM（nanoLLaVA-1.5）＋ Sentence-BERT ＋ 対照学習 | ライフスタイル特徴 |
| 味の好み特徴 | 材料・調理手順 | Sentence-BERT ＋ HAN | 味の好み特徴 |
| 統合 | 3 特徴・利用者 | HGT | 料理と利用者の埋め込み |
| 推薦 | 2 つの埋め込み | 多層パーセプトロン＋シグモイド | 推薦確率 |

### ライフスタイル特徴：説明文と栄養を対照学習でそろえる

<figure>
  <img src="/column-images/hpcc2025-food-recommendation/lifestyle-module.png" alt="Lifestyle intention feature module" />
  <figcaption><strong>Figure 2.</strong> ライフスタイル特徴モジュール（論文の Fig. 2）。同じ料理の説明文特徴と栄養特徴を引き寄せ、別の料理とは引き離します。</figcaption>
</figure>

まず VLM（nanoLLaVA-1.5）に料理の画像を見せ、栄養上の特徴・どんな生活に向くか・健康上の利点を含む説明文を書かせます。説明文は Sentence-BERT でベクトルにします。並行して、栄養データも前処理してベクトルにします。

同じ料理の説明文ベクトルと栄養ベクトルを正例の組、ミニバッチ内の別の料理との組を負例として、対照学習で共通の空間にそろえます。温度は 0.3 です。さらに、栄養特徴を k-means で 6 個のクラスタに分け（2〜20 を試してエルボーが出たのが 6）、クラスタ内はまとまり、クラスタ間は離れるような損失を加えます。

### 味の好み特徴：材料と調理手順の関係を HAN で学ぶ

材料リストと調理手順をそれぞれ Sentence-BERT でベクトルにし、材料ノードと調理手順（味）ノードからなるグラフを作ります。コサイン類似度が 0.75 以上の材料は同じものとみなしてまとめます。HAN（Heterogeneous graph Attention Network）で 2 種類のノードの間に双方向にメッセージを流し、調理手順ノードの最終的な表現を「味の好み特徴」とします。

### 統合と学習

料理ノードに 3 つの特徴ノードをつなぎ、利用者が食べた料理とその利用者をつないだグラフを作って、HGT（Heterogeneous Graph Transformer）で情報を流します。これにより、利用者は過去に関わった料理から、料理は共通の利用者を通じて別の料理から情報を受け取ります。

損失は、BPR 損失・対照学習の損失・クラスタ内とクラスタ間の損失・ランキング用の XENDCG 損失の 5 つの和です。

## 実験 1：学習で特徴は分かれるか

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- データ：AllRecipes（英国のレシピサイト。利用者約 68,000 人、料理約 456,000 件、材料約 33,400 種。評価は 1〜5）
- 分割：データセットにあらかじめ用意された学習・検証・テスト
- 主な設定：埋め込み 128 次元、画像入力 1,024 次元、対照学習の温度 0.3、クラスタ損失の重み 1.2・マージン 0.5、Adam（学習率 1×10⁻⁵）
- 可視化：3 種類の特徴を UMAP で 2 次元に写す

</div>

<figure>
  <img src="/column-images/hpcc2025-food-recommendation/umap-1600.webp" alt="UMAP of multimodal features before and after learning" />
  <figcaption><strong>Figure 3.</strong> 3 種類の特徴の UMAP（論文の Fig. 5）。(a) 学習前、(b) 学習後。赤が見た目、青が味の好み（Sensing）、緑がライフスタイル特徴です。</figcaption>
</figure>

学習前は 3 種類の特徴が同じ領域に重なっていて、区別がつきません。学習後は 3 つのはっきり分かれた塊になりました。論文は、それぞれのモジュールが重複の少ない別々の情報をとらえるようになったと解釈しています。ただし、これは図による定性的な確認です。

## 実験 2：既存の推薦手法との比較

<p class="experiment-label">Experiment 2</p>

<div class="setup">

**Setup**

- 評価指標：AUC、NDCG@10、Recall@10
- 負例：料理の人気が偏っている（ロングテール）ことを考え、学習データでの人気に基づいて利用者ごとに 500 件の負例をサンプリング
- 比較手法：LDA、FM、MF-BPR、VBPR、FM-VBPR、HAFR（画像と材料を階層的な注意で使う食品推薦モデル）

</div>

<figure>
  <img src="/column-images/hpcc2025-food-recommendation/baselines-1600.webp" alt="Comparison with baselines" />
  <figcaption><strong>Figure 4.</strong> 比較手法との比較（論文の Table I）。金色が GNNMF-CL、青が最も強い比較手法の HAFR です。AUC と Recall@10 では上回り、NDCG@10 では下回りました。</figcaption>
</figure>

AUC は 0.7148 で、最も強い比較手法 HAFR（0.6435）を含むすべての比較手法を上回りました。Recall@10 は 0.1297 で、HAFR（0.0674）の約 2 倍です。

一方、NDCG@10 は 0.0247 で、HAFR（0.0455）や LDA・FM より低くなりました。NDCG は上位に正解をどれだけ高い順位で並べられたかを見る指標です。論文はこれを、GNNMF-CL が上位の並び順の厳密さより、関連する料理を幅広く拾う方向に働いていると解釈し、上位の順位づけは今後の改善点としています。

## 実験 3：対照学習と HAN を外すと

<p class="experiment-label">Experiment 3</p>

<div class="setup">

**Setup**

- w/o CL：ライフスタイル特徴モジュールから対照学習を外したもの
- w/o HAN：HAN による味の好み特徴を、ランダムに初期化した特徴に置き換えたもの
- 評価：Precision・Recall・F1・NDCG（すべて @10）と AUC

</div>

<figure>
  <img src="/column-images/hpcc2025-food-recommendation/ablation-1600.webp" alt="Ablation study" />
  <figcaption><strong>Figure 5.</strong> アブレーション（論文の Table II）。Precision・Recall・F1 では完全版が最も高く、NDCG では対照学習を外した方が高くなりました。</figcaption>
</figure>

Precision@10・Recall@10・F1@10 では完全版が最も高く、対照学習と HAN のどちらも推薦に役立っていることがわかります。Recall@10 は 0.146 でした。

NDCG@10 だけは、対照学習を外した w/o CL が 0.035 で最も高くなっています。論文は、対照学習を入れると上位リストでの並び方が変わり、厳密な順位より多様さや網羅性が優先される可能性があると述べています。

<figure>
  <img src="/column-images/hpcc2025-food-recommendation/ablation-auc-1600.webp" alt="Ablation AUC" />
  <figcaption><strong>Figure 6.</strong> アブレーションの AUC（論文本文の値）。横軸は 0.70 から始めているため、差が大きく見えています。実際の差は 0.001〜0.004 です。</figcaption>
</figure>

AUC は完全版 0.715、w/o CL 0.711、w/o HAN 0.716 で、差は小さいものでした。論文では ROC 曲線の差分も調べており、対照学習を外すと一貫して真陽性率が下がる一方、HAN を外した場合は一部の範囲でわずかに上回りました。論文は、対照学習の寄与は一貫しているが、HAN の寄与はより小さく、状況に依存すると結論しています。

なお、完全版の Recall@10 と NDCG@10 は Table I（0.1297・0.0247）と Table II（0.146・0.025）で値が異なります。論文にはこの違いの説明がないため、ここではそれぞれの表の値をそのまま載せています。

## わかったこと・わかっていないこと

この研究でわかったのは次の点です。

- 画像から VLM が書いた説明文と栄養データを対照学習でそろえると、料理の「ライフスタイル特徴」を取り出せる。学習後は、見た目・味の好み・ライフスタイルの 3 特徴が別々の塊に分かれた。
- 3 特徴を HGT で利用者と料理のグラフに統合した GNNMF-CL は、AllRecipes で AUC と Recall@10 が比較手法を上回った。
- アブレーションでは、対照学習を外すと Precision・Recall・F1 と AUC が一貫して下がった。HAN の寄与はより小さかった。

一方で、限界もあります。

- NDCG@10 は比較手法より低く、上位の並び順には改善の余地がある。
- 事前学習済みのモジュールを複数使っており、食品や栄養の分野向けには微調整していない。
- ライフスタイル上の目標は暗黙にしか扱っておらず、利用者が料理を選ぶときに何を重視したかを明示的にはモデル化していない。
- データは英語圏のレシピサイトのものだけで、文化や地域の違いへの一般化は確かめていない。

今後は、利用者ごとの判断の理由をとらえて説明できるようにし、推薦の信頼性と透明性を高めることに取り組みます。

本論文は IEEE HPCC 2025 で Best Paper Award を受賞しました。
