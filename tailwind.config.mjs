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
        slate: "#6B7280",
        amber: "#C4974A",
        steel: "#3D6B8C",
        rose: "#B5737A",
        sage: "#6B8F7A",
        deepslate: "#1E2A38",
      },
      fontFamily: {
        // Unified serif stack: English uses Times New Roman, Japanese uses
        // Noto Serif JP. The same stack is reused across display / heading /
        // body so Japanese text always renders in a consistent serif.
        display: ['"Times New Roman"', '"Noto Serif JP"', "Times", "serif"],
        serif: ['"Times New Roman"', '"Noto Serif JP"', "Times", "serif"],
        heading: ['"Times New Roman"', '"Noto Serif JP"', "Times", "serif"],
        sans: ['"Times New Roman"', '"Noto Serif JP"', "Times", "serif"],
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
        section: "8rem",
        "section-sm": "4rem",
      },
      lineHeight: {
        relaxed: "1.7",
        manifesto: "1.85",
      },
      fontSize: {
        // Fluid display via clamp() expressed as a custom value.
        display: ["clamp(2.5rem, 5vw, 4.5rem)", { lineHeight: "1.1", letterSpacing: "-0.02em" }],
        manifesto: ["clamp(3rem, 6vw, 5.5rem)", { lineHeight: "1.05", letterSpacing: "-0.02em" }],
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
