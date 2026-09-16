// Header-image generator for the research domains.
//
// Same brand-locked master prompt as scripts/gen-images.mjs: flat editorial
// illustration, the lab palette only, no text, no logos, no people. Each domain
// supplies one short visual concept so the set reads as one family.
//
// Writes to public/field-images/<slug>.png — new filenames, so the images the
// PI prepared are left in place untouched.
//
// Usage:  node scripts/gen-field-images.mjs [slug ...]
//
// The OpenAI key is read from ~/.claude/api_keys.env and is NEVER printed.

import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { homedir } from "node:os";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const OUT_DIR = join(ROOT, "public", "field-images");

const PALETTE =
  "cream background (#F4F0E8 / #FAFAF7), warm amber accent (#C4974A), deep charcoal (#1A1A1A); " +
  "at most one muted secondary accent of steel-blue (#3D6B8C) or sage (#6B8F7A); no vivid or neon colors";

// One concept per domain. These describe the idea of the domain, not a scene:
// the point is that a reader grasps the domain faster from the image than from
// the first sentence of the text.
const CONCEPTS = {
  "ethics-philosophy":
    "translucent horizontal planes stacked like sediment layers, with visible seams between them; a pair of balance scales drawn as thin geometric lines resting across the topmost layer",
  "human-emotion-understanding":
    "several overlapping translucent circles of slightly different sizes, each one a different person's reading of the same feeling; where they overlap the tone deepens, and no single circle dominates",
  "data-augmentation":
    "a sparse scattering of points on one side growing into a dense structured field on the other, connected by thin interpolation lines that preserve the shape of the original cluster",
  interpretability:
    "a rounded solid form opened in cross-section like a geode, thin contour lines tracing the internal structure that was hidden from outside",
  "emotion-recognition":
    "an abstract waveform resolving not into a single point but into a smooth probability curve, with the spread of the curve clearly visible",
  "human-ai-interaction":
    "two rounded forms facing each other across a shared band of overlap, small pulses travelling in both directions through that band",
  business:
    "stacked rounded bars and one gentle upward curve at an office scale, with a single warm accent marking the one human-sized element among them",
  "affective-ai-art":
    "a loose organic brush-like stroke meeting a precise geometric grid, the two interleaving where they cross rather than one covering the other",
  "application-development":
    "modular rounded blocks assembling into a working whole, one block in warm amber showing where a person fits into the assembly",
  "other-ai-research":
    "a loose collection of distinct abstract motifs — a leaf vein pattern, a small network graph, a column of abstract text lines — arranged as separate specimens on one surface",
  "ai-for-science":
    "an abstract instrument form and a smooth data curve merging into each other, organic growth patterns interleaved with geometric measurement marks",
};

function buildPrompt(concept) {
  return [
    "A flat editorial vector illustration for a section header, 3:2 horizontal composition.",
    `Concept: ${concept}`,
    "Style: clean modern flat illustration, simple geometric shapes with gentle organic curves,",
    "subtle paper-grain texture, soft long shadows, minimal detail, generous negative space,",
    "calm and professional editorial tone, suitable behind a light overlay with text on top.",
    `Color palette strictly limited to: ${PALETTE}.`,
    "Hard constraints: absolutely NO text, letters, numbers, words, captions, or labels;",
    "NO logos, brand marks or trademarks; NO real or recognizable people or faces;",
    "NO celebrity likeness; NO copyrighted characters or mascots; NO watermark.",
    "Make it metaphorical and conceptual, not a literal UI screenshot or a photograph.",
    "Keep the centre calm and uncluttered so a headline can sit over it.",
  ].join("\n");
}

const MODELS = ["gpt-image-2-2026-04-21", "gpt-image-1"];
const SIZE = "1536x1024";

function loadApiKey() {
  const txt = readFileSync(join(homedir(), ".claude", "api_keys.env"), "utf8");
  for (const line of txt.split("\n")) {
    const m = line.match(/^OPENAI_API_KEY=(.+)$/);
    if (m && m[1].trim()) return m[1].trim();
  }
  throw new Error("OPENAI_API_KEY not found in ~/.claude/api_keys.env");
}

async function generateOne(apiKey, slug, concept, attempt = 1) {
  const prompt = buildPrompt(concept);
  let lastErr;
  for (const model of MODELS) {
    try {
    const res = await fetch("https://api.openai.com/v1/images/generations", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${apiKey}` },
      body: JSON.stringify({ model, prompt, size: SIZE, n: 1 }),
    });
    if (res.ok) {
      const data = await res.json();
      const b64 = data?.data?.[0]?.b64_json;
      if (!b64) throw new Error(`No image data returned for ${slug}`);
      return { buf: Buffer.from(b64, "base64"), model };
    }
      lastErr = `[${model}] ${res.status}: ${(await res.text()).slice(0, 300)}`;
      if (res.status !== 404 && res.status !== 400) break;
    } catch (err) {
      // Transient network failure: the request never completed.
      lastErr = `[${model}] ${err?.message ?? err}`;
      break;
    }
  }
  if (attempt < 4) {
    await new Promise((r) => setTimeout(r, attempt * 4000));
    return generateOne(apiKey, slug, concept, attempt + 1);
  }
  throw new Error(`Image API failed for ${slug}: ${lastErr}`);
}

async function main() {
  const only = process.argv.slice(2).filter((a) => !a.startsWith("--"));
  const slugs = only.length > 0 ? only : Object.keys(CONCEPTS);
  mkdirSync(OUT_DIR, { recursive: true });
  const apiKey = loadApiKey();

  let made = 0;
  for (const slug of slugs) {
    const concept = CONCEPTS[slug];
    if (!concept) {
      console.log(`  ? unknown slug: ${slug}`);
      continue;
    }
    const out = join(OUT_DIR, `${slug}.png`);
    if (existsSync(out)) {
      console.log(`  = exists, skipping: ${slug}.png`);
      continue;
    }
    process.stdout.write(`  … ${slug}`);
    try {
      const { buf, model } = await generateOne(apiKey, slug, concept);
      writeFileSync(out, buf);
      made += 1;
      console.log(`  → ${(buf.length / 1024).toFixed(0)} KB (${model})`);
    } catch (err) {
      console.log(`  ! failed: ${String(err.message || err).slice(0, 120)}`);
    }
  }
  console.log(`\n${made} image(s) written to public/field-images/`);
}

main().catch((err) => {
  console.error(String(err.message || err));
  process.exit(1);
});
