# SEO Monthly Report — August 2026
Date: 22 August 2026
Data source: N8N SEO weekly pipeline v2 (Google Search Console)
Coverage: week ending 19 August 2026
Comparison baseline: last verified data point 12 June 2026 (10-week gap due to Google credential issue on n8n pipeline)

---

## Executive summary

**Headline:** Rankings had one of the strongest weeks on record. **17+ Page 1 entries** on important commercial keywords. But **CTR dropped 40%** from June baseline and **clicks stayed flat at 11** despite improved rankings. The site is showing up more but converting the impressions worse.

**Two things need attention immediately:**
1. **Branded term "hadi photography london" dropped from position 1 to position 27.** Serious — this is Hadi's own name. Needs investigation today.
2. **CTR regression is the real bottleneck.** 4 of the top 10 keywords by impressions are at Page 1 (positions 1-30) but returning ZERO clicks. Meta title/description work on those specific pages is the highest-leverage next action.

---

## The numbers

### Overview (week ending 19 August)

| Metric | This week | vs 12 June (baseline) | Direction |
|---|---|---|---|
| Clicks | 11 | 12 | roughly flat |
| Impressions | 2,861 | 2,489 | +15% |
| CTR | 0.38% | 0.62% | **-40%** |
| Avg Position | 30.7 | 26.7 | -4 positions |
| Keywords ranking | 361 | 533 | **-32%** |

### The picture in one line
More people see us in search results (+15% impressions), but fewer click through (-40% CTR), and we rank for a third fewer keywords than 10 weeks ago.

### Traffic concentration
- Top 10 keywords by impressions: 875 impressions, **0 clicks (0%)**
- Top 50 keywords: 1,489 impressions, 3 clicks (27% of clicks)
- Long tail (50+): 1,372 impressions, 8 clicks (73% of clicks)
- Homepage carries **10 of 11 clicks (91%)** at 0.48% CTR

---

## The story: rankings surged, CTR crashed

### 17+ Page 1 entries this week
Genuinely strong movement on commercial keywords:
- **"hire photographer london"** 67.1 → **1.0** (from nowhere to top spot)
- **"photography services london"** 65.7 → **1.0**
- **"london wedding photos"** 24.3 → **1.0**
- **"best wedding photographers london"** 32.3 → **2.0**
- **"west london wedding photographer"** 14.8 → **2.2**
- **"couple photographers"** 28.0 → **2.0**
- **"pre wedding photographers"** 16.5 → **1.6**
- **"couples photoshoot london"** 16.4 → **3.1**
- **"small wedding photography london"** 77.0 → **3.0**
- **"elopement photography london"** 22.5 → **3.0**
- Plus another 7+ Page 1 entries

### But CTR at 0.38% is the worst reading since March
For comparison: industry benchmark for photography SERPs sits around 2-3%. We're at 0.38%. Even our May-June peak was 0.62%.

**Where CTR is dying:**
| Keyword | Position | Impressions | Clicks | CTR |
|---|---|---|---|---|
| photography | 2.1 | 322 | 0 | 0.00% |
| wedding photographer london | 27.1 | 142 | 0 | 0.00% |
| london wedding photographer | 28.6 | 120 | 0 | 0.00% |
| wedding photography london | 23.5 | 105 | 0 | 0.00% |
| best wedding photographers in london | 11.4 | 31 | 0 | 0.00% |

"Photography" at position 2 with zero clicks is the strangest data point. That's such a broad term it's likely image searches or brand adjacencies. The other four are money keywords sitting at Page 2-3 where impressions come from Google testing our positioning — CTR at those positions is naturally low but zero across 100+ impressions is unusual.

### The alarming individual movement
**"hadi photography london"** dropped from **position 1 → position 27** and exited Page 1. This is a branded search — Hadi's own business name. Losing Page 1 on your own brand name in a week is a red flag. Possible causes:
- Someone else launched a similar-named business
- Google reclassified the site (algorithmic issue)
- Site technical issue (indexing, hosting, or cache problem)
- The rank drop coincides with the 10-week n8n gap — coincidence, or is there something else that broke around mid-June?

**Same class of drops:**
- best wedding photographer london: 3.5 → 36.5 (Page 1 exit)
- pre wedding photoshoot in london: 1.6 → 52.0 (Page 1 exit)
- photographer wedding london: 2.0 → 12.0 (Page 1 exit)
- london photoshoot: 3.0 → 20.5 (Page 1 exit)
- london photographers: 1.3 → 11.0 (Page 1 exit)
- local photographers for weddings: 1.0 → 11.0 (Page 1 exit)

Not all of these are same-cause, but the pattern of losing hard-won Page 1 spots on ~7 keywords in the same week alongside gaining 17+ Page 1 spots elsewhere suggests **Google is actively recalibrating** the site's placement. Rankings are unstable this month.

---

## Top 3 actions

### 1. Investigate "hadi photography london" drop today (30 mins)
Search the term in Google incognito. If you're not on Page 1, check:
- Is a competing business ranking? (someone else with similar name)
- Is your Google Business Profile still showing? (this feeds branded searches)
- Any technical alert in Search Console? (manual actions, indexing errors)
This is the fastest thing to diagnose and the most concerning single data point.

### 2. Meta title + description rewrite on the top 4 zero-CTR keywords (2 hours)
Target pages behind these keywords:
- "photography" — likely homepage
- "wedding photographer london" + "london wedding photographer" — likely the wedding photographer blog #4 or a service page
- "wedding photography london" — likely a service page
Rewrite meta titles to lead with the strongest emotional or specific hook (not generic). Rewrite meta descriptions to include the keyword phrase AND a reason to click (specific benefit, credential, or call to action).

### 3. Fix the n8n pipeline monitoring (real ops)
This is the second time the pipeline died on a Google credential issue and no one noticed for 10 weeks. Two options:
- Set up an alert in n8n so if the workflow fails or doesn't run, you get an email
- Or: add a weekly calendar reminder Mon 10am to check the file has updated. If `last_updated` in `memory/seo-current-data.md` is more than 7 days stale, restart the workflow.
Without weekly data, we cannot do SEO management. Every week of blind spot is a week of decisions made from stale ground.

---

## Positive signals worth naming

Not all bad. Rankings moving up on commercial keywords is real value being created. When CTR is fixed:
- Position 1 on "photography services london" + "hire photographer london" + "london wedding photos" alone could add 15-30 clicks/week if CTR gets to industry norm.
- 17 new Page 1 entries this week is the strongest single-week ranking movement since we started tracking.

The work is landing. The issue is at the SERP click-through step, not at the ranking step.

---

## Data appendix

- Raw data file: `memory/seo-current-data.md` (updated 19 Aug 2026)
- Google Sheet: https://docs.google.com/spreadsheets/d/1Q2s49XED4TnyM4Fv9QVTjwyH-p9vXg89wCBHbL9fyy0
- Pipeline JSON: `projects/photography/seo-recovery/n8n-seo-weekly-pipeline-v2.json`
