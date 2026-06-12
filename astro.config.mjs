import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
  // Production URL. Used for sitemap generation, canonical URLs, and og:url.
  // Update if a custom domain is configured later.
  site: "https://lab.affectosphere.group",
  integrations: [
    tailwind({
      // Inject Tailwind base styles via a custom entrypoint so we can layer
      // our own CSS variables and font-face declarations on top.
      applyBaseStyles: false,
    }),
    sitemap(),
  ],
  build: {
    format: "directory",
  },
});
