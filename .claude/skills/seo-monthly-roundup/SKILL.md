# Skill: SEO Monthly Roundup

Run this skill once a month to produce a comprehensive SEO research report covering your website, 25 direct competitors, audience signal, SWOT, and scored content ideas.

Invoke with: "Run the SEO monthly roundup" or "Do the monthly SEO report"

---
Name: seo-monthly-roundup


## IMPORTANT: Tool Architecture

**All research runs directly in the main Claude context.**

- **Competitor research:** Use Perplexity API via Bash (`sonar-deep-research`). This is the primary method — much more thorough than WebSearch alone.
- **Site audit + audience signal:** Use WebSearch + WebFetch directly in the main context.
- **Do NOT** use specialised sub-agent types (`website-audit`, `youtube-trends`, `research`) — they cannot use Bash or WebSearch/WebFetch.
- **Do NOT** use `general-purpose` agents for research — they hit rate limits and lose context.
- **Curl pattern:** Always write the JSON body to a temp file first (`-d @/tmp/file.json`). Never embed JSON inline in the curl command — shell quoting breaks it.

---

## Step 1 — Load Context

Read these files before starting:
- `context/me.md`
- `context/work.md`
- `context/current-priorities.md`
- `context/goals.md`
- `memory/seo-current-data.md` — **primary data source**. This file is auto-generated every Monday by the N8N SEO weekly pipeline. It contains live Search Console data: top keywords by impressions, top pages by clicks, flagged movements, week-on-week changes. Use this as the analytics input for Steps 2 and 6. If `last_updated` is more than 7 days old, flag to Hadi that the pipeline may not have run before proceeding.
- `projects/seo-monthly-roundup/README.md` — check which competitors are tracked

**Do not look for a manual CSV export in `references/analytics/`.** The weekly pipeline replaces manual exports. The Google Sheet with full history is linked in `memory/seo-current-data.md` for deeper data if needed.

---

## Step 2 — Site Audit (WebSearch + WebFetch, main context)

Run these searches to discover all pages:
```
site:hadiphotographylondon.com
site:hadiphotographylondon.com blog
```

Fetch the homepage, all service pages, and all blog posts found.

For each page record:
- Full URL
- Title tag and H1
- H2/H3 structure
- Meta description
- Approximate word count
- Any obvious SEO issues (thin content, missing H1, off-brand topic, JS-heavy platform)
- Internal links to/from other pages

Flag pages that are off-brand, outdated, or should be noindexed.

---

## Step 3 — Competitor Research (Perplexity API via Bash)

Before running competitor calls, inject the live keyword data from `memory/seo-current-data.md` into the Perplexity system prompt. This gives Perplexity context on which keywords Hadi is already ranking for and where the gaps are — making the competitor analysis sharper and directly actionable.

Use `sonar-deep-research` for deep, cited competitor analysis. Run 3 Perplexity calls in sequence — one per batch of ~8-9 competitors. This is far more thorough than WebSearch alone.

**Pattern for each call — always use temp file, never inline JSON:**

```bash
cd "/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI" && source .env

cat > /tmp/seo_competitors_batch1.json << 'ENDJSON'
{
  "model": "sonar-deep-research",
  "messages": [
    {
      "role": "system",
      "content": "You are a competitor research analyst for Hadi Photography London (hadiphotographylondon.com), a London photographer specialising in couples, engagement, pre-wedding, elopement, and surprise proposal photography. His business is in SEO recovery after a website redesign. Be specific: list actual blog post titles, actual pricing figures, actual awards/associations, and concrete content gaps vs Hadi."
    },
    {
      "role": "user",
      "content": "Analyse these London photography competitors for Hadi Photography: [LIST DOMAINS HERE]. For each: (A) site status and primary services (B) blog post titles found (C) SEO keywords in page titles and H1s (D) positioning: luxury/documentary/editorial/value (E) pricing if visible (F) awards, press features, associations (G) content strengths (H) specific keywords or pages they have that Hadi does not. Be specific — quote actual titles and figures."
    }
  ]
}
ENDJSON

curl -s -X POST https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/seo_competitors_batch1.json \
  > /tmp/seo_competitors_batch1_response.json

python3 -c "
import json
d = json.load(open('/tmp/seo_competitors_batch1_response.json'))
if 'choices' in d:
    print(d['choices'][0]['message']['content'])
else:
    print('ERROR:', json.dumps(d, indent=2))
"
```

Repeat for batch 2 and batch 3, using different temp file names each time (`batch2`, `batch3`).

**After all three batches**, run a fourth synthesis call:

```bash
cat > /tmp/seo_synthesis.json << 'ENDJSON'
{
  "model": "sonar-pro",
  "messages": [
    {
      "role": "system",
      "content": "You are a competitor research analyst for Hadi Photography London (hadiphotographylondon.com)."
    },
    {
      "role": "user",
      "content": "Based on research across 25 London photography competitors, what are: (1) the top 10 keywords they rank for that Hadi has no page targeting? (2) blog topics that appear on 5+ competitor sites that Hadi is missing? (3) the positioning gap Hadi can own — what style, niche, or angle is underserved in the London market? Focus on: couples, engagement, pre-wedding, elopement, surprise proposal photography in London."
    }
  ]
}
ENDJSON

curl -s -X POST https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/seo_synthesis.json \
  > /tmp/seo_synthesis_response.json

python3 -c "
import json
d = json.load(open('/tmp/seo_synthesis_response.json'))
if 'choices' in d:
    print(d['choices'][0]['message']['content'])
else:
    print('ERROR:', json.dumps(d, indent=2))
"
```

The full 25-competitor list is in `projects/seo-monthly-roundup/README.md`.

---

## Step 4 — Audience Signal (WebSearch + WebFetch, main context)

Search for real discussions where couples ask about photographers:
```
reddit "london photographer" couples engagement recommendation
mumsnet wedding photographer london questions
"how to find" OR "how to choose" wedding photographer london forum
london proposal photographer advice forum 2025 2026
```

Fetch the most relevant results. Extract:
- What specific questions couples ask
- What concerns or fears they have (price, intrusiveness, missing moments)
- What makes them choose one photographer over another
- Recurring pain points

---

## Step 5 — YouTube Trends (WebSearch, main context)

```
"london elopement photographer" youtube trending views
"couples photoshoot london" youtube channel
"surprise proposal london" youtube reaction viral
"london wedding photographer" youtube channel 2025 2026
```

Extract:
- Trending video formats (BTS, reaction, tutorial, vlog)
- Title patterns that get views
- Content gaps — what London photographers are NOT making

---

## Step 6 — Synthesise SWOT

Using all research gathered, build a data-backed SWOT:

**Strengths** — pages near page 1, content assets, brand signals, pricing advantages
**Weaknesses** — missing pages, thin content, off-brand pages, low CTR pages
**Opportunities** — keyword gaps competitors rank for, content angles nobody owns, YouTube gap
**Threats** — competitors gaining authority (awards, press, new pages), content moats being built

Each SWOT point must cite a specific competitor, page, or data point. No generic statements.

---

## Step 7 — Score Content Ideas

For each topic or content angle surfaced by the research, score it:

| Criterion | 1 | 2 | 3 |
|---|---|---|---|
| **Relevance** | Loosely related | Directly related to services | Core service + current priority |
| **Keyword gap** | Hadi has coverage | Partial coverage | No page exists at all |
| **Competitor signal** | 1 competitor has it | 2-3 competitors have it | 5+ competitors have it |
| **Audience demand** | Not mentioned in discussions | Mentioned occasionally | Recurring pain point or question |
| **SEO potential** | Unlikely to rank | Could rank with effort | Clear gap confirmed |

Maximum: 15. Prioritise anything scoring 11+.

---

## Step 8 — Generate Report

Save the report to:
```
projects/seo-monthly-roundup/seo-roundup-[YYYY-MM-DD].html
```

### Report Sections (in order)

1. **Cover** — title, date, tagline
2. **Executive Summary** — 5 bullets, most important findings
3. **Analytics Snapshot** — metrics table from Search Console if available
4. **Full Site Audit** — all pages with titles, issues, missing pages table
5. **SWOT Analysis** — 2x2 grid, data-backed
6. **Competitor Breakdown** — all 25 with positioning, blog content, content gaps
7. **Audience Signal** — real quotes and concern table
8. **Keyword Gap Table** — keyword, intent, who ranks, Hadi's gap, priority
9. **Top Blog & Content Ideas** — scored table
10. **Top Video Ideas** — scored table
11. **LLM Visibility Ideas** — scored table
12. **Recommended Next Steps** — this week / this month / this quarter
13. **Full Competitor List** — all 25 in a table

Use the HTML template style from the existing report at `projects/seo-monthly-roundup/seo-roundup-2026-03-29.html` as the visual reference.

---

## Step 9 — Open Report

```bash
open "projects/seo-monthly-roundup/seo-roundup-[YYYY-MM-DD].html"
```

Tell Hadi the report is ready and where it's saved.

---

## Step 10 — Update README

Add the new report to the table in `projects/seo-monthly-roundup/README.md`.

---

## Notes

- Run monthly. Data comes from `memory/seo-current-data.md` — auto-generated every Monday by the N8N SEO weekly pipeline. No manual CSV export needed. For deeper historical data, use the Google Sheet linked in that file.
- The 25 competitor list is in `projects/seo-monthly-roundup/README.md` — update it if competitors change.
- `sonar-deep-research` takes 1-3 minutes per call. This is normal — do not retry. Wait for it.
- Always use temp files for curl JSON bodies. Never embed JSON inline in curl commands.
- If a Perplexity call returns an error, check the raw JSON in `/tmp/` for the error message.
- WebSearch rate limit: if you hit a daily limit on WebSearch, finish remaining steps with Perplexity calls instead.
- Do not use specialised sub-agents (`website-audit`, `youtube-trends`, `research`). Do not use general-purpose agents for research steps.
- Full pipeline time: 25-40 minutes running all Perplexity calls sequentially.
