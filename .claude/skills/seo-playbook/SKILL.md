---
name: seo-playbook
description: Evidence-based SEO methodology for taking a new or rebranded low-authority site to Page 1 in a competitive local service market. Load before any SEO strategy work, Search Console analysis, content brief, or on-page recommendation for either business. Contains hard decision gates, CTR benchmarks, the phased playbook, local SEO weights, diagnosis protocols, and the cargo-cult ban list.
---

# SEO Playbook — Evidence-Based Methodology

Built 22 August 2026 from two independent research passes, cross-checked against each other. Every claim is source-tagged. Claims that could not be verified are in section 9 (Flagged Uncertainties) and must be presented as unverified if used. This file supersedes generic SEO intuition in every agent that touches SEO for either business.

**Why this exists:** between May and August 2026, three rounds of meta title/description rewrites were prescribed for pages ranking at positions 11-35 and produced zero click improvement. The arithmetic below shows why that outcome was guaranteed. The failure wasn't effort; it was a methodology with no position-realism gate, no authority model, no local layer, and no measurement discipline. This playbook is the structural fix.

---

## 0. Evidence standards — how to smoke-test any SEO advice

Hierarchy of evidence, strongest first:
1. Controlled A/B tests (e.g. SearchPilot's published experiments)
2. Large-sample studies (Ahrefs, Backlinko, Zyppy — millions of results)
3. Google primary statements (Search Central docs, Mueller/Illyes on record)
4. Expert surveys (Whitespark Local Ranking Factors)
5. Correlation studies (directional only, never causal)
6. Practitioner consensus (flag as consensus, not fact)
7. Single-site anecdotes (never a basis for a recommendation)

**Statistical power rule:** a site producing under ~100 clicks/week has no internal statistical power to validate any on-page test. External evidence must carry the decisions. Do not run "tests" on this site and read the noise as results.

### Cargo-cult ban list — tested and shown NOT to matter

Never prescribe these. If found in an existing agent file, remove them.

| Tactic | Verdict | Source |
|---|---|---|
| Meta keywords tag | Ignored by Google | Google official statement, 2009 |
| Word-count targets | "Not a ranking factor" | Mueller, on record |
| Keyword density % | Not a thing | Mueller, Search Engine Roundtable 2021 |
| LSI keywords | "No such thing" | Mueller, 2019 |
| Exact-match anchor ratios | No published test supports any ratio | Practitioner invention |
| Meta rewrites for pages at position >10 | Mathematically unmeasurable | See CTR table, section 2 |

### What survived testing

- Title/intent alignment — SearchPilot A/B tests show +8.5% to +17.5% traffic wins (and losses), **but only on pages already ranking positions 1-10 with real volume**
- Links/domain authority — every large study; referring domains is the strongest correlating factor (Ahrefs 10K-SERP study; Backlinko 11.8M results)
- Redirect/indexation hygiene — Illyes: pages deindexed for weeks/months lose signals and "pretty much start from the bottom"
- GBP + review signals for local queries — Whitespark expert survey (section 4)
- Note: Google rewrites ~61% of titles (Zyppy 80K-title study) and ~63% of meta descriptions (Ahrefs 20K-keyword study) anyway — snippet copy is a suggestion, not a setting

---

## 1. Hard decision gates

These are blocking rules for every SEO recommendation in every agent.

1. **Position-realism gate:** No snippet (title/meta) rewrite recommendations for pages ranking below position 10 on the target query. The constraint at position 11+ is position, not snippet copy. Fix ranking inputs (authority, relevance, internal links), not descriptions.
2. **Impression-count gate:** Before interpreting any position change, check the impression count behind it. Weekly GSC position is impression-weighted; under ~10 impressions, a swing of 20+ places is presumptively an averaging artifact, not an event. Verify in incognito/local search before reporting as real.
3. **Query+page granularity gate:** Sitewide average position is never a decision input. It routinely worsens as SEO improves (new long-tail queries enter at low positions). Read position only at the individual query + page level.
4. **Measurement cadence gate:** Weekly data is for anomaly detection only (indexation breaks, crawl errors, pennies-to-zero drops). Initiatives are judged at 90 days. Strategy is judged at 6-12 months. No strategy pivots off weekly data, ever.
5. **Winnability gate:** On a low-authority domain, new content targets keyword difficulty under ~20 (Ahrefs/Semrush KD) until authority is established. Head terms are deferred, not chased.
6. **Local-intent gate:** Before treating any query as an organic blue-link target, check whether the live SERP is dominated by the map pack, ads, or image packs. If the pack is present, GBP work on that query outranks content work (section 4).

---

## 2. CTR by position — the reference table

FirstPageSage 2025-26 meta-analysis (primary source verified), cross-checked with Advanced Web Ranking and Backlinko:

| Position | Expected CTR |
|---|---|
| 1 | ~39.8% |
| 2 | ~18.7% |
| 3 | ~10.2% |
| 5 | ~5.1% |
| 10 | ~1.6% |
| 11-20 (page 2) | ~1.0-1.5% |
| 21-30 | effectively zero |
| Featured snippet | ~42.9% |

- All of page 2 combined receives ~0.63% of clicks (seoClarity).
- **Zero clicks at positions 15-35 is normal.** It is not a meta-description problem. It is not a content problem. It is a position problem.
- Context: ~68% of US Google searches ended with no click at all in early 2026 (SparkToro/Datos), up from ~60% in 2024. CTR expectations must be set against this.

---

## 3. The phased playbook — new/rebranded low-authority site

Consensus sequence across documented agency roadmaps (SEO Sherpa, Seobility, Shortlist.io):

**Phase 1 — Technical foundation + migration forensics (weeks 0-4)**
GSC/GA verified, clean indexation, 301 redirect integrity, canonical/hostname consistency (www vs non-www, http/https), flat architecture (key pages ≤3 clicks deep), all sitemaps valid and submitted, Core Web Vitals, schema. For a rebranded site: crawl the OLD URL inventory (Wayback Machine / old sitemap), find 404s and soft-404s and homepage-dumps, map 1:1 redirects to relevant pages, reclaim live external links pointing at dead URLs. Redirects to irrelevant pages/homepage are treated as soft 404s and pass nothing (Mueller). This is the cheapest recovery of already-earned equity; everything else compounds on it.

**Phase 2 — Winnable keyword architecture (weeks 2-8)**
Target KD <20 terms first. Collect positions and authority that eventually let you compete for harder terms. Explicitly defer head terms.

**Phase 3 — Content in topic clusters (months 2-6)**
Pillar + cluster + deliberate internal linking. A small site covering a narrow topic completely can outrank bigger generalists (Search Engine Land). Sustained cadence beats bursts: 1-2 cluster pages/week for 6+ months outperforms 20 pages then silence (practitioner consensus — flag as such). Topical authority in a competitive niche takes 6-18 months of structured production.

**Phase 4 — Authority (months 3+, never stops)**
Earned links, slowly. Buying links on a low-authority domain is the highest-risk waste of budget.

**Local layer — runs in parallel from day 1** (section 4). Produces visibility while organic authority builds.

**Explicitly NOT early:** chasing head keywords, paid links, mass directory submissions beyond core citations, reacting to weekly rank movement.

### Timeline reality (set expectations with these numbers)

- Only 5.7% of new pages reach top 10 within one year (Ahrefs 2017); the 2025 update puts it at ~1.74% (secondary confirmation only — flag). Winners took 61-182 days. The average #1-ranking page is ~3 years old.
- Site-wide quality re-evaluation after major changes takes "months (6+ months)" — Mueller, on record. Each major site change partially restarts this clock.
- Clean migrations recover in 4-8 weeks. Botched migrations take 12-24 months and some equity never returns. A site unrecovered 18+ months post-migration should be treated as a **new-site authority build**, not a migration fix — while still running Phase 1 forensics to reclaim what's reclaimable.
- Ranking volatility (positions swinging 20+ places week to week) on a low-authority domain is textbook trust-evaluation: relevance is close, authority is absent. Expect anchored improvement to appear as REDUCED VOLATILITY first, clicks second.

---

## 4. Local SEO layer — service businesses

For local-intent queries ("wedding photographer london", "aesthetic clinic chelsea"), the local pack is a parallel battlefield where domain authority matters less.

**Click distribution on local SERPs:** map pack ~42-44% of clicks vs ~29% organic (BrightLocal). Organic #1 still takes 25.5-27.4% of clicks on local SERPs — organic remains worth winning, especially in style-driven niches like photography where buyers browse portfolios, not proximity.

**Local pack ranking weights** (Whitespark Local Search Ranking Factors survey, 2026 edition — figures via secondary summaries, verify against primary before quoting externally):
- GBP signals: ~32%
- Review signals: ~20% (rising; was 16% in 2023)
- On-page: ~15%
- Links: ~15%
- Behavioural: ~8%
- Citations: ~7% (declining)

**Proven GBP factors:** primary category choice, proximity to searcher (#1 individual factor), review quantity + velocity + **recency** (recency jumped to estimated top-5 impact in 2025 — old reviews decay in value; velocity must continue), business hours matching search time, completed services fields, photo volume (100+ images correlates with materially more calls/clicks).

**Photographer-specific local plays (documented consensus):**
1. **Venue-specific pages** — one page per real wedding per venue, targeting "[venue] wedding photographer / wedding photos". Repeatedly cited as the highest-converting photographer SEO play.
2. Complete GBP with continuous photo uploads and review velocity.
3. NAP consistency across site ↔ GBP ↔ core citations.

---

## 5. Authority building — small local business tactics

**The evidence for needing links:** 66.31% of pages have zero backlinks and get almost no search traffic (Ahrefs); no-link pages rank almost exclusively for single-digit-KD keywords. Competitive local head terms require referring domains.

**Tactics that work for a photographer/local service (2025-26):**
- Real-wedding features submitted to wedding blogs/magazines (editorial links)
- Styled shoots with venues, florists, planners — published shoots yield links for every participant
- Venue/vendor "recommended suppliers" pages (ask every venue you've shot at)
- Curated local content that earns citations (best-of guides with genuine research)
- Local press human-interest pitches
- Journalist request platforms: HARO relaunched under Featured.com (April 2025); free alternatives: Source of Sources, Qwoted free tier, Help a B2B Writer
- Core citations only (Google Business Profile, Bing Places, key directories) — citations are only ~7% of local weight now

**Velocity:** no credible published benchmark exists for a solo local business (evidence gap — flagged). Practitioner guides imply a handful of quality local/editorial links per month is a strong pace.

---

## 6. Measurement framework

**Weekly (anomaly detection ONLY):** indexation status, crawl errors, sitemap health, impressions on target topics (directional), GBP actions (calls/direction requests). No strategic conclusions.

**Monthly (KPI trends):** clicks, impressions, CTR at query+page level (never sitewide), referring domains, enquiries/conversions attributed to organic, GBP insights, review count + recency.

**Quarterly (strategy):** initiative scorecard vs 90-day expectations, pivot decisions.

**Leading indicators (move in 60-90 days):** impressions on target topics, indexation coverage, new referring domains, long-tail rankings, reduced volatility.
**Lagging indicators (a quarter+):** clicks, enquiries, revenue.

**Pivot discipline:** judge initiatives at 90 days; judge strategy at 6-12 months on a low-authority site. Growing impressions + flat clicks mid-way through an authority build is ON CURVE, not failure. Never pivot off weekly data.

**A proper monthly report contains:** query+page level position/CTR for the target keyword set (not sitewide averages), brand vs non-brand split, referring domain delta, GBP metrics, content shipped vs plan, link acquisitions, initiative scorecard vs 90-day expectations, and exactly one prioritised action list.

---

## 7. Diagnosis protocols

### A. Ranking volatility (positions swinging 20+ places weekly)
1. Check impression counts per swung query (gate 2). Under ~10 impressions = presumptive artifact.
2. If real: on a low-authority domain this is trust-evaluation, not damage. The fix is authority (section 5), not on-page churn.
3. Track volatility itself as a metric — stabilisation is the leading indicator that authority is anchoring.

### B. Branded query drops
Diagnostic order: (1) impression count that week — under ~10, treat as noise pending verification; (2) incognito UK search for the brand; (3) URL Inspection on homepage — indexed? canonical match?; (4) `site:` sanity check; (5) hostname/duplicate-URL crawl; (6) GBP name/URL match; (7) GSC country filter (foreign impressions skew position). Urgency: 30 minutes to verify, possibly nothing to fix. A CONFIRMED persistent brand-name loss is a critical signal (indexing/canonical/entity problem); an artifact is nothing.

### C. Impressions up, clicks flat
Check in order: (1) where do the real positions sit — if 11-30, zero CTR is expected (section 2), fix is position; (2) SERP real estate — pack/ads/images pushing organic below fold; (3) brand vs non-brand split; (4) zero-click/AI Overview exposure on informational queries.

### D. "Keywords ranking" count changes
Weekly keyword-count from an API pull is a noise metric at small-site scale. Count falling while impressions rise = consolidation (fringe queries dropping below tracking depth while surviving queries strengthen), not decline. Do not report it as a headline metric.

### E. Unrecovered migration profile (18+ months post-migration)
Signature: impressions rebuilt, clicks flat, rankings unanchored, click volume concentrated on homepage, interior pages starved. Response: Phase 1 forensics (old-URL crawl, redirect repair, equity reclamation) + accept that lost equity is partly permanent + rebuild as new-site authority play. Expect fractional recovery from forensics, not full.

---

## 8. Applying this playbook to a site (procedure)

When loaded for SEO strategy or analysis work:
1. Run the diagnosis protocols (section 7) against current GSC data BEFORE recommending anything.
2. Check every proposed action against the hard gates (section 1).
3. Sequence actions per the phased playbook (section 3) — technical/forensics debt first, local layer always-on, winnable content next, authority continuously.
4. Set expectations from section 3 timelines in every plan delivered.
5. Structure reporting per section 6 — and refuse to draw strategic conclusions from weekly data.

---

## 9. Flagged uncertainties (present as unverified if used)

- Ahrefs 2025 figure of 1.74% new pages reaching top-10 within a year — secondary confirmation only
- Whitespark 2026 exact weighting percentages — via secondary summaries; verify against primary report
- "Proximity = 55% of ranking decisions" — could not be verified as a Whitespark number; do not use
- AI Overview impact on CTR — directly contradictory studies (some claim ~60% CTR reduction, FirstPageSage found minimal impact); present both
- Content-cadence numbers (1-2/week) — practitioner consensus, no controlled study
- Link velocity benchmarks for small local businesses — no credible published data
- "SEJ study of 892 migrations, 523-day average recovery" — found only in secondary citations; treat as unconfirmed

---

## Sources

Primary: FirstPageSage CTR reports · Ahrefs (ranking-timeline study 2017/2025, search-traffic study, meta-description study, SEO statistics 2026) · Whitespark Local Search Ranking Factors · BrightLocal (LSA click study, local SEO statistics) · SparkToro/Datos zero-click 2026 · Backlinko 11.8M-result analysis · Zyppy 80K-title study · SearchPilot A/B test library · Google Search Central / Mueller / Illyes statements (via Search Engine Roundtable, GSQI) · seoClarity page-2 CTR · Advanced Web Ranking CTR reports · Search Engine Land (topical authority, GSC impressions interpretation) · SEOTesting + Practical Ecommerce (GSC average-position mechanics) · Seobility / SEO Sherpa / Shortlist.io phased roadmaps · SLR Lounge + Proud Marketer + Belman & Co (photographer link building) · Prowly (HARO/Featured.com landscape) · Sara Does SEO + SnapSEO + MoCo Marketing (Showit platform SEO) · GSQI + Krawl + Numen (migration recovery)
