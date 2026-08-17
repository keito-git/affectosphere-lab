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
    date: "2026-08-16",
    label: "論文",
    body: "井下が筆頭の共著論文が IEEE ICDM 2026 (Research Track) に採択されました。",
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
          "感情コンピューティングを6層のパイプラインとして捉え直し、分野を横断して連鎖する4つの断絶（サイロ）を診断し、それらに噛み合う5つの統合的な設計指針を提示する立場表明論文。感情AIを、人間の感情主体性を尊重すべき社会技術システムとして位置づける。",
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
