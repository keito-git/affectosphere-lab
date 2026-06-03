// Header-image generator for Affectosphere Lab columns.
//
// Generates copyright-clean, flat editorial illustrations via the OpenAI
// image API. The brand-locked MASTER prompt lives here; each article only
// supplies a short {concept} string, so daily runs vary one part and keep
// the house style consistent.
//
// Usage:
//   node scripts/gen-images.mjs <manifest.json> [--note-dir <dir>]
//
// manifest.json: [{ "slug": "...", "concept": "one-line visual concept" }, ...]
//
// Output:
//   public/column-images/<slug>.png            (site header)
//   <note-dir>/<slug>.png        (if --note-dir given; note upload copy)
//
// The OpenAI key is read internally from ~/.claude/api_keys.env and is
// NEVER printed or written anywhere.

import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { homedir } from "node:os";

const PALETTE =
  "cream background (#F4F0E8 / #FAFAF7), warm amber accent (#C4974A), deep charcoal (#1A1A1A); " +
  "at most one muted secondary accent of steel-blue (#3D6B8C) or sage (#6B8F7A); no vivid or neon colors";

// Brand-locked master prompt. Only {CONCEPT} varies per article.
function buildPrompt(concept) {
  return [
    "A flat editorial vector illustration for a blog header, 16:9 horizontal composition.",
    `Concept: ${concept}`,
    "Style: clean modern flat illustration, simple geometric shapes with gentle organic curves,",
    "subtle paper-grain texture, soft long shadows, minimal detail, generous negative space,",
    "calm and professional editorial tone.",
    `Color palette strictly limited to: ${PALETTE}.`,
    "Hard constraints: absolutely NO text, letters, numbers, words, captions, or labels;",
    "NO logos, brand marks or trademarks; NO real or recognizable people or faces;",
    "NO celebrity likeness; NO copyrighted characters or mascots; NO watermark.",
    "Make it metaphorical and conceptual, not a literal UI screenshot.",
    "Centered, balanced composition that reads well both as a small thumbnail and a wide banner.",
  ].join("\n");
}

// Models to try in order (doc references gpt-image-2; fall back to gpt-image-1).
const MODELS = ["gpt-image-2-2026-04-21", "gpt-image-1"];
const SIZE = "1536x1024"; // landscape; closest supported to a wide header

function loadApiKey() {
  const envPath = join(homedir(), ".claude", "api_keys.env");
  const txt = readFileSync(envPath, "utf8");
  for (const line of txt.split("\n")) {
    const m = line.match(/^OPENAI_API_KEY=(.+)$/);
    if (m && m[1].trim()) return m[1].trim();
  }
  throw new Error("OPENAI_API_KEY not found in ~/.claude/api_keys.env");
}

async function generateOne(apiKey, slug, concept) {
  const prompt = buildPrompt(concept);
  let lastErr;
  for (const model of MODELS) {
    const res = await fetch("https://api.openai.com/v1/images/generations", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({ model, prompt, size: SIZE, n: 1 }),
    });
    if (res.ok) {
      const data = await res.json();
      const b64 = data?.data?.[0]?.b64_json;
      if (!b64) throw new Error(`No image data returned for ${slug}`);
      return { buf: Buffer.from(b64, "base64"), model };
    }
    const errText = await res.text();
    lastErr = `[${model}] ${res.status}: ${errText.slice(0, 300)}`;
    // If the model is unknown/unavailable, try the next; otherwise stop.
    if (res.status !== 404 && res.status !== 400) break;
  }
  throw new Error(`Image API failed for ${slug}: ${lastErr}`);
}

async function main() {
  const manifestPath = process.argv[2];
  if (!manifestPath) {
    console.error("Usage: node scripts/gen-images.mjs <manifest.json> [--note-dir <dir>]");
    process.exit(1);
  }
  const noteIdx = process.argv.indexOf("--note-dir");
  const noteDir = noteIdx !== -1 ? process.argv[noteIdx + 1] : null;

  const jobs = JSON.parse(readFileSync(manifestPath, "utf8"));
  const apiKey = loadApiKey();

  mkdirSync("public/column-images", { recursive: true });
  if (noteDir) mkdirSync(noteDir, { recursive: true });

  let ok = 0;
  for (const { slug, concept } of jobs) {
    if (!slug || !concept) {
      console.error(`SKIP: entry missing slug/concept: ${JSON.stringify({ slug, concept })}`);
      continue;
    }
    try {
      const { buf, model } = await generateOne(apiKey, slug, concept);
      const sitePath = join("public/column-images", `${slug}.png`);
      writeFileSync(sitePath, buf);
      if (noteDir) writeFileSync(join(noteDir, `${slug}.png`), buf);
      ok++;
      console.log(`OK  ${slug}  (${model}, ${SIZE}, ${(buf.length / 1024).toFixed(0)}KB) -> ${sitePath}`);
    } catch (e) {
      console.error(`FAIL ${slug}: ${e.message}`);
    }
  }
  console.log(`Done: ${ok}/${jobs.length} images generated.`);
}

main();
