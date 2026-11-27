---
title: "Can Layered Personas Make LLM-Generated Emotion Text Closer to Real Data?"
subtitle: "Persona-Based Synthetic Data Generation Using Multi-Stage Conditioning with Large Language Models for Emotion Recognition"
date: "2026-11-27"
excerpt: "年齢や職業から生活背景、場面、文体へと段階的にペルソナを組み立て、LLM に感情テキストを書かせる PersonaGen を提案しました。実データとの分布の近さでは既存の作り方を上回りましたが、実データの代わりにはまだなりません。International Journal of Activity and Behavior Computing 掲載論文の解説です。"
readingMinutes: 10
showImage: false
image: "/column-images/ijabc-persona-synthetic-data/framework.png"
imageAlt: "PersonaGen の全体図。基本属性、社会文化的背景、場面と文体の 3 段階でペルソナを組み立て、最後に LLM へ感情テキストの生成を指示する。"
authors:
  - name: "井下 敬翔"
    url: "/about/"
    affiliation: "関西大学"
  - name: "Rushia Harada"
    affiliation: "Almondays Co., Ltd."
tldr: "感情データは主観的で、集めるのに倫理上・実務上の制約があります。PersonaGen は、基本属性 → 社会文化的背景 → 場面と文体の順にペルソナを積み上げ、各段で LLM による整合性チェックをかけてから、GPT-4.1-mini に感情テキストを書かせます。生成した 3,500 文は感情ごとに LightGBM で F1 0.80 で分類でき、GPT-4o による自然さの評価も高めでした。実ツイートとの比較では PRD-Fβ・KL・ヒストグラム類似度で既存の 2 方式を上回りましたが、FID では最も不利でした。合成データだけで学習した分類器は、実データで学習した場合（F1 0.567）には届かず、F1 0.321 でした。"
links:
  - label: "Preprint (arXiv)"
    url: "https://arxiv.org/abs/2507.13380"
citation: |
  @article{inoshita2026persona,
    title   = {Persona-Based Synthetic Data Generation Using Multi-Stage Conditioning
               with Large Language Models for Emotion Recognition},
    author  = {Inoshita, Keito and Harada, Rushia},
    journal = {International Journal of Activity and Behavior Computing},
    volume  = {1},
    pages   = {1--18},
    year    = {2026}
  }
---

<div class="teaser">
<div>

Generate

ペルソナを **3 段階** で積み上げ、7 感情 × 500 文 = **3,500 文** を生成。

</div>
<div>

Separate

感情ごとの分類で全体 **F1 0.80**。ただし joy と pleasure は 0.62・0.61 と混ざりやすい。

</div>
<div>

Compare

実ツイートとの分布の近さは PRD-Fβ **0.367**（既存方式 0.259・0.282）。ただし FID では最も不利。

</div>
</div>

## 感情データはなぜ足りないのか

感情認識モデルの性能が伸びにくい理由の一つは、質のよい感情データが少ないことです。感情の表れ方は人によって大きく違い、性格や社会文化的な背景、その場の状況に左右されます。そのため、いろいろな人の感情表現を幅広く集めたデータを作るのは難しくなります。

集めること自体にも制約があります。職場や医療の現場では、本人の心理的な負担やプライバシーの問題があります。子どもや高齢者の感情反応を集めることは、今の倫理の枠組みではほぼできません。

そこで注目されているのが、LLM に感情テキストを書かせる方法です。ペルソナや状況を与えると、LLM はそれに沿った感情表現を書けます。この研究では、**ペルソナをどう作れば、多様で、実データに近い感情テキストになるのか**を問いにしました。

## PersonaGen の仕組み

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/framework-1600.webp" alt="PersonaGen framework" />
  <figcaption><strong>Figure 1.</strong> PersonaGen の全体図（論文の Figure 1）。左の 3 段でペルソナと場面を組み立て、右で LLM に感情テキストを書かせます。</figcaption>
</figure>

PersonaGen は、ペルソナを一度に決めるのではなく、段階的に積み上げます。

1. **基本属性**：年齢層・性別・職業・性格タイプ（MBTI の 32 類型）を、実際の人口統計や調査に近い確率分布から引きます。「小学生」と「弁護士」のようなありえない組み合わせは、ルールで先に除きます。
2. **社会文化的背景**：学歴・居住地・地域・家族構成・宗教・価値観・収入の 7 項目を足します。学歴は年齢層に合わせ、収入はライフステージに合わせるなど、条件つきで引きます。
3. **場面と文体**：場所・活動・話し相手・伝達手段・言葉づかいの 5 項目を決めます。例として「病院のロビーで待ちながら、SNS で医師とやりとりする」「丁寧語、若者言葉、感情豊か、話し言葉」のような設定ができます。
4. **生成**：ここまでの情報と目標の感情を一つのプロンプトにまとめ、LLM に最大 2 文の短い文章を書かせます。

各段で、属性の組み合わせを LLM に「自然」「まれだがありうる」「ありえない」の 3 段階で判定させ、前の 2 つだけを残します。ルールでは拾えない不自然な組み合わせを除くためです。

場面の項目を絞れば、用途に合わせたデータも作れます。たとえば SNS 向けなら活動を「SNS 投稿」に固定し、職場向けなら場所や相手を職場のものに寄せます。後の実験 4 では、この仕組みでツイート風の文章を作っています。

## 実験 1：感情ごとに区別できる文章になっているか

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- 生成モデル：GPT-4.1-mini（temperature 1.2）
- 感情：joy, anger, sadness, pleasure, surprise, fear, neutral の 7 種、各 500 文（計 3,500 文）
- 埋め込み：all-MiniLM-L6-v2
- 分類：LightGBM、学習 80% / テスト 20%

</div>

まず、生成した文章を埋め込み空間に置いて、感情ごとにまとまるかを見ました。

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/tsne-1600.webp" alt="t-SNE of synthetic emotion texts" />
  <figcaption><strong>Figure 2.</strong> 生成した 3,500 文の埋め込みを t-SNE で 2 次元にしたもの（論文の Figure 2）。sadness・fear・anger はまとまり、joy と pleasure は重なっています。</figcaption>
</figure>

sadness、fear、anger は比較的はっきりした塊になりました。一方、joy と pleasure は一部が重なっています。どちらも快で覚醒度も近い感情なので、意味の上でも近いことを反映していると考えられます。

同じ埋め込みを使って LightGBM で 7 感情を分類しました。

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/per-emotion-f1-1600.webp" alt="Per-emotion F1" />
  <figcaption><strong>Figure 3.</strong> 感情ごとの F1（論文の Table 5）。青の joy と pleasure 以外は 0.8 を超えています。</figcaption>
</figure>

全体の F1 は 0.80 でした。fear（0.92）、anger（0.91）、sadness（0.89）は高く、joy（0.62）と pleasure（0.61）は低めです。混同行列でも joy と pleasure の取り違えが目立ち、neutral と pleasure の間にも重なりがありました。近い感情をもっとはっきり書き分けるには、追加の条件づけが必要です。

## 実験 2：表現の幅はどのくらいあるか

<p class="experiment-label">Experiment 2</p>

区別できるだけでなく、同じ感情の中で表現に幅があるかも見ました。指標は 3 つです。平均コサイン距離（MCD）は同じ感情の文どうしがどれだけ離れているか、クラスタエントロピー（CE）は分布がどれだけ均等に広がっているか、重心距離（CD）は感情どうしの重心がどれだけ離れているかを表します。

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/diversity-1600.webp" alt="Semantic diversity per emotion" />
  <figcaption><strong>Figure 4.</strong> 感情ごとの MCD と CE（論文の Table 4）。縦軸は 0 から始まっていません。</figcaption>
</figure>

surprise、anger、neutral は MCD が 0.73〜0.75 と高く、表現にばらつきがあります。joy（0.572）と pleasure（0.586）は低く、言い回しが似通っていました。実験 1 で混ざりやすかった 2 つの感情は、表現の幅も狭かったことになります。

## 実験 3：人が書いたように見えるか

<p class="experiment-label">Experiment 3</p>

GPT-4o に、感情の一致・文法・語彙の多様さと適切さ・構成と論理の 4 項目を 5 段階で採点させました。

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/human-likeness-1600.webp" alt="Human-likeness scores" />
  <figcaption><strong>Figure 5.</strong> GPT-4o による 4 項目の採点（平均 ± 標準偏差、論文の Figure 4 の値）。縦軸は 3 から始めています。</figcaption>
</figure>

文法は 5.00、構成と論理は 4.83 でした。感情の一致（4.65）と語彙（4.68）はばらつきがやや大きく、surprise や joy で点が揺れていました。なお、この評価は人間ではなく LLM による採点です。

## 実験 4：実際のツイートにどれだけ近いか

<p class="experiment-label">Experiment 4</p>

<div class="setup">

**Setup**

- 実データ：Kaggle で公開されている感情ツイートのデータ（joy, anger, sadness, love, surprise, fear の 6 種）
- 合成データ：場面を SNS の単発投稿に固定し、短くくだけたツイート風に制約して各感情 500 文（計 3,000 文）
- 比較：AttrPrompt（属性をランダムに引いて 1 つのプロンプトに並べる）、RandPersona（ペルソナ属性を独立に引き、整合性の制御をしない）

</div>

まず、合成データの分布が実データにどれだけ近いかを 4 つの指標で比べました。

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/similarity-1600.webp" alt="Similarity to gold tweets" />
  <figcaption><strong>Figure 6.</strong> 実ツイートとの分布の近さ（論文の Table 6）。↓ は低いほど、↑ は高いほどよい指標です。</figcaption>
</figure>

| 方式 | FID ↓ | PRD-Fβ ↑ | KL ↓ | HC ↑ |
|---|---|---|---|---|
| AttrPrompt | **0.388** | 0.259 | 0.070 | 0.982 |
| RandPersona | 0.397 | 0.282 | 0.055 | 0.986 |
| PersonaGen | 0.414 | **0.367** | **0.049** | **0.988** |

PersonaGen は PRD-Fβ、KL、ヒストグラム類似度（HC）で最もよい値でした。一方、FID では 3 方式の中で最も不利です。すべての指標で勝っているわけではありません。論文では、語彙の幅が広いことと統計的なそろい方との間のトレードオフとして解釈しています。

次に、実データの学習用部分を合成データに置き換えて 6 感情の分類器（LightGBM）を学習し、実データのテストセットで評価しました。

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/downstream-1600.webp" alt="Downstream classification" />
  <figcaption><strong>Figure 7.</strong> 合成データだけで学習した分類器の、実データのテストセットでの性能（論文の Table 7）。上の青は実データで学習した場合です。</figcaption>
</figure>

どの合成データも、実データで学習した場合（Accuracy 0.568、F1 0.567）には届きませんでした。合成データの中では PersonaGen が Accuracy 0.359、Precision 0.400、Recall 0.359、F1 0.321 と、4 指標すべてで最もよい値でした。ただし F1 は AttrPrompt の 0.320 とほぼ同じです。PersonaGen のデータは、実データの代わりではなく、補うためのものとして位置づけています。

最後に、生成文の例を著者 2 名が独立に読み、感情を示す語や状況が目標の感情に合っているかを確かめました。たとえば fear では「Feeling lost and uncertain about the future. The weight of being unemployed fills me with fear.」のように、失業という具体的な不安が書かれていました。

## わかったこと・わかっていないこと

この研究でわかったのは次の点です。

- ペルソナを段階的に積み上げて生成すると、7 感情の大半を区別でき（全体 F1 0.80）、文法や構成の点でも自然な文章になった。
- 実ツイートとの比較では、属性をランダムに並べる方式より分布が近くなった（PRD-Fβ・KL・HC）。ただし FID では不利だった。
- 合成データだけで学習した分類器は、実データで学習した分類器に大きく及ばない。

限界もあります。実データとの比較はツイートのデータセット 1 つだけで、会話・ニュース・臨床などのコーパスでは試していません。生成モデルも 1 種類だけで、別の LLM で結果が変わるかはわかっていません。joy と pleasure のような近い感情の書き分けは、まだできていません。また、扱っているのは静的なテキストだけで、対話の流れや時間変化、マルチモーダルな文脈は入っていません。

今後は、複数の種類のコーパスでの評価、LLM や生成設定による違いの検証、近い感情を分けるための条件づけ（valence–arousal や評価理論の属性、対照的なプロンプト）に取り組みます。
