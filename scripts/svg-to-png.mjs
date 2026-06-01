// SVG → PNG converter for note-export images.
// note.com does not accept SVG uploads, so we rasterize each
// src/note-export/**/<slug>.svg to a 1200x675 PNG (16:9).
//
// Recursively walks src/note-export/ so per-day folders
// (e.g. src/note-export/2026-06-02/foo.svg) are picked up.
//
// Usage:  npm run notes:images
//   or:   node scripts/svg-to-png.mjs

import sharp from "sharp";
import { readdirSync, statSync } from "node:fs";
import { join, basename } from "node:path";

const SRC_DIR = "src/note-export";
const WIDTH = 1200;
const HEIGHT = 675;

function walkSvgs(dir) {
  const out = [];
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) {
      out.push(...walkSvgs(full));
    } else if (entry.endsWith(".svg")) {
      out.push(full);
    }
  }
  return out;
}

const svgFiles = walkSvgs(SRC_DIR);

if (svgFiles.length === 0) {
  console.log("No SVG files found under", SRC_DIR);
  process.exit(0);
}

console.log(
  `Converting ${svgFiles.length} SVG file(s) to ${WIDTH}x${HEIGHT} PNG...`
);

for (const inputPath of svgFiles) {
  const outputPath = inputPath.replace(/\.svg$/, ".png");
  await sharp(inputPath, { density: 300 })
    .resize(WIDTH, HEIGHT, { fit: "cover" })
    .png({ compressionLevel: 9 })
    .toFile(outputPath);
  console.log(`  ✓ ${inputPath} → ${basename(outputPath)}`);
}

console.log("Done.");
