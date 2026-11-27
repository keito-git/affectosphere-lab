---
title: "Can an LLM Turn Down the Emotional Volume of News Without Changing the Facts?"
subtitle: "Multi-Agent Large Language Model Based Emotional Detoxification Through Personalized Intensity Control for Consumer Protection"
date: "2026-11-27"
excerpt: "怒りや不安をあおるニュースの書き方だけを LLM で穏やかに書き直し、事実は保てるかを調べました。刺激の強さは最大 19.3% 下がり、意味の保持とはほぼ無相関でした。一方、事実そのものが強い国際ニュースでは下がりませんでした。IEEE ZINC 2026 論文の解説です。"
readingMinutes: 10
showImage: false
image: "/column-images/zinc2026-emotional-detox/overview.png"
imageAlt: "MALLET の全体図。感情分析・感情調整の 2 エージェントによる実時間の処理と、バランス監視・パーソナルガイドの 2 エージェントによる週単位の個人化からなる。"
authors:
  - name: "井下 敬翔"
    url: "/about/"
    affiliation: "関西大学"
tldr: "扇情的な見出しは、読み手を怒りや不安にさらし、落ち着いた判断を妨げます。MALLET は 4 つのエージェントで、ニュース文の刺激の強さを測り、事実を保ったまま穏やかな表現に書き直し（BALANCED と COOL の 2 段階）、週ごとの閲覧の偏りを助言し、読み手の感受性に合う表示モードを勧めます。AG News 800 件では、平均刺激スコアが BALANCED で 13.1%、COOL で 19.3% 下がりました。刺激の下がり幅と意味の保持の相関はほぼ 0 で、両者は独立に扱えることがわかりました。ただし、事実そのものが強い World カテゴリではほとんど下がりませんでした。"
links:
  - label: "Paper (IEEE ZINC)"
    url: "https://doi.org/10.1109/zinc69910.2026.11655671"
citation: |
  @inproceedings{inoshita2026mallet,
    title     = {Multi-Agent Large Language Model Based Emotional Detoxification
                 Through Personalized Intensity Control for Consumer Protection},
    author    = {Inoshita, Keito},
    booktitle = {Proceedings of the IEEE ZINC},
    year      = {2026},
    month     = jun,
    doi       = {10.1109/zinc69910.2026.11655671}
  }
---

<div class="teaser">
<div>

Reduce

平均刺激スコアは **RAW 0.482 → COOL 0.389**（−19.3%）。しきい値を超える文の割合も 0.446 から 0.330 に下がる。

</div>
<div>

Preserve

意味の類似度は **0.846 / 0.827**。NLI で矛盾と判定された書き換えは 1.9% / 3.6%。刺激の下がり幅との相関は r ≈ −0.04。

</div>
<div>

Limit

**World カテゴリでは効かない**（BALANCED −0.1%、COOL 2.2%）。「爆発」「攻撃」は修飾ではなく事実そのものだから。

</div>
</div>

## 情報の「中身」ではなく「伝え方」に介入する

注目を集めることが収益になる環境では、扇情的な見出しや極端な言い回しが増えます。こうした強い感情刺激は怒りや不安を高め、落ち着いた判断を妨げます。消費者がニュースを受け取る場面でも同じです。

消費者向けの情報対策は、これまでフェイクニュースの検出のように**情報そのもの**を対象にするものが中心でした。この研究は、受け手の感情の側に目を向けます。事実は変えずに**伝え方の刺激の強さだけを下げる**ことで、消費者が落ち着いて情報を受け取れるよう支援する、という考え方です。

既存のテキストスタイル変換は、感情の極性（ポジティブ⇔ネガティブ）を入れ替えることが主な目的でした。この研究で扱うのは極性ではなく**強さ**で、それを段階的に調整できるかを問いにしました。

## MALLET の仕組み

<figure>
  <img src="/column-images/zinc2026-emotional-detox/overview-1600.webp" alt="MALLET overview" />
  <figcaption><strong>Figure 1.</strong> MALLET の全体図（論文の図をそのまま掲載）。上段が文ごとの実時間処理、下段が週単位の個人化です。</figcaption>
</figure>

MALLET（Multi-Agent LLM-based Emotional deToxification）は、4 つのエージェントを順につないだシステムです。

1. **感情分析エージェント**：6 感情（anger / fear / sadness / joy / love / surprise）の BERT 分類器で各文の確率分布を出します。怒り・恐れ・驚きの確率の和を**刺激スコア S**（0〜1）とし、S が 0.6 を超える文の割合を **HIR**（High-Impact Rate）、6 感情の分布がどれだけ均等かを **EBI**（Emotion Balance Index）とします。読みやすさの指標 FRE（Flesch Reading Ease）も並行して測ります。
2. **感情調整エージェント**：GPT-4.1-mini で、事実・固有名詞・数値を保ったまま書き直します。**BALANCED** は扇情的な語を中立的な語に置き換えた 1 文、**COOL** はそれに背景や用語の説明を 1 文足した 2 文です。長さは原文の ±20% 以内、温度は 0.2 です。書き直しが意味を壊していないかは、SBERT のコサイン類似度と NLI の矛盾率で確かめます。
3. **バランス監視エージェント**：消費者ごとに 1 週間の閲覧履歴を集計し（平均 S、HIR、EBI、6 感情の平均）、その要約を LLM に渡して具体的な助言を作ります。
4. **パーソナルガイドエージェント**：消費者の感受性のプロフィールから、最初の表示モード（RAW / BALANCED / COOL）を LLM が選び、理由を 1 文で添えます。

分析と調整を分けたので、各部品を別々に更新できます。また表示モードを 2 段階用意したことで、刺激をどこまで下げるかを読み手ごとに変えられます。

## 実験 1：刺激はどれだけ下がるか

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- データ：AG News（英語ニュース）の 4 カテゴリ（World / Sports / Business / Sci/Tech）から各 200 件、計 800 件
- 条件：同じ文に対する RAW（原文）・BALANCED・COOL の 3 条件の被験者内比較
- 指標：刺激スコア S、HIR（θ = 0.6）、EBI、FRE
- 検定：両側の対応のある t 検定（Holm 補正）、効果量は Cohen の d

</div>

<figure>
  <img src="/column-images/zinc2026-emotional-detox/mode-metrics-1600.webp" alt="Primary metrics across presentation modes" />
  <figcaption><strong>Figure 2.</strong> 表示モードごとの主な指標。灰色が原文（RAW）、青が BALANCED、金色が COOL です。</figcaption>
</figure>

原文の平均刺激スコアは 0.482 で、HIR は 0.446 でした。原文の約 45% がしきい値 0.6 を超えていることになります。書き直し後は、BALANCED で平均刺激スコアが 13.1%、HIR が 20.6% 下がり、COOL ではそれぞれ 19.3% と 26.0% 下がりました。COOL の方が大きく下がるのは、補足の 1 文で中立的な表現の割合が増えるためと考えられます。感情の偏りを表す EBI も 0.316 から 0.338、0.346 へと上がりました。

一方、読みやすさ（FRE）は BALANCED で 30.23（24.3% 低下）、COOL で 34.54（13.5% 低下）に下がりました。BALANCED は 1 文に収める制約のもとで抽象的な語を選びやすく、COOL では補足文の平易な説明がそれを和らげています。

<figure>
  <img src="/column-images/zinc2026-emotional-detox/effect-sizes-1600.webp" alt="Effect sizes of paired t-tests" />
  <figcaption><strong>Figure 3.</strong> 6 つの比較の効果量（絶対値）。いずれも Holm 補正後 p &lt; 0.001 です。点線は Cohen の基準で「小」（0.2）と「中」（0.5）。</figcaption>
</figure>

6 つの比較はすべて有意でした。ただし、刺激スコアの低下の効果量は d = 0.210（BALANCED）と d = 0.282（COOL）で、Cohen の基準では**小さい**効果です。読みやすさの低下は BALANCED で d = 0.609（中程度）と、刺激の低下よりも大きく出ています。

## 実験 2：どのニュースで効くか

<p class="experiment-label">Experiment 2</p>

<figure>
  <img src="/column-images/zinc2026-emotional-detox/category-1600.webp" alt="Mean stimulus score by category" />
  <figcaption><strong>Figure 4.</strong> カテゴリ別の平均刺激スコア。上のラベルは COOL による低下率です。World だけほとんど下がっていません。</figcaption>
</figure>

| カテゴリ | RAW | BALANCED | COOL | 低下率（BAL） | 低下率（COOL） |
|---|---|---|---|---|---|
| World | 0.659 | 0.660 | 0.645 | −0.1% | 2.2% |
| Sports | 0.393 | 0.312 | 0.260 | 20.6% | 33.8% |
| Business | 0.500 | 0.396 | 0.350 | 20.8% | 30.0% |
| Sci/Tech | 0.374 | 0.308 | 0.299 | 17.8% | 20.0% |

Sports・Business・Sci/Tech では刺激が大きく下がりましたが、World ではほぼ変わらず、BALANCED ではわずかに上がりました（−0.1%）。World は紛争やテロなど、出来事そのものが強い刺激をもつニュースを扱います。そこでは「爆発」「攻撃」といった語は扇情的な修飾ではなく、事実を伝えるのに欠かせない語なので、語彙のレベルでは中立化できません。論文では、こうした内容には段階的に情報を開示するなど、別の介入が必要になると述べています。

## 実験 3：どの感情が減ったのか

<p class="experiment-label">Experiment 3</p>

刺激スコアは 6 感情の分布を 1 つの値にまとめたものなので、感情ごとの変化も見ました。

最も大きく変わったのは**怒り**で、平均確率は 0.34 から 0.24 へ約 29% 下がりました。LLM が「scorching」「outrage」のような扇情的な語を「recorded」「reported」のような中立的な語に置き換えたためです。同時に**喜び**が 0.37 から 0.42（BALANCED）/ 0.45（COOL）に上がりました。これは softmax の制約によるもので、怒りから抜けた確率が他の感情に配り直され、分類器の上で中立的な表現に最も近い喜びが一番多く受け取った、という解釈です。

恐れ・悲しみ・愛・驚きには大きな変化がありませんでした。恐れが動かないことは、World で刺激が下がらなかったことと整合します。MALLET による刺激低下の主な仕組みは怒りの選択的な減少であり、恐れに対しては別の介入が要る、というのが論文の見立てです。

## 実験 4：意味は保たれているか

<p class="experiment-label">Experiment 4</p>

<figure>
  <img src="/column-images/zinc2026-emotional-detox/semantic-1600.webp" alt="NLI judgement distribution" />
  <figcaption><strong>Figure 5.</strong> 原文を前提、書き直し文を仮説としたときの NLI 判定の内訳。括弧内は SBERT のコサイン類似度の平均です。</figcaption>
</figure>

SBERT の類似度は BALANCED で 0.846、COOL で 0.827 でした。NLI では、BALANCED の 95.1% が含意と判定されました。COOL では中立が 68.6% を占めますが、これは補足の 1 文が「原文にない追加情報」と判定されたためで、矛盾ではありません。矛盾と判定された割合は BALANCED で 1.9%、COOL で 3.6% でした。

さらに、文ごとの刺激の下がり幅（S_RAW − S_mode）と SBERT 類似度の相関は、BALANCED で r = −0.039、COOL で r = −0.046 でした。**大きく穏やかにした文ほど意味が崩れる、という関係は見られませんでした**。この範囲では、刺激を下げることと意味を保つことはトレードオフではなく、別々に扱えるということです。

## 実験 5：週ごとの集計と助言

<p class="experiment-label">Experiment 5</p>

<div class="setup">

**Setup**

- 実際の閲覧ログはないため、刺激スコアを付けた文の集まりから 1 人あたり 100 件を非復元抽出し、5 人の疑似消費者をつくった
- 週ごとの要約（平均 S、HIR、EBI、6 感情の平均）を JSON にして GPT-4.1-mini に渡し、助言を生成（温度 0.3）

</div>

<figure>
  <img src="/column-images/zinc2026-emotional-detox/consumers-1600.webp" alt="Weekly summary of pseudo-consumers" />
  <figcaption><strong>Figure 6.</strong> 疑似消費者 5 人の週ごとの HIR と怒りの平均確率。HIR は 0.41〜0.53、怒りは全員で 0.31〜0.40 と高めです。</figcaption>
</figure>

怒りが全員で高めなのは、AG News というデータの性質を反映しています。助言の例を 2 人分見ると、HIR が 0.53 と 0.5 を超えた消費者 0 には、紛争関連のニュースから話題を広げることと、表示モードを COOL か BALANCED に切り替えることが勧められました。喜びが優勢（0.404）で HIR が 0.44 の消費者 3 には、モードはそのままで話題を広げることだけが勧められました。どちらの助言にも、感情の偏りの診断、具体的な行動の提案、数値の根拠の 3 つが含まれていました。

## 実験 6：表示モードの推薦

<p class="experiment-label">Experiment 6</p>

感受性の異なる 3 つのペルソナについて、パーソナルガイドエージェントが最初の表示モードを選びました。

| ペルソナ | 特徴 | 推薦 | 理由（要約） |
|---|---|---|---|
| P1 | 不安や怒りに敏感で、ドゥームスクロールに陥りやすい | COOL | 穏やかで文脈の多い書き直しが不安を和らげる |
| P2 | 事実と感情的なトーンの両方を求める | BALANCED | 事実の正確さとほどよいトーンの両立が合う |
| P3 | 大胆な表現を好むが正確さも重視する | RAW | 原文の勢いを保ちつつ正確さも保てる |

感受性が高い順に COOL → BALANCED → RAW と段階的に推薦されました。これは実験 1 の刺激低下の大きさ（COOL 19.3% ＞ BALANCED 13.1% ＞ RAW 0%）の順と一致しています。

## わかったこと・わかっていないこと

この研究でわかったのは次の点です。

- LLM による書き直しで、ニュースの感情刺激の**強さ**を 2 段階で下げられる（平均刺激スコア −13.1% / −19.3%）。ただし効果量は小さい。
- 刺激の下がり幅と意味の保持はほぼ無相関で、この範囲では両者をトレードオフなしに扱える。
- 効果は扇情的な修飾を取り除くことから来ており、出来事そのものが強い World カテゴリでは効かない。減ったのは主に怒りで、恐れは動かなかった。
- 週ごとの指標から具体的な助言を作ることと、感受性に合わせた表示モードの推薦は、仕組みとして実現できる。

一方で、限界もあります。刺激が下がったかどうかの評価は感情分類器の出力に頼っており、人が実際に感じる刺激での検証が必要です。BALANCED の読みやすさの低下（d = 0.609）は、プロンプトに読みやすさの制約を明示して抑える必要があります。バランス監視エージェントの評価は疑似消費者によるもので、実際の閲覧ログを使った長期の検証はこれからです。対象は英語のテキストだけで、日本語を含む多言語での有効性は確かめていません。

今後は、人による評価、事実そのものが強い内容への別の介入、実データでの長期評価、多言語対応に取り組みます。
