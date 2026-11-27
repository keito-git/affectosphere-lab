---
title: "Are AI Essays Less Original, or Just More Alike?"
subtitle: "Argument Rarity as a Measure of Essay Originality in the Age of AI-Assisted Writing"
date: "2026-11-27"
excerpt: "エッセイの主張・根拠・論証構造が、同じ課題の学生エッセイの中でどれくらい珍しいかを測る枠組み AROA を提案しました。AI のエッセイは 1 本ずつではそれほど典型的ではないのに、集団としては非常に似通っていました。Research Methods in Applied Linguistics 採択論文の解説です。"
readingMinutes: 13
showImage: false
image: "/column-images/rmal-argument-rarity/framework.png"
imageAlt: "AROA の処理の流れ。LLM でエッセイから主張・理由・根拠・反論・再反論を取り出し、構造・主張・根拠の希少性と対話的な展開を計算し、品質で調整して最終スコアにする。"
authors:
  - name: "井下 敬翔"
    url: "/about/"
    affiliation: "関西大学"
  - name: "Michiaki Omura"
    affiliation: "Arbege Corporation"
  - name: "Tsukasa Yamanaka"
    affiliation: "College of Life Sciences, Ritsumeikan University"
  - name: "Go Maeda"
    affiliation: "Office of General Education, Ritsumeikan University"
  - name: "Kentaro Tsuji"
    affiliation: "Office of General Education, Ritsumeikan University"
tldr: "LLM が流暢で整った文章を書けるようになり、文章の品質だけでは学生自身が考えたかどうかを見分けにくくなりました。AROA は、エッセイの主張・根拠・論証構造が、同じ課題を書いた学生エッセイの中でどれくらい珍しいかを測り、独創性のうち「新規性」の側面を数値にします。学生エッセイ 1,354 本と GPT-4.1-mini のエッセイ 1,000 本に適用すると、AI のエッセイは集団としては非常に均質で、集団内の主張の多様性は学生の約 3 分の 1 でした。一方、学生集団と比べた 1 本ずつの典型性はそれほど変わりませんでした。どちらが見えるかは参照コーパスの構成で決まります。また、捏造した根拠にも高い得点が付くなど、希少性をそのまま独創性とは呼べないこともわかりました。"
links:
  - label: "Paper (RMAL, accepted)"
    url: "https://lab.affectosphere.group/news/20261117-rmal-argument-rarity/"
  - label: "Data (AIDE, Kaggle)"
    url: "https://www.kaggle.com/datasets/lburleigh/tla-lab-ai-detection-for-essays-aide-dataset"
citation: |
  @article{inoshita2026aroa,
    title   = {Argument Rarity as a Measure of Essay Originality in the Age of
               {AI}-Assisted Writing},
    author  = {Inoshita, Keito and Omura, Michiaki and Yamanaka, Tsukasa and
               Maeda, Go and Tsuji, Kentaro},
    journal = {Research Methods in Applied Linguistics},
    year    = {2026},
    note    = {Accepted, to appear}
  }
---

<div class="teaser">
<div>

Separate

AI のエッセイは **集団として** 均質。集団内の主張の多様性は学生の 0.32〜0.36 倍。1 本ずつの典型性は課題によっては学生と差がない。

</div>
<div>

Corpus

AI のエッセイを参照コーパスに混ぜると、主張の希少性の差は **d = 0.47 から 1.58** に広がる。参照コーパスが尺度の意味を決める。

</div>
<div>

Limits

根拠を捏造すると最終スコアは **+0.405**。希少性は、検証済みの独創性ではない。

</div>
</div>

## 品質では見分けられなくなった

LLM は、どんなテーマでも論理的で流暢な文章を数秒で書けるようになりました。その結果、提出されたエッセイが学生自身の考えなのか、AI が典型的なパターンを組み立て直したものなのかを、教員が見分けにくくなっています。AI の文章の品質が人に近づくと、**品質はもう、誰が書いたか・どれだけ考えたかの手がかりになりません**。

これまでの自動エッセイ採点（AES）は、論理の一貫性・文法・構成といった品質を予測することに力を注いできました。しかしエッセイ課題の目的は、良い文章を作ることそのものではなく、自分の視点を持ち、多様な根拠を探り、反論に答えるという批判的思考に学生を関わらせることです。どの主張を立て、どの根拠を選び、どう組み立てたかという、**論証の要素レベルの独創性**は、今の AES では測られていません。

人の採点者にも限界があります。大人数を短期間で採点すると、順序効果や疲労が入ります。さらに、ある主張が数百本のエッセイ全体の中でどれくらい珍しいかを判断するのは、人の作業記憶を超えています。

## AROA の仕組み

<figure>
  <img src="/column-images/rmal-argument-rarity/framework-1600.webp" alt="AROA framework" />
  <figcaption><strong>Figure 1.</strong> AROA の処理の流れ（原論文 Figure 1）。左で論証の要素を取り出し、中央で構造と意味の希少性、右上で対話的な展開を計算し、品質で調整して最終スコアにします。</figcaption>
</figure>

AROA（Argument Rarity-based Originality Assessment）は、**同じ課題を書いた学生エッセイの集まり（参照コーパス）と比べて、論証がどれくらい典型的でないか**を測ります。創造性研究では、独創性を「その回答が統計的にどれくらい少ないか」で測る伝統があり、AROA はそれを論証の要素に当てはめています。論文は、これが独創性のうち新規性の側面だけを表すもので、それ自体は検証済みの独創性ではないと明記しています。

処理は次のとおりです。

1. **論証の取り出し**：LLM（温度 0）がエッセイから 5 種類の要素を取り出します。

| 要素 | 内容 |
|---|---|
| 主張（Claims） | 中心となる結論や主張 |
| 理由（Reasons） | 主張を支える論拠 |
| 根拠（Evidence） | 理由を裏づける例・データ・引用 |
| 反論（Counterarguments） | 想定される反対意見 |
| 再反論（Rebuttals） | 反論への応答 |

2. **ベクトル化**：各要素を Sentence-BERT で、意味が近いものが近くに来る空間に置きます。
3. **4 つの下位スコア**：構造の希少性（要素の数や比率など 12 個の特徴がどれくらい珍しい組み合わせか）、主張の希少性と根拠の希少性（参照コーパスの中で最も近い 5 つとの平均類似度の補数）、対話的な展開（反論と再反論のやり取りの量と網羅度）です。自分自身や、AI 生成時に例として見せたエッセイは比較相手から除きます。
4. **品質ゲート**：LLM が一貫性と論理的妥当性を 3 段階で評価します。4 つの下位スコアを合成して参照コーパス内のパーセンタイルに直し、品質を掛けて最終スコアにします。**品質が下がって得点が上がることはない**設計です。

## 実験 1：AI のエッセイは学生より典型的か

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- 学生エッセイ：AIDE データセットの 2 課題（Car-free cities 686 本、Electoral College 668 本、計 1,354 本を採点）。どちらも資料を読んで立場を論じる課題
- AI エッセイ：GPT-4.1-mini で各課題 500 本、計 1,000 本を生成。プロンプトには課題文・資料・同じ課題の学生エッセイ 3 本を例として入れた
- 主たる設定：各課題の学生エッセイだけを参照コーパスにし、学生・AI の両方をそれに対して採点

</div>

<figure>
  <img src="/column-images/rmal-argument-rarity/student-vs-ai-1600.webp" alt="Student vs AI effect sizes" />
  <figcaption><strong>Figure 2.</strong> 学生と AI の差（Cohen's d、正の値は学生のほうが典型的でない）。課題によって向きや大きさが変わります。</figcaption>
</figure>

最もはっきりした差は品質で、AI は 0.998 とほぼ満点、学生は平均 0.609 でした。希少性の差はずっと小さく、課題に依存しました。

- AI の主張は Car-free cities では学生より典型的（d = 0.99）でしたが、Electoral College では差がありませんでした（d = −0.01、p = 0.79）。
- AI の根拠は、どちらの課題でも一貫して学生より典型的とは言えませんでした（d = −0.38 と 0.12）。
- 論証の構造は、両課題で AI のほうがやや典型的でした（d = 0.34 と 0.51）。
- 反論と再反論のやり取りを含むエッセイは、Car-free cities では AI 2.6%・学生 51.2%、Electoral College では AI 100%・学生 74.0% で、向きが逆でした。

品質ゲートは品質を掛けるので、AI の高い品質がそのまま最終スコアに入り、最終スコアは全体として AI のほうが高くなりました（d = −0.57）。**最終スコアは書き手を判定する指標ではない**ので、品質の分布が違う集団同士を比べるときは下位スコアと合わせて読む必要があります。

## 実験 2：集団としての均質さと、参照コーパスの影響

<p class="experiment-label">Experiment 2</p>

1 本ずつの差は小さい一方で、AI のエッセイ同士はとてもよく似ていました。それぞれの集団の中だけで（同じ 500 本の規模で）希少性を計算すると、AI の主張の希少性は学生の 0.32 倍と 0.36 倍、根拠は 0.58 倍と 0.64 倍でした。

<figure>
  <img src="/column-images/rmal-argument-rarity/homogeneity-1600.webp" alt="Within-population homogeneity" />
  <figcaption><strong>Figure 3.</strong> 集団内の希少性の、AI と学生の比（1 なら学生と同じ多様さ）。主の AI エッセイの主張は学生の約 3 分の 1 の多様さです。右の 2 組は実験 4 の生成条件（各 250 本）です。</figcaption>
</figure>

この均質さは、参照コーパスに AI のエッセイを混ぜると、1 本ずつの得点にも入り込みます。AI の主張は、ほかの AI の主張と近いためです。AI の主張とそれに最も近い 5 つの AI の主張との平均類似度は 0.961 と 0.966 で、学生同士の 0.884 と 0.909 より高くなっていました。

<figure>
  <img src="/column-images/rmal-argument-rarity/composition-1600.webp" alt="Reference-corpus composition" />
  <figcaption><strong>Figure 4.</strong> 参照コーパスの構成による学生と AI の差の変化。AI のエッセイを混ぜると、主張でも根拠でも差が大きく広がります。</figcaption>
</figure>

つまり、**AI 集団の均質さ**と、**学生集団に対する 1 本ずつの典型性**という 2 つの現象を、混合コーパスの希少性は区別できません。AI の支援を受けた提出物が多い集団で採点すると、それぞれが他の提出物の均質さの分まで減点されます。論文が学生だけの参照コーパスを主たる設定にしているのはこのためです。参照コーパスの構成・課題・版は、ノルム準拠のテストが標準化サンプルを報告するのと同じように、得点と一緒に報告すべきだとしています。

## 実験 3：新しいエッセイを安定して採点できるか

<p class="experiment-label">Experiment 3</p>

授業で使うなら、提出が増えるたびに過去の学生の得点が変わるのは困ります。そこで、学生エッセイを固定した参照用の半分と、採点対象の半分にランダムに 20 回分けて、固定した参照だけで採点しました。参照コーパスに入れたときの得点とほぼ一致し（最終スコアの平均 Spearman ρ = 0.99）、平均パーセンタイルも 0.49 と 0.50 で、ずれは見られませんでした。

<figure>
  <img src="/column-images/rmal-argument-rarity/reference-size-1600.webp" alt="Reference corpus size" />
  <figcaption><strong>Figure 5.</strong> 参照コーパスを小さくしたときの、最終スコアの順位の一致（同じ学生集団から取った大きなコーパスとの比較）。</figcaption>
</figure>

参照コーパスを 50 本まで減らしても順位の一致は 0.91 でした。ただし論文は、これは同じ学生集団の大きなコーパスとの一致であり、一般的な最小コーパス数として読まないよう注意しています。

ほかの頑健性も確かめています。

| 確認したこと | 結果 |
|---|---|
| 近傍数（3〜50） | 主張の順位は ρ ≥ 0.97。根拠の差は設定で符号が変わるため解釈しない |
| 合成の重み（ランダム 1,000 通り） | 等重みとの順位相関の中央値 0.91 |
| 別のエンコーダ（all-MiniLM-L6-v2） | 順位は保たれる（ρ = 0.91〜0.93）が、主張の差は d = 0.25 に縮む |
| 別の抽出モデル（Gemini、Claude） | 最終スコアの一致は中程度（平均 r = 0.34、品質を固定すると 0.56） |

## 実験 4：「珍しいことを書け」と指示すると

<p class="experiment-label">Experiment 4</p>

AI の典型性が「学生の例をまねる」プロンプトのせいかを確かめるため、3 つの生成条件を比べました。C0 は本実験と同じ模倣、C1 は典型的な議論を避けて珍しい視点と根拠を出すよう指示、C2 は 25 人分の学生ペルソナから 1 つを割り当てる条件です。

<figure>
  <img src="/column-images/rmal-argument-rarity/generation-strategy-1600.webp" alt="Generation strategy" />
  <figcaption><strong>Figure 6.</strong> 生成条件ごとの学生との差（負の値は AI のほうが典型的でない）。新規性を求める C1 では、1 本ずつは学生より珍しくなります。</figcaption>
</figure>

C0 は本実験の結果を再現しました。C1 では 1 本ずつのエッセイが学生より珍しくなり、とくに根拠で大きく差が出ました（d = −1.94）。それでも C1 の集団内の多様さは学生の 0.62 倍と 0.56 倍で、**少数の珍しい議論に集まる**形になっていました。

根拠が珍しいのは捏造のせいではないかも調べました。C1 の根拠のうち、資料にない具体的な事実の主張は 2.7%（学生は 30.0%）で、41.7% は一般論や仮定の例でした。この分類自体も LLM によるもので、事実の誤りではなく「出典のない具体性」を見たものです。

## 実験 5：希少性は独創性と言えるか

<p class="experiment-label">Experiment 5</p>

学生エッセイ 100 本に 4 種類の編集を加え、得点の変化を見ました。

<figure>
  <img src="/column-images/rmal-argument-rarity/perturbation-1600.webp" alt="Perturbation test" />
  <figcaption><strong>Figure 7.</strong> 編集による最終スコアの平均変化（Wilcoxon 符号順位検定、* p < .05、** p < .01、*** p < .001）。捏造した根拠に最も大きな加点が付きました。</figcaption>
</figure>

- **言い換え**：希少性はほとんど変わらず、意味に基づく尺度として狙いどおりでした。ただし LLM で書き直すと品質スコアが上がり（+0.243）、論証が変わっていないのに最終スコアが上がりました。
- **捏造した根拠**：根拠の希少性が +0.113 上がり、品質ゲートでも減点されず、最終スコアは +0.405 でした。
- **無関係な主張と、関連する珍しい議論**：どちらもわずかしか上がらず、両者を区別できませんでした。

ほかの検証も合わせると、次のように整理できます。

| 検証 | 結果 |
|---|---|
| 同じ論点の主張がいくつあるかを数えた判断との一致 | 主張の希少性が高いほど同等の主張は少ない（ρ = −0.32、p < .01） |
| 経験のある教員 1 人による 120 本の独創性評定 | 最終スコアと ρ = 0.33。主に対話的な展開（ρ = 0.38）によるもので、3 つの希少性には有意な関連なし |
| 同じ教員の再評定の安定性（3 か月以上後） | 独創性 ρ = 0.42、品質 ρ = 0.64 |

<figure>
  <img src="/column-images/rmal-argument-rarity/expert-1600.webp" alt="Expert ratings" />
  <figcaption><strong>Figure 8.</strong> 教員 1 人の独創性評定との順位相関。層内の値は、層別抽出による範囲の広がりを除いた控えめな推定です。</figcaption>
</figure>

教員の評定は、コーパス全体の中での珍しさよりも、1 本の中で読み取れる論証の展開に反応していました。論文はこれを、人が希少性を知覚できないことの証拠とはせず、評定の信頼性が限られた 1 人のデータでわかる範囲にとどめています。

## わかったこと・わかっていないこと

わかったことは次の 3 点です。

- AI のエッセイは、**1 本ずつよりも集団として**学生と大きく違う。学生集団に対する 1 本ずつの典型性は課題によっては差がないが、集団内の主張の多様性は学生の約 3 分の 1。
- 参照コーパスの構成が、希少性スコアの意味を決める。学生だけの固定した参照コーパスなら、新しいエッセイを安定して採点できる。
- 希少性は言い換えには左右されない一方、捏造した根拠に加点し、関連する珍しさと無関係な珍しさを区別できない。**希少性は有望な探索的尺度だが、検証済みの独創性の尺度ではない**。

限界も多く残っています。教員評価は 1 人で、評定者間の信頼性は測れていません。論証要素の抽出は独立した人手の注釈で検証しておらず、反論への再反論が中身として答えているかも確かめていません。品質スコアは LLM の判断で、関連性・事実の正確さ・資料の使い方は別に確認する必要があります。データは 1 つのデータセットの英語の 2 課題だけで、AI のエッセイも 1 つのモデルが生成したもので、学生が AI の支援を受けて書いた文章ではありません。

論文は、成績づけや書き手の判定には使わず、教員の確認と関連性・出典のチェックを組み合わせたうえで、「どの論証の動きが過去の学生と比べて最も型どおりか」を示すフィードバックとして使う方向を提案しています。

データ：学生エッセイは公開されている AIDE データセット（[Kaggle](https://www.kaggle.com/datasets/lburleigh/tla-lab-ai-detection-for-essays-aide-dataset)）から取っています。
