# Outreach Script Rewrite — 15 May 2026 (DEPRECATED — content split)

> **DO NOT USE THIS FILE.** Per Hadi's 15 May call, content has been split into two channel-specific files for cleaner ownership:
>
> - **DM scripts:** `outreach-scripts-dm.md` (Instagram, manual Zizi workflow)
> - **Email scripts:** `outreach-scripts-email.md` (Cold email, Instantly + Lead Engine automation)
>
> File kept for git history reference only. All future review and edits happen in the two split files.

**Status:** DEPRECATED. Content migrated.

**Replaces:** All prior outreach templates in `outreach/message-library.md`. After Hadi approval, this file becomes the new canonical source; `outreach/message-library.md` updated to reference it or migrated in full.

**Owner:** Jodie drafts, Hadi approves, Zizi executes (DMs) + Instantly executes (emails) + Workflow 2 (n8n) executes auto-openers.

---

## Section 1 — Operating principles (read before using any template)

### What every message must do

1. **Personalised to the prospect.** Real observation from their Instagram, Google profile, website, or local context. NOT a fake compliment.
2. **Outcome-led, not feature-led.** Lead with what changes for the buyer (more bookings, recovered missed calls, hours back) — NOT with product names, AI jargon, or package contents.
3. **One specific question.** Every message ends with a yes/no decision question OR a single open question. Never both.
4. **Short.** DMs under 60 words. Emails under 150 words. Buyers don't read walls of text.
5. **Sourced where it counts.** When citing a stat, name the source (Hostie AI, Resonate, GymMaster, etc.). Builds credibility, differentiates from spam.

### Banned phrases (zero exceptions, audit before sending)

| Category | Banned |
|---|---|
| Chase language | "just checking in", "no rush", "totally understand if you're busy", "whenever you're ready", "happy to jump on a call", "sorry to bother you", "did you get my message?" |
| Generic compliments | "love that", "great that", "impressive that", "rare to see", "good to see", "amazing work" |
| Free / trial misuse | "free trial", "free audit" — say "14-day trial" or "trial period" instead. We have a trial, not a free trial. |
| Jargon | "AI-powered", "cutting-edge", "revolutionary", "synergy", "leverage", "NLP", "machine learning" |
| Punctuation | NO em dashes anywhere — ever. Use commas, full stops, or new sentences. |

### Quality gate (split by channel — manual for DMs, structural for emails)

Manual per-send checking doesn't scale at 50-100 outreach/day. The gate is split:

**For Instagram DMs (Zizi sends manually):**

Zizi runs this checklist per message before sending:
- [ ] Personalised observation is real and specific (not template-able)
- [ ] No banned phrases
- [ ] One question, not two
- [ ] Under word count
- [ ] No em dashes
- [ ] Variable placeholders ({first_name}, {business_name}, etc.) are all filled
- [ ] If a stat is included, source is named

DMs are slow-throughput, manual-channel work. The per-send check is appropriate here.

**For cold emails (Instantly + Lead Engine, automated):**

Three structural layers replace the per-send checklist:

1. **Template-level quality (locked once at approval time).** All banned phrases, word counts, one-question rule, em-dash check, sourced stats are properties of the templates themselves. Once Hadi approves the templates, they are LOCKED. No ad-hoc edits. Any change requires a new template version + re-audit.

2. **Deterministic variable population (automated, no Claude generation needed).** The Lead Engine outputs structured CSV data: `business_name`, `best_email`, `email_tier` (named/role/generic), `category`, `rating`, `review_count`, `postcode`, `address`. These map DIRECTLY into the email templates via Instantly's variable merge. No AI generation needed for the email opener — the personalisation IS the factual data fields. See Section 7.5 for the full architecture.

3. **Random sample audit (weekly, 5 random sent emails).** Zizi (or Hadi) pulls 5 random emails from Instantly's outbox each week. ~10-minute review. Catches any drift. Cheap insurance.

Total time per email = 0 minutes per send + 10 minutes per week audit. Scales cleanly to 100+ emails/day.

**Total per-channel time impact for Zizi:**
- DMs: Per-send manual check stays (low volume, high personalisation)
- Emails: Lead loading + reply handling + weekly audit only. No per-send work.

This unblocks the path to 100/day outreach volume without bottlenecking on Zizi.

### Channel rhythm

| Channel | Step 1 → Step 2 | Step 2 → Step 3 | Step 3 → Archive |
|---|---|---|---|
| Instagram DM | 4 days no reply | 5 days no reply | 7 days no reply → archive |
| Cold email | 4 days no open OR no reply | 5 days no reply | 7 days no reply → archive |

**Total max touches per cold lead: 3.** After Step 3, do not contact further unless they reach back out.

---

## Section 2 — Restaurants and Cafes

### Positioning angle

Lead with missed booking revenue. Use Hostie AI 43% revenue leak as the credibility stat. Click Voice (£290/month) is the entry-level offer for this segment specifically — the only segment we promote Click Voice to in v1.

**Avoid:** Competing against $299 SaaS voice tools on price. Frame against doing nothing OR hiring a part-time receptionist.

**Personalisation variables — TWO DIFFERENT SOURCES depending on channel:**

**For DMs (Instagram, Zizi manual):**
- `{first_name}` — owner's first name (Zizi finds from Instagram profile or via tagged owner posts)
- `{restaurant_name}` — exact spelling
- `{cuisine_or_concept}` — "Persian", "Italian", "neighbourhood cafe"
- `{location}` — "West Hampstead", "Soho", "Notting Hill"
- `{observation}` — one specific real detail from Instagram (dish post, anniversary, special) — Zizi sources OR Workflow 2 generates

**For emails (Lead Engine CSV, fully automated merge):**

Data fields populated directly from the CSV row, no Claude generation needed:
- `{first_name}` — derived from `best_email` if email_tier = "named" (alex@ukai.co.uk → "Alex"). Fallback for role/generic emails: skip first name entirely OR use "there"
- `{restaurant_name}` — from `business_name`
- `{category_phrase}` — first segment of `category` field, formatted as natural language ("Persian restaurant" → "Persian spot"; "Italian restaurant, Pizza restaurant" → "Italian and pizza place")
- `{location_area}` — from `postcode` mapped to area name (W14 → "West Kensington"; NW1 → "Camden"; SW3 → "Chelsea"). Fallback to bare postcode if mapping unavailable.
- `{rating}` — from `rating` field (e.g., "4.6")
- `{review_count}` — from `review_count`, formatted with thousands separator (1496 → "1,496")
- `{review_count_rounded}` — rounded down to nearest 100 for natural language (1496 → "1,400+")

These are all deterministic. Instantly's variable merge handles them directly. No Claude API call needed for email opener generation.

---

### 🍽️ R-DM-1 — Restaurants Instagram DM Step 1 (Opener)

**Send when:** First touch to a cold restaurant lead
**Next step:** If no reply after 4 days → send R-DM-2
**Word count:** ~40

```
Hey {first_name}, saw your post about {observation} at {restaurant_name}.
Quick question — how many calls a week do you reckon you miss when the floor's slammed? Most {cuisine_or_concept} spots in {location} lose 1 in 3, and most of those callers don't leave a message.
Curious what your number looks like.
```

---

### 🍽️ R-DM-2 — Restaurants Instagram DM Step 2 (Value follow-up)

**Send when:** R-DM-1 sent + 4 days no reply
**Next step:** If no reply after 5 days → send R-DM-3
**Word count:** ~55

```
{first_name}, came across some data that surprised me. Hostie AI tracked UK restaurants losing up to 43% of inbound booking revenue to unanswered or abandoned calls. £292K recovered for a single restaurant in their case study.
We've just launched a voice agent built specifically for UK restaurants and cafes — £290/month, custom-built per venue. Want to see a 48-hour demo of how it'd sound for {restaurant_name}?
```

---

### 🍽️ R-DM-3 — Restaurants Instagram DM Step 3 (Final touch)

**Send when:** R-DM-2 sent + 5 days no reply
**Next step:** No reply after 7 days → archive
**Word count:** ~25

```
{first_name}, last one from me. If the timing's not right, totally fine. If it changes, you know where I am. Best with {restaurant_name}.
```

---

### 🍽️ R-EMAIL-1 — Restaurants Cold Email Step 1 (Opener)

**Send when:** First touch via Instantly
**Subject:** `How many booking calls does {restaurant_name} miss?`
**Preview:** `Most UK restaurants lose 1 in 3. Quick question.`
**Word count:** ~95

```
Hi {first_name_or_there},

Came across {restaurant_name} on Google earlier this week. A {category_phrase} in {location_area} with {review_count_rounded} reviews and a {rating} rating, clearly a busy spot.

One question. UK restaurants lose roughly 43% of inbound booking revenue to unanswered calls during service hours (Hostie AI tracked this in 2024). For a venue your size, that adds up fast.

What's your rough estimate of weekly missed calls? Two? Five? Ten?

Not selling anything in this email. Just curious if it's something you've thought about.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

**Variable note:** `{first_name_or_there}` resolves to "Alex" for named emails, "there" for role/generic emails (info@, reservations@). This avoids the awkward "Hi info@minemane.co.uk" effect when the lead engine couldn't extract a personal name.

---

### 🍽️ R-EMAIL-2 — Restaurants Cold Email Step 2 (Value)

**Send when:** R-EMAIL-1 sent + 4 days no open OR no reply
**Subject:** `Re: How many booking calls does {restaurant_name} miss?`
**Preview:** `New voice agent for UK restaurants, £290/month.`
**Word count:** ~130

```
Hi {first_name_or_there},

Quick follow-up. We just launched Click Voice — an AI voice receptionist built specifically for UK restaurants and cafes. £290/month. Answers every call in your restaurant's voice. Books straight into OpenTable, Resy, or your existing system.

Two things make it different from the $299/month SaaS tools you might have seen:

1. We build it for you. You don't configure anything. We script the agent on your menu, your tone, your booking policy.
2. We're not a tool. We're a team. When you change your hours, you text us, we update the agent the same day.

48-hour demo of how it'd sound for {restaurant_name}? Reply yes and I'll send the booking link.

Hadi
clickaiagency.com/ai-phone-answering-and-booking-automation-uk-restaurants-cafes
```

---

### 🍽️ R-EMAIL-3 — Restaurants Cold Email Step 3 (Final touch)

**Send when:** R-EMAIL-2 sent + 5 days no reply
**Subject:** `Closing the loop on Click Voice for {restaurant_name}`
**Preview:** `Last note from me.`
**Word count:** ~70

```
Hi {first_name_or_there},

Last email from me. If now isn't the right time for {restaurant_name}, no worries.

If anything changes (you start losing bookings, you want to compare options, you have a quick question), the door's open. Reply to this thread and we pick it up.

Otherwise, best with the restaurant.

Hadi
```

---

## Section 3 — Dental Practices

### Positioning angle

Lead with missed booking calls and lost new-patient LTV. Use Reach + Resonate AI stats. Recommend Click+ (£790/month) as standard, mention Click Pro (£1,290/month) for multi-site or specialist practices. **Do NOT mention Click Voice — restricted to restaurants in v1.**

**Avoid:** Clinical claims, treatment recommendations, GDPR-sensitive language. The AI books, the dentist treats.

**Personalisation variables:**
- `{first_name}` — owner or practice manager's first name
- `{practice_name}`
- `{location}`
- `{observation}` — recent new dentist join, new service launch, specific Google post
- `{specialism}` — "general dentistry", "cosmetic", "implants", "orthodontics"

---

### 🦷 D-DM-1 — Dental Instagram DM Step 1 (Opener)

**Send when:** First touch
**Next step:** If no reply after 4 days → D-DM-2
**Word count:** ~45

```
Hey {first_name}, saw {observation} on the {practice_name} feed.
Quick one — Reach tracked UK dental practices missing roughly 32% of inbound calls, and 80% of those are booking requests. For a {specialism} practice that's a lot of new patients walking past.
How does that match your reception experience?
```

---

### 🦷 D-DM-2 — Dental Instagram DM Step 2 (Value)

**Send when:** D-DM-1 sent + 4 days no reply
**Next step:** If no reply after 5 days → D-DM-3
**Word count:** ~55

```
{first_name}, follow-up. We run the AI receptionist for UK dental practices — voice, WhatsApp, recall sequences, integrated with Software of Excellence, Dentally, EXACT. Click+ at £790/month, full bundle.
We've just opened a founding cohort with setup at £150 instead of £500 (70% off). Want to see a 48-hour demo of how it'd answer for {practice_name}?
```

---

### 🦷 D-DM-3 — Dental Instagram DM Step 3 (Final touch)

**Send when:** D-DM-2 sent + 5 days no reply
**Next step:** No reply after 7 days → archive
**Word count:** ~25

```
{first_name}, last note. If the timing's wrong, no problem. If it changes, message me direct. Best with {practice_name}.
```

---

### 🦷 D-EMAIL-1 — Dental Cold Email Step 1 (Opener)

**Send when:** First touch via Instantly
**Subject:** `{first_name}, how many calls does {practice_name} miss per week?`
**Preview:** `Reach tracks UK dental at 32%.`
**Word count:** ~110

```
Hi {first_name},

Saw {practice_name} via Google earlier. {observation}.

Quick context. UK dental practices miss approximately 32% of inbound calls, and around 80% of those are patients trying to book (Reach 2023, Resonate AI 2024). The average practice misses 300 calls per month. At an average new-patient lifetime value of £500 to £2,000, the maths gets uncomfortable fast.

What's your rough monthly missed-call figure? Some practices know, most don't.

Not selling anything in this email. Curious if it's on your radar.

Hadi
Founder, Click AI Agency
clickaiagency.com
```

---

### 🦷 D-EMAIL-2 — Dental Cold Email Step 2 (Value)

**Send when:** D-EMAIL-1 sent + 4 days no open OR reply
**Subject:** `Re: {first_name}, how many calls does {practice_name} miss per week?`
**Preview:** `AI receptionist built for UK dental. Click+ £790/mo.`
**Word count:** ~135

```
Hi {first_name},

Quick follow-up. We run the AI receptionist for UK dental practices specifically. Voice agent that books patients into Software of Excellence, Dentally, EXACT, or a shared calendar. WhatsApp/SMS/email confirmations. Recall and reactivation sequences that fill the chair.

Click+ at £790/month. Setup is £150 right now (founding cohort, 70% off the £500 standard rate). 14-day trial from go-live, no fee until the agent is actually working for you.

What it does NOT do: clinical claims, treatment recommendations, anything outside the booking remit. The AI books. The dentist treats.

48-hour demo of how it'd answer for {practice_name}? Reply yes and I'll set it up.

Hadi
clickaiagency.com/ai-receptionist-for-uk-dental-practices
```

---

### 🦷 D-EMAIL-3 — Dental Cold Email Step 3 (Final touch)

**Send when:** D-EMAIL-2 sent + 5 days no reply
**Subject:** `Closing the loop on AI receptionist for {practice_name}`
**Preview:** `Last email from me.`
**Word count:** ~70

```
{first_name},

Last email from me on this. If the timing isn't right for {practice_name}, no worries.

If your missed-call rate changes, or a new dentist joins and you want consistent reception across the team, the door's open. Reply to this thread and we pick it up.

Best with the practice.

Hadi
```

---

## Section 4 — Aesthetic Clinics

### Positioning angle

Lead with high-value missed enquiries. Use Xtreme Gen AI 30-42% missed calls + Boutique SEO £2,950+ LTV. Recommend Click Pro (£1,290/month) as standard. Reference Pabau and Phorest Medical integration explicitly — biggest trust signal in this segment. Regulatory framing baked in: AI books, does not prescribe.

**Avoid:** Clinical claims, treatment outcome promises, anything that implies the AI handles consultations. Be respectful of NMC face-to-face consultation requirement (1 June 2025).

**Personalisation variables:**
- `{first_name}` — owner, clinic manager, or lead practitioner's first name
- `{clinic_name}`
- `{location}`
- `{observation}` — recent treatment showcase, new prescriber join, specific clinic detail
- `{treatment_focus}` — "injectables", "advanced skin", "body contouring", "combined aesthetic"

---

### 💉 A-DM-1 — Aesthetic Clinics Instagram DM Step 1 (Opener)

**Send when:** First touch
**Next step:** If no reply after 4 days → A-DM-2
**Word count:** ~50

```
Hey {first_name}, saw the {observation} on {clinic_name}'s feed.
Quick question — Xtreme Gen AI tracks UK aesthetic clinics missing 30-42% of inbound calls, and 85% of those callers don't call back. For a {treatment_focus} clinic, that's significant.
How does your missed-call rate compare? Most clinic managers don't know their actual number.
```

---

### 💉 A-DM-2 — Aesthetic Clinics Instagram DM Step 2 (Value)

**Send when:** A-DM-1 sent + 4 days no reply
**Next step:** If no reply after 5 days → A-DM-3
**Word count:** ~60

```
{first_name}, follow-up. We run the AI receptionist for UK aesthetic clinics — integrates directly with Pabau and Phorest Medical. The agent books consultations only, never gives medical advice. Click Pro at £1,290/month, full bundle.
Founding cohort setup is £250 instead of £850 right now. Want to see a 48-hour demo of how it'd handle a Botox enquiry for {clinic_name}?
```

---

### 💉 A-DM-3 — Aesthetic Clinics Instagram DM Step 3 (Final touch)

**Send when:** A-DM-2 sent + 5 days no reply
**Next step:** No reply after 7 days → archive
**Word count:** ~25

```
{first_name}, last note. If now isn't the right time, that's fine. If it changes, message direct. Best with {clinic_name}.
```

---

### 💉 A-EMAIL-1 — Aesthetic Clinics Cold Email Step 1 (Opener)

**Send when:** First touch via Instantly
**Subject:** `{first_name}, what's your missed-call rate at {clinic_name}?`
**Preview:** `30-42% across UK aesthetics. £150-£350 per booking.`
**Word count:** ~120

```
Hi {first_name},

Saw {clinic_name} earlier this week. {observation}.

Context for the question. UK aesthetic clinics miss 30-42% of inbound calls, with average missed-call rate at 29% (Xtreme Gen AI 2024). 85% of those callers don't call back. 67% contact a competitor if their first-choice clinic doesn't answer.

For a clinic at £150-£350 per Botox booking and £2,950+ annual patient LTV (Boutique SEO), every missed call adds up to roughly £23,000 to £31,000 of unrealised revenue per year per clinic.

What's your rough number, if you know it?

Hadi
Founder, Click AI Agency
```

---

### 💉 A-EMAIL-2 — Aesthetic Clinics Cold Email Step 2 (Value)

**Send when:** A-EMAIL-1 sent + 4 days no open OR reply
**Subject:** `Re: {first_name}, what's your missed-call rate at {clinic_name}?`
**Preview:** `AI receptionist that books into Pabau + Phorest.`
**Word count:** ~140

```
Hi {first_name},

Quick follow-up. We run the AI receptionist for UK aesthetic clinics specifically. Integrates directly with Pabau, Phorest Medical, Aesthetic Nurse Software, Consentz, and Clinicminds. Books consultations 24/7 into your existing system.

Two important boundaries: the AI never gives medical advice and never replaces the prescriber consultation. Per NMC requirements from June 2025, all prescribers must conduct face-to-face consultations before prescribing injectables. The agent books that consultation. Your prescriber takes it from there.

Click Pro at £1,290/month, full bundle (voice + WhatsApp + content + automation). Founding cohort setup at £250 instead of the £850 standard (70% off).

48-hour demo of how it'd handle a Botox enquiry for {clinic_name}? Reply yes and I'll send the booking link.

Hadi
clickaiagency.com/ai-receptionist-for-uk-aesthetic-clinics
```

---

### 💉 A-EMAIL-3 — Aesthetic Clinics Cold Email Step 3 (Final touch)

**Send when:** A-EMAIL-2 sent + 5 days no reply
**Subject:** `Closing the loop on AI receptionist for {clinic_name}`
**Preview:** `Final email.`
**Word count:** ~75

```
{first_name},

Final email from me. If now isn't the right time for {clinic_name}, no problem.

If your phones get busier, or a new prescriber joins and reception gets stretched, the door stays open. Reply to this thread and we pick it back up.

Best with the clinic.

Hadi
```

---

## Section 5 — Gyms and Fitness Studios

### Positioning angle

Lead with lead leakage outside hours + retention math. Use GymMaster 33% cancellation reduction stat. Recommend Click+ (£790/month). Reference Mindbody/Glofox/TeamUp integration. Differentiate from generic SaaS by emphasising done-for-you positioning.

**Avoid:** Generic "scale your gym" copy. Be specific to fitness operators.

**Personalisation variables:**
- `{first_name}` — owner's first name
- `{studio_name}` or `{gym_name}`
- `{location}`
- `{observation}` — recent class series, new trainer, specific detail
- `{discipline}` — "Pilates", "yoga", "HIIT", "CrossFit", "PT studio", "boutique fitness"

---

### 🏋️ F-DM-1 — Fitness Instagram DM Step 1 (Opener)

**Send when:** First touch
**Next step:** If no reply after 4 days → F-DM-2
**Word count:** ~45

```
Hey {first_name}, saw the {observation} at {studio_name}.
Quick question — most {discipline} studios get 50-60% of new-member enquiries outside reception hours. Evenings, Sundays, that kind of thing. They miss most of them. Voicemail, unread DMs, the lot.
How are you handling that traffic currently?
```

---

### 🏋️ F-DM-2 — Fitness Instagram DM Step 2 (Value)

**Send when:** F-DM-1 sent + 4 days no reply
**Next step:** If no reply after 5 days → F-DM-3
**Word count:** ~60

```
{first_name}, follow-up. GymMaster tracked something interesting — just 2 staff-member interactions per month reduces cancellation risk by 33%. The problem is those interactions never happen because no one has time.
We run the AI receptionist that captures every lead and runs retention sequences automatically. Click+ at £790/month, integrates with Mindbody, Glofox, TeamUp. Demo for {studio_name}?
```

---

### 🏋️ F-DM-3 — Fitness Instagram DM Step 3 (Final touch)

**Send when:** F-DM-2 sent + 5 days no reply
**Next step:** No reply after 7 days → archive
**Word count:** ~25

```
{first_name}, last note from me. If timing's off, no problem. If it changes, message direct. Best with {studio_name}.
```

---

### 🏋️ F-EMAIL-1 — Fitness Cold Email Step 1 (Opener)

**Send when:** First touch via Instantly
**Subject:** `{first_name}, where are {studio_name}'s evening leads going?`
**Preview:** `50-60% of fitness enquiries arrive after hours.`
**Word count:** ~100

```
Hi {first_name},

Saw {studio_name} earlier this week. {observation}.

One question. Most UK fitness studios get 50-60% of new-member enquiries outside reception hours. Evenings, weekends, holiday weeks. Voicemail and unread DMs lose a substantial chunk of these. Industry average annual retention sits at 66.4% (GymMaster).

For a {discipline} studio at average member LTV, those leaks add up.

What's your current setup for evening and weekend enquiries?

Hadi
Founder, Click AI Agency
```

---

### 🏋️ F-EMAIL-2 — Fitness Cold Email Step 2 (Value)

**Send when:** F-EMAIL-1 sent + 4 days no open OR reply
**Subject:** `Re: {first_name}, where are {studio_name}'s evening leads going?`
**Preview:** `AI receptionist for UK fitness. Click+ £790/mo.`
**Word count:** ~130

```
Hi {first_name},

Quick follow-up. We run the AI receptionist for UK gyms and fitness studios specifically. Voice agent + WhatsApp + class booking integration with Mindbody, Glofox, TeamUp, Acuity. Captures every lead. Runs retention sequences at 30, 60, 90 days.

GymMaster's data: just 2 staff-member interactions per member per month cuts cancellation risk by 33%. We run those interactions automatically.

Click+ at £790/month, full bundle. Founding cohort setup at £150 instead of £500 (70% off). 14-day trial from go-live.

48-hour demo of how it'd handle a new-member enquiry for {studio_name}? Reply yes and I'll send the booking link.

Hadi
clickaiagency.com/ai-receptionist-uk-gyms-fitness-studios
```

---

### 🏋️ F-EMAIL-3 — Fitness Cold Email Step 3 (Final touch)

**Send when:** F-EMAIL-2 sent + 5 days no reply
**Subject:** `Closing the loop on AI receptionist for {studio_name}`
**Preview:** `Last email.`
**Word count:** ~70

```
{first_name},

Last email from me. If now isn't the right time for {studio_name}, no worries.

If lead volume picks up, or retention slips below where you'd want it, the door's open. Reply to this thread and we pick it up.

Best with the studio.

Hadi
```

---

## Section 6 — Reply handler library

When a lead replies, Zizi classifies the reply type and responds per the handler below. Most replies fit one of seven categories.

### Handler 1 — Positive ("Tell me more" / "Sounds interesting")

**Goal:** Move them to a 30-minute demo call.

**DM/Email response:**
```
Great, thanks {first_name}. Best way to do this is a short 30-minute call where I walk you through how it'd actually work for {business_name}, and we look at the numbers together. No pitch, no slide deck.

Two slots that work my end this week: {time_option_1} or {time_option_2}. Either of those, or suggest one that works better for you.
```

**Internal note:** Zizi flags the reply to Hadi same-day. Hadi takes the call.

---

### Handler 2 — Objection: "Too expensive"

**Goal:** Reframe value, do NOT discount in the moment.

**DM/Email response:**
```
Fair question {first_name}. Worth comparing against the right alternative — most {segment_type} owners hiring a part-time receptionist spend £1,500-£1,800/month for partial coverage. We're £290 to £1,290 depending on tier, with 24/7 cover and content production included from {tier_for_segment} upward.

If you tell me what you're spending or considering spending, I can show you what changes when we run it instead. No pitch, just the maths.
```

**Internal note:** This message surfaces what the prospect is actually comparing against. Then Hadi knows whether to defend the price, restructure the offer, or walk away. Never drop price in the response itself.

---

### Handler 3 — Objection: "Already have something" / "Just signed with X"

**Goal:** Surface what's not working with their current setup, OR exit cleanly.

**DM/Email response:**
```
Got it {first_name}, fair enough. Two quick questions while I'm here, and either is fine — what's working well with {current_solution}? And what would you change if you could?

Asking because we usually pick up clients who've tried a couple of solutions and want something more specific to {segment_type}. If yours is already nailed, no need to keep talking.
```

**Internal note:** Their answer tells you everything. If they say "actually X frustrates me", you're in. If they say "all good", you walk away politely.

---

### Handler 4 — "Not now" / "Maybe later" (soft no)

**Goal:** Set a specific re-contact window, then go silent.

**DM/Email response:**
```
Totally fair {first_name}. Want me to come back to you in {30 / 60 / 90 days}, or is it more of a "not in the foreseeable future" kind of thing? Either's fine, just want to know whether to keep you on my list or not.
```

**Internal note:** Forces them to pick. Most will say "30 days fine" — log it in tracker, do not contact in between. If they say "not foreseeable future", archive properly and don't re-engage.

---

### Handler 5 — Unsubscribe / "Stop messaging me"

**Goal:** Confirm and remove. No defending, no last-ditch sell.

**DM/Email response:**
```
Done. Removed from my list. Best with {business_name}.
```

**Internal note:** Zizi removes from tracker same-day. Update Instantly suppression list if email. Never contact again unless they re-initiate.

---

### Handler 6 — Referral ("Not me, but try X")

**Goal:** Thank them and reach the referred contact warm.

**DM/Email response (to the original lead):**
```
Appreciate that {first_name}. Quick check — okay if I mention you suggested I reach out when I get in touch with {referred_contact}? Just to give the message some context.
```

**Internal note:** Wait for permission, then reach the referred contact with the warm referral as opener. If permission granted, Hadi sometimes takes the new conversation directly given the warm intro.

---

### Handler 7 — Annoyed / hostile reply

**Goal:** De-escalate, apologise, remove. Do not engage with the hostility.

**DM/Email response:**
```
Sorry {first_name}, didn't mean to cause any frustration. Removed from my list. Won't message again.
```

**Internal note:** Add to do-not-contact list. Note the lead source so we can audit how they got into the list in the first place.

---

## Section 7 — Workflow 2 prompt update (n8n + Claude API)

The Workflow 2 in n8n generates Step 1 DM openers automatically via Claude Haiku. The current prompt was tuned to old positioning. Below is the updated prompt to paste into the Claude node in n8n.

### New prompt to paste into Workflow 2 (Claude API node)

```
You are an outreach copywriter for Click AI Agency. Your job is to generate a single short Instagram DM opener (Step 1) for a UK service business.

Read the lead data below and produce ONE DM opener that follows these rules strictly:

1. Length: 30 to 55 words maximum
2. Personalised to a real observation about the business (look at the bio, recent posts, specific details in the data — never use a generic compliment)
3. Lead with a question or outcome, never with what we sell
4. End with one specific question (yes/no or open) the recipient can answer in one sentence
5. NEVER use these phrases: "just checking in", "no rush", "happy to jump on a call", "love that", "great that", "impressive that", "rare to see", "good to see", "amazing work", "AI-powered", "cutting-edge", "revolutionary", "free trial", "synergy", "leverage"
6. NEVER use em dashes. Use commas, full stops, or new sentences instead
7. NEVER mention price or package names in Step 1
8. Sound like a human, not a sales script

The angle per segment (use whichever fits):

- Restaurants and cafes: Missed booking calls. Most UK restaurants lose 1 in 3. Ask how many they reckon they miss.
- Dental practices: Missed booking calls + lost new patients. Reach tracked UK dental at 32% missed. Ask how it matches their reception experience.
- Aesthetic clinics: High-value missed enquiries. Xtreme Gen AI tracks 30-42% missed in aesthetics. Ask how their missed-call rate compares.
- Gyms and fitness studios: Lead leakage outside hours. 50-60% of new enquiries arrive after reception closes. Ask how they're handling that traffic.

Lead data:
{{ $json.lead_data }}

Generate the DM opener now. Output the message only, no preamble, no explanation.
```

### Where to paste this

n8n → Workflow 2 (Claude API Opener Generation) → Claude node → System prompt field.

Replace the existing system prompt entirely. Test on 3 sample leads before activating the full schedule.

### What to test

After updating the prompt, run Workflow 2 manually against 3 test leads (one restaurant, one dental, one fitness). Check the output for:

- Word count within 30-55
- No banned phrases
- No em dashes
- Personalisation is real, not template-able
- Question at the end is specific, not generic

If any of the 3 fail the check, iterate on the prompt before activating.

---

## Section 7.5 — Email outreach automation build (Lead Engine → Instantly)

**Architecture for fully automated cold email outreach.** No per-send manual work. Hadi reviews templates once + 5 random emails per week.

### Lead source: Hadi's custom Lead Engine (NOT Apify, NOT Apollo)

Lead Engine outputs CSV files with this schema (sample structure observed in `clean_restaurants_leads_20260420_195627.csv`):

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
| `review_count` | int | → `{review_count}` + `{review_count_rounded}` |
| `category` | comma-separated list | → `{category_phrase}` via parser |
| `address` | string | future use, not in current templates |
| `latitude`/`longitude` | float | future use (e.g., London zone segmentation) |
| `data_source` | string | provenance: `rapidapi_alexanderxbx` |

**Pre-filtering already done by Lead Engine:**
- Rating ≥ 3.5
- Review count ≥ 50
- Non-chain businesses
- Real London (or specified region) operators only

This means we trust the list quality and don't need to filter again at outreach time.

### The variable resolution rules (these power Instantly's merge)

| Variable | Source | Logic |
|---|---|---|
| `{restaurant_name}` | `business_name` | Direct copy. Clean any encoding artefacts. |
| `{first_name_or_there}` | `best_email` + `email_tier` | If `email_tier == "named"`: extract name from local part of email (alex@ → "Alex"). Capitalise. Otherwise: literal "there". |
| `{category_phrase}` | first segment of `category` | Strip "restaurant" suffix where redundant. ("Persian restaurant" → "Persian spot"; "Italian restaurant, Pizza restaurant" → "Italian and pizza place"; "Cafe" stays "cafe"). Lookup table for common phrasings. |
| `{location_area}` | first 2-4 chars of `postcode` | Map to area name via lookup table. W14 → "West Kensington"; NW1 → "Camden"; SW3 → "Chelsea"; EC1 → "Clerkenwell". Fallback: bare postcode. |
| `{rating}` | `rating` | One decimal: 4.6, 4.7, etc. |
| `{review_count}` | `review_count` | Thousands separator: 1,496 |
| `{review_count_rounded}` | `review_count` | Round down to nearest 100, append "+": 1,496 → "1,400+"; 234 → "200+"; 75 → "50+" |

### The build needed (estimated 4-6 hours total)

| Task | Tool | Time |
|---|---|---|
| 1. Build a CSV → Instantly importer that maps Lead Engine fields to Instantly variables (`{restaurant_name}`, `{first_name_or_there}`, etc.) | n8n workflow OR Instantly's CSV import + custom field mapping | 90 min |
| 2. Build the `email_tier` → `{first_name_or_there}` logic (named → extract first name; role/generic → "there") | n8n function node OR Instantly custom field formula | 30 min |
| 3. Build the `postcode` → `{location_area}` lookup table (start with top 30 London postcodes covering the lead list) | Google Sheet + n8n lookup OR Instantly snippet library | 60 min |
| 4. Build the `category` → `{category_phrase}` parser (top 20 most common category strings in the lead engine output) | n8n function node | 60 min |
| 5. Encode-clean the email data (strip `u003e`, `%20`, other URL-encoded artefacts before sending) | n8n cleanup node | 30 min |
| 6. Set up Instantly templates with the merge variables exactly as named in this file | Instantly UI | 60 min |
| 7. Run end-to-end test on 10 sample leads from the CSV, inspect rendered emails | Manual | 60 min |
| 8. Set up the weekly random-sample audit reminder (Mondays 9am, pull 5 random sent emails from Instantly outbox) | Calendar | 5 min |

### Data quality issues observed in the sample CSV (TODO list for Lead Engine)

These are bugs in the lead engine output that should be fixed at source. Workarounds applied at the Instantly merge layer as a safety net, but the real fix is upstream.

1. **URL-encoded artefacts in some emails.** Examples:
   - `u003ehello@libertinelondon.co.uk` (should be `hello@libertinelondon.co.uk`)
   - `%20info@rowleys.co.uk` (should be `info@rowleys.co.uk`)
   - `nfo@sangennaro.co.uk` (missing leading "i", should be `info@sangennaro.co.uk`)
2. **Encoding corruption in some business names.** Non-ASCII characters not properly decoded:
   - `Crystal China å³ç¼` (intended Chinese characters lost in encoding)
   - `Andromeda Greek Restaurant ð¬ð·` (Greek flag emoji corrupted)
   - `Eliâs Restaurant` (apostrophe rendered as `â`)
3. **Some "named" emails are department aliases, not real names.** Examples:
   - `events@`, `bookings@`, `reservations@`, `info@` — these should be `email_tier = "role"`, not "named"
   - Currently mis-classified in some rows. Affects `{first_name_or_there}` resolution if not corrected.

**Recommendation:** Fix encoding + email_tier classification in the Lead Engine. Until then, the n8n cleanup node strips artefacts and the `email_tier` logic falls back to "there" if local-part doesn't look like a name (e.g., contains "info", "events", "bookings", "reservations", "contact", "hello", "press", "admin", "sales", "marketing").

### Lead enrichment opportunities (future, not in this build)

The Lead Engine has more fields than the current templates use. Future enhancements:

- **Phone number** (`phone_e164`) — could power SMS follow-up if compliance and consent allow
- **Coordinates** (`latitude`/`longitude`) — could segment by London zones (central / inner / outer) for tier-targeted messaging
- **Multiple category tags** — could trigger different templates for combined-type businesses (e.g., restaurant + bar + cocktail lounge)
- **Multiple emails per business** (`all_emails`) — could try named email first, fall back to role/generic if no engagement after Step 3

These belong to a Phase 2 build after the basic flow is working.

### Email tier prioritisation (recommended for queue ordering)

Send order priority in Instantly:

1. **`email_tier = "named"`** highest priority (real human first name extractable). Higher reply rate expected.
2. **`email_tier = "role"`** medium priority (`reservations@`, `bookings@`). Functional but less personal.
3. **`email_tier = "generic"`** lowest priority (`info@`). Often filtered or ignored. Worth sending but expect lower open rates.

This means: for a batch of 200 leads, send the named ones first across the week, then role, then generic. Maximises early reply yield.

### How this scales

- 50 emails/day: handled entirely by the automation. Zero per-send work. 10 min/week audit.
- 100 emails/day: same architecture. No additional load on Zizi.
- 200 emails/day: same architecture. Increase audit sample to 10/week.
- 500+ emails/day: revisit architecture. Probably need warmup batching across multiple sending domains and IP rotation.

This is the path that makes the 70/day → 100/day goal in the 60-day plan actually achievable without hiring.

---

## Section 8 — Deployment checklist (after Hadi approval)

Order matters. Do not skip steps.

- [ ] Hadi reviews this entire file. Flags edits.
- [ ] Jodie applies edits.
- [ ] Migrate the approved final version into `outreach/message-library.md` as the new canonical, or update message-library.md to point here.
- [ ] Brief Zizi: walk her through Sections 1, 2, and 6 in a 30-minute call. She understands the new positioning, the banned phrases list, and the reply handler classification.
- [ ] Update Instantly templates with R-EMAIL-1, R-EMAIL-2, R-EMAIL-3 (and equivalents for dental, aesthetic, fitness).
- [ ] Paste new Workflow 2 prompt into the Claude API node in n8n. Test on 3 sample leads.
- [ ] Reset Zizi's outreach tracker structure if needed (segment column, step column, reply classification column).
- [ ] Run first batch of 10 new-positioning DMs + 10 new-positioning emails, mixed segments.
- [ ] Review reply rates after 7 days. If reply rate is up vs the old baseline (~5-8%), positioning is working. If flat or down, iterate.
- [ ] First kill condition check at 30 sends per segment.

---

## Section 9 — Risks I've flagged for you to push back on

1. **Click Voice is restaurants-only.** Other segments get Click+ as entry tier. This means dental/aesthetic/fitness cold leads see £790-£1,290 monthly, no £290 option. If reply rates in those segments are weak, the missing lower-price tier could be a factor.

2. **No subject line A/B variant set up.** Single subject line per email step. If open rates are weak in Instantly, we'll need variants. Worth setting up A/B testing on R-EMAIL-1 first (restaurants is the highest volume).

3. **The "founding cohort" framing repeats across every step 2 message.** If a lead sees multiple Step 2 messages from different segments (e.g., an aesthetic clinic owner also runs a restaurant), the framing will feel formulaic. Low probability but worth noting.

4. **Reply handlers assume Zizi classifies replies correctly.** A misclassified reply (e.g., reading hostility into a sharp but not hostile reply) could damage relationships. Consider monthly audit of reply classifications in the first 90 days.

5. **Workflow 2 generates Step 1 DMs only.** Step 2 and Step 3 remain manual by Zizi. If automation is desired for Step 2/3 later, that's a separate build.

---

**End of master draft. Awaiting Hadi review.**

Once approved, this becomes the canonical outreach playbook for Click AI Agency. Replaces prior templates.
