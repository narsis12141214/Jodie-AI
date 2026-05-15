# DM Outreach Scripts — Instagram (Manual, Zizi)

**Channel:** Instagram DMs
**Owner:** Zizi sends manually. Workflow 2 (n8n + Claude API) auto-generates Step 1 openers.
**Data source:** Instagram profile data (bio, recent posts, business observation)
**Status:** Master draft. AWAITING HADI REVIEW. Do not deploy until reviewed.

**Companion file:** `outreach-scripts-email.md` (cold email, Instantly + Lead Engine, automated)

---

## Section 1 — DM operating principles

### What every DM must do

1. **Personalised to a real observation.** Something specific from the prospect's Instagram (recent post, bio detail, current promotion). NOT a fake compliment.
2. **Outcome-led, not feature-led.** Lead with what changes for the buyer (more bookings, recovered missed calls, hours back).
3. **One question per message.** Yes/no or open, never both.
4. **Short.** Under 60 words per DM.
5. **Sourced where it counts.** When citing a stat, name the source.

### Banned phrases (zero exceptions, audit before sending)

| Category | Banned |
|---|---|
| Chase language | "just checking in", "no rush", "totally understand if you're busy", "whenever you're ready", "happy to jump on a call", "sorry to bother you", "did you get my message?" |
| Generic compliments | "love that", "great that", "impressive that", "rare to see", "good to see", "amazing work" |
| Free / trial misuse | "free trial", "free audit" — say "14-day trial" instead |
| Jargon | "AI-powered", "cutting-edge", "revolutionary", "synergy", "leverage", "NLP", "machine learning" |
| Punctuation | NO em dashes anywhere — ever. Use commas, full stops, or new sentences. |

### Manual quality gate (Zizi runs per DM before sending)

- [ ] Personalised observation is real and specific (not template-able)
- [ ] No banned phrases
- [ ] One question, not two
- [ ] Under 60 words
- [ ] No em dashes
- [ ] Variable placeholders all filled
- [ ] If a stat is included, source is named

DMs are slow-throughput, manual-channel work. Per-send check is appropriate.

### Channel rhythm

| Step | Trigger | Action |
|---|---|---|
| Step 1 | First touch | Opener |
| Step 2 | 4 days no reply to Step 1 | Value follow-up |
| Step 3 | 5 days no reply to Step 2 | Final touch / clean exit |
| Archive | 7 days no reply to Step 3 | Move to dead pipeline. Do not contact further. |

**Total max touches per cold DM lead: 3.**

---

## Section 2 — Restaurants and Cafes

### Positioning angle

Lead with missed booking revenue. Use Hostie AI 43% revenue leak as the credibility stat. Click Voice (£290/month) is the entry-level offer for this segment specifically.

**Avoid:** Competing against $299 SaaS voice tools on price. Frame against doing nothing OR hiring a part-time receptionist.

**Personalisation variables (Zizi fills from Instagram profile):**
- `{first_name}` — owner's first name
- `{restaurant_name}` — exact spelling
- `{cuisine_or_concept}` — "Persian", "Italian", "neighbourhood cafe"
- `{location}` — "West Hampstead", "Soho", "Notting Hill"
- `{observation}` — one specific real detail (recent dish post, anniversary, opening hours mention)

---

### 🍽️ R-DM-1 — Restaurants Instagram DM Step 1 (Opener)

**Send when:** First touch
**Next step:** No reply after 4 days → R-DM-2
**Word count:** ~40

```
Hey {first_name}, saw your post about {observation} at {restaurant_name}.
Quick question — how many calls a week do you reckon you miss when the floor's slammed? Most {cuisine_or_concept} spots in {location} lose 1 in 3, and most of those callers don't leave a message.
Curious what your number looks like.
```

### 🍽️ R-DM-2 — Restaurants Instagram DM Step 2 (Value)

**Send when:** R-DM-1 sent + 4 days no reply
**Next step:** No reply after 5 days → R-DM-3
**Word count:** ~55

```
{first_name}, came across some data that surprised me. Hostie AI tracked UK restaurants losing up to 43% of inbound booking revenue to unanswered or abandoned calls. £292K recovered for a single restaurant in their case study.
We've just launched a voice agent built specifically for UK restaurants and cafes — £290/month, custom-built per venue. Want to see a 48-hour demo of how it'd sound for {restaurant_name}?
```

### 🍽️ R-DM-3 — Restaurants Instagram DM Step 3 (Final touch)

**Send when:** R-DM-2 sent + 5 days no reply
**Next step:** No reply after 7 days → archive
**Word count:** ~25

```
{first_name}, last one from me. If the timing's not right, totally fine. If it changes, you know where I am. Best with {restaurant_name}.
```

---

## Section 3 — Dental Practices

### Positioning angle

Lead with missed booking calls and lost new-patient LTV. Use Reach + Resonate AI stats. Recommend Click+ (£790/month) as standard. **Do NOT mention Click Voice — restricted to restaurants in v1.**

**Avoid:** Clinical claims, treatment recommendations.

**Personalisation variables:**
- `{first_name}` — owner or practice manager's first name
- `{practice_name}`
- `{location}`
- `{observation}` — recent new dentist join, new service launch, specific Google post
- `{specialism}` — "general dentistry", "cosmetic", "implants", "orthodontics"

---

### 🦷 D-DM-1 — Dental Instagram DM Step 1 (Opener)

**Send when:** First touch
**Next step:** No reply after 4 days → D-DM-2
**Word count:** ~45

```
Hey {first_name}, saw {observation} on the {practice_name} feed.
Quick one — Reach tracked UK dental practices missing roughly 32% of inbound calls, and 80% of those are booking requests. For a {specialism} practice that's a lot of new patients walking past.
How does that match your reception experience?
```

### 🦷 D-DM-2 — Dental Instagram DM Step 2 (Value)

**Send when:** D-DM-1 sent + 4 days no reply
**Next step:** No reply after 5 days → D-DM-3
**Word count:** ~55

```
{first_name}, follow-up. We run the AI receptionist for UK dental practices — voice, WhatsApp, recall sequences, integrated with Software of Excellence, Dentally, EXACT. Click+ at £790/month, full bundle.
We've just opened a founding cohort with setup at £150 instead of £500 (70% off). Want to see a 48-hour demo of how it'd answer for {practice_name}?
```

### 🦷 D-DM-3 — Dental Instagram DM Step 3 (Final touch)

**Send when:** D-DM-2 sent + 5 days no reply
**Next step:** No reply after 7 days → archive
**Word count:** ~25

```
{first_name}, last note. If the timing's wrong, no problem. If it changes, message me direct. Best with {practice_name}.
```

---

## Section 4 — Aesthetic Clinics

### Positioning angle

Lead with high-value missed enquiries. Use Xtreme Gen AI 30-42% missed calls + Boutique SEO £2,950+ LTV. Recommend Click Pro (£1,290/month). Reference Pabau and Phorest Medical integration explicitly. Regulatory framing baked in: AI books, does not prescribe.

**Avoid:** Clinical claims, treatment outcome promises.

**Personalisation variables:**
- `{first_name}` — owner, clinic manager, or lead practitioner's first name
- `{clinic_name}`
- `{location}`
- `{observation}` — recent treatment showcase, new prescriber join, specific clinic detail
- `{treatment_focus}` — "injectables", "advanced skin", "body contouring", "combined aesthetic"

---

### 💉 A-DM-1 — Aesthetic Clinics Instagram DM Step 1 (Opener)

**Send when:** First touch
**Next step:** No reply after 4 days → A-DM-2
**Word count:** ~50

```
Hey {first_name}, saw the {observation} on {clinic_name}'s feed.
Quick question — Xtreme Gen AI tracks UK aesthetic clinics missing 30-42% of inbound calls, and 85% of those callers don't call back. For a {treatment_focus} clinic, that's significant.
How does your missed-call rate compare? Most clinic managers don't know their actual number.
```

### 💉 A-DM-2 — Aesthetic Clinics Instagram DM Step 2 (Value)

**Send when:** A-DM-1 sent + 4 days no reply
**Next step:** No reply after 5 days → A-DM-3
**Word count:** ~60

```
{first_name}, follow-up. We run the AI receptionist for UK aesthetic clinics — integrates directly with Pabau and Phorest Medical. The agent books consultations only, never gives medical advice. Click Pro at £1,290/month, full bundle.
Founding cohort setup is £250 instead of £850 right now. Want to see a 48-hour demo of how it'd handle a Botox enquiry for {clinic_name}?
```

### 💉 A-DM-3 — Aesthetic Clinics Instagram DM Step 3 (Final touch)

**Send when:** A-DM-2 sent + 5 days no reply
**Next step:** No reply after 7 days → archive
**Word count:** ~25

```
{first_name}, last note. If now isn't the right time, that's fine. If it changes, message direct. Best with {clinic_name}.
```

---

## Section 5 — Gyms and Fitness Studios

### Positioning angle

Lead with lead leakage outside hours + retention math. Use GymMaster 33% cancellation reduction stat. Recommend Click+ (£790/month). Reference Mindbody/Glofox/TeamUp integration.

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
**Next step:** No reply after 4 days → F-DM-2
**Word count:** ~45

```
Hey {first_name}, saw the {observation} at {studio_name}.
Quick question — most {discipline} studios get 50-60% of new-member enquiries outside reception hours. Evenings, Sundays, that kind of thing. They miss most of them. Voicemail, unread DMs, the lot.
How are you handling that traffic currently?
```

### 🏋️ F-DM-2 — Fitness Instagram DM Step 2 (Value)

**Send when:** F-DM-1 sent + 4 days no reply
**Next step:** No reply after 5 days → F-DM-3
**Word count:** ~60

```
{first_name}, follow-up. GymMaster tracked something interesting — just 2 staff-member interactions per month reduces cancellation risk by 33%. The problem is those interactions never happen because no one has time.
We run the AI receptionist that captures every lead and runs retention sequences automatically. Click+ at £790/month, integrates with Mindbody, Glofox, TeamUp. Demo for {studio_name}?
```

### 🏋️ F-DM-3 — Fitness Instagram DM Step 3 (Final touch)

**Send when:** F-DM-2 sent + 5 days no reply
**Next step:** No reply after 7 days → archive
**Word count:** ~25

```
{first_name}, last note from me. If timing's off, no problem. If it changes, message direct. Best with {studio_name}.
```

---

## Section 6 — Reply handler library (DM)

When a lead replies, Zizi classifies the reply type and responds per the handler below.

### Handler 1 — Positive ("Tell me more")

```
Great, thanks {first_name}. Best way to do this is a short 30-minute call where I walk you through how it'd actually work for {business_name}, and we look at the numbers together. No pitch, no slide deck.

Two slots that work my end this week: {time_option_1} or {time_option_2}. Either of those, or suggest one that works better for you.
```

Zizi flags reply to Hadi same-day. Hadi takes the call.

### Handler 2 — Objection: "Too expensive"

```
Fair question {first_name}. Worth comparing against the right alternative — most {segment_type} owners hiring a part-time receptionist spend £1,500-£1,800/month for partial coverage. We're £290 to £1,290 depending on tier, with 24/7 cover and content production included from Click+ upward.

If you tell me what you're spending or considering spending, I can show you what changes when we run it instead. No pitch, just the maths.
```

Never drop price in the response. Surface what they're comparing against.

### Handler 3 — Objection: "Already have something"

```
Got it {first_name}, fair enough. Two quick questions while I'm here, and either is fine — what's working well with {current_solution}? And what would you change if you could?

Asking because we usually pick up clients who've tried a couple of solutions and want something more specific to {segment_type}. If yours is already nailed, no need to keep talking.
```

### Handler 4 — "Not now" / "Maybe later"

```
Totally fair {first_name}. Want me to come back to you in {30 / 60 / 90 days}, or is it more of a "not in the foreseeable future" kind of thing? Either's fine, just want to know whether to keep you on my list or not.
```

Force them to pick. Log specific return date in tracker.

### Handler 5 — Unsubscribe

```
Done. Removed from my list. Best with {business_name}.
```

Zizi removes from tracker same-day.

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

## Section 7 — Workflow 2 prompt (n8n + Claude API)

The Workflow 2 in n8n generates Step 1 DM openers automatically via Claude Haiku from Instagram profile data. Below is the updated prompt to paste into the Claude node in n8n.

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

## Section 8 — DM deployment checklist (after Hadi approval)

- [ ] Hadi reviews this file. Flags edits.
- [ ] Jodie applies edits.
- [ ] Brief Zizi: walk through Sections 1 and 6 in a 30-minute call. She understands new positioning, banned phrases, and reply handler classification.
- [ ] Paste new Workflow 2 prompt into the Claude API node in n8n. Test on 3 sample leads.
- [ ] Reset Zizi's outreach tracker structure if needed (segment column, step column, reply classification column).
- [ ] Run first batch of 10 new-positioning DMs across mixed segments.
- [ ] Review DM reply rates after 7 days vs old baseline (~5-8%).
- [ ] First kill condition check at 30 DMs per segment.

---

## Section 9 — DM risks flagged for pushback

1. **Step 1 has no price/tier.** Lead is curious or not by end of Step 1. If they ask "what does it cost?" before Step 2, Zizi answers honestly with the tier they should consider for their segment, then converts to Step 2 in the next message.

2. **{observation} requires real human eye.** Zizi must pull a genuine observation from each prospect's Instagram. Workflow 2 helps with Step 1 only. Steps 2 and 3 stay manual.

3. **Instagram DM volume is capped by Zizi's manual capacity.** Realistic ceiling ~30-50 DMs/day. To hit higher volumes, email channel must do the heavy lifting (see companion file `outreach-scripts-email.md`).

4. **Reply handlers assume Zizi classifies correctly.** Misclassification risk. Monthly audit recommended in first 90 days.

5. **No A/B testing built in.** Single template per step per segment. If reply rates lag for a specific segment, we'd iterate on Step 1 before adding variants.

---

**End of DM scripts file. Awaiting Hadi review.**
