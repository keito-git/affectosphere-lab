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
    body: "共著論文が PLOS ONE および Journal of Plankton Research に掲載されました。",
    slug: "20260701-papers-plosone-jpr",
    title: "共著論文2本が PLOS ONE / Journal of Plankton Research に掲載",
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
