# Quality Log
## Jodie-AI — Continuous Improvement Record

This file is append-only. Every error caught during or after the pipeline gets logged here — whether caught by Hadi, Jodie, or during post-publish review. Over time this becomes the institutional memory of what the system gets wrong and how it was fixed.

**Log every entry. No exceptions. A missed entry is a missed improvement.**

---

## Format

```
[DATE] | [AGENT] | [ERROR] | [HOW CAUGHT] | [FIX APPLIED] | [RULE ADDED TO AGENT]
```

---

## Log

| Date | Agent | Error | How Caught | Fix Applied | Rule Added |
|------|-------|-------|------------|-------------|------------|
| 2026-04-01 | photography/seo | Keyword not flagged as missing from first 100 words — post would have published with keyword buried mid-paragraph | Caught by Hadi during manual review | Keyword moved to standalone sentence within first 100 words | Yes — mandatory flag added to SEO checklist + hard rule at bottom of seo.md |
| 2026-04-01 | photography/blog-copywriter | No rule requiring keyword in first 100 words of opening — agent was structuring intros as pure narrative without keyword signal | Caught by Hadi during manual review | Rule added to Voice section of blog-copywriter.md | Yes — keyword-in-first-100-words rule added |
| 2026-04-01 | photography/seo | Word count not being checked at SEO review stage — post came in at ~1,800 words against 2,500-2,700 target | Post-review quality check | St Dunstan section added to bring post into range | Yes — flag anything under 2,400 words before clearing |
| 2026-04-01 | photography/seo + photography/blog-copywriter | Meta title and meta description not included in final HTML deliverable | Post-review quality check | SEO agent updated to embed meta data block at top of every cleared HTML file | Yes — meta data block format added to seo.md output requirements |
| 2026-04-01 | photography/seo | Structural review triggered by 3 quality log entries in one session — flat checklist gave no hierarchy between blocking and advisory failures | Quality log pattern review | Full structural rebuild — two-tier blocking/advisory checklist, duplicate reference checklist removed, rules consolidated | Yes — rebuilt file replaces patched version |
| 2026-04-05 | shared/operator | Blog post #6 assigned as "london engagement photoshoot" without checking the monthly report's scored content ideas table. Pre-wedding photoshoot (13/15) was the correct next topic — engagement was not in the top-scored list and carried cannibalisation risk. | Caught by Hadi during operator review | Blog post #6 topic corrected to Pre-Wedding Photoshoot London | Yes — Blog Post Topic Assignment mandatory check added to operator.md |
| 2026-04-05 | agency/outreach workflow-1 | Three bugs in Workflow 1 JSON: (1) resultsType set to "profiles" — invalid, should be "details"; (2) Fetch node used /runs/last/ instead of run-specific ID; (3) wait time 4 mins too short for Apify to complete | Caught during live test run | Fixed in JSON + N8N: resultsType→details, fetch URL uses $('Start Apify Instagram Scraper').item.json.data.id, wait increased to 8 mins | Yes — workflow-1 JSON updated |
| 2026-04-08 | agency/workflow-2-opener-generation | Claude generated "Love that you're keeping the seasonal momentum going" — soft compliment disguised as observation, violating no-generic-compliments rule | Caught by Hadi during live outreach (Cocorico Italian restaurant reply) | Prompt updated — added explicit ban: no "love that", "great that", "impressive that", "rare to see", "good to see". State what you noticed, not how you feel about it | Yes — JSON updated; Hadi to paste updated prompt into N8N live workflow |
| 2026-04-09 | agency/outreach workflow-1 | Get Existing Leads node using default header row 1 instead of row 3 — caused duplicate leads appearing 3-4 times in tracker | Caught by Hadi during live run review | Header row corrected to 3 in N8N. Wait node re-enabled. Append to Lead Sheet switched to Map Automatically. Filter by Follower Count node added. | Yes — workflow-1 session log updated |
| 2026-04-09 | agency/outreach — Zizi manual scripts | Crockers Tring opener broke three rules: "genuinely impressive" (compliment), "No pressure" (forbidden phrase), "Free 7 day trial" (forbidden word "free") | Caught by Jodie during reply review | Flagged to Hadi. Changes did not apply as message sent before 8 April fixes. | Reminder issued — Zizi manual scripts must follow same rules as generated openers |

---

## Patterns (update monthly)

Review this section every Monday. If the same agent appears 3+ times, it needs a structural rewrite, not just rule additions.

| Agent | Error Count | Most Common Failure | Last Reviewed |
|-------|-------------|---------------------|---------------|
| photography/seo | 4 | Missing checklist items at review stage — structurally rebuilt 2026-04-01 | 2026-04-01 |
| photography/blog-copywriter | 1 | Keyword placement in opening | 2026-04-01 |
| shared/operator | 1 | Blog post topic assigned without checking monthly report scored table | 2026-04-05 |

---

## Rules

- Every entry must be logged on the day the error is caught
- If Hadi catches something the pipeline should have caught — log it immediately and update the agent before the next post
- If the same error recurs after a rule was added — the rule was written wrong. Rewrite it, don't just add another rule.
- Once per week (Monday): review patterns table and decide if any agent needs a structural update
