# Skill: Idea Mining

Use this skill to generate scored video and blog ideas by combining website analytics, a full site inventory, competitor keyword gap analysis, and YouTube/web trends in Hadi's niche.

Invoke with: "Run the idea mining skill" or "Mine some content ideas"

---
Name: idea-mining


## Step 1 — Load Context

Read these files before anything else:

- `context/me.md`
- `context/work.md`
- `context/current-priorities.md`
- `context/goals.md`

---

## Step 2 — Read Analytics

Check `references/analytics/` for any exported analytics file (CSV, PDF, or text). Read the most recently modified file in that folder.

If a file exists: summarise the top pages by traffic, any visible search queries, and traffic sources. Note which services or topics are already drawing visitors.

If no file exists: note the gap ("No analytics data available — proceeding without it") and continue. Prompt Hadi to drop a Google Analytics export there when he gets a chance.

---

## Step 3 — Research Phase (main Claude context — WebSearch + WebFetch directly)

**IMPORTANT:** Do NOT use specialised sub-agent types (`website-audit`, `youtube-trends`, `research`). They do not inherit WebSearch/WebFetch permissions in this environment. Run all research directly using WebSearch and WebFetch in the main context.

### Phase A — Site Audit (WebSearch + WebFetch)

Search for all indexed pages:
```
site:hadiphotographylondon.com
site:hadiphotographylondon.com blog
```

Fetch the homepage, all service pages, and blog posts. For each page record: URL, title, H1, target keyword, word count estimate, content gaps.

### Phase B — Competitor Research (WebSearch, main context)

Run WebSearch queries for direct competitors. The full tracked competitor list is in `projects/seo-monthly-roundup/README.md`. Use that list. For each competitor:
- Search: `[domain] blog posts services london photographer`
- Identify: keywords targeted, blog topics, content gaps vs Hadi

Focus on the 25 tracked direct competitors rather than finding new ones.

### Phase C — YouTube Trends (WebSearch, main context)

Search for trending content in the niche:
```
"london elopement photographer" youtube trending
"couples photoshoot london" youtube views
"surprise proposal london" youtube reaction
```

Extract: trending video formats, title patterns, content gaps nobody is making.

Wait until all three phases are complete before proceeding to Step 4.

---

## Step 4 — Score and Cross-Reference

For each topic or theme surfaced by any of the three agents, assign a score:

| Criterion | 1 | 2 | 3 |
|---|---|---|---|
| **Relevance** | Loosely related to Hadi's work | Directly related to his services | Core service + current priority |
| **Trend signal** | One agent mentioned it | Strong signal from one agent | Appeared in multiple agents |
| **SEO / LLM potential** | Unlikely to rank | Could rank with effort | Clear keyword gap confirmed by competitor analysis |
| **Content gap** | Well-covered on Hadi's site already | Partial coverage | Not covered at all — missing page |

Cross-reference bonus: +2 if a topic appears in both the YouTube agent AND the research agent output.
Analytics bonus: +1 if the topic maps to a keyword already getting impressions in Search Console.

Maximum possible score: 15.

---

## Step 5 — Output

Deliver three lists, sorted by score. Aim for 5-8 ideas per list.

---

**Idea Mining Results**
*Based on: [analytics data / no analytics] + website audit + YouTube trends + 20+ competitor analysis*

**Top Video Ideas**

| # | Title | Format | Score | Why |
|---|---|---|---|---|
| 1 | [title] | [vlog/tutorial/story/BTS] | [X/15] | [1-line reason] |

**Top Blog / Content Ideas**

| # | Title | Content Type | Target Keyword | Score | Why |
|---|---|---|---|---|---|
| 1 | [title] | [blog post / guide / FAQ / location page] | [keyword] | [X/15] | [1-line reason] |

**LLM Visibility Ideas**
Content designed to appear in AI-generated answers (ChatGPT, Perplexity, Google AI Overviews):

| # | Title | Question It Answers | Score | Why |
|---|---|---|---|---|
| 1 | [title] | [e.g. "Who are the best elopement photographers in London?"] | [X/15] | [1-line reason] |

**Repurpose Opportunities**
Ideas that work as BOTH a video and a blog post:
- [title] — [how to angle each]

**Keyword Gap Summary**
- Top 5 keywords competitors rank for that Hadi has no page targeting:
  1. [keyword] — [competitor ranking for it]

**Analytics Insights** *(if data was available)*
- [What's already working that content should support]

---

## Step 6 — Generate PDF Report

After delivering the results in Step 5, compile everything into a full PDF report.

### Report Structure

The report should contain these sections in order:

1. **Cover** — "Idea Mining Report", date, "Hadi Photography London"
2. **Executive Summary** — 3-5 bullet overview of the most important findings
3. **Strengths** — What's working: pages with good rankings, keywords already gaining traction, content that's performing
4. **Weaknesses** — What's holding the site back: thin pages, keyword gaps, missing content types, low CTR despite impressions
5. **Opportunities** — The highest-scored ideas from Step 5, plus keyword gaps identified by competitors, plus LLM visibility angles
6. **Threats** — Competitors who are outranking on key terms; trends that could erode traffic if not acted on
7. **Top Video Ideas** — Full scored table from Step 5
8. **Top Blog / Content Ideas** — Full scored table from Step 5
9. **LLM Visibility Ideas** — Full table from Step 5
10. **Keyword Gap Table** — Keywords competitors rank for that Hadi doesn't
11. **Competitor List** — All 20+ competitors reviewed with URLs
12. **Recommended Next Steps** — Top 3 actions to take this week, this month, this quarter
13. **Analytics Snapshot** — Key metrics from Search Console if available (impressions, clicks, top queries, top pages)

### Save the Report

Save the report to:
```
references/reports/idea-mining-[YYYY-MM-DD].html
```

Generate it as a styled HTML file using this Python script structure:

```python
html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body { font-family: Georgia, serif; max-width: 900px; margin: 40px auto; padding: 0 40px; color: #1a1a1a; line-height: 1.6; }
  h1 { font-size: 2.2em; border-bottom: 3px solid #1a1a1a; padding-bottom: 10px; margin-top: 60px; }
  h2 { font-size: 1.5em; color: #333; margin-top: 40px; border-left: 4px solid #c9a84c; padding-left: 12px; }
  h3 { font-size: 1.1em; color: #555; }
  .cover { text-align: center; padding: 80px 0 60px; border-bottom: 2px solid #eee; }
  .cover h1 { border: none; font-size: 2.8em; }
  .cover p { color: #666; font-size: 1.1em; }
  table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 0.9em; }
  th { background: #1a1a1a; color: white; padding: 10px 12px; text-align: left; }
  td { padding: 9px 12px; border-bottom: 1px solid #eee; }
  tr:nth-child(even) td { background: #f9f9f9; }
  .strength { border-left: 4px solid #2ecc71; padding-left: 12px; margin: 8px 0; }
  .weakness { border-left: 4px solid #e74c3c; padding-left: 12px; margin: 8px 0; }
  .opportunity { border-left: 4px solid #3498db; padding-left: 12px; margin: 8px 0; }
  .threat { border-left: 4px solid #e67e22; padding-left: 12px; margin: 8px 0; }
  .next-step { background: #f0f7ff; border: 1px solid #3498db; border-radius: 6px; padding: 16px 20px; margin: 12px 0; }
  ul { padding-left: 20px; }
  li { margin: 6px 0; }
</style>
</head>
<body>
[REPORT CONTENT HERE]
</body>
</html>"""

with open("references/reports/idea-mining-YYYY-MM-DD.html", "w") as f:
    f.write(html_content)
```

Fill in all sections with the actual data from the run. Use the colour-coded div classes (`.strength`, `.weakness`, `.opportunity`, `.threat`) for the SWOT items.

### Convert to PDF

After saving the HTML, check for available PDF tools and use the best one:

```bash
# Check what's available
if command -v wkhtmltopdf &> /dev/null; then
    wkhtmltopdf --page-size A4 --margin-top 15mm --margin-bottom 15mm \
      --margin-left 15mm --margin-right 15mm \
      "references/reports/idea-mining-YYYY-MM-DD.html" \
      "references/reports/idea-mining-YYYY-MM-DD.pdf"
    echo "PDF saved to references/reports/"
elif command -v pandoc &> /dev/null; then
    pandoc "references/reports/idea-mining-YYYY-MM-DD.html" \
      -o "references/reports/idea-mining-YYYY-MM-DD.pdf"
    echo "PDF saved to references/reports/"
else
    open "references/reports/idea-mining-YYYY-MM-DD.html"
    echo "No PDF converter found. HTML report opened in browser. Press Cmd+P then Save as PDF to export."
fi
```

Tell Hadi where the report was saved (or opened) once complete.

---

## Notes

- Run this skill monthly or whenever Hadi needs a fresh batch of ideas.
- Update `references/analytics/` with a fresh export before running for best results.
- Phase A agents run in parallel. Phase B runs after. Full pipeline: 5-8 minutes.
- The PDF is saved to `references/reports/` with the date in the filename.
- Ideas with the highest scores are the best starting points. Don't act on all of them at once.
- The keyword gap table is the most actionable SEO output — prioritise those first.
