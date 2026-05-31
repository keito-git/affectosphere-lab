// Awards & honors received by the PI.  Two top-level groups: research awards
// (papers, conferences) and contest / academic awards (idea contests,
// scholarships, etc.).  Each entry carries a date so the list can be ordered
// chronologically.  Paper-related awards also embed the cited paper title
// and authors for context.  Sourced from 業績リスト_井下敬翔.docx.

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

// Helper: URL-encode a Japanese-named asset under /award-images/.
const certImg = (filename: string): string =>
  `/award-images/${encodeURIComponent(filename)}`;

export type AwardGroup = {
  key: string;
  label: string;
  items: Award[];
};

const _rawResearch: Award[] = [
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
    title: "人と仕事の未来研究所 第1回懸賞論文",
    rank: "奨励賞",
    date: "2024-12-01",
    paperTitle: "パーソナルAIと組織AIによる人事管理の革新と最適化",
    paperAuthors: "井下敬翔",
    image: certImg("マーサージャパン懸賞論文.jpg"),
  },
  {
    title: "第25回 理工系学生科学技術論文コンクール",
    rank: "入賞",
    date: "2025-03-01",
    paperTitle: "感情データが導く生成AI時代のWell-beingは職場環境",
    paperAuthors: "井下敬翔",
    image: certImg("理工系学生科学技術論文コンクール.jpg"),
  },
  {
    title: "第44回 学生論文昭和池田賞",
    rank: "特別奨励賞",
    date: "2025-06-01",
    paperTitle: "大規模言語モデルの政治的影響とガバナンスの指針",
    paperAuthors: "井下敬翔",
    image: certImg("2025昭和池田賞.jpg"),
  },
  {
    title: "2025年度 情報処理学会関西支部 支部大会",
    rank: "支部大会奨励賞",
    date: "2025-09-01",
    paperTitle: "ペルソナを活用した大規模言語モデルによる感情テキスト生成",
    paperAuthors: "井下敬翔",
    image: certImg("2025情報処理学会関西支部奨励賞.jpg"),
  },
  {
    title: "関西大学 第4回院生合同学術研究ポスター発表大会",
    rank: "優秀賞",
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
  { title: "第2回 高速道路DXアイデアコンテスト", rank: "優秀賞", date: "2024-01-01" },
  {
    title: "水地域イノベーション財団 2024年度支援事業ビジネスプランコンテスト",
    rank: "採択",
    date: "2024-01-01",
    image: certImg("「しま」のビジネスチャレンジ賞.jpg"),
  },
  {
    title: "メ〜テレ(名古屋テレビ放送株式会社)主催アイデアコンテスト",
    rank: "最優秀賞・小島プレス工業テーマ賞",
    date: "2024-01-01",
  },
  {
    title: "IEEE R10 Ethics and Enterprise Risk Management Committee Student Contest",
    rank: "アジア3位",
    date: "2024-01-01",
    image: certImg("ERMコンテスト賞状.png"),
  },
  { title: "学生 ACTION CAMP 2024", rank: "採用", date: "2024-01-01" },
  {
    title: "関西大学ビジネスプラン・コンペティション(KUBIC)",
    rank: "優秀賞",
    date: "2024-01-01",
    image: certImg("関西大学KUBIC賞状.png"),
  },
  {
    title: "NEC Analytics Challenge Cup for Business Idea 2024",
    rank: "最優秀賞",
    date: "2024-01-01",
    image: certImg("NECビジコン.jpg"),
  },
  { title: "Panda杯 全日本青年作文コンクール 2024", rank: "優秀賞", date: "2024-01-01" },
  {
    title: "スポーツ・健康まちづくりデザイン学生コンペティション 2024",
    rank: "スポーツ庁長官賞",
    date: "2024-01-01",
    image: certImg("スポーツ庁コンテスト.jpg"),
  },
  {
    title: "APEV「モビリティで2030を創る」国際ワークショップ",
    rank: "環境大臣賞",
    date: "2024-01-01",
    image: certImg("APEVコンテスト.jpg"),
  },
  {
    title: "夢をつくるプロジェクト 2024",
    rank: "優秀賞",
    date: "2024-01-01",
    image: certImg("夢をつくるプロジェクト.jpg"),
  },
  {
    title: "岡山ガス ビジネスプランコンテスト 2024",
    rank: "エシカル・データ賞",
    date: "2024-01-01",
    image: certImg("岡山ガスビジネスプランコンテスト.jpg"),
  },
  {
    title: "LOD チャレンジ 2024",
    rank: "AI賞",
    date: "2024-01-01",
    image: certImg("LODコンテスト.jpg"),
  },
  {
    title: "KINTO未来ファンド賞",
    rank: "採択",
    date: "2024-01-01",
    image: certImg("KINTO未来ファンド賞状.jpg"),
  },
  {
    title: "第2回 西播磨ビジネスコンテスト",
    rank: "優秀賞",
    date: "2024-01-01",
    image: certImg("西播磨ビジネスコンテスト.jpg"),
  },
  { title: "武蔵大学ビジネスプランコンテスト", rank: "審査員特別賞", date: "2024-01-01" },
  {
    title: "滋賀大学 学長賞",
    date: "2024-01-01",
    image: certImg("滋賀大学学長賞.jpg"),
  },
  { title: "ISUZU AI Innovation Challenge 2024", rank: "奨励賞", date: "2024-01-01" },
  { title: "関西大学 SFinX", rank: "優秀賞・協賛企業賞", date: "2024-01-01" },
  {
    title: "〜未踏的な地方の若手人材発掘育成事業〜 LEADING EDGE 四国",
    rank: "採択",
    date: "2025-08-01",
  },
  { title: "第3回 鉄道150年記念障害福祉賞", rank: "第2位", date: "2024-01-01" },
  { title: "イチBizアワード", rank: "優秀賞", date: "2024-01-01" },
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
