// Helpers for serving the WebP variants produced by scripts/optimize-images.mjs.
//
// Every raster under public/ has "<name>-800.webp" and "<name>-1600.webp"
// siblings. Templates keep referencing the original path and call these
// helpers to pick a variant, so the source files stay untouched on disk.

import rawDimensions from "../data/image-dimensions.json";

type Dimension = { width: number | null; height: number | null };

const dimensions = rawDimensions as Record<string, Dimension>;

export type VariantWidth = 800 | 1600;

/** Path of the WebP variant for a public/ image at the given width. */
export function webp(src: string, width: VariantWidth = 800): string {
  const dot = src.lastIndexOf(".");
  if (dot === -1) return src;
  return `${src.slice(0, dot)}-${width}.webp`;
}

/**
 * srcset for the variants that actually exist. Sources narrower than 1600px
 * get no wide variant (the optimiser never upscales), so listing one here
 * would point the browser at a 404.
 */
export function webpSrcset(src: string): string {
  const { width } = intrinsic(src);
  const small = `${webp(src, 800)} 800w`;
  if (width !== null && width <= 800) return small;
  // The wide variant is capped at the source width, so advertise that width.
  const wide = width !== null ? Math.min(width, 1600) : 1600;
  return `${small}, ${webp(src, 1600)} ${wide}w`;
}

/**
 * Intrinsic size of the source image, used to set width/height and stop
 * layout shift. Paths may arrive percent-encoded (Japanese filenames), so
 * both spellings are tried before giving up.
 */
export function intrinsic(src: string): Dimension {
  if (dimensions[src]) return dimensions[src];
  try {
    const decoded = decodeURIComponent(src);
    if (dimensions[decoded]) return dimensions[decoded];
  } catch {
    // Malformed escape sequence: fall through to the empty result.
  }
  return { width: null, height: null };
}
