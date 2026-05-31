# Affectosphere Lab Website

Static website for **Affectosphere Lab** (情動圏ラボ), the Kansai University research group
led by Keito Inoshita. Built with [Astro](https://astro.build) and
[Tailwind CSS](https://tailwindcss.com).

> **Affectosphere** = *affect* + *sphere*. The atmospheric envelope of emotion that
> quietly shapes individuals and societies. The lab studies it through three pillars:
> ubiquity, measurability, and universal well-being.

## Stack

- **Astro** 4.x (static output)
- **Tailwind CSS** 3.x via `@astrojs/tailwind`
- **TypeScript** (strict)
- Google Fonts: EB Garamond / DM Sans / Inter / JetBrains Mono
- Vanilla JS only (no React/Vue/etc.); progressive enhancement via
  `IntersectionObserver` for scroll reveals.

## Getting started

```bash
# from the project root
cd /Users/ishitatakashishou/Desktop/研究/affectosphere-lab

# 1. Install dependencies (one-time)
npm install

# 2. Start the dev server (default: http://localhost:4321)
npm run dev

# If port 4321 is taken, pass an alternative:
npm run dev -- --port 4322

# 3. Build a static production bundle into ./dist
npm run build

# 4. Preview the production build locally
npm run preview
```

## Directory structure

```
affectosphere-lab/
├── astro.config.mjs          # Astro + Tailwind integration
├── tailwind.config.mjs       # Color tokens, typography, spacing
├── tsconfig.json             # strict TS, path aliases (@/, @components/, ...)
├── package.json
├── public/
│   ├── favicon.svg
│   └── robots.txt
└── src/
    ├── components/
    │   ├── Footer.astro
    │   ├── Hero.astro
    │   ├── Nav.astro
    │   ├── NewsItem.astro
    │   ├── PlaceholderPage.astro
    │   ├── PublicationItem.astro
    │   ├── ResearchCard.astro
    │   ├── RevealObserver.astro     # IntersectionObserver fade-in
    │   └── SectionHeader.astro
    ├── data/
    │   ├── news.ts
    │   ├── publications.ts
    │   ├── research.ts
    │   └── site.ts                   # site metadata + nav items
    ├── layouts/
    │   └── BaseLayout.astro          # <html> shell, fonts, nav, footer
    ├── pages/
    │   ├── about.astro               # placeholder
    │   ├── affectosphere.astro       # manifesto page (auto-loads MANIFESTO.md if present)
    │   ├── contact.astro             # placeholder
    │   ├── index.astro               # home (hero + featured sections)
    │   ├── news.astro                # placeholder
    │   ├── publications.astro        # placeholder
    │   └── research.astro            # placeholder
    └── styles/
        └── global.css                # Tailwind layers + design tokens
```

## Design tokens (Tailwind)

| Token        | Hex       | Role                          |
| ------------ | --------- | ----------------------------- |
| `ivory`      | `#FAFAF7` | Page background               |
| `cream`      | `#F4F0E8` | Card surfaces                 |
| `stone`      | `#E2DDD6` | Borders / dividers            |
| `charcoal`   | `#1A1A1A` | Primary text                  |
| `slate`      | `#6B7280` | Secondary text                |
| `amber`      | `#C4974A` | Warm accent (A: 感情の波紋)   |
| `steel`      | `#3D6B8C` | Cool accent (B: 曖昧さの構造) |
| `rose`       | `#B5737A` | Chart accent 1                |
| `sage`       | `#6B8F7A` | Chart accent 2                |
| `deepslate`  | `#1E2A38` | Code background               |

Typography roles:

- **Display / H1** &mdash; EB Garamond (serif), `clamp(2.5rem, 5vw, 4.5rem)`
- **H2 / H3** &mdash; DM Sans
- **Body** &mdash; Inter
- **Mono** &mdash; JetBrains Mono

## The Manifesto page

`/affectosphere` reads from the project-root file `MANIFESTO.md`:

- If `MANIFESTO.md` **exists**, its paragraphs (split on blank lines) are rendered
  inline in EB Garamond at 680px max-width / 1.85 line-height.
- If it does **not** exist, a "マニフェスト準備中 / Coming soon" placeholder is shown.

This lets the prose be edited as plain Markdown without touching the site code.
(For a richer migration path, switch to Astro Content Collections later.)

## TODO

- [ ] **Hero vector field animation.** `src/components/Hero.astro` reserves an
  absolutely-positioned `<div data-hero-vector-field>`; drop in an SVG/Canvas of an
  "emotion vector space" at opacity 0.06–0.10. Marker comment is in place.
- [ ] **MANIFESTO.md content.** Awaiting the lab's authored manifesto.
- [ ] **Profile photo.** Optional: place a `profile.jpg` under `public/images/`
  (e.g. fetched from the existing `keito-git/keito-website` repo) and wire it in
  on `/about`.
- [ ] **Real publication list.** `src/data/publications.ts` currently holds
  placeholder entries; replace with real metadata (and ideally a BibTeX export).
- [ ] **Research pillar pages.** Convert `/research` from placeholder to a
  per-pillar index (Uncertainty / Affective Computing / Society).
- [ ] **Contact form / mailto.** Decide on a contact channel and wire it in.
- [ ] **Deployment.** Configure `site` and `base` in `astro.config.mjs` for the
  chosen target (GitHub Pages, Cloudflare Pages, etc.).
- [ ] **Markdown rendering for /affectosphere.** Current implementation reads the
  raw file and splits on blank lines; switch to a proper Markdown parser
  (e.g. `marked`, or move to Astro Content Collections) when rich formatting is needed.

## License

Content &copy; Affectosphere Lab. Code under MIT (TBD).
