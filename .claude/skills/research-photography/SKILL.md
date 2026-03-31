# Skill: Research — Hadi Photography London

Use this skill whenever research is needed for Hadi Photography London — competitor photographers, SEO keywords, wedding/elopement trends, London market data, content ideas, or any information that benefits from real-time web sources.

Invoked by: `photography/research` agent

---
Name: research-photography

---

## When to Use This Skill

- "Research [topic] for the photography business"
- "What are competitor photographers doing with [X]?"
- "Find content ideas for @hadyyazdani"
- "Research SEO keywords for hadiphotographylondon.com"
- "What are wedding/elopement trends in London right now?"
- Any photography-specific request needing current, sourced, web-based information

---

## How to Execute Research

### Step 1 — Load Context

Before forming any queries, read:

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

Load the API key from `.env` and call the API using `curl`. Always write the request body to a temp file first — do not embed JSON inline in the curl command.

```bash
cd "/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI" && source .env

cat > /tmp/perplexity_request.json << 'ENDJSON'
{
  "model": "sonar-deep-research",
  "messages": [
    {
      "role": "system",
      "content": "You are a research assistant helping Hadi Yazdani, a London-based photographer who specialises in couples, engagement, pre-wedding, surprise proposal, and elopement photography. His business is called Hadi Photography London (hadiphotographylondon.com, Instagram @hadyyazdani, 13.5K followers, verified). He has 100 five-star reviews and is in an active SEO recovery phase — key rankings are improving fast. His priorities are: growing organic search traffic, publishing one SEO blog post per week, rebuilding @hadyyazdani Instagram presence, and converting inbound enquiries. Keep all research grounded in this context and make it actionable for a solo photographer in London."
    },
    {
      "role": "user",
      "content": "INSERT RESEARCH QUERY HERE"
    }
  ]
}
ENDJSON

curl -s -X POST https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/perplexity_request.json \
  > /tmp/perplexity_response.json

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
- `sonar-deep-research` — default. Best for competitive research, SEO analysis, content strategy, industry deep-dives. Takes 1–3 minutes. Returns cited sources.
- `sonar-pro` — faster. Good for quick facts or follow-up questions.
- `sonar` — fastest. Simple factual lookups only.

### Step 4 — Synthesise and Deliver

```
RESEARCH: [Topic]
BUSINESS: Hadi Photography London

SUMMARY
[3–5 key findings]

WHAT THIS MEANS FOR HADI
[How findings apply specifically — London photography market, his current rankings, his audience]

ACTIONABLE NEXT STEPS
1. [Concrete action]
2. [Concrete action]
3. [Concrete action]

SOURCES
[Citations from Perplexity response]

FOLLOW-UP ANGLES
[Suggested deeper threads if useful]
```

---

## Error Handling

- **Empty response or file not found:** Check `cd` into project directory and `source .env` before writing temp file
- **API key missing:** Open `.env` and confirm `PERPLEXITY_API_KEY=pplx-...` is present with no extra spaces
- **401 Unauthorized:** API key wrong or expired — check at perplexity.ai
- **JSON parse error:** Query contains a single quote — rephrase to avoid single quotes
- **Slow response:** Normal for `sonar-deep-research` — takes 1–3 minutes. Do not retry. Wait.
- **Results too generic:** Re-run with more specific query — include London, photography niche, competitor names

---

## Notes

- `.env` is git-ignored and never committed
- `sonar-deep-research` is the default — use it unless speed is the priority
- Always tie output back to photography priorities — generic research is not the goal
