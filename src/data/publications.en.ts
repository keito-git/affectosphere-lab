// Publications from Affectosphere Group.
//
// All entries are sourced from the principal investigator's master publication
// list (Publication_List_Keito_Inoshita.docx) and re-classified into the kinds
// below so the /publications page can filter by both category and year.

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
  "journal-international": "International Journal",
  "journal-domestic": "Domestic Journal",
  "international-conference": "International Conference",
  "domestic-conference": "Domestic Conference",
  preprint: "Preprint",
  "tech-report": "Technical Report",
  other: "Other",
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
      "Historical, taxonomic, and cultural patterns in scientific naming across Animalia",
    venue: "PLOS ONE",
    date: "2026-07-01",
    year: 2026,
    authors: "Kota Nojiri, Keito Inoshita, Haruto Sugeno, Takumi Taga",
    kind: "journal-international",
    reviewed: true,
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
  {
    slug: "inoshita-driver-intervention-2026",
    title:
      "Safety-Aware Evaluation of LLM-Generated Driver Intervention Messages through Multi-Task Risk Fusion",
    venue: "arXiv",
    date: "2026-06-01",
    year: 2026,
    authors: "Keito Inoshita",
    kind: "preprint",
    firstAuthor: true,
  },
  {
    slug: "inoshita-uncertainty-routing-2026",
    title:
      "Interpretable Uncertainty Routing Separating Emotion Ambiguity from Distribution Shift in Facial Expression Recognition",
    venue: "arXiv",
    date: "2026-06-01",
    year: 2026,
    authors: "Keito Inoshita, Takato Ueno",
    kind: "preprint",
    firstAuthor: true,
  },
  {
    slug: "inoshita-affective-sovereignty-2026",
    title:
      "Who Determines the Meaning of an Emotion? Affective Sovereignty as an Epistemic Consequence of Measurement Limits",
    venue: "arXiv",
    date: "2026-07-01",
    year: 2026,
    authors: "Keito Inoshita",
    kind: "preprint",
    firstAuthor: true,
  },
  // ---- International Journal (2026) ----
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
    venue: "Discovery Artificial Intelligence, vol. 6, no. 606",
    date: "2026-05-01",
    year: 2026,
    authors: "Keito Inoshita, Shinnosuke Mizuno",
    kind: "journal-international",
    firstAuthor: true,
  },
  // ---- International Conference (2026) ----
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
  // ---- Domestic Conference (2026) ----
  {
    slug: "nlc-2026",
    title: "Interpolation- and Extrapolation-Based Data Augmentation Framework for Complementing the Structure of Emotion Data",
    venue: "IEICE Technical Committee on Natural Language Understanding and Communication (NLC)",
    date: "2026-03-01",
    year: 2026,
    authors: "Keito Inoshita",
    kind: "domestic-conference",
    firstAuthor: true,
  },

  // ===== 2025 =====
  // ---- International Journal (2025) ----
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
  // ---- International Conference (2025) ----
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
  // ---- Domestic Journal (2025) ----
  {
    slug: "joho-chishiki-multimodal-2025",
    title: "Current State and Prospects of Multimodal Emotion Recognition Technology in Workplace Environments",
    venue: "Journal of the Japan Society of Information and Knowledge, vol. 35, issue 2, pp. 151-156",
    date: "2025-03-01",
    year: 2025,
    authors: "Keito Inoshita, Hironobu Ozaki",
    kind: "journal-domestic",
    firstAuthor: true,
  },
  {
    slug: "joho-chishiki-tourism-2025",
    title:
      "Analysis of Candidate Tourist Area Groups Focusing on Review Similarities among Tourist Sites across Kyoto, Shiga, and Nara Prefectures",
    venue: "Journal of the Japan Society of Information and Knowledge, vol. 35, issue 2, pp. 327-333",
    date: "2025-03-01",
    year: 2025,
    authors: "Hironobu Ozaki, Keito Inoshita",
    kind: "journal-domestic",
  },
  {
    slug: "chikyu-uchu-mirai-2025",
    title: "Workplace Emotion Analysis and Well-being Improvement Using Generative AI",
    venue: "Earth, Space, and Future, vol. 1, issue 2, pp. 109-114",
    date: "2025-04-01",
    year: 2025,
    authors: "Keito Inoshita",
    kind: "journal-domestic",
    firstAuthor: true,
  },
  // ---- Domestic Conference (2025) ----
  {
    slug: "biology-3gakkai-sugeno-2025",
    title: "Unveiling the Stories Behind Scientific Names: Exploring the Etymology of Fish and Zooplankton with Large Language Models",
    venue: "2025 Joint Meeting of the Three Biological Societies in the Chugoku-Shikoku Region, Ehime Conference",
    date: "2025-03-01",
    year: 2025,
    authors: "Haruto Sugeno, Keito Inoshita, Kota Nojiri, Takumi Taga",
    kind: "domestic-conference",
  },
  {
    slug: "biology-3gakkai-nojiri-2025",
    title: "Etymological Classification of Scientific Names and Temporal Changes in Naming Trends Using Large Language Models (LLMs)",
    venue: "2025 Joint Meeting of the Three Biological Societies in the Chugoku-Shikoku Region, Ehime Conference",
    date: "2025-03-01",
    year: 2025,
    authors: "Kota Nojiri, Keito Inoshita, Haruto Sugeno",
    kind: "domestic-conference",
  },
  {
    slug: "fit-2025",
    title: "Can Large Language Models Generate Writing Styles Across Different Ages?",
    venue: "The 24th Forum on Information Technology (FIT 2025)",
    date: "2025-09-01",
    year: 2025,
    authors: "Keito Inoshita",
    kind: "domestic-conference",
    firstAuthor: true,
  },
  {
    slug: "dobutsugakkai-2025",
    title: "The Arbitrariness Revealed by Scientific Names: Visualizing the Structure of Bias Hidden in Etymology",
    venue: "The 96th Meeting of the Zoological Society of Japan, Nagoya",
    date: "2025-09-01",
    year: 2025,
    authors: "Kota Nojiri, Keito Inoshita, Haruto Sugeno, Takumi Taga",
    kind: "domestic-conference",
  },
  {
    slug: "kansei-kogaku-2025",
    title: "Verification and Mitigation of Language Models' Classification Performance on Child-Authored Text",
    venue: "The 27th Annual Conference of the Japan Society of Kansei Engineering",
    date: "2025-09-01",
    year: 2025,
    authors: "Keito Inoshita, Yuken Kimura, Rushia Harada",
    kind: "domestic-conference",
    firstAuthor: true,
  },
  {
    slug: "ipsj-kansai-2025",
    title: "Persona-Based Emotional Text Generation Using Large Language Models",
    venue: "2025 IPSJ Kansai Branch Conference",
    date: "2025-09-01",
    year: 2025,
    authors: "Keito Inoshita",
    kind: "domestic-conference",
    firstAuthor: true,
  },
  {
    slug: "wakate-symposium-2025",
    title: "Emotion Data Generation Using Large Language Models with Reduced Annotator Dependency",
    venue: "The 20th Symposium for Young Researchers in Natural Language Processing",
    date: "2025-09-01",
    year: 2025,
    authors: "Keito Inoshita",
    kind: "domestic-conference",
    firstAuthor: true,
  },
  {
    slug: "text-analytics-2025",
    title:
      "Emotion Data Generation Using Large Language Models Based on Knowledge-Driven Domain Adjustment and Diversity Expansion",
    venue: "The 22nd Text Analytics Symposium",
    date: "2025-09-01",
    year: 2025,
    authors: "Keito Inoshita",
    kind: "domestic-conference",
    firstAuthor: true,
  },
  // ---- Technical Report (2025) ----
  {
    slug: "ipsj-ch-ueno-2025",
    title: "Verification of a Multi-Agent Probabilistic Inference Framework Inspired by Kairanban and IdoBata Conversation",
    venue: "IPSJ SIG Technical Report on Computers and the Humanities (CH), vol. 2025-CH-138, issue 7, pp. 1-6",
    date: "2025-03-01",
    year: 2025,
    authors: "Takato Ueno, Keito Inoshita",
    kind: "tech-report",
  },
  {
    slug: "ipsj-nl-2025",
    title: "Research Trends and Future Challenges in Emotion Recognition Technology Using Natural Language Processing",
    venue: "IPSJ SIG Technical Report on Natural Language Processing, vol. 2025-NL-264, issue 10, pp. 1-6",
    date: "2025-07-01",
    year: 2025,
    authors: "Yutaro Hara, Keito Inoshita",
    kind: "tech-report",
  },
  // ---- Preprint (2025) ----
  {
    slug: "sugeno-plankton-2026",
    title:
      "Applying large language models to expert-based etymological classification in zooplankton",
    venue: "Journal of Plankton Research",
    date: "2026-07-01",
    year: 2026,
    authors: "Haruto Sugeno, Keito Inoshita, Kota Nojiri",
    kind: "journal-international",
    reviewed: true,
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
  // ---- Other (2025) ----
  {
    slug: "rikoukei-essay-2025",
    title: "Emotion Data Guides Workplace Well-being in the Era of Generative AI",
    venue: "Proceedings of the 25th Science and Engineering Students' Science and Technology Paper Contest",
    date: "2025-03-01",
    year: 2025,
    authors: "Keito Inoshita",
    kind: "other",
    firstAuthor: true,
  },
  {
    slug: "showa-ikeda-2025",
    title: "Political Influence of Large Language Models and Guidelines for Governance",
    venue: "The 44th Showa Ikeda Award for Student Papers",
    date: "2025-06-01",
    year: 2025,
    authors: "Keito Inoshita",
    kind: "other",
    firstAuthor: true,
  },

  // ===== 2024 =====
  // ---- International Conference (2024) ----
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
  // ---- Domestic Conference (2024) ----
  {
    slug: "jinmoncon-2024",
    title:
      "Bias Examination of International Conflict Structures in Large Language Models and Debiasing Methods Based on Active and Passive Approaches",
    venue: "Proceedings of Jinmoncon 2024, vol. 2024, pp. 167-174",
    date: "2024-12-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "domestic-conference",
    firstAuthor: true,
    reviewed: true,
  },
  // ---- Technical Report (2024) ----
  {
    slug: "ipsj-ch-2024-1",
    title:
      "Multifaceted Exploration of War Perceptions in the Japanese Twitter Space: Reactions and Insights Regarding the Ukraine-Russia War",
    venue: "IPSJ SIG Technical Report on Computers and the Humanities (CH), vol. 2024-CH-135, issue 1, pp. 1-8",
    date: "2024-03-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "tech-report",
    firstAuthor: true,
  },
  {
    slug: "ipsj-ch-2024-2",
    title:
      "A Novel Dataset Development Method for Evaluating Sentiment Recognition Bias of Large Language Models in Conflict Structures",
    venue: "IPSJ SIG Technical Report on Computers and the Humanities (CH), vol. 2024-CH-136, issue 2, pp. 1-4",
    date: "2024-07-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "tech-report",
    firstAuthor: true,
  },
  // ---- Other (2024) ----
  {
    slug: "nuclear-opinion-2024",
    title: "To Leaders of Nations Relying on Nuclear Weapons: A Path to Peace Through Realism and Innovation",
    venue: "\"Nuclear-Free Future\" Opinion",
    date: "2024-01-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "other",
    firstAuthor: true,
  },
  {
    slug: "hito-shigoto-2024",
    title: "Innovation and Optimization of Human Resource Management Through Personal AI and Organizational AI",
    venue: "The 1st Prize Essay of the Institute for the Future of People and Work",
    date: "2024-01-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "other",
    firstAuthor: true,
  },
  {
    slug: "taiku-shisetsu-2024",
    title: "Well-being-Oriented Urban Design Through the Miniaturization of Sports and Modular Small-Scale Stadiums",
    venue: "Monthly Physical Education Facilities, December Issue, pp. 43-44",
    date: "2024-12-01",
    year: 2024,
    authors: "Keito Inoshita",
    kind: "other",
  },
  {
    slug: "shakai-kyoiku-2024",
    title: "Well-being-Oriented Urban Design Through the Miniaturization of Sports and Modular Small-Scale Stadiums",
    venue: "Social Education, vol. 44, issue 45, pp. 43-44",
    date: "2024-01-01",
    year: 2024,
    authors: "Keito Inoshita",
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

/** Format ISO date as English-style "May 2026". */
export function formatDateJa(iso: string): string {
  const months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
  ];
  const [y, m] = iso.split("-");
  return `${months[Number(m) - 1]} ${y}`;
}
