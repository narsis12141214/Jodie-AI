# Skool Playbook — Click AI Agency Outreach Strategy

**Source:** Consolidated from AI Automation Society Plus (Skool community) materials by Nate Herk, Suvam Khadka, and the AIS+ team.
**Purpose:** Canonical strategic reference for all Click AI Agency outreach decisions. Every JD agent involved in outreach — Strategist, Campaign Builder, Copywriter, Closer, Reply Classifier — consults this document as the authoritative source of truth.
**Last updated:** 21 April 2026
**Owner:** Hadi Yazdani

---

## How agents use this document

This playbook is strategy, not copy. For actual message templates, see `message-library.md`.

Decision hierarchy when handling any outreach task:

1. **Check this playbook first** for the relevant principle, framework, or diagnostic.
2. **Then check `message-library.md`** for the matching template.
3. **Apply segment-specific adaptations** from the Click AI Agency section (Section 11).
4. **Pass through Golden Rules checklist** before returning output.

If any instruction in this playbook conflicts with a downstream agent prompt, this playbook wins. If the user (Hadi) explicitly overrides a playbook principle in a given conversation, log the override and ask for confirmation before propagating it into future work.

---

## 1. The foundation: why this playbook exists

Click AI Agency ran ~100 cold emails between 13-18 April 2026 and generated a single positive reply, approximately 1% positive reply rate. The Skool playbook's reply rate diagnostic table (Section 6 of this doc) classifies this as a "deliverability or lead list issue" rather than a copy problem, but post-mortem analysis revealed problems at all three layers:

- **Infrastructure:** sending from the main business domain without warmup, no tracking, manual sends from Gmail
- **Targeting:** gatekeeper inboxes (info@, hello@, contact@) rather than decision-makers
- **Copy:** templated openers, no risk reversal, vague CTAs, subject lines that screened as marketing

This playbook exists to prevent those failure modes from recurring. Every principle below was either earned through Skool community case studies (most notably Suvam Khadka's $500k in <6 months case study) or established as a counter-response to documented Click AI Agency campaign failures.

---

## 2. Core mindset principles

### Sell first, build later

Do not build elaborate systems before validating market demand. Offer outcomes you know you can deliver, use outreach as direct market feedback, and build only after someone commits.

**Click AI Agency application:** We already have Arman (Rendezvous restaurant receptionist) and Kailee (aesthetics voice receptionist) as live builds. Any outreach must reference these as proof, not promise custom builds before a prospect has engaged meaningfully.

### You're consulting, not selling

Outreach is starting conversations, not closing deals. The goal of every first message is a reply, not a sale.

**Click AI Agency application:** Copywriter should never write emails that attempt to close. Closer agent handles the conversation flow from positive reply onwards, following the Conversation Roadmap (Section 8).

### Zero-risk offer framing

Every offer must include three components:

- **Outcome** — what they get (specific, measurable)
- **Timeframe** — when they'll see results
- **Risk reversal** — what happens if we fail

Example: "We'll handle your DM enquiries and table bookings for 30 days free. If it doesn't save your team at least 10 hours a week, you don't pay."

**Click AI Agency application:** Every outreach campaign must have a zero-risk offer defined before launch. Strategist owns this. Copywriter references it in the message body.

### Data is a compass

Positive signals (replies, meetings, closed deals) mean keep going in that direction. Negative signals (silence, uninterested replies) mean pivot. Track every positive responder's attributes — company size, industry, what resonated — and use the pattern to refine future lead lists. This is how reply rates climb from 3% to 5% to 8% to 10%+.

**Click AI Agency application:** Outreach tracker sheet must include a "positive responder attributes" section. Strategist reviews this monthly to refine segment definitions.

### Expect harsh results

Cold outreach is rough. Insults and hostile replies are normal even in high-performing campaigns. Do not interpret hostile replies as a signal to change the system. Interpret low reply rates and silence as signals.

---

## 3. Infrastructure foundations

### Domain strategy

- Never use the main business domain for cold outreach
- Use a clean secondary .com domain (avoid .xyz, .io, hyphens, numbers)
- Forward the outreach domain to the main website for trust signal
- Maximum 2 email accounts per domain
- Maximum 50 emails/day per domain (30 cold + 20 warmup)

**Click AI Agency state:** Main domain `clickaiagency.com`. Outreach domain `getclickagency.com` registered via Cloudflare, forwarded via 301 redirect. Two inboxes live: `hadi@getclickagency.com` (founder persona, Super Admin) and `zizi@getclickagency.com` (outreach operator persona).

### Email authentication stack

All four records must be configured before sending begins:

- **MX:** routes inbound mail
- **SPF:** authorises Google to send on domain's behalf (`v=spf1 include:_spf.google.com ~all`)
- **DKIM:** cryptographic signature, 2048-bit key, selector `google`
- **DMARC:** policy record. Start at `p=none` (monitoring), tighten to `p=quarantine` after 2-3 weeks of clean sending, eventually `p=reject`

**Click AI Agency state:** All four records live and verified. Mail-tester scores 10/10 on both inboxes as of 21 April 2026.

### Warmup is non-negotiable

- 16-day initial warmup before any real cold send
- Ramp from 3 emails/day to 50 emails/day
- Maintain 20-30 warmup emails/day indefinitely after launch
- Use a dedicated warmup service (Instantly, Smartlead, Mailreach) — never manual

**Click AI Agency state:** Instantly selected as sending/warmup platform. Warmup to begin upon account setup. No real cold sends from `getclickagency.com` until day 17 at earliest.

### Sending limits

- Maximum 30 cold emails per inbox per day
- Start at 10/day and ramp to 30 over 2 weeks
- Send consistently across business hours, never in bursts
- Rotate between inboxes for natural traffic patterns

---

## 4. Messaging frameworks

The playbook specifies two core frameworks depending on whether the contact is warm or cold.

### ACA framework (warm outreach)

For past colleagues, existing clients, prior conversations, or introductions:

- **A**cknowledge something specific and recent about them
- **C**ompliment genuinely, tied to a real achievement
- **A**sk a simple, relevant question

### 4T's framework (cold outreach)

For prospects with no prior relationship:

- **T**rigger — crisp observation or change event (hiring, expansion, funding, award, press feature)
- **T**hink — question that reframes the status quo
- **T**hird-party — brief social proof or peer pattern
- **T**alk? — light, low-friction ask ("worth a look?")

**Copywriter instruction:** Every first-touch cold email must structurally follow 4T's. Every warm-touch email must structurally follow ACA. No other frameworks are permitted without Strategist approval.

### Offer vs value proposition (they are different)

- **Offer:** what they get right now (e.g., "free 15-minute audit")
- **Value proposition:** the outcome they'll achieve (e.g., "cut first-response time by 30% in 30 days")

Emails should lead with the concrete offer and tie it to a believable outcome. Generic benefit language ("reduce manual workload") without a specific outcome and timeframe does not meet this bar.

---

## 5. Subject line strategy

Subject lines must sound like internal team communication or a curious question, never like a sales pitch or marketing email.

### Patterns that work

- `[FirstName], q: is [Company] taking on more clients?`
- `[FirstName], q from your neighbour`
- `2-min teardown for [Company]?`
- `specific trigger at [Company]` (e.g., `New site for Berenjak?`)
- `Quick question about [specific thing they do]`

### Patterns that don't work (retired from Click AI Agency use)

- `Bookings and Guests Follow-up` (generic, screens as marketing)
- `Follow-up Question` (deceptive when there's no prior conversation)
- `Business Enquiry` (bland, high spam signal)
- `A quick thought for [Name]` (weak, no curiosity hook)
- Anything with emoji, ALL CAPS, or exclamation marks in the subject

### Rules

- Curiosity or cliffhanger intent — make them need to open it
- Lower case unless grammatically required
- No "Follow-up" language for first-touch emails
- Never lie or imply prior contact that doesn't exist

---

## 6. Reply rate diagnostic table

Use this table to diagnose campaign performance at the 100+ email mark:

| Reply Rate | Diagnosis | Action |
|---|---|---|
| Below 2% | Lead list or deliverability issue | Check spam folder delivery. Verify list quality. Re-run mail-tester. Check warmup status. |
| 2%-5% | Copy or offer issue | Emails are landing but not compelling. Sharpen offer, add risk reversal, improve personalisation. |
| 5%-10% | Golden zone | Sufficient for meaningful pipeline. Scale volume. |
| Above 10% | Excellent | Keep optimising but don't change what's working. Document what you did. |

**The math:** At 60 cold emails/day across both inboxes, 5 days/week, we send ~1,200/month. At 5% reply rate = 60 replies. If half are positive = 30 positive replies. At 50% of positive replies booking a call = 15 discovery calls/month. At 40% close rate on calls = 6 closed deals/month.

This projection is what the 60-day sprint goals are calibrated against. If reply rate drops below 5% consistently, the system is broken and must be diagnosed before scaling.

---

## 7. Personalisation tiers

Not all personalisation is equal. The playbook ranks four tiers:

| Tier | Example | Effort | Impact |
|---|---|---|---|
| Basic | Name, role, company | Automated | Low — every cold email has this |
| Segmented | Industry, size, tool stack | Low | Medium — helps relevance |
| Situational | Recent hire, funding, launch, new location | Medium | High — shows timing |
| Micro-specific | Line from their post, podcast quote, review language | High | Highest — proves genuine research |

**Rule of thumb:** 30-60 seconds per contact is enough to find one true detail. One sharp micro-specific detail beats five fluffy segmented details.

**Click AI Agency application:** Every email generated by Copywriter must contain at minimum one Situational or Micro-specific detail. If the Lead Engine's output lacks this, either a Research agent step is inserted or Zizi manually adds research notes before Copywriter runs.

---

## 8. The Conversation Roadmap (post-reply flow)

When a prospect replies, Closer agent guides them through this five-step flow:

### Step 1: Reply Received
- Acknowledge their reply
- Add immediate value (don't just say "great, let me send more info")
- Match their energy and length

### Step 2: Qualify Interest
- Ask 1-2 soft, conversational questions to determine fit
- "How are you handling [pain point] right now?"
- "What tools are you currently using for [process]?"
- "Is [outcome] something you're focused on this quarter?"

### Step 3: Bridge to Call
- Frame the call as helpful, not as a pitch
- 15-20 minutes maximum
- "Happy to share quick wins I've seen in your space — want to jump on a 15-min call?"
- "Easier to explain with a quick screen share — want me to send over a Calendly link?"

### Step 4: Discovery Call
- Human (Hadi) handles this, not JD
- Learn challenges deeply before proposing anything
- Listen more than talk

### Step 5: Convert to Client
- Propose the smallest commitment that delivers genuine value
- Tiered options: paid audit (£100-500) — small project (£500-2,000) — full build (£2,000+)
- "Based on what we discussed, I think we could start with [small project/audit]. You get immediate value without a big commitment."

---

## 9. Objection handling

Most objections are buying signals in disguise. The playbook's core objection responses:

### "We don't have budget."
"Totally understand. Most of my clients started with a small pilot build to prove ROI first. Would it help if I shared what that looked like?"

### "We already have a tool for that."
"Makes sense — most teams do. The way we fit in is by connecting those tools so they work together. Want me to show you an example?"

### "Not right now."
"No worries at all. Would it be helpful if I checked back in next quarter? In the meantime, happy to send you a 2-min breakdown so you've got it for later."

### Key principles across all objections
- Acknowledge their concern
- Offer a low-friction alternative
- Keep the door open for future contact
- Never push back defensively

---

## 10. Follow-up cadence

- Cold prospects: 2-3 follow-ups maximum, spaced 2-5 days apart
- Each follow-up must add new value, not just "bumping this up"
- Warm prospects: continue until clear yes/no, 2-3 day spacing while active
- Nurture (long-term): 1 relevant insight per month, congratulate wins, share helpful artifacts

**Breakup email structure:** After 2-3 unanswered attempts, send a permission close that keeps the door open. "Happy to close the loop if now's not the right time. If [outcome] becomes a priority, I can share what's working. Check back next quarter?"

---

## 11. Click AI Agency segment-specific strategy

### Segment 1 (Priority): Persian/Iranian restaurants in London

**Why this segment first:**
- Strongest defensible angle — founder Iranian-to-Iranian connection, genuine, uncopiable
- Finite walkable market, hand-researchable in batches of 50
- Live case study available (Arman at Rendezvous)
- Pre-existing positive sentiment from earlier outreach attempts (Berenjak, Naroon warm)

**Target prospects:** Owners, founders, or general managers. Never info@/hello@/contact@.

**Geographic focus:** London initially. Prioritise established independents and small groups over chains.

**Offer:** 30-day free pilot. Full DM/booking/enquiry handling via voice receptionist (same stack as Arman). Zero risk — if it doesn't save 10+ hours/week, they don't pay.

**Sender:** `hadi@` for first-touch (Iranian-to-Iranian angle requires founder voice). `zizi@` for follow-ups.

**Volume target:** 50 prospects in the first campaign batch.

### Segment 2: High-end London restaurants/shisha lounges (non-Persian)

**Strongest angle:** Missed bookings, late-night DMs, social content inconsistency.

**Target prospects:** Owners or GMs. Premium venues (Mayfair, Soho, Chelsea, Knightsbridge, Notting Hill). Shisha lounges specifically — existing vocabulary fit with previous outreach.

**Offer:** Same 30-day free pilot structure.

**Sender:** `zizi@` primary. `hadi@` for warm follow-ups on interested replies.

**Volume target:** 100 prospects, launched after Segment 1 campaign has 2 weeks of data.

### Segment 3: Aesthetics clinics (Harley Street, Mayfair, Knightsbridge, Pall Mall)

**Strongest angle:** Bespoke luxury experience preservation. Framing must be "supports, not disrupts."

**Language register:** Professional medical tone. Explicitly differentiate from "stupid robots that fire back booking links."

**Target prospects:** Practice managers and clinic owners. Doctors are typically not the right first contact (they don't manage operations).

**Offer:** Same 30-day free pilot structure, adapted for consultation bookings and patient enquiry management.

**Sender:** `zizi@` primary. `hadi@` for interested replies at Director-level.

**Reference proof:** Kailee (live aesthetics voice receptionist).

**Volume target:** 100 prospects, launched in parallel with Segment 2.

---

## 12. Banned phrases and failed patterns

Based on analysis of Click AI Agency's pre-rebuild outreach (13-18 April 2026, ~100 emails, ~1% positive reply rate), the following phrases and patterns must not appear in any Copywriter output:

### Banned opener patterns
- "I've been following [Company] and honestly, it's my go to place for..."
- "As your regular customer..."
- "I hope this email finds you well"
- "I hope you are well"
- "I wanted to reach out because..."
- "Just circling back"
- "Quick thought for [Name]"

### Banned closing/CTA patterns
- "Revolutionise your business"
- "Would love to show you what we can do"
- "2-minute demo" as a standalone CTA (permitted only when referencing a specific pre-recorded universal demo asset that currently exists)
- "No problem at all" (passive, weak)

### Banned subject line patterns
- `Follow-up Question` (deceptive on first touch)
- `Bookings and Guests Follow-up` (generic marketing feel)
- `Business Enquiry` (bland)
- Anything starting with emojis
- Anything with "Urgent" or "Important"

### Banned structural patterns
- Identical openers across multiple prospects in the same segment
- "As your regular customer" claim to more than one business in the same niche (credibility-destroying)
- Promising a custom demo without confirmation it exists
- Emailing competing venues the same week with similar language (owners compare notes)

---

## 13. Golden Rules — pre-send checklist

Every email must pass all seven before being queued for Zizi's review:

1. **One clear objective** and one simple CTA — what do we want from this touch?
2. **3-6 sentences**, plain text, mobile-friendly
3. **One true research-derived detail** that proves homework
4. **Offer is specific and low-friction** — video, mini-audit, or snippet they can consume
5. **No banned phrases or patterns** from Section 12
6. **Follow-ups scheduled** with fresh value adds, not "just bumping"
7. **Tracking enabled** — the send is logged with sender, timestamp, segment, sequence step

If any check fails, Copywriter flags the draft for revision rather than passing to review queue.

---

## 14. Success criteria — rebuild validation

The rebuild (post-16-day warmup, from day 17 onwards) is validated against these 30-day metrics:

| Metric | Target | Current baseline | Diagnostic if missed |
|---|---|---|---|
| Reply rate | 5%+ | ~3.7% (pre-rebuild) | Copy or offer issue |
| Positive reply rate | 2%+ | ~1% (pre-rebuild) | Targeting or personalisation issue |
| Bounce rate | <2% | Unknown (pre-rebuild) | Lead list quality issue |
| Discovery calls/week | 2-3 | 0 | Bridge-to-call step failing |
| Paid pilots or zero-risk offers accepted | 1+ | 0 | Offer not compelling or wrong segment |

If 30-day metrics miss these targets, do not scale volume. Diagnose using the reply rate table (Section 6), fix the specific failure, validate with a fresh batch of 50, then scale.

---

## 15. Operational architecture

### Pipeline

```
Lead Engine (Google scraping — enriched prospect data with direct emails)
  |
Google Sheet: prospect data + research notes + one sharp detail
  |
Outreach Copywriter agent: generates email draft per row
  referencing this playbook + message-library.md templates
  |
Google Sheet: drafts added to new column
  |
Zizi review: approves, edits, or rejects drafts
  |
Instantly: sends approved drafts via warmed-up inboxes
  rotates between hadi@ and zizi@ for natural traffic
  |
Instantly webhook — n8n — Reply Classifier agent (Haiku)
  tags: positive / objection / not-now / unsubscribe / referral / bounce
  |
Positive replies — Closer agent (Opus) drafts next-step response
  following Conversation Roadmap (Section 8)
  |
All interactions logged to tracker sheet with positive responder attributes
  |
Weekly: Outreach Strategist reviews tracker, refines segment definitions
```

### Agent roster

| Agent | Model | Responsibility |
|---|---|---|
| Outreach Strategist | Opus | Campaign planning, segment selection, offer design, sequence approval |
| Campaign Builder | Sonnet | Selects templates from library, matches to segment, briefs Copywriter |
| Outreach Copywriter | Sonnet | Generates per-prospect email drafts against playbook + library |
| Reply Classifier | Haiku | Tags incoming replies by intent category |
| Closer | Opus | Handles positive reply conversation flow, follows Conversation Roadmap |

### File references

- This file: `outreach/skool-playbook.md`
- Template library: `outreach/message-library.md`
- Agent prompts: `agency/outreach.md`, `shared/closer.md`, etc.

---

## 16. Change log

- **21 April 2026:** Initial version created by Hadi + Claude. Based on six Skool community documents and post-mortem of 13-18 April 2026 outreach campaign.

---

*End of playbook. For message templates, see `message-library.md`.*
