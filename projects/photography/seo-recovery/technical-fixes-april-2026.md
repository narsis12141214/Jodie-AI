# SEO Technical Fixes — April 2026
Generated: 3 April 2026
Priority: Complete before any new blog content. All four tasks below.

---

## SHOWIT SESSION — 4 APRIL 2026
All copy finalised and ready to paste. Do all three in one Showit session.

### 1. Homepage
**Title tag** (Showit > Pages > Homepage > SEO Settings > Title Tag):
```
London Elopement & Wedding Photographer | Hadi Photography
```
Log Search Console baseline before changing. See monitoring protocol in Task 2 below.

**Meta description** (Showit > Pages > Homepage > SEO Settings > Meta Description):
```
London elopement, wedding and couples photographer. Storytelling photography for romantic couples who want an intentional day in London. 100 five-star reviews.
```
159 chars. Approved 4 April 2026.

---

### 2. Elopement Service Page
Keyword pivot: from "london elopement photographer" (research intent — blog post owns this) to "elopement photography london" (booking intent).

**Title tag:**
```
Elopement Photography London | Hadi Photography
```

**H1** (note: Showit renders headings in JavaScript — Google may not read this from the initial HTML crawl; verify via Search Console coverage report):
```
Elopement Photography in London
```

**Meta description:**
```
Elopement photography in London from £1,800. Intimate storytelling for couples who want their day done their way. 100 five-star reviews.
```
136 chars.

Also add this internal link CTA to the elopement blog post (The Complete Guide 2026):
```
Ready to book? See our elopement photography packages →
```
Link target: the elopement service page URL.

---

### 3. Proposal Service Page
Keyword pivot: from overlap with blog post to "surprise proposal photographer london" (transactional intent).

**Title tag:**
```
Surprise Proposal Photographer London | Hadi Photography
```

**H1** (same Showit JS flag applies):
```
Surprise Proposal Photographer in London
```

**Meta description:**
```
Surprise proposal photographer in London. Discreet, experienced, and trusted by 100+ couples. Your moment, captured exactly as it happens.
```
139 chars.

Also add this internal link CTA to the proposal blog post (How to Plan a Surprise Proposal in London):
```
Need a photographer for your proposal? See how we work →
```
Link target: the proposal service page URL.

---

## JODIE TASKS (done)

### Task 1 — Meta Descriptions (paste into Showit SEO settings for each page)

**Homepage**
Page: hadiphotographylondon.com
Primary keywords: london elopement photographer, london wedding photographer, couples photographer london
Meta description (finalised 4 April 2026, 159 chars):
```
London elopement, wedding and couples photographer. Storytelling photography for romantic couples who want an intentional day in London. 100 five-star reviews.
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

**Elopement Service Page**
Page: hadiphotographylondon.com/london-elopement-photographer (or equivalent)
Primary keyword: elopement photography london (PIVOTED — 4 April 2026)
Note: "london elopement photographer" now belongs to the blog post (The Complete Guide 2026). Service page targets booking intent.
See SHOWIT SESSION section above for full title tag, H1, and meta description.

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
New title tag: `London Elopement & Wedding Photographer | Hadi Photography`

Rationale: Search Console confirms homepage impressions and clicks are driven by elopement and wedding queries. Proposal is excluded — dedicated page already competes for that term, no homepage click data justifies inclusion. Elopement leads — it is the brand differentiator and where authority is established. Wedding is included for query breadth, not as the primary positioning signal. "London wedding photographer" is one of the most competitive keyword clusters in the UK — leading with it would put the title in a fight it cannot win from a homepage title change alone, and would dilute the elopement authority that is already built.

Where to update: Showit > Pages > Homepage > SEO Settings > Title Tag field.

Before making this change, log today's baseline in the monitoring table below. Do not change the title without a baseline recorded.

---

### Task 2 — Monitoring Protocol (Title Tag Change)

**Step 1 — Log baseline today (before making any change)**

Go to Google Search Console > Performance > Search Results.
Set date range: last 28 days.
Filter: Page = hadiphotographylondon.com (homepage only).
Record the following:

| Metric | Baseline (date: ___) |
|--------|---------------------|
| Total impressions | |
| Total clicks | |
| Average CTR | |
| Average position | |
| Top 5 queries by clicks | |

Save this table. You need it to measure the change.

**Step 2 — Make the title change in Showit. Record the date.**

Change date: ___________

**Step 3 — Weekly checks (4 weeks post-change)**

Same Search Console view, same homepage filter, 28-day rolling window each time.

| Week | Date checked | Impressions | Clicks | CTR | Avg position | Notes |
|------|-------------|-------------|--------|-----|-------------|-------|
| Baseline | | | | | | Pre-change |
| Week 1 | | | | | | |
| Week 2 | | | | | | |
| Week 3 | | | | | | |
| Week 4 | | | | | | |

**Decision rules at Week 4:**
- CTR improved and impressions stable or growing: change succeeded. Close this task.
- CTR flat, impressions stable: monitor one more week before deciding.
- Impressions dropped more than 10% and have not recovered by Week 3: revert to original title immediately and log in decisions.md.

Log the outcome in `context/decisions.md` at the 4-week mark regardless of result.

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

- [x] Task 1 — Meta descriptions — done 4 April 2026
- [x] Task 2 — Homepage title tag — done 4 April 2026 (log baseline in Search Console monitoring table)
- [x] Task 3 — Duplicate redirect — done 4 April 2026
- [x] Task 4 — Noindex flags — done 4 April 2026. lightroom-presets + cart/checkout/shop noindexed. editorial-street-fashion left indexed intentionally for now.

Blog post #6 (london engagement photoshoot) is paused until all four tasks above are confirmed done.
