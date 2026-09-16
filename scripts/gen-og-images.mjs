// Render one Open Graph card per top-level page.
//
// Every page used to share a single og/default.png, so a link to the research
// map and a link to the contact form looked identical when shared. This draws
// the page's own title on the lab's concentric mark and writes it to
// public/og/, plus a manifest the layout reads to pick the right card.
//
// Requires a built site (dist/) for the titles, and Chrome for rendering.
//
// Usage:  node scripts/gen-og-images.mjs

import { readFile, writeFile, mkdir, rm } from "node:fs/promises";
import { existsSync } from "node:fs";
import { execFile } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { promisify } from "node:util";
import sharp from "sharp";

const run = promisify(execFile);
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const DIST = path.join(ROOT, "dist");
const OUT = path.join(ROOT, "public", "og");
const TMP = path.join(ROOT, ".og-tmp");

const CHROME_CANDIDATES = [
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  "/Applications/Chromium.app/Contents/MacOS/Chromium",
  "/usr/bin/google-chrome",
  "/usr/bin/chromium",
];

// Pages that get their own card. Everything else falls back to default.png.
const PAGES = [
  "", "affectosphere", "research", "publications", "column", "news",
  "about", "member", "awards", "grants", "ai-for-science", "services", "contact",
];

const chrome = CHROME_CANDIDATES.find((p) => existsSync(p));
if (!chrome) {
  console.error("No Chrome binary found; skipping OG generation.");
  process.exit(0);
}

/** Title as rendered, minus the site-name suffix. */
async function titleOf(relPath) {
  const file = path.join(DIST, relPath, "index.html");
  if (!existsSync(file)) return null;
  const html = await readFile(file, "utf8");
  const m = html.match(/<title>(.*?)<\/title>/s);
  if (!m) return null;
  return m[1].replace(/\s*\|\s*Affectosphere Group$/, "").trim();
}

function card({ title, kicker, tagline }) {
  // Inline everything: the renderer loads this file directly off disk.
  return `<!doctype html><html><head><meta charset="utf-8"><style>
  @page { margin: 0 }
  * { margin: 0; padding: 0; box-sizing: border-box }
  body {
    width: 1200px; height: 630px; background: #111318; color: #F4F2ED;
    font-family: "Hiragino Mincho ProN", "Times New Roman", serif;
    position: relative; overflow: hidden;
  }
  .grid {
    position: absolute; inset: 0;
    background-image:
      linear-gradient(to right, rgba(233,230,223,.05) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(233,230,223,.05) 1px, transparent 1px);
    background-size: 72px 72px;
  }
  svg { position: absolute; left: 50%; top: 50%; transform: translate(-50%,-50%); }
  .inner { position: relative; height: 100%; padding: 74px 88px; display: flex; flex-direction: column; }
  .kicker {
    font-family: "SF Mono", ui-monospace, monospace; font-size: 20px;
    letter-spacing: .22em; color: #9AA4B4; text-transform: uppercase;
  }
  h1 { margin-top: auto; font-size: ${title.length > 26 ? 62 : 78}px; line-height: 1.24; font-weight: 600; letter-spacing: -.01em; }
  .tagline { margin-top: 26px; font-size: 27px; line-height: 1.6; color: #CFCBC2; max-width: 30ch; }
  .foot {
    margin-top: auto; padding-top: 34px; display: flex; justify-content: space-between;
    align-items: baseline; border-top: 1px solid #2B3341;
    font-family: "SF Mono", ui-monospace, monospace; font-size: 19px;
    letter-spacing: .12em; color: #6E7889;
  }
  .amber { color: #C4974A }
  </style></head><body>
  <div class="grid"></div>
  <svg width="900" height="900" viewBox="0 0 200 200" fill="none">
    <g stroke="#E9E6DF" stroke-width=".25" opacity=".26">
      <circle cx="100" cy="100" r="26"/><circle cx="100" cy="100" r="44"/>
      <circle cx="100" cy="100" r="64"/><circle cx="100" cy="100" r="86"/>
    </g>
    <circle cx="100" cy="100" r="26" stroke="#C4974A" stroke-width=".45" opacity=".55"/>
  </svg>
  <div class="inner">
    <p class="kicker">${kicker}</p>
    <h1>${title}</h1>
    ${tagline ? `<p class="tagline">${tagline}</p>` : ""}
    <div class="foot"><span>Affectosphere <span class="amber">Group</span></span><span>lab.affectosphere.group</span></div>
  </div>
  </body></html>`;
}

async function render(html, outPath) {
  const tmpHtml = path.join(TMP, "card.html");
  const tmpPng = path.join(TMP, "card.png");
  await writeFile(tmpHtml, html, "utf8");
  await run(chrome, [
    "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
    "--force-device-scale-factor=1", "--window-size=1200,630",
    `--screenshot=${tmpPng}`, "--virtual-time-budget=4000",
    `file://${tmpHtml}`,
  ]).catch(() => {});
  if (!existsSync(tmpPng)) throw new Error(`render failed for ${outPath}`);
  await sharp(tmpPng).png({ quality: 88, compressionLevel: 9 }).toFile(outPath);
}

async function main() {
  await mkdir(OUT, { recursive: true });
  await mkdir(TMP, { recursive: true });

  const manifest = {};
  for (const locale of ["ja", "en"]) {
    for (const page of PAGES) {
      const rel = locale === "en" ? path.join("en", page) : page;
      const title = await titleOf(rel);
      if (!title) continue;

      const isHome = title === "Affectosphere Group";
      const name = `${locale}-${page || "home"}.png`;
      await render(
        card({
          kicker: isHome ? "Affectosphere Group / CAI" : "Affectosphere Group",
          title: isHome
            ? (locale === "en"
                ? "Computational Affective Intelligence"
                : "世界一の CAI をつくる。")
            : title,
          tagline: isHome
            ? (locale === "en"
                ? "Building the world's most advanced Computational Affective Intelligence."
                : "感情を確率として測り、人の感情知性を高める側へ AI を据え直す。")
            : "",
        }),
        path.join(OUT, name),
      );
      const urlPath = locale === "en" ? `/en/${page ? page + "/" : ""}` : `/${page ? page + "/" : ""}`;
      manifest[urlPath] = `/og/${name}`;
      process.stdout.write(`  ${urlPath} -> og/${name}\n`);
    }
  }

  await writeFile(
    path.join(ROOT, "src", "data", "og-images.json"),
    JSON.stringify(manifest, null, 2) + "\n",
    "utf8",
  );
  await rm(TMP, { recursive: true, force: true });
  console.log(`\n${Object.keys(manifest).length} cards written to public/og/`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
