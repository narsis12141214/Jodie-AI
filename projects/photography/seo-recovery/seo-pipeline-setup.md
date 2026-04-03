# SEO Weekly Pipeline — Setup Instructions
Created: 3 April 2026

Complete all steps in order. Do not import the workflow until credentials are set up.

---

## Step 1 — Google Cloud Console setup

1. Go to console.cloud.google.com
2. Create a new project (or use an existing one)
3. Enable these two APIs:
   - Google Search Console API
   - Google Sheets API
4. Go to APIs & Services > Credentials > Create Credentials > OAuth 2.0 Client ID
5. Application type: Web application
6. Add authorised redirect URI: `https://n8n.srv1466538.hstgr.cloud/rest/oauth2-credential/callback`
7. Save the Client ID and Client Secret

---

## Step 2 — Set up Google OAuth2 credential in N8N

1. Open N8N: n8n.srv1466538.hstgr.cloud
2. Settings > Credentials > Add Credential > OAuth2 API (generic)
3. Fill in:
   - Name: `Google OAuth2 (Search Console + Sheets)`
   - Grant Type: Authorization Code
   - Authorization URL: `https://accounts.google.com/o/oauth2/auth`
   - Access Token URL: `https://oauth2.googleapis.com/token`
   - Client ID: [from Step 1]
   - Client Secret: [from Step 1]
   - Scope: `https://www.googleapis.com/auth/webmasters.readonly https://www.googleapis.com/auth/spreadsheets`
   - Auth URI Query Parameters: `access_type=offline&prompt=consent`
4. Click Connect — this opens Google OAuth flow
5. Authorize with the Google account that has access to hadiphotographylondon.com in Search Console
6. Save the credential — note the credential ID (visible in the URL when editing)
7. Replace `GOOGLE_OAUTH2_CREDENTIAL_ID` in the workflow JSON with this ID

---

## Step 3 — Set up Gmail credential in N8N

1. Settings > Credentials > Add Credential > Gmail OAuth2
2. Follow the Google OAuth flow — same Google account
3. Authorize Gmail send access
4. Save and note the credential ID
5. Replace `GMAIL_CREDENTIAL_ID` in the workflow JSON with this ID
6. Replace `YOUR_HADI_EMAIL` with your actual email address

---

## Step 4 — Create the Google Sheet

1. Go to Google Drive
2. Create a new Google Sheet named: `Hadi Photography — SEO Weekly Data`
3. Create four tabs with exactly these names:
   - `This Week Keywords`
   - `This Week Pages`
   - `Weekly History`
   - `Flagged Items`
4. In `This Week Keywords` — add these headers in row 1:
   Keyword | Clicks | Impressions | CTR | Avg Position | Click Change | Impression Change | Position Change | Flag
5. In `This Week Pages` — add headers in row 1:
   Page | Clicks | Impressions | CTR | Avg Position | Flag
6. In `Weekly History` — add headers in row 1:
   Week Ending | Total Clicks | Total Impressions | Overall CTR | Avg Position | Top Keyword | Top Page
7. In `Flagged Items` — add headers in row 1:
   Date | Type | Item | Flag Reason | Current Value | Previous Value
8. Copy the Sheet ID from the URL (the long string between /d/ and /edit)
9. Replace `YOUR_SEO_SHEET_ID` in the workflow JSON with this ID (appears in 8 places)

---

## Step 5 — Generate a GitHub personal access token

1. Go to github.com/settings/tokens
2. Generate new token (classic)
3. Scopes needed: `repo` (full control of private repositories)
4. Copy the token
5. Replace `YOUR_GITHUB_TOKEN` in the workflow JSON (appears in 2 places — nodes 017 and 018)

---

## Step 6 — Verify Search Console property

1. Confirm hadiphotographylondon.com is verified in Google Search Console
2. The property type must be URL prefix: `https://www.hadiphotographylondon.com/`
3. The Google account used in Step 2 must have at least Read access to this property

---

## Step 7 — Import and test the workflow

1. Open N8N > Workflows > Import
2. Import `n8n-seo-weekly-pipeline.json`
3. Open the imported workflow
4. Verify all credential references are connected (yellow warnings = disconnected)
5. Connect credentials to each node where prompted

**Test run 1 — confirm API auth:**
- Manually run just nodes 001-005 (Schedule, Set Dates, three HTTP nodes)
- Check that data is returned from Search Console (rows array with keywords/pages)
- If 401/403: credential setup is wrong — revisit Step 2
- If 403 with "User does not have sufficient permissions": account doesn't have Search Console access

**Test run 2 — confirm sheet writes:**
- Run the full workflow manually
- Check all four tabs in the Google Sheet have data
- Keywords tab: should have up to 50 rows
- Pages tab: should have up to 25 rows
- History tab: one new row appended
- Flagged Items tab: rows only if movements detected (may be empty on first run)

**Test run 3 — confirm email and GitHub:**
- Check email arrived with subject "SEO Weekly Snapshot — week ending [date]"
- Check GitHub repo: memory/seo-current-data.md should be updated with current week's data
- Confirm the file is readable and the last_updated date is correct

**First run note:** On the first run, previous week comparison data does not exist in the system yet. Change columns will show 'N/A' or 'first run' — this is expected. Week-on-week comparison will be available from the second run onwards.

---

## Step 8 — Activate the schedule trigger

Only after all three test runs pass:
1. Toggle the workflow to Active in N8N
2. The Monday 7am trigger is now live
3. Log the activation date in decisions.md

---

## What runs automatically after setup

Every Monday at 7am (UTC):
1. Pulls last 7 days of keyword data from Search Console
2. Pulls last 7 days of page data from Search Console
3. Pulls previous 7 days for comparison
4. Calculates week-on-week changes and applies flags (IMPROVED, DROPPED, LOW CTR, PAGE 1 ENTRY/EXIT)
5. Overwrites This Week Keywords and This Week Pages tabs
6. Appends one row to Weekly History
7. Appends any flagged movements to Flagged Items
8. Sends summary email to Hadi
9. Updates memory/seo-current-data.md in the GitHub repo

---

## Error handling

If any API call fails, N8N logs the error in the execution history. Check:
N8N > Executions > [failed run] > View details

Common failures:
- 401 from Google: OAuth token expired — reconnect credential in N8N
- 403 from Sheets: Sheet ID wrong or account doesn't have edit access
- 404 from GitHub on GET: normal on first run — the file doesn't exist yet, PUT will create it
- 422 from GitHub on PUT: SHA mismatch — this means the file was edited manually; delete memory/seo-current-data.md from GitHub and let the pipeline recreate it

---

## Success criteria checklist

- [ ] Credential ID replaced in workflow JSON (GOOGLE_OAUTH2_CREDENTIAL_ID)
- [ ] Gmail credential ID replaced (GMAIL_CREDENTIAL_ID)
- [ ] Email address replaced (YOUR_HADI_EMAIL)
- [ ] Sheet ID replaced in all 8 places (YOUR_SEO_SHEET_ID)
- [ ] GitHub token replaced in 2 places (YOUR_GITHUB_TOKEN)
- [ ] Four sheet tabs created with correct names and headers
- [ ] Test run 1 passed — Search Console data returned
- [ ] Test run 2 passed — all four sheet tabs written correctly
- [ ] Test run 3 passed — email received, seo-current-data.md updated in repo
- [ ] Schedule trigger activated
- [ ] Activation logged in decisions.md
