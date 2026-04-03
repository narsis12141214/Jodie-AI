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

[2026-04-03] DECISION: SEO technical fixes take priority over new blog content — blog post #6 paused | REASONING: Monthly SEO report identified four high-impact technical fixes (meta descriptions, title tag, duplicate page redirect, noindex flags) that will have more ranking impact than any new post right now. Publishing new content on a technically flawed site wastes the effort. | CONTEXT: Blog post #6 (london engagement photoshoot) moves to next week after all four technical fixes are confirmed done by Hadi. New workflow rule added: all reports and audits route through operator first, operator assigns tasks, specialist agents never self-assign from raw reports.
