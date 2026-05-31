// Recent news entries shown on Home and in the News timeline.

export type NewsItem = {
  date: string; // ISO YYYY-MM-DD
  label: string;
  body: string;
};

// All news items in reverse-chronological order.  Add new items at the top.
export const allNews: NewsItem[] = [
  {
    date: "2026-05-27",
    label: "Lab",
    body: "Launched the website of the Affectosphere Group.",
  },
];

// Items rendered on the Home page (top 5 by date).
export const recentNews: NewsItem[] = allNews.slice(0, 5);
