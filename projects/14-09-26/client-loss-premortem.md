# Client-loss pre-mortem — where else can we lose someone?
**Date:** 14 September 2026
**Asked by Hadi:** "I wonder what else is missing that we haven't come across yet and it could cost us another client. I need you to figure this out."
**Method:** Walked the full client lifecycle for both businesses, stage by stage, and asked at each one: where has a client been lost or nearly lost, what does the record show, and what structural gap let it happen. Every gap below is grounded in the session log, quality log, priorities file or a file check run tonight. Nothing is speculative; where a gap is inferred rather than observed, it says so.
**Scope:** Both businesses. Internal document.

---

## The pattern behind the losses so far

Five deals lost or nearly lost since May. Different symptoms, one shape:

| Deal | What happened | Stage | Root |
|---|---|---|---|
| Kish (May) | Adobe e-sign friction, deal switched off for two weeks | Close | No close mechanism in the room |
| Hanna (May) | Discount terms inferred into the email, caught pre-send | Proposal | Drafting from defaults, not confirmed terms |
| LaMure (Aug) | Verbal yes, no deposit ask, lost to a competitor | Close | Gap between yes and paperwork |
| Michael & Carly (Sept) | Invented crowd conditions at Tower Bridge, caught pre-send | Proposal | Asserting what we do not know |
| Implant + Perio (Sept) | Cold-lead proposal to a warm referral, volume framing, capitulating apology | Discovery + Proposal + Close | No lead-source read, no discovery debrief, no read-before-reply |

**Every one of them is a handoff failure.** Information existed (in the room, in the prep doc, in a file) and did not make it to the point of decision. The fixes below are mostly about making handoffs structural instead of relying on memory.

---

## Stage 1 — Inbound: losing people before we know they exist

### 1.1 The website form goes to spam. Open since 12 August.
**Evidence:** Steva's inquiry landed in Gmail spam. She reached out a second time by direct email or a £2,300 booking would never have existed. Flagged 12 Aug. Still listed as an open carry-forward on 14 Sept (33 days).
**How it costs a client:** Silently. Every inquiry that goes to spam and does not retry is a client we never knew we lost. This is the only gap on this list that is losing clients right now, invisibly, and we cannot count them.
**Fix:** 15 minutes. Check spam for the last 60 days. Safelist the form sender. Add a filter that stars and labels form submissions. Then a monthly spam check on the calendar.
**Owner:** Hadi. **Effort:** 15 min. **Priority: 1.**

### 1.2 No response-time standard on inquiries.
**Evidence:** File check tonight: no SLA stated anywhere in the agents or admin rules.
**How it costs a client:** Photography inquiries are comparison-shopped. The first warm, specific reply usually wins. Steva, Selina and Michael were all answered fast because Hadi happened to be at his desk. Nothing guarantees that.
**Fix:** Written standard: same business day, under 4 hours where possible. If Hadi is shooting, an auto-acknowledgement with a real time promise ("I am photographing today and will reply properly this evening").
**Owner:** Jodie writes it, Hadi sets up the auto-reply. **Effort:** 20 min.

---

## Stage 2 — Discovery: the meeting, and what comes out of it

### 2.1 No post-meeting debrief. This is the biggest gap on the list.
**Evidence:** File check: no debrief template exists anywhere. Hadi briefs me verbally after meetings. The Implant + Perio brief said "they love that idea." Her reply said the opposite. Elan's second business partner was unknown to us for weeks. Implant + Perio has two principals and a practice manager; we do not know who decides.
**How it costs a client:** Everything downstream is built on the brief. A lossy brief produces a wrong proposal, and a wrong proposal to a warm referral is a lost referral. This is exactly what happened.
**Fix:** A 5-minute structured debrief, voice note or typed, straight after every meeting, before anything is drafted:
1. How did this lead reach us? (source, who referred, how warm)
2. What did they say they want? **Their words, not my summary.**
3. What did I propose in the room, and what was their reaction? **Their words.**
4. What constraints did they state? (budget, time, camera, staff, existing supplier)
5. Who else decides, and have I met them?
6. What did we agree happens next, by when?
7. My confidence they will buy, 1 to 5, and why.
Jodie drafts from the debrief, not from memory. Where the debrief and the draft disagree, the debrief wins.
**Owner:** Jodie builds the template tonight. Hadi uses it after every meeting. **Effort:** 5 min per meeting. **Priority: 2.**

### 2.2 No decision-maker map.
**Evidence:** Elan: partner unknown for weeks, then a partner meeting became the real close. Implant + Perio: proposal addressed to Dr Tehrani; Dr Negahban and the practice manager (there since 2011, with a finance manager since 2013) are unaccounted for.
**How it costs a client:** We close the person in the room and the person not in the room says no.
**Fix:** Question 5 of the debrief. For any deal over £1,000/month, the proposal is not sent until the decision-maker map is known.
**Owner:** Hadi. **Effort:** part of the debrief.

---

## Stage 3 — Proposal: the document

### 3.1 The proposal carries no close mechanism.
**Evidence:** Elan proposal (July): no signature page, no payment link, "reply to proceed." Implant + Perio (Sept): "we send the agreement the same day." Every proposal so far has required a second document and a second round to become money.
**How it costs a client:** The 19 Aug rule says pair the yes with the paperwork. But if the proposal itself has no paperwork in it, the yes and the signature are still two events, and LaMure lived in that gap.
**Fix:** Every proposal ships with its agreement page and a payment link inside the same PDF. "To proceed, sign page 6 and pay the first invoice here." One document, one action. For in-person: iPad with the same page pre-loaded (12 May protocol).
**Owner:** Jodie adds an agreement page to the proposal generator template. **Effort:** 1 hour once, then automatic. **Priority: 3.**

### 3.2 Volume framing as the default for content offers.
**Evidence:** Implant + Perio. Quality log 14 Sept. Rule now added: volume is a positioning decision, not a default.
**Status:** Fixed today. Listed for completeness.

### 3.3 Canonical pricing drift.
**Evidence:** "Grace collection" used with Selina since 23 Aug. File check tonight: zero mentions in shared/presence-method-packages.md. The homepage carried retired package names for four weeks in May before anyone noticed.
**How it costs a client:** I draft from the canonical file. If Hadi quotes something not in it, the next document contradicts the last conversation. Clients notice inconsistent numbers and read it as either disorganisation or a hidden markup.
**Fix:** Hadi gives me the Grace collection details (what it is, price, what it includes). 10 minutes. Then a standing rule: any new collection or package name is added to the canonical file the same day it is first used with a client.
**Owner:** Hadi (10 min brief), Jodie (file). **Effort:** 10 min.

### 3.4 Objection library is two objections behind.
**Evidence:** File check: shared/objections.md has no entry for "we don't want to be influencers / Instagram as a second job" (Implant + Perio) and no entry for SevenRooms/OpenTable (5+ restaurants lost on it since June, Zizi one-pager never built).
**How it costs a client:** The same objection lands twice and we improvise twice. The SevenRooms one has already cost five prospects.
**Fix:** Jodie writes both entries tonight from what we now know.
**Owner:** Jodie. **Effort:** 30 min.

---

## Stage 4 — Close: yes to signed to paid

### 4.1 Two live LaMure-pattern exposures, right now.
**Evidence:**
- **Chic Salon & Clinic:** contract drafted 14 Aug, work delivered, £400 paid, signature status "unconfirmed" for 31 days.
- **Monsieur:** terms agreed 14 Aug (£340/mo + £350 website + 1-month trial), contract never drafted, 31 days.
**How it costs a client:** LaMure was lost in the gap between agreement and paper. These are the same gap, open for a month each. Monsieur is the cheapest revenue available and it is unsecured.
**Fix:** Chic: confirm signature this week, or send it again with a one-line note. Monsieur: I draft the contract tomorrow morning on your go-ahead, you send it same day.
**Owner:** Hadi (Chic check, Monsieur send), Jodie (Monsieur draft). **Effort:** 30 min. **Priority: 4.**

### 4.2 Follow-up cadence exists on paper and not in practice.
**Evidence:** Michael & Carly: day-3 nudge 7 Sept, day-5 phone trigger, day-7 11 Sept, day-10 today. File check: no call logged. They travel from Orlando on fixed dates; the 23rd is nine days away. Elan sat ~3 weeks with no touch from us in August. John & Oksana 21 days past the close-out date.
**How it costs a client:** A cadence that is not enforced is a wish. Michael & Carly may already be gone.
**Fix:** Two parts. (a) Cadence dates go into the morning brief as **named actions with a phone number**, not as a table row. (b) If a cadence action is missed two days running, I say so at the top of the brief, not in a list.
**Owner:** Jodie. **Effort:** process change, tomorrow.

---

## Stage 5 — Delivery: losing the clients we already have

### 5.1 Week-2 and week-3 check-ins were locked in May and never logged as done.
**Evidence:** Decision 21 May: "Week 2 + week 3 satisfaction check-ins locked as standard process for any month-1 client." File check tonight: not one instance logged as executed for Haleh, Kish, Galleria or Chic.
**How it costs a client:** A paying client who has a problem and no scheduled moment to raise it does not complain. They cancel. Four paid clients, zero recorded check-ins.
**Fix:** One message to each of the four this week: "Two things: what is working, what is not?" Then check-ins at week 2, week 3, month 3 and quarterly go into the diary for every client, and into the morning brief as named actions.
**Owner:** Hadi sends, Jodie drafts and diarises. **Effort:** 20 min. **Priority: 5.**

### 5.2 Credentials die silently and take deliverables with them.
**Evidence:** GSC pipeline dead ~10 weeks before anyone noticed (Aug). n8n Google credential died twice. Perplexity `.env` gone. Content Studio credentials unverified since May. Three casualties in one summer, all discovered by accident.
**How it costs a client:** If Haleh's or Chic's content depends on an n8n workflow and its credential expires, content stops and the first person to notice is the client.
**Fix:** A Monday-morning health check: does each client-facing workflow have a successful run in the last 7 days? Yes or no, in the brief. Ten minutes to build, zero minutes to run.
**Owner:** Jodie. **Effort:** 30 min once.

### 5.3 The review ask has been "diarised" for a month and never sent.
**Evidence:** "Post-delivery review asks (GBP velocity restart, Selina first)" appears in priorities on 25 Aug, 27 Aug, 5 Sept, 12 Sept, 14 Sept. File check: no review ask ever logged as sent. Mozhgan (22 May) and Steva (repeat client) are also un-asked.
**How it costs a client:** Not directly. It costs the next client. GBP reviews are 20% of map-pack weight, the pack takes 42-44% of local clicks, and this is the highest-leverage SEO action available. Every delivered session that passes without a review ask is a compounding loss.
**Fix:** The review ask goes into the delivery email as a standard paragraph, not as a separate diarised task that never fires. Selina's final gallery email is the first one.
**Owner:** Jodie writes the paragraph into the delivery template. **Effort:** 15 min.

---

## Stage 6 — Referral: the channel we are not working

### 6.1 The best leads are referrals and there is no referral ask.
**Evidence:** Kish came through the community. Implant + Perio came from a friend you both trust. Steva is a repeat client. me.md, 30 March: "Warm contacts convert far better than cold outreach." Cold email has produced zero substantive replies in four months. File check: no referral ask exists in any delivery flow, contract, or check-in script.
**How it costs a client:** This one is about the clients we never meet. Every happy client who is not asked "who else should I be talking to" is a referral that did not happen.
**Fix:** One sentence in every check-in and every delivery email. Not a scheme, not a discount. Just the question.
**Owner:** Jodie writes it into the templates. **Effort:** 10 min.

---

## If you only do five things

| # | Action | Why first | Time |
|---|---|---|---|
| **1** | **Fix the spam filter** | The only gap losing clients right now, invisibly, and open for 33 days | 15 min |
| **2** | **Use the post-meeting debrief** (Jodie builds tonight) | Would have caught Implant + Perio at the source | 5 min per meeting |
| **3** | **Agreement page + payment link inside every proposal** (Jodie builds) | Closes the LaMure gap structurally instead of by discipline | 1 hr once |
| **4** | **Chic signature confirmed, Monsieur contract sent** | Two LaMure-pattern exposures, 31 days each | 30 min |
| **5** | **Check-in message to all four paid clients this week** | Zero recorded check-ins on four paying clients | 20 min |

Plus one phone call that is not a process fix: **Michael & Carly, +1 407 405 4389, tomorrow.** Day 11.

---

## What Jodie is building tonight, without waiting
- Post-meeting debrief template → `.claude/templates/post-meeting-debrief.md`
- Two objection entries (influencer / second job; SevenRooms / OpenTable) → `shared/objections.md`
- Review ask + referral ask paragraphs → delivery email template

## What needs Hadi
Spam filter (15 min). Grace collection details (10 min). Chic signature check. Monsieur go-ahead. Four check-in sends. The Michael & Carly call.

## Honest note on this document
It lists thirteen gaps. That is not a sign the system is broken; it is what a pre-mortem is supposed to produce. Six of them are under 20 minutes each. The three that matter most (spam filter, debrief, close mechanism) are the ones that map directly onto the deals already lost.
