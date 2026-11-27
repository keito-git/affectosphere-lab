---
title: "Where Does LLM Context Actually Help Emotion Recognition?"
subtitle: "ACE-Net: Diagnosing Learned Deep Prior Injection for Fine-Grained Emotion Recognition in Under-Determined Texts"
date: "2026-11-27"
excerpt: "感情語を含まない短文の感情認識に、LLM が作った文脈を中間層へ注入して効くかを調べました。効いていたのは辞書の中身ではなく、注入する層の深さでした。Knowledge-Based Systems 採択論文の解説です。"
readingMinutes: 15
showImage: false
image: "/column-images/ace-net/architecture.png"
imageAlt: "ACE-Net の全体図。オフラインで LLM の文脈記述から 32 個のプロトタイプ辞書を作り、実行時に中間層へ文脈ベクトルを足し込む。"
tldr: "GoEmotions のテスト文の 88.8% には感情語がありません。ACE-Net は、LLM が書いた文脈記述を 32 個のプロトタイプにまとめて凍結し、Transformer の中間層に注入します。macro-F1 は +0.041 改善しました。ところが分解してみると、辞書の中身・離散選択・適応温度はどれも単独では効いておらず、効果は「中間層に入れた学習済みベクトル 1 本」でほぼ説明できました。効く場所（中間層）と効く入力（文脈が足りない文）も特定し、本番投入前にどの入力で効くかを見分ける指標 FORGE-Ω も作りました。"
links:
  - label: "Paper (KBS, accepted)"
    url: "https://lab.affectosphere.group/news/20261124-kbs-ace-net/"
  - label: "Code"
    url: "https://github.com/keito-git/ace-net"
  - label: "Data"
    url: "https://doi.org/10.5281/zenodo.23415199"
citation: |
  @article{inoshita2026acenet,
    title   = {{ACE-Net}: Diagnosing Learned Deep Prior Injection for Fine-Grained
               Emotion Recognition in Under-Determined Texts},
    author  = {Inoshita, Keito},
    journal = {Knowledge-Based Systems},
    year    = {2026},
    note    = {Accepted, to appear}
  }
---

<div class="teaser">
<div>

Diagnose

効果の正体は **学習済みベクトル 1 本**。辞書つきの完全版 0.4965 に対し、ベクトル 1 本だけで 0.4960。

</div>
<div>

Locate

効くのは **中間層（L5〜L8）**。最終層付近に入れると、逆に基準より下がる。

</div>
<div>

Select

効くのは **文脈が足りない文だけ**。GoEmotions で +0.041、文脈が文中にそろう ISEAR では −0.001（有意差なし）。

</div>
</div>

## 感情語のない文をどう読むか

SNS の短い投稿から感情を読み取るタスクは、28 種類の感情を見分ける GoEmotions のように、細かな分類へ進んでいます。ここで問題になるのが、**感情を表す言葉がそもそも書かれていない文**です。GoEmotions のテストセット 5,427 文のうち、88.8% にあたる 4,817 文には明示的な感情語がありません。文脈が足りない文は例外ではなく、むしろ普通です。

足りない文脈を補う方法として、まず思いつくのは LLM に背景を書かせて入力につなげることです。しかし実際に GPT-4o-mini の文脈を入力の後ろにつなげてみると、macro-F1 は 0.4559 から 0.4552 になり、改善しませんでした。TF-IDF で近い文を取ってくる RAG 型も 0.452 でした。

そこでこの研究では、「文脈を足すか」ではなく、**いつ・どこに・どんな形で足すと効くのか**を問いにしました。

## ACE-Net の仕組み

<figure>
  <img src="/column-images/ace-net/architecture.png" alt="ACE-Net architecture" />
  <figcaption><strong>Figure 1.</strong> ACE-Net の全体図。上がオフラインの辞書づくり、下が実行時の注入です。推論時に LLM は呼びません。</figcaption>
</figure>

ACE-Net は二段階で動きます。

1. **オフライン（1 回だけ）**：学習データから 3,500 文を選び、GPT-4o-mini に「この文の感情を読むのに役立つ背景」を書かせます。それを DeBERTa でベクトルにし、K-means で 32 個のプロトタイプにまとめて凍結します。感情ラベルは使いません。
2. **実行時**：入力文ごとに、32 個のプロトタイプをどう混ぜるかを小さなヘッドが決め（Gumbel-Softmax）、できた文脈ベクトルを 9 層目（0 始まりで L = 8）の全トークンに足します。混ぜ方の鋭さ（温度）も入力の曖昧さに合わせて変えます。

追加パラメータは学習するもので 25,377 個、凍結辞書を含めても約 5 万個で、バックボーンの +0.06% です。推論は 1 回の順伝播で終わります。

この設計は、**辞書の中身・選び方・温度・注入する層をそれぞれ切り離して調べられるように**組んであります。精度を上げることより、どの部品が効いているのかを突き止めることを目的にしたためです。

## 実験 1：そもそも効くのか

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- データ：GoEmotions（Reddit コメント 58,009 件・28 感情・マルチラベル）
- バックボーン：DeBERTa-v3-base（全条件で同じ）
- 評価：macro-F1、5 シード（42 / 123 / 456 / 789 / 1024）の平均と標準偏差
- 比較：文脈なし（A1）、RAG（A2）、LLM 文脈の連結（A3）、自己学習（A4）、Prefix-tuning 1 トークン（A6）

</div>

<figure>
  <img src="/column-images/ace-net/main-results.png" alt="Main results on GoEmotions" />
  <figcaption><strong>Figure 2.</strong> GoEmotions での macro-F1。点線は文脈なしの基準（A1）。灰色の 3 本は文脈を足す既存のやり方で、いずれも基準とほぼ同じです。GPT-4o-mini のゼロショット CoT（A5）は 0.3099 で、軸の外になるため省いています。</figcaption>
</figure>

ACE-Net は 0.4965 で、基準より +0.041 高くなりました。文脈を文字列としてつなげる A3 は効かず、**同じ LLM の文脈でも、蒸留して中間層に入れると効く**ことがわかります。

ただし、ここで目を引くのは青い棒です。学習可能なベクトルを 1 トークン分だけ入れる Prefix-tuning（A6）が 0.5037 で、ACE-Net と差がありません（Welch の t 検定で p = 0.14）。辞書も LLM も使わない手法が同じ水準に届いています。これが次の実験の出発点になりました。

## 実験 2：何が効いているのか

<p class="experiment-label">Experiment 2</p>

部品を一つずつ外して、macro-F1 がどう変わるかを見ました。

<figure>
  <img src="/column-images/ace-net/ablation.png" alt="Core-mechanism ablation" />
  <figcaption><strong>Figure 3.</strong> 部品を外したときの macro-F1。金色が完全版、青は辞書も選択も使わず「L = 8 に学習済みベクトルを 1 本足すだけ」の条件です。最終層の CLS に足す late fusion だけがはっきり下がります。</figcaption>
</figure>

温度を固定しても、Gumbel を外しても、多様性の損失を外しても、ほとんど変わりません。そして **辞書を丸ごと捨てて、ベクトル 1 本を L = 8 に足すだけ（C_freevec）でも 0.4960** で、完全版との差は −0.0005 でした。

「差が有意でない」だけでは同じとは言えないので、直接確かめました。テスト文ごとに作られた文脈ベクトルを比べると、平均ベクトルとのコサイン類似度は 1.000、相対的なばらつきは 0.0001 でした。全入力に平均ベクトル 1 本を入れても macro-F1 は 0.4964 で、**予測は全件同じ**でした。入力ごとに文脈を選ぶ仕組みは、学習が終わる頃には働いておらず、ACE-Net は実質的に「固定の学習済み事前知識（learned deep prior）」として効いていたことになります。

実験 1 の Prefix-tuning と結果が重なるのもこれで説明がつきます。内側からの分解と外側からの比較が、同じ結論を指しています。

## 実験 3：どの層に入れるべきか

<p class="experiment-label">Experiment 3</p>

効果がベクトル 1 本で説明できるなら、残る変数は「どこに入れるか」です。12 層すべてに入れ分けました。

<figure>
  <img src="/column-images/ace-net/layer-sweep.png" alt="Injection-layer sweep" />
  <figcaption><strong>Figure 4.</strong> 注入する層ごとの macro-F1（帯は 5 シードの標準偏差）。中間層 L5〜L8 で 0.49〜0.50 にそろい、L10・L11 では基準を下回ります。</figcaption>
</figure>

中間の L5〜L8 では 0.49〜0.50 でほぼ横並びです。最高は L6 の 0.5004 ですが、L8 との差 0.0017 はシードのばらつきの範囲内なので、「L8 でなければならない」とは言いません。L8 はこの帯の中でばらつきが最も小さい（標準偏差 0.0043）ため採用しました。

一方、最終層に近い L10 では 0.4382、L11 では 0.3728 まで落ち、**文脈を入れない基準より悪く**なります。注入ベクトルの大きさを変える対照実験でも、中間層の結果は変わらず、落ちた層は大きさを変えても回復しませんでした。効果を決めているのは大きさではなく深さです。

## 実験 4：どんな文で効くのか

<p class="experiment-label">Experiment 4</p>

性質の違う 3 つのデータセットで同じことをしました。ISEAR は「When I ... I felt ...」という自己語りの文で、文脈が文の中にそろっています。効かないはずの対照として入れています。

<figure>
  <img src="/column-images/ace-net/selectivity.png" alt="Selectivity across datasets" />
  <figcaption><strong>Figure 5.</strong> データセットごとの改善幅。文脈が足りないほど効き、文脈が文中にそろう ISEAR では効きません。</figcaption>
</figure>

GoEmotions（+0.041）＞ SemEval-2018（+0.013）＞ ISEAR（−0.001、有意差なし）の順になりました。ただし 3 つのデータはラベル数や文の出どころも違うので、この並びだけで結論にはしません。そこで GoEmotions の中で、文脈の足りなさの種類ごとに分けました。

| 層 | 内容 | n | 改善幅 | p |
|---|---|---|---|---|
| S1 | 感情語なし | 4,817 | +0.025 | < 0.01 |
| S2 | 短文 | 1,991 | +0.044 | < 0.001 |
| S3 | 暗黙の前提 | 89 | n.s. | 0.936 |
| S4 | 皮肉 | 16 | n.s. | 0.692 |

同じデータの中でも、感情語がない文（S1）と短い文（S2）で有意に効いています。S3・S4 は件数が少なすぎて判断できないため、そのまま載せています。

さらにクラス別に見ると、改善は**極端に少ない 3 クラスに集中**していました。

<figure>
  <img src="/column-images/ace-net/tail3.png" alt="Tail-3 decomposition" />
  <figcaption><strong>Figure 6.</strong> 改善をクラスの頻度で分解したもの。最も少ない 3 クラスを除くと改善は +0.008（有意差なし）で、3 クラスだけを見ると +0.315 です。</figcaption>
</figure>

macro-F1 の改善のうち 83.3% が、最も少ない 3 クラスから来ています。pride と relief では、基準モデルの F1 が 0 だったのに対し、ACE-Net は 0.411 と 0.230 でした。基準モデルが 0 なのは、しきい値 0.5 のもとで一度も陽性と予測しないためで、特徴がまったくないわけではありません。

## 実験 5：クラスの重みづけで足りるのでは？

<p class="experiment-label">Experiment 5</p>

少ないクラスに効くなら、ロングテール向けの標準的な手当て（ロジット調整、クラス重みつき損失）で同じことができるのでは、という疑問が出ます。同じ条件で比べました。

<figure>
  <img src="/column-images/ace-net/rebalancing.png" alt="Comparison with long-tail rebalancing" />
  <figcaption><strong>Figure 7.</strong> 基準からの改善幅。標準的な手当てで届くのは ACE-Net の改善の 4〜5 割です。</figcaption>
</figure>

クラス重みつき損失が強い方で +0.0207、ACE-Net の改善の約 51% です。残りの約半分（+0.020 前後）は、クラスの頻度を補正するだけでは届かない部分でした。重みづけと中間層への事前知識の注入は、置き換えではなく補い合う関係にあります。

## 実験 6：本番の前に、効く入力を見分ける

<p class="experiment-label">Experiment 6</p>

新しいドメインに入れる前に「どの入力で効くか」がわかると便利です。FORGE-Ω は、ラベル付きの小さなサンプルで、注入ありとなしの分類損失の差（ΔL）を文ごとに計算し、それを効き目の目安にします。

<figure>
  <img src="/column-images/ace-net/forge-omega.png" alt="FORGE-Omega correlations" />
  <figcaption><strong>Figure 8.</strong> 各シグナルと文ごとの改善量との相関（頻度をそろえた 444 文）。損失差 ΔL は 2 つのバックボーンで正の相関を示し、ラベルを使わない代替指標は相関しませんでした。</figcaption>
</figure>

DeBERTa で r = 0.345、別のバックボーンの BERT でも r = 0.477 と、損失差は効く入力をとらえていました。一方、ラベルを使わずに計算できる ΔL_mask は r = 0.066 で有意ではなく、今回は不採用としました。基準モデルの確信度や上位 2 クラスの差も、改善量とはほとんど相関しませんでした。つまり FORGE-Ω は、少量のラベル付きデータで行う**導入前のスクリーニング**として使う指標です。

## わかったこと・わかっていないこと

この研究でわかったのは次の 3 点です。

- LLM の文脈を中間層に入れると、文脈が足りない文で効く。ただし効果の正体は辞書の中身ではなく、**中間層に置いた学習済みの事前知識**だった。
- 効く場所は中間層の帯で、最終層付近では逆効果になる。
- 効く入力は文脈が足りない文と、極端に少ないクラス。文脈が文中にそろう場合は効かない。

一方で、限界もあります。辞書づくりには一度だけ GPT-4o-mini の API が必要で、完全に LLM なしではありません。評価はどれも一文単位のタスクで、文書単位では試していません。皮肉や暗黙の前提の層は件数が少なく、結論を出せていません。ラベルなしで効き目を見分ける指標も、今後の課題です。

今後は、辞書を自己教師ありで更新して LLM への依存をなくすことと、ラベルを使わない監視指標をつくることに取り組みます。

コード：[github.com/keito-git/ace-net](https://github.com/keito-git/ace-net)、データ（辞書・生成した文脈記述・層掃引の結果など）：[Zenodo](https://doi.org/10.5281/zenodo.23415199) で公開しています。
