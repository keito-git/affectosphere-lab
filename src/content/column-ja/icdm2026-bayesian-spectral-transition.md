---
title: "What Does Annotator Disagreement Reveal about How Emotions Move in Conversation?"
subtitle: "Bayesian Spectral Emotion Transition Discovery from Multi-Annotator Disagreement"
date: "2026-11-27"
excerpt: "会話の感情ラベルを多数決で 1 つにまとめず、アノテーターの票の分布のまま残して、感情がどう移り変わるかを調べました。嫌悪と怒りは行き来しやすく、喜びと怒りは続きにくいという構造が、教師なしで取り出せました。IEEE ICDM 2026 採択論文の解説です。"
readingMinutes: 12
showImage: false
image: "/column-images/icdm2026-bayesian-spectral-transition/pipeline.png"
imageAlt: "BSETD の全体図。複数アノテーターのソフトラベルから遷移行列の事後分布を作り（Stage 1）、グラフラプラシアンのスペクトル分解で慣性と伝染に分ける（Stage 2）。"
authors:
  - name: "井下 敬翔"
    url: "/about/"
    affiliation: "関西大学"
  - name: "Takato Ueno"
    affiliation: "Shiga University"
tldr: "会話の感情コーパスでは、EmotionLines の発話の 72.6% でアノテーターの判断が割れ、14.3% は多数決すら決まりません。BSETD は票の分布（ソフトラベル）をそのまま使い、感情の遷移行列をベイズ推定して、各セルに信用区間と FDR 制御つきの有意判定を付けます。さらにグラフのスペクトル分解で、同じ話者の中で続く「慣性」と、話者をまたいで移る「伝染」を分けます。EmotionLines では disgust→anger（log2 lift +0.94）が最も起きやすく、joy→anger（−0.90）が最も起きにくい遷移でした。5 つのデータ源の間で構造の相関は 0.79〜0.98 でした。発見されるのは関連であり、因果ではありません。"
links:
  - label: "Paper (IEEE ICDM 2026, accepted)"
    url: "https://lab.affectosphere.group/news/20260816-icdm2026-bsetd/"
  - label: "Preprint (arXiv)"
    url: "https://arxiv.org/abs/2606.01906"
  - label: "Code"
    url: "https://github.com/keito-git/bayesian-spectral-emotion-transition-discovery"
citation: |
  @inproceedings{inoshita2026bsetd,
    title     = {Bayesian Spectral Emotion Transition Discovery from
                 Multi-Annotator Disagreement},
    author    = {Inoshita, Keito and Ueno, Takato},
    booktitle = {Proceedings of the IEEE International Conference on Data Mining (ICDM)},
    year      = {2026},
    note      = {Accepted, to appear}
  }
---

<div class="teaser">
<div>

Discover

**disgust ↔ anger** は起きやすく（log2 lift +0.94 / +0.86）、**joy ↔ anger** は起きにくい（−0.90 / −0.89）。

</div>
<div>

Separate

同じ話者の中で続く確率は、話者が替わったときより **7 感情すべてで高い**。差が最も大きいのは anger（+0.146）。

</div>
<div>

Replicate

5 つのデータ源の間で、遷移構造の相関は英語内 **0.91〜0.98**、中国語 M3ED とは **0.79〜0.85**。

</div>
</div>

## 多数決で捨てられる情報

会話の中で感情は移り変わります。最初は平静だった人が励まされて喜び、しばらくその気分が続き、思わぬ知らせで驚く。こうした「ある感情の次にどの感情が来やすいか」という遷移の構造は、メンタルヘルスのスクリーニングや対話システムの基礎になります。

ところが、会話の感情コーパスをつくるときは、複数のアノテーターの判断を多数決で 1 つのラベルにまとめるのが普通です。EmotionLines では、5 人のアノテーターの判断が割れる発話が 72.6%、多数決が成立しない発話が 14.3% あります。これは作業ミスというより、その発話の感情が本当に曖昧であることを反映しています。多数決はこの不確かさを取り返せない形で消してしまいます。

既存の会話感情認識（ERC）は、次の発話の感情ラベルを当てる方向で進んできました。そこではラベルは予測の目標であって、遷移の構造そのものを理解する対象にはなっていません。この研究では、**票の分布（ソフトラベル）を残したまま、感情の遷移構造を教師なしで見つける**ことを問いにしました。

## BSETD の仕組み

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/pipeline-1600.webp" alt="BSETD pipeline" />
  <figcaption><strong>Figure 1.</strong> BSETD の全体図（論文の図 1）。Stage 1 でソフトラベルから遷移行列の事後分布を作り、同一話者（慣性）と話者間（伝染）に分けます。Stage 2 では対称化した行列のスペクトル分解で、低周波（慣性）と高周波（伝染）の成分を取り出します。</figcaption>
</figure>

BSETD（Bayesian Spectral Emotion Transition Discovery）は二段階で動きます。感情は Ekman の 7 カテゴリ（neutral, joy, sadness, fear, anger, surprise, disgust）です。

1. **Stage 1：ベイズ事後分布**。隣り合う 2 発話のソフトラベルの外積を足し合わせて、7×7 の「ソフトな遷移回数」を作ります。ラベルが one-hot なら通常の遷移回数と同じになります。各行に Dirichlet 事前分布を置いた Dirichlet–Multinomial モデルで事後分布を閉じた形で求め、事前分布の集中度は経験ベイズで推定します。各セルには 95% 信用区間と、周辺分布との比である lift が付き、非対角 42 セルには Benjamini–Hochberg 法で FDR を制御した有意判定をかけます。同じ話者が続く発話対と、話者が替わる発話対を分けて数えると、慣性と伝染の行列が得られます。
2. **Stage 2：スペクトル分解**。事後平均の遷移行列を重み付きグラフとみなし、対称化した上で正規化グラフラプラシアンを固有分解します。固有値の中央値で低周波と高周波に分け、低周波成分の対角から慣性指標 I_j、高周波成分の非対角から伝染指標 C_j を計算します。

注意点が 2 つあります。対称化によって「j→k」と「k→j」の向きの違いは Stage 2 では失われ、向きの情報は Stage 1 と話者別の分割だけが担います。また、見つかる辺は**関連であって因果ではありません**。図 1 の例のように、コンサートの喜びのあとに雨の悲しみが来ても、それは感情の伝達ではなく外の出来事のせいかもしれません。

## 実験 1：どの遷移が起きやすく、どれが起きにくいか

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- データ：EmotionLines（29,245 発話・2,000 対話・1 発話あたり 5 人のアノテーター）。票の分布をそのままソフトラベルにする
- 指標：log2 lift（次の発話の周辺分布に対する、遷移確率の比の対数）
- 有意判定：非対角 42 セルに BH-FDR（q = 0.10）

</div>

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/top-transitions-1600.webp" alt="Top-10 transitions by log2 lift" />
  <figcaption><strong>Figure 2.</strong> EmotionLines で |log2 lift| が大きい上位 10 の遷移（論文の表 I）。金色は起きやすい遷移、青は起きにくい遷移です。</figcaption>
</figure>

発話対は 27,245 あり、総量が大きいため、BH-FDR のリストに入った非対角セルはすべて独立の帰無仮説を棄却しました。そのため論文では有意かどうかより、効果量（log2 lift）の順位を主に見ています。

最も起きやすいのは disgust→anger（+0.94）と anger→disgust（+0.86）で、Plutchik の感情の輪で隣り合う組です。最も起きにくいのは joy→anger（−0.90）と anger→joy（−0.89）でした。この 2 つは Plutchik の輪では向かい合わせではありませんが、Russell の円環モデルの快・不快の軸では反対側にあります。どちらも覚醒度が高い感情なので、覚醒の軸だけではこの結果を説明できません。距離の教師なしで、2 つの異なる感情空間の特徴が遷移の統計から出てきたことになります。

fear→anger（+0.49）も起きやすい側でした。論文は、恐れのあとに防御的・攻撃的な反応が来るという評価理論の説明と整合するとしつつ、BSETD が推定しているのは条件付きの関連だけだと明記しています。

## 実験 2：同じ話者の中で続くか、相手に移るか

<p class="experiment-label">Experiment 2</p>

同じ話者が続けて話す発話対（慣性）と、話者が替わる発話対（伝染）に分けて Stage 1 を当て、自己ループ（同じ感情が続く確率）を比べました。

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/inertia-contagion-1600.webp" alt="Self-loop posterior means on inertia and contagion splits" />
  <figcaption><strong>Figure 3.</strong> 同じ感情が続く確率の事後平均（論文の表 II）。金色が同一話者、青が話者間。右の数字は差です。</figcaption>
</figure>

7 感情すべてで、同じ話者の中で続く確率の方が高くなりました。差が大きいのは anger（+0.146）と sadness（+0.116）で、同じ人が話している間は続きやすく、相手に渡ると薄れやすい感情です。差が小さいのは joy（+0.022）と surprise（+0.039）で、相手に引き継がれる確率と、本人の中で続く確率がほぼ同じです。これは Hatfield らが示した、喜びや驚きの社会的な伝わりやすさと整合します。

disgust→anger と anger→disgust の起きやすさも、同一話者の分割（log2 lift +1.28 / +1.14）の方が話者間（+0.72 / +0.66）より強く出ました。Gottman が関係破綻の予兆として挙げた怒りから軽蔑・嫌悪へのエスカレーションが、相手とのやりとりより、話し手自身の中で深まる形で現れていると読めます。逆に fear→anger は、話者間の lift が同一話者の lift を上回る唯一の感情間の組でした。

## 実験 3：別のコーパス、別の言語でも同じ構造が出るか

<p class="experiment-label">Experiment 3</p>

<div class="setup">

**Setup**

- EmotionLines：5 人の実アノテーターの票（主評価）
- MELD：13,708 発話。1 発話 1 ラベルを Dirichlet 平滑化（集中度 3.0）で疑似ソフトラベル化
- DailyDialog：102,979 発話。one-hot のまま
- DailyDialog-LLM：同じ発話を GPT-5.4-mini で温度 1.0・5 回独立に再ラベル付け
- M3ED：中国語ドラマ 23,893 発話。3 人のアノテーター
- 比較：非対角 42 セルの事後平均の Pearson 相関

</div>

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/cross-corpus-1600.webp" alt="Cross-corpus correlations" />
  <figcaption><strong>Figure 4.</strong> 5 つのデータ源の間の、遷移構造（非対角 42 セル）の Pearson 相関（論文の表 III）。</figcaption>
</figure>

英語のデータ源どうしでは 0.91〜0.98、中国語の M3ED と英語の 3 コーパスの間では 0.79〜0.85 でした。実アノテーターの EmotionLines と疑似ソフトラベルの MELD でも 0.910（95% CI [0.899, 0.917]）で、どの遷移が起きやすいかは、ソフトラベルの作り方が変わっても保たれます。中国語との相関がやや低いのは、言語や文化による違いが入る余地を残した結果と論文は読んでいます。

一方、同じ感情が続く確率（対角）はコーパスによって大きく違いました。DailyDialog は neutral が続きやすく、M3ED は anger（0.65）や sadness（0.54）のような負の感情が続きやすいという特徴があります。

人のハードラベルと LLM の仮想ソフトラベル（同じ発話）の相関は 0.979 で、構造はほぼ同じでした。ただし LLM の 5 回の判断が割れた率は 12.5% で、実アノテーターの 72.6% より一桁低くなっています。LLM は最頻のラベルの構造は再現しても、人の不確かさは強く縮めてしまうということで、論文はこの一致を「人の複数判断の代わりになる」とは読んでいません。

## 実験 4：慣性と伝染をスペクトルで分ける

<p class="experiment-label">Experiment 4</p>

Stage 2 を EmotionLines の事後平均行列に当てました。7 つの固有値は中央値 λ* ≈ 0.88 で分かれ、低周波 4 モード・高周波 3 モードになりました。

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/results-overview-1600.webp" alt="BSETD results on EmotionLines" />
  <figcaption><strong>Figure 5.</strong> EmotionLines での結果（論文の図 2）。(a) log2 lift のヒートマップ（* は BH-FDR で有意なセル）、(b) 低周波成分（ノードの大きさが慣性指標）、(c) 高周波成分（線の太さが伝染の強さ）。</figcaption>
</figure>

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/spectral-indices-1600.webp" alt="Inertia and contagion indices" />
  <figcaption><strong>Figure 6.</strong> 感情ごとの慣性指標と伝染指標（論文の表 IV）。右下が「本人の中で続く」感情、左上が「相手に移りやすい」感情です。</figcaption>
</figure>

| 感情 | 慣性指標 I_j | 伝染指標 C_j |
|---|---|---|
| neutral | 0.378 | 0.025 |
| joy | 0.338 | 0.011 |
| sadness | 0.227 | 0.010 |
| anger | 0.206 | 0.028 |
| surprise | 0.177 | 0.031 |
| fear | 0.162 | 0.046 |
| disgust | 0.123 | 0.052 |

慣性では neutral と joy が上位（0.378 / 0.338）、伝染では disgust と fear が上位（0.052 / 0.046）でした。慣性を担う感情と、伝染的にふるまう感情が別のものとして分かれています。これは、覚醒度の高い負の感情は話者の間で伝わりやすいという Hatfield の説明と、中立や正の感情は本人の中で持続するという Kuppens の説明の両方と整合します。この分かれ方は前もって仮定したものではなく、固有値を中央値で切るという 1 つの操作から出てきたものです。

論文は、これらの対応はあくまで解釈であり、心理学的な仕組みを特定したものではないとしています。2 つの帯域は統計的な構成物で、その振る舞いが慣性・伝染の概念と整合する、という位置づけです。

## 実験 5：結果はどこまで頑健か

<p class="experiment-label">Experiment 5</p>

不確かさ・帰無分布・部分集団・モデル選択・下流予測の 5 つの観点で確かめました。

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/robustness-1600.webp" alt="Robustness checks" />
  <figcaption><strong>Figure 7.</strong> (a) アノテーターを R 人に減らしたときの、5 人全員の場合との相関。(b) BSETD の lift を特徴量として次の感情の予測に加えたときの macro-F1（論文の表 VI）。ロジスティック回帰は「改善なし」とだけ報告されています。</figcaption>
</figure>

| 確認項目 | 結果 |
|---|---|
| 対話単位のクラスタ・ブートストラップ（慣性−伝染の差の 95% CI 下限） | joy +0.003、anger +0.112（7 感情とも 0 を含まない） |
| 対話内の並べ替え検定（B = 50） | p < 0.02 |
| 6 つの部分集団の間の相関 | 0.873〜0.978 |
| Friends と EmotionPush の間の相関 | 0.962 |
| ハードラベルに置き換えたとき（判断が最も割れる上位 10% での事後平均の平均絶対偏差） | 0.014 |
| 事前分布を α = 1 に固定 | lift の順位は変化なし |
| 有向ラプラシアン（慣性 / 伝染指標の相関） | 0.91 / 0.80 |

アノテーターを 2〜4 人に減らしても、5 人の場合と 0.991〜0.999 で一致しました。並べ替え検定では、実データの最大 |log2 lift| = 0.94 がすべての並べ替えを上回り、構造が周辺分布だけからは生じないことを示しています。

下流の予測に lift を加えた効果は小さく、ロジスティック回帰では改善なし、2 系統 GRU で +0.015、凍結 DistilBERT で +0.007 でした。エンコーダが強くなるほど寄与は縮むため、論文は BSETD を予測器ではなく発見の枠組みとして位置づけています。

表の 5 行目には、もう 1 つ大事な結果があります。票の分布を多数決のハードラベルに置き換えても、lift の順位は変わらず、事後平均の動きも 0.014 にとどまりました。論文はこれを正直に認め、**不一致を残すことで「どの遷移が見つかるか」が変わる、とは主張しません**。不一致を残す意味は、信用区間や FDR 判定のもとになる事後分布の広がりを持てることと、多数決が決まらない 14.3% の発話も恣意的なタイブレークなしに使えることにある、としています。

## わかったこと・わかっていないこと

この研究でわかったのは次の 3 点です。

- アノテーターの票の分布をそのまま使っても、会話の感情遷移の構造は教師なしで取り出せる。Plutchik で隣り合う disgust ↔ anger は起きやすく、Russell の快・不快が反転する joy ↔ anger は起きにくい。
- 同じ感情が続く確率は、7 感情すべてで同一話者の方が高い。スペクトル分解では、慣性を担う感情（neutral, joy）と伝染的な感情（disgust, fear）が分かれる。
- この構造は 5 つのデータ源、2 つの言語、アノテーター数の削減、部分集団の分割に対して安定している。

一方で、論文は 6 つの限界を挙げています。コーパス全体で集計するため、1 つの対話の中で前半と後半の流れが違う場合は混ざって見えます。Stage 2 の対称化は向きの情報を捨てます。ソフトラベルの外積は隣り合うラベルの条件付き独立を仮定しています。推定は隣り合う発話の感情ラベルだけを見ており、話題・外の出来事・話者の役割などの文脈は観測していないので、ある辺は共通の原因を反映しているだけかもしれません。不一致には意味の曖昧さやカテゴリの重なり、アノテーター固有の偏りも混ざっており、今回の設計ではそれらを分けられません。そして証拠は関連と再現性にもとづくもので、仕組みを示したものではなく、学習済みの ERC モデルが持つ遷移構造との定量比較もしていません。

今後は、対話ごとの階層事後分布で対話内の変化を見ること、向きを保ったスペクトル解析、そして LLM の仮想アノテーターが人の不確かさの「形」まで再現できるかを確かめることに取り組みます。

すべての表と図を再現するスクリプトを含むコードは [github.com/keito-git/bayesian-spectral-emotion-transition-discovery](https://github.com/keito-git/bayesian-spectral-emotion-transition-discovery) で公開しています。
