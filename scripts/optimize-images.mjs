// Generate responsive WebP variants for every raster image under public/.
//
// The site ships ~535 MB of untouched PNG/JPG in public/, which makes the
// column index alone pull 33 MB over the wire. This script derives two WebP
// widths per source image so templates can serve a <picture>/srcset pair.
//
// Source files are never modified, moved or deleted: the variants are written
// next to the original as "<name>-800.webp" / "<name>-1600.webp". Re-running is
// cheap because variants newer than their source are skipped.
//
// Usage:  node scripts/optimize-images.mjs [--force] [--dir <name>]

import { readdir, stat, mkdir, writeFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import sharp from "sharp";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const PUBLIC_DIR = path.join(ROOT, "public");

// Directories holding rasters that the site actually serves.
const TARGET_DIRS = [
  "column-images",
  "award-images",
  "field-images",
  "research-figures",
  "people",
  "face-images",
  "logo",
];

const WIDTHS = [800, 1600];
const SOURCE_EXT = new Set([".png", ".jpg", ".jpeg"]);

const args = process.argv.slice(2);
const force = args.includes("--force");
const dirFlag = args.indexOf("--dir");
const onlyDir = dirFlag !== -1 ? args[dirFlag + 1] : null;

/** Recursively collect convertible files under a directory. */
async function collect(dir) {
  const out = [];
  let entries;
  try {
    entries = await readdir(dir, { withFileTypes: true });
  } catch {
    return out;
  }
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      out.push(...(await collect(full)));
    } else if (SOURCE_EXT.has(path.extname(entry.name).toLowerCase())) {
      out.push(full);
    }
  }
  return out;
}

/** Variant path for a source file at a given width. */
function variantPath(src, width) {
  const dir = path.dirname(src);
  const base = path.basename(src, path.extname(src));
  return path.join(dir, `${base}-${width}.webp`);
}

/** True when the variant is missing or older than its source. */
async function needsWork(src, out) {
  if (force) return true;
  if (!existsSync(out)) return true;
  const [a, b] = await Promise.all([stat(src), stat(out)]);
  return a.mtimeMs > b.mtimeMs;
}

async function main() {
  const dirs = onlyDir ? [onlyDir] : TARGET_DIRS;
  const dimensions = {};
  let converted = 0;
  let skipped = 0;
  let srcBytes = 0;
  let outBytes = 0;

  for (const dirName of dirs) {
    const dir = path.join(PUBLIC_DIR, dirName);
    const files = await collect(dir);
    if (files.length === 0) continue;
    process.stdout.write(`\n${dirName}: ${files.length} source files\n`);

    for (const src of files) {
      const rel = "/" + path.relative(PUBLIC_DIR, src).split(path.sep).join("/");
      let meta;
      try {
        meta = await sharp(src).metadata();
      } catch (err) {
        process.stdout.write(`  ! unreadable: ${rel} (${err.message})\n`);
        continue;
      }
      // Record intrinsic size so templates can set width/height and avoid CLS.
      dimensions[rel] = { width: meta.width ?? null, height: meta.height ?? null };
      srcBytes += (await stat(src)).size;

      for (const width of WIDTHS) {
        // Never upscale: a 900px-wide source gets no 1600 variant.
        if (meta.width && meta.width < width && width !== WIDTHS[0]) continue;
        const out = variantPath(src, width);
        if (!(await needsWork(src, out))) {
          skipped += 1;
          outBytes += (await stat(out)).size;
          continue;
        }
        await sharp(src)
          .resize({ width, withoutEnlargement: true })
          .webp({ quality: 78, effort: 5 })
          .toFile(out);
        converted += 1;
        outBytes += (await stat(out)).size;
      }
      process.stdout.write(".");
    }
  }

  // Dimension manifest consumed by components that render public/ images.
  const manifestDir = path.join(ROOT, "src", "data");
  await mkdir(manifestDir, { recursive: true });
  await writeFile(
    path.join(manifestDir, "image-dimensions.json"),
    JSON.stringify(dimensions, null, 2) + "\n",
    "utf8",
  );

  const mb = (n) => (n / 1024 / 1024).toFixed(1);
  process.stdout.write(
    `\n\nconverted ${converted}, skipped ${skipped}` +
      `\nsource total   ${mb(srcBytes)} MB` +
      `\nwebp variants  ${mb(outBytes)} MB` +
      `\nwrote src/data/image-dimensions.json (${Object.keys(dimensions).length} entries)\n`,
  );
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
