// The CAI stack, and where each publication sits on it.
//
// Computational Affective Intelligence is described here as six stages an
// affective system passes through — perception, representation, reasoning,
// generation, interaction, society. The map shows how far each stage has
// actually been filled in.
//
// HOW THE ASSIGNMENT WAS MADE — this is stated on the page too: every entry in
// publications.ts was read and placed at the single stage it contributes to
// most. Work spanning several stages is counted once, at its main
// contribution. Nothing is invented, counted twice, or moved to make a stage
// look fuller, and AI research outside affective AI is kept off the stack
// rather than folded into it.

import { allPublications, type Publication } from "./publications";

export type StageId =
  | "human-affect"
  | "perception"
  | "representation"
  | "reasoning"
  | "generation"
  | "interaction"
  | "society"
  | "beyond";

export type Stage = {
  id: StageId;
  label: string;
  labelJa: string;
  note: string;
  noteEn: string;
};

export const stages: Stage[] = [
  {
    id: "human-affect",
    label: "Human Affect",
    labelJa: "人間の感情を理解する",
    note: "そもそも人は感情をどう経験し、どう食い違うのか。計算の前にある問い。",
    noteEn: "How people actually experience emotion, and where they disagree — the question that precedes any model.",
  },
  {
    id: "perception",
    label: "Perception",
    labelJa: "読み取る",
    note: "テキスト・音声・映像・生理信号から、感情を推定する。",
    noteEn: "Estimating emotion from text, speech, video and physiological signals.",
  },
  {
    id: "representation",
    label: "Representation",
    labelJa: "保持する",
    note: "読み取った感情を、確率分布と不確実性のまま内部に持つ。",
    noteEn: "Holding what was read as a distribution, with its uncertainty intact.",
  },
  {
    id: "reasoning",
    label: "Reasoning",
    labelJa: "考える",
    note: "感情を前提に、文脈と因果をたどって判断する。",
    noteEn: "Judging from emotion: following context and causal structure.",
  },
  {
    id: "generation",
    label: "Generation",
    labelJa: "形にする",
    note: "感情を帯びた言語・データ・振る舞いを生成する。",
    noteEn: "Producing affect-bearing language, data and behaviour.",
  },
  {
    id: "interaction",
    label: "Interaction",
    labelJa: "向き合う",
    note: "人と AI が感情を介して往復する場をつくる。",
    noteEn: "Building the place where a person and an AI meet through emotion.",
  },
  {
    id: "society",
    label: "Society",
    labelJa: "社会に据える",
    note: "誰が感情の意味を決めるのかを含めて、社会に置き直す。",
    noteEn: "Placing it in society, including who decides what an emotion means.",
  },
  {
    id: "beyond",
    label: "Beyond affect",
    labelJa: "感情AIの外側",
    note: "感情AIの外側で進めている、AI研究そのもの。",
    noteEn: "AI research pursued outside affective computing.",
  },
];

/** The stages of CAI, excluding the "beyond" band. */
export const caiStages = stages.filter((s) => s.id !== "beyond");

export type TierId =
  | "human-affect"
  | "computational-representation"
  | "affective-intelligence"
  | "human-ai-society";

export type Tier = {
  id: TierId;
  numeral: string;
  label: string;
  labelJa: string;
  note: string;
  noteEn: string;
};

/**
 * The four tiers the field divides into: understanding human affect, giving it
 * a computational representation, letting a system reason and act with it, and
 * placing the result back among people.
 */
export const tiers: Tier[] = [
  {
    id: "human-affect",
    numeral: "I",
    label: "Human Affect",
    labelJa: "人間の感情",
    note: "人間の感情そのものを理解する層。",
    noteEn: "Understanding human emotion itself.",
  },
  {
    id: "computational-representation",
    numeral: "II",
    label: "Computational Representation",
    labelJa: "計算表現",
    note: "それを AI の内部で計算可能な形に置く層。",
    noteEn: "Giving it a form a machine can hold and compute over.",
  },
  {
    id: "affective-intelligence",
    numeral: "III",
    label: "Affective Intelligence",
    labelJa: "感情知能",
    note: "AI がそれを使って推論し、生成し、判断する層。",
    noteEn: "Where the system reasons, generates and decides with it.",
  },
  {
    id: "human-ai-society",
    numeral: "IV",
    label: "Human–AI Society",
    labelJa: "人とAIの社会",
    note: "それが人と社会のあいだで何を起こすかを扱う層。",
    noteEn: "What all of it does between people, and in society.",
  },
];

/** Which tier each stage belongs to. */
export const stageTier: Record<string, TierId> = {
  "human-affect": "human-affect",
  perception: "computational-representation",
  representation: "computational-representation",
  reasoning: "affective-intelligence",
  generation: "affective-intelligence",
  interaction: "human-ai-society",
  society: "human-ai-society",
};

/**
 * Research domain -> the stage it mainly serves, so the ten domains and the
 * stack describe one structure rather than two.
 */
export const domainStage: Record<string, StageId> = {
  "emotion-recognition": "perception",
  "human-emotion-understanding": "human-affect",
  interpretability: "reasoning",
  "data-augmentation": "generation",
  "human-ai-interaction": "interaction",
  "application-development": "interaction",
  "ethics-philosophy": "society",
  business: "society",
  "affective-ai-art": "society",
  "other-ai-research": "beyond",
};

/** Publication slug -> stage. */
export const publicationStage: Record<string, StageId> = {
  // --- Perception ----------------------------------------------------------
  "nldb-2025": "perception",
  "ieee-iaict-2025-sarcasm": "perception",
  "ieee-icoailo-2025": "perception",
  "joho-chishiki-multimodal-2025": "perception",
  "kansei-kogaku-2025": "perception",
  "ipsj-nl-2025": "perception",
  "c-dira-2025": "perception",
  "ieee-ithings-2024": "perception",

  // --- Human affect --------------------------------------------------------
  "inoshita-bayesian-spectral-2026": "human-affect",

  // --- Representation ------------------------------------------------------
  "inoshita-llm-emotion-uncertainty-2026": "representation",
  "inoshita-uncertainty-decomp-2026": "representation",
  "inoshita-uncertainty-routing-2026": "representation",

  // --- Reasoning -----------------------------------------------------------
  "inoshita-cognitive-causal-2026": "reasoning",
  "world-model-sarcasm-2026": "reasoning",
  "ieee-picom-2025": "reasoning",
  "ipsj-ch-ueno-2025": "reasoning",

  // --- Generation ----------------------------------------------------------
  "inoshita-driver-intervention-2026": "generation",
  "persona-synthetic-2026": "generation",
  "kdda-2026": "generation",
  "ieee-zinc-2026": "generation",
  "nlc-2026": "generation",
  "ieee-gcce-2025": "generation",
  "fit-2025": "generation",
  "ipsj-kansai-2025": "generation",
  "wakate-symposium-2025": "generation",
  "text-analytics-2025": "generation",
  "geometric-control-2025": "generation",
  "inoshita-class-structure-2026": "generation",

  // --- Interaction ---------------------------------------------------------
  "matsuo-self-reflective-2026": "interaction",
  "ieee-hpcc-2025": "interaction",
  "ai-dhwp-2025": "interaction",

  // --- Society -------------------------------------------------------------
  "inoshita-ai-homogenize-2026": "society",
  "inoshita-affective-silos-2026": "society",
  "inoshita-affective-sovereignty-2026": "society",
  "joho-chishiki-tourism-2025": "society",
  "chikyu-uchu-mirai-2025": "society",
  "rikoukei-essay-2025": "society",
  "showa-ikeda-2025": "society",
  "ieee-bdcloud-2024": "society",
  "hito-shigoto-2024": "society",

  // --- Beyond affect -------------------------------------------------------
  "inoshita-name-region-2026": "beyond",
  "inoshita-name-remind-2026": "beyond",
  "inoshita-argument-rarity-2026": "beyond",
  "nojiri-etymology-2026": "beyond",
  "nojiri-gliding-2026": "beyond",
  "automated-labeling-2025": "beyond",
  "ieee-iaict-2025-naming": "beyond",
  "biology-3gakkai-sugeno-2025": "beyond",
  "biology-3gakkai-nojiri-2025": "beyond",
  "dobutsugakkai-2025": "beyond",
  "sugeno-plankton-2026": "beyond",
  "times-icon-2024": "beyond",
  "icitacee-2024": "beyond",
  "diges-grace-2024": "beyond",
  "icelitics-2024": "beyond",
  "nlp4dh-emnlp-2024": "beyond",
  "ieee-iotais-2024-evolutionary": "beyond",
  "ieee-iotais-2024-multifaceted": "beyond",
  "3ict-2024": "beyond",
  "ieee-dss-2024": "beyond",
  "jinmoncon-2024": "beyond",
  "ipsj-ch-2024-1": "beyond",
  "ipsj-ch-2024-2": "beyond",
  "nuclear-opinion-2024": "beyond",
  "taiku-shisetsu-2024": "beyond",
  "shakai-kyoiku-2024": "beyond",
  "okugawa-vanishing-municipalities-2026": "beyond",
};


/**
 * Publication -> research domain. A second axis, independent of the stage: the
 * stage says what part of a system the work advances, the domain says which of
 * the lab's ten research areas it belongs to. Assigned by reading each entry.
 */
export const publicationDomain: Record<string, string> = {
  // 感情AIの倫理と哲学
  "inoshita-ai-homogenize-2026": "ethics-philosophy",
  "inoshita-affective-silos-2026": "ethics-philosophy",
  "inoshita-affective-sovereignty-2026": "ethics-philosophy",
  "showa-ikeda-2025": "ethics-philosophy",
  "ieee-bdcloud-2024": "ethics-philosophy",

  // 人間の感情理解
  "inoshita-bayesian-spectral-2026": "human-emotion-understanding",

  // 感情AIの内部理解
  "inoshita-llm-emotion-uncertainty-2026": "interpretability",
  "inoshita-uncertainty-decomp-2026": "interpretability",
  "inoshita-uncertainty-routing-2026": "interpretability",

  // 感情データの拡張
  "persona-synthetic-2026": "data-augmentation",
  "kdda-2026": "data-augmentation",
  "nlc-2026": "data-augmentation",
  "ieee-gcce-2025": "data-augmentation",
  "fit-2025": "data-augmentation",
  "kansei-kogaku-2025": "data-augmentation",
  "ipsj-kansai-2025": "data-augmentation",
  "wakate-symposium-2025": "data-augmentation",
  "text-analytics-2025": "data-augmentation",
  "geometric-control-2025": "data-augmentation",
  "inoshita-class-structure-2026": "data-augmentation",

  // AIによる感情の認識
  "world-model-sarcasm-2026": "emotion-recognition",
  "nldb-2025": "emotion-recognition",
  "ieee-iaict-2025-sarcasm": "emotion-recognition",
  "ieee-icoailo-2025": "emotion-recognition",
  "ieee-picom-2025": "emotion-recognition",
  "ipsj-ch-ueno-2025": "emotion-recognition",
  "ipsj-nl-2025": "emotion-recognition",
  "c-dira-2025": "emotion-recognition",
  "ieee-ithings-2024": "emotion-recognition",

  // 感情AIと人間のインタラクション
  "matsuo-self-reflective-2026": "human-ai-interaction",

  // 感情AIとビジネス
  "ieee-zinc-2026": "business",
  "joho-chishiki-multimodal-2025": "business",
  "joho-chishiki-tourism-2025": "business",
  "chikyu-uchu-mirai-2025": "business",
  "rikoukei-essay-2025": "business",
  "hito-shigoto-2024": "business",

  // 感情AIに基づく開発
  "inoshita-cognitive-causal-2026": "application-development",
  "inoshita-driver-intervention-2026": "application-development",
  "ieee-hpcc-2025": "application-development",
  "ai-dhwp-2025": "application-development",

  // その他AI研究
  "inoshita-name-region-2026": "other-ai-research",
  "inoshita-name-remind-2026": "other-ai-research",
  "inoshita-argument-rarity-2026": "other-ai-research",
  "nojiri-etymology-2026": "other-ai-research",
  "nojiri-gliding-2026": "other-ai-research",
  "automated-labeling-2025": "other-ai-research",
  "ieee-iaict-2025-naming": "other-ai-research",
  "biology-3gakkai-sugeno-2025": "other-ai-research",
  "biology-3gakkai-nojiri-2025": "other-ai-research",
  "dobutsugakkai-2025": "other-ai-research",
  "sugeno-plankton-2026": "other-ai-research",
  "okugawa-vanishing-municipalities-2026": "other-ai-research",
  "times-icon-2024": "other-ai-research",
  "icitacee-2024": "other-ai-research",
  "diges-grace-2024": "other-ai-research",
  "icelitics-2024": "other-ai-research",
  "nlp4dh-emnlp-2024": "other-ai-research",
  "ieee-iotais-2024-evolutionary": "other-ai-research",
  "ieee-iotais-2024-multifaceted": "other-ai-research",
  "3ict-2024": "other-ai-research",
  "ieee-dss-2024": "other-ai-research",
  "jinmoncon-2024": "other-ai-research",
  "ipsj-ch-2024-1": "other-ai-research",
  "ipsj-ch-2024-2": "other-ai-research",
  "nuclear-opinion-2024": "other-ai-research",
  "taiku-shisetsu-2024": "other-ai-research",
  "shakai-kyoiku-2024": "other-ai-research",
};

/** Venue tier, derived from `kind` — not guessed. */
export function tier(pub: Publication): "international" | "domestic" | "preprint" {
  if (pub.kind === "journal-international" || pub.kind === "international-conference") {
    return "international";
  }
  if (pub.kind === "preprint") return "preprint";
  return "domestic";
}

export type StageStat = {
  id: StageId;
  total: number;
  years: number[];
  pubs: Publication[];
};

/** Counts per stage, computed from publications.ts at build time. */
export function stageStats(): Record<StageId, StageStat> {
  const stats = {} as Record<StageId, StageStat>;
  for (const stage of stages) {
    stats[stage.id] = { id: stage.id, total: 0, years: [], pubs: [] };
  }
  for (const pub of allPublications) {
    const id = publicationStage[pub.slug];
    if (!id || !stats[id]) continue;
    stats[id].total += 1;
    if (!stats[id].years.includes(pub.year)) stats[id].years.push(pub.year);
    stats[id].pubs.push(pub);
  }
  for (const s of Object.values(stats)) s.years.sort();
  return stats;
}

/** Publications not placed on the stack, so the page cannot overstate coverage. */
export function unmappedCount(): number {
  return allPublications.filter((p) => !publicationStage[p.slug]).length;
}
