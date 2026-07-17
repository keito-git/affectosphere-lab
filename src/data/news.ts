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
    label: "受賞",
    body: "日本情報教育学会 第10回研究会「AI Grand Prix」にて大賞を受賞しました。",
  },
  {
    date: "2026-07-01",
    label: "論文",
    body: "共著論文が PLOS ONE および Journal of Plankton Research に掲載されました。",
  },
  {
    date: "2026-05-27",
    label: "ラボ",
    body: "Affectosphere Group のウェブサイトを公開しました。",
  },
  {
    date: "2026-05-24",
    label: "受賞",
    body: "JpGU・JSAI 主催「GeoSciAI2026」気象課題にて学生賞を受賞しました。",
  },
];

// Items rendered on the Home page (top 5 by date).
export const recentNews: NewsItem[] = allNews.slice(0, 5);
