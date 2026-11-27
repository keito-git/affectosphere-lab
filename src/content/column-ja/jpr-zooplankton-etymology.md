---
title: "Can an LLM Match Taxonomists in Classifying Zooplankton Names?"
subtitle: "Applying large language models to expert-based etymological classification in zooplankton"
date: "2026-11-27"
excerpt: "ワムシと微小甲殻類 989 種の種小名の由来を、専門家の分類と LLM の分類で比べました。全体の正解率は 0.84、κ は 0.74 で、形態と人名はよく一致した一方、文化のカテゴリには大きな過剰分類がありました。Journal of Plankton Research 掲載論文の解説です。"
readingMinutes: 9
showImage: false
image: "/column-images/jpr-zooplankton-etymology/pipeline.png"
imageAlt: "研究の流れ。専門家がラベルを付けた動物プランクトンの種小名を GPT-4o-mini で分類し、一致度と長期の傾向を比べる。"
authors:
  - name: "Haruto Sugeno"
    affiliation: "Fukushima University"
  - name: "井下 敬翔"
    url: "/about/"
    affiliation: "関西大学"
  - name: "Kota Nojiri"
    affiliation: "The University of Tokyo"
tldr: "学名の語源の研究は、分類学者が原記載を読んで判断する手間のかかる作業です。この研究では、専門家が語源を分類した動物プランクトン（ワムシと微小甲殻類）989 種のデータを使い、GPT-4o-mini による自動分類がどこまで専門家に一致するかを調べました。全体の正解率は 0.84、Cohen の κ は 0.74 でした。F1 は形態 0.92、人名 0.91、地理 0.83 と高く、生態・行動は 0.62、文化は 0.20 でした。文化では、LLM が文化と判定した名前の多くが専門家の分類では別のカテゴリでした。年ごと・10 年ごとの件数の長期傾向は GAM でほぼ再現でき、両者に有意な差が出たのは文化の年単位の比較（P = 0.04）だけでした。"
links:
  - label: "Paper (Journal of Plankton Research)"
    url: "https://doi.org/10.1093/plankt/fbag061"
citation: |
  @article{sugeno2026applying,
    title   = {Applying large language models to expert-based etymological
               classification in zooplankton},
    author  = {Sugeno, Haruto and Inoshita, Keito and Nojiri, Kota},
    journal = {Journal of Plankton Research},
    volume  = {48},
    number  = {5},
    pages   = {fbag061},
    year    = {2026},
    doi     = {10.1093/plankt/fbag061}
  }
---

<div class="teaser">
<div>

Agreement

全体の正解率は **0.84**、Cohen の κ は **0.74**。989 種の分類は 14 分で終わった。

</div>
<div>

Strong

形態（F1 **0.92**）と人名（**0.91**）は適合率 0.97 で、専門家の判断とよく一致。

</div>
<div>

Weak

文化は F1 **0.20**。適合率が 0.12 で、LLM が文化と判定しすぎる。

</div>
</div>

## 専門家の語源分類を LLM で置き換えられるか

学名の種小名には、形態、生態や行動、分布、人名、文化などさまざまな由来があります。由来の分析は、命名の歴史や、人名由来の名前の性別の偏りといった議論の基礎になります。しかし語源を確かめるには原記載を読む必要があり、記載が古かったり、語源の説明がなかったりすると判断が難しくなります。

動物プランクトンは、古い原記載を持つ種が多い一方で、今も新種の記載が続いているグループです。長期の命名の傾向を調べるのに向いていますが、語源の判定は特に難しい対象でもあります。

この研究で使った Macêdo et al. (2023) のデータセットは、ワムシと微小甲殻類の種小名に**分類学の専門家が語源のラベルを付けた**ものです。専門家のラベルを基準にできるため、LLM による自動分類の精度と偏りを確かめるのに適しています。これまで LLM による語源の自動分類は一部の節足動物で試されていましたが、ここでは専門家の判断とどこが合い、どこがずれるかを細かく調べました。

## 方法

<figure>
  <img src="/column-images/jpr-zooplankton-etymology/pipeline-1600.webp" alt="Study pipeline" />
  <figcaption><strong>Figure 1.</strong> 研究の流れ。専門家のラベルを基準に、LLM の分類の一致度と、長期の命名傾向の再現性を調べました。</figcaption>
</figure>

データは、1758 年から 2021 年に記載された動物プランクトンの公開データセット（Macêdo et al., 2023）です。記載年がわかった 989 種を分析しました。

LLM には OpenAI の API 経由で GPT-4o-mini を使い、temperature を 0 にして、few-shot の例を含むプロンプトで 5 つのカテゴリ（形態、生態・行動、地理、人名、文化）に分類させました。

専門家のラベルを基準に混同行列をつくり、正解率、Cohen の κ、カテゴリごとの適合率・再現率・F1 を計算しました。さらにカイ二乗検定の標準化残差（|r| > 2 を目安）で、どのカテゴリの組み合わせで偏りが出るかを調べました。長期の傾向は、年ごと・10 年ごとの件数に準ポアソン分布の GAM を当てはめ、専門家と LLM の曲線を比べています。

## 実験 1：全体としてどれだけ一致するか

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- 対象：ワムシと微小甲殻類 989 種の種小名
- 基準：Macêdo et al. (2023) の専門家ラベル（5 カテゴリ）
- 指標：正解率、Cohen の κ、カテゴリごとの適合率・再現率・F1

</div>

全体の正解率は 0.84、Cohen の κ は 0.74 で、論文では「かなりの一致（substantial）」と評価しています。989 種すべての分類にかかった時間は 14 分で、1 種あたり平均 0.85 秒でした。

<figure>
  <img src="/column-images/jpr-zooplankton-etymology/prf1-1600.webp" alt="Precision, recall and F1 by category" />
  <figcaption><strong>Figure 2.</strong> カテゴリごとの適合率・再現率・F1（論文の Table I）。形態と人名が高く、文化が最も低くなりました。</figcaption>
</figure>

| カテゴリ | 再現率 | 適合率 | F1 |
|---|---|---|---|
| 形態（Morphology） | 0.87 | 0.97 | 0.92 |
| 生態・行動（Ecology & Behavior） | 0.52 | 0.75 | 0.62 |
| 地理（Geography） | 0.91 | 0.76 | 0.83 |
| 人名（People） | 0.86 | 0.97 | 0.91 |
| 文化（Culture） | 0.64 | 0.12 | 0.20 |

F1 は 0.20 から 0.92 まで、カテゴリによって大きく違いました。形態と人名は F1 が 0.9 を超え、地理も 0.83 と高い値です。生態・行動は 0.62 で中程度、文化は 0.20 でした。

## 実験 2：どこでずれるのか

<p class="experiment-label">Experiment 2</p>

適合率と再現率を分けて見ると、ずれ方の違いがわかります。

<figure>
  <img src="/column-images/jpr-zooplankton-etymology/precision-recall-1600.webp" alt="Precision versus recall by category" />
  <figcaption><strong>Figure 3.</strong> カテゴリごとの再現率（横軸）と適合率（縦軸）。形態と人名はほぼ同じ位置（右上）に重なっています。文化だけが大きく離れています。</figcaption>
</figure>

- **形態と人名**：適合率 0.97 で、LLM がこれらと判定したものはほとんど正しい。再現率も 0.86〜0.87 です。
- **地理**：再現率 0.91 に対して適合率 0.76 で、地理と判定する範囲がやや広めです。
- **生態・行動**：適合率 0.75 に対して再現率 0.52 で、専門家が生態・行動とした名前の半分近くを別のカテゴリに入れています。
- **文化**：適合率が 0.12 しかありません。LLM が文化と判定した名前の多くは、専門家の分類では別のカテゴリでした。

カイ二乗検定の標準化残差でも、対角成分（正しく一致した組み合わせ）で最も強い正の残差が出たのは形態と人名で、文化では対角以外の残差が比較的大きくなっていました。文化に関する名前の判断で、LLM と専門家の違いが最も大きくなっていました。

## 実験 3：命名の長期傾向は再現できるか

<p class="experiment-label">Experiment 3</p>

各カテゴリの件数の時間変化を、年単位と 10 年単位の GAM で専門家と LLM について推定し、両者の曲線に差があるかを検定しました。

| カテゴリ | 10 年単位 | 年単位 |
|---|---|---|
| 形態 | P = NA | P = NA |
| 生態・行動 | P = NA | P = NA |
| 地理 | P = NA | P = NA |
| 人名 | P = NA | P = NA |
| 文化 | P = 0.40 | **P = 0.04** |

論文の Table II では、文化以外の 4 カテゴリの P 値は NA と記載されています。**専門家と LLM の間で有意な差が出たのは、文化の年単位の比較だけ**です。長期の命名の傾向は LLM の分類でもほぼ再現でき、ずれは文化に関する名前に限られていました。

## 実験 4：ほかの分類群と比べると

<p class="experiment-label">Experiment 4</p>

同じ枠組みを植食性節足動物に使った私たちの先行研究（Zoological Science, 2025）と、共通する 4 カテゴリの F1 を並べました。

<figure>
  <img src="/column-images/jpr-zooplankton-etymology/cross-taxa-f1-1600.webp" alt="F1 across two taxa" />
  <figcaption><strong>Figure 4.</strong> 共通する 4 カテゴリの F1。灰色は植食性節足動物（Zoological Science 論文の Table 1）、金色は今回の動物プランクトン（Table I）。データセットとカテゴリの定義が同じではないため、目安としての比較です。</figcaption>
</figure>

どちらの分類群でも、形態・地理・人名は高く、生態・行動が最も低いという順序は共通していました。今回は専門家がラベルを付けたデータで、全体に値が高くなっています。ただし、データセット、カテゴリの細かな定義、LLM に与えた例が異なるため、数値の差をそのまま精度の差とは読めません。

## わかったこと・わかっていないこと

この研究でわかったのは次の 3 点です。

- 専門家が語源を付けた動物プランクトン 989 種で、LLM の分類は全体の正解率 0.84、κ 0.74 と、かなりの一致を示した。
- 形態と人名は特に高い一致（F1 0.92 と 0.91）を示した一方、文化は F1 0.20 で、LLM が文化と判定しすぎる偏りがあった。
- 年単位・10 年単位の長期傾向はほぼ再現でき、有意な差は文化の年単位だけだった。

一方で、限界もあります。文化に関する名前の判断は、LLM と専門家で大きく違いました。生態・行動も再現率が 0.52 にとどまっています。論文では、LLM のラベルは専門家の判断を置き換えるものではなく、人が確認しながら使う（human-in-the-loop）補助的な道具として、大規模なデータの分析に役立てることを勧めています。
