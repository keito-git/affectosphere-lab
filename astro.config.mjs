import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  // Static output by default. Set `site` and `base` when deploying to GitHub Pages.
  site: "https://example.com",
  integrations: [
    tailwind({
      // Inject Tailwind base styles via a custom entrypoint so we can layer
      // our own CSS variables and font-face declarations on top.
      applyBaseStyles: false,
    }),
  ],
  build: {
    format: "directory",
  },
});
