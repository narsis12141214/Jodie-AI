# Instantly Infrastructure — Click AI Agency

**Status:** Live, warmup active as of 22 April 2026
**Purpose:** Context annex documenting the sending infrastructure layer. Does not change agent architecture or canonical files.

---

## Two outreach inboxes

### hadi@getclickagency.com
- **Role:** Founder persona for higher-trust touches
- **Used for:** Persian restaurant first-touch (Template 1E), warm prospect follow-ups, founder escalations, closer moves
- **Admin role:** Super Admin on Google Workspace
- **Voice:** Warm, personal, slightly more formal. First-person singular ("I"), signs off "Best, Hadi"

### zizi@getclickagency.com
- **Role:** Outreach operator persona for cold reach-out and operational touches
- **Used for:** Non-Persian cold first-touch, soft reminders (2A), value drops (2B), breakup emails (2C), gatekeeper routing
- **Admin role:** Standard user (deliberate, outreach inboxes face higher compromise risk)
- **Voice:** Professional, concise, operational. Signs off "Zizi"
- **Note:** Zizi is a real human team member who reviews Copywriter drafts and may compose replies manually

---

## Instantly platform

- **Account owner:** hello@clickaiagency.com
- **Plan:** 14-day free trial, ending 6 May 2026
- **Plan decision pending:** Hypergrowth upgrade recommended before trial expiry
- **Connection method:** Google OAuth for both inboxes
- **API Keys:** accessible (Version 2), not yet generated
- **Webhooks:** accessible, not yet configured

---

## Sending configuration (both inboxes identical)

| Setting | Value |
|---|---|
| Daily cold send limit | 30 emails/day per inbox (60 total) |
| Spacing | 10-15 minute randomised gaps |
| Sending hours | 09:00-17:00 London time |
| Sending days | Monday-Friday only |
| Timezone | Europe/London |

---

## Warmup configuration (both inboxes identical)

| Setting | Value |
|---|---|
| Status | Active since 22 April 2026 |
| Starting volume | 3 emails/day |
| Daily increment | 1 email/day |
| Maximum cap | 40 emails/day |
| Reply rate | 30% |
| Weekdays only | Enabled |
| Read emulation, Open rate, Spam protection, Mark important | All maxed (100) |

---

## Warmup timeline

| Date | Milestone |
|---|---|
| 22 April 2026 | Warmup started (Day 1 of 16) |
| 6 May 2026 | Trial expires. Plan decision required before this date. |
| 8 May 2026 | Day 17. Warmup complete. First real cold sends authorised. |
| Post-launch | Warmup continues at 20-40 emails/day per inbox indefinitely. |

---

## What is NOT live yet

- No real cold sends until 8 May
- No campaigns loaded in Instantly
- No API key generated (deferred to n8n wiring)
- No webhook configured (Reply Classifier pipeline deferred to post-launch)
- Instantly plan decision pending before 6 May

---

## Agent implications

- **Outreach Copywriter:** Match sender persona voice (hadi@ vs zizi@) per prospect row
- **Campaign Builder:** Include sender persona in every campaign brief
- **Closer:** Match response persona to original sender. Handoff from zizi@ to hadi@ framed as "Let me loop in Hadi"
- **Reply Classifier:** No change, operates on content regardless of inbox
- **Outreach Strategist:** Total capacity 60 cold/day. Plan volumes against this ceiling.

---

*Last updated: 23 April 2026*
