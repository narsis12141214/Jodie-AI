# Current Priorities

Last updated: 2026-04-06

## TOMORROW (Tuesday 7 April — Day 7 of 60)

**PRIORITY 1 (Agency): Import Workflow 2 to N8N, add Anthropic key, test**
**PRIORITY 2 (Agency): Zizi briefing — review opener sheet, brief her on Day 1 sends**

Agency:
- [ ] Import workflow-2-opener-generation.json to N8N — Hadi
- [ ] Add Anthropic API key to Workflow 2 "Generate Opener via Claude" code node — Hadi
- [ ] Test Workflow 2 manually — confirm opener written to sheet + email received — Hadi
- [ ] Activate Workflow 2 schedule trigger — Hadi
- [ ] Brief Zizi — share opener sheet, explain "Opener Ready" status, Day 1 outreach — Hadi
- [ ] Humble Grape — Closer follow-up (Step 2 sent 3 Apr, 4 days silence) — Hadi
- [ ] Maria — follow up Wednesday if no reply — Hadi
- [ ] N8N Workflow 3 — follow-up reminder (3-day trigger) — by Day 10 (10 April)
- [ ] N8N Workflow 4 — CRM auto-logging — by Day 10

Photography:
- [ ] Answer 5 input questions for blog post #6 (pre-wedding photoshoot london) — Hadi
- [ ] Blog post #6 brief — Jodie (after Hadi answers input questions)
- [ ] Log Search Console baseline for homepage title tag change (28-day window in GSC, homepage filter)

Pipeline:
- [ ] Maria — DM sent 7 April. Follow up Wednesday 8 April if silent.
- [ ] Humble Grape — Closer follow-up Tuesday
- [ ] Somewhere Café Harrods — check for contact response
- [ ] Restaurant Owner 2 — follow up needed

### Google Sheets Connection (N8N) — Steps
1. Open N8N: n8n.srv1466538.hstgr.cloud
2. Go to Settings → Credentials → Add Credential → Google Sheets OAuth2 API
3. Follow OAuth flow (you'll need Google Cloud Console or use existing credentials)
4. Once credential is saved, open Workflow 1 (Lead Identification)
5. Click both Google Sheets nodes (Get Existing Leads + Append to Lead Sheet) and connect them to the new credential
6. Save the workflow
7. Run manually once → confirm leads land in the sheet with correct columns

## THIS WEEK (April 1–4)
- [ ] N8N automation — all 4 workflows built and tested with Zizi before 10 April
- [ ] Finish filming @clickaiagency Reels — 5 remaining, shoot ASAP — Hadi
- [ ] Outreach — brief Zizi, scale toward 40/day
- [ ] Follow up Maria — if no reply by Friday 4 April
- [ ] Blog post #5 published in WordPress — Hadi (HTML ready, paste and publish)
- [ ] Blog post #6 brief generated — Jodie (topic: pre-wedding photoshoot london, not engagement)

## AGENCY PIPELINE
- Maria: Proposal sent £300+£497/mo. Reviewing. → Follow up Friday 4 April if silent
- Paris: Silent since Mar 27. → Final chase today 2 April
- Restaurant Owner 2: Has agency. → Follow up needed
- Walid: PARKED — not interested for now
- Hasan: PARKED — not interested for now
- Navid: PARKED — not interested for now

## ONGOING PRIORITIES
1. Close first agency client — nothing else matters more
2. N8N outreach automation — built and live before Day 10 (10 April)
3. @clickaiagency — post daily from content calendar
4. Photography SEO — one blog post per week minimum (post #5 ready to publish)
5. @hadyyazdani — reactivate with daily posting

## NEXT WEEK (Days 8–14)
- [ ] Photography voice agent / receptionist — Vapi build for @hadiphotographylondon inbound calls — Hadi/Jodie

## TOMORROW (Wednesday 8 April — Day 8 of 60)

**PRIORITY 1 (Agency): Brief Zizi — opener sheet, Step 1 instructions, daily target 8-10 DMs**
**PRIORITY 2 (Photography): Answer 5 blog post #6 questions (pre-wedding photoshoot london)**

Agency:
- [ ] Brief Zizi — share opener sheet, explain Opener Ready status, Step 1 formula, daily target — Hadi
- [ ] Maria — follow up if no reply (message sent 7 Apr, chase Wednesday) — Hadi
- [ ] Build Workflow 3 — follow-up reminder, 3-day trigger — Jodie + Hadi — by Day 10 (Thu 10 Apr)
- [ ] Build Workflow 4 — CRM auto-logging — Jodie + Hadi — by Day 10 (Thu 10 Apr)

Photography:
- [ ] Answer 5 blog post #6 input questions — Hadi — Wednesday morning
- [ ] Blog post #6 brief — Jodie (after answers received)
- [ ] @hadyyazdani — confirm Post 1 photo (St Dunstan proposal) for Monday 13 April launch — Hadi

Weekend (11-12 April):
- [ ] Film 2 @hadyyazdani Reels — Post 2 script (permission to elope) + Post 7 script (never feel awkward) — Hadi
- [ ] Film 5 @clickaiagency Reels — scripts in agency 30-day calendar — Hadi
- [ ] Drop @hadyyazdani Week 1 photos in Drive folder (Post 1–5) — Hadi

Pipeline:
- [ ] Maria — follow up Wednesday if silent
- [ ] Humble Grape — await reply (message sent today, 48hr window — decision Thursday)

## COMPLETED — 2026-04-07
- [x] 2026-04-07: Workflow 1 upgraded — two-stage scrape added (Start Profile Scraper, Wait, Fetch Profile Results, Merge Profile Data). Remove Duplicates fixed to reference Merge Profile Data. Append to Lead Sheet switched to Map Automatically.
- [x] 2026-04-07: Workflow 2 built and fixed — Filter New Leads strips rogue 'json' field, Read Lead Sheet restricted to A3:R, Generate Opener loops internally (Run Once for All Items), Update Lead Row matches on row_number, Build Email Summary uses string concatenation.

## COMPLETED — 2026-04-06
- [x] 2026-04-06: Workflow 2 (opener generation) built — Claude Haiku generates personalised Step 1 openers from lead sheet, writes back to "Message Sent", emails daily summary
- [x] 2026-04-06: closer.md deployed — warm lead follow-up and closing messages for both businesses
- [x] 2026-04-06: strategist.md deployed — positioning, messaging angles, campaign planning, pipeline review
- [x] 2026-04-06: campaign-builder.md deployed — multi-step outreach and nurture sequence design
- [x] 2026-04-06: CLAUDE.md registry updated — marketing hierarchy, routing rules, forbidden phrases, agency/marketer (DEFERRED) removed
- [x] 2026-04-06: Maria follow-up message sent (7 April)

## COMPLETED — 2026-04-05
- [x] 2026-04-05: Google Sheets credential created and connected in N8N
- [x] 2026-04-05: Workflow 1 (Lead Identification) tested and running — 3 bugs fixed: resultsType profiles→details, fetch URL now uses run-specific ID, wait increased to 8 minutes
- [x] 2026-04-05: Email notification node added to Workflow 1 (run confirmation)
- [x] 2026-04-05: Photography voice agent scoped and deferred to next week

## COMPLETED — 2026-04-04
- [x] 2026-04-04: Homepage meta description finalised (159 chars) and pasted into Showit
- [x] 2026-04-04: Homepage title tag updated — "London Elopement & Wedding Photographer | Hadi Photography"
- [x] 2026-04-04: Elopement service page pivoted — new title tag, H1, meta description targeting "elopement photography london" (booking intent)
- [x] 2026-04-04: Proposal service page pivoted — new title tag, H1, meta description targeting "surprise proposal photographer london" (transactional)
- [x] 2026-04-04: Internal links added to 3 blog posts (best-places-to-elope, elopement complete guide, proposal guide)
- [x] 2026-04-04: 301 redirects completed
- [x] 2026-04-04: Noindex flags done — lightroom-presets, cart/checkout/shop (editorial-street-fashion left indexed intentionally)
- [x] 2026-04-04: Blog post #6 topic corrected to pre-wedding photoshoot london (13/15) — engagement post dropped (not in top-scored list, cannibalisation risk)
- [x] 2026-04-04: Operator rule added — blog post topic must be cross-checked against monthly report scored table before assignment
- [x] 2026-04-04: 5 input questions written for pre-wedding photoshoot blog post — Hadi to answer

## COMPLETED — 2026-04-03
- [x] 2026-04-03: SEO agent operating protocol overhauled — cannibalisation check, Showit JS flag, hard stop, recommendation format, /blog/ rule
- [x] 2026-04-03: N8N SEO Weekly Data Pipeline built and live — runs every Monday 7am, Sheets + GitHub + email
- [x] 2026-04-03: Monthly roundup skill updated to use pipeline data as primary source
- [x] 2026-04-03: Workflow 1 filters updated — floor 500, ceiling 5k, 21-day recency
- [x] 2026-04-03: Step 2 outreach scripts (2A follow-up DM, 2B email, 2C human reply) written and pushed to Notion
- [x] 2026-04-03: Homepage title tag recommendation finalised — London Elopement & Wedding Photographer | Hadi Photography — with monitoring protocol
- [x] 2026-04-03: Meta descriptions for 5 service pages written and saved
- [x] 2026-04-03: /blog/ subfolder rule logged in decisions.md
- [x] 2026-04-03: SEO pipeline Google Sheet ID added (1Q2s49XED4TnyM4Fv9QVTjwyH-p9vXg89wCBHbL9fyy0)

## COMPLETED — 2026-04-02
- [x] 2026-04-02: N8N Workflow 1 (Lead Identification) built and pushed live to N8N server (ID: xnQpX1V1vNqpOSXO)
- [x] 2026-04-02: Blog post #5 (best-places-to-elope-in-london) published and reviewed — 3,557 words, clean
- [x] 2026-04-02: 5 cold outreach scripts written and pushed to Notion (Outreach Scripts DB)
- [x] 2026-04-02: Somewhere Café Harrods live lead — two response scripts drafted
- [x] 2026-04-02: @clickaiagency AM carousel + PM hook post published (Day 2 content done)
- [x] 2026-04-02: Paris final touchpoint sent — Hadi explained the system
- [x] 2026-04-02: Workflow 1 JSON pushed to GitHub (Apify key replaced with placeholder)

## COMPLETED — 2026-04-01
- [x] 2026-04-01: Strategy agent built and deployed (shared/strategy.md)
- [x] 2026-04-01: goals.md rewritten — both businesses, 60-day targets, review dates
- [x] 2026-04-01: 60-day-plan-agency.md built (phases 1-3, risk register, automation decision)
- [x] 2026-04-01: 60-day-plan-photography.md built (SEO, Instagram, enquiry pipeline)
- [x] 2026-04-01: Outreach automation decision confirmed — N8N build starts Day 2
- [x] 2026-04-01: context/decisions.md created — automation decision logged
- [x] 2026-04-01: projects/goals/ folder created — README, plans, PDF reference
- [x] 2026-04-01: photography/seo.md structurally rebuilt — two-tier blocking/advisory checklist
- [x] 2026-04-01: memory/quality-log.md created — 4 pipeline errors logged
- [x] 2026-04-01: shared/admin.md updated — post-publish review + Monday quality audit added
- [x] 2026-04-01: best-places-to-elope-in-london.html — ready to publish in WordPress
- [x] 2026-04-01: All changes pushed to GitHub

## COMPLETED — EARLIER
- [x] 2026-03-31: Full agent registry built (10 agents across shared/agency/photography)
- [x] 2026-03-31: research-agency + research-photography skills deployed
- [x] 2026-03-31: SEO monthly roundup report generated
- [x] 2026-03-31: Day 1 carousel live on @clickaiagency (60+ views)
- [x] 2026-03-30: EA AI pushed to GitHub (SSH configured)
- [x] 2026-03-30: Opening post live on @clickaiagency
- [x] 2026-03-30: 30-day content calendar built (60 posts)
- [x] 2026-03-30: Carousel builder HTML created
- [x] 2026-03-30: Hook posts CSV generated (30 posts)
- [x] 2026-03-27: Outreach tracker built (Excel, 3 sheets)
- [x] 2026-03-27: Maria proposal sent (£300+£497/mo)
- [x] 2026-03-24: 4th SEO blog post published
- [x] 2026-03-20: N8N content engine adapted for Click AI Agency
- [x] 2026-03-17: 3 SEO blog posts published and indexed
