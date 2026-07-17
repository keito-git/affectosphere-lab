// Recent news entries shown on Home and in the News timeline.

export type NewsItem = {
  date: string; // ISO YYYY-MM-DD
  label: string;
  body: string;
};

// All news items in reverse-chronological order.  Add new items at the top.
export const allNews: NewsItem[] = [
  {
    date: "2026-08-05",
    label: "Award",
    body: "Received the Grand Prize at the AI Grand Prix (10th Workshop of the Japan Society of Educational Information).",
  },
  {
    date: "2026-07-01",
    label: "Paper",
    body: "Co-authored papers were published in PLOS ONE and the Journal of Plankton Research.",
  },
  {
    date: "2026-05-27",
    label: "Lab",
    body: "Launched the website of the Affectosphere Group.",
  },
  {
    date: "2026-05-24",
    label: "Award",
    body: "Received the Student Award in the Meteorology Task of GeoSciAI2026, hosted by JpGU and JSAI.",
  },
];

// Items rendered on the Home page (top 5 by date).
export const recentNews: NewsItem[] = allNews.slice(0, 5);
