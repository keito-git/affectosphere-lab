/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,ts,tsx,md,mdx}"],
  theme: {
    extend: {
      colors: {
        ivory: "#FAFAF7",
        cream: "#F4F0E8",
        stone: "#E2DDD6",
        charcoal: "#1A1A1A",
        // Soft black for navigation: reads as black, one step back
        // from the charcoal used for the current page.
        softink: "#2E2E2E",
        slate: "#6B7280",
        amber: "#C4974A",
        // AA-compliant amber for text on ivory (5.64:1); see global.css.
        "amber-deep": "#7B5E28",
        steel: "#3D6B8C",
        rose: "#B5737A",
        sage: "#6B8F7A",
        deepslate: "#1E2A38",
        // Observation surface: the dark ground the hero and the research map
        // are drawn on.
        ink: "#111318",
        "ink-soft": "#1B2029",
        "ink-line": "#2B3341",
      },
      fontFamily: {
        // Unified serif stack: English uses Times New Roman, Japanese uses
        // Noto Serif JP. The same stack is reused across display / heading /
        // body so Japanese text always renders in a consistent serif.
        display: ['"Times New Roman"', '"Noto Serif JP"', "Times", "serif"],
        serif: ['"Times New Roman"', '"Noto Serif JP"', "Times", "serif"],
        heading: ['"Times New Roman"', '"Noto Serif JP"', "Times", "serif"],
        // Metadata (authors, dates, captions). Same serif as everything else:
        // all Japanese on the site renders in Noto Serif JP.
        sans: ['"Times New Roman"', '"Noto Serif JP"', "Times", "serif"],
        // Instrument labels: counts, coordinates, domain codes, eyebrows.
        // JetBrains Mono is already loaded for <code>.
        label: [
          '"JetBrains Mono"',
          "ui-monospace",
          "SFMono-Regular",
          '"Noto Serif JP"',
          "monospace",
        ],
        // Monospace (kept for <code> / <pre> blocks only).
        mono: ['"JetBrains Mono"', "ui-monospace", "SFMono-Regular", "monospace"],
      },
      maxWidth: {
        // Content: full-bleed.  No outer cap — padding (see .page-x in
        // global.css) provides breathing room, the page uses the entire
        // viewport edge-to-edge like the Ochiai Lab site.
        content: "100%",
        // Prose / manifesto: capped by character count for line-length
        // readability when text is long.
        prose: "65ch",
        manifesto: "58ch",
      },
      spacing: {
        section: "5rem",
        "section-sm": "2.75rem",
      },
      lineHeight: {
        relaxed: "1.7",
        manifesto: "1.85",
      },
      // The whole type scale, one step tighter than Tailwind's default. The
      // reduction grows with the size: captions and labels are left alone,
      // body copy loses a few percent, and headings lose the most, since the
      // display sizes were what kept so little of a page on screen at once.
      // Every size carries its own line-height, because overriding a key here
      // drops Tailwind's paired default.
      fontSize: {
        xs: ["0.75rem", { lineHeight: "1.05rem" }],
        sm: ["0.85rem", { lineHeight: "1.3rem" }],
        base: ["0.95rem", { lineHeight: "1.55rem" }],
        lg: ["1.05rem", { lineHeight: "1.7rem" }],
        xl: ["1.15rem", { lineHeight: "1.65rem" }],
        "2xl": ["1.35rem", { lineHeight: "1.85rem" }],
        "3xl": ["1.6rem", { lineHeight: "2rem" }],
        "4xl": ["1.9rem", { lineHeight: "2.2rem" }],
        "5xl": ["2.4rem", { lineHeight: "1.1" }],
        "6xl": ["2.9rem", { lineHeight: "1.08" }],
        "7xl": ["3.4rem", { lineHeight: "1.05" }],
        // Fluid display via clamp() expressed as a custom value.
        display: ["clamp(2rem, 3.6vw, 3.2rem)", { lineHeight: "1.12", letterSpacing: "-0.02em" }],
        manifesto: ["clamp(2.4rem, 4.4vw, 3.9rem)", { lineHeight: "1.08", letterSpacing: "-0.02em" }],
      },
      transitionDuration: {
        DEFAULT: "200ms",
      },
      boxShadow: {
        card: "0 1px 2px rgba(26,26,26,0.04), 0 1px 1px rgba(26,26,26,0.02)",
        "card-hover":
          "0 10px 20px rgba(26,26,26,0.08), 0 6px 8px rgba(26,26,26,0.04)",
      },
    },
  },
  plugins: [],
};
