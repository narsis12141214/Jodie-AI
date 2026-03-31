# Skill: Research — Click AI Agency

Use this skill whenever research is needed for Click AI Agency — competitor agencies, local business market data, AI tool comparisons, outreach targeting, industry trends, lead qualification, or any information that benefits from real-time web sources.

Invoked by: `agency/research` agent

---
Name: research-agency

---

## When to Use This Skill

- "Research competitor AI agencies in London"
- "What are [industry] businesses in London struggling with right now?"
- "Compare [tool A] vs [tool B] for client use case"
- "Find leads in [industry] for Zizi's outreach"
- "What are small businesses paying for AI services?"
- "Research [industry] market data for a proposal"
- Any agency-specific request needing current, sourced, web-based information

---

## How to Execute Research

### Step 1 — Load Context

Before forming any queries, read:

- `@context/me.md` — who Hadi is
- `@context/work.md` — both businesses, agency services, pricing, pipeline
- `@context/current-priorities.md` — active leads and this week's targets
- `@context/goals.md` — Q2 2026 milestones

If the research relates to an active lead, also read the relevant pipeline notes.

### Step 2 — Frame the Research

Before calling the API, briefly state:
- What you're researching and why it's relevant to the agency right now
- The angle (competitor intel, lead qualification, tool comparison, market sizing, etc.)
- Which model: `sonar-deep-research` for thorough work, `sonar-pro` for quicker lookups

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
      "content": "You are a research assistant helping Hadi Yazdani, founder of Click AI Agency (clickaiagency.com, Instagram @clickaiagency), a London-based AI agency that builds AI systems for small businesses — primarily AI receptionists, voice agents, and content engines. Target clients are one-to-three person businesses in industries including dental clinics, beauty clinics, estate agents, barbers, cafes, restaurants, electricians, plumbers, carpenters, and photographers. The agency is in week 3 of its launch with no revenue closed yet and approximately two months of financial runway. Active pipeline includes leads in health, restaurant, and beauty sectors. Outreach is conducted via Instagram DM by an employee named Zizi. Keep all research grounded in this context and make it actionable for an early-stage AI agency targeting small businesses in London."
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
- `sonar-deep-research` — default. Best for competitor analysis, market sizing, industry deep-dives, tool comparisons. Takes 1–3 minutes. Returns cited sources.
- `sonar-pro` — faster. Good for quick lead qualification or follow-up questions.
- `sonar` — fastest. Simple factual lookups only.

### Step 4 — Synthesise and Deliver

```
RESEARCH: [Topic]
BUSINESS: Click AI Agency

SUMMARY
[3–5 key findings]

WHAT THIS MEANS FOR THE AGENCY
[How findings apply specifically — London small business market, active pipeline, outreach targeting, pricing, positioning]

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
- **Results too generic:** Re-run with more specific query — include London, specific industry, business size, competitor names

---

## Notes

- `.env` is git-ignored and never committed
- `sonar-deep-research` is the default — use it unless speed is the priority
- Always tie output back to agency priorities — closing the first client is the only metric that matters right now
- When researching leads or industries for Zizi, always output in a format she can act on immediately
