---
title: "Can an LLM Read Where Scientific Names Come From?"
subtitle: "Automated Labeling of Scientific Names and Etymological Trend Analysis in Phytophagous Arthropods Using Large Language Model"
date: "2026-11-27"
excerpt: "植物を食べる昆虫・ダニ 2,705 種の学名（種小名）の由来を、LLM で自動分類しました。形態・寄主・地名・人名は人手の分類とよく一致し、命名の長期的な傾向も再現できました。Zoological Science 掲載論文の解説です。"
readingMinutes: 10
showImage: false
image: "/column-images/zoolsci-scientific-names/pipeline.png"
imageAlt: "研究の流れ。Heard et al. (2023) のデータセットを 6 カテゴリに整理し、GPT-4o mini で分類して、人手の分類と比較する。"
authors:
  - name: "Kota Nojiri"
    affiliation: "The University of Tokyo"
  - name: "井下 敬翔"
    url: "/about/"
    affiliation: "関西大学"
  - name: "Haruto Sugeno"
    affiliation: "Fukushima University"
tldr: "学名の種小名には、形や色、寄主植物、見つかった場所、人の名前など、さまざまな由来があります。由来を調べるには原記載を読む必要があり、大規模な分析は手間がかかります。この研究では、植食性節足動物 2,705 種の種小名を GPT-4o mini で 6 カテゴリに自動分類し、人手の分類と比べました。形態・寄主・地名・人名では F1 が 75% 以上、正解率が 90% 前後で、Cohen の κ も 0.7 以上でした。一方、生態・行動とその他は F1 が 30% 台にとどまりました。年代ごとの傾向では、形態由来の名前が減り、地名と人名が増えるという、クモでの先行研究と同じ流れを LLM の分類でも確認できました。"
links:
  - label: "Paper (Zoological Science)"
    url: "https://doi.org/10.2108/zs250025"
citation: |
  @article{nojiri2025automated,
    title   = {Automated Labeling of Scientific Names and Etymological Trend
               Analysis in Phytophagous Arthropods Using Large Language Model},
    author  = {Nojiri, Kota and Inoshita, Keito and Sugeno, Haruto},
    journal = {Zoological Science},
    volume  = {42},
    number  = {5},
    year    = {2025},
    doi     = {10.2108/zs250025}
  }
---

<div class="teaser">
<div>

Accuracy

形態・寄主・地名・人名は **F1 75% 以上**。最も高いのは形態の 82.6%。

</div>
<div>

Agreement

同じ 4 カテゴリで Cohen の **κ は 0.70〜0.76**。生態・行動とその他は 0.3 前後。

</div>
<div>

Trends

形態由来が減り、**地名と人名が増える**流れを、人手と LLM の両方で確認。

</div>
</div>

## 学名の由来を調べるのはなぜ大変か

動物の学名は、属名と種小名（種の名前）の二つでできています。種小名をどう付けるかは、国際動物命名規約の最低限のルールを守れば著者に任されています。そのため由来は多様で、形や色、生息地、分布、人の名前、文化的な背景などから名付けられています。寄生性の動物や、特定の生物に強く依存する種では、寄主の名前が使われることもあります。

近年、学名には倫理的な議論も起きています。犯罪者や差別的な人物にちなんだ名前の問題や、人名由来の名前（エポニム）の約 9 割が男性を記念しているという偏りなどです。規約を見直すべきという意見と、学名の安定性を優先すべきという意見の両方が出ています。

こうした議論の土台になるのが、学名の由来の統計です。ただ、これまでの研究は文献を一つずつ読み、ランダムに抜き出したものを相互に確認するやり方で、大きな手間がかかっていました。節足動物の 8 割以上はまだ記載されていないという推定もあり、既存の学名の分析に人手をかけすぎることは現実的ではありません。

先行研究（Inoshita et al., 2025）では、クモの種小名の由来を LLM が人手と同程度に分類できることを示しました。ただしクモという一つのグループだけの結果でした。そこでこの研究では、**分類群が異なり、カテゴリに「寄主」が加わる植食性節足動物でも同じことができるか**を確かめ、あわせて命名の時代的な傾向を調べました。

## 方法

<figure>
  <img src="/column-images/zoolsci-scientific-names/pipeline-1600.webp" alt="Study pipeline" />
  <figcaption><strong>Figure 1.</strong> 研究の流れ。公開データセットのカテゴリを 6 つに整理し、GPT-4o mini で自動分類して、人手の分類と比較しました。</figcaption>
</figure>

データには、Heard et al. (2023) が公開した植食性節足動物の語源データセットを使いました。寄主適応による分化（host-associated differentiation）の研究によく使われる 30 種と、それぞれの属の種を合わせた 2,709 種です。記載年がない 4 種を除き、2,705 種を分析しました。

元のデータは 7 カテゴリで分類されています。先行研究とそろえるため、次のように 6 カテゴリへ整理しました。

| 元のカテゴリ | この研究のカテゴリ | 内容 |
|---|---|---|
| Morphology | Morphology（形態） | 大きさ・形・色など形態の特徴 |
| Host | Host（寄主） | 寄主となる生物 |
| Place | Geography（地理） | 分布や発見された場所 |
| Behavior, Habitat | Ecology & Behavior（生態・行動） | 生息環境や行動の特徴 |
| Person | People（人名） | 研究者などの人物への献名 |
| Other | Other（その他） | 上のどれにも当てはまらないもの |

LLM には OpenAI の API 経由で GPT-4o mini を使いました。プロンプトは先行研究のものをもとに、この対象に合わせた few-shot の例を加えています。人手の分類（元データのラベル）を正解として、カテゴリごとの正解率・適合率・再現率・F1、Cohen の κ、年ごとの件数の誤差（MAE）を計算しました。時代的な傾向は、一般化加法モデル（GAM）で分析しています。GAM は直線でない緩やかな変化をとらえられるため、命名の流行の分析に向いています。

## 実験 1：カテゴリごとにどれだけ当たるか

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- 対象：植食性節足動物 2,705 種の種小名
- 正解：Heard et al. (2023) の人手ラベル（6 カテゴリに整理したもの）
- 指標：カテゴリごとの正解率・適合率・再現率・F1

</div>

<figure>
  <img src="/column-images/zoolsci-scientific-names/prf1-1600.webp" alt="Precision, recall and F1 by category" />
  <figcaption><strong>Figure 2.</strong> カテゴリごとの適合率・再現率・F1。点線は 75%。形態・寄主・地名・人名は F1 が 75% を超え、生態・行動とその他は 30% 台です。</figcaption>
</figure>

F1 は形態 82.6%、人名 80.0%、寄主 76.4%、地名 75.8% で、この 4 カテゴリは適合率と再現率の釣り合いもとれていました。寄主は適合率 89.1% に対して再現率 66.9% で、LLM が寄主由来と判断したものはよく当たる一方、人手が寄主としたものの一部を別のカテゴリに入れていたことになります。

生態・行動（F1 31.7%）とその他（38.3%）は低い値でした。先行研究のクモでも、生態・行動と文化のカテゴリで精度が低く、同じ傾向です。論文では、生態・行動に関するデータが十分でなく、深い文脈の意味をモデルがとらえにくいことが原因の一つと考えています。

<figure>
  <img src="/column-images/zoolsci-scientific-names/accuracy-vs-f1-1600.webp" alt="Accuracy versus F1 by category" />
  <figcaption><strong>Figure 3.</strong> カテゴリごとの正解率（四角）と F1（丸）。生態・行動は正解率が 94.5% と最も高いのに、F1 は 31.7% です。</figcaption>
</figure>

正解率だけを見ると、どのカテゴリも 85% 以上です。生態・行動は 94.5% で、むしろ最も高い値でした。これは、そのカテゴリに当たらない種が大半を占めるため、「当てはまらない」と答えるだけで正解率が上がるためです。正しく拾えているかを見るには、F1 を合わせて見る必要があります。

## 実験 2：人手とどれだけ一致するか

<p class="experiment-label">Experiment 2</p>

偶然の一致を差し引いた一致度として、Cohen の κ をカテゴリごとに計算しました。

<figure>
  <img src="/column-images/zoolsci-scientific-names/kappa-1600.webp" alt="Cohen's kappa by category" />
  <figcaption><strong>Figure 4.</strong> カテゴリごとの Cohen の κ。点線は、論文で許容できる一致とした 0.4 です。</figcaption>
</figure>

人名 0.758、形態 0.738、地名 0.724、寄主 0.703 で、4 カテゴリとも 0.7 を超える一致でした。一方、生態・行動は 0.286、その他は 0.299 で、低い一致にとどまりました。年ごとの件数の誤差（MAE）は、どのカテゴリでも 1 未満でした。

主要なカテゴリでは LLM が人手の分類をよく再現できる一方、定義があいまいなカテゴリや、さまざまなものが混ざるカテゴリには限界がある、という結果です。

## 実験 3：カテゴリの件数は人手と同じになるか

<p class="experiment-label">Experiment 3</p>

<figure>
  <img src="/column-images/zoolsci-scientific-names/counts-1600.webp" alt="Species counts by category" />
  <figcaption><strong>Figure 5.</strong> 本文に件数が記載されている 3 カテゴリについて、人手と LLM が分類した種数。</figcaption>
</figure>

全体として、各カテゴリに入る種数は人手と LLM でよく似ていました。人手の分類で多かったのは形態（894 種）、寄主（646 種）、人名（534 種）で、LLM でも形態（940 種）、寄主（486 種）、人名（534 種）が多くなりました。寄主は LLM の方が少なく、実験 1 で見た再現率の低さと対応しています。

## 実験 4：命名の傾向は時代とともにどう変わったか

<p class="experiment-label">Experiment 4</p>

各カテゴリの割合の時間変化を GAM で推定しました。人手と LLM の分類を一つのモデルに入れて、両者の曲線を比べています。分散の比は人手のモデルで 0.25、LLM のモデルで 0.24 で、過分散は見られませんでした。

| カテゴリ | 人手の分類 | LLM の分類 |
|---|---|---|
| 形態 | 減少。1900 年ごろに傾向が変わる | 減少。1900 年ごろの変化は曲線に現れない |
| 寄主 | 減少 | 減少（減り方の速さは人手と異なる） |
| 地名 | 増加 | 増加（人手とほぼ同じ曲線） |
| 人名 | 増加 | 増加（人手とほぼ同じ曲線） |
| 生態・行動、その他 | 両者で異なるパターン | 両者で異なるパターン |

形態由来の名前が減り、地名と人名が増えるという流れは、クモやワムシでの先行研究とも一致しました。分類群をまたいだ一般的な傾向である可能性があります。

一方で、人手の分類では形態が 1900 年ごろを境に急に減っていますが、LLM の曲線ではこの変化が見えませんでした。**長期的な傾向を見るには LLM の分類で足りるが、細かな変化は見落とすことがある**、というのが論文の結論です。

論文では、1900 年ごろの形態由来の急減について、メンデルの法則の再発見や電子顕微鏡などの技術の発達によって、分類の記載が遺伝学や微細構造の視点に移ったことが関係しているかもしれないと考察しています。ただし、これは解釈の一つで、個々の種の語源をさらに調べる必要があるとしています。

## わかったこと・わかっていないこと

この研究でわかったのは次の 3 点です。

- 植食性節足動物でも、形態・寄主・地名・人名の 4 カテゴリでは、LLM の分類が人手の分類とよく一致した（F1 75% 以上、κ 0.7 以上）。クモ以外の節足動物にも適用できる。
- LLM の分類で、形態由来が減り地名・人名が増えるという長期的な傾向を再現できた。分類は 1 時間ほどで終わった。
- 寄主由来の名前が減っていることもわかった。寄主由来の名前を持つ種は寄主適応の研究対象に選ばれやすいという先行研究があり、命名のしかたが研究の注目度に影響している可能性がある。

一方で、限界もあります。生態・行動とその他のカテゴリは精度が低く、まだ人手の確認が必要です。論文では、このカテゴリだけを重点的に人手で確認すれば、全体の手間は減らせるとしています。また、形態の 1900 年ごろの変化のような細かな傾向は LLM の分類では見落とされました。ほかの分類群でもさらに評価する必要があります。
