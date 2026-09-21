// AI for Science page content.
// Mirrors the structure of research-domains.ts NarrativeBlock for visual
// consistency with the affective-AI research detail pages.

export type NarrativeBlock = {
  /** Optional sub-section heading (rendered above the paragraph). */
  heading?: string;
  text: string;
  figure?: {
    src: string;
    caption: string;
    alt: string;
  };
};

export const aiForScienceLongDescription =
  "AI for Science brings AI in as a new instrument of observation, replacing knowledge production that depended on experience and judgement with procedures that can be measured and repeated. Affectosphere Group works with researchers across education, political science, ecology and law, carrying over the techniques built in CAI for treating the variance in human judgement as data.";

export const aiForScienceFindings =
  "One structure recurs across fields: an LLM produces the plausible average at high quality, and systematically drops the tails — the rare argument, the minority state, the long tail of naming, the domain-specific rule. AI for Science is less the application of a method than the work of deciding, field by field, what may be delegated and what may not.";

// Inquiry endpoint (the form opens the user's email client with this address).
export const inquiryEmail = "inquiry@affectosphere.group";

export const aiForScienceNarrative: NarrativeBlock[] = [
  {
    text: "Using AI as the analyser creates a new validity problem: the bias of the analyser itself. So in AI for Science the methodology of evaluation becomes as much the object of study as the result.",
  },
  {
    heading: "Education × AI",
    text: "Generative AI lifts the quality of student writing sharply, while the rarity of its claims sits at about a fifth of a human's and it strips roughly seventy per cent of the variance out of how arguments are joined. Writing assessment should move from “was this written well” to “is this thought anyone else's”.",
  },
  {
    heading: "Political science × AI",
    text: "From sentiment analysis over 200,000 Japanese tweets, and from measuring how far predictions invert when the country names are swapped, we quantified the national bias sitting inside LLMs. Scanning the large pre-training corpora shows that the skew is already present in the training data.",
  },
  {
    heading: "Ecology × AI",
    text: "Across 48,464 spider species, we evaluated automatic classification of the etymology behind their scientific names. Names derived from morphology or geography approach human accuracy; names derived from behaviour or culture fall away sharply — and the boundary of what can be delegated shows up right there.",
  },
  {
    heading: "Law × AI",
    text: "Given ten years of the Japanese real-estate transaction licence exam, no model reached the pass mark. Not a stage of full substitution, then, but promising as support for a learner or an assistant to a legal team.",
  },
  {
    text: "It is where diagnostic technique built in CAI is carried out to questions that matter socially — and, through the exchange with domain experts, where CAI's own methodology gets reworked.",
  },
];
