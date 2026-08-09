// Recent news entries shown on Home and in the News timeline (English).
// Each item can have a detail page at /en/news/{slug}/ (see src/pages/en/news/[slug].astro).

export type NewsEntry = {
  title: string;
  authors?: string;
  venue: string;
  summary?: string;
  href?: string;
};

export type NewsItem = {
  date: string; // ISO YYYY-MM-DD
  label: string;
  body: string;
  slug?: string;
  title?: string;
  summary?: string;
  entries?: NewsEntry[];
  links?: { label: string; url: string }[];
};

// All news items in reverse-chronological order.  Add new items at the top.
export const allNews: NewsItem[] = [
  {
    date: "2026-08-05",
    label: "Award",
    body: "Received the Grand Prize at the AI Grand Prix (10th Workshop of the Japan Society of Educational Information).",
    slug: "20260805-ai-grand-prix",
    title: "Grand Prize at the AI Grand Prix",
    summary:
      "We received the Grand Prize at the AI Grand Prix, held at the 10th Workshop of the Japan Society of Educational Information.",
  },
  {
    date: "2026-07-01",
    label: "Paper",
    body: "Co-authored papers were published in PLOS ONE and the Journal of Plankton Research.",
    slug: "20260701-papers-plosone-jpr",
    title: "Two co-authored papers published in PLOS ONE / Journal of Plankton Research",
    entries: [
      {
        title:
          "Historical, taxonomic, and cultural patterns in scientific naming across Animalia",
        authors: "Kota Nojiri, Keito Inoshita, Haruto Sugeno, Takumi Taga",
        venue: "PLOS ONE",
        summary:
          "A large-scale analysis of the historical, taxonomic, and cultural patterns in the etymology of scientific names across the animal kingdom.",
      },
      {
        title:
          "Applying large language models to expert-based etymological classification in zooplankton",
        authors: "Haruto Sugeno, Keito Inoshita, Kota Nojiri",
        venue: "Journal of Plankton Research",
        summary:
          "A study applying large language models to support expert-based etymological classification of zooplankton.",
      },
    ],
  },
  {
    date: "2026-05-27",
    label: "Lab",
    body: "Launched the website of the Affectosphere Group.",
    slug: "20260527-website-launch",
    title: "Affectosphere Group website launched",
    summary:
      "We launched the website of the Affectosphere Group, sharing our research on affective AI (affective computing).",
  },
  {
    date: "2026-05-24",
    label: "Award",
    body: "Received the Student Award in the Meteorology Task of GeoSciAI2026, hosted by JpGU and JSAI.",
    slug: "20260524-geosciai-meteorology",
    title: "Student Award in the Meteorology Task of GeoSciAI2026",
    summary:
      "We received the Student Award in the Meteorology Task of GeoSciAI2026, hosted by the Japan Geoscience Union (JpGU) and the Japanese Society for Artificial Intelligence (JSAI).",
  },
];

// Items rendered on the Home page (top 5 by date).
export const recentNews: NewsItem[] = allNews.slice(0, 5);
