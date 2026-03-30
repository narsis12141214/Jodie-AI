# Skill: Research

Use this skill whenever Hadi asks you to research a topic, investigate competitors, find content ideas, explore SEO opportunities, or gather any information that benefits from real-time web sources.

---
Name: research


## When to Use This Skill

- "Research [topic]"
- "Look into [topic] for me"
- "What are competitors doing with [X]?"
- "Find content ideas for [X]"
- "Research SEO keywords for [X]"
- Any request that needs current, sourced, web-based information

---

## How to Execute Research

### Step 1 — Load Context

Before forming any queries, read these files to ground the research in Hadi's reality:

- `@context/me.md` — who Hadi is
- `@context/work.md` — his business, services, pricing, current situation
- `@context/current-priorities.md` — what matters right now
- `@context/goals.md` — Q2 2026 milestones

If the topic maps to an active project, also read the relevant `projects/[project]/README.md`.

### Step 2 — Frame the Research

Before calling the API, briefly state:
- What you're researching and why it's relevant to Hadi
- The angle (competitive intel, SEO, content ideas, market trends, etc.)
- Which model you're using: `sonar-deep-research` for thorough work, `sonar-pro` for quicker lookups

### Step 3 — Call the Perplexity API

Load the API key from `.env` and call the API using `curl`. Always write the request body to a temp file first — do not embed JSON inline in the curl command (shell quoting breaks it).

```bash
cd "/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI" && source .env

# Step 1: Write the request body to a temp file
cat > /tmp/perplexity_request.json << 'ENDJSON'
{
  "model": "sonar-deep-research",
  "messages": [
    {
      "role": "system",
      "content": "You are a research assistant helping Hadi Yazdani, a London-based photographer who specialises in couples, engagement, pre-wedding, surprise proposal, and elopement photography. His business is called Hadi Photography London (hadiphotographylondon.com, Instagram @hadyyazdani). He is currently in a business recovery phase after a website redesign caused a drop in Google rankings and ~1 year of social media dormancy. His priorities are rebuilding SEO, reactivating Instagram, launching YouTube, building LinkedIn, and creating pricing guides. Keep all research grounded in this context and make it actionable for a solo photographer in London."
    },
    {
      "role": "user",
      "content": "INSERT RESEARCH QUERY HERE"
    }
  ]
}
ENDJSON

# Step 2: Call the API, save response
curl -s -X POST https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/perplexity_request.json \
  > /tmp/perplexity_response.json

# Step 3: Extract the content
python3 -c "
import json, sys
d = json.load(open('/tmp/perplexity_response.json'))
if 'choices' in d:
    print(d['choices'][0]['message']['content'])
elif 'error' in d:
    print('API ERROR:', d['error'])
else:
    print(json.dumps(d, indent=2))
"
```

**Important:** Replace `INSERT RESEARCH QUERY HERE` inside the ENDJSON block with the actual query. Do not use single quotes inside the query — use double quotes or rephrase.

**Model guidance:**
- `sonar-deep-research` — default. Best for competitive research, SEO analysis, content strategy, industry deep-dives. Takes 1-3 minutes. Returns cited sources.
- `sonar-pro` — faster. Good for quick facts, follow-up questions, or when speed matters more than depth.
- `sonar` — fastest. Use for simple factual lookups only.

Craft the query to be specific and tied to Hadi's context. Don't send a generic query — include relevant details (London, photography niche, business stage) in the user message itself as well.

### Step 4 — Synthesise and Deliver

Parse the API response and present findings in this structure:

---

**Research: [Topic]**

**Summary**
- [3-5 key findings as bullets]

**What This Means for Hadi**
- [How findings apply specifically to his business, projects, and current priorities]

**Actionable Next Steps**
1. [Concrete action]
2. [Concrete action]
3. [Concrete action]

**Sources**
- [Citations from Perplexity response]

**Follow-up Research Angles**
- [Suggested deeper threads if useful]

---

## Error Handling

- **Empty response or file not found:** Check that you `cd` into the project directory and `source .env` before writing the temp file. The working directory must be correct.
- **API key missing:** Tell Hadi to open `.env` and confirm `PERPLEXITY_API_KEY=pplx-...` is present with no extra spaces.
- **401 Unauthorized:** API key is wrong or expired. Ask Hadi to check at perplexity.ai.
- **JSON parse error:** The query inside the ENDJSON block may contain a single quote or unescaped character. Rephrase to avoid single quotes.
- **Slow response (sonar-deep-research):** Normal — takes 1-3 minutes. Do not retry. Wait for it.
- **Results too generic:** Re-run with a more specific query including more of Hadi's context (location, niche, business stage, specific competitor names).

---

## Notes

- The `.env` file is git-ignored and never committed. It's safe to store the API key there.
- `sonar-deep-research` is slower but gives the most thorough, cited results. Use it by default.
- Always tie research output back to Hadi's active priorities and projects — generic research is not the goal.
