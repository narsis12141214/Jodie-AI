# SEO Week 1 — Migration Forensics Report
Date: 24 August 2026 (scorecard execution item: weeks 1-2, migration forensics + indexation plumbing)
Method: live curl audit of hostname/canonical layer, all sitemaps, robots meta; Wayback Machine CDX inventory of pre-Nov-2024 URLs tested against current status codes.

---

## HEALTHY (verified, no action)

- **Hostname canonicalisation is clean.** http → https and non-www → www both 301 in one hop. Single canonical host: `https://www.hadiphotographylondon.com`. No hostname splits (this also weakens the "branded-term technical problem" theory — good).
- **Sitemap index + all 5 sub-sitemaps valid.** Proper XML, correct content-type, 200s. The June Showit Support fix has held. robots.txt correctly references sitemap_index.xml.
- **Most pre-rebrand URLs redirect sensibly.** Old blog-at-root URLs → /blog/ equivalents (correct). /about-me/ → /about. /booking/ → /contact. Old service pages → current equivalents.
- **Showit money pages are indexable** (no robots meta = default index). Blog posts carry explicit index,follow.

## ISSUES FOUND (ranked by impact)

### 1. Showit service pages are in NO sitemap — the money pages are crawl orphans
The Rank Math sitemap covers only WordPress content (14 posts, 9 WP pages — mostly WooCommerce plumbing like /cart/ and /checkout/). **Not in any sitemap:** `/about`, `/contact`, `/london-elopement-packages`, `/london-engagement-photographer`, `/portrait-photographer-london`, `/portfolio` behaviour unclear, and any other Showit front-end page. This is the April flag, still unfixed. Google discovers them anyway, but they get no sitemap crawl signals, no lastmod, and GSC coverage reporting for them is weaker.
**Fix:** inject the Showit URLs into the WP sitemap (Rank Math filter snippet, ~15 mins with WP admin) OR hand-build a supplementary `showit-pages.xml`, upload via WP, submit in GSC. I'll prepare the exact snippet/file when Hadi confirms WP admin access.

### 2. Redirect chains on the old pricing pages (up to 3 hops, one via non-www)
`/family-photography-packages-prices/` → `https://hadiphotographylondon.com/elopement-wedding-packages` (non-www!) → www → `/london-elopement-packages`. Same pattern for `/portrait-fashion-photography-prices/` and `/couple-engagement-photo-shoot-prices/` and `/investment/` via `/elopement-wedding-packages` (which itself 301s). Chains dilute signals and waste crawl.
**Fix (Redirection plugin, 10 mins):** repoint these 4+ source URLs DIRECTLY to `https://www.hadiphotographylondon.com/london-elopement-packages` in one hop. Also fix the two rules that point at the non-www host.

### 3. Homepage-dump redirects = soft-404 signals (pass nothing, per Mueller)
- `/education/` → homepage
- `/london-elopement-photography` → homepage (May "cannibalisation fix" — but a homepage dump passes no equity)
**Fix:** repoint `/london-elopement-photography` → `/london-elopement-packages` (or the elopement guide post); `/education/` → `/lightroom-presets/` (its closest heir) or accept the loss consciously.

### 4. Dead pre-rebrand URLs with NO redirect (hard 404s, equity abandoned)
- `/gallery/london-pre-wedding-and-engagement-photographer/` → 404 (aged gallery page, keyword-relevant URL)
- `/category/couple-photoshoot/`, `/category/portraits/` → 404
- `/shop/` → 404 (product pages live on, the shop hub is dead)
**Fix (Redirection plugin):** gallery URL → `/portfolio/`; categories → `/blog/`; `/shop/` → `/lightroom-presets/`.

### 5. Two live, indexable blog posts are absent from post-sitemap
`/blog/best-engagement-photo-locations-london/` and `/blog/male-street-fashion-photography-in-london-correy/` both 200 + index,follow, but not in post-sitemap (14 listed).
**Fix:** Rank Math check in WP admin — likely "exclude from sitemap" flag or post-type quirk on those two posts.

### 6. Legacy 200s worth a content decision later (not urgent)
`/dark-moody/` and `/gallery/` still live from the old site. Thin/orphan risk. Decide in the content phase: refresh, redirect, or leave.

---

## Hadi's parallel checklist (needs your hands/access)

A. **GSC branded-query check (completes the artifact diagnosis):** Search Console → Performance → query "hadi photography london" → last 7 days → note IMPRESSION COUNT. Under ~10 impressions = the 1→27 "drop" was noise, case closed. Also eyeball an incognito search for the brand.
B. **WP admin (20 mins, fixes #2, #3, #4, #5):** Redirection plugin repoints per above + Rank Math sitemap-exclusion check on the two posts. I'll produce the exact old→new redirect table on request.
C. **GBP completeness pass:** primary category, services fields filled, photo count (target 100+), start weekly photo upload habit. Review velocity: decide the ask script for every completed shoot (Steva 10 Oct is the first natural one; Selina 6 Sept if she pays).
D. **Venue list:** every venue you've shot in 10 years (name + rough count of weddings there). Feeds both venue pages and the link-ask list. Even 10 minutes of brain-dump helps.
E. **Confirm sitemap_index.xml is the submitted sitemap in GSC** (and nothing stale alongside it).

## Next Jodie tasks (this week)
- Venue page prep docs for Old Marylebone Town Hall + Chelsea Old Town Hall — NOTE: venue pages are customer-facing copy → Customer-Facing Copy Protocol applies → Step 1 needs Hadi's real material (which weddings shot there, real moments, client words). Will request as part of item D.
- Redirect repoint table for WP (on Hadi's go).
- Rank Math sitemap-injection snippet for the Showit pages (on WP admin confirmation).
- WSJ interview hunt — agent running.

## Scorecard status (30-day items)
- Migration forensics crawl: ✅ DONE (this report). Redirect repairs: pending Hadi's WP session.
- Both sitemaps verified: ✅ DONE — valid, submitted reference in robots.txt; gap = Showit pages (fix identified).
- Branded-query artifact check: 80% done (no hostname split found; GSC impression count = Hadi, item A).
- GBP pass, venue pages, link-ask list: in flight this week.
