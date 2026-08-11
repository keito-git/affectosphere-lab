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
    date: "2026-08-11",
    label: "Paper",
    body: "A single-author paper was accepted to AI & Society (Springer, IF 6.1).",
    slug: "20260811-ai-society-silos",
    title: "Single-author paper accepted to AI & Society",
    entries: [
      {
        title:
          "Bridging the Silos in Affective AI: A Critical Perspective from Data to Society",
        authors: "Keito Inoshita",
        venue: "AI & Society (Springer)",
        summary:
          "A position paper that reframes affective computing as a six-layer pipeline, diagnoses four recurring silo-bridge disconnections that cascade across it, and proposes five integrated design criteria — situating affective AI as a sociotechnical system that must respect human emotional agency.",
      },
    ],
  },
  {
    date: "2026-08-11",
    label: "Paper",
    body: "Two co-authored papers were accepted to IEEE GCCE 2026.",
    slug: "20260811-gcce2026",
    title: "Two co-authored papers accepted to IEEE GCCE 2026",
    entries: [
      {
        title:
          "Re-Defining Vanishing Municipalities in Japan: A Multidimensional Clustering and SLM-Based Policy Insight Framework",
        authors: "Toma Okugawa, Keito Inoshita",
        venue: "IEEE GCCE 2026",
        summary:
          "A reproducible framework (UBRS) that re-defines Japan's 'vanishing municipalities' beyond a single demographic axis — clustering 1,721 municipalities across 125 indicators (UMAP + HDBSCAN + SHAP) and injecting each cluster profile as RAG context into a locally deployable small language model to generate municipality-tailored policy insights.",
      },
      {
        title:
          "Behavioral Fidelity and Philosophy-Grounded Design for Self-Reflective Conversational AI",
        authors: "Takumi Matsuo, Keito Inoshita",
        venue: "IEEE GCCE 2026",
        summary:
          "Proposes Behavioral Fidelity (BF), a framework that quantifies whether an LLM dialogue agent actually follows its designer-specified behavioral rules — via LLM-as-judge strategy classification, KL-divergence analysis, and sequential constraint checks — and applies it to Mirra, a philosophy-of-language-grounded self-reflection app.",
      },
    ],
  },

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
