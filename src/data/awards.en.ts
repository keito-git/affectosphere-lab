// Awards & honors received by the PI. Two top-level groups: research awards
// (papers, conferences) and contest / academic awards (idea contests,
// scholarships, etc.). Each entry carries a date so the list can be ordered
// chronologically. Paper-related awards also embed the cited paper title
// and authors for context. Sourced from the PI's CV.

export type Award = {
  title: string;
  /** Display label for the rank/category (e.g., "Best Paper Award"). */
  rank?: string;
  /** ISO YYYY-MM-DD (year + month, day defaults to 01). */
  date: string;
  /** For paper awards: the actual paper title. */
  paperTitle?: string;
  /** For paper awards: the author list as it appears in the publication. */
  paperAuthors?: string;
  /** Optional certificate / photo image (already URL-encoded). */
  image?: string;
};

// Helper: URL-encode an asset under /award-images/.
const certImg = (filename: string): string =>
  `/award-images/${encodeURIComponent(filename)}`;

export type AwardGroup = {
  key: string;
  label: string;
  items: Award[];
};

const _rawResearch: Award[] = [
  {
    title: "GeoSciAI2026 (Geoscience Data AI Modeling Competition — Meteorology Task)",
    rank: "Student Award",
    date: "2026-05-24",
  },
  {
    title: "ICITACEE 2024",
    rank: "Best Paper Award",
    date: "2024-08-01",
    paperTitle:
      "Sentiment Analysis of Japanese Twitter Users Regarding the Ukraine-Russia War and Its Implications for Security Policy",
    paperAuthors: "Keito Inoshita",
    image: certImg("ICITACEE-Best-Paper-Award.png"),
  },
  {
    title: "IEEE BDCloud 2024",
    rank: "Best Paper Award",
    date: "2024-10-01",
    paperTitle:
      "Sentiment Bias and Security Analysis in Training Datasets of Large Language Models",
    paperAuthors: "Keito Inoshita, Xiaokang Zhou",
    image: certImg("IEEEBDCloud.jpg"),
  },
  {
    title: "IEEE IoTaIS 2024",
    rank: "Best Paper Award",
    date: "2024-11-01",
    paperTitle:
      "Evolutionary Expert Model Merging with Task-Adaptive Iterative Self-Improvement Process for Large Language Modeling on Aspect-Based Sentiment Analysis",
    paperAuthors: "Keito Inoshita",
    image: certImg("IEEE-IoTaIS-Best-Paper-Award.png"),
  },
  {
    title: "IEEE DSS 2024",
    rank: "Best Paper Award",
    date: "2024-12-01",
    paperTitle:
      "Multi-Stage Evolutionary Model Merging with Meta Data Driven Curriculum Learning for Sentiment-Specialized Large Language Modeling",
    paperAuthors: "Keito Inoshita, Xiaokang Zhou, Akira Kawai",
    image: certImg("IEEE-DSS-Best-Paper-Award.jpg"),
  },
  {
    title: "NLDB 2025",
    rank: "Best Paper Award",
    date: "2025-07-01",
    paperTitle:
      "Multi-Scale Convolutional Fusion with Contrastive Feature Alignment for Imbalanced Data Classification",
    paperAuthors: "Keito Inoshita, Takato Ueno, Xiaokang Zhou",
    image: certImg("NLDB_BestPaperAward.jpg"),
  },
  {
    title: "IEEE ICoAILO 2025",
    rank: "Best Paper Award",
    date: "2025-08-01",
    paperTitle:
      "Enhancing Sentiment Analysis Accuracy and Evaluating Task Affinity Using Large Language Models",
    paperAuthors: "Keito Inoshita",
    image: certImg("IEEE-ICoAILO-Best-Paper-Award.jpg"),
  },
  {
    title: "IEEE HPCC 2025",
    rank: "Best Paper Award",
    date: "2025-08-01",
    paperTitle:
      "GNN-Enhanced Multimodal Fusion with Contrastive Learning for Smart Health Oriented Food Recommendation System",
    paperAuthors:
      "Ryutaro Matsuoka, Keito Inoshita, Xiaokang Zhou, Zhigao Zheng, Akira Kawai, Katsutoshi Yada",
    image: certImg("IEEE-HPCC-Best-Paper-Award.jpg"),
  },
  {
    title: "Institute for the Future of People and Work, 1st Prize Essay Contest",
    rank: "Encouragement Award",
    date: "2024-12-01",
    paperTitle:
      "Innovation and Optimization of Human Resource Management through Personal AI and Organizational AI",
    paperAuthors: "Keito Inoshita",
    image: certImg("マーサージャパン懸賞論文.jpg"),
  },
  {
    title: "25th Science and Technology Paper Contest for Science and Engineering Students",
    rank: "Award Winner",
    date: "2025-03-01",
    paperTitle:
      "Workplace Environment for Well-being in the Generative AI Era Guided by Emotion Data",
    paperAuthors: "Keito Inoshita",
    image: certImg("理工系学生科学技術論文コンクール.jpg"),
  },
  {
    title: "44th Showa Ikeda Prize for Student Papers",
    rank: "Special Encouragement Award",
    date: "2025-06-01",
    paperTitle:
      "Political Influence of Large Language Models and Guidelines for Governance",
    paperAuthors: "Keito Inoshita",
    image: certImg("2025昭和池田賞.jpg"),
  },
  {
    title: "IPSJ Kansai Branch Conference 2025",
    rank: "Branch Conference Encouragement Award",
    date: "2025-09-01",
    paperTitle:
      "Emotional Text Generation by Large Language Models Using Personas",
    paperAuthors: "Keito Inoshita",
    image: certImg("2025情報処理学会関西支部奨励賞.jpg"),
  },
  {
    title: "Kansai University 4th Joint Graduate Student Academic Research Poster Presentation",
    rank: "Excellence Award",
    date: "2025-08-01",
  },
  {
    title: "IEEE CyberScieTech / DASC / PICom / CBDCom 2025",
    rank: "Excellent Supporter Award",
    date: "2025-10-01",
    image: certImg(
      "IEEE-CyberScieTech-DASC-PICom-CBDCom-2025-Excellent-Supporter-Award.jpg"
    ),
  },
];

const _rawContest: Award[] = [
  {
    title: "AI Grand Prix (10th Workshop, Japan Society of Educational Information)",
    rank: "Grand Prize",
    date: "2026-08-01",
  },
  {
    title: "2nd Expressway DX Idea Contest",
    rank: "Excellence Award",
    date: "2024-01-01",
  },
  {
    title: "Water Region Innovation Foundation 2024 Business Plan Contest",
    rank: "Adopted",
    date: "2024-01-01",
    image: certImg("「しま」のビジネスチャレンジ賞.jpg"),
  },
  {
    title: "Idea Contest hosted by Nagoya TV Broadcasting Co., Ltd. (Mete-le)",
    rank: "Grand Prize / Kojima Press Industry Theme Award",
    date: "2024-01-01",
  },
  {
    title: "IEEE R10 Ethics and Enterprise Risk Management Committee Student Contest",
    rank: "3rd Place in Asia",
    date: "2024-01-01",
    image: certImg("ERMコンテスト賞状.png"),
  },
  {
    title: "Student ACTION CAMP 2024",
    rank: "Adopted",
    date: "2024-01-01",
  },
  {
    title: "Kansai University Business Plan Competition (KUBIC)",
    rank: "Excellence Award",
    date: "2024-01-01",
    image: certImg("関西大学KUBIC賞状.png"),
  },
  {
    title: "NEC Analytics Challenge Cup for Business Idea 2024",
    rank: "Grand Prize",
    date: "2024-01-01",
    image: certImg("NECビジコン.jpg"),
  },
  {
    title: "Panda Cup All-Japan Youth Essay Contest 2024",
    rank: "Excellence Award",
    date: "2024-01-01",
  },
  {
    title: "Sports and Health Community Design Student Competition 2024",
    rank: "Commissioner of the Japan Sports Agency Award",
    date: "2024-01-01",
    image: certImg("スポーツ庁コンテスト.jpg"),
  },
  {
    title: "APEV International Workshop: Creating 2030 with Mobility",
    rank: "Minister of the Environment Award",
    date: "2024-01-01",
    image: certImg("APEVコンテスト.jpg"),
  },
  {
    title: "Dream Creation Project 2024",
    rank: "Excellence Award",
    date: "2024-01-01",
    image: certImg("夢をつくるプロジェクト.jpg"),
  },
  {
    title: "Okayama Gas Business Plan Contest 2024",
    rank: "Ethical Data Award",
    date: "2024-01-01",
    image: certImg("岡山ガスビジネスプランコンテスト.jpg"),
  },
  {
    title: "LOD Challenge 2024",
    rank: "AI Award",
    date: "2024-01-01",
    image: certImg("LODコンテスト.jpg"),
  },
  {
    title: "KINTO Future Fund Award",
    rank: "Adopted",
    date: "2024-01-01",
    image: certImg("KINTO未来ファンド賞状.jpg"),
  },
  {
    title: "2nd Nishi-Harima Business Contest",
    rank: "Excellence Award",
    date: "2024-01-01",
    image: certImg("西播磨ビジネスコンテスト.jpg"),
  },
  {
    title: "Musashi University Business Plan Contest",
    rank: "Judges' Special Award",
    date: "2024-01-01",
  },
  {
    title: "Shiga University President's Award",
    date: "2024-01-01",
    image: certImg("滋賀大学学長賞.jpg"),
  },
  {
    title: "ISUZU AI Innovation Challenge 2024",
    rank: "Encouragement Award",
    date: "2024-01-01",
  },
  {
    title: "Kansai University SFinX",
    rank: "Excellence Award / Sponsor Company Award",
    date: "2024-01-01",
  },
  {
    title: "LEADING EDGE Shikoku — Unexplored Regional Young Talent Discovery and Development Program",
    rank: "Adopted",
    date: "2025-08-01",
  },
  {
    title: "3rd Railway 150th Anniversary Disability Welfare Award",
    rank: "2nd Place",
    date: "2024-01-01",
  },
  {
    title: "Ichi-Biz Award",
    rank: "Excellence Award",
    date: "2024-01-01",
  },
];

const byDateDesc = (a: Award, b: Award) => b.date.localeCompare(a.date);

export const awardGroups: AwardGroup[] = [
  {
    key: "research",
    label: "Research Awards",
    items: [..._rawResearch].sort(byDateDesc),
  },
  {
    key: "contest",
    label: "Contest & Academic Awards",
    items: [..._rawContest].sort(byDateDesc),
  },
];

/** All awards merged & sorted chronologically (newest first). */
export const allAwards: Award[] = [..._rawResearch, ..._rawContest].sort(
  byDateDesc
);

export const totalAwards = allAwards.length;
