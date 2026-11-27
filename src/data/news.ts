// Recent news entries shown on Home and in the News timeline.
// Each item can have a detail page at /news/{slug}/ (see src/pages/news/[slug].astro).

export type NewsEntry = {
  /** Bibliographic title (e.g., paper title). */
  title: string;
  authors?: string;
  /** Venue / where it was accepted or published. */
  venue: string;
  /** Summary (for papers, paste the paper's abstract). */
  summary?: string;
  /** Optional external link (DOI / publisher / event). */
  href?: string;
};

export type NewsItem = {
  date: string; // ISO YYYY-MM-DD
  label: string; // category shown in the timeline (受賞 / 論文 / ラボ ...)
  body: string; // one-line text shown in the timeline
  /** Detail-page slug. When set, the item links to /news/{slug}/. */
  slug?: string;
  /** Detail-page heading (announcement title). Falls back to body. */
  title?: string;
  /** Main text for award / announcement detail pages. */
  summary?: string;
  /** One or more bibliographic entries (e.g., papers accepted at the same venue). */
  entries?: NewsEntry[];
  /** Extra external links shown on the detail page. */
  links?: { label: string; url: string }[];
};

// All news items in reverse-chronological order.  Add new items at the top.
export const allNews: NewsItem[] = [
  {
    date: "2026-11-24",
    label: "論文",
    body: "井下の単著論文が Knowledge-Based Systems（IF 8.0）に採択されました。",
    slug: "20261124-kbs-ace-net",
    title: "井下の単著論文が Knowledge-Based Systems に採択",
    entries: [
      {
        title:
          "ACE-Net: Diagnosing Learned Deep Prior Injection for Fine-Grained Emotion Recognition in Under-Determined Texts",
        authors: "Keito Inoshita",
        venue: "Knowledge-Based Systems (Elsevier, IF 8.0, Q1, SJR 1.753)",
        summary:
          "短い文や感情語を含まない文では、表面の文字列だけでは書き手の感情が決まらないことが多く、細かな感情カテゴリの認識は難しい。外部資源に頼る手法は規模が大きく、LLMが生成した文脈を入力にそのまま連結しても改善しないことが知られていたが、文脈の注入がどのような条件で効くのかは明らかでなかった。本研究は、LLMが事前に生成した文脈の説明を蒸留してプロトタイプ辞書にまとめ、合成した文脈ベクトルをTransformerの中間層に注入する ACE-Net（Adaptive Context-Embedding Network）を提案した。辞書の作成に感情ラベルは不要で、推論時にLLMを呼び出さず、追加パラメータもわずかである。統制したアブレーションから、辞書の内容・離散的な選択・適応的な温度はいずれも単独では寄与せず、改善の全体が中間層の一定範囲に注入される単一の学習済み事前ベクトルに帰着し、改善を左右するのは注入の深さであることを示した。性質の異なる3つのベンチマークでは、文脈が不足するデータでのみ有意な改善が得られ、文脈が十分なデータでは改善がなかった。さらに、少数のラベル付き標本から計算する内部指標 FORGE-Ω が、注入がどの入力に効くかを事前に見分ける診断として、異なるバックボーンでも機能することを示した。",
      },
    ],
    links: [
      { label: "コード（GitHub）", url: "https://github.com/keito-git/ace-net" },
      { label: "データ（Zenodo）", url: "https://doi.org/10.5281/zenodo.23415199" },
    ],
  },
  {
    date: "2026-11-18",
    label: "受賞",
    body: "井下が 日本貨物鉄道株式会社 第26回貨物鉄道論文賞 にて最優秀賞を受賞しました。",
    slug: "20261118-kamotsu-tetsudo-ronbunsho",
    title: "第26回貨物鉄道論文賞 にて最優秀賞を受賞",
    summary:
      "日本貨物鉄道株式会社（JR貨物）が主催する「第26回貨物鉄道論文賞」において、井下の論文が最優秀賞を受賞しました。受賞論文は、国土交通省の貨物地域流動調査（2020～2024年度）を用いて全国の区間ごとに期待される鉄道コンテナの分担率を統計モデルと機械学習で推定し、期待を持続的に下回る区間からモーダルシフトの潜在量を推計したものです。",
    entries: [
      {
        title: "鉄道コンテナの「伸びしろ」はどこにあるか――公的流動統計と機械学習による区間別モーダルシフト潜在量の推計と優先回廊の提案――",
        authors: "井下 敬翔",
        venue: "第26回貨物鉄道論文賞（日本貨物鉄道株式会社）",
      },
    ],
  },
  {
    date: "2026-11-18",
    label: "受賞",
    body: "井下が NHK財団 第4回インフォメーション・ヘルスAWARD オープン部門 にて準グランプリを受賞しました。",
    slug: "20261118-information-health-award",
    title: "第4回インフォメーション・ヘルスAWARD オープン部門 にて準グランプリを受賞",
    summary:
      "一般財団法人NHK財団が主催する「第4回インフォメーション・ヘルスAWARD」のオープン部門において、井下が準グランプリを受賞しました。本アワードは、情報との付き合い方のバランス（インフォメーション・ヘルス）に関するアイデアや取り組みを募集するものです。",
  },
  {
    date: "2026-11-18",
    label: "論文",
    body: "井下が筆頭の共著論文が IEEE SocialCom 2026 に採択されました。",
    slug: "20261118-socialcom2026-lslm-bcf",
    title: "井下が筆頭の共著論文が IEEE SocialCom 2026 に採択",
    entries: [
      {
        title:
          "Label-Conditioned Speaker–Listener Model with Bayes-Based Cross-Family Fusion for LLM-Oriented Sarcasm Recognition",
        authors: "Keito Inoshita, Xiaokang Zhou, Akira Kawai, Huazhong Liu, Katsutoshi Yada",
        venue: "IEEE SocialCom 2026",
        summary:
          "LLMは皮肉な文章を生成できるが、その生成能力を実際の皮肉投稿の識別にどう生かせるかは明らかでない。本研究は、皮肉／非皮肉のラベルを条件として文章の書かれ方を学習した話者（Speaker）LLMと、ラベルトークンのロジット差で投稿を採点する識別的な聞き手（Listener）LLMを組み合わせる LSLM-BCF を提案した。話者は観測された投稿の尤度を両ラベルの下で計算し、ベイズの定理により尤度比を皮肉の事後オッズに変換するため、文章を生成せずに採点できる。異なるモデルファミリーの2つの話者のスコアを平均して聞き手のスコアと統合し、一方の話者は事後正則化尤度（PRL）損失で学習する。4つの皮肉データセットで比較手法中最高のF1を達成し、すべてのデータセットで聞き手単体のテストAUCを改善した（iSarcasm で0.889）。分析から、改善は投稿ごとの話者情報に由来し、異なるファミリーの統合は単一話者との統合より安定していることを示した。",
      },
    ],
  },
  {
    date: "2026-11-17",
    label: "論文",
    body: "井下の筆頭論文が Research Methods in Applied Linguistics（IF 5.5）に採択されました。",
    slug: "20261117-rmal-argument-rarity",
    title: "井下の筆頭論文が Research Methods in Applied Linguistics に採択",
    entries: [
      {
        title:
          "Argument Rarity as a Measure of Essay Originality in the Age of AI-Assisted Writing",
        authors: "Keito Inoshita, Michiaki Omura, Tsukasa Yamanaka, Go Maeda, Kentaro Tsuji",
        venue: "Research Methods in Applied Linguistics (Elsevier, IF 5.5)",
        summary:
          "LLMが流暢で整ったエッセイを書けるようになり、文章評価では論証の独創性が重要な対象になっている。本研究は、同じ課題に対する学生エッセイを参照コーパスとし、主張・根拠・論証構造の希少性として独創性のうち新規性の側面を測る枠組み AROA（Argument Rarity-based Originality Assessment）を提案した。2つの資料型課題の学生エッセイ1,354本と GPT-4.1-mini が生成したエッセイ1,000本に適用したところ、AIのエッセイは集団として著しく均質で、集団内の主張の多様性は学生の約3分の1だった。一方、個々の主張が学生より典型的だったのは1課題のみで、根拠は典型的とはいえなかった。AIのエッセイを参照コーパスに加えると主張の希少性の差は見かけ上3倍以上に広がり、参照コーパスの構成が希少性の意味を決めることを示した。摂動実験では捏造した根拠にも得点が付くことなども分かり、希少性を独創性と解釈するにはさらなる検証が必要としている。",
      },
    ],
  },
  {
    date: "2026-11-06",
    label: "論文",
    body: "井下の共著論文が Journal of Ethnic Foods に採択されました。",
    slug: "20261106-jef-kyotango-butyrate",
    title: "井下の共著論文が Journal of Ethnic Foods に採択",
    entries: [
      {
        title:
          "Diachronic Analysis of Food Culture and Butyrate Production Potential in the Kyotango Region, Japan: From the Jomon Period to the Present",
        authors: "Yutaro Inoshita, Keito Inoshita",
        venue: "Journal of Ethnic Foods (Springer Nature)",
        summary:
          "百寿者の割合が全国平均の約3倍で、腸内に酪酸産生菌が多いことで知られる京都府京丹後市について、縄文時代から現代までの6つの時代の食文化資料を、大規模言語モデル（LLM）を文献統合の道具として横断的にまとめた叙述的統合レビュー。浜詰貝塚の考古資料、延喜式、毛吹草、近世の郷土料理調査、現代のコホート研究を、酪酸産生菌が利用する食材と照らし合わせた。多様な海産物と食物繊維源はすべての時代に見られ、保存食・発酵食品は時代とともに加わり、へしこに至る。各時代を4軸の指標（BPPS）で評価し、1名と3種のオープンなLLMによる採点の一致度は高かった（ICC(2,k) = 0.91）。延喜式（927年）に丹後国の貢納品として記された山椒が現代のへしこ作りにも使われ続けていることを示し、京丹後の腸内環境が縄文期にさかのぼる食文化の構造を反映している可能性を提起した。因果の検証は今後の実証研究に委ねている。",
      },
    ],
  },
  {
    date: "2026-11-03",
    label: "論文",
    body: "井下の単著論文が WSDM 2027（Main Conference, Rank A）に採択されました。Main Conference の採択率は15.8%（査読対象1,756件中277件）でした。",
    slug: "20261103-wsdm2027-free-anchors",
    title: "井下の単著論文が WSDM 2027 に採択",
    entries: [
      {
        title:
          "Adding Judges Is Not Enough: Free Anchors for Identifiable LLM Judge Panels",
        authors: "Keito Inoshita",
        venue: "WSDM 2027 (Main Conference)",
        summary:
          "LLMを評価者（judge）として並べたパネルは、判定者を増やせば信頼できると考えられてきた。本論文は、判定者を足して効くかどうかは判定者の数ではなく、判定に使うプールと評価契約の条件で決まることを示す。パネルをファミリー単位の潜在クラスモデルとして扱い、識別に必要な条件と、ファミリーを足しても消えない混同の下限を導いた。ファミリーが識別力を増やすのは、その誤りが既存のファミリーから導けない場合だけで、二値ラベルでは調達の前に2つの尤度比で判定できる。独立に判定された2つのパネルでは、最初のファミリー以降のファミリーで識別集合の直径が縮むことは検出されず、二値の判定は検証した69件すべてを当てた。プールに既にある正解確認済みの明確な2項目で直径は18%縮んだが、LLMJudgeパネルではそうした項目が1つの関連度レベルにしかない。",
      },
    ],
  },
  {
    date: "2026-10-15",
    label: "論文",
    body: "井下の単著論文が Applied Soft Computing（IF 7.8）に採択されました。",
    slug: "20261015-asc-driver-intervention",
    title: "井下の単著論文が Applied Soft Computing に採択",
    entries: [
      {
        title:
          "Safety-Aware Evaluation of LLM-Generated Driver Intervention Messages through Multi-Task Risk Fusion",
        authors: "Keito Inoshita",
        venue: "Applied Soft Computing (Elsevier, IF 7.8)",
        summary:
          "LLMが生成する運転者向けの介入メッセージを、安全性の観点から評価する枠組み。複数のリスク次元をマルチタスクで統合し、メッセージを多面的に採点する。",
      },
    ],
  },
  {
    date: "2026-09-16",
    label: "論文",
    body: "井下の単著論文が 情報処理学会論文誌デジタルプラクティス に採録されました。",
    slug: "20260916-ipsj-dp-uncertainty",
    title: "井下の単著論文が 情報処理学会論文誌デジタルプラクティス に採録",
    entries: [
      {
        title:
          "「LLMはラベルを出すが不確実性は出さない」という壁をどう越えるか -主観的判断タスクへの生成AI導入における実装・運用プラクティス-",
        authors: "井下敬翔",
        venue: "情報処理学会論文誌デジタルプラクティス（2027年4月号 掲載予定）",
      },
    ],
  },
  {
    date: "2026-09-16",
    label: "受賞",
    body: "井下が 公益社団法人教育文化協会 第23回 私の提言募集 にて奨励賞を受賞しました。",
    slug: "20260916-watashi-no-teigen",
    title: "第23回 私の提言募集 にて奨励賞を受賞",
  },
  {
    date: "2026-09-16",
    label: "受賞",
    body: "井下が 若者を考えるつどい2026「働くってなんだろう」エッセイ にて勤労青少年躍進会理事長賞を受賞しました。",
    slug: "20260916-hataraku-essay",
    title: "「働くってなんだろう」エッセイ にて勤労青少年躍進会理事長賞を受賞",
  },
  {
    date: "2026-08-16",
    label: "論文",
    body: "井下が筆頭の共著論文が IEEE ICDM 2026 (Research Track, Rank A*) に採択されました。Research Track の採択率は19.93%（投稿1,450件中289件）でした。",
    slug: "20260816-icdm2026-bsetd",
    title: "井下が筆頭の共著論文が IEEE ICDM 2026 に採択",
    entries: [
      {
        title:
          "Bayesian Spectral Emotion Transition Discovery from Multi-Annotator Disagreement",
        authors: "Keito Inoshita, Takato Ueno",
        venue: "IEEE ICDM 2026 (Research Track)",
        summary:
          "アノテーター間の不一致を「ノイズ」ではなく「信号」として扱い、多アノテーターのソフトラベルから感情の遷移構造を教師なしで発見する2段階フレームワーク（BSETD）。ベイズ的な遷移確率推定（Dirichlet-Multinomial階層モデル＋FDR制御）とグラフスペクトル分解により、感情の慣性（inertia）と伝染（contagion）を分離する。5コーパスの多言語横断検証で、心理学的知見（Plutchik／Russell 等）と整合することを示した。",
      },
    ],
  },

  {
    date: "2026-08-11",
    label: "論文",
    body: "井下の単著論文が AI & Society（Springer, IF 6.1）に採択されました。",
    slug: "20260811-ai-society-silos",
    title: "井下の単著論文が AI & Society に採択",
    entries: [
      {
        title:
          "Bridging the Silos in Affective AI: A Critical Perspective from Data to Society",
        authors: "Keito Inoshita",
        venue: "AI & Society (Springer)",
        summary:
          "感情コンピューティングを6層のパイプラインとして捉え直し、分野を横断して連鎖する4つの断絶（サイロ）を診断し、それらに噛み合う5つの統合的な設計指針を提示する立場表明論文。Affective AIを、人間の感情主体性を尊重すべき社会技術システムとして位置づける。",
      },
    ],
  },
  {
    date: "2026-08-11",
    label: "論文",
    body: "井下の共著論文2本が IEEE GCCE 2026 に採択されました（うち1本は奥河が筆頭）。",
    slug: "20260811-gcce2026",
    title: "井下の共著論文2本が IEEE GCCE 2026 に採択",
    entries: [
      {
        title:
          "Re-Defining Vanishing Municipalities in Japan: A Multidimensional Clustering and SLM-Based Policy Insight Framework",
        authors: "Toma Okugawa, Keito Inoshita",
        venue: "IEEE GCCE 2026",
        summary:
          "「消滅可能性自治体」を20〜39歳女性人口の減少という単一指標ではなく、125の指標・1,721自治体から多次元にクラスタリング（UMAP＋HDBSCAN＋SHAP）し、各クラスタのプロファイルを小規模言語モデル（SLM）へRAGで与えて自治体別の政策提言を生成する、再現可能な枠組み（UBRS）を提案した研究。",
      },
      {
        title:
          "Behavioral Fidelity and Philosophy-Grounded Design for Self-Reflective Conversational AI",
        authors: "Takumi Matsuo, Keito Inoshita",
        venue: "IEEE GCCE 2026",
        summary:
          "LLM対話エージェントが設計者の意図した振る舞いの仕様に実際に従っているかを定量化する評価枠組み「Behavioral Fidelity（BF）」を提案。LLM-as-judgeによる戦略分類・KLダイバージェンス分析・逐次制約検証で検査し、言語哲学に基づく自己省察アプリ Mirra へ適用。消費者向けAIには振る舞いの検証と目的整合的な設計の両方が必要であることを示す研究。",
      },
    ],
  },

  {
    date: "2026-08-05",
    label: "受賞",
    body: "日本情報教育学会 第10回研究会「AI Grand Prix」にて大賞を受賞しました。",
    slug: "20260805-ai-grand-prix",
    title: "「AI Grand Prix」にて大賞を受賞",
    summary:
      "日本情報教育学会 第10回研究会にて開催された「AI Grand Prix」において、大賞を受賞しました。",
  },
  {
    date: "2026-07-01",
    label: "論文",
    body: "井下の共著論文が PLOS ONE および Journal of Plankton Research に掲載されました。",
    slug: "20260701-papers-plosone-jpr",
    title: "井下の共著論文2本が PLOS ONE / Journal of Plankton Research に掲載",
    entries: [
      {
        title:
          "Historical, taxonomic, and cultural patterns in scientific naming across Animalia",
        authors: "Kota Nojiri, Keito Inoshita, Haruto Sugeno, Takumi Taga",
        venue: "PLOS ONE",
        summary:
          "動物界全体を対象に、学名の語源に見られる歴史的・分類学的・文化的なパターンを大規模に分析した研究。",
      },
      {
        title:
          "Applying large language models to expert-based etymological classification in zooplankton",
        authors: "Haruto Sugeno, Keito Inoshita, Kota Nojiri",
        venue: "Journal of Plankton Research",
        summary:
          "大規模言語モデルを用いて、専門家ベースの動物プランクトンの語源分類を支援する手法を提案した研究。",
      },
    ],
  },
  {
    date: "2026-05-27",
    label: "ラボ",
    body: "Affectosphere Group のウェブサイトを公開しました。",
    slug: "20260527-website-launch",
    title: "Affectosphere Group ウェブサイトを公開",
    summary:
      "感情×AI（affective computing）の研究を発信する Affectosphere Group のウェブサイトを公開しました。",
  },
  {
    date: "2026-05-24",
    label: "受賞",
    body: "JpGU・JSAI 主催「GeoSciAI2026」気象課題にて学生賞を受賞しました。",
    slug: "20260524-geosciai-meteorology",
    title: "「GeoSciAI2026」気象課題にて学生賞を受賞",
    summary:
      "日本地球惑星科学連合（JpGU）・人工知能学会（JSAI）が主催する「GeoSciAI2026」の気象課題において、学生賞を受賞しました。",
  },
];

// Items rendered on the Home page (top 5 by date).
export const recentNews: NewsItem[] = allNews.slice(0, 5);
