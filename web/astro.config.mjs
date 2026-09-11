import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.hadiphotographylondon.com',
  // Every route Astro knows about is written into the sitemap at build time.
  // There is no second system to be blind to, which is the whole point.
  integrations: [sitemap()],
  build: { inlineStylesheets: 'always' },
  compressHTML: true,
});
