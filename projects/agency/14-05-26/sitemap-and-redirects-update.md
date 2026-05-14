# Sitemap and Redirect Update — clickaiagency.com

**Date:** 14 May 2026
**Trigger:** Homepage rewrite + 4 segment landing page rewrites/rebuilds with new canonical URLs.
**Owner:** Hadi to apply on Lovable + Google Search Console.

---

## NEW SITEMAP

File: `sitemap.xml` (same folder).

The sitemap includes 5 priority URLs. Add any other live pages (about, contact, privacy, terms, demo, blog) before pushing to Lovable — note added inline in the XML.

### Pages in the new sitemap

| URL | Priority | Change frequency |
|---|---|---|
| `https://clickaiagency.com/` | 1.0 | weekly |
| `https://clickaiagency.com/ai-phone-answering-and-booking-automation-uk-restaurants-cafes` | 0.9 | monthly |
| `https://clickaiagency.com/ai-receptionist-for-uk-dental-practices` | 0.9 | monthly |
| `https://clickaiagency.com/ai-receptionist-for-uk-aesthetic-clinics` | 0.9 | monthly |
| `https://clickaiagency.com/ai-receptionist-uk-gyms-fitness-studios` | 0.9 | monthly |

---

## 301 REDIRECT MAP

Configure these 3 redirects in Lovable (or your DNS/hosting layer) BEFORE submitting URL changes in Google Search Console.

| From (old URL) | To (new URL) |
|---|---|
| `clickaiagency.com/ai-voice-receptionist-restaurants-cafes` | `clickaiagency.com/ai-phone-answering-and-booking-automation-uk-restaurants-cafes` |
| `clickaiagency.com/dental-clinics-ai-voice-receptionist` | `clickaiagency.com/ai-receptionist-for-uk-dental-practices` |
| `clickaiagency.com/ai-voice-receptionist-beauty-aesthetics-clinics` | `clickaiagency.com/ai-receptionist-for-uk-aesthetic-clinics` |

### Redirect rules
- HTTP 301 (permanent), not 302 (temporary)
- Preserve trailing slashes consistently with the canonical URLs in the sitemap
- Test each redirect in an incognito browser before submitting to GSC

### Pages without a redirect
- **Fitness page (`/ai-receptionist-uk-gyms-fitness-studios`)** — net new, never published before. No redirect required.
- **Homepage (`/`)** — canonical URL unchanged, no redirect needed even though copy and structure are rewritten.

---

## EXECUTION ORDER (do in this sequence to avoid SEO damage)

1. **Build all 5 pages in Lovable using the HTML + Lovable prompts in this folder**
2. **Confirm visually** that each page matches the existing brand
3. **Configure 301 redirects** in Lovable
4. **Test redirects** in incognito browser, confirm 301 (not 302, not 404)
5. **Replace sitemap.xml** with the new version (add about/contact/privacy/etc. if those exist)
6. **Submit new sitemap.xml** in Google Search Console
7. **Inspect each new URL** in Google Search Console URL inspection tool, click "Request indexing"
8. **Submit URL change** in GSC for each redirected page (Move tool or change-of-address request where applicable)
9. **Monitor GSC for 14 to 21 days** — equity should pass via the 301s within that window
10. **Update Google Business Profile** website link if it points to any old URL
11. **Audit internal links** across the live site (nav, footer, any other pages, blog posts) — replace old URLs with new

---

## INTERNAL LINK AUDIT

After the rebuilds, the live site likely still has internal links pointing to the OLD URLs. Run a manual check on:

| Location | What to check |
|---|---|
| Top navigation menu | Does any nav link point to `/dental-clinics-ai-voice-receptionist` or similar old URLs? |
| Footer | Any old URLs in the footer industry list? |
| Homepage industry cards | Confirm 4 cards point to new canonical URLs |
| Other landing pages | Cross-links between segment pages must use new URLs |
| Blog posts (if any) | Replace any contextual mentions of old URLs |
| Email signatures | Update Hadi's signature, Zizi's signature, any team signatures |
| Lovable internal redirects | Remove any stale internal redirects pointing to old URLs |
| Outreach scripts (Zizi) | When Zizi sends a link, it must be the new canonical |
| Cold email templates (Instantly) | Same |
| Meta Business / Instagram bio | If the bio link points to a specific landing page, update |
| LinkedIn company page | If any link references the old URLs |
| Marketing PDFs / proposals | Any printed material with old URLs |

Recommend doing this audit in a single 30-minute sweep after the Lovable build is complete and before Zizi's next outreach batch.

---

## GOOGLE SEARCH CONSOLE STEPS (after Lovable build is live)

1. **Submit new sitemap:** GSC → Sitemaps → submit `https://clickaiagency.com/sitemap.xml`
2. **Inspect each new URL** (5 total) → "Request Indexing" button
3. **For each old URL that's been 301'd, use the Change of Address tool** if available (the new URLs are on the same domain, so this is straightforward) OR rely on the 301 redirects + new sitemap
4. **Monitor Coverage Report** for the next 14 days. Watch for:
   - Old URLs moving to "Page with redirect" status (good)
   - New URLs moving to "Indexed" status (good)
   - Any "Crawled but not indexed" errors (investigate)
   - Any "Discovered but not indexed" errors (investigate)
5. **Monitor Performance Report** for impression / click drops. Some short-term volatility is normal (1-3 weeks). If positions don't recover by week 4, investigate.

---

## ROLLBACK PLAN

If something goes badly wrong (e.g., positions drop significantly on a high-traffic page and don't recover within 21 days):

1. Reverse the 301 redirects so old URLs serve the new content (or restore old content if you kept a backup)
2. Update sitemap.xml back to old URLs
3. Re-submit to GSC
4. Diagnose what broke before re-attempting

Lovable should keep version history so reverting is feasible if needed.

---

## ESTIMATED TIMELINE

| Stage | Estimated duration |
|---|---|
| Lovable build (5 pages) | 1 to 2 days, depending on Lovable iterations |
| 301 redirects configured + tested | 1 hour |
| Sitemap + GSC submission | 1 hour |
| Internal link audit + cleanup | 30 to 60 minutes |
| GSC reindexing recognised | 3 to 14 days |
| Position recovery / equity pass via 301s | 14 to 21 days |
| Full SEO stabilisation | 4 to 6 weeks |

---

## FILES IN THIS FOLDER FOR THE LANDING PAGE WORK

For your reference, the complete set of deliverables produced today (14 May 2026):

### Homepage
- `homepage-rewrite.md` — copy brief
- `homepage.html` — clean HTML
- `lovable-prompt-homepage.md` — Lovable instruction

### Restaurants and Cafes
- `landing-page-restaurants-cafes.md` — copy brief
- `landing-page-restaurants-cafes.html` — clean HTML
- `lovable-prompt-restaurants-cafes.md` — Lovable instruction

### Dental Practices
- `landing-page-dental-practices.md` — copy brief
- `landing-page-dental-practices.html` — clean HTML
- `lovable-prompt-dental-practices.md` — Lovable instruction

### Aesthetic Clinics
- `landing-page-aesthetic-clinics.md` — copy brief
- `landing-page-aesthetic-clinics.html` — clean HTML
- `lovable-prompt-aesthetic-clinics.md` — Lovable instruction

### Gyms and Fitness Studios
- `landing-page-fitness-gyms.md` — copy brief
- `landing-page-fitness-gyms.html` — clean HTML
- `lovable-prompt-fitness-gyms.md` — Lovable instruction

### Site-wide
- `sitemap.xml` — new sitemap
- `sitemap-and-redirects-update.md` — this file

### Research (reference)
- `homepage-research.md` — homepage H1 + positioning research
- `aesthetics-clinics-keyword-research.md` — aesthetics-specific keyword research
- `landing-page-keyword-research.md` (in `13-05-26` folder) — restaurants/dental/beauty/fitness keyword research
