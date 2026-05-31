// Blog posts and informal essays ("Column").
//
// These are short-form pieces by the PI: research blog entries, essay-style
// notes, and translations of papers into accessible prose.  Long-form
// content can live in `src/pages/column/[slug].astro` later; for now we
// only render the index card grid.
//
// TODO(inoshita): once a post is written, drop the body in Markdown under
// `src/content/column/` (an Astro Content Collection) and switch the index
// to read from there instead of this hand-maintained array.

export type ColumnPost = {
  slug: string;
  date: string; // ISO YYYY-MM-DD
  title: string;
  /** One-sentence dek shown on the index card. */
  excerpt: string;
  /** Optional external link if the post lives elsewhere (Note, Medium, ...). */
  href?: string;
  /** When true, render the card as a "coming soon" placeholder. */
  placeholder?: boolean;
};

// Newest first.
export const columnPosts: ColumnPost[] = [
  {
    slug: "why-affectosphere",
    date: "2026-05-27",
    title: "Why \"Affectosphere\"?",
    excerpt:
      "A short note on coining the word — emotion as an atmosphere that envelops society, and why the lab needs a name that sits beside biosphere and noosphere.",
    placeholder: true,
  },
  {
    slug: "labels-vs-uncertainty",
    date: "2026-05-15",
    title: "Labels Are Easy. Uncertainty Is Not.",
    excerpt:
      "Plain-language companion to the EMNLP submission: why an LLM can name the emotion in a sentence and still get the disagreement structure wrong.",
    placeholder: true,
  },
  {
    slug: "five-silos",
    date: "2026-05-25",
    title: "Five Silos in Affective AI",
    excerpt:
      "A walkthrough of the data / model / modality / interaction / society fractures argued in the lab's AI & Society submission.",
    placeholder: true,
  },
];
