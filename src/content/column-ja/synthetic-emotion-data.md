---
title: "感情データは「集める」から「作る」へ ── 合成データという第三の選択肢"
date: "2026-06-01"
excerpt: "感情ラベル付きデータは、心理的負担・プライバシー・代表性の壁で集めにくい。最新研究 3 本が示すのは、ドメイン知識と LLM を使えば、倫理とコストを同時に解決できる場面が出てきたという事実です。データ運用担当者向けに 5 分で。"
image: "/column-images/synthetic-emotion-data.png"
imageAlt: "散らばるデータポイントの欠落部分を amber 色のドットが補完し、薄い人型シルエットが重なる抽象的なビジュアル"
readingMinutes: 5
basedOnPaper: "Persona-Based Synthetic Data Generation Using Multi-Stage Conditioning with Large Language Models for Emotion Recognition"
basedOnPaperUrl: "https://arxiv.org/"
---

こんにちは。Affectosphere Group の井下です。

最近、データ基盤の責任者の方からこんな相談を受けました。

「感情分析の精度上げたいんですけど、ラベル付きデータが圧倒的に足りないんですよ。集めようとすると、コストも倫理ハードルも壁が高くて」

これ、すごく分かるんです。

感情データの調達は、ふつうのアノテーション業務とぜんぜん事情が違います。
怒り・悲しみ・不安に満ちた文章を一日中読んでラベリングする作業って、それ自体がアノテーターさんに二次的なメンタルダメージを残すんですよね。

さらに、感情データは個人の内面そのものに直結する最も繊細な情報。
GDPR や個情法でも特に注意深く扱う必要があるし、少数派の顧客層・特定文化圏のユーザ・社会的に脆弱な立場の人々から、倫理的に十分な配慮をしながら集めるのは、構造的にかなりキツい。

「集められないから精度が出ない、精度が出ないから事業展開できない」── このループ、どこかで断ち切らないと進みません。

ここ 1〜2 年で急速に注目されているのが、合成感情データ(synthetic emotional data)です。
今日は、私たちが 2025-2026 年に公開した 3 本の研究[^1][^2][^3]を、データ運用と倫理担当の言葉で書きます。

[^1]: Keito Inoshita, Rushia Harada, "Persona-Based Synthetic Data Generation Using Multi-Stage Conditioning with Large Language Models for Emotion Recognition", International Journal of Activity and Behavior Computing, vol. 1, pp. 1-18, 2026.
[^2]: Keito Inoshita, Hayato Tomisu, Xiaokang Zhou, Akira Kawai, Katsutoshi Yada, "KDDA: A Knowledge-Driven Domain and Diversity Alignment Framework for Emotion Data Generation with Large Language Models", International Journal of Activity and Behavior Computing, vol. 1, pp. 1-24, 2026.
[^3]: Keito Inoshita, Xiaokang Zhou, Akira Kawai, Katsutoshi Yada, "Geometric Control-Based Data Augmentation with Cluster-Conditioned Interpolation and Extrapolation for Imbalanced Learning in LLM", arXiv preprint, 2025.

---

## 今日の結論を 3 行で

1. 価値: 「集める」より「作る」のほうが、倫理・コスト・精度のすべてで合理的になる場面が増えてきた。合成データは劣化版、という常識はもう古い。
2. 設計の肝: 幾何制御・ドメイン知識の統計的特徴化・多段ペルソナ条件付け、の 3 つを組み合わせると、合成データは実データに近づける。
3. 感情 AI 視点: 倫理的に集められない領域(メンタルヘルス・子ども・脆弱層)こそ、合成データの価値が爆発する。ここに踏み込めるか否かが、感情 AI の社会実装の分水嶺。

順に書きます。

---

## ① 3 本の研究、それぞれ何をやっているか

ざっくり並べると、こんな分担です。

### CIEGAD ── 少数派クラスを幾何的に補完する

CIEGAD(Cluster-conditioned Interpolation/Extrapolation Geometric Augmentation for Data)は、感情データに必ず生じる「クラスごとのサンプル数の偏り」への処方箋です。

「喜び」「悲しみ」は大量にあるけど、「畏敬」「軽蔑」は極端に少ない、というやつですね。

ここで CIEGAD は、埋め込み空間でのクラスタごとに「内挿(穴埋め)」と「外挿(周縁拡張)」を幾何制御して、少数派クラスのサンプルを生成します。
既存サンプル間を補間すれば穴を埋められ、クラスタの外側に外挿すれば周縁を広げられる、というシンプルだけど効く設計。
LLM に条件付けして条件に合うテキストを生成させることで、少数派クラスの F1 と Recall が安定的に改善することが示されました。

### KDDA ── ドメイン知識を「統計的特徴」に変換して生成する

KDDA(Knowledge-Driven Data Augmentation)は、もっと大胆です。
個人からデータを直接集める代わりに、対象領域に関する人間の知識を統計的特徴に変換し、LLM に条件付けして生成する。

たとえば「職場ストレス」というドメインなら、そのドメイン固有の語彙頻度、典型的状況、特徴的な感情パターンから「ドメインプロファイル」を構築して、それを生成条件として使います。
生成データは語彙レベルの重複抑制と統計的整合性評価で二重にフィルタリングされる。

合成データのみで学習した感情分類器が、実データに近い分布を達成できる ── という結果が出ました。
「集めずに作る」が、実用水準に近づいてきている。

### PersonaGen ── 多段ペルソナで自然な文体差を再現する

PersonaGen は、「同じ感情でも、人によって表現は違う」という当たり前の事実を、合成データに織り込む方法です。

10 代の学生が表現する「悲しみ」と、60 代の医師が表現する「悲しみ」は、語彙も文体も社会的文脈も全然違いますよね。

PersonaGen は「属性 → 社会文化背景 → 状況文脈」の 3 段階でペルソナ条件を積み重ねて、それぞれの人物像にふさわしい文体差を再現します。
同じ感情ラベルでも、語り手によって多様な表現が生まれる。
表現多様性と感情ラベル整合性を両立させる鍵は、ペルソナ条件付けの粒度を上げることだと示されました。

---

## ② これがビジネスに何を生むか

3 本まとめて見ると、こんな図式になります。

「集める」コストが下がるだけじゃなくて、「これまで集められなかった領域」に手が届くようになる、というのが本質的な変化です。

具体的に効く場面を 3 つ。

ひとつめは、データ調達コストの削減。
感情ラベル付きデータのアノテーションは、品質を担保しようとすると一文あたり数百円〜数千円規模になります。
合成データへの部分置き換えだけで、年間のデータ調達コストが桁単位で下がるケースは珍しくありません。

ふたつめは、アノテーター保護。
怒り・暴力・絶望に満ちたテキストを延々とラベリングさせる業務は、コンテンツモデレーション業界で訴訟事例が積み上がっている領域です。
合成データに一部置き換えるだけで、安全配慮義務の観点でも一歩前に出られます。

みっつめは、規制対応の前倒し。
EU AI Act、GDPR の解釈強化、各国の個情法改正 ── どれも「個人の内面を推論する処理」への要求水準を上げ続けています。
実データの収集と保管を続けるほど、規制環境変化時のリスクが累積する。
合成データへの段階的移行は、技術投資というよりリスクヘッジに近い意味合いを持ち始めています。

---

## ③ 感情 AI として一番伝えたいのは、ここ

ここが、Affectosphere Group が研究室として強調したいポイントです。

合成感情データの本当の価値は、「コスト削減」じゃないと思っています。

本質は、これまで倫理的に踏み込めなかった領域に、感情 AI を届けられるようになることです。

具体的にはこういう領域です。

- メンタルヘルス相談のテキスト解析
- 児童虐待相談・DV ホットライン
- 高齢者ケアの会話分析
- 自死リスクの早期検知
- 少数派文化圏の感情表現研究

どれも、実データを集めようとした瞬間に倫理ハードルが極限まで上がる領域です。
当事者からデータを取ること自体が、本人にさらなる負担を強いることになる。

でも、これらの領域こそ、感情 AI が最も社会的に価値を生む可能性のある場所でもあるんですよね。

ここで KDDA や PersonaGen のような技術が効いてきます。
「専門家の知識」を統計的特徴に変換して、「実在しないけれど、その領域の感情分布に忠実な」データを作る。
当事者から直接データを取らずに、当事者支援のための AI を作れる ──これが、感情 AI と合成データが組み合わさったときの最大のインパクトです。

私たちの研究室は、感情を「曖昧で多義的なまま扱う」ことを核にしています。
そして、最も曖昧で最も繊細な感情は、多くの場合、最もデータを取りにくい場所にあります。

合成データは、そこに技術側から橋をかける手段だと思っています。
ただし、誤って使えば「本物そっくりの偽物」を量産してしまう危険もある。
ドメイン知識との結合、品質監査、生成パイプラインの透明性 ── このあたりを丁寧に設計しないと、すぐ崩れます。

---

## じゃあ、明日から何をするか

動かせる打ち手を 3 つだけ。

- 自社が今集めている感情データを、「合成置換可能 / 実データ必須」で 2 列に分類してみる。これだけで議論の解像度がガラッと変わります。
- アノテーターの負荷が高いカテゴリを 1 つ特定して、合成データ生成パイロットを回す。完全置換ではなく、人手と合成のハイブリッドが現実解です。
- 評価データセットに合成データを意図的に加えて、地域別・属性別の精度均等性を KPI 化する。少数派の取りこぼしを構造的に減らせます。

「集めにくいから諦める」から、「集められないからこそ作る」へ。
データ戦略の前提が、ここ数年で確実にひっくり返りつつあります。

---

## 締め

データを集める力ではなく、データを作る力が、次の競争優位を決める ──と言うと大げさですが、感情 AI の領域では、もうかなり現実味のある話になってきました。

合成データは、技術的にも倫理的にも、扱いを間違えると簡単に毒に変わります。
だからこそ、「何を作って、何を作らないか」を決める設計判断が、これまで以上に重要になっていきます。

「うちのデータ戦略、本当にこのままで良いのか」と気になった方、まずは社内データの 2 列分類から始めてみてください。
意外と「これ、合成で十分じゃない?」というものがゴロゴロ見つかります。

では!

---

## 参考論文

1. Keito Inoshita, Rushia Harada (2026). *Persona-Based Synthetic Data Generation Using Multi-Stage Conditioning with Large Language Models for Emotion Recognition*. International Journal of Activity and Behavior Computing, vol. 1, pp. 1-18.
2. Keito Inoshita, Hayato Tomisu, Xiaokang Zhou, Akira Kawai, Katsutoshi Yada (2026). *KDDA: A Knowledge-Driven Domain and Diversity Alignment Framework for Emotion Data Generation with Large Language Models*. International Journal of Activity and Behavior Computing, vol. 1, pp. 1-24.
3. Keito Inoshita, Xiaokang Zhou, Akira Kawai, Katsutoshi Yada (2025). *Geometric Control-Based Data Augmentation with Cluster-Conditioned Interpolation and Extrapolation for Imbalanced Learning in LLM*. arXiv preprint.

<p class="ai-notice"><small>※ 本記事は一部 AI により執筆されており、間違った情報が含まれる恐れがあります。</small></p>
