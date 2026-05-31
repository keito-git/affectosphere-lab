// Research threads of Affectosphere Group.
//
// Each entry corresponds to an ongoing or recently-completed project tracked
// in the lab's internal memory.  Update `status` as projects move through
// submission, review, and publication.

export type ResearchPillar =
  | "Uncertainty"
  | "Affective Computing"
  | "Society"
  | "Interdisciplinary";

export type ResearchCard = {
  slug: string;
  pillar: ResearchPillar;
  /** Short English title. */
  title: string;
  /** Japanese title used for bilingual display where space permits. */
  titleJa?: string;
  /** One-sentence elevator pitch in English. */
  summary: string;
  /** Current lifecycle status: "Submitted", "Under review", "In preparation", "Completed". */
  status: string;
  /** Optional anchor to a related publication entry (matched by Publication.slug). */
  publicationSlug?: string;
};

// All research threads, ordered by "front of mind" first.
// TODO(inoshita): tighten copy as more results land; add per-project pages
// under /research/[slug] when the bibliography stabilizes.
export const allResearch: ResearchCard[] = [
  {
    slug: "mcmc-emotion",
    pillar: "Uncertainty",
    title: "MCMC for Emotion Classification",
    titleJa: "MCMCによる感情分類の不確実性定量化",
    summary:
      "Sampling label posteriors with Markov-chain Monte Carlo to model the intrinsic ambiguity of emotion judgements and unify human and model uncertainty.",
    status: "In preparation",
  },
  {
    slug: "human-vs-ai-emotion",
    pillar: "Affective Computing",
    title: "LLMs Capture Labels, Not Uncertainty",
    titleJa: "LLMは感情ラベルを捉えるが不確実性は捉えない",
    summary:
      "A distributional analysis showing zero-shot LLMs mimic majority labels but fail to reproduce the disagreement structure of human annotators; in-domain fine-tuning and post-hoc calibration recover up to ~14% JSD.",
    status: "Submitted to EMNLP 2026 (ARR)",
    publicationSlug: "human-vs-ai-emotion",
  },
  {
    slug: "affective-silos",
    pillar: "Society",
    title: "Bridging the Silos in Affective AI",
    titleJa: "Affective AI のサイロを越えて",
    summary:
      "A position paper mapping five fractures (data, model, modality, interaction, society) that hold affective AI back from social impact, and proposing a unifying agenda.",
    status: "Submitted to AI & Society",
    publicationSlug: "affective-silos",
  },
  {
    slug: "mirra",
    pillar: "Affective Computing",
    title: "Mirra: A Mirror for Self-Reflection",
    titleJa: "Mirra — 自己省察のための対話AI",
    summary:
      "A conversational system designed not to answer but to mirror, scaffolding self-reflection through language-philosophical, Socratic, and narrative modes.",
    status: "Submitted to GCCE 2026",
    publicationSlug: "mirra",
  },
  {
    slug: "ipsj-dp-practice",
    pillar: "Society",
    title: "Practices for Uncertain Affective AI",
    titleJa: "不確実性下のAffective AI実務7プラクティス",
    summary:
      "Seven practices for handling distributional uncertainty in real-world affective AI deployments, distilled from the lab's recent emotion-LLM work.",
    status: "Submitted to IPSJ DP Vol.8 No.1",
    publicationSlug: "ipsj-dp",
  },
  {
    slug: "emotion-datamining",
    pillar: "Uncertainty",
    title: "Bayesian Spectral Emotion Transitions",
    titleJa: "ベイズ・スペクトル感情遷移発見 (BSETD)",
    summary:
      "A two-stage framework that estimates Bayesian emotion-transition matrices and decomposes them spectrally into emotional inertia (low frequency) and contagion (high frequency).",
    status: "Targeting ICDM 2027",
  },
  {
    slug: "phage-ai",
    pillar: "Interdisciplinary",
    title: "Phage Genome × AI",
    titleJa: "ファージゲノム × AI",
    summary:
      "Honest benchmarking and cross-attention models for phage-host interaction prediction, with active learning to make wet-lab experiments cheaper.",
    status: "Ongoing (3-paper plan)",
  },
  {
    slug: "hiyari-prediction",
    pillar: "Interdisciplinary",
    title: "Near-Miss Prediction from Probe Data",
    titleJa: "ヒヤリハット予測",
    summary:
      "A 40-model OOF ensemble that predicts near-miss events from Shiga prefectural probe data at PR-AUC 0.6445, a +21% relative gain over the previous benchmark.",
    status: "Completed (seminar)",
  },
];

// Three cards highlighted on the Home page.  Keep this set deliberately small.
export const featuredResearch: ResearchCard[] = [
  allResearch.find((r) => r.slug === "mcmc-emotion")!,
  allResearch.find((r) => r.slug === "mirra")!,
  allResearch.find((r) => r.slug === "affective-silos")!,
];
