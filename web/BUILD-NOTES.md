# Astro prototype — build notes
Built 11 September 2026. Purpose: let Hadi judge the platform on evidence rather than description.

## Run it
```bash
cd web && npm install && npm run dev
```
Laptop: http://localhost:4321  ·  Phone on the same wifi: http://192.168.1.205:4321

## Measured results

| | Showit today | This prototype |
|---|---|---|
| HTML weight | 492 KB | **21.8 KB** (6.5 KB gzipped) |
| JavaScript | Showit runtime | **4.6 KB**, no dependencies |
| Sitemap | Money pages in none | Generated from the route manifest |
| Build | n/a | 136 ms |
| Content without JS | Renders | Renders (535 words, h1, 2× h2, JSON-LD) |

## Copy provenance — what is locked and what is not

**Locked, used verbatim:**
| Element | Source |
|---|---|
| Hero H1 "Your love has a city. / Let it live in the photographs the way it lives in you." | Block 1 Hero, LOCKED 5 June (decisions.md) |
| Hero subhead "…the city stands as a witness to the relationship, not a backdrop for it." | Block 1, LOCKED 5 June |
| CTA "Begin with a message" | Block 1, LOCKED 5 June |
| Statement "Twenty years of photojournalism… the breath before the laugh." | Brand voice reference paragraph, LOCKED 4 June |
| The three "Perhaps…" panels | Brand voice reference paragraph, LOCKED 4 June. The locked copy already has three parallel clauses, which is why the pinned sequence fits it exactly. |
| Resolve line | Locked UVP, 2 June |
| Guide section | Brand Story Guide + the prompt-not-pose positioning, LOCKED 4 June / 12 June |

⚠️ **NOT locked, prototype only, needs Hadi's green-light before it goes near production:**
- The three **concern cards** (touristy / crowds / weather). Drafted from Hadi's verbatim Step 1 input in `projects/photography/20-06-26/prep-block-3-myth-busting.md` and his own weather answer in `.claude/agents/shared/objections.md`, so the source material is real. But Block 3 was never locked and this copy has not been through the Customer-Facing Copy Protocol green-light. **Treat as placeholder.**
- Gallery captions. Location names read off the original filenames, not confirmed by Hadi.
- `hello@hadiphotographylondon.com` is a guess. Needs the real address or a form.

## Images
14 photographs pulled from Hadi's own live site, plus the WSJ, Forbes and Airbnb press logos he already displays there. His own work, used for his own prototype. Unoptimised originals at 4.2 MB total — production would run them through `astro:assets` for AVIF/WebP and responsive `srcset`, which typically cuts that by 70 to 85%.

## What the motion actually does
Everything continuous runs through **one rAF-throttled scroll pass**. Discrete reveals use IntersectionObserver so they work in every browser.

1. **Scroll progress bar** — native `animation-timeline: scroll()` where supported, JS fallback otherwise
2. **Hero** — masked line-by-line type on load, image drifts and scales as you leave
3. **Statement** — line-by-line mask reveal
4. **Pinned three-way** — the showpiece. Section pins for three viewport heights while the three "Perhaps" lines cross-fade over three cross-fading photographs
5. **Concern cards** — staggered reveal
6. **Horizontal gallery** — vertical scroll drives horizontal movement, greyscale to colour on hover
7. **Guide portrait** — parallax inside its frame
8. **Chapter rail** — right-hand dots track the active section, click to jump

`prefers-reduced-motion` is fully honoured: the pinned section unstacks into a normal vertical list, all transforms are dropped, nothing is lost.

## Deliberately not done
Not a full site. One page, to answer one question. No blog templates, no service pages, no contact form, no image optimisation, no analytics, no deployment.

## If Hadi says yes
1. Confirm the Showit renewal notice window (still unchecked, still the binding constraint)
2. Full URL inventory + 1:1 redirect map
3. Migrate the 13 blog posts to `/blog/[slug]/`, paths unchanged
4. WordPress and WooCommerce move to `shop.` subdomain
5. Build remaining pages, run `astro:assets` over the images
6. Staging on the VPS, full crawl, cutover, then GSC monitoring daily for two weeks
