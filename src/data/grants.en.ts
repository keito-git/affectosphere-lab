// Competitive grants & research funding received by the PI.
// Sourced from the PI's CV.

export type Grant = {
  /** Project title (English). */
  projectTitle: string;
  /** Funding program / scheme name. */
  program: string;
  /** Awarding body / organization. */
  organization?: string;
  /** Period string, e.g. "2025/4 – 2028/3". */
  period: string;
  /** Optional public amount. Leave undefined when private. */
  amount?: string;
  /** PI / Co-I / Principal Investigator etc. */
  role?: string;
  /** Optional comma-separated co-investigator list. */
  coInvestigators?: string;
};

// Newest start-date first.
export const grants: Grant[] = [
  {
    projectTitle:
      "Building Context-Aware Emotion Recognition Multi-Agents Based on World Models",
    program: "Nippon Foundation HUMAI Program Grant B",
    organization: "The Nippon Foundation",
    period: "2026/8 – 2027/3",
    role: "Principal Investigator",
  },
  {
    projectTitle:
      "Improving Emotion Perception Capability of Large Language Models via Diagonalization of Emotion Parameters",
    program:
      "Support for Pioneering Research Initiated by the Next Generation (SPRING)",
    organization: "Japan Science and Technology Agency (JST)",
    period: "2026/4 – 2027/3",
    role: "Principal Investigator",
  },
  {
    projectTitle:
      "Building Large Language Models with Enhanced Pragmatic Reasoning through Bidirectional Learning of Irony Generation and Understanding",
    program: "Research Investigation Grant",
    organization: "The Telecommunications Advancement Foundation",
    period: "2026/4 – 2027/3",
    role: "Principal Investigator",
    coInvestigators: "Takato Ueno, Katsutoshi Yada",
  },
  {
    projectTitle:
      "Research on Foundational Technologies for Empathetic Large Language Models through Fine-Grained Control of Emotional Expression",
    program: "GMO Research Grant Program",
    organization: "GMO Internet Foundation",
    period: "2026/4 – 2027/3",
    role: "Principal Investigator",
  },
  {
    projectTitle:
      "Development of a Mental Health Support System That Adapts to Emotional Changes Using Wearable Devices and AI",
    program: "Public Health Science Research Grant",
    organization: "Public Health Research Foundation",
    period: "2026/4 – 2027/3",
    role: "Principal Investigator",
  },
  {
    projectTitle:
      "Development of Risk Detection and Visual Support Interfaces Focusing on Driving Behavior of Hearing-Impaired People",
    program: "ECOMO Transportation Barrier-Free Research and Activity Grant",
    organization: "Foundation for Promoting Personal Mobility and Ecological Transportation",
    period: "2026/4 – 2027/3",
    role: "Principal Investigator",
  },
  {
    projectTitle:
      "Building Self-Evolving Emotion Recognition AI through Self-Sufficient Emotion Data",
    program: "Nippon Foundation HUMAI Program Grant B",
    organization: "The Nippon Foundation",
    period: "2025/8 – 2026/3",
    role: "Principal Investigator",
  },
  {
    projectTitle:
      "Generative AI for Ethically and Legally Unconstrained Emotion Data Generation and a Well-being Support Platform Accessible to All",
    program: "LEADING EDGE Shikoku — Unexplored Regional Young Talent Discovery and Development Program",
    period: "2025/8 – 2026/1",
    role: "Principal Investigator",
  },
  {
    projectTitle:
      "Building a Dialogue-Based Multimodal Emotion Recognition System for Improving Workplace Well-being",
    program:
      "Support for Pioneering Research Initiated by the Next Generation (SPRING)",
    organization: "Japan Science and Technology Agency (JST)",
    period: "2025/4 – 2028/3",
    role: "Principal Investigator",
  },
  {
    projectTitle:
      "Decision Support and Organizational Learning Enhancement through Emotion Simulation and Gaming Using Multimodal LLMs in Workplace Environments",
    program: "Research Grant",
    organization: "Foundation for the Fusion of Science and Technology",
    period: "2025/4 – 2026/3",
    amount: "JPY 180,000",
    role: "Principal Investigator",
  },
];

export const totalGrants = grants.length;
