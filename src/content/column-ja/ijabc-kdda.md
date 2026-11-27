---
title: "Can an LLM Generate Usable Emotion Data from 20 Example Sentences per Class?"
subtitle: "KDDA: A Knowledge-Driven Domain and Diversity Alignment Framework for Emotion Data Generation with Large Language Models"
date: "2026-11-27"
excerpt: "実データを学習に使わず、クラスごと 20 文から取り出した文体の統計だけを手がかりに、LLM で感情データを生成する枠組み KDDA を提案しました。International Journal of Activity and Behavior Computing 掲載論文の解説です。"
readingMinutes: 11
showImage: false
image: "/column-images/ijabc-kdda/overview.png"
imageAlt: "KDDA の全体図。人の事前知識からドメインプロファイルを作り、LLM の生成、Jaccard フィルタ、NLL による選択を経て合成データを積み上げる。"
authors:
  - name: "井下 敬翔"
    url: "/about/"
    affiliation: "関西大学"
  - name: "Hayato Tomisu"
  - name: "Xiaokang Zhou"
  - name: "Akira Kawai"
  - name: "Katsutoshi Yada"
tldr: "感情データは集めにくいデータです。KDDA は、クラスごとに 20 文だけを「ドメイン知識」として使い、文の長さ・読点の数・話題などの統計分布（ドメインプロファイル）に変えます。LLM はこの分布に沿って候補文を 6 本ずつ書き、似すぎた文を Jaccard 類似度で落とし、分布との NLL で 1 本を選びます。生成データだけで学習した DistilBERT は、IMDb で正解率 0.826、Emotions で 0.405 となり、比較した 4 手法を上回りました。Yelp では AGOS と同じ 0.872 でした。"
citation: |
  @article{inoshita2026kdda,
    title   = {{KDDA}: A Knowledge-Driven Domain and Diversity Alignment Framework
               for Emotion Data Generation with Large Language Models},
    author  = {Inoshita, Keito and Tomisu, Hayato and Zhou, Xiaokang and
               Kawai, Akira and Yada, Katsutoshi},
    journal = {International Journal of Activity and Behavior Computing},
    volume  = {1},
    pages   = {1--24},
    year    = {2026}
  }
---

<div class="teaser">
<div>

Profile

使う実データは **クラスごと 20 文** だけ。文の中身ではなく、長さや読点などの統計だけを取り出す。

</div>
<div>

Select

候補 6 本から、**似すぎた文を落とし**、ドメインの分布に最も合う 1 本を選ぶ。

</div>
<div>

Train

生成データだけで学習した分類器が、IMDb で 0.826、Emotions で 0.405。比較した 4 手法を上回る。

</div>
</div>

## 感情データはなぜ足りないのか

感情認識のモデルは、人がラベルを付けたデータに強く依存しています。ところが感情のデータは、他の言語データより集めるのが難しいデータです。職場・医療・教育の場面では、参加者の心理的な負担や利用目的の説明が厳しく問われます。子どもや高齢者が対象なら、倫理審査もさらに厳しくなります。その結果、手に入る感情データは、ツイートや商品レビューのような公開の場に偏りがちです。

この研究では、**実データを学習にも生成にも直接使わずに**、感情データを作れないかを考えました。ただし人の知識を完全に捨てるわけではありません。「この場面ではこういう書き方が多い」という対象ドメインについての知識は使います。その知識を手がかりに、LLM にそれらしい感情文を書かせます。

LLM に感情ラベルだけを渡して大量に書かせると、二つの問題が出ます。似た文ばかりになること（多様性の不足）と、対象ドメインの書き方からずれること（ドメインの不一致）です。KDDA はこの二つを同時に抑えるための枠組みです。

## KDDA の仕組み

<figure>
  <img src="/column-images/ijabc-kdda/overview-1600.webp" alt="KDDA framework overview" />
  <figcaption><strong>Figure 1.</strong> KDDA の全体図（論文の図）。左がドメインプロファイルの構築、中央が生成と多様性の拡張、右が NLL によるドメイン整合の評価です。</figcaption>
</figure>

KDDA は 3 つの段階で動きます。

1. **ドメインプロファイルの構築**：対象ドメインの代表的な文を、感情クラスごとに 20 文用意します。ルールベースの解析で、文の長さ・読点の数・節の種類・文頭の語の種類・話題・感情形容詞が明示されているかなど、10 種類の特徴を数えます。これをクラスごとの確率分布 P_e にまとめたものがドメインプロファイルです。LLM はこの段階では使いません。
2. **生成と多様性の拡張**：P_e から特徴の組（例：「19〜26 語、読点 1 つ、話題は仕事」）をサンプリングし、自然文の指示に変えてプロンプトに入れます。すでに採用した文や避けたい文を「負例」としてプロンプトに入れ、それと違う文を書くよう指示します。LLM は 1 回に 6 本の候補を書きます。候補は、既存の合成データとの単語 Jaccard 類似度が 0.62 以上、bigram の Jaccard 類似度が 0.40 以上なら、重複とみなして捨てます。
3. **NLL による選択**：残った候補について、文単体が P_e にどれだけ合うか（局所 NLL）と、その文を加えたときにデータ全体の特徴分布が P_e にどれだけ近づくか（大域 NLL）を計算します。大域 NLL、局所 NLL、多様性スコアの順に比べて 1 本を選び、合成データに加えます。

LLM のパラメータは変えません。制御はプロンプトと、統計にもとづく選択だけで行っています。

## 実験の設定

<div class="setup">

**Setup**

- 実データ（Golden）：IMDb（映画レビュー、肯定・否定）、Yelp（店舗レビュー、肯定・否定）、Emotions（Twitter、joy / anger / sadness / love / surprise / fear の 6 クラス）
- ドメイン知識：各データからクラスごとに 20 文を無作為に取り出し、特徴の抽出だけに使用（学習・テストからは除外）
- 生成量：2 クラスのデータはクラスごと 2,500 文（計 5,000 文）、Emotions はクラスごと 1,000 文（計 6,000 文）。比較手法も同数
- LLM：GPT-4.1-mini-2025-04-14（既定パラメータ）
- 比較手法：LOZP（ラベルだけのゼロショット）、CAZP（「肯定的な文を書け」型の指示）、AGOS（ペルソナなどの属性つき生成）、ARISE（ルール誘導と自己学習による合成データ生成）
- テスト：重複のない実データ 2,000 文。3 つの乱数シードの平均

</div>

分布の評価には 4 つの指標を使いました。どれも all-MiniLM-L6-v2 の文埋め込みで計算し、**実データ（Golden）の値に近いほど良い**と読みます。

| 指標 | 何を見るか |
|---|---|
| MCD（Mean Cosine Distance） | 文どうしの平均コサイン距離。大きいほど表現が多様 |
| CE（Cluster Entropy） | 埋め込み空間のクラスタへの散らばりの均一さ |
| FID（Fréchet Inception Distance） | 生成データと実データの分布の距離。Golden は 0 |
| CD（Centroid Distance） | クラスごとの重心どうしの距離。クラスの分かれ方 |

## 実験 1：生成データは実データに似ているか

<p class="experiment-label">Experiment 1</p>

<figure>
  <img src="/column-images/ijabc-kdda/distance-to-golden-1600.webp" alt="Distance to Golden for four distribution metrics" />
  <figcaption><strong>Figure 2.</strong> 各指標の値と Golden（実データ）との差の絶対値。短いほど実データに近く、枠線つきがそのセルで最も近い手法です。金色が KDDA です。</figcaption>
</figure>

MCD は 3 データすべてで KDDA が Golden に最も近くなりました。Yelp では差 0.040、Emotions では差 0.086 で、実データに近い多様さを保っています。FID は IMDb と Emotions で KDDA が最も近く、Yelp では AGOS（0.477）が KDDA（0.483）をわずかに上回りました。CD は Yelp と Emotions で KDDA が最も近く、IMDb では ARISE が最も近くなっています。

CE は KDDA の弱いところです。Yelp と Emotions では CAZP が最も近く、KDDA の値は Golden よりやや低くなりました。

差が大きく出たのは 6 クラスの Emotions です。FID は KDDA が 0.388 で、次に良い AGOS の 0.477 より小さく、CD も KDDA の 0.292 に対し、比較手法で最も近いのは AGOS の 0.477 でした。一方、ARISE は Emotions で FID 0.657、CD 0.768 と離れており、論文はこれを多クラスでの不安定さと見ています。

論文は全体として「12 指標中 9 で KDDA が Golden に最も近い」と述べています。なお、表の太字を数えると KDDA は 8 セル（IMDb の MCD・CE・FID、Yelp の MCD・CD、Emotions の MCD・FID・CD）です。

## 実験 2：生成データだけで分類器を学習する

<p class="experiment-label">Experiment 2</p>

各手法の生成データだけで DistilBERT を学習し、実データ 2,000 文で評価しました（IMDb と Yelp は 3 エポック、Emotions は 5 エポック、バッチサイズ 128）。Golden は同じ数の実データで学習した場合で、上限の目安です。

<figure>
  <img src="/column-images/ijabc-kdda/classification-1600.webp" alt="Classification accuracy on real test data" />
  <figcaption><strong>Figure 3.</strong> 生成データだけで学習した DistilBERT の正解率（3 シードの平均と標準偏差）。点線は同数の実データで学習した Golden です。</figcaption>
</figure>

| データ | Golden | LOZP | CAZP | AGOS | ARISE | KDDA |
|---|---|---|---|---|---|---|
| IMDb（F1） | 0.863 | 0.692 | 0.799 | 0.808 | 0.811 | **0.824** |
| Yelp（F1） | 0.889 | 0.802 | 0.771 | 0.872 | 0.849 | **0.872** |
| Emotions（F1） | 0.460 | 0.193 | 0.358 | 0.283 | 0.269 | **0.386** |

IMDb では KDDA が正解率 0.826、F1 0.824 で、比較手法をすべて上回りました。Yelp では AGOS と同じ正解率 0.872 で、差はありません。Emotions は 6 クラスの境界が重なるため全手法で値が下がりますが、KDDA は正解率 0.405 で、比較手法で最も高い CAZP の 0.371 を上回りました。ARISE は Emotions で標準偏差 0.124 と、シードによって結果が大きく揺れています。

Golden との差は、IMDb で 0.037、Emotions で 0.054 残っています。生成データだけで実データと同じ水準に届いたわけではありません。

## 実験 3：どの感情で間違えるか

<p class="experiment-label">Experiment 3</p>

<figure>
  <img src="/column-images/ijabc-kdda/confusion-matrices-1600.webp" alt="Confusion matrices on the Emotions dataset" />
  <figcaption><strong>Figure 4.</strong> Emotions データでの混同行列（論文の図）。行が正解、列が予測です。(a) が実データで学習した Golden、(f) が KDDA です。</figcaption>
</figure>

LOZP と AGOS は、予測が fear に偏っています。どの正解クラスでも fear 列の値が大きく、生成データが一部の表現に集中した結果と考えられます。KDDA の行列は対角が比較的はっきりしており、joy は 116 件、anger は 107 件を正しく当てて、6 手法の中でこの 2 クラスの正解数が最も多くなりました。

苦手なのは fear と sadness です。sadness は 77 件が anger と予測され、fear も anger と sadness に散らばっています。ただし、実データで学習した Golden でも fear の 68 件が sadness と予測されています。論文は、この混同は生成の仕組みよりも、否定的な感情どうしの意味の重なりから来ていると解釈しています。

## 実験 4：埋め込み空間での分布

<p class="experiment-label">Experiment 4</p>

Emotions の生成データを 384 次元の埋め込みにし、独立成分分析（ICA）で 2 次元に落としました。楕円は実データの各クラスの平均 ± 2 標準偏差で、実データがあるはずの範囲を表しています。

<figure>
  <img src="/column-images/ijabc-kdda/feature-distribution-1600.webp" alt="ICA projection of real and synthetic embeddings" />
  <figcaption><strong>Figure 5.</strong> 生成データ（点）と実データの範囲（楕円）の比較（論文の図）。色は感情クラスです。(e) が KDDA です。</figcaption>
</figure>

LOZP は感情ごとにはっきりしたまとまりを作りますが、その中心が実データの楕円から大きく外れています。ARISE もまとまりは明確ですが、実データの範囲を覆いきれていません。AGOS は広く散らばり、半分ほどの点しか楕円に入っていません。KDDA の点は楕円の中に集まり、外れる点も少なくなりました。

## 実験 5：どの部品が効いているか

<p class="experiment-label">Experiment 5</p>

Emotions で、KDDA の部品を一つずつ外しました。

<figure>
  <img src="/column-images/ijabc-kdda/ablation-1600.webp" alt="Ablation study on Emotions" />
  <figcaption><strong>Figure 6.</strong> 部品を外したときの、Golden との差の絶対値（Emotions）。金色が完全版です。</figcaption>
</figure>

完全版は MCD・FID・CD で Golden に最も近くなりました。CE だけは完全版が最も離れています（差 0.102）。論文はこれを、散らばりすぎではなく、クラスタの中がほどよくまとまっている結果と説明しています。

部品ごとに見ると、役割が分かれています。

- **ドメインプロファイル**を外すと、FID が 0.604、CD が 0.498 と最も大きくずれました。分布を実データに合わせる中心の部品です。
- **負例**を外すと、MCD が 0.542 まで下がり（Golden は 0.804）、似た文の繰り返しが増えました。
- **Jaccard フィルタ**を外しても多様性が下がりました。
- **NLL フィルタ**を外すと、FID と CD が中程度にずれました。論文はこれを、全体の整合を微調整する安定化の役割と見ています。

## わかったこと・わかっていないこと

この研究でわかったのは次の点です。

- クラスごと 20 文から取り出した文体の統計だけを手がかりにしても、LLM の生成を対象ドメインに寄せられる。生成データだけで学習した分類器は、比較した 4 手法を IMDb と Emotions で上回り、Yelp では AGOS と同等だった。
- 分布を合わせる役はドメインプロファイルが、多様性を広げる役は負例と Jaccard フィルタが担っていた。
- 多クラスの Emotions で差が大きく、FID 0.388 と実データの分布に最も近かった。

限界もあります。

- ドメインプロファイルは人の事前知識に依存します。今回は 20 文を使いましたが、知識の形や量で結果が変わる可能性があり、知識に含まれる文化的・言語的な偏りが生成データに移るおそれもあります。
- 実データで学習した場合との差は残っています。どれだけの合成データで実環境に十分汎化するかは、まだわかっていません。
- 評価は英語の 3 データ、比較的少ない感情クラス、GPT 系の LLM に限られています。より細かい感情分類や他言語では、sadness と anger のような意味の近い感情の区別がさらに難しくなる可能性があります。

今後は、記述的なガイドラインなど 20 文以外の形のドメイン知識を試すこと、多言語への拡張、より細かい感情分類での評価に取り組みます。
