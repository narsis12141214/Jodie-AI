# Photography inquiry tracker — LIVE
**Canonical state for every open inquiry and every booked client's next milestone.**
Updated: 29 September 2026 (follow-ups drafted, Steva insurance query in). Jodie maintains this. It opens every morning brief.
Cadence and templates: `.claude/templates/inquiry-follow-up-playbook.md`

---

## ⚠️ OVERDUE TODAY

| Who | Track | Last contact | Days | Touches missed | Action now |
|---|---|---|---|---|---|
| **Nicole & Ioannis** | A | 21 Sept (inquiry reply) | **8** | Day 2 email, Day 5 WhatsApp | CONFIRMED SILENT (Hadi, 29 Sept). Follow-up #1 drafted: `projects/photography/29-09-26/followups-nicole-margareth.md`. Send today, same thread. |
| **Margareth & Liviu** | A | 21 Sept (discovery questions) | **8** | Day 2 email, Day 5 WhatsApp | CONFIRMED SILENT (Hadi, 29 Sept). Follow-up #1 drafted, ask deliberately shrunk to two questions. Send today, same thread. |

Both confirmed silent by Hadi on 29 Sept. Drafts ready.

**Also today:** Steva asked whether we hold public liability insurance (council park permit). We do. Reply drafted at `projects/photography/29-09-26/email-steva-public-liability.md`. ⚠️ Check the cover level against the council's stated minimum before sending.

---

## OPEN INQUIRIES

| Who | Date / event | Value | Track | Stage | Next touch | When |
|---|---|---|---|---|---|---|
| Nicole Wong & Ioannis Andoniou | 17 Jun 2027, Islington Town Hall → Underground → Royal Exchange → Waterhouse Project | The Bloom £2,300 (Glow £3,500 realistic) | A | Inquiry reply sent 21 Sept, The Bloom named, asked to hold the date | Follow-up #1 | **OVERDUE** |
| Margareth Cartagena & Liviu Tudor | 24 May 2027 (Mon), Chelsea Old Town Hall. Wedding + pre-wedding | TBC, Glow-shaped if both | A | Discovery questions sent 21 Sept, no price yet | Follow-up #1 | **OVERDUE** |

---

## BOOKED — next milestone

| Who | Event | Status | Next milestone | When |
|---|---|---|---|---|
| **Steva Alexander & Percy Jacks** | 10 Oct 2026, Bexleyheath historic house. The Bloom £2,300 | Deposit £690 paid | **Balance £1,610 due** | **Fri 3 Oct — 4 days** |
| | | | Planning conversation | Trigger was 21 Sept, status unverified. She is clearly mid-planning (park permit applied for, insurance checked), so this may be happening informally by email. |
| **Selina Khuu & Marli Oshlack** | Shot 12 Sept, Westminster. Grace collection, paid | Proofs delivered and received ✅ | They select 50 → final gallery within 2 weeks of selection | Awaiting their selection |
| | | | **Review ask + referral ask** go IN the final gallery email | Not a separate task. Template: `.claude/templates/delivery-email-standard-paragraphs.md` |

---

## CLOSED

| Who | Outcome | Date | Why it matters |
|---|---|---|---|
| **Arijit Deb & Raima Banerjee** | **LOST.** Said yes 21 Sept, asked for next steps, booking link sent, no payment, no reply. Shoot date 23 Sept passed. | 29 Sept | **Hadi's read (29 Sept): they opened the email, the link and the proposal, then went quiet. Their plans likely changed.** So this was probably a decision rather than an oversight, and a follow-up may not have converted it. What a day-1 call WOULD have done is tell us why, which is worth knowing. Still the Track C stage that killed LaMure, still no mechanism at the time. £680. |
| **Michael Curtis & Carly** | **LOST.** Silent since our reply 4 Sept. Day-5 phone trigger written into the priorities file, never fired. Shoot dates 23/24 Sept passed. | 29 Sept | **Track B failure.** Fixed travel dates from Orlando. The one lead type where email alone never works, and email alone is what they got. £680. |
| John Waite & Oksana Ryjouk | Silent since 24 Aug (36 days). 10 Jul 2027 wedding. Day-14 close-out never sent. | 29 Sept | Close out properly or leave dormant. Hadi's call. Wedding is 9 months out so a Track A close-out email costs nothing and may reopen it. |
| Implant + Perio Clinic (agency) | Parked. One-line touch diarised first week of Jan 2027. | 14 Sept | — |
| Kanaka, Samantha, Maria, Andrey (scam) | Lost / closed earlier | — | — |

**Two bookings lost to our own silence in September. £1,360.** Neither couple said no. Neither was asked twice.

---

## How this file stays true
1. **Every outbound message gets logged here the day it goes** (date + what + which track).
2. **Every reply resets the clock** and moves the stage.
3. **Jodie opens every morning brief with the OVERDUE TODAY table.** If it is empty, that is the report.
4. The n8n workflow (`projects/photography/n8n-inquiry-followup.json`) fires at 9am daily and emails Hadi the same list with the message text ready to send, so the cadence does not depend on a session happening.
