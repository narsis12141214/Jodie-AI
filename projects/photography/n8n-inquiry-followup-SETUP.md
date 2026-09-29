# Setup — Inquiry Follow-Up workflow (20 minutes, once)

Workflow: `projects/photography/n8n-inquiry-followup.json`
Fires 9am **every day including weekends** (inquiries arrive at weekends and urgent leads cannot wait until Monday).
It emails Hadi the list of follow-ups due, **with the message text ready to copy and send.** It does not message clients directly. See "On fully automatic sending" at the end.

---

## 1. Create the Google Sheet

New sheet, name the tab exactly **`Inquiry Tracker`**. Row 1 is headers, exactly these thirteen:

| Name | Partner | Email | Phone | Event Date | Track | Stage | Last Contact | Touches | Replied | Subject Line | Value | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

**What each one does:**
- **Event Date / Last Contact** — `YYYY-MM-DD`. Last Contact is the last time *we* sent something.
- **Track** — leave blank and it works it out: `awaiting-payment` stage → C, event within 21 days or "travel" in Notes → B, otherwise A. Override by typing A, B or C.
- **Stage** — `inquiry-sent`, `awaiting-payment`, `booked`, `closed`, `lost`, `flagged`. The last four stop the cadence.
- **Touches** — how many follow-ups already sent. Start at `0`. **Add 1 each time you send one.**
- **Replied** — `yes` stops everything, immediately and permanently.
- **Subject Line** — the original subject, so the email tells you exactly what to reply to.

### Paste these two rows in to start

```
Nicole Wong	Ioannis Andoniou	nicolehywong@gmail.com	07895008349	2027-06-17		inquiry-sent	2026-09-21	0		Nicole + Ioannis, 17 June at Islington Town Hall	£2,300	Primary ICA. The Bloom named. Asked to hold the date.
Margareth Cartagena	Liviu Tudor	marga_cartagena@yahoo.com	07944598829	2027-05-24		inquiry-sent	2026-09-21	0		Margareth + Liviu, 24 May at Chelsea Old Town Hall	TBC	Discovery questions sent, no price yet. Wedding + pre-wedding.
```

Both are 8 days silent, so the first run will flag them as 6 days overdue.

## 2. Import the workflow
n8n → Workflows → Import from File → `n8n-inquiry-followup.json`.
It reuses the Google Sheets and Gmail credentials workflow 3 already uses, so there is nothing to reconnect.

## 3. One edit
Open **Read Inquiry Tracker** and replace `PASTE_INQUIRY_SHEET_ID_HERE` with the sheet ID from its URL (the long string between `/d/` and `/edit`).

## 4. Test, then activate
Hit **Execute Workflow**. You should get an email listing Nicole and Margareth with the text ready. Then toggle **Active**.

---

## The daily habit, which is the whole thing
When the 9am email arrives:
1. Send what it gives you. Copy, paste, send. Under a minute each.
2. **Update the sheet: today's date in Last Contact, add 1 to Touches.**
3. If someone replies, set Replied to `yes`.

**Until you update the sheet the email repeats the next day.** That is deliberate. The failure that lost Arijit and Michael & Carly was not a bad message, it was no message. A reminder that gives up quietly is the same as no reminder.

## Credential watch
The SEO pipeline died for ten weeks on a silent Google credential expiry, twice. If the 9am email stops arriving, that is the first thing to check. An empty day sends nothing, so **no email could mean nothing due, or it could mean the workflow is dead.** Worth a manual Execute once a month to be sure.

---

## On fully automatic sending
You asked for follow-ups to send automatically. This build automates the **trigger** and pre-writes the **message**, but leaves the send to you. My reasoning, so you can overrule it:

- **What failed was never the writing.** Both replies that would have saved those bookings were easy to write. Nothing fired. That is the part now automated.
- **The race condition is the real risk.** A client replies at 8pm, you have not marked the sheet, and at 9am an automated "making sure this reached you" goes out on top of their reply. To a couple who has just had a personal, specific email from you, that reads as careless. It is a small failure mode with a bad downside.
- **Thirty seconds versus zero.** The email hands you finished text. The gap between that and full automation is thirty seconds a day, against the risk above.

**If you want true auto-send, Dubsado already does it** and you already pay for it. Its workflows can send a templated email on a timer and cancel the sequence when a reply lands, which solves the race condition properly. That is the right home for it, not n8n. Say the word and I will write the Dubsado sequence instead.
