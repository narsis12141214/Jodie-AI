# Workflow 2 — Opener Generation — Setup Instructions

## What it does

Runs every weekday at 9am (one hour after Workflow 1).
Reads the outreach tracker Google Sheet, finds every row with Status = "New Lead" and no message drafted yet, calls Claude API to generate a personalised Step 1 opener for each lead, writes the opener back to the "Message Sent" column, updates Status to "Opener Ready", then emails you a summary.

Zizi opens the sheet, reviews the openers, personalises if needed, and sends manually.

---

## Before you import

You need four things ready:

1. **Anthropic API key** — from console.anthropic.com
2. **Google Sheets credential** — already connected in N8N from Workflow 1 (reuse same credential)
3. **Gmail credential** — already connected in N8N from the SEO pipeline (reuse same credential)
4. **Your email address** — for the daily summary notification

---

## Import steps

1. Open N8N — n8n.srv1466538.hstgr.cloud
2. Create New Workflow
3. Click the three-dot menu — Import from File
4. Select `workflow-2-opener-generation.json`
5. Click Import

---

## After import — credentials to connect

**node-002 (Read Lead Sheet):**
- Click the node
- Under Credentials, select "Google Sheets Account" (same as Workflow 1)

**node-005 (Update Lead Row):**
- Same — select "Google Sheets Account"

**node-004 (Generate Opener via Claude):**
- Click the node
- In the Code, replace `YOUR_ANTHROPIC_API_KEY` with your real Anthropic API key
- The model is `claude-haiku-4-5-20251001` — cheapest Claude model, fine for opener generation
- Cost estimate: ~$0.001 per opener (less than a penny each)

**node-007 (Send Email to Hadi):**
- Click the node
- Under Credentials, select your Gmail account
- Replace `YOUR_EMAIL_ADDRESS` with your actual email

---

## Test before activating the schedule

1. Make sure at least one row in the sheet has Status = "New Lead" and Message Sent = empty
   - If there are none, manually add a test row or temporarily change an existing row's Status to "New Lead"
2. Open the workflow in N8N
3. Click "Test workflow" (NOT the schedule — just the test button)
4. Watch each node execute
5. Check the Google Sheet — the test row's "Message Sent" should now contain an opener and Status should say "Opener Ready"
6. Check your email — the summary notification should have arrived
7. If it worked: activate the schedule trigger toggle (top right of the workflow)

---

## If the test fails

**"Generate Opener via Claude" errors with 401:**
- Your Anthropic API key is wrong or expired. Double-check console.anthropic.com.

**"Update Lead Row" errors — no rows updated:**
- The Instagram Handle in the test row must exactly match what was written by Workflow 1 (including the @ symbol)
- Check that the column name in the sheet is exactly "Instagram Handle" (capital I, capital H)

**"Build Email Summary" runs but "Send Email to Hadi" errors:**
- The Gmail credential may need reauthorising. Go to Settings > Credentials > find Gmail > reconnect.

**No items reach "Generate Opener via Claude":**
- Check that your test row has Status = "New Lead" (exact spelling, capital N and L)
- Check that Message Sent is completely empty (no spaces)

---

## How the opener is generated

Claude receives the lead's business name, industry type, location, and Instagram bio (the "Notes" column). It generates an opener following the Step 1 formula from the outreach playbook:

> "Hey [Business Name] - saw [something specific from their bio]. [One genuine observation]. Would this be the best place to ask you a quick question?"

If the bio contains no useful specific detail, Claude outputs `REVIEW NEEDED - add profile detail before sending` instead of a generic opener. Zizi sees this flag in the sheet and the email, and handles those manually.

---

## What Zizi does after the workflow runs

1. Open the Google Sheet
2. Filter by Status = "Opener Ready"
3. Review each opener in "Message Sent" — edit if anything sounds off or generic
4. Open Instagram, find the account, send the DM manually
5. After sending: update Status to "Sent", add today's date to "First Contact Date"
6. Flag any interesting replies to Hadi immediately

---

## Schedule

- Workflow 1 runs: 8am weekdays (scrapes leads, fills sheet)
- Workflow 2 runs: 9am weekdays (generates openers for new leads)
- One hour gap ensures Workflow 1 has finished before Workflow 2 reads the sheet

If Workflow 1 runs late or adds leads at other times during the day, those leads will be picked up the following morning at 9am.
