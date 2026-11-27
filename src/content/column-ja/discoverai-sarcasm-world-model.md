---
title: "Can Sarcasm Be Read as a Prediction Error?"
subtitle: "World model inspired sarcasm reasoning with large language model agents"
date: "2026-11-27"
excerpt: "皮肉を「言葉の表面」と「その場で普通に期待される評価」のずれとして捉え、LLM エージェントに役割を分けて数値化し、最後はロジスティック回帰で判定する WM-SAR を作りました。Discover Artificial Intelligence 掲載論文の解説です。"
readingMinutes: 12
showImage: false
image: "/column-images/discoverai-sarcasm-world-model/framework.png"
imageAlt: "WM-SAR の全体図。字義・文脈・規範・矛盾・意図の 5 つのエージェントが出した数値を、特徴量化してロジスティック回帰で統合する。"
authors:
  - name: "井下 敬翔"
    url: "/about/"
    affiliation: "関西大学"
  - name: "Shinnosuke Mizuno"
    affiliation: "東京大学"
tldr: "皮肉は「表面は褒めているのに、状況からすれば普通は悪く言うはず」というずれとして現れます。WM-SAR は、世界モデルの「観測 → 潜在状態 → 予測 → 予測誤差 → 判断」という流れに沿って、字義の評価・文脈の仮説・規範にもとづく期待・その差・話者の意図を別々の LLM エージェントに担当させ、最後の判定だけを軽いロジスティック回帰に任せます。3 つのベンチマークで比較手法を上回り（平均 macro-F1 0.750）、外すと最も大きく下がるのは意図のスコアでした。一方、表面も規範も意図もそろって「誠実な褒め言葉」に見える皮肉は取りこぼします。"
links:
  - label: "Paper (Discover Artificial Intelligence)"
    url: "https://doi.org/10.1007/s44163-026-01360-7"
citation: |
  @article{inoshita2026wmsar,
    title   = {World model inspired sarcasm reasoning with large language model agents},
    author  = {Inoshita, Keito and Mizuno, Shinnosuke},
    journal = {Discover Artificial Intelligence},
    volume  = {6},
    number  = {606},
    year    = {2026},
    doi     = {10.1007/s44163-026-01360-7}
  }
---

<div class="teaser">
<div>

Decompose

皮肉の判断を **5 つの役割**（字義・文脈・規範・矛盾・意図）に分け、それぞれが数値と理由を出す。

</div>
<div>

Integrate

最後の判定は LLM ではなく **ロジスティック回帰**。3 データの平均 macro-F1 は 0.750 で、比較手法の中で最高。

</div>
<div>

Diagnose

意図スコアを外すと平均 macro-F1 が **0.750 → 0.558**。ずれの大きさだけでは皮肉と言い切れない。

</div>
</div>

## 皮肉はどこで「ひっくり返る」のか

皮肉は、表面ではほめているのに、実際には批判している発話です。「サーバーを落とすなんて、素晴らしい仕事だね」という文では、言葉は肯定的ですが、サーバーが落ちたという状況は普通なら否定的に評価されます。皮肉を読むには、字義を読むだけでなく、その状況が社会的にどう評価されるはずか、話者が何を意図しているかを推し量る必要があります。

最近の PLM や LLM は皮肉検出でも高い性能を出していますが、多くの場合、判定は一つのモデルにまかされています。そのため、モデルが何を手がかりに皮肉と判断したのか、間違えたときに字義・文脈・意図のどこで失敗したのかがわかりません。

この研究では、皮肉を**観測と予測のずれ**として扱いました。画像の分野で使われる世界モデルは、観測 → 潜在状態 → 予測 → 予測誤差 → 判断という流れをもちます。皮肉も「字義の評価（観測）」と「状況から期待される評価（予測）」が食い違う現象として定義できるので、この流れにそのまま乗せられると考えました。

## WM-SAR の仕組み

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/framework-1600.webp" alt="WM-SAR framework" />
  <figcaption><strong>Figure 1.</strong> WM-SAR の全体図（論文の図をそのまま掲載）。各エージェントは数値と自然言語の理由を出し、最後はロジスティック回帰で統合します。</figcaption>
</figure>

WM-SAR（World-Model-inspired SArcasm Reasoning）は、皮肉の理解に必要な処理を 5 つのエージェントに分けます。どのエージェントも GPT-4.1-mini で動かしています。

| 世界モデルの要素 | WM-SAR のモジュール | 出力 |
|---|---|---|
| 観測 | 字義エージェント | 字義の評価 M_literal ∈ [−1, 1] |
| 潜在状態の推定 | 文脈エージェント | 背景の仮説 C(u)（話し手と聞き手の関係・場面・直前の出来事） |
| 状態の予測 | 規範エージェント | その状況で普通に期待される評価 E_norm ∈ [−1, 1] |
| 予測誤差 | 矛盾検出 | D = M_literal − E_norm と、符号の食い違い SD ∈ {0, 1} |
| 判断 | 意図エージェント＋ロジスティック回帰 | 皮肉の意図スコア T_sar ∈ [0, 1] と最終確率 |

ポイントは 2 つあります。

1. **予測誤差は LLM に考えさせず、引き算で計算する。** 字義と規範は同じ [−1, 1] の尺度で出させ、その差 D を決定的に計算します。符号の判定には ±0.05 の中立域を設けています。
2. **最後の判定は LLM にまかせず、ロジスティック回帰で行う。** 入力は |D|、T_sar、SD の 3 つと、その組み合わせ（D + T、T − D、D × T、√T、log(1 + T) など）です。正則化の強さと判定のしきい値は、train + val の交差検証で決めます。

ずれ D が大きいことは皮肉の必要条件の候補にすぎず、誇張やユーモアでも起こります。そのため、話者の意図を推し量る意図エージェント（心の理論にもとづく推論）を別の経路として残しています。

## 実験 1：既存手法と比べて

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- データ：IAC-V1、IAC-V2（オンライン討論の投稿）、SemEval-2018 Task 3（英語ツイート）。各データを 8:1:1 で分割
- 指標：Accuracy と macro-F1
- 比較：MIARN、SAWS、DC-Net、BERT のファインチューニング、GPT-4.1-mini のゼロショット、CoC / GoC / BoC のプロンプト法、マルチエージェント手法 CAF-I
- LLM を使う手法はすべて GPT-4.1-mini にそろえた（CAF-I も元の GPT-4o から置き換えて再評価）

</div>

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/main-results-1600.webp" alt="Main results" />
  <figcaption><strong>Figure 2.</strong> 3 つのデータセットと平均の macro-F1。金色が WM-SAR、青が GPT-4.1-mini のゼロショット、濃い灰色が BERT です。</figcaption>
</figure>

WM-SAR は 3 つのデータすべてで、Accuracy と macro-F1 の両方が最も高くなりました。平均 macro-F1 は 0.750 で、GPT-4.1-mini 単体（0.730）、BERT（0.713）を上回ります。

目を引くのは、同じ GPT-4.1-mini を使っていても、CoC・GoC・BoC といった推論を促すプロンプトがゼロショットより低いことです（平均 0.698〜0.722）。LLM の出力をそのまま判定に使うより、推論を役割に分けて数値として取り出し、統合するほうが効いていました。ただし IAC-V2 での BERT との差は 0.001 と小さく、どのデータでも大差というわけではありません。

## 実験 2：どの信号が効いているのか

<p class="experiment-label">Experiment 2</p>

ロジスティック回帰に入れる信号を一つずつ外しました。

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/ablation-1600.webp" alt="Ablation" />
  <figcaption><strong>Figure 3.</strong> 信号を外したときの macro-F1。w/o D はずれの大きさ |D|、w/o T は意図スコア、w/o S は符号の食い違い、w/o Interaction は組み合わせ特徴を外した条件です。数値は論文の図から転記しました。</figcaption>
</figure>

最も大きく下がったのは意図スコアを外した場合（w/o T）で、平均 macro-F1 は 0.750 から 0.558 になりました。表面と規範のずれだけでは、皮肉を見分けるには足りないということです。

ずれの大きさ |D| を外すと平均 0.742、組み合わせ特徴を外すと 0.738 で、下がり方は小さいものの一貫しています。符号の食い違い SD は、SemEval-2018 では外した方がわずかに高く（0.720 対 0.714）、短くくだけたツイートでは |D| と T_sar の方が主に効いている可能性があります。

## 実験 3：LLM の大きさを変えると

<p class="experiment-label">Experiment 3</p>

エージェントの中の LLM を GPT-4.1、GPT-4.1-mini、GPT-4.1-nano に入れ替えました。他の設定は同じです。

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/backbone-1600.webp" alt="Backbone robustness" />
  <figcaption><strong>Figure 4.</strong> バックボーンを変えたときの WM-SAR の macro-F1。</figcaption>
</figure>

GPT-4.1 と GPT-4.1-mini の平均はそれぞれ 0.751 と 0.750 で、ほとんど差がありません。データ別に見ると、IAC-V1 では mini の方が高く、SemEval-2018 では GPT-4.1 の方が高くなっています。一方、GPT-4.1-nano では平均 0.646 まで下がりました。文脈の構成や規範・意図の推論の質が落ち、ロジスティック回帰に渡る数値の質が下がったためと考えています。ある程度の推論力があれば、最大のモデルでなくても枠組みは働くと言えますが、確かめたのは GPT-4.1 系列の中だけです。

## 実験 4：推論にかかる時間

<p class="experiment-label">Experiment 4</p>

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/cost-1600.webp" alt="Cost versus accuracy" />
  <figcaption><strong>Figure 5.</strong> 1 件あたりの推論時間（横軸は対数）と平均 macro-F1。</figcaption>
</figure>

1 回か数回 LLM を呼ぶだけの手法は 1 件あたり 1 秒前後です。WM-SAR は複数のエージェントを使うため平均 7.65 秒かかりますが、エージェント同士がやり取りを繰り返す CAF-I（21.10 秒）の 3 分の 1 程度に収まっています。LLM の出力は一度だけ数値として取り出し、判定は軽いロジスティック回帰で行うためです。単純な方法より重いことは確かで、精度との引き換えになります。

## 実験 5：判断の中身を読む

<p class="experiment-label">Experiment 5</p>

まず、テストセットで正解した文と間違えた文で、中間の信号を比べました。

| 指標 | 正解した文 | 間違えた文 |
|---|---|---|
| T_sar の平均 | 0.417 | 0.394 |
| \|D\| の平均 | 0.432 | 0.439 |
| SD = 1 の割合 | 0.245 | 0.286 |

どの信号も単独では大きな差がなく、一つの信号だけでは皮肉を切り分けられないことがわかります。

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/lr-weights-1600.webp" alt="Top-10 LR weights" />
  <figcaption><strong>Figure 6.</strong> ロジスティック回帰の重み（絶対値の上位 10 個、論文の図をそのまま掲載）。正は皮肉側、負は非皮肉側に寄与します。</figcaption>
</figure>

ロジスティック回帰の重みでは、σ(T)、√T、log(1 + T) など意図スコアから作った特徴が上位を占めました。T − D は正、D − T は負の重みで、「意図の信号がずれより強いときに皮肉になりやすく、ずれだけが大きいときは皮肉と判定されにくい」という設計の考え方と合っています。

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/cases-1600.webp" alt="Case studies" />
  <figcaption><strong>Figure 7.</strong> 2 つの事例で各エージェントが出した値。左は正しく非皮肉と判定した丁寧な訂正の投稿、右は皮肉を見逃した例です。</figcaption>
</figure>

右の例 "A truly charming publication. Overflowing with the warmth of human goodness." では、字義も規範もそろって 0.80、ずれは 0、意図スコアも 0.10 でした。すべてのエージェントが「誠実な褒め言葉」と読んだため、皮肉を見逃しています。このように表面・規範・意図がそろって肯定的に見える皮肉は、ずれと意図を軸にした WM-SAR が苦手とする型です。ただ、どのエージェントがどう読んだかを数値と理由で追えるので、どこで読み違えたかは確認できます。

## わかったこと・わかっていないこと

わかったことは次の 3 点です。

- 皮肉の理解を字義・文脈・規範・ずれ・意図に分け、ロジスティック回帰で統合すると、3 つのベンチマークで既存の深層学習手法・LLM 手法を上回った。
- 最も効いているのは話者の意図の推論で、表面と規範のずれは補助的な信号として働く。
- 中間の数値と理由が残るため、正解・誤りのどちらについても、どこで何が起きたかを人が追える。

限界もあります。使った LLM は GPT-4.1 系列だけで、他の系列で同じ傾向になるかは確かめていません。評価は一文単位のデータで、対話の履歴が必要な皮肉は扱っていません。表面・規範・意図がそろって肯定的に見える皮肉は取りこぼしやすく、特徴量の間に冗長さも残っています（L2 正則化で抑えています）。また、各エージェント内部の推論は部分的に見えないままです。

今後は、別系列の LLM での検証、対話の文脈を含むデータへの拡張、マルチモーダルな情報への展開を考えています。
