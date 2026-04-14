# Decision Log
Append-only. One entry per decision. Format: [YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...

---

[2026-04-01] DECISION: Outreach automation via N8N — confirmed and build starts before Day 10 (10 April 2026) | REASONING: Zizi cannot reach 70/day manually without automation support. Automating lead identification and Step 1 opener generation frees her time for the human-only tasks (sending, replying, escalating). Sending remains manual to avoid Instagram detection and bans. | CONTEXT: 60-day agency plan targets 40/day by Day 20, 70/day by Day 45. Automation is the mechanism that makes 70/day achievable with one person. 100/day decision deferred to Day 20 checkpoint — may require second person regardless of automation.

Automation scope confirmed:
- Lead identification: N8N scrapes Instagram by industry + location + follower range (200-10,000). Output: daily lead list for Zizi.
- Step 1 opener generation: N8N + Claude API pulls profile data, generates personalised opener per account. Zizi reviews, edits if needed, sends manually.
- Follow-up reminders: N8N + Google Sheets — triggers reminder when lead not followed up in 3 days.
- CRM logging: N8N + Google Sheets — every contact auto-logged (date, account, industry, status).

What stays manual: all DM sending, all replies, all escalations to Hadi.

[2026-04-03] DECISION: N8N SEO Weekly Data Pipeline built — runs every Monday 7am, writes to Google Sheets + seo-current-data.md + sends email summary | REASONING: SEO agent recommendations were being made without live data. Static monthly report was the only source of truth. This pipeline provides current Search Console data automatically every week, making every SEO recommendation traceable to live data rather than a static snapshot. | CONTEXT: Workflow JSON at projects/photography/seo-recovery/n8n-seo-weekly-pipeline.json. Requires credentials setup before first run — see seo-pipeline-setup.md. Three manual test runs required before activating the schedule trigger.

[2026-04-03] DECISION: All new blog posts publish under /blog/ subfolder — existing post URLs unchanged | REASONING: Structural URL consistency for all future posts. Existing 5 posts at root URLs stay permanently — changing them would destroy existing rankings and require 301 redirects across every post. | CONTEXT: Established as part of the April 2026 SEO agent operating protocol overhaul. Blog post #6 (london engagement photoshoot) and all future posts follow /blog/[slug] format.

[2026-04-14] DECISION: Photography content built on 5-pillar framework — My Story, The Belief, Results, Education, The Human. Every reel, carousel, blog, caption, and DM maps to one or more pillars. Story bank serves as raw material library. | REASONING: Current content was drifting into generic territory because there was no identity framework. Hadi diagnosed this and proposed the pillar structure. | CONTEXT: Story bank at projects/photography/story-bank.md. 5 pillars defined with usage rules.

[2026-04-14] DECISION: Manual Instagram research replaces agent-based research for content format discovery. | REASONING: Initial research agent returned weak findings — no UK or EU elopement photographer specifics, mostly generic big-account references. Manual scrolling and observation will be more accurate for niche-specific intelligence. | CONTEXT: Jodie to spend 30 mins on Instagram Explore tomorrow on UK/EU elopement photographer handles.

[2026-04-14] DECISION: 4 content formats approved for photography content rebuild — 30 London Locations in 30 Days, Things I say on a shoot that make couples cry, Photos couples almost didn't take, What I saw today. | REASONING: Selected from 10 brainstormed formats based on attention-grabbing mechanics, follow-along potential, and pillar alignment. | CONTEXT: First format to be built in full once story bank is seeded.

[2026-04-13] DECISION: Photography pricing restructured to The Presence Method — 4 commissions: The Vow (£1,400), The Bloom (£2,300), The Glow (£3,500, most requested), The Odyssey (£5,100). Pre-wedding shoot included from Glow upward. Old 3-tier pricing retired. | REASONING: Perceived discount model anchored at £700/hr (The Vow). Middle tiers feel like the obvious choice. Pre-wedding shoot positioned as the mechanism, not an add-on. | CONTEXT: Full structure at shared/presence-method-packages.md

[2026-04-13] DECISION: Agency pricing restructured to Gear Shift Packages — 4 unified bundles: Core (£497), Drive (£797), Turbo (£1,297, most popular), Nitro (£1,997). Every tier includes voice + WhatsApp + social + content + automation. Old £297/£597/£997 tiers retired. | REASONING: Unified bundle is the differentiator. Competitors sell voice OR social. We sell the full engine. | CONTEXT: Full structure at shared/click-ai-agency-packages.md

[2026-04-13] DECISION: Blog pre-publish checklist is now a mandatory gate. No post goes live without completed checklist + Operator sign-off. | REASONING: Blog #6 went live with insufficient internal links and underplayed core insight. Both caught post-publish. | CONTEXT: Checklist at shared/blog-pre-publish-checklist.md

[2026-04-10] DECISION: Cold email outreach domain is getclick.uk (registered Cloudflare). Stack: Instantly.ai Growth ($37/month) + Apify Google Maps Scraper + Hunter.io (free tier) + ZeroBounce. Target volume 300-500/week. Warmup starts immediately, full volume at Week 5. | REASONING: .uk preferred over .work for deliverability. Apollo dropped — poor coverage for UK local small businesses. | CONTEXT: Setup guide at projects/agency/outreach-system/email-outreach-setup-guide.pdf

[2026-04-10] DECISION: Daily file organisation convention — all files go into DD-MM-YY folder under the relevant business project (projects/photography/DD-MM-YY/ or projects/agency/DD-MM-YY/). Check if folder exists before creating. | REASONING: Hadi requested for easier daily access. | CONTEXT: First folders: projects/photography/10-04-26/ and projects/agency/10-04-26/

[2026-04-10] DECISION: Workflow 4 (CRM auto-logging) deferred to next week — test Workflow 3 in live N8N first. | REASONING: Ship and test before building the next one. | CONTEXT: Workflow 3 JSON at projects/agency/outreach-system/workflow-3-followup-reminder.json

[2026-04-09] BASELINE LOGGED: Homepage title tag change baseline captured. Title changed 4 April 2026 to "London Elopement & Wedding Photographer | Hadi Photography". 28-day baseline (homepage filter): Clicks 40, Impressions 6,310, CTR 0.6%, Avg Position 16.6. Review on 7 May 2026. Primary signal to watch: CTR improvement.

[2026-04-03] DECISION: SEO technical fixes take priority over new blog content — blog post #6 paused | REASONING: Monthly SEO report identified four high-impact technical fixes (meta descriptions, title tag, duplicate page redirect, noindex flags) that will have more ranking impact than any new post right now. Publishing new content on a technically flawed site wastes the effort. | CONTEXT: Blog post #6 (london engagement photoshoot) moves to next week after all four technical fixes are confirmed done by Hadi. New workflow rule added: all reports and audits route through operator first, operator assigns tasks, specialist agents never self-assign from raw reports.
