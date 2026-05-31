// SVG → PNG converter for note-export images.
// note.com does not accept SVG uploads, so we rasterize each
// src/note-export/<slug>.svg to a 1200x675 PNG (16:9, suitable
// for note's header-image slot and OGP).
//
// Usage:  node scripts/svg-to-png.mjs

import sharp from "sharp";
import { readdirSync } from "node:fs";
import { join, basename } from "node:path";

const SRC_DIR = "src/note-export";
const WIDTH = 1200;
const HEIGHT = 675;

const svgFiles = readdirSync(SRC_DIR).filter((f) => f.endsWith(".svg"));

if (svgFiles.length === 0) {
  console.log("No SVG files found in", SRC_DIR);
  process.exit(0);
}

console.log(
  `Converting ${svgFiles.length} SVG file(s) to ${WIDTH}x${HEIGHT} PNG...`
);

for (const file of svgFiles) {
  const inputPath = join(SRC_DIR, file);
  const outputPath = inputPath.replace(/\.svg$/, ".png");
  await sharp(inputPath, { density: 300 })
    .resize(WIDTH, HEIGHT, { fit: "cover" })
    .png({ compressionLevel: 9 })
    .toFile(outputPath);
  console.log(`  ✓ ${file} → ${basename(outputPath)}`);
}

console.log("Done.");
