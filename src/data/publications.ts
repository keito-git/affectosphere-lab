// Publications from Affectosphere Group.
//
// All entries are sourced from the principal investigator's master publication
// list (業績リスト_井下敬翔.docx) and re-classified into the kinds below so
// the /publications page can filter by both category and year.

export type PublicationKind =
  | "journal-international"
  | "journal-domestic"
  | "international-conference"
  | "domestic-conference"
  | "preprint"
  | "tech-report"
  | "other";

export type Publication = {
  /** Stable identifier. */
  slug: string;
  title: string;
  /** Free-form venue string. */
  venue: string;
  /** ISO YYYY-MM-DD (year-month-day). Used for ordering & year filter. */
  date: string;
  year: number;
  authors: string;
  kind: PublicationKind;
  /** First-author flag for highlighting. */
  firstAuthor?: boolean;
  /** Optional reviewed/award flag, etc. */
  reviewed?: boolean;
  award?: string;
  /** Lifecycle hint shown next to the venue. */
  status?: string;
  /** Optional external link. */
  href?: string;
};

/** English display label for each publication kind. */
export const kindLabel: Record<PublicationKind, string> = {
  "journal-international": "International Journal",
  "journal-domestic": "Domestic Journal",
  "international-conference": "International Conference",
  "domestic-conference": "Domestic Conference",
  preprint: "Preprint",
  "tech-report": "Technical Report",
  other: "Other",
};

/** Japanese display label (kept for any future i18n switch). */
export const kindLabelJa: Record<PublicationKind, string> = {
  "journal-international": "国際ジャーナル",
  "journal-domestic": "国内ジャーナル",
  "international-conference": "国際会議",
  "domestic-conference": "国内会議",
  preprint: "プレプリント",
  "tech-report": "研究報告",
  other: "その他",
};

/** Ordered list of kinds (used by data consumers if filtering returns). */
export const kindOrder: PublicationKind[] = [
  "journal-international",
  "journal-domestic",
  "international-conference",
  "domestic-conference",
  "preprint",
  "tech-report",
  "other",
];

// All publications, ordered chronologically (newest first).  The raw list
// below is hand-curated; we sort at the bottom of the file so editors can
// keep entries grouped by kind here without breaking display order.
const rawPublications: Publication[] = [
  // ===== 2026 =====
  // ---- Preprint (2026) ----
  {
    slug: "inoshita-name-region-2026",
    title:
      "Nationality and Region Prediction from Names: A Comparative Study of Neural Models and Large Language Models",
    venue: "arXiv",
    date: "2026-04-01",
    year: 2026,
    authors: "Keito Inoshita",
    kind: "preprint",
    firstAuthor: true,
  },
  {
    slug: "inoshita-name-remind-2026",
    title:
      "Who Does This Name Remind You of? Nationality Prediction via Large Language Model Associative Memory",
    venue: "arXiv",
    date: "2026-04-01",
    year: 2026,
    authors: "Keito Inoshita",
    kind: "preprint",
    firstAuthor: true,
  },
  {
    slug: "inoshita-argument-rarity-2026",
    title: "Argument Rarity-based Originality Assessment for AI-Assisted Writing",
    venue: "arXiv",
    date: "2026-02-01",
    year: 2026,
    authors: "Keito Inoshita, Michiaki Omura, Tsukasa Yamanaka, Go Maeda, Kentaro Tsuji",
    kind: "preprint",
    firstAuthor: true,
  },
  {
    slug: "nojiri-etymology-2026",
    title:
      "Unravelling historical, taxonomic, and cultural influences on the etymology of scientific names across Animalia",
    venue: "bioRxiv",
    date: "2026-02-01",
    year: 2026,
    authors: "Kota Nojiri, Keito Inoshita, Haruto Sugeno, Takumi Taga",
    kind: "preprint",
  },
  {
    slug: "inoshita-ai-homogenize-2026",
    title:
      "Does AI Homogenize Student Thinking? A Multi-Dimensional Analysis of Structural Convergence in AI-Augmented Essays",
    venue: "arXiv",
    date: "2026-03-01",
    year: 2026,
    authors: "Keito Inoshita, Michiaki Omura, Tsukasa Yamanaka, Go Maeda, Kentaro Tsuji",
    kind: "preprint",
    firstAuthor: true,
  },
  {
    slug: "inoshita-cognitive-causal-2026",
    title:
      "Cognitive-Causal Multi-Task Learning with Psychological State Conditioning for Assistive Driving Perception",
    venue: "arXiv",
    date: "2026-04-01",
    year: 2026,
    authors: "Keito Inoshita, Nobuhiro Hayashida, Akira Imanishi",
    kind: "preprint",
    firstAuthor: true,
  },
  {
    slug: "inoshita-llm-emotion-uncertainty-2026",
    title:
      "LLMs Capture Emotion Labels, Not Emotion Uncertainty: Distributional Analysis and Calibration of Human-LLM Judgment Gaps",
    venue: "arXiv",
    date: "2026-04-01",
    year: 2026,
    authors: "Keito Inoshita, Xiaokang Zhou, Akira Kawai, Katsutoshi Yada",
    kind: "preprint",
    firstAuthor: true,
  },
  {
    slug: "nojiri-gliding-2026",
    title:
      "Convergent gliding, divergent ecology: Environmental drivers of gliding vertebrates in Southeast Asia",
    venue: "arXiv",
    date: "2026-05-01",
    year: 2026,
    authors: "Kota Nojiri, Haruto Sugeno, Keito Inoshita",
    kind: "preprint",
  },
  {
    slug: "inoshita-affective-silos-2026",
    title:
      "Bridging the Silos in Affective AI: A Critical Perspective from Data to Society",
    venue: "SSRN",
    date: "2026-05-25",
    year: 2026,
    authors: "Keito Inoshita",
    kind: "preprint",
    firstAuthor: true,
  },
  {
    slug: "inoshita-uncertainty-decomp-2026",
    title:
      "Uncertainty Decomposition via Cyclical SG-MCMC and Soft-label Learning for Subjective NLP",
    venue: "arXiv",
    date: "2026-05-01",
    year: 2026,
    authors: "Keito Inoshita, Takato Ueno",
    kind: "preprint",
    firstAuthor: true,
  },
  {
    slug: "inoshita-bayesian-spectral-2026",
    title:
      "Bayesian Spectral Emotion Transition Discovery from Multi-Annotator Disagreement",
    venue: "arXiv",
    date: "2026-05-01",
    year: 2026,
    authors: "Keito Inoshita, Takato Ueno",
    kind: "preprint",
    firstAuthor: true,
  },
  // ---- 国際ジャーナル (2026) ----
  {
    slug: "persona-synthetic-2026",
    title:
      "Persona-Based Synthetic Data Generation Using Multi-Stage Conditioning with Large Language Models for Emotion Recognition",
    venue: "International Journal of Activity and Behavior Computing, vol. 1, pp. 1-18",
    date: "2026-03-01",
    year: 2026,
    authors: "Keito Inoshita, Rushia Harada",
    kind: "journal-international",
    firstAuthor: true,
    reviewed: true,
  },
  {
    slug: "kdda-2026",
    title:
      "KDDA: A Knowledge-Driven Domain and Diversity Alignment Framework for Emotion Data Generation with Large Language Models",
    venue: "International Journal of Activity and Behavior Computing, vol. 1, pp. 1-24",
    date: "2026-03-01",
    year: 2026,
    authors: "Keito Inoshita, Hayato Tomisu, Xiaokang Zhou, Akira Kawai, Katsutoshi Yada",
    kind: "journal-international",
    firstAuthor: true,
    reviewed: true,
  },
  {
    slug: "world-model-sarcasm-2026",
    title: "World model inspired sarcasm reasoning with large language model agents",
    venue: "Discovery Artificial Intelligence",
    date: "2026-06-01",
    year: 2026,
    authors: "Keito Inoshita, Shinnosuke Mizuno",
    kind: "journal-international",
    firstAuthor: true,
  },
  // ---- 国際会議 (2026) ----
  {
    slug: "ieee-zinc-2026",
    title:
      "Multi-Agent Large Language Model Based Emotional Detoxification Through Personalized Intensity Control for Consumer Protection",
    venue: "IEEE ZINC 2026",
    date: "2026-06-01",
    year: 2026,
    authors: "Keito Inoshita",
    kind: "international-conference",
    firstAuthor: true,
  },
  // ---- 国内会議 (2026) ----
  {
    slug: "nlc-2026",
    title: "感情データの構造を補完する内挿・外挿型データ拡張フレームワーク",
    venue: "言語理解とコミュニケーション研究会(NLC)",
    date: "2026-03-01",
    year: 2026,
    authors: "井下敬翔",
    kind: "domestic-conference",
    firstAuthor: true,
  },

  // ===== 2025 =====
  // ---- 国際ジャーナル (2025) ----
  {
    slug: "automated-labeling-2025",
    title:
      "Automated Labeling of Scientific Names and Etymological Trend Analysis in Phytophagous Arthropods Using Large Language Model",
    venue: "Zoological Science, vol. 42, issue 5",
    date: "2025-10-01",
    year: 2025,
    authors: "Kota Nojiri, Keito Inoshita, Haruto Sugeno",
    kind: "journal-international",
    reviewed: true,
  },
  // ---- 国際会議 (2025) ----
  {
    slug: "nldb-2025",
    title:
      "Multi-Scale Convolutional Fusion with Contrastive Feature Alignment for Imbalanced Data Classification",
    venue: "NLDB 2025, vol. 15836",
    date: "2025-07-01",
    year: 2025,
    authors: "Keito Inoshita, Takato Ueno, Xiaokang Zhou",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
    award: "Best Paper Award",
  },
  {
    slug: "ieee-iaict-2025-naming",
    title:
      "Evaluation of the Automated Labeling Method for Taxonomic Nomenclature Through Prompt-Optimized Large Language Model",
    venue: "IEEE IAICT 2025, pp. 528-535",
    date: "2025-07-01",
    year: 2025,
    authors: "Keito Inoshita, Kota Nojiri, Haruto Sugeno, Takumi Taga",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
  },
  {
    slug: "ieee-iaict-2025-sarcasm",
    title:
      "Dual-Branch Feature Extraction via Discrepancy-Aware Fusion with Evidential Deep Learning for Sarcasm Detection",
    venue: "IEEE IAICT 2025, pp. 345-352",
    date: "2025-07-01",
    year: 2025,
    authors: "Takato Ueno, Keito Inoshita",
    kind: "international-conference",
    reviewed: true,
  },
  {
    slug: "ieee-hpcc-2025",
    title:
      "GNN-Enhanced Multimodal Fusion with Contrastive Learning for Smart Health Oriented Food Recommendation System",
    venue: "IEEE HPCC 2025, pp. 864-871",
    date: "2025-08-01",
    year: 2025,
    authors: "Ryutaro Matsuoka, Keito Inoshita, Xiaokang Zhou, Zhigao Zheng, Akira Kawai, Katsutoshi Yada",
    kind: "international-conference",
    reviewed: true,
    award: "Best Paper Award",
  },
  {
    slug: "ieee-icoailo-2025",
    title:
      "Enhancing Sentiment Analysis Accuracy and Evaluating Task Affinity Using Large Language Models",
    venue: "IEEE ICoAILO 2025, pp. 181-187",
    date: "2025-08-01",
    year: 2025,
    authors: "Keito Inoshita",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
    award: "Best Paper Award",
  },
  {
    slug: "ieee-gcce-2025",
    title:
      "Reproducing Developmental Features and Preserving Semantics in Child-Style Text Generation Using LLM",
    venue: "IEEE GCCE 2025",
    date: "2025-09-01",
    year: 2025,
    authors: "Keito Inoshita, Keisuke Motomura, Rushia Harada",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
  },
  {
    slug: "ieee-picom-2025",
    title:
      "A Multi-Agent Probabilistic Inference Framework Inspired by Kairanban-Style CoT System with IdoBata Conversation for Debiasing",
    venue: "IEEE PICom 2025",
    date: "2025-10-01",
    year: 2025,
    authors: "Takato Ueno, Keito Inoshita",
    kind: "international-conference",
    reviewed: true,
  },
  {
    slug: "ai-dhwp-2025",
    title:
      "Role-Playing LLM-Based Multi-Agent Support Framework for Detecting and Addressing Family Communication Bias",
    venue: "AI-DHWP @ CyberSciTech 2025",
    date: "2025-10-01",
    year: 2025,
    authors: "Rushia Harada, Yuken Kimura, Keito Inoshita",
    kind: "international-conference",
    reviewed: true,
  },
  // ---- 国内ジャーナル (2025) ----
  {
    slug: "joho-chishiki-multimodal-2025",
    title: "職場環境におけるマルチモーダル感情認識技術の現状と展望",
    venue: "情報知識学会誌, vol. 35, issue 2, pp. 151-156",
    date: "2025-03-01",
    year: 2025,
    authors: "井下敬翔, 尾崎博信",
    kind: "journal-domestic",
    firstAuthor: true,
  },
  {
    slug: "joho-chishiki-tourism-2025",
    title:
      "京都・滋賀・奈良3府県の観光拠点間における口コミの類似性に着目した観光候補地群の分析",
    venue: "情報知識学会誌, vol. 35, issue 2, pp. 327-333",
    date: "2025-03-01",
    year: 2025,
    authors: "尾崎博信, 井下敬翔",
    kind: "journal-domestic",
  },
  {
    slug: "chikyu-uchu-mirai-2025",
    title: "生成AIを活用した職場感情分析とWell-beingの向上",
    venue: "地球・宇宙・未来, vol. 1, issue 2, pp. 109-114",
    date: "2025-04-01",
    year: 2025,
    authors: "井下敬翔",
    kind: "journal-domestic",
    firstAuthor: true,
  },
  // ---- 国内会議 (2025) ----
  {
    slug: "biology-3gakkai-sugeno-2025",
    title: "学名の裏側をズバリ解明: 魚類と動物プランクトンの語源を大規模言語モデルで探る",
    venue: "2025年度中国四国地区生物系三学会合同大会愛媛大会",
    date: "2025-03-01",
    year: 2025,
    authors: "菅野遥登, 井下敬翔, 野尻康太, 多賀匠",
    kind: "domestic-conference",
  },
  {
    slug: "biology-3gakkai-nojiri-2025",
    title: "大規模言語モデル(LLM)を用いた学名の語源分類と命名傾向の時系列変化",
    venue: "2025年度中国四国地区生物系三学会合同大会愛媛大会",
    date: "2025-03-01",
    year: 2025,
    authors: "野尻康太, 井下敬翔, 菅野遥登",
    kind: "domestic-conference",
  },
  {
    slug: "fit-2025",
    title: "大規模言語モデルは年齢を超えて文体を生成できるか",
    venue: "第24回情報科学技術フォーラム(FIT 2025)",
    date: "2025-09-01",
    year: 2025,
    authors: "井下敬翔",
    kind: "domestic-conference",
    firstAuthor: true,
  },
  {
    slug: "dobutsugakkai-2025",
    title: "学名が語る恣意性: 語源に潜むバイアスの構造を可視化する",
    venue: "日本動物学会 第96回名古屋大会",
    date: "2025-09-01",
    year: 2025,
    authors: "野尻康太, 井下敬翔, 菅野遥登, 多賀匠",
    kind: "domestic-conference",
  },
  {
    slug: "kansei-kogaku-2025",
    title: "言語モデルの児童テキスト分類性能の検証と対処",
    venue: "第27回日本感性工学会大会",
    date: "2025-09-01",
    year: 2025,
    authors: "井下敬翔, 木村裕健, 原田琉碧",
    kind: "domestic-conference",
    firstAuthor: true,
  },
  {
    slug: "ipsj-kansai-2025",
    title: "ペルソナを活用した大規模言語モデルによる感情テキスト生成",
    venue: "2025年度情報処理学会関西支部 支部大会",
    date: "2025-09-01",
    year: 2025,
    authors: "井下敬翔",
    kind: "domestic-conference",
    firstAuthor: true,
  },
  {
    slug: "wakate-symposium-2025",
    title: "属人性を排除した大規模言語モデルによる感情データ生成",
    venue: "第20回言語処理若手シンポジウム",
    date: "2025-09-01",
    year: 2025,
    authors: "井下敬翔",
    kind: "domestic-conference",
    firstAuthor: true,
  },
  {
    slug: "text-analytics-2025",
    title:
      "知識駆動のドメイン調整と多様性の拡張に基づく大規模言語モデルを活用した感情データ生成",
    venue: "第22回テキストアナリティクス・シンポジウム",
    date: "2025-09-01",
    year: 2025,
    authors: "井下敬翔",
    kind: "domestic-conference",
    firstAuthor: true,
  },
  // ---- 研究報告 (2025) ----
  {
    slug: "ipsj-ch-ueno-2025",
    title: "回覧板と井戸端会議に着想を得たマルチエージェント確率的推論フレームワークの検証",
    venue: "研究報告人文科学とコンピュータ(CH), vol. 2025-CH-138, issue 7, pp. 1-6",
    date: "2025-03-01",
    year: 2025,
    authors: "上野孝斗, 井下敬翔",
    kind: "tech-report",
  },
  {
    slug: "ipsj-nl-2025",
    title: "自然言語処理による感情認識技術の研究動向と今後の課題",
    venue: "研究報告自然言語処理, vol. 2025-NL-264, issue 10, pp. 1-6",
    date: "2025-07-01",
    year: 2025,
    authors: "原佑太郎, 井下敬翔",
    kind: "tech-report",
  },
  // ---- Preprint (2025) ----
  {
    slug: "sugeno-bioRxiv-2025",
    title:
      "Introducing Large Language Models to Human-Based Etymological Classification in Zooplankton",
    venue: "bioRxiv",
    date: "2025-05-01",
    year: 2025,
    authors: "Haruto Sugeno, Keito Inoshita, Kota Nojiri",
    kind: "preprint",
  },
  {
    slug: "c-dira-2025",
    title:
      "C-DIRA: Computationally Efficient Dynamic ROI Routing and Domain-Invariant Adversarial Learning for Lightweight Driver Behavior Recognition",
    venue: "arXiv",
    date: "2025-12-01",
    year: 2025,
    authors: "Keito Inoshita",
    kind: "preprint",
    firstAuthor: true,
  },
  {
    slug: "geometric-control-2025",
    title:
      "Geometric Control-Based Data Augmentation with Cluster-Conditioned Interpolation and Extrapolation for Imbalanced Learning in LLM",
    venue: "arXiv",
    date: "2025-12-01",
    year: 2025,
    authors: "Keito Inoshita, Xiaokang Zhou, Akira Kawai, Katsutoshi Yada",
    kind: "preprint",
    firstAuthor: true,
  },
  // ---- その他 (2025) ----
  {
    slug: "rikoukei-essay-2025",
    title: "感情データが導く生成AI時代のWell-beingは職場環境",
    venue: "第25回理工学系学生科学技術論文コンクール入賞論文集",
    date: "2025-03-01",
    year: 2025,
    authors: "井下敬翔",
    kind: "other",
    firstAuthor: true,
  },
  {
    slug: "showa-ikeda-2025",
    title: "大規模言語モデルの政治的影響とガバナンスの指針",
    venue: "第44回学生論文昭和池田賞",
    date: "2025-06-01",
    year: 2025,
    authors: "井下敬翔",
    kind: "other",
    firstAuthor: true,
  },

  // ===== 2024 =====
  // ---- 国際会議 (2024) ----
  {
    slug: "times-icon-2024",
    title: "Assessment of Conflict Structure Recognition and Bias Impact in Japanese LLMs",
    venue: "TIMES-iCON 2024",
    date: "2024-06-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
  },
  {
    slug: "ieee-ithings-2024",
    title:
      "Multi-Domain and Multi-View Oriented Deep Neural Network for Sentiment Analysis in Large Language Models",
    venue: "IEEE iThings 2024, pp. 149-156",
    date: "2024-08-01",
    year: 2024,
    authors: "Keito Inoshita, Xiaokang Zhou, Shohei Shimizu",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
  },
  {
    slug: "icitacee-2024",
    title:
      "Sentiment Analysis of Japanese Twitter Users Regarding the Ukraine-Russia War and Its Implications for Security Policy",
    venue: "ICITACEE 2024, pp. 338-343",
    date: "2024-08-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
    award: "Best Paper Award",
  },
  {
    slug: "diges-grace-2024",
    title:
      "Quantitative Analysis of Political Party Understanding and the Impact of Political Bias through ChatGPT",
    venue: "DiGeS-Grace 2024, pp. 1-11",
    date: "2024-08-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
  },
  {
    slug: "icelitics-2024",
    title:
      "The Efficient Development of Conflict Structure Datasets for Evaluating Sentiment Recognition Bias in Large Language Models",
    venue: "ICELTICs 2024, pp. 7-12",
    date: "2024-09-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
  },
  {
    slug: "ieee-bdcloud-2024",
    title:
      "Sentiment Bias and Security Analysis in Training Datasets of Large Language Models",
    venue: "IEEE BDCloud 2024, pp. 1-8",
    date: "2024-10-01",
    year: 2024,
    authors: "Keito Inoshita, Xiaokang Zhou",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
    award: "Best Paper Award",
  },
  {
    slug: "nlp4dh-emnlp-2024",
    title:
      "Corpus Development Based on Conflict Structures in the Security Field and LLM Bias Verification",
    venue: "NLP4DH @ EMNLP 2024, pp. 504-512",
    date: "2024-11-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
  },
  {
    slug: "ieee-iotais-2024-evolutionary",
    title:
      "Evolutionary Expert Model Merging with Task-Adaptive Iterative Self-Improvement Process for Large Language Modeling on Aspect-Based Sentiment Analysis",
    venue: "IEEE IoTaIS 2024, pp. 130-136",
    date: "2024-11-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
    award: "Best Paper Award",
  },
  {
    slug: "ieee-iotais-2024-multifaceted",
    title:
      "Multifaceted Exploration of Perceptions on the Ukraine-Russia War in the Japanese Twitter Space",
    venue: "IEEE IoTaIS 2024, pp. 58-64",
    date: "2024-11-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
  },
  {
    slug: "3ict-2024",
    title: "Assessing GPT's Legal Knowledge in Japanese Real Estate Transactions Exam",
    venue: "3ICT 2024, pp. 149-155",
    date: "2024-11-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
  },
  {
    slug: "ieee-dss-2024",
    title:
      "Multi-Stage Evolutionary Model Merging with Meta Data Driven Curriculum Learning for Sentiment-Specialized Large Language Modeling",
    venue: "IEEE DSS 2024, pp. 58-65",
    date: "2024-12-01",
    year: 2024,
    authors: "Keito Inoshita, Xiaokang Zhou, Akira Kawai",
    kind: "international-conference",
    firstAuthor: true,
    reviewed: true,
    award: "Best Paper Award",
  },
  // ---- 国内会議 (2024) ----
  {
    slug: "jinmoncon-2024",
    title:
      "Bias Examination of International Conflict Structures in Large Language Models and Debiasing Methods Based on Active and Passive Approaches",
    venue: "じんもんこん2024論文集, vol. 2024, pp. 167-174",
    date: "2024-12-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "domestic-conference",
    firstAuthor: true,
    reviewed: true,
  },
  // ---- 研究報告 (2024) ----
  {
    slug: "ipsj-ch-2024-1",
    title:
      "日本語Twitter空間における戦争認識の多角的探索: ウクライナ-ロシア戦争への反応と洞察",
    venue: "研究報告人文科学とコンピュータ(CH), vol. 2024-CH-135, issue 1, pp. 1-8",
    date: "2024-03-01",
    year: 2024,
    authors: "井下敬翔",
    kind: "tech-report",
    firstAuthor: true,
  },
  {
    slug: "ipsj-ch-2024-2",
    title:
      "A Novel Dataset Development Method for Evaluating Sentiment Recognition Bias of Large Language Models in Conflict Structures",
    venue: "研究報告人文科学とコンピュータ(CH), vol. 2024-CH-136, issue 2, pp. 1-4",
    date: "2024-07-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "tech-report",
    firstAuthor: true,
  },
  // ---- その他 (2024) ----
  {
    slug: "nuclear-opinion-2024",
    title: "核兵器に頼る国のリーダーへ: リアリズムと革新による平和への道",
    venue: "「核なき未来」オピニオン",
    date: "2024-01-01",
    year: 2024,
    authors: "井下敬翔",
    kind: "other",
    firstAuthor: true,
  },
  {
    slug: "hito-shigoto-2024",
    title: "パーソナルAIと組織AIによる人事管理の革新と最適化",
    venue: "人と仕事の未来研究所第1回懸賞論文",
    date: "2024-01-01",
    year: 2024,
    authors: "井下敬翔",
    kind: "other",
    firstAuthor: true,
  },
  {
    slug: "taiku-shisetsu-2024",
    title: "スポーツの小型化とモジュール型小規模競技場によるウェルビーイングな都市デザイン",
    venue: "月刊体育施設12月号, pp. 43-44",
    date: "2024-12-01",
    year: 2024,
    authors: "井下敬翔",
    kind: "other",
  },
  {
    slug: "shakai-kyoiku-2024",
    title: "スポーツの小型化とモジュール型小規模競技場によるウェルビーイングな都市デザイン",
    venue: "社会教育, vol. 44, issue 45, pp. 43-44",
    date: "2024-01-01",
    year: 2024,
    authors: "井下敬翔",
    kind: "other",
  },
];

// Sorted master list (newest first).  Re-used by all helpers below.
export const allPublications: Publication[] = [...rawPublications].sort(
  (a, b) => b.date.localeCompare(a.date)
);

// Recent items shown on the Home page (top 5 by activity).
export const recentPublications: Publication[] = allPublications.slice(0, 5);

// ---------------------------------------------------------------------------
// Helpers used by the /publications page.
// ---------------------------------------------------------------------------

/** Sorted list of all years present in the publication list (descending). */
export const allYears: number[] = Array.from(
  new Set(allPublications.map((p) => p.year))
).sort((a, b) => b - a);

/** Group publications by year (descending) → entries in original order. */
export function groupByYear(
  pubs: Publication[]
): { year: number; items: Publication[] }[] {
  const byYear = new Map<number, Publication[]>();
  for (const p of pubs) {
    if (!byYear.has(p.year)) byYear.set(p.year, []);
    byYear.get(p.year)!.push(p);
  }
  return Array.from(byYear.entries())
    .sort((a, b) => b[0] - a[0])
    .map(([year, items]) => ({ year, items }));
}

/** Format ISO date as Japanese-style "2026年5月". */
export function formatDateJa(iso: string): string {
  const [y, m] = iso.split("-");
  return `${y}年${Number(m)}月`;
}
