// Research map: which of the ten CAI domains each publication belongs to, and
// how the domains stack into the three layers of the field.
//
// HOW THE ASSIGNMENT WAS MADE — this matters, so it is stated on the page too:
// every entry in publications.ts was read and assigned to the single domain it
// contributes to most. Papers that touch several domains are counted once, in
// the domain of their main contribution. No publication is invented, counted
// twice, or moved to make a domain look fuller; the two domains with no
// publications yet are shown as empty.

import { allPublications, type Publication } from "./publications";

export type LayerId = "foundation" | "technology" | "application" | "beyond";

export const layers: { id: LayerId; label: string; labelEn: string; note: string; noteEn: string }[] = [
  {
    id: "foundation",
    label: "基盤",
    labelEn: "Foundation",
    note: "CAI を「なぜ・何のために」つくるのかを決める層。",
    noteEn: "Why CAI is built, and what it is answerable to.",
  },
  {
    id: "technology",
    label: "技術",
    labelEn: "Technology",
    note: "感情を確率として扱うための、データとモデルの層。",
    noteEn: "The data and models that let emotion be handled as a distribution.",
  },
  {
    id: "application",
    label: "実装",
    labelEn: "Application",
    note: "測った感情を、人の手元に届ける層。",
    noteEn: "Returning what was measured to the people it came from.",
  },
  {
    id: "beyond",
    label: "感情AI以外",
    labelEn: "Beyond affect",
    note: "感情AIの外側で進めている、AI研究そのものの領域。",
    noteEn: "AI research pursued outside affective computing.",
  },
];

/** The three layers that make up CAI, excluding the "beyond" band. */
export const caiLayers = layers.filter((l) => l.id !== "beyond");

/** Domain slug -> layer. Slugs match research-domains.ts. */
export const domainLayer: Record<string, LayerId> = {
  "ethics-philosophy": "foundation",
  "human-emotion-understanding": "foundation",
  // Work that is AI research but not affective AI. Kept off the CAI map
  // proper and shown separately, so the map reads as coverage of CAI.
  "other-ai-research": "beyond",
  "data-augmentation": "technology",
  interpretability: "technology",
  "emotion-recognition": "technology",
  "human-ai-interaction": "application",
  business: "application",
  "affective-ai-art": "application",
  "application-development": "application",
};

/** Publication slug -> domain slug. */
export const publicationDomain: Record<string, string> = {
  // --- Ethics & philosophy -------------------------------------------------
  "inoshita-ai-homogenize-2026": "ethics-philosophy",
  "inoshita-affective-silos-2026": "ethics-philosophy",
  "inoshita-affective-sovereignty-2026": "ethics-philosophy",
  "showa-ikeda-2025": "ethics-philosophy",
  "ieee-bdcloud-2024": "ethics-philosophy",

  // --- Human emotion understanding ----------------------------------------
  "inoshita-bayesian-spectral-2026": "human-emotion-understanding",

  // --- Interpretability ----------------------------------------------------
  "inoshita-llm-emotion-uncertainty-2026": "interpretability",
  "inoshita-uncertainty-decomp-2026": "interpretability",
  "inoshita-uncertainty-routing-2026": "interpretability",

  // --- Emotion data augmentation -------------------------------------------
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

  // --- Emotion recognition --------------------------------------------------
  "world-model-sarcasm-2026": "emotion-recognition",
  "nldb-2025": "emotion-recognition",
  "ieee-iaict-2025-sarcasm": "emotion-recognition",
  "ieee-icoailo-2025": "emotion-recognition",
  "ieee-picom-2025": "emotion-recognition",
  "ipsj-ch-ueno-2025": "emotion-recognition",
  "ipsj-nl-2025": "emotion-recognition",
  "c-dira-2025": "emotion-recognition",
  "ieee-ithings-2024": "emotion-recognition",

  // --- Business --------------------------------------------------------------
  "ieee-zinc-2026": "business",
  "joho-chishiki-multimodal-2025": "business",
  "joho-chishiki-tourism-2025": "business",
  "chikyu-uchu-mirai-2025": "business",
  "rikoukei-essay-2025": "business",
  "hito-shigoto-2024": "business",

  // --- Application development ----------------------------------------------
  "inoshita-cognitive-causal-2026": "application-development",
  "inoshita-driver-intervention-2026": "application-development",
  "ieee-hpcc-2025": "application-development",
  "ai-dhwp-2025": "application-development",

  // --- Other AI research ------------------------------------------------------
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

/** Peer-reviewed international venues, derived from `kind` — not guessed. */
export function tier(pub: Publication): "international" | "domestic" | "preprint" {
  if (pub.kind === "journal-international" || pub.kind === "international-conference") {
    return "international";
  }
  if (pub.kind === "preprint") return "preprint";
  return "domestic";
}

export type DomainStat = {
  slug: string;
  layer: LayerId;
  total: number;
  international: number;
  domestic: number;
  preprint: number;
  years: number[];
  pubs: Publication[];
};

/** Counts per domain, computed from publications.ts at build time. */
export function domainStats(): Record<string, DomainStat> {
  const stats: Record<string, DomainStat> = {};
  for (const slug of Object.keys(domainLayer)) {
    stats[slug] = {
      slug,
      layer: domainLayer[slug],
      total: 0,
      international: 0,
      domestic: 0,
      preprint: 0,
      years: [],
      pubs: [],
    };
  }
  for (const pub of allPublications) {
    const domain = publicationDomain[pub.slug];
    if (!domain || !stats[domain]) continue;
    const s = stats[domain];
    s.total += 1;
    s[tier(pub)] += 1;
    if (!s.years.includes(pub.year)) s.years.push(pub.year);
    s.pubs.push(pub);
  }
  for (const s of Object.values(stats)) s.years.sort();
  return stats;
}

/** Publications that fall outside the map, so the page can never overstate coverage. */
export function unmappedCount(): number {
  return allPublications.filter((p) => !publicationDomain[p.slug]).length;
}
