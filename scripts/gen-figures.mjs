// Figure generator for the home page's two field illustrations.
//
// Same house style and same model as the column headers (see gen-images.mjs),
// but for the pair of pictures under "感情の主体": affective computing on the
// left, CAI on the right. The images carry NO text — every label on the page
// is HTML, so nothing can collide with the drawing and both languages work
// from one picture.
//
// Usage:
//   node scripts/gen-figures.mjs [ac|cai ...] [--openai]
//
// Routes through OpenRouter by default (the direct OpenAI account is out of
// credit); --openai uses the OpenAI image API instead.
//
// Output:
//   public/figures/<slug>.png   and   public/figures/<slug>.webp
//
// API keys are read internally from ~/.claude/api_keys.env and are NEVER
// printed or written anywhere.

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { homedir } from "node:os";
import sharp from "sharp";

const PALETTE =
  "cream and off-white background (#F4F0E8 / #FAFAF7), warm amber accent (#C4974A), " +
  "deep charcoal line work (#1A1A1A); at most one muted secondary accent of " +
  "steel-blue (#3D6B8C) or sage (#6B8F7A); no vivid or neon colors";

const STYLE = [
  "Style: clean modern flat vector illustration with confident thin charcoal outlines,",
  "simple geometric shapes with gentle organic curves, cute and friendly without being childish,",
  "soft long shadows, minimal detail, generous negative space, calm editorial tone.",
  `Color palette strictly limited to: ${PALETTE}.`,
  "Hard constraints: absolutely NO text, letters, numbers, words, captions, labels, UI chrome",
  "or writing of any kind anywhere in the image; NO logos, brand marks or trademarks;",
  "NO real or recognizable people; NO copyrighted characters or mascots; NO watermark.",
  "Wide horizontal composition, every element fully inside the frame, nothing cropped at the edges.",
].join("\n");

const FIGURES = {
  ac: [
    "A single wide scene, read left to right.",
    "On the left, one cute simple character: a rounded body, a round head, two dot eyes and a small calm smile.",
    "Three small floating cards rise from the character and travel to the right:",
    "a speech bubble, a framed portrait of a simple smiling face, and a heartbeat ECG waveform line.",
    "The three cards converge into one broad warm amber arrow that enters a cute boxy robot on the right,",
    "a rounded rectangular body with a simple screen face, two round eyes and a flat mouth, small feet.",
    "A second, thinner charcoal arrow curves back along the bottom from the robot to the character.",
    "The person is the one holding the feeling; the robot is reading it and answering.",
  ].join(" "),
  cai: [
    "A single wide scene with NO human beings anywhere, only one machine.",
    "In the centre, one cute robot with a large round head seen from the front.",
    "The upper half of the head is open like a clean cross-section, revealing a small network of",
    "round nodes joined by thin lines inside the head; three of those nodes glow warm amber and the",
    "rest are plain outlined circles. The lower half of the head keeps two dot eyes and a small smile,",
    "and a small body with little feet sits below.",
    "Three tools reach toward the inside of the head from outside, without touching the face:",
    "from the left a rounded capsule pouring a stream of warm amber light into the network,",
    "from the upper right a magnifying glass examining one glowing node,",
    "from the lower right a round control dial with a pointer adjusting another glowing node.",
    "The feeling lives inside the machine and is being given, found and tuned there.",
  ].join(" "),
  "ac-face": [
    "A single cute character seen head and shoulders, facing the viewer straight on and centred,",
    "as if framed by a webcam: a rounded head, two dot eyes, a small calm smile, simple shoulders.",
    "Plain uncluttered background with a soft shadow. Nothing else in the frame.",
  ].join(" "),
  "ac-interaction": [
    "A single wide scene with two characters.",
    "On the left a cute rounded person, mid-sentence, with a speech bubble containing a gentle wave line.",
    "On the right a small cute rounded device with a simple screen face, answering with a softer bubble;",
    "a calm curve glows warm amber on its screen.",
    "Between them a low amber band rises and falls like a mood meter following the conversation.",
    "The machine is adjusting how it answers to how the person feels.",
  ].join(" "),
  "cai-phenomena": [
    "An abstract cluster of many small rounded shapes floating loosely together, each a slightly",
    "different form and a different muted colour: some round, some wavy, some gently spiky, some soft.",
    "Three faint framing devices overlap the cluster without agreeing with one another:",
    "a set of separate boxes, a pair of crossed axes, and one loose contour drawn around part of it.",
    "Nothing is resolved. No faces, no figures, no characters.",
  ].join(" "),
  "cai-intelligence": [
    "One cute rounded robot with a simple screen face, seen from the front, centred.",
    "Six small round badges are spaced evenly in a ring around it, all the same size,",
    "each holding one simple pictogram: an eye, a small grid, a branching line, a spark,",
    "two arrows facing each other, and a dial with a pointer.",
    "Calm and tidy, plenty of space between the badges.",
  ].join(" "),
  "cai-grounding": [
    "A cute rounded robot lying on its back on a tidy workbench, like a model being worked on,",
    "its front panel open. Four tools are arranged evenly around it, none touching the others:",
    "a blueprint sheet with a drawn outline on it, a small funnel pouring a stream of warm light into the panel,",
    "a magnifying glass held over the opening, and a measuring gauge with a needle.",
    "Workshop calm, soft long shadows.",
  ].join(" "),
  "cai-divergence": [
    "One single object in the centre: a plain rounded card with an ambiguous wavy mark drawn on it.",
    "Four observers are arranged around it at equal distances, each holding up a small flag of a",
    "different muted colour: a cute rounded person on the left, a pair of cute rounded people together",
    "at the top, a small cute machine with a screen face on the right, and a clipboard standing on a",
    "little easel at the bottom. The four flags are clearly different colours from one another.",
  ].join(" "),
  "cai-axes": [
    "A wide scene split into two halves by one thin vertical line.",
    "On the left, a set of small rounded tokens gathered into four loose uneven piles.",
    "On the right, the very same tokens laid out neatly on a rectangular grid of empty cells,",
    "in tidy rows and columns, one token per cell.",
    "A single curved arrow runs from the left half to the right half, showing the same tokens",
    "being re-arranged rather than replaced.",
  ].join(" "),
  "aff-tracking": [
    "A small town seen from a high angle: plain rooftops, straight streets, a square in the middle.",
    "Soft rounded auras of different muted colours rest over the crossings and the square where the",
    "tiny simple walking figures gather, overlapping gently where they meet.",
    "The town itself is pale and quiet; the auras are what the picture is about.",
  ].join(" "),
  "aff-analysis": [
    "The soft coloured auras of a town lifted off it and separated into three flat horizontal sheets,",
    "stacked one above the other in the air, each sheet thin and translucent and carrying part of the",
    "pattern. The small pale rooftops of the town sit far below. Thin guide lines connect the sheets.",
  ].join(" "),
  "aff-personal": [
    "One cute rounded person walking alone along a quiet street, centred.",
    "The surroundings are quietly adjusting to them: a street lamp glowing warmer, a shopfront sign",
    "dimming, a small rounded device on a post turned to face them, a bench with a softened light.",
    "Thin warm guide lines run inward from each of these toward the person.",
  ].join(" "),
  "aff-sovereignty": [
    "A cute rounded person standing in the centre, holding a small dial in both hands close to their chest,",
    "a thin warm line running from the dial into them. Three small rounded machines stand around them,",
    "each holding up a card with a different simple mark on it, offering it. None of the cards is connected",
    "to the person. The dial is the only thing that is.",
  ].join(" "),
  "cai-fluctuation": [
    "A row of upright bars of different heights standing in a line, like a probability distribution.",
    "A soft warm wave passes through the row from the left, and where it has passed the bars lean and",
    "change height: some risen, some sunk, the tallest one no longer the tallest.",
    "Ahead of the row, several faint paths branch away in different directions instead of one single path.",
    "Abstract and calm. No faces, no figures, no characters.",
  ].join(" "),
  "ethics-philosophy-flat": [
    "Six thin horizontal slabs stacked one above the other with clear gaps between them, seen slightly from the side, like the layers of one system. Between the third and the fourth the gap is wider than the rest, and a small pair of scales rests in that gap, tilted. No people, no faces.",
    "All of it sits in a band across the middle of the frame, with generous empty space above and below, so that a wide crop through the centre still reads.",
  ].join(" "),
  "human-emotion-understanding-flat": [
    "Three cute rounded people standing side by side, each holding up a small card with a different simple mark on it. In front of all three, one single small object they are all looking at. The three cards clearly disagree.",
    "All of it sits in a band across the middle of the frame, with generous empty space above and below, so that a wide crop through the centre still reads.",
  ].join(" "),
  "emotion-recognition-flat": [
    "A cute rounded robot on the right holding a lens up to a small framed portrait card on the left. Between them, a short row of upright bars of different heights, like an estimate forming.",
    "All of it sits in a band across the middle of the frame, with generous empty space above and below, so that a wide crop through the centre still reads.",
  ].join(" "),
  "interpretability-flat": [
    "A cute rounded robot head drawn open in cross-section, showing a small network of nodes and links inside. One single path through the network is traced in warm amber from one side to the other, while the rest of the links stay pale.",
    "All of it sits in a band across the middle of the frame, with generous empty space above and below, so that a wide crop through the centre still reads.",
  ].join(" "),
  "data-augmentation-flat": [
    "One small solid card on the left, and to its right the same card repeated many times in a widening fan, each repeat lighter and slightly different from the last. The original is crisp; the copies are soft.",
    "All of it sits in a band across the middle of the frame, with generous empty space above and below, so that a wide crop through the centre still reads.",
  ].join(" "),
  "human-ai-interaction-flat": [
    "A cute rounded person on the left and a cute rounded robot on the right, facing each other across a low table. A soft band of warm colour passes between them in both directions, crossing over the table.",
    "All of it sits in a band across the middle of the frame, with generous empty space above and below, so that a wide crop through the centre still reads.",
  ].join(" "),
  "business-flat": [
    "A cute rounded robot on one side of a low counter handing a small glowing token across it to a cute rounded person on the other side. Behind them a simple line rises in steps.",
    "All of it sits in a band across the middle of the frame, with generous empty space above and below, so that a wide crop through the centre still reads.",
  ].join(" "),
  "affective-ai-art-flat": [
    "A cute rounded robot holding a brush, painting a long flowing ribbon of warm colour onto a canvas standing on a simple easel. The ribbon leaves the canvas at one end and curls into the air.",
    "All of it sits in a band across the middle of the frame, with generous empty space above and below, so that a wide crop through the centre still reads.",
  ].join(" "),
  "application-development-flat": [
    "Small modular blocks of different shapes laid out on a workbench on the left, and on the right the same blocks assembled into one small rounded device with a simple screen face. A few loose blocks still wait in between.",
    "All of it sits in a band across the middle of the frame, with generous empty space above and below, so that a wide crop through the centre still reads.",
  ].join(" "),
  "other-ai-research-flat": [
    "A loose row of small objects that plainly do not belong to one family: a gear, a leaf, a magnifying glass, a dice, a tuning fork, a small cloud. They are spaced evenly and share no connecting line.",
    "All of it sits in a band across the middle of the frame, with generous empty space above and below, so that a wide crop through the centre still reads.",
  ].join(" "),
  "ai-for-science-flat": [
    "Five small instruments arranged in a wide ring: a leaf, a ballot box, a gavel, a test tube and a school bell. A thin warm line runs inward from each of them to one shared rounded form at the centre.",
    "All of it sits in a band across the middle of the frame, with generous empty space above and below, so that a wide crop through the centre still reads.",
  ].join(" "),
};

const MODELS = ["gpt-image-2-2026-04-21", "gpt-image-1"];
// OpenRouter exposes image-output models through chat completions.
const OR_MODELS = ["openai/gpt-5.4-image-2", "google/gemini-3-pro-image"];
const SIZE = "1536x1024";
const OUT = (() => {
  const i = process.argv.indexOf("--dir");
  return i > -1 && process.argv[i + 1] ? process.argv[i + 1] : "public/figures";
})();

function loadKey(name) {
  const txt = readFileSync(join(homedir(), ".claude", "api_keys.env"), "utf8");
  for (const line of txt.split("\n")) {
    const m = line.match(new RegExp(`^${name}=(.+)$`));
    if (m && m[1].trim()) return m[1].trim();
  }
  throw new Error(`${name} not found in ~/.claude/api_keys.env`);
}

async function generateViaOpenRouter(apiKey, slug) {
  const prompt = `${FIGURES[slug]}\n${STYLE}`;
  let lastErr;
  for (const model of OR_MODELS) {
    const res = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${apiKey}` },
      body: JSON.stringify({
        model,
        messages: [{ role: "user", content: prompt }],
        modalities: ["image", "text"],
      }),
    });
    if (res.ok) {
      const data = await res.json();
      const msg = data?.choices?.[0]?.message;
      const url = msg?.images?.[0]?.image_url?.url;
      if (!url) {
        lastErr = `[${model}] no image in response: ${JSON.stringify(data).slice(0, 300)}`;
        continue;
      }
      const b64 = url.slice(url.indexOf(",") + 1);
      return { buf: Buffer.from(b64, "base64"), model };
    }
    lastErr = `[${model}] ${res.status}: ${(await res.text()).slice(0, 300)}`;
  }
  throw new Error(lastErr || `Generation failed for ${slug}`);
}

async function generateOne(apiKey, slug) {
  const prompt = `${FIGURES[slug]}\n${STYLE}`;
  let lastErr;
  for (const model of MODELS) {
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
    const errText = await res.text();
    lastErr = `[${model}] ${res.status}: ${errText.slice(0, 300)}`;
    if (res.status !== 404 && res.status !== 400) break;
  }
  throw new Error(lastErr || `Generation failed for ${slug}`);
}

const args = process.argv.slice(2);
const useOpenAI = args.includes("--openai");
const slugs = args.filter(s => s in FIGURES);
const targets = slugs.length ? slugs : Object.keys(FIGURES);
const apiKey = loadKey(useOpenAI ? "OPENAI_API_KEY" : "OPENROUTER_API_KEY");
mkdirSync(OUT, { recursive: true });

for (const slug of targets) {
  const { buf, model } = useOpenAI
    ? await generateOne(apiKey, slug)
    : await generateViaOpenRouter(apiKey, slug);
  writeFileSync(join(OUT, `${slug}.png`), buf);
  // Keep the native size: the model returns 1024 square, upscaling buys nothing.
  await sharp(buf).webp({ quality: 86 }).toFile(join(OUT, `${slug}.webp`));
  console.log(`${slug}: ${model} -> ${OUT}/${slug}.png + .webp`);
}
