# Uber Direct UK — Platform Partner Brief for Click AI Agency

**Prepared:** 15 June 2026 | **Read time:** ~15 min | **Sources flagged stale where >12 months old**

---

## 1. Uber Direct UK partner program — current state

Uber Direct operates **two distinct integration tracks**, and the distinction matters for Click:

**Track A — Direct merchant API access.** Any single merchant can sign up for a Uber Direct account at `direct.uber.com` and use the API to fulfil their own deliveries. No partner status required. This is what Kish or Galleria would do if they integrated alone.

**Track B — Integration Partner / Platform Partner program.** A formal track for SaaS platforms (POS, ordering, ops, KDS) that resell or embed Uber Direct to multiple merchants. Uber states it has **"100+ integration partners globally"** and all of them **"go through a technical certification process"** before being listed on the public partner directory. (Uber Eats UK integration partners: https://merchants.ubereats.com/gb/en/integration-partners/, US integration partners — Direct: https://merchants.ubereats.com/us/en/integration-partners/direct/)

**What Track B partners get that solo merchants do not (confirmed):**
- Listing on the public Uber Direct integration partners directory (lead-gen channel)
- Technical certification stamp (trust signal in sales conversations)
- A two-way certified integration (orders flow back into the partner's order management/POS rather than sitting in a separate Uber dashboard)

**What is NOT publicly confirmed for the UK partner track:**
- Preferential per-delivery pricing
- Revenue share to the platform
- White-label rights beyond the standard merchant-facing white-label (Uber Direct is already a white-label product at the merchant level — the courier and tracking can be branded by the merchant)
- Dedicated UK partnerships rep

These almost certainly exist but are negotiated privately. Treat them as **TBC until a call with the partnerships team**.

**UK-facing pages:**
- https://merchants.ubereats.com/gb/en/services/uber-direct/ — UK product page (confirms 20+ countries, "90%+ of UK population" coverage, per-delivery pricing only, no startup/commission/minimum)
- https://merchants.ubereats.com/gb/en/integration-partners/ — UK partner directory

---

## 2. Application path

**There is no public "apply to be a platform partner" form for the UK.** Confirmed by checking the UK contact page, the partner directory, and the global integration-partner pages — none surface a partner application URL. The route is via the UK merchant team, then internal routing to partnerships/BD.

**Best-known UK contacts** (from https://merchants.ubereats.com/gb/en/contact-us/):
- `ukirestaurants@uber.com` — small/medium UK restaurants team (best first touch given Click's client base)
- `ukieats-support@uber.com` — Strategic & Enterprise UK restaurants
- `merchant-uki@uber.com` — non-restaurant UK merchants
- `uki-onboarding@uber.com` — onboarding
- `pr@support-uber.com` — for "broader partnership outside merchant integrations" (per a global Uber support page; treat as secondary)

**Named role evidence:** Uber has run a "Client Partner, Enterprise — Uber Direct UK" role (listing previously visible via TheMuse, now 404 — stale signal but confirms the function exists). This sits inside Uber Direct's UK enterprise/partnerships team.

**Typical response time:** Not published. Industry norm for Uber merchant/partner inbound is 5–15 business days for first qualification, longer for partnership conversations.

**What Uber expects in an initial approach** (synthesised from the partner directory pattern — not officially published):
- One-page company overview (what you sell, to whom, in which UK regions)
- Current merchant count + 6/12-month merchant projections
- Use case (orders/month per merchant, average basket, current delivery solution if any)
- Technical readiness statement (in-house dev capacity, OMS architecture, multi-tenant model)
- Commercial ask (volume tier expected, any co-marketing interest)

---

## 3. Commercials (best-effort, partial confirmation)

**Publicly confirmed (UK):**
- **Per-delivery pricing only.** "No start-up costs, commissions or monthly minimums." (https://merchants.ubereats.com/gb/en/services/uber-direct/)
- Fees vary by **distance, speed (express / same-day / next-day / scheduled), order type, integration type, and region**. (https://www.uber.com/gb/en/b/courier-services/london-eng-gb/)
- Coverage: typically a 10-mile radius, up to 20+ on request. Weight <50 lb.

**Not published anywhere public:**
- Per-delivery £ figure for London. Uber publishes a **US rate-starting-point of $6.99/delivery** (https://merchants.uber.com/uber-direct.html) but does not publish a UK equivalent. Treat any UK £ number as **unconfirmed until quoted by Uber**. Stuart, the direct UK competitor, publishes **from £5.50/delivery** (https://softwarefinder.com/fleet-management-software/stuart) — useful as a competitive sanity-check.
- Platform partner discounts, revenue share, or pass-through pricing — **all unconfirmed publicly**. Industry norm in this space is volume-tiered pass-through with a revenue share triggered after a commit-spend threshold. Confirm in the partnership call, do not assume.

---

## 4. Technical scope

**Developer portal:** https://developer.uber.com/docs/deliveries/overview — public, no gate.

**Endpoints a platform integration must hit (confirmed from the public docs):**
- **Create Delivery** (`POST /eats/deliveries/orders` and Direct API v1 equivalent) — submit the delivery request. (https://developer.uber.com/docs/deliveries/direct/api/v1/post-eats-deliveries-orders)
- **Delivery quote** — price + ETA before commit (referenced in the API reference at https://developer.uber.com/docs/deliveries/api-reference/daas).
- **Webhooks** — `event.delivery_status`, `event.courier_update`, `event.refund_request`, `event.shopping_progress`. Configured in the Uber Direct Dashboard, authenticated via signed `x-uber-signature` (SHA-256 + signing key). (https://developer.uber.com/docs/deliveries/guides/webhooks)
- **Cancel Delivery** — covered in the reference.
- **Authentication** — OAuth, documented under Guides → Authentication.

**Multi-tenant / sub-merchant model:** **Not publicly documented.** The dev docs read as single-account by default. This is the single most important question to put to Uber's partnerships team — Click's whole model depends on one parent account fanning out to many merchant tenants with separate billing/reporting. Deliverect, Lightspeed, and Toast clearly do this in production, so the capability exists — but the contractual and technical mechanism for it is gated behind the partner conversation.

**Integration effort (estimate for a competent dev team):**
- Sandbox + first happy-path delivery: **3–5 days**
- Full Click Desk integration (quote → create → status webhook → cancel + refund handling + per-tenant config + dashboard surfacing): **2–4 weeks**
- Pilot with one live merchant before production: **+1–2 weeks** (Uber's docs explicitly describe a sandbox → pilot → production lifecycle)
- Technical certification for the public partner directory listing: **+2–6 weeks** depending on Uber's queue. **Not publicly time-bound.**

**Total realistic: 6–10 weeks from kickoff to certified, live, multi-merchant.**

**UK compliance / food handling:** Uber Direct is a logistics layer. **FSA registration, allergen handling, alcohol licensing, and packaging compliance sit with the merchant**, not Click and not Uber. No DBS requirements surface for the platform partner. Uber requires the merchant to confirm product category at signup (food, alcohol, pharma flag, etc.) and applies category-specific courier handling. Not detailed publicly — confirm in onboarding.

---

## 5. Competitive benchmarks

**UK SaaS platforms with publicly announced Uber Direct integrations:**

| Partner | Type | Notes |
|---|---|---|
| **Deliverect** | Order management / POS aggregator | UK partnership since 2018, Uber Direct integration added Sept 2023, extended to Ireland Sept 2025. Two-way integration. (https://www.deliverect.com/en-gb/integrations/uber-direct) |
| **Lightspeed** | Restaurant POS (K-Series) | UK-live. Marketed on margin control + courier dispatch from POS. (https://www.lightspeedhq.com/uk/integrations/uber-direct/) |
| **Toast** | POS | Multi-year global partnership expanded in 2024 to add Uber Direct; UK rollout 2026. (https://www.restaurantdive.com/news/uber-toast-enter-strategic-global-partnership/804484/) |
| **Square** | POS | Marketplace integration confirmed UK; Direct integration available in core markets. |
| **Flipdish, Slerp, Vita Mojo, OrderYoyo** | Ordering platforms | Not confirmed in this research. Worth a one-line check before applying — Uber lists 90+ partners globally and not all are surfaced via search. |

**Marketing language to model** (from Deliverect and Lightspeed UK pages): "Keep control of your margins." "Same-day local delivery, your brand." "No marketplace fee — pay per delivery." "Your customer, your data, our couriers."

**Competing UK delivery-aggregator partner programs Click should also evaluate:**

| Provider | One-line take |
|---|---|
| **Stuart** | UK-native, from **£5.50/delivery** (https://softwarefinder.com/fleet-management-software/stuart), 75+ partner integrations, API public, no meal commission. Strongest UK competitor to Uber Direct for platform plays. |
| **Just Eat Logistics (Scoober / JET Delivers)** | Closed program, harder to partner with as a SaaS. Skip unless a specific merchant asks. |
| **Gophr** | London-strong, API public, light partner program. Useful as a fallback / secondary. |
| **DoorDash Drive** | UK presence limited; not worth pursuing as primary. |
| **Pedivan / local couriers** | Hyperlocal, not API-first. Not platform-suitable. |

**Best move: Uber Direct primary, Stuart secondary.** Building Click Desk to abstract the courier layer (so a merchant can choose Uber Direct or Stuart per drop) is a strong technical hedge and a clear sales narrative.

---

## 6. Bottom line — recommended next move for Click AI Agency

**Recommendation: Apply now via the UK merchant team, but lead the conversation with platform-partner positioning, not single-merchant signup.**

Click has the only thing that matters in a partner pitch: **named merchants ready to onboard**. Two live (Kish, Haleh), one signed today (Galleria with delivery in scope from day one), Elan Cafe in talks, 5+ in pipeline. That's a credible 6–10 merchant Q3 projection. Uber's partner team takes inbound from much thinner stories.

**Concrete next 14 days:**

1. **Day 1–3 — Prep the 1-page partner deck.** Sections: who we are (Click AI Agency, UK Ltd, voice + Click Desk SaaS), current live merchants (Kish, Haleh, Galleria — names, volumes, segments), 90-day merchant projection (10+), 12-month projection (40+), technical readiness (Click Desk multi-tenant SaaS already live, dev capacity in-house), use case (AI-captured orders auto-dispatch to Uber Direct), ask (platform partner status, multi-tenant account model, certified directory listing).
2. **Day 3 — Email `ukirestaurants@uber.com`** with the deck attached. Subject line: *"Click AI Agency — UK platform partner enquiry, 10+ merchants in pipeline."* CC `uki-onboarding@uber.com`. Ask explicitly for a call with the partnerships/BD function — not the merchant onboarding flow.
3. **Day 3–10 — Parallel-track Stuart.** Same deck, different sender, send to Stuart's partner team. Whichever responds first sets the negotiating floor.
4. **Day 7 — If no reply, follow up.** Single chase. Add Galleria's specific volume.
5. **Day 14 — Decision point.** If a discovery call is booked, push hard on (a) multi-tenant account architecture, (b) UK per-delivery rate card, (c) certification timeline. If silence, escalate via LinkedIn to a named UK Uber Direct Client Partner.

**While that runs — start the dev work against the public Direct API in sandbox.** It's public, you don't need partner status to integrate, and a working sandbox prototype shortens the partner conversation by weeks. Build the Click Desk delivery abstraction now (Uber Direct adapter + Stuart adapter behind one interface).

**Realistic timeline to "delivery integrated and live for first client":**
- Sandbox build + Galleria pilot via direct merchant API: **4–6 weeks from start** (does not require partner status)
- Certified platform partner status, multi-tenant rollout to all clients: **3–5 months** (depends on Uber's certification queue and the commercial conversation)

**Bottom-line bottom line:** Don't wait for partner status to ship delivery to Galleria. Use the public Direct API + a per-merchant account for the first 1–3 clients to prove the model. Apply for partner status in parallel with that real-world evidence in hand. That's the shortest path to both revenue and leverage.

---

## Sources

- https://merchants.ubereats.com/gb/en/services/uber-direct/ — current
- https://merchants.ubereats.com/gb/en/integration-partners/ — current
- https://merchants.ubereats.com/us/en/integration-partners/direct/ — current
- https://merchants.uber.com/uber-direct.html — current
- https://www.uber.com/gb/en/b/courier-services/london-eng-gb/ — current
- https://merchants.ubereats.com/gb/en/contact-us/ — current
- https://developer.uber.com/docs/deliveries/overview — current
- https://developer.uber.com/docs/deliveries/api-reference/daas — current
- https://developer.uber.com/docs/deliveries/direct/api/v1/post-eats-deliveries-orders — current
- https://developer.uber.com/docs/deliveries/guides/webhooks — current
- https://www.deliverect.com/en-gb/integrations/uber-direct — current
- https://retailtechinnovationhub.com/home/2025/9/3/deliverect-builds-on-uk-partnership-as-it-announces-integration-with-uber-direct-in-ireland — current (9 months old)
- https://www.lightspeedhq.com/uk/integrations/uber-direct/ — current
- https://www.restaurantdive.com/news/uber-toast-enter-strategic-global-partnership/804484/ — current
- https://softwarefinder.com/fleet-management-software/stuart — current
- https://info.stuart.com/delivery-for-restaurant — current

**Stale / flagged:**
- Original Deliverect–Uber Direct partnership announcement, Sept 2023 via Food On Demand: https://foodondemand.com/09192023/uber-partners-with-deliverect-on-direct-order-integration/ — 30+ months old, historical context only.
- TheMuse "Client Partner Enterprise Uber Direct UK" — listing returned 404 at fetch time. Confirms the role exists but cannot extract current detail.
