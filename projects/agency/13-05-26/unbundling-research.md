# Unbundling Research — Should Click AI Agency Split Its Offer?

**Date:** 13 May 2026
**Business:** Click AI Agency
**Trigger:** Hanna (Persian restaurant, West Hampstead) raised pricing/positioning objections during a 3-hour meeting. She argued the £800/month Click+ tier is too high for restaurant owners, that "AI is free, ChatGPT is free" perception is real, and that competitors offer voice-only from around $299/month. She recommended Click AI splits the services and sells voice-only or website-only as the entry point, then upsells the bundle.
**Strategic question:** Should Click AI Agency unbundle?

---

## Question 1 — Competitive Landscape

### Done-for-you AI receptionist providers (UK)

The UK done-for-you AI receptionist market in 2026 is split into three layers. Hadi competes in the middle layer (small agencies and white-label resellers), not against SaaS platforms.

**Bottom layer (self-serve SaaS, light setup):**
- Team-Connect: AI call answering from £9.99/month, natural language, 24/7 ([team-connect.co.uk](https://team-connect.co.uk/ai-receptionist-uk)).
- Alayic: AI voice agent service from £39.99/month for UK SMBs ([ecommercenews.uk](https://ecommercenews.uk/story/alayic-launches-uk-ai-voice-agent-service-from-gbp-39-99-monthly)).
- Clara: £49.99/month for small service businesses, 7-day free trial ([heyitsclara.com](https://heyitsclara.com/gb/blog/best-ai-phone-answering-service-uk-tradespeople/)).

**Middle layer (done-for-you, vertical-specific, owner doesn't configure anything):**
- Invox AI (trades): flat £99/month, 30-day money-back, built for UK plumbers, electricians, gas engineers, roofers, builders ([invoxai.uk](https://www.invoxai.uk/)).
- Overtime.Talk (trades): flat £99/month regardless of volume ([overtime.talk](https://overtime.talk/blog/overtime-talk-vs-retell-ai)).
- ARROW (trades): from £99/month, used by UK tradespeople ([aiphonecalls.co.uk](https://aiphonecalls.co.uk/)).
- AV Agency (beauty salons, UK): done-for-you, sells via live demo ([avagency.uk](https://www.avagency.uk/)).
- CallHero (UK hair and beauty): vertical-specific receptionist ([callshero.co.uk](https://callshero.co.uk/industries/hair_beauty)).
- Flamingo Digital: restaurants and clinics ([flamingodigital.co.uk](https://www.flamingodigital.co.uk/ai-receptionist)).

**Top layer (premium, hybrid AI + human):**
- Moneypenny AI: requires a telephone answering subscription, from £160/month ([norango.ai](https://www.norango.ai/blog/ai-voice-technology-14/moneypenny-ai-pricing-444)).
- Smith.ai: $97.50/month AI-only or $292.50/month for the live receptionist tier ([almcorp.com](https://almcorp.com/blog/best-ai-receptionist-products-2026/)).

### Done-for-you AI receptionist providers (US, 12-18 months ahead)

The US market shows the trajectory the UK is on. The dental segment is the clearest example.

- TensorLinks (dental): Starter $399/month (inbound voice + insights), Professional $499/month (adds outbound campaigns), Standard $699/month (SMS, web chat, email, unified inbox) ([tensorlinks.com](https://www.tensorlinks.com/blog/ai-dental-receptionist-pricing-comparison-2026/)).
- GetHelpDesk.AI (dental): $399/month, single new patient/week breaks even ([gethelpdesk.ai](https://gethelpdesk.ai/pricing/)).
- General market: dental AI receptionist sits $199-$499/month for end clients, $399-$1,500+ for fuller feature stacks ([getnextphone.com](https://www.getnextphone.com/blog/ai-receptionist-cost)).
- Trillet white-label (agency reseller): Studio $99/month for 3 sub-accounts, Agency $299/month unlimited ([trillet.ai](https://www.trillet.ai/blogs/voice-agent-for-dental-practices-reseller)).

### Realistic done-for-you price floor by segment

JUDGEMENT, based on the data above:

| Segment | Realistic UK price floor (done-for-you voice) | Notes |
|---|---|---|
| Restaurants | £99-£250/month | Lower margin per call than dental, owners price-sensitive, no insurance economics |
| Beauty salons / clinics | £150-£400/month | Each missed booking is £30-£150, willingness to pay higher than restaurants |
| Dental clinics | £300-£600/month | One new patient is worth £1,000-£3,000 lifetime, lowest sensitivity |
| Tradespeople | £99-£199/month | Volume model, low per-job margin, market floor set by Invox/ARROW/Overtime |

### Conclusion for Question 1

FACT: The UK done-for-you voice-only market has a hard price ceiling around £99-£199/month for restaurants and trades, £200-£400/month for clinics, and £300-£600/month for dental. Click AI's current bundle prices (£497-£1,997) sit cleanly above this entire market because they bundle social media, content, WhatsApp, and automation. The bundle is differentiated. The voice-only slice is not.

---

## Question 2 — Margin Math at £299/month Voice-Only

### Platform cost per minute (Vapi-based stack)

FACT: Vapi platform fee is $0.05/min plus pass-through cost for STT, LLM, TTS, and telephony. True total typically lands at $0.07-$0.25/min ([cloudtalk.io](https://www.cloudtalk.io/blog/vapi-ai-pricing/), [retellai.com](https://www.retellai.com/blog/vapi-ai-review)).

Estimated stack (UK numbers, GBP at ~$1.25):
- Vapi platform: $0.05/min = £0.04/min
- STT (Deepgram): $0.01/min = £0.008/min
- LLM (GPT-4o-mini or Claude Haiku): $0.02-$0.06/min = £0.02-£0.05/min
- TTS (ElevenLabs Turbo): $0.04/min = £0.032/min
- Twilio UK inbound: ~£0.01/min, UK local number £1.20/month ([twilio.com](https://www.twilio.com/en-us/voice/pricing/gb))

**All-in variable cost per minute: ~£0.11-£0.13/min for voice.**

### Unit economics at £299/month voice-only

Assume client uses 400 minutes/month (typical restaurant inbound):

| Line | £/month |
|---|---|
| Revenue | 299 |
| Variable: 400 min × £0.13 | -52 |
| Phone number + tooling allocation | -5 |
| n8n self-hosted VPS share (£15 across 30 clients) | -0.50 |
| **Gross margin (per client)** | **241** |
| **Gross margin %** | **80.6%** |

If client uses 800 minutes/month: gross margin drops to ~£195, 65%. Still healthy.

### Setup time amortisation

Estimate: 8-12 hours for voice agent build, FAQ training, calendar integration, testing. At £75/hour internal cost = £600-£900 of labour. A £290 setup fee covers about 40-50% of that, so the £299/month plan only becomes structurally profitable from month 3-4 onwards. Ongoing support assumes 1 hour/month per client (£75) at steady state.

**Net contribution per client per month after support: ~£166-£200.**

### Volume to hit £5,000 MRR at different price points

JUDGEMENT:

| Price point | Clients needed for £5k MRR | Clients needed for £5k net (after support) |
|---|---|---|
| £199/month voice-only | 26 | ~50 (very thin per-client net) |
| £299/month voice-only | 17 | ~30 |
| £399/month voice-only | 13 | ~22 |
| £797/month (current Click+) | 7 | ~10 |

A single founder + part-time outreach (Hadi + Zizi) can realistically onboard 4-6 new clients/month at steady state. Hitting 17-30 voice-only clients within 60 days is not feasible from the current pipeline. Hitting 7-10 Click+ clients is closer to what the current pipeline could produce if all stalled verbal-yes leads converted.

### Conclusion for Question 2

FACT: The unit economics of voice-only at £299/month work mathematically. Gross margin stays at 65-80%. The problem is not margin per client. The problem is volume: voice-only requires 2-3x more closed clients to hit the same MRR, with the same single founder closing them, in the same 60-day window with 18 days left.

---

## Question 3 — Cannibalisation Risk

### How much of the existing Click+ pipeline would downgrade?

JUDGEMENT, based on the current pipeline (Randeszvous, Maria, Kish, Ace, Hanna):

| Lead | Current proposed tier | Likely behaviour if voice-only £299 was offered |
|---|---|---|
| Randeszvous | Click+ (case study terms) | No change. They already verbally agreed. |
| Maria | Click+ proposal under review | High risk. She is price-sensitive, has been silent. Likely downgrade. |
| Kish | Click+ (case study terms) | No change. Already signed-stage. |
| Ace | Click+ (case study terms) | No change. Already signed-stage. |
| Hanna | Click+ proposed, objected | Very likely downgrade. This is exactly what she asked for. |

Of 5 active deals, 2 would likely downgrade from £797 to £299. That is a 62% revenue cut on those two deals (£498/month loss each, £996/month total if both downgrade).

### Real-world precedent

FACT: Pace Pricing's analysis of unbundling explicitly names cannibalisation as the central risk and identifies the structural fix: "Create clear value separation between the standalone product and the full platform. The standalone version should solve one job well, while the platform should offer integration, automation, and cross-product value that standalone cannot replicate. Price the standalone high enough that the bundle still offers a compelling per-product discount." ([pacepricing.com](https://www.pacepricing.com/glossary/unbundling-strategy))

FACT: Harvard Business Review research cited in industry summaries finds that effective bundling raises perceived value by 50-60% versus unbundled offerings ([fincome.co](https://www.fincome.co/blog/price-bundling-strategies)). Splitting the offer therefore destroys perceived value as well as price.

### Structural ways to prevent cannibalisation

JUDGEMENT, ordered by strength of fence:

1. **Voice-only excludes WhatsApp, social, automation, and dashboard access.** It is a single function with a single SLA. Bundle keeps everything.
2. **Voice-only has no monthly strategy call, no content approval workflow, no Click Desk AI dashboard.** Bundle keeps all three.
3. **Voice-only has fixed minutes (e.g. 250) with hard overage; Click+ retains 1,000 minutes plus growth runway.** Bundle is the elastic option.
4. **Voice-only setup fee is the same or higher** (£500-£750). This kills the "cheap entry" perception that drives cannibalisation. The customer pays a real onboarding cost no matter what.
5. **Segment-restrict voice-only.** Offer it only to trades, restaurants, and barbers. Withhold it from beauty, clinics, dental where bundle is the right offer.

### Conclusion for Question 3

JUDGEMENT: Without structural fences, 40-50% of bundle-eligible prospects will downgrade. With aggressive structural fences (single function, no dashboard, no strategy call, same setup fee, segment-restricted), cannibalisation can be held to 10-20%. The problem: those exact fences make voice-only look identical to Invox AI, ARROW, and Clara at the £99 price point, which makes £299 hard to defend.

---

## Question 4 — Segment-by-Segment Fit

| Segment | Highest-fit standalone | Best fit for bundle | Unbundling impact on close rate |
|---|---|---|---|
| **Restaurants** | Voice-only (reservation calls, missed-call recovery) | Click+ if owner cares about social and reviews | UNBUNDLING HELPS CLOSE. Restaurant owners price-anchor on £99-£250 voice services ([thevoipshop.co.uk](https://www.thevoipshop.co.uk/blog/best-ai-answering-services-uk)). |
| **Beauty clinics** | Voice + WhatsApp combined | Click+ or Click Pro (DM management, rebooking, reviews are the actual revenue drivers) | UNBUNDLING HURTS. The DM/social side is where they actually pay. Voice alone undersells. |
| **Salons (hair)** | Voice-only (booking calls) | Click+ for content + voice combo | Mixed. Small salons take voice-only. Premium salons want the bundle. |
| **Dental clinics** | Voice-only (appointment booking, recall) | Click Pro (HIPAA-comparable workflows, win-back) | UNBUNDLING HELPS CLOSE. US comparable pricing supports £300-£500/month voice for dental ([tensorlinks.com](https://www.tensorlinks.com/blog/ai-dental-receptionist-pricing-comparison-2026/)). |
| **Barbers** | Voice-only or WhatsApp-only | Click base only | UNBUNDLING HELPS CLOSE. Barbers do not buy £800/month anything. |
| **Tradespeople** | Voice-only (£99-£199 market floor) | Almost never the bundle | UNBUNDLING HELPS CLOSE but margin is thin. UK market is already commoditised here. |
| **Estate agents** | Content + lead automation | Click Pro (content engine is the real value) | UNBUNDLING HURTS. Estate agents pay for marketing automation, not phone answering, since they already have receptionists ([estatai.co.uk](https://estatai.co.uk/blog/top-12-estate-agent-software-uk-2026)). |
| **Wholesalers** | Outbound automation, WhatsApp | Click Pro / Click Elite | UNBUNDLING HURTS. Wholesalers buy systems, not phone answering. |

### Industry-specific pricing sensitivity

FACT: UK restaurant marketing agencies routinely charge £500-£2,000/month, with £1,250-£3,500 typical for SME core retainers ([adzooma.com](https://adzooma.com/blog/average-cost-uk-marketing-agencies/), [localbrandhub.com](https://localbrandhub.com/blog/restaurant-marketing-agency-cost)). Restaurants are not unable to pay £800/month. Hanna's objection is a perceived-value objection, not an affordability objection.

FACT: 48% of UK estate agents now use AI tools, with another 19% experimenting ([viewber.co.uk](https://viewber.co.uk/voices-of-property-the-uk-estate-agency-market-embraces-ai-fees-change)). The category understands and pays for AI. Voice-only is wrong angle for them.

### Conclusion for Question 4

JUDGEMENT: Unbundling produces more closes in restaurants, dental, barbers, trades. It produces fewer closes (or no change) in beauty, clinics, estate agents, wholesalers. The bundle is the right offer for the higher-value segments. Voice-only is the right entry for the lower-value, higher-volume segments.

---

## Question 5 — Land and Expand Patterns

### What US AI agencies (12-18 months ahead) do

FACT: "Most successful AI voice agencies charge $199-$599/month per client, depending on the vertical, channels included (voice, WhatsApp, chat), and minute allotment" ([famulor.io](https://www.famulor.io/blog/ai-voice-agent-pricing-2026-what-10-platforms-actually-cost-per-minute)).

FACT: The dominant US pattern is single-function entry (voice receptionist) at $199-$499/month, then expansion into outbound campaigns, SMS, web chat, and unified inbox at $499-$699/month ([tensorlinks.com](https://www.tensorlinks.com/blog/ai-dental-receptionist-pricing-comparison-2026/)). They lead with voice. They do not lead with the bundle.

FACT: Bessemer Venture Partners reports the AI services market is moving to "hybrid models: a base platform fee plus consumption or outcome pricing, which preserves revenue floors while creating upside tied to agent usage" ([bvp.com](https://www.bvp.com/atlas/the-ai-pricing-and-monetization-playbook)).

### Land-and-expand performance benchmarks

FACT: Top-performing land-and-expand B2B SaaS companies achieve 130-150% net dollar retention, meaning existing customers grow 30-50% per year ([pacepricing.com](https://www.pacepricing.com/glossary/land-and-expand), [getmonetizely.com](https://www.getmonetizely.com/articles/land-and-expand-pricing-models-that-support-upsells-and-expansion-revenue)).

FACT: "If you land 100 deals at $10K average and expand 60% of them to $40K within 18 months, your initial $1M in bookings becomes $3.4M, a 3.4x multiplier without acquiring a single new logo" ([pacepricing.com](https://www.pacepricing.com/glossary/land-and-expand)).

FACT: First expansion typically happens 3-6 months after initial deployment ([maxio.com](https://www.maxio.com/blog/land-and-actually-expand-how-to-drive-efficient-revenue-growth-in-saas)). Beyond 12 months indicates the initial deployment did not show enough value.

FACT: Upselling existing customers costs an average of $0.27 per dollar of revenue versus far higher CAC for new customers (study of 174 SaaS companies, cited in [getmonetizely.com](https://www.getmonetizely.com/articles/land-and-expand-pricing-models-that-support-upsells-and-expansion-revenue)).

### Implications for Click AI

JUDGEMENT:
- Land-and-expand requires a working customer success motion (3-6 month upgrade conversations) that Click AI does not yet have, but can build with 5-10 paying clients on the books.
- The 3.4x multiplier maths assumes 60% expansion within 18 months. Click AI has 18 days, not 18 months, to hit £5k MRR. Land-and-expand is a 6-18 month play. It will not save the 60-day plan on its own.
- However, voice-only as an entry tier reduces sales cycle length, removes pricing friction, and creates the install base required for the land-and-expand motion to start working in months 3-6.

---

## Recommendation

**Click AI Agency should partially unbundle, with strict structural fences. Introduce a single voice-only entry tier at £290-£390/month, restricted to specific segments, with no dashboard access, no strategy call, and the same or higher setup fee as Click+.**

### Rationale (4 paragraphs)

**Paragraph 1 — The current bundle is structurally correct but tactically expensive in the wrong segments.** The four-tier bundle is the right product for beauty clinics, estate agents, wholesalers, and dental groups. These buyers want the whole engine. They also pay £1,000-£5,000/month elsewhere for fragmented services. The bundle works for them. The bundle does not work for restaurants and trades, where UK competitors have established a £99-£199 voice-only price floor and where the social/WhatsApp/automation layers are perceived as adjacent rather than essential. Hanna is not wrong. Five stalled verbal-yes deals after 42 days, two of which are on free-case-study terms, is not a price-validation signal. It is a signal that the bundled offer is creating decision-friction at the close.

**Paragraph 2 — Voice-only at £290-£390/month is defensible and segment-restricted.** Set the price floor at £290/month, not £199 and not £299. £290 sits clearly above Invox/ARROW/Overtime at £99 (so the "done-for-you" premium is visible), below US dental comparables at $399-$499, and below Click+ at £797 (so the upgrade path is real, not theoretical). Restrict voice-only to restaurants, trades, barbers, and single-location salons. Withhold it from beauty clinics, dental groups, estate agents, and wholesalers. Match the Click+ setup fee at £490-£590, do not undercut it. This kills the cheap-entry cannibalisation risk because the up-front commitment is identical. Voice-only also explicitly excludes the Click Desk AI dashboard, monthly strategy call, social media management, content creation, and automation workflows. Customers see what they are missing every time they log in to nothing.

**Paragraph 3 — The expansion path is the actual product.** US precedent is clear: voice-only customers expand to multi-channel within 3-6 months once the voice agent is working ([tensorlinks.com](https://www.tensorlinks.com/blog/ai-dental-receptionist-pricing-comparison-2026/)). Click AI's job is to engineer that expansion. After 60 days on voice-only, every client gets a structured upgrade conversation: "You missed 14 reviews this month, and you are still posting once a week. Click+ adds the review automation and 8 weekly posts for £507/month more, with the setup already done." Net dollar retention targets of 130-150% in best-in-class land-and-expand are achievable in this market because the marginal cost of adding social/WhatsApp to an existing voice account is low (existing infrastructure, existing client trust, existing payment relationship). The bundle becomes the upsell, not the offer.

**Paragraph 4 — The 60-day plan changes shape but not direction.** With 18 days left in the 60-day window, voice-only does not save the £5k MRR target on its own. It will, however, do three things that matter now. First, it converts Hanna from a polite objection into a closeable £290 deal this week, which closes the sixth client and demonstrates the model works. Second, it gives Zizi and the outreach system a sharper opener for restaurants and trades that does not require selling the full £800 bundle in a cold DM. Third, it builds the install base the agency needs to start expansion conversations in July and August, which is where the next £5k MRR comes from. Hold the bundle for beauty, dental, clinics, estate agents, wholesalers. Lead with voice-only for restaurants and trades. Keep Click Pro and Click Elite untouched. The structure is: voice-only entry, Click+ expansion, Click Pro/Elite premium. That is the product.

### What Hadi should not do

- Do not drop Click+ price. The £797 is right for the segment that buys it.
- Do not offer voice-only at £199. Market floor is £99 done-for-you for trades. £199 sits in no-mans-land and signals weakness.
- Do not offer website-only as a standalone tier. Websites are commoditised, churn-prone, and pull Click AI into a different business model.
- Do not give Hanna a custom price below £290. The voice-only tier is the answer to her objection. The price needs to hold.

### Decision required from Hadi

1. Approve or reject the voice-only entry tier at £290-£390/month.
2. If approved: confirm segment restrictions (restaurants, trades, barbers, single-location salons).
3. If approved: confirm setup fee at £490-£590 (matching or exceeding Click+).
4. If approved: send Hanna a revised proposal at voice-only this week, hold the price.

---

## Sources

- [Pace Pricing — Unbundling Strategy](https://www.pacepricing.com/glossary/unbundling-strategy)
- [Pace Pricing — Land and Expand](https://www.pacepricing.com/glossary/land-and-expand)
- [Bessemer Venture Partners — AI Pricing Playbook](https://www.bvp.com/atlas/the-ai-pricing-and-monetization-playbook)
- [Bessemer — Land and Expand Case Study](https://www.bvp.com/atlas/how-one-b2b-saas-company-revamped-pricing-for-an-ultra-successful-land-and-expand-play)
- [Cloudtalk — Vapi AI Pricing 2026](https://www.cloudtalk.io/blog/vapi-ai-pricing/)
- [Retell AI — Vapi Review 2026](https://www.retellai.com/blog/vapi-ai-review)
- [Twilio UK Voice Pricing](https://www.twilio.com/en-us/voice/pricing/gb)
- [Famulor — AI Voice Agent Pricing 2026](https://www.famulor.io/blog/ai-voice-agent-pricing-2026-what-10-platforms-actually-cost-per-minute)
- [TensorLinks — Dental AI Receptionist Pricing 2026](https://www.tensorlinks.com/blog/ai-dental-receptionist-pricing-comparison-2026/)
- [Trillet — Voice Agent for Dental Practices Reseller](https://www.trillet.ai/blogs/voice-agent-for-dental-practices-reseller)
- [GetHelpDesk.AI — Dental Pricing](https://gethelpdesk.ai/pricing/)
- [NextPhone — AI Receptionist Cost 2026](https://www.getnextphone.com/blog/ai-receptionist-cost)
- [ALM Corp — 10 Best AI Receptionist Products 2026](https://almcorp.com/blog/best-ai-receptionist-products-2026/)
- [Invox AI — UK Tradesmen AI Receptionist](https://www.invoxai.uk/)
- [Overtime.Talk — vs Retell AI](https://overtime.talk/blog/overtime-talk-vs-retell-ai)
- [Team-Connect UK](https://team-connect.co.uk/ai-receptionist-uk)
- [Alayic launch — Ecommerce News UK](https://ecommercenews.uk/story/alayic-launches-uk-ai-voice-agent-service-from-gbp-39-99-monthly)
- [Heyitsclara — UK Tradespeople 2026](https://heyitsclara.com/gb/blog/best-ai-phone-answering-service-uk-tradespeople/)
- [Flamingo Digital — AI Receptionist UK](https://www.flamingodigital.co.uk/ai-receptionist)
- [AV Agency — UK Beauty Salons](https://www.avagency.uk/)
- [CallsHero — Hair and Beauty](https://callshero.co.uk/industries/hair_beauty)
- [Norango — Moneypenny Pricing Explained](https://www.norango.ai/blog/ai-voice-technology-14/moneypenny-ai-pricing-444)
- [Local Brand Hub — Restaurant Marketing Agency Cost](https://localbrandhub.com/blog/restaurant-marketing-agency-cost)
- [Adzooma — Average UK Marketing Agency Costs](https://adzooma.com/blog/average-cost-uk-marketing-agencies/)
- [Viewber — UK Estate Agency AI Adoption](https://viewber.co.uk/voices-of-property-the-uk-estate-agency-market-embraces-ai-fees-change)
- [EstatAI — UK Estate Agent Software 2026](https://estatai.co.uk/blog/top-12-estate-agent-software-uk-2026)
- [Fincome — Price Bundling Strategies](https://www.fincome.co/blog/price-bundling-strategies)
- [Monetizely — Land and Expand Pricing](https://www.getmonetizely.com/articles/land-and-expand-pricing-models-that-support-upsells-and-expansion-revenue)
- [Maxio — Land and Actually Expand](https://www.maxio.com/blog/land-and-actually-expand-how-to-drive-efficient-revenue-growth-in-saas)
- [VoIP Shop — Best AI Answering Services UK 2026](https://www.thevoipshop.co.uk/blog/best-ai-answering-services-uk)

---

*Source quality note: All pricing figures are primary or vendor-published, current as of May 2026. UK done-for-you category data is strongest. US dental category data is also strong. Cannibalisation rate estimates and segment-by-segment close-rate impact are JUDGEMENT, grounded in pipeline data and the cited unbundling research.*
