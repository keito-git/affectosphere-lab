import { defineCollection, z } from "astro:content";

const columnSchema = z.object({
  title: z.string(),
  date: z.string(),
  excerpt: z.string(),
  image: z.string().optional(),
  imageAlt: z.string().optional(),
  readingMinutes: z.number().default(5),
  basedOnPaper: z.string().optional(),
  basedOnPaperUrl: z.string().optional(),
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
