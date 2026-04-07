# Session Log — 7 April 2026

## Workflow 1 (Lead Identification) — Updated

Added two-stage scrape to pull real profile data after the hashtag scrape.

**New nodes added** (inserted between Filter & Format Leads and Get Existing Leads):
`Start Profile Scraper → Wait 3 Minutes → Fetch Profile Results → Merge Profile Data`

**Start Profile Scraper**
- Apify actor: `apify~instagram-profile-scraper`
- Limited to 20 usernames per run — free tier memory limit is 8192MB, exceeding it causes 502 errors
- Execute Once must be ON — otherwise N8N fires one request per input item (96 calls instead of 1)
- Body format: `{ "usernames": {{ JSON.stringify($input.all().slice(0,20).map(i => i.json['Instagram Handle'].replace('@',''))) }} }`
- Usernames must be a JSON array, not a comma-separated string

**Fetch Profile Results**
- GET request to Apify dataset endpoint using run ID from Start Profile Scraper
- URL: `https://api.apify.com/v2/actor-runs/{{$('Start Profile Scraper').item.json.data.id}}/dataset/items?token=TOKEN&clean=true`
- URL field must be in expression mode (fx) — not typed as a literal string starting with `=`

**Merge Profile Data**
- Pulls `biography` → Notes and `followersCount` → Followers from profile results
- Falls back to post caption if no bio found
- Builds a profileMap keyed by lowercase username for O(1) lookup

**Remove Duplicates — critical fix**
- Must reference `$('Merge Profile Data').all()` not `$('Filter & Format Leads').all()`
- Using the wrong source bypasses all merged profile data — leads would write with "Check manually" and no bio

**Append to Lead Sheet**
- Switch Mapping Column Mode to Map Automatically when new columns are added to the sheet after the workflow was originally built
- Hardcoded column schemas go stale — Map Automatically reads headers dynamically

---

## Workflow 2 (Opener Generation) — Built and fixed

**Generate Opener node (Code node)**
- Mode: Run Once for All Items — loops internally, one Claude API call per lead
- Uses `$input.all()` and returns an array of items
- API key stored directly in code (VPS is private — acceptable short term, migrate to environment variable when possible)
- Model: `claude-haiku-4-5`
- Output fields: `row_number`, `business_name`, `instagram_handle`, `status`, `opener`, `generated_at`

**The `json` field conflict — root cause and fix**
- Unnamed extra columns in the Google Sheet get internally named `json` by N8N
- Spreading `...lead` on Google Sheets data copies this field and causes: `A 'json' property isn't an object`
- Fix 1: Restrict read range to `A3:R` in Read Lead Sheet node to cut off unnamed columns
- Fix 2: Never use spread on sheet data — always explicitly pick named fields
- Fix 3: In Filter New Leads, strip rogue `json` field from all items before returning — return `cleanLeads` not `newLeads`

**Filter New Leads node**
- Mode: Run Once for All Items
- Must clean items before returning — loop through keys, skip any key named `json`, return `{ json: cleaned }`
- Return variable must be `cleanLeads` not `newLeads`

**Update Lead Row node**
- Column to match on: must be set to `row_number`
- Without this set, N8N returns: `Could not find column for key "undefined"`

**Build Email Summary node**
- Use string concatenation not template literals — avoids N8N parsing issues with backticks
- Field names must match Generate Opener output exactly: `instagram_handle`, `business_name`, `industry`, `opener`
- Syntax errors in the map function silently break all name/handle lookups — everything returns 'unknown'

---

## General N8N lessons from this session

- `$input.first()` is only valid in Run Once for All Items mode — in Run Once for Each Item, use `$input.item.json`
- Execute Once must be ON for: Get Existing Leads, Start Profile Scraper, Gmail notify nodes
- HTTP Request nodes cannot access N8N credentials from inside Code nodes — use a dedicated HTTP Request node with Header Auth credential, or hardcode on private VPS
- Apify profile scraper takes ~40 seconds for 20 profiles — Wait node before Fetch should be at least 2 minutes
- Apify returns 502 Bad Gateway occasionally under load — retry the node, it's server-side and not a code issue
- When Google Sheets columns are added after a workflow is built, refresh or switch to Map Automatically — hardcoded schemas go stale silently
- Never store API keys in chat messages or screenshots — rotate immediately if exposed
