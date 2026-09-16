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

/** The six stages of CAI, excluding the "beyond" band. */
export const caiStages = stages.filter((s) => s.id !== "beyond");

/**
 * Research domain -> the stage it mainly serves, so the ten domains and the
 * stack describe one structure rather than two.
 */
export const domainStage: Record<string, StageId> = {
  "emotion-recognition": "perception",
  "human-emotion-understanding": "representation",
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

  // --- Representation ------------------------------------------------------
  "inoshita-llm-emotion-uncertainty-2026": "representation",
  "inoshita-uncertainty-decomp-2026": "representation",
  "inoshita-bayesian-spectral-2026": "representation",
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

  // --- Interaction ---------------------------------------------------------
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
