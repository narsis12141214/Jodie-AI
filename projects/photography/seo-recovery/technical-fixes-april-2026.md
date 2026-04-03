# SEO Technical Fixes — April 2026
Generated: 3 April 2026
Priority: Complete before any new blog content. All four tasks below.

---

## JODIE TASKS (done)

### Task 1 — Meta Descriptions (paste into Showit SEO settings for each page)

**Homepage**
Page: hadiphotographylondon.com
Primary keyword: london elopement photographer
Meta description (150 chars):
```
Hadi is a London elopement photographer specialising in intimate couples photography. Based in London, available for elopements and weddings worldwide.
```

---

**Engagement Photography Page**
Page: hadiphotographylondon.com/engagement-photography (or equivalent Showit page)
Primary keyword: london engagement photoshoot
Meta description (147 chars):
```
Natural, unposed London engagement photoshoots for couples who want to remember how the day truly felt. Based in London, shooting in every season.
```

---

**Elopement Photographer Page**
Page: hadiphotographylondon.com/london-elopement-photographer (or equivalent)
Primary keyword: london elopement photographer
Meta description (151 chars):
```
London elopement photographer with 100 five-star reviews. Intimate, unhurried elopement photography for couples who want the day to feel like theirs.
```

---

**Elopement Packages Page**
Page: hadiphotographylondon.com/elopement-packages (or equivalent)
Primary keyword: elopement packages london
Meta description (151 chars):
```
Elopement packages in London from £1,800. Ceremony planning, location guidance, and photography in one. Built around your day, not a standard format.
```

---

**Surprise Proposal Blog Post**
Page: hadiphotographylondon.com/how-to-plan-a-surprise-proposal-in-london (WordPress)
Primary keyword: surprise proposal photographer london
Meta description (158 chars):
```
Everything you need to plan a surprise proposal in London, from location and timing to how to work with a surprise proposal photographer. A practical guide.
```

---

### Task 2 — Homepage Title Tag

Current title tag: `London Elopement Photographer | Hadi Photography`
New title tag: `London Couples, Elopement & Proposal Photographer | Hadi Photography`

Where to update: Showit > Pages > Homepage > SEO Settings > Title Tag field
Note: This expands the keyword footprint to cover couples and proposal searches without losing the elopement ranking. Do not shorten or reorder.

---

## HADI TASKS (action required in Showit + Google Search Console)

### Task 3 — Duplicate Elopement Packages Pages — 301 Redirect

Two URLs may be indexed for elopement packages content. You need to:

1. Go to Google Search Console > URL Inspection
2. Search both of these (or similar — check your Showit sitemap for the exact slugs):
   - hadiphotographylondon.com/elopement-packages
   - hadiphotographylondon.com/london-elopement-packages
3. Identify which one has more backlinks or impressions — that is your canonical (keep it)
4. In Showit: go to the duplicate page > Page Settings > Redirect > set 301 to the canonical URL
5. In Google Search Console: Request Removal on the duplicate URL after the redirect is live
6. Allow 2-4 weeks for Google to process

If you are unsure which is the duplicate, share both URLs and I will check Search Console data.

---

### Task 4 — Noindex Flags

The following pages should not be indexed by Google. They add no SEO value and dilute crawl budget.

Pages to noindex:
- hadiphotographylondon.com/editorial-street-fashion (or similar slug)
- hadiphotographylondon.com/lightroom-presets (or similar slug)
- Any /shop/* URLs (e.g. /shop, /shop/cart, /shop/checkout)
- Any /cart and /checkout URLs

How to noindex in Showit:
1. Open Showit > Pages
2. Find each page listed above
3. Page Settings > SEO > uncheck "Allow search engines to index this page" (or equivalent toggle)
4. Publish

For WordPress shop/cart pages:
- If using WooCommerce: Settings > Advanced > Page setup — these are typically noindexed by Yoast automatically. Confirm in Yoast SEO > Search Appearance > Pages.
- If Yoast is not doing it: add `<meta name="robots" content="noindex">` via Yoast's custom meta field on each page.

Confirm once done and I will flag for Search Console removal.

---

## STATUS

- [ ] Task 1 — Meta descriptions — Hadi to paste into Showit/WordPress
- [ ] Task 2 — Homepage title tag — Hadi to update in Showit
- [ ] Task 3 — Duplicate redirect — Hadi to action in Showit + Search Console
- [ ] Task 4 — Noindex flags — Hadi to action in Showit/Yoast

Blog post #6 (london engagement photoshoot) is paused until all four tasks above are confirmed done.
