# Haleh Cake — Click Desk AI Tenant Provisioning Checklist

**Status:** Pre-build. Trial clock starts at go-live, not signature.
**Owner:** Hadi + Arman
**Target go-live:** Within 7 to 10 days of kickoff call

---

## Phase 1 — Tenant Setup (Day 1-2 after kickoff call)

- [ ] Create Haleh Cake tenant in Click Desk AI dashboard (clickdesk-ai.vercel.app)
  - Tenant name: `haleh-cake`
  - Tenant ID: auto-generated, log it here once created
  - Tenant ID: ____________________
- [ ] Provision Supabase row for tenant (confirm with Arman that multi-tenant refactor is live for the relevant workflows)
- [ ] Set up tenant-specific environment variables in n8n (currently 6 workflows — Send Booking Emails is first per session log)
- [ ] Confirm Send Booking Emails workflow is multi-tenant ready before assigning Haleh to it
- [ ] Create dedicated Google Drive folder: `Click AI Agency / Clients / Haleh Cake`
  - Sub-folders: Assets, Onboarding, Content Calendar, Voice Agent Scripts, Reports

## Phase 2 — Voice Agent Build (Day 2-5)

- [ ] Vapi voice agent provisioned for Haleh Cake
  - Use Ahla Tallah agent as template (per me.md, voice agent already built and tested)
  - Customise: greeting, business info, FAQ, order flow, escalation rules
- [ ] Pull voice agent config from onboarding pack answers (sections 4 and 5)
- [ ] Twilio phone number provisioned for Haleh Cake
  - Decision: new number vs port existing? Confirm with client on kickoff call
  - If new: order number, confirm with Twilio (display name change ticket already open from earlier client)
- [ ] Test voice agent end-to-end: greeting, FAQ, order flow, escalation, message-taking
- [ ] Record sample call and share with Haleh for approval before go-live

## Phase 3 — WhatsApp Business Setup (Day 3-6)

- [ ] WhatsApp Business API account for Haleh Cake
  - Note: WABA process for Click AI Agency itself was completed 1 May. Confirm whether sub-tenants share the parent WABA or each gets their own.
  - Decision: confirm with Arman
- [ ] Submit 3 message templates to Meta for approval:
  - Order confirmation
  - Order ready / out for delivery
  - Review request (post-delivery)
- [ ] Wire WhatsApp branch in n8n to Haleh's tenant (queued behind multi-tenant refactor)
- [ ] Test message flow end-to-end with internal numbers before go-live

## Phase 4 — Social Media Setup (Day 4-7)

- [ ] Receive admin access from Haleh (Instagram, Facebook, TikTok) — kickoff call task
- [ ] Connect accounts to Metricool ($25/mo plan, 10 brands, already paid)
- [ ] Set up Haleh as one of the 10 brand slots in Metricool
- [ ] Pull existing content from her accounts for audit
- [ ] Draft Month 1 content calendar (12 posts + 2 reels per Kish template — confirm Haleh contract delivers same)
  - Wait — Haleh contract says "social media content creation and management" but does NOT specify post count. Confirm verbally on kickoff call. Default benchmark: 12 posts/month + 2 reels.
- [ ] Brand template kit in Canva: colour palette, fonts, post template grid

## Phase 5 — Go-Live (Day 7-10)

- [ ] Final pre-launch check across voice + WhatsApp + social
- [ ] Walkthrough call with Haleh — show her the dashboard, confirm she's happy
- [ ] Flip systems live — voice agent active, WhatsApp templates approved, first post scheduled
- [ ] Mark go-live date in CRM. Trial Day 1 begins.
- [ ] Set calendar reminder for Day 7 of trial: "Haleh trial ending tomorrow. Check satisfaction. Invoice tomorrow."
- [ ] Set calendar reminder for Day 8: send first invoice (£398.50 — Month 1, 50% off)

## Phase 6 — Trial Week (Day 1-7 of trial)

- [ ] Daily check-in via WhatsApp: "All good today?" — quick, no friction
- [ ] Day 3 mid-trial review call (15 mins): any tweaks needed?
- [ ] Day 6 pre-billing call: confirm she's continuing, walk through what's coming in Month 1
- [ ] Day 7: trial ends. If she continues — invoice Day 8. If she cancels — wind down per contract clause 4(c)
- [ ] Begin case study data capture from Day 1: calls answered, messages handled, engagement growth

## Phase 7 — Case Study Capture (Month 1+)

- [ ] Baseline metrics captured at go-live: current call volume, current social engagement, current weekly order count (where available)
- [ ] Week 4 review: data pull, before/after numbers
- [ ] Month 3 review: case study draft, client approval
- [ ] Publish case study on clickaiagency.com + social

---

## Critical Risks to Flag

1. **Multi-tenant n8n refactor not complete** — per 9 May session log, Send Booking Emails is the first workflow being refactored. WhatsApp branch comes after. If Haleh's go-live is rushed before refactor is done, we risk cross-tenant data leakage. Hold go-live until at minimum Send Booking Emails + voice workflow are confirmed multi-tenant safe.

2. **Twilio display name change ticket open** — affects how voice agent identifies itself on caller ID. Confirm status before Haleh go-live.

3. **WABA template approval lag** — Meta usually approves within 24 hours but can take up to 5 days. Submit templates early in Phase 3 to avoid blocking go-live.

4. **Content approval clause 2.4** — Haleh has 5 business days to approve content. First batch of approvals needs to land before Month 1 starts, or content schedule slips immediately.

---

## Dependencies on Arman

- Confirm multi-tenant refactor status (which of 6 workflows are ready)
- Confirm Click Desk AI dashboard handles tenant creation cleanly
- Confirm tenant-specific Supabase row provisioning is automated or manual
- WhatsApp sub-tenant decision (shared WABA vs separate)
- Twilio phone number provisioning per tenant

Brief Arman this week. Block one hour for a technical walk-through before kickoff call.
