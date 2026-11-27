import { defineCollection, z } from "astro:content";

// One schema for both languages. The research-blog fields (subtitle onward)
// are optional, so a short column needs only the first block.
const columnSchema = z.object({
  title: z.string(),
  date: z.string(),
  excerpt: z.string(),
  image: z.string().optional(),
  imageAlt: z.string().optional(),
  readingMinutes: z.number().default(5),
  basedOnPaper: z.string().optional(),
  basedOnPaperUrl: z.string().optional(),
  // Research-blog fields.
  subtitle: z.string().optional(),
  authors: z
    .array(
      z.object({
        name: z.string(),
        url: z.string().optional(),
        affiliation: z.string().optional(),
        /** Marks equal contribution with an asterisk. */
        equal: z.boolean().optional(),
      })
    )
    .optional(),
  /** Short summary shown in a box above the body. */
  tldr: z.string().optional(),
  /** Links shown under the title and on the list page (Paper, Code, X ...). */
  links: z.array(z.object({ label: z.string(), url: z.string() })).optional(),
  /** BibTeX entry shown at the end with a copy button. */
  citation: z.string().optional(),
  /** Dated notes appended after publication. */
  updated: z.string().optional(),
  /** Drafts are skipped by every page. */
  draft: z.boolean().default(false),
});

const columnJa = defineCollection({
  type: "content",
  schema: columnSchema,
});

const columnEn = defineCollection({
  type: "content",
  schema: columnSchema,
});

export const collections = {
  "column-ja": columnJa,
  "column-en": columnEn,
};
