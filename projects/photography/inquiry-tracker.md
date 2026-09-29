# Photography inquiry tracker — LIVE
**Canonical state for every open inquiry and every booked client's next milestone.**
Updated: 29 September 2026. Jodie maintains this. It opens every morning brief.
Cadence and templates: `.claude/templates/inquiry-follow-up-playbook.md`

---

## ⚠️ OVERDUE TODAY

| Who | Track | Last contact | Days | Touches missed | Action now |
|---|---|---|---|---|---|
| **Nicole & Ioannis** | A | 21 Sept (inquiry reply) | **8** | Day 2 email, Day 5 WhatsApp | ⚠️ **STATUS UNVERIFIED — did they reply?** If silent: Day 9 email is due tomorrow. Send the Day 2 email today instead and reset. WhatsApp 07895 008349. |
| **Margareth & Liviu** | A | 21 Sept (discovery questions) | **8** | Day 2 email, Day 5 WhatsApp | ⚠️ **STATUS UNVERIFIED — did they reply?** Same as above. WhatsApp 07944 598829. |

Both were sent on the same day and neither has a logged reply. If they did reply and Hadi handled it, tell me and I will move them.

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
| | | | Planning conversation | Trigger was 21 Sept. Status unverified. |
| **Selina Khuu & Marli Oshlack** | Shot 12 Sept, Westminster. Grace collection, paid | Proofs delivered and received ✅ | They select 50 → final gallery within 2 weeks of selection | Awaiting their selection |
| | | | **Review ask + referral ask** go IN the final gallery email | Not a separate task. Template: `.claude/templates/delivery-email-standard-paragraphs.md` |

---

## CLOSED

| Who | Outcome | Date | Why it matters |
|---|---|---|---|
| **Arijit Deb & Raima Banerjee** | **LOST.** Said yes 21 Sept, asked for next steps, booking link sent, no payment, no reply. Shoot date 23 Sept passed. | 29 Sept | **Track C failure.** A verbal yes with no follow-up mechanism. Same stage that killed LaMure. £680. Four hours and one WhatsApp would have told us whether the link worked. |
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
