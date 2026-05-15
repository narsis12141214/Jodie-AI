# Email Outreach Scripts — Cold Email (Automated, Instantly + Lead Engine)

**Channel:** Cold email
**Owner:** Instantly handles delivery automatically. Lead Engine provides CSV data. Zizi loads leads, handles replies, runs weekly audit.
**Data source:** Hadi's custom Lead Engine (CSV output) — pre-filtered for rating ≥ 3.5, review count ≥ 50, non-chain
**Status:** ALL 4 SEGMENTS LOCKED 15 May 2026. Restaurants, Dental, Aesthetic Clinics, Fitness/Gyms — 12 email templates total (4 segments × 3 steps), all approved by Hadi step-by-step. Architecture is data-backed per `cold-email-research.md`.

**Companion file:** `outreach-scripts-dm.md` (Instagram DMs, Zizi manual)

---

## Master segment status

| Segment | Step 1 | Step 2 | Step 3 | Clip ready? |
|---|---|---|---|---|
| 🍽️ Restaurants & Cafes | ✅ APPROVED | ✅ APPROVED | ✅ APPROVED (A/B subject) | ✅ Yes |
| 🦷 Dental Practices | ✅ APPROVED | ✅ APPROVED (A/B outcome) | ✅ APPROVED (A/B subject) | ✅ Yes |
| 💉 Aesthetic Clinics | ✅ APPROVED | ✅ APPROVED (A/B outcome) | ✅ APPROVED (A/B subject) | ⚠️ NOT YET |
| 🏋️ Gyms & Fitness Studios | ✅ APPROVED | ✅ APPROVED (A/B outcome) | ✅ APPROVED (A/B subject) | ⚠️ NOT YET |

**Build dependencies before send:**
1. 60-second aesthetic clip (Botox enquiry scenario) — record before A-EMAIL-1 sends
2. 60-second fitness clip (new-member enquiry scenario) — record before F-EMAIL-1 sends

**Cadence (all segments):** Step 1 sends Tue/Wed/Thu 8-10am UK. Step 2 fires next Mon-Thu, +2 to +5 days after Step 1, never Fri/Sat/Sun. Step 3 fires next Mon-Thu, +3 days after Step 2. Total sequence: 12-16 days.

**Architecture across all segments (locked):**
- Stat-led opener, NO personalisation in line 1 (avoids 2026 AI fingerprint)
- One personalisation line in paragraph 2 (Lead Engine data)
- Source anonymised: "a recent study" — no third-party AI providers named
- Soft value-offer ask: 60-second clip of AI handling a segment-relevant scenario
- "AI receptionist" for dental/aesthetic/fitness, "AI phone answering" for restaurants/cafes
- Click Desk dashboard mentioned in Step 1 P3
- Practice management integrations named where credible (SOE/Dentally for dental, Pabau/Phorest Medical for aesthetic, Mindbody/Glofox/TeamUp for fitness)
- "Costs nothing, no commitment. Reply yes." closing ask in Step 2
- A/B testing on Step 2 outcome variants and Step 3 subject lines

**Click Voice extension (15 May decision):** Click Voice (£290/mo voice-only) now available across ALL segments, not restaurants-only. Click+/Pro/Elite remain as upgrade paths. See decisions.md for trade-offs.

---

---

## Section 1 — Email operating principles

### What every email must do

1. **Personalised via real Lead Engine data**, NOT Claude generation. Templates merge deterministic fields directly. Zero per-send AI calls.
2. **Outcome-led, not feature-led.** Lead with what changes for the buyer.
3. **One question per email.** Specific. Easy to reply to in one sentence.
4. **Short.** Under 150 words per email.
5. **Sourced where it counts.** When citing a stat, name the source.

### Banned phrases (zero exceptions — audit at template approval time)

| Category | Banned |
|---|---|
| Chase language | "just checking in", "no rush", "totally understand if you're busy", "whenever you're ready", "happy to jump on a call", "sorry to bother you", "did you get my message?" |
| Generic compliments | "love that", "great that", "impressive that", "rare to see", "good to see", "amazing work" |
| Free / trial misuse | "free trial", "free audit" |
| Jargon | "AI-powered", "cutting-edge", "revolutionary", "synergy", "leverage", "NLP", "machine learning" |
| Punctuation | NO em dashes anywhere — ever |

### Automated quality gate (three structural layers, no per-send work)

Per-send manual checking does not scale. The gate is structural:

1. **Template-level quality (locked once at approval time).** All banned phrases, word counts, one-question rule, em-dash check, sourced stats are properties of the templates themselves. Once Hadi approves, the templates are LOCKED. Any change requires a new template version + re-audit.

2. **Deterministic variable population (automated, no Claude generation).** Lead Engine outputs structured CSV. Fields map DIRECTLY to template variables via Instantly's variable merge. No AI generation needed.

3. **Random sample audit (weekly, 5 random sent emails).** Zizi or Hadi pulls 5 random emails from Instantly's outbox each week. ~10-min review. Catches drift.

**Zero per-send time impact on Zizi.** Her email-related work is lead loading + reply handling + weekly audit.

### Channel rhythm (restaurant-specific, NOT the generic +4 rule)

Restaurants are open Fri-Sun for service. Emails landing during service hours get buried or read tired. Cadence rule respects that:

**Step 2 fires the NEXT Mon-Thu morning at least 2 days after Step 1. Never Friday, Saturday, or Sunday.**

| Step 1 sent | Step 2 fires | Gap |
|---|---|---|
| Monday | Wednesday | +2 |
| Tuesday | Thursday | +2 |
| Wednesday | Monday (next week) | +5 (skip weekend) |
| Thursday | Monday (next week) | +4 (skip weekend) |

**Step 3 fires the NEXT Mon-Thu morning at least 3 days after Step 2. Same Fri/Sat/Sun avoidance.**

**Archive trigger:** 7 days after Step 3 send. Suppress in Instantly. No further contact.

**Total max touches per cold email lead: 3.**
**Total sequence span: 12-16 days depending on which day Step 1 starts.**

---

## Section 2 — Restaurants and Cafes (NEW FORMAT, ready to deploy)

### Positioning angle

Lead with missed booking revenue. Use Hostie AI 43% revenue leak as the credibility stat. Click Voice (£290/month) is the entry-level offer for this segment specifically.

**Avoid:** Competing against $299 SaaS voice tools on price. Frame against doing nothing OR hiring a part-time receptionist.

### Personalisation variables (deterministic merge from Lead Engine CSV)

| Variable | Source field | Logic |
|---|---|---|
| `{restaurant_name}` | `business_name` | Direct, with encoding cleanup |
| `{first_name_or_there}` | `best_email` + `email_tier` | If `email_tier == "named"` AND local part looks like a real name, extract and capitalise. Otherwise: literal `there` |
| `{category_phrase}` | first segment of `category` | "Persian restaurant" → "Persian spot"; "Italian restaurant, Pizza restaurant" → "Italian and pizza place" |
| `{location_area}` | first 2-4 chars of `postcode` | W14 → "West Kensington"; NW1 → "Camden"; SW3 → "Chelsea". Fallback to bare postcode. |
| `{rating}` | `rating` | One decimal: 4.6 |
| `{review_count_rounded}` | `review_count` | Rounded down to nearest 100, append "+": 1496 → "1,400+" |

---

### 🍽️ R-EMAIL-1 — Restaurants Cold Email Step 1 (Opener) — APPROVED 15 May 2026

**Send when:** First touch via Instantly
**Subject:** `a quick question about bookings during busy hours`
**Preview:** `43% of UK restaurant calls miss. Worth 60 seconds?`
**Word count:** ~99
**Send window:** Tue / Wed / Thu, 8am to 10am UK time (per cold email research)

```
A recent study shows UK restaurants miss roughly 43% of inbound calls. Most are booking attempts, and most happen between 6pm and 9pm when the phone goes to voicemail.

For a {category_phrase} like {restaurant_name} in {location_area} with {review_count_rounded} reviews, this adds up fast.

We build AI phone answering for independent London restaurants. It picks up every call, takes the booking, sends it to Click Desk, our most advanced booking dashboard, built specifically for restaurants and cafes.

Want me to send a 60-second clip of one handling a Friday-night enquiry? No call, no deck, just the clip.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**Architecture notes (locked):**
- Stat-led opener, NO personalisation in line 1 (avoids the AI fingerprint pattern flagged in `cold-email-research.md`)
- One personalisation line in paragraph 2 only (Option B per Hadi 15 May)
- Source anonymised ("a recent study"), no third-party AI providers named
- Soft value-offer ask ("Want me to send X?") — 4.2% reply rate vs 1.4% for hard CTAs (Puzzle Inbox study)
- "AI phone answering" terminology (NOT "AI receptionist") — research-validated for restaurant segment
- "Click Desk" branded dashboard mention, framed as our purpose-built system
- 99 words, 4 short paragraphs, mobile-first

### 🍽️ R-EMAIL-2 — Restaurants Cold Email Step 2 (Value) — APPROVED 15 May 2026

**Send when:** Next Mon-Thu morning at least 2 days after R-EMAIL-1, never Fri/Sat/Sun
**Subject:** `following up, here's the clip`
**Preview:** `60-second AI call. Then a quick offer.`
**Word count:** ~62

```
Didn't hear back. Here's the 60-second clip I mentioned: [LINK].

If it sounds like something that'd work for {restaurant_name}, we can build a version specifically trained on your menu and booking system, so you can see for yourself how it would change your bookings and revenue. Takes 48 hours.

Want to try that? Costs nothing, no commitment. Reply yes.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**Architecture notes (locked):**
- Deliver the promised clip WITHOUT requiring a reply first (Option A from Hadi 15 May)
- Escalated ask: from "receive a generic clip" (Step 1) to "demo trained on your venue" (Step 2)
- Single personalisation token ({restaurant_name}) — less than Step 1, intentional. Over-personalising a follow-up feels manipulative.
- "Costs nothing, no commitment" replaces "free" (avoids spam-trigger word, lowers friction without sounding cheap)
- Soft binary ask: "Reply yes"
- 62 words, 3 paragraphs, mobile-first

### 🍽️ R-EMAIL-3 — Restaurants Cold Email Step 3 (Final touch) — APPROVED 15 May 2026

**Send when:** Next Mon-Thu morning at least 3 days after R-EMAIL-2, never Fri/Sat/Sun
**Subject (A/B test):**
- Variant A: `more bookings, one last time`
- Variant B: `last note about more bookings`
**Preview:** `Door stays open if it changes.`
**Word count:** ~35

```
Last email from me on this. If the timing isn't right, no worries.

If it changes, the door's open. And if you'd like to see how it works for {restaurant_name}, just reply yes.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**Architecture notes (locked):**
- Combined A (clean exit) + B (soft re-ask) per Hadi 15 May
- Soft re-ask folded into paragraph 2, not led with — doesn't feel pushy
- Single personalisation token ({restaurant_name}), matches Step 2 level
- "The door's open" singular (UK English natural reading)
- Subject A is curiosity-driven, Subject B is cleaner / more professional. Split-test on first batch, measure open rate after 100 sends, lock the winner for ongoing
- 35 words, 2 paragraphs, mobile-first
- No business-name insertion in subject (avoids AI fingerprint)

---

## RESTAURANTS SEGMENT — COMPLETE (15 May 2026)

All three email steps approved and locked. Cadence rule restaurant-specific (Mon-Thu only, never Fri/Sat/Sun).

Ready to migrate into Instantly templates per Section 7 build plan, once Hadi green-lights the deployment checklist in Section 8.

---

## Section 3 — Dental Practices (OLD FORMAT — AWAITING HADI REVIEW)

> **Note:** These templates still use Instagram-shaped {observation} variables. Once Hadi reviews the dental segment content (positioning, source data, tier recommendation), templates will be updated to use the deterministic Lead Engine merge pattern (same architecture as restaurants).

### Positioning angle

Lead with missed booking calls and lost new-patient LTV. Use Reach + Resonate AI stats. Recommend Click+ (£790/month). **Do NOT mention Click Voice — restricted to restaurants in v1.**

### Personalisation variables (CURRENT — to be replaced with Lead Engine deterministic format)
- `{first_name}` — owner or practice manager's first name
- `{practice_name}`
- `{location}`
- `{observation}` — recent new dentist join, new service launch
- `{specialism}` — "general dentistry", "cosmetic", "implants", "orthodontics"

---

### 🦷 D-EMAIL-1 — Dental Cold Email Step 1 (Opener) — APPROVED 15 May 2026

**Send when:** First touch via Instantly. Tue/Wed/Thu, 8am-10am UK.
**Subject:** `a quick question about new patient calls`
**Preview:** `32% of dental calls miss. Worth 60 seconds?`
**Word count:** ~115

```
A recent study shows UK dental practices miss roughly 32% of inbound calls. Most are patients trying to book, and most happen during the lunch service window when reception is at capacity.

For a {specialism} practice like {practice_name} in {location_area} with {review_count_rounded} reviews, every missed call is potentially a new patient walking past.

We build AI receptionists for UK dental practices. They pick up every call, qualify the enquiry, and book the patient into Click Desk, our dashboard built specifically for dental clinics. Integrates with Software of Excellence, Dentally, and EXACT.

Want me to send a 60-second clip of one handling a new-patient enquiry? No call, no deck, just the clip.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**Architecture notes (locked):**
- Same stat-led architecture as restaurants Step 1 (R-EMAIL-1)
- "AI receptionist" terminology — appropriate for dental segment per research
- Personalisation tokens in P2: {specialism}, {practice_name}, {location_area}, {review_count_rounded}
- Practice management integrations named (SOE, Dentally, EXACT) — real credibility signals, unlike restaurants where most don't have systems
- Soft value-offer ask: 60-second clip of AI handling new-patient enquiry (clip exists, confirmed by Hadi)
- No price/tier mentioned in Step 1
- 115 words, 4 short paragraphs

### 🦷 D-EMAIL-2 — Dental Cold Email Step 2 (Value) — APPROVED 15 May 2026

**Send when:** Next Mon-Thu morning at least 2 days after D-EMAIL-1, never Fri/Sat/Sun
**Subject:** `following up, here's the clip`
**Preview:** `60-second AI call. Then a quick offer.`
**Word count:** ~65
**Outcome variant A/B test:**

```
Didn't hear back. Here's the 60-second clip I mentioned: [LINK].

If it sounds like something that'd work for {practice_name}, we can build a version specifically trained on your services and booking system, so you can see for yourself how it would change your [OUTCOME] and revenue. Takes 48 hours.

Want to try that? Costs nothing, no commitment. Reply yes.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**[OUTCOME] A/B variants (split 50/50, measure reply rate at first 100 sends):**
- Variant A: `patient bookings` (frames both new AND existing patient calls — current-client inconvenience signal)
- Variant B: `new patient capture` (frames as new-patient acquisition — high LTV pull)

**Architecture notes (locked):**
- Same architecture as R-EMAIL-2 (deliver clip without requiring reply + escalate to demo offer)
- Single personalisation token ({practice_name})
- Clip exists per Hadi 15 May
- "Costs nothing, no commitment" replaces "free" (spam-trigger avoidance)
- 65 words, 3 paragraphs

### 🦷 D-EMAIL-3 — Dental Cold Email Step 3 (Final touch) — APPROVED 15 May 2026

**Send when:** Next Mon-Thu morning at least 3 days after D-EMAIL-2, never Fri/Sat/Sun
**Subject (A/B test):**
- Variant A: `more patients, one last time`
- Variant B: `last note about patient calls`
**Preview:** `Door stays open if it changes.`
**Word count:** ~35

```
Last email from me on this. If the timing isn't right, no worries.

If it changes, the door's open. And if you'd like to see how it works for {practice_name}, just reply yes.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**Architecture notes (locked):**
- Same pattern as R-EMAIL-3 — soft re-ask folded into clean exit
- Single personalisation token ({practice_name})
- A/B test on subject, measure open rate after 100 sends
- 35 words, 2 paragraphs

---

## DENTAL SEGMENT — COMPLETE (15 May 2026)

All three email steps approved and locked. Same architecture as restaurants. Different stat (32% vs 43%), different terminology ("AI receptionist" vs "AI phone answering"), different integrations (SOE/Dentally/EXACT). Clip exists per Hadi confirmation.

---

## Section 4 — Aesthetic Clinics (NEW FORMAT — APPROVED 15 May 2026)

### Positioning angle

Lead with high-value missed enquiries. Use 30-42% missed call rate + 85% no-callback rate. Reference Pabau and Phorest Medical for integration credibility. Regulatory framing baked in: AI books consultations, never gives medical advice.

### Personalisation variables (deterministic merge from Lead Engine CSV)

| Variable | Source field | Logic |
|---|---|---|
| `{clinic_name}` | `business_name` | Direct |
| `{treatment_focus}` | first segment of `category` | "Aesthetic clinic" → "aesthetic"; "Medical aesthetics" → "medical aesthetics"; "Cosmetic clinic" → "cosmetic". Lookup table for natural phrasings. |
| `{location_area}` | first 2-4 chars of `postcode` | Same as restaurants/dental |
| `{review_count_rounded}` | `review_count` | Same as restaurants/dental |

---

### 💉 A-EMAIL-1 — Aesthetic Clinics Cold Email Step 1 (Opener) — APPROVED 15 May 2026

**Send when:** First touch via Instantly. Tue/Wed/Thu, 8am-10am UK.
**Subject:** `a quick question about consultation enquiries`
**Preview:** `30-42% of aesthetic calls miss. Worth 60 seconds?`
**Word count:** ~120

```
A recent study shows UK aesthetic clinics miss between 30% and 42% of inbound calls. 85% of those callers don't call back. Most are patients enquiring about high-value treatments at the moment they're closest to booking.

For an aesthetic clinic like {clinic_name} doing {treatment_focus} in {location_area} with {review_count_rounded} reviews, every missed call could be a multi-thousand-pound patient walking past.

We build AI receptionists for UK aesthetic clinics. They pick up every call, qualify the enquiry, and book the consultation into Click Desk, our dashboard built specifically for aesthetic practices. Integrates with Pabau and Phorest Medical. The agent never gives medical advice or makes treatment claims.

Want me to send a 60-second clip of one handling a Botox enquiry? No call, no deck, just the clip.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**Architecture notes (locked):**
- Same stat-led architecture as restaurants/dental
- Two key data points: 30-42% missed + 85% no-callback (the latter is distinctive to aesthetics and creates urgency)
- "AI receptionist" terminology — matches landing page positioning
- Regulatory disclaimer baked in: "never gives medical advice or makes treatment claims" — removes the biggest cold-email objection in this segment
- Pabau + Phorest Medical named — biggest credibility integrations for aesthetic clinics
- 120 words, 4 short paragraphs
- ⚠️ **BUILD DEPENDENCY:** 60-second clip of AI handling a Botox enquiry NOT yet recorded. Production task before sending.

---

### 💉 A-EMAIL-2 — Aesthetic Clinics Cold Email Step 2 (Value) — APPROVED 15 May 2026

**Send when:** Next Mon-Thu morning at least 2 days after A-EMAIL-1, never Fri/Sat/Sun
**Subject:** `following up, here's the clip`
**Preview:** `60-second AI call. Then a quick offer.`
**Word count:** ~65
**Outcome variant A/B test:**

```
Didn't hear back. Here's the 60-second clip I mentioned: [LINK].

If it sounds like something that'd work for {clinic_name}, we can build a version specifically trained on your treatments and booking system, so you can see for yourself how it would change your [OUTCOME] and revenue. Takes 48 hours.

Want to try that? Costs nothing, no commitment. Reply yes.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**[OUTCOME] A/B variants:**
- Variant A: `consultation bookings` (direct operational framing — easy to picture)
- Variant B: `new patient capture` (strategic LTV framing — patient lifetime value pull)

**Architecture notes (locked):**
- Same architecture as R-EMAIL-2 / D-EMAIL-2
- Single personalisation token ({clinic_name})
- "Treatments and booking system" replaces "menu" / "services"
- 65 words, 3 paragraphs

---

### 💉 A-EMAIL-3 — Aesthetic Clinics Cold Email Step 3 (Final touch) — APPROVED 15 May 2026

**Send when:** Next Mon-Thu morning at least 3 days after A-EMAIL-2, never Fri/Sat/Sun
**Subject (A/B test):**
- Variant A: `more consultations, one last time`
- Variant B: `last note about consultation calls`
**Preview:** `Door stays open if it changes.`
**Word count:** ~35

```
Last email from me on this. If the timing isn't right, no worries.

If it changes, the door's open. And if you'd like to see how it works for {clinic_name}, just reply yes.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**Architecture notes (locked):**
- Same pattern as R-EMAIL-3 / D-EMAIL-3
- Single personalisation token ({clinic_name})
- 35 words, 2 paragraphs

---

## AESTHETIC CLINICS SEGMENT — COMPLETE (15 May 2026)

All three email steps approved and locked.

**⚠️ Production blocker:** 60-second aesthetic clinic clip (Botox enquiry scenario) not yet recorded. Build dependency before A-EMAIL-1 sends start.

---

## Section 5 — Gyms and Fitness Studios (NEW FORMAT — APPROVED 15 May 2026)

### Positioning angle

Lead with lead leakage outside reception hours + retention math. Reference Mindbody/Glofox/TeamUp integration for credibility.

### Personalisation variables (deterministic merge from Lead Engine CSV)

| Variable | Source field | Logic |
|---|---|---|
| `{studio_name}` | `business_name` | Direct |
| `{discipline}` | first segment of `category` | "Pilates studio" → "Pilates"; "Yoga studio" → "yoga"; "CrossFit gym" → "CrossFit"; "Personal training" → "PT". Lookup table. |
| `{location_area}` | first 2-4 chars of `postcode` | Same as other segments |
| `{review_count_rounded}` | `review_count` | Same as other segments |

---

### 🏋️ F-EMAIL-1 — Fitness Cold Email Step 1 (Opener) — APPROVED 15 May 2026

**Send when:** First touch via Instantly. Tue/Wed/Thu, 8am-10am UK.
**Subject:** `a quick question about new member enquiries`
**Preview:** `50-60% of fitness enquiries arrive after hours.`
**Word count:** ~120

```
A recent study shows UK fitness studios get 50-60% of new-member enquiries outside reception hours. Evenings, Sundays, the gaps between class times. Most never get a callback. Industry average annual retention sits at 66.4%, and 2 staff-member interactions per member per month reduces cancellation risk by a third. Those interactions rarely happen.

For a {discipline} studio like {studio_name} in {location_area} with {review_count_rounded} reviews, this is exactly where the leakage compounds.

We build AI receptionists for UK fitness studios. They pick up every call and DM 24/7, capture the lead, book trial classes, and route every enquiry into Click Desk, our dashboard built specifically for fitness operators. Integrates with Mindbody, Glofox, and TeamUp.

Want me to send a 60-second clip of one handling a new-member enquiry? No call, no deck, just the clip.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**Architecture notes (locked):**
- Same stat-led architecture as other segments
- Two data points combined: 50-60% off-hours enquiries + 33% retention lift from 2 monthly interactions
- "AI receptionist" terminology — appropriate for fitness segment
- Mindbody/Glofox/TeamUp named — top-3 UK fitness booking systems
- 120 words, 4 short paragraphs
- ⚠️ **BUILD DEPENDENCY:** 60-second clip of AI handling a new-member fitness enquiry NOT yet recorded. Production task before sending.

---

### 🏋️ F-EMAIL-2 — Fitness Cold Email Step 2 (Value) — APPROVED 15 May 2026

**Send when:** Next Mon-Thu morning at least 2 days after F-EMAIL-1, never Fri/Sat/Sun
**Subject:** `following up, here's the clip`
**Preview:** `60-second AI call. Then a quick offer.`
**Word count:** ~65
**Outcome variant A/B test:**

```
Didn't hear back. Here's the 60-second clip I mentioned: [LINK].

If it sounds like something that'd work for {studio_name}, we can build a version specifically trained on your classes and booking system, so you can see for yourself how it would change your [OUTCOME] and revenue. Takes 48 hours.

Want to try that? Costs nothing, no commitment. Reply yes.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**[OUTCOME] A/B variants:**
- Variant A: `new member bookings` (direct operational framing — class booking conversion)
- Variant B: `lead capture and retention` (strategic framing — retention math)

**Architecture notes (locked):**
- Same architecture as R/D/A Step 2 templates
- Single personalisation token ({studio_name})
- "Classes and booking system" replaces "menu" / "services" / "treatments"
- 65 words, 3 paragraphs

---

### 🏋️ F-EMAIL-3 — Fitness Cold Email Step 3 (Final touch) — APPROVED 15 May 2026

**Send when:** Next Mon-Thu morning at least 3 days after F-EMAIL-2, never Fri/Sat/Sun
**Subject (A/B test):**
- Variant A: `more members, one last time`
- Variant B: `last note about lead capture`
**Preview:** `Door stays open if it changes.`
**Word count:** ~35

```
Last email from me on this. If the timing isn't right, no worries.

If it changes, the door's open. And if you'd like to see how it works for {studio_name}, just reply yes.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**Architecture notes (locked):**
- Same pattern as R/D/A Step 3 templates
- Single personalisation token ({studio_name})
- 35 words, 2 paragraphs

---

## FITNESS / GYMS SEGMENT — COMPLETE (15 May 2026)

All three email steps approved and locked.

**⚠️ Production blocker:** 60-second fitness clip (new-member enquiry scenario) not yet recorded. Build dependency before F-EMAIL-1 sends start.

---

## Section 6 — Reply handler library (Email)

When a cold-email reply arrives, Zizi classifies it and responds.

### Handler 1 — Positive ("Tell me more")

```
Great, thanks {first_name}. Best way to do this is a short 30-minute call where I walk you through how it'd actually work for {business_name}, and we look at the numbers together. No pitch, no slide deck.

Two slots that work my end this week: {time_option_1} or {time_option_2}. Either of those, or suggest one that works better for you.
```

### Handler 2 — Objection: "Too expensive"

```
Fair question {first_name}. Worth comparing against the right alternative — most {segment_type} owners hiring a part-time receptionist spend £1,500-£1,800/month for partial coverage. We're £290 to £1,290 depending on tier, with 24/7 cover and content production included from Click+ upward.

If you tell me what you're spending or considering spending, I can show you what changes when we run it instead. No pitch, just the maths.
```

### Handler 3 — Objection: "Already have something"

```
Got it {first_name}, fair enough. Two quick questions while I'm here, and either is fine — what's working well with {current_solution}? And what would you change if you could?

Asking because we usually pick up clients who've tried a couple of solutions and want something more specific to {segment_type}. If yours is already nailed, no need to keep talking.
```

### Handler 4 — "Not now" / "Maybe later"

```
Totally fair {first_name}. Want me to come back to you in {30 / 60 / 90 days}, or is it more of a "not in the foreseeable future" kind of thing? Either's fine, just want to know whether to keep you on my list or not.
```

### Handler 5 — Unsubscribe

```
Done. Removed from my list. Best with {business_name}.
```

Suppress in Instantly + remove from outreach tracker same-day.

### Handler 6 — Referral

```
Appreciate that {first_name}. Quick check — okay if I mention you suggested I reach out when I get in touch with {referred_contact}? Just to give the message some context.
```

### Handler 7 — Annoyed / hostile

```
Sorry {first_name}, didn't mean to cause any frustration. Removed from my list. Won't message again.
```

Add to do-not-contact list. Audit how they got into the list.

---

## Section 7 — Email outreach automation build (Lead Engine → Instantly)

**Architecture for fully automated cold email outreach.** No per-send manual work. Hadi reviews templates once + 5 random emails per week.

### Lead source: Hadi's custom Lead Engine (NOT Apify, NOT Apollo)

Lead Engine outputs CSV files with this schema (observed in `clean_restaurants_leads_20260420_195627.csv`):

| Field | Type | Use |
|---|---|---|
| `business_name` | string | → `{restaurant_name}` |
| `best_email` | string | recipient email |
| `email_tier` | enum: `named` / `role` / `generic` | controls `{first_name_or_there}` resolution |
| `all_emails` | semicolon-separated list | fallback emails if `best_email` bounces |
| `phone_e164` | string | future use, not in current templates |
| `website_domain` | string | enrichment / future reference |
| `postcode` | string | → `{location_area}` via postcode-to-area lookup |
| `rating` | float | → `{rating}` |
| `review_count` | int | → `{review_count_rounded}` |
| `category` | comma-separated list | → `{category_phrase}` via parser |
| `address` | string | future use |
| `latitude`/`longitude` | float | future use (London zone segmentation) |
| `data_source` | string | provenance |

**Pre-filtering already done by Lead Engine:**
- Rating ≥ 3.5
- Review count ≥ 50
- Non-chain
- Real London (or specified region) operators

Trust the list quality. No re-filtering needed at outreach time.

### Variable resolution rules

| Variable | Source | Logic |
|---|---|---|
| `{restaurant_name}` | `business_name` | Direct copy. Clean encoding artefacts. |
| `{first_name_or_there}` | `best_email` + `email_tier` | If `email_tier == "named"` AND local part looks like a real name: extract + capitalise. Otherwise: literal `there`. Fallback ALSO triggers if local part contains: `info`, `events`, `bookings`, `reservations`, `contact`, `hello`, `press`, `admin`, `sales`, `marketing`, `office`, `support`, `help`, `team`. |
| `{category_phrase}` | first segment of `category` | Lookup table for natural phrasings ("Persian restaurant" → "Persian spot"; "Italian restaurant, Pizza restaurant" → "Italian and pizza place") |
| `{location_area}` | `postcode` first 2-4 chars | Map to area name. W14 → "West Kensington"; NW1 → "Camden"; SW3 → "Chelsea"; EC1 → "Clerkenwell". Fallback: bare postcode. |
| `{rating}` | `rating` | One decimal |
| `{review_count_rounded}` | `review_count` | Round down to nearest 100, append "+": 1,496 → "1,400+" |

### Build needed (estimated 4-6 hours)

| Task | Tool | Time |
|---|---|---|
| 1. CSV → Instantly importer mapping Lead Engine fields to Instantly variables | n8n or Instantly CSV import + field mapping | 90 min |
| 2. `email_tier` → `{first_name_or_there}` logic | n8n function node or Instantly formula | 30 min |
| 3. Postcode → `{location_area}` lookup table (top 30 London postcodes) | Sheet + n8n lookup or Instantly snippet | 60 min |
| 4. Category parser for `{category_phrase}` (top 20 common categories) | n8n function node | 60 min |
| 5. Encode-clean email data (strip `u003e`, `%20`, other URL artefacts) | n8n cleanup node | 30 min |
| 6. Instantly templates set up with merge variables | Instantly UI | 60 min |
| 7. End-to-end test on 10 sample leads | Manual | 60 min |
| 8. Weekly random-sample audit reminder (Mondays 9am) | Calendar | 5 min |

### Data quality issues observed in sample CSV (Lead Engine TODO)

1. **URL-encoded artefacts in some emails:**
   - `u003ehello@libertinelondon.co.uk` (should be `hello@libertinelondon.co.uk`)
   - `%20info@rowleys.co.uk` (should be `info@rowleys.co.uk`)
   - `nfo@sangennaro.co.uk` (missing leading "i")
2. **Encoding corruption in some business names:**
   - `Crystal China å³ç¼` (Chinese characters lost)
   - `Andromeda Greek Restaurant ð¬ð·` (Greek flag emoji corrupted)
   - `Eliâs Restaurant` (apostrophe rendered as `â`)
3. **Some "named" emails are role aliases mis-classified:**
   - `events@`, `bookings@`, `reservations@`, `info@` tagged as "named" when they should be "role"

**Recommendation:** Fix encoding + email_tier classification in the Lead Engine. Until then, n8n cleanup node strips artefacts and the fallback logic in `{first_name_or_there}` catches mis-classified role aliases.

### Email tier prioritisation (queue order in Instantly)

Send order priority:

1. **`email_tier = "named"`** highest priority. Higher reply rate expected.
2. **`email_tier = "role"`** medium priority. Functional but less personal.
3. **`email_tier = "generic"`** lowest priority. Often filtered. Send last.

For a batch of 200 leads: named first, then role, then generic. Maximises early reply yield.

### Lead enrichment opportunities (Phase 2, after basic flow works)

- **`phone_e164`** → SMS follow-up channel (compliance + consent permitting)
- **Coordinates** → London zone segmentation (central / inner / outer) for tier targeting
- **Multiple category tags** → trigger different templates for combined-type businesses
- **`all_emails`** → fallback chain if `best_email` bounces

### Scalability

- 50 emails/day: handled. Zero per-send work. 10 min/week audit.
- 100 emails/day: same architecture.
- 200 emails/day: same architecture. Increase audit sample to 10/week.
- 500+ emails/day: revisit. Probably need warmup batching + sending domain rotation.

This is the path to 70/day → 100/day from the 60-day plan, achievable without hiring.

---

## Section 8 — Email deployment checklist (after Hadi approval)

- [ ] Hadi reviews this file (Restaurants segment + automation architecture). Flags edits.
- [ ] Hadi reviews Dental, Aesthetic, Fitness segments. Once approved, Jodie updates those templates to use Lead Engine deterministic format (same as Restaurants).
- [ ] Jodie applies edits.
- [ ] Build the 8 tasks in Section 7 (~4-6 hours).
- [ ] Test end-to-end on 10 sample leads from the Restaurants CSV.
- [ ] Set up Instantly templates with merge variables exactly as named.
- [ ] Queue first batch of 50 restaurants emails sorted by `email_tier` priority.
- [ ] Set Monday 9am calendar reminder for weekly audit.
- [ ] First reply-rate check at 100 sends.
- [ ] First kill condition check at 200 sends per segment.

---

## Section 9 — Email risks flagged for pushback

1. **Restaurants is the only segment with NEW format ready.** Dental, aesthetic, fitness still in OLD format. Cannot deploy those segments via email automation until templates are converted post-review.

2. **Subject lines: one per template, no A/B yet.** If open rates lag in Instantly, we add A/B variants. Worth setting up on R-EMAIL-1 first.

3. **Click Voice is restaurants-only.** Other segments lead with Click+ (£790) or Click Pro (£1,290) as entry. If reply rates in those segments are weak, the missing lower-price tier could be a factor.

4. **Lead Engine data quality issues** (URL-encoded emails, encoding corruption, email_tier mis-classification) need upstream fixes. n8n workarounds catch most but a clean Lead Engine output is the real solution.

5. **No bounce / spam complaint handling defined.** Standard Instantly suppression handles this, but worth confirming the suppression list is up to date before first batch.

---

**End of email scripts file. Awaiting Hadi review.**

Restaurants segment ready to deploy after build. Dental, Aesthetic, Fitness segments need format conversion after Hadi reviews them.
