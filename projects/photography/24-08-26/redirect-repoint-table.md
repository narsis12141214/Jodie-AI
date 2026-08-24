# Redirect Repoint Table — WP Redirection Plugin Session
Date: 24 August 2026 · Source: migration forensics report (same day)
Est. time: 15-20 minutes in WP Admin → Tools → Redirection
Rule of thumb applied: every source points DIRECTLY at its final 200 destination, always on `https://www.` — no chains, no non-www hops, no homepage dumps.

## A. Flatten the chains (edit existing rules)

| # | Source URL | Currently does | Change target to |
|---|---|---|---|
| 1 | `/couple-engagement-photo-shoot-prices/` | → /elopement-wedding-packages → chain | `https://www.hadiphotographylondon.com/london-elopement-packages` |
| 2 | `/family-photography-packages-prices/` | → NON-WWW /elopement-wedding-packages → chain (3 hops) | `https://www.hadiphotographylondon.com/london-elopement-packages` |
| 3 | `/portrait-fashion-photography-prices/` | → NON-WWW /elopement-wedding-packages → chain (3 hops) | `https://www.hadiphotographylondon.com/london-elopement-packages` |
| 4 | `/investment/` | → /elopement-wedding-packages → chain | `https://www.hadiphotographylondon.com/london-elopement-packages` |

(Leave `/elopement-wedding-packages` → `/london-elopement-packages` itself in place as a catch-all for any stragglers. Leave `/london-wedding-photography-packages-prices/` alone — it already lands in one hop.)

## B. Fix the homepage dumps (edit existing rules — homepage redirects are treated as soft 404s and pass nothing)

| # | Source URL | Currently does | Change target to |
|---|---|---|---|
| 5 | `/london-elopement-photography` | → homepage | `https://www.hadiphotographylondon.com/london-elopement-packages` |
| 6 | `/education/` | → homepage | `https://www.hadiphotographylondon.com/lightroom-presets/` |

## C. Add redirects for dead URLs (new rules — currently hard 404s)

| # | Source URL | Currently | New target |
|---|---|---|---|
| 7 | `/gallery/london-pre-wedding-and-engagement-photographer/` | 404 | `https://www.hadiphotographylondon.com/portfolio/` |
| 8 | `/category/couple-photoshoot/` | 404 | `https://www.hadiphotographylondon.com/blog/` |
| 9 | `/category/portraits/` | 404 | `https://www.hadiphotographylondon.com/blog/` |
| 10 | `/shop/` | 404 | `https://www.hadiphotographylondon.com/lightroom-presets/` |

## D. While you're in WP Admin (same session)

- **Rank Math sitemap check:** find why `/blog/best-engagement-photo-locations-london/` and `/blog/male-street-fashion-photography-in-london-correy/` are excluded from post-sitemap.xml (per-post "Exclude from sitemap" setting in the Rank Math meta box, or the Advanced tab robots settings). Both are live + indexable and should be listed.
- **⚠️ Before touching the Redirection plugin, EXPORT the current rules** (Redirection → Import/Export → Export all → CSV) and email the file to yourself. The June incident (plugin deletion wiped all rules, needed a Showit database restore) must never repeat. 30 seconds of insurance.

## Verification (Jodie, after Hadi's session)
I'll re-run the curl sweep on all 10 sources and confirm every one lands in exactly one hop on a 200 at `https://www.`. Just tell me when done.
