# Current Priorities

Last updated: 2026-05-13
Note: Sections below the WEDNESDAY 13 MAY block are stale (last full refresh 17 April). Full rewrite pending — Hadi to schedule.

## MONDAY 18 MAY — Day 48 of 60

**PRIORITY 1 (Agency): Record aesthetic + fitness 60-sec clips (production blocker for cold email sends)**
**PRIORITY 2 (Agency): Build n8n + Instantly email automation per Section 7 of email scripts (4-6 hrs)**
**PRIORITY 3 (Agency): Brief Zizi on new DM scripts**

Agency — Cold email implementation (priority 1):
- [ ] Record 60-sec clip: AI handling Botox enquiry (aesthetic segment) — Hadi
- [ ] Record 60-sec clip: AI handling new-member fitness enquiry (fitness segment) — Hadi
- [ ] Host clips with clean URLs — Hadi
- [ ] Build CSV → Instantly importer with deterministic variable merge (see Section 7) — Hadi/Arman
- [ ] Postcode → location_area lookup table (top 30 London postcodes)
- [ ] Category parser for {category_phrase} / {specialism} / {treatment_focus} / {discipline}
- [ ] Encode-clean step (strip u003e, %20 artefacts from Lead Engine output)
- [ ] Set up all 12 Instantly templates per email scripts file
- [ ] End-to-end test on 10 sample leads per segment
- [ ] Lock the new cadence rule in Instantly: Mon-Thu only, never Fri/Sat/Sun

Agency — DM channel:
- [ ] Brief Zizi on Sections 1 + 6 of outreach-scripts-dm.md
- [ ] Update Workflow 2 prompt in n8n with new positioning (see Section 7 of DM file)
- [ ] Test Workflow 2 on 3 sample Instagram leads

Agency — Landing page cleanup:
- [ ] Lovable update: remove "Click Voice not available for [segment]" lines from dental, aesthetic, fitness landing pages
- [ ] Lovable update: fix "AI receptionist" → "AI phone answering" body copy on restaurants/cafes landing page

Agency — Active deals:
- [ ] Ace Monday 10am callback (from 7:30pm Fri text — assuming he picks Mon)
- [ ] Hanna email reply monitoring
- [ ] Kish 19 May check-in (Tuesday — step-back message protocol)

## FRIDAY 15 MAY — Day 45 of 60 — COMPLETED

Strategic + operational marathon today:
1. Pricing restructure (Click+/Pro/Elite refined) — canonical packages file updated + Lovable site update applied
2. Cold email research dispatched + completed (UK SMB outreach, 8 questions answered with sourced data)
3. ALL 4 email outreach segments rebuilt step-by-step (12 templates total): restaurants, dental, aesthetic clinics, fitness/gyms
4. New cadence rule (Mon-Thu only, never Fri/Sat/Sun) replaces generic +4 rule
5. Strategic decision: Click Voice extended to all service segments (was restaurants-only v1)
6. Ace 20-second call + 7:30pm text scheduled

Full email playbook ready at: projects/agency/15-05-26/outreach-scripts-email.md
DM playbook ready at: projects/agency/15-05-26/outreach-scripts-dm.md
Research backing at: projects/agency/15-05-26/cold-email-research.md

## FRIDAY 15 MAY — Day 45 of 60

**PRIORITY 1 (Agency): Outreach script rewrite (Zizi) — now the bottleneck. 5 landing pages live with new positioning, but cold pitches still using old language.**
**PRIORITY 2 (Agency): Internal link audit across live site (nav, footer, email signatures, outreach scripts) + monitor GSC indexing**
**PRIORITY 3 (Agency): Ace 48hr decision (Coventry voice note if still silent) + Brief Arman on Click Voice provisioning**

Agency — Lovable builds (PRIORITY 1 yesterday): COMPLETED Thursday 14 May evening
- [x] All 5 landing pages built on Lovable (homepage + restaurants/cafes + dental + aesthetic clinics + fitness/gyms)
- [x] 3 × 301 redirects configured (restaurants old → new, dental old → new, aesthetics old → new)
- [x] Sitemap.xml updated with new canonical URLs
- [x] All new URLs submitted to Google Search Console for indexing
- [ ] Monitor GSC indexing status (3-21 days typical) — Hadi to check weekly
- [ ] Test all 3 redirects in incognito browser to verify 301 (not 302, not 404)
- [ ] Internal link audit (nav, footer, blog, email signatures) — Hadi 30-min sweep

Agency — Outreach scripts (PRIORITY 1 today):
- [ ] Greenlight outreach script rewrite scope (24 templates, 4 segments × 2 channels × 3 steps) — Hadi
- [ ] Draft all 24 templates + reply handler library + Workflow 2 prompt update — Jodie (when greenlit)
- [ ] Brief Zizi on new scripts before next outreach batch — Hadi

Agency — Active deals:
- [ ] Hanna email reply monitoring (sent Wed 13 May afternoon)
- [ ] Ace 48hr voice note today PM if still silent: "When are you next in London? Happy to walk through Phorest with you in person." — Hadi
- [ ] Brief Arman on Click Voice tenant provisioning (no social, no website, no SEO automation) — Hadi

Agency — Pending Jodie work (Hadi to greenlight):
- [ ] Outreach script rewrite (Zizi) — 24 templates planned across 4 segments × 2 channels × 3 steps. Plan documented in last message of 14 May session.
- [ ] Workflow 2 prompt update (n8n + Claude API opener generator) — bake in new positioning
- [ ] Click Voice Python contract template — separate from Click+ template
- [ ] Apply 3 contract clause revisions (12 May) to all new templates
- [ ] Update agent files (closer, copywriter, outreach) with new positioning language
- [ ] operator.md structural review (3+ entries in quality log)

## THURSDAY 14 MAY — Day 44 of 60 — COMPLETED

All 5 landing pages drafted (homepage + restaurants/cafes + dental + aesthetic clinics + fitness/gyms). Each has markdown brief + clean HTML + Lovable prompt. Sitemap.xml + 301 redirect map + execution guide produced. Aesthetics keyword research dispatched + completed. Homepage research dispatched + completed. Quality log entries added (homepage rotating animation misread by Jodie, corrected). Decisions logged: URL=H1 principle, no standalone Click Voice page, "service businesses" audience descriptor, Click Pro recommended for aesthetics, Randeszvous archived as dead.

Full file index: projects/agency/14-05-26/sitemap-and-redirects-update.md

## THURSDAY 14 MAY — Day 44 of 60

**PRIORITY 1 (Agency): Landing pages rebuild (Click Voice + restaurants + dental) — must be live before next prospect meeting**
**PRIORITY 2 (Agency): Investigate clickaiagency.com/dental 404 on Lovable**
**PRIORITY 3 (Agency): Send Hanna's amended email (carry-over) + Ace 48hr decision**

Agency — Landing pages (Priority 1):
- [ ] Investigate /dental 404 on Lovable. Restore or rebuild — Hadi
- [ ] Draft new Click Voice landing page copy (H1 + body per keyword research) — Jodie
- [ ] Draft updated restaurants landing page (Click Voice entry + Click+ bundle on same page) — Jodie
- [ ] Draft updated dental landing page once Lovable status confirmed — Jodie
- [ ] Light refresh on beauty + fitness landing pages — Jodie
- [ ] Hadi approves all copy, builds on Lovable, publishes

Agency — Outreach & scripts:
- [ ] Rewrite Zizi Step 1 + Step 2 templates with new positioning + Click Voice option — Jodie
- [ ] Brief Zizi on updated scripts before next outreach batch — Hadi

Agency — Click Voice contract:
- [ ] Generate Click Voice Python contract generator (separate from Click+/Haleh template) — Jodie
- [ ] Apply 3 clause revisions from 12 May to Click Voice template from launch — Jodie
- [ ] Hadi reviews and approves template

Agency — Active deals:
- [x] Hanna's amended follow-up email SENT 13 May afternoon. Awaiting reply.
- [ ] Ace 48hr decision today PM. Voice note: "When are you next in London? Happy to walk through Phorest in person." — Hadi
- [ ] Brief Arman on Click Voice tenant provisioning differences (no social, no website, no SEO automation) — Hadi
- DEAD — Randeszvous archived. Will not offer services even if they reach out. Owner classified as a problem maker (Hadi's call). Remove from all future pipeline tracking.

Agency — Memory & agent updates:
- [ ] Update agent files (closer, copywriter, outreach) with new positioning language — Jodie
- [ ] Update memory rules with Click Voice spec, new positioning principle, 14-day trial — Jodie

## WEDNESDAY 13 MAY — Day 43 of 60 — COMPLETED

Strategist session ran today. 4 topics locked:
1. Click Voice tier finalised (£290/mo, £100 launch setup, 14-day trial, restaurants only v1)
2. Positioning shift to "Done-for-you AI Operations Partner" with SEO-led H1 split
3. 14-day pipeline action plan defined (window to 27 May)
4. Kill conditions set for Click Voice, positioning, signing protocol, 60-day window

Full decisions log: projects/agency/13-05-26/strategist-session-decisions.md
Decisions appended to context/decisions.md

Pipeline state at end of 13 May:
- Haleh Cake: closed, in onboarding
- Hanna: amended email ready to send tomorrow
- Kish: silent until 19 May review
- Ace: 48hr window expires tomorrow PM
- Randeszvous: hold until 26 May
- Maria: parked

## RECENT PIPELINE STATE (13 May)

| Lead | Status | Next Action |
|------|--------|-------------|
| Haleh Cake | CLOSED 11 May | Multi-tenant n8n refactor before go-live. Brief Arman. WABA templates. |
| Hanna ([RESTAURANT NAME]) | Interested, 3hr meeting 12 May, reads on his own | Follow-up email going out today |
| Kish Restaurant | Stalled, "wait for now" | Silent until 19 May review per step-back protocol |
| Ace Hair & Beauty | Silent past 48hr after Phorest answer | Decision point: in-person walk-in or accept loss |
| Randeszvous | Deadline expired weekend 9-10 May | Wait until 26 May, then re-engage with new social proof |
| Maria Gautam | Reviewing for 6+ weeks | Kill this week, send final close-loop message |

## KEY DECISIONS THIS WEEK

- 11 May: First agency client signed (Haleh Cake) — see decisions.md
- 12 May: Contract signing protocol adopted (sign-in-the-room) — see decisions.md
- 12 May: 3 contract clauses to be revised for new contracts — see decisions.md
- 13 May: Partial unbundle approved as direction (voice-only entry tier £290-£390) — see decisions.md

## STALE BELOW THIS LINE — NEEDS FULL REWRITE
---

## SATURDAY (18 April — Day 18 of 60)

**PRIORITY 1 (Agency): Build first 2 industry landing pages (restaurants + dental)**
**PRIORITY 2 (Agency): Create LinkedIn posts for next week (Monday + Thursday)**
**PRIORITY 3 (Photography): Hadi finishes seed question answers in story bank**

Agency:
- [ ] Build /restaurants landing page — industry pain, solution, CTA, Click Pro recommendation — Jodie + Hadi
- [ ] Build /dental landing page — same structure, dental-specific pain — Jodie + Hadi
- [ ] Create LinkedIn post #2 (Monday) — industry insight with specific number — Jodie
- [ ] Create LinkedIn post #3 (Thursday) — behind-the-scenes win or build — Jodie
- [ ] Connect email accounts to Instantly.ai + enable warmup — Hadi
- [ ] Discuss Workflow 3 changes — Hadi flagged issues to review

Photography:
- [ ] Hadi finishes 9 priority seed question answers in story bank
- [ ] Hadi provides micro wedding blog post #7 input answers (5 questions)
- [ ] Jodie does manual Instagram research — UK/EU elopement photographers (30 mins)
- [ ] Drop Week 1 photos in Drive folder once first content formats are ready

## NEXT WEEK (19-25 April)

Agency:
- [ ] Build /beauty + /fitness landing pages (complete the 4)
- [ ] Start accountant/consultant referral partnership outreach (50 targets)
- [ ] Publish first case study (Randeszvous or demo-based)
- [ ] Directory listings (G2, Capterra, Futurepedia, Yell.com, FreeIndex)
- [ ] LinkedIn posts continue 2x per week

Photography:
- [ ] Build first content format from approved picks (#2, #4, #5, #10)
- [ ] Blog post #7 brief (Micro Wedding Photographer London)
- [ ] Rewrite all 7 reel scripts once story bank is seeded

## DAY 20 CHECKPOINT — Monday 20 April

Full Phase 1 review of both businesses:
- Agency: clients closed vs target, outreach volume, pipeline status, @clickaiagency growth
- Photography: SEO rankings, enquiry volume, @hadyyazdani posting cadence, content rebuild progress
- Pull fresh SEO data from GitHub (pipeline runs Monday 7am)
- Adjust next 40 days based on real numbers

## PIPELINE

Agency:
- [ ] Randeszvous — in-person meeting done, follow-up meeting next week to close
- [ ] Maria — proposal under review, "one setup slot left" framing
- [ ] Cocorico, Lumiere, Rwayda, The Bank, Dr Noura, Pavilion — awaiting replies
- [ ] Crockers Tring — email sent 10 Apr, awaiting reply
- [ ] 70+ cold emails sent manually — monitoring replies

Photography:
- [ ] No active leads — content rebuild and SEO recovery in progress

## EMAIL OUTREACH (IN PROGRESS)
- [x] Google Workspace setup on getclick.uk
- [x] DNS records (MX, SPF, DKIM, DMARC) in Cloudflare — done
- [ ] Connect both email accounts to Instantly.ai
- [ ] Enable warmup on both accounts
- [ ] Build lead list from Apify Google Maps Scraper
- [ ] Verify leads with ZeroBounce
- [ ] Import email templates to Instantly.ai
- Setup guide: projects/agency/outreach-system/email-outreach-setup-guide.pdf

## CONTENT FORMATS APPROVED (PHOTOGRAPHY)
1. **30 London Locations in 30 Days** — daily reel, 15-20s each
2. **Things I say on a shoot that make couples cry** — series, one prompt per reel
3. **Photos couples almost didn't take** — series, tension/payoff format
4. **What I saw today** — POV, walking through London

## ONGOING PRIORITIES
1. Close first agency client — Randeszvous follow-up meeting is the closest shot
2. @clickaiagency — daily posts + LinkedIn 2x per week
3. Industry landing pages — build all 4 this week
4. Photography SEO — blog post #7 brief (micro wedding) next week
5. @hadyyazdani — content rebuild via 5 pillars + story bank
6. Email outreach — Instantly.ai warmup setup pending

## FUTURE / PARKED
- Autodream (memory cleanup sub-agent) — build when memory grows large enough
- Workflow 4 (CRM auto-logging) — deferred
- Reel script full rewrite — paused, resume once story bank seeded
- 5-pillar framework for agency — after photography is established
- Google Ads — after 5 clients closed
- SEO blog posts for agency — after 3 clients closed
- Sitemap fix (missing Showit pages) — Monday task

## COMPLETED — 2026-04-17
- [x] 2026-04-17: Agency packages updated — Click, Click+, Click Pro, Click Elite. Old names (Core/Drive/Turbo/Nitro) retired.
- [x] 2026-04-17: Objection handling docs saved — 6 photography + 7 agency objections — shared/objections.md
- [x] 2026-04-17: Full site crawl of hadiphotographylondon.com — 10 blog posts, 8 service pages identified
- [x] 2026-04-17: Sitemap gap identified — 5 Showit pages missing from XML sitemap (indexed via Search Console but not in sitemap)
- [x] 2026-04-17: SEO rule reinforced — always crawl site before making content recommendations. Memory saved.
- [x] 2026-04-17: Blog #7 topic confirmed — Micro Wedding Photographer London (14/15). Input questions sent to Hadi.
- [x] 2026-04-17: Agency traffic growth research completed — strategy doc saved, execution plan approved
- [x] 2026-04-17: Randeszvous pipeline update — in-person meeting done from cold DM, follow-up next week
- [x] 2026-04-17: Companies House registration done
- [x] 2026-04-17: @clickaiagency Meta verified (blue badge)
- [x] 2026-04-17: 70+ cold emails sent manually
- [x] 2026-04-17: DNS for getclick.uk fully configured

## COMPLETED — EARLIER
- [x] See session log for full history
