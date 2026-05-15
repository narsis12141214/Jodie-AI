# Lovable Prompt — Site-Wide Pricing Update (15 May 2026)

**Purpose:** Update all package pricing and features across clickaiagency.com to match the new canonical spec (`.claude/agents/shared/click-ai-agency-packages.md`).

**Scope:** Homepage + 4 segment landing pages. No new pages, no design changes.

---

## The prompt

```
Update the package pricing and feature lists across these 5 pages:

1. Homepage (/)
2. /ai-phone-answering-and-booking-automation-uk-restaurants-cafes
3. /ai-receptionist-for-uk-dental-practices
4. /ai-receptionist-for-uk-aesthetic-clinics
5. /ai-receptionist-uk-gyms-fitness-studios

CRITICAL: Do not change design, fonts, colours, layout, imagery, or any visual element. Update text content within the existing pricing cards / tables only.

Every page has a pricing section. Update each pricing display with the new spec below.

DESIGN RULE: Setup fee must be displayed UNDER the package name and monthly price (as a separate styled line), NOT as an item in the feature bullet list.

---

NEW PRICING SPEC (use this exactly across all pages):

==============================================
CLICK VOICE — £290/month
Setup: £100 launch (founding cohort) / £350 standard — 70% off launch pricing

Entry tier. Voice-only. Restaurants and cafes only.

Features:
- Custom AI voice agent trained on your business
- 1,000 minutes/month combined voice + transactional confirmations
- WhatsApp, SMS, or email confirmations and reminders
- Integration with your existing booking system
- Click Desk AI dashboard
- Basic Google Business Profile setup
- 14-day trial from go-live, no monthly fee during trial

==============================================
CLICK+ — £790/month
Setup: £150 launch (founding cohort) / £500 standard — 70% off launch pricing

The growth tier. Voice, WhatsApp, content, all run by our team.

Features:
- Custom AI voice agent trained on your business
- 1,500 minutes/month calls
- WhatsApp, SMS, or email confirmations and reminders
- Integration with your existing booking system
- 4 original social posts per week (Instagram + Facebook) — quality-focused, strategic content, not posts for the sake of posts
- Reels, carousels, and stories produced for you
- Click Desk AI dashboard
- Basic Google Business Profile setup
- Multi-language support
- 14-day trial from go-live, no monthly fee during trial

==============================================
CLICK PRO — £1,290/month
Setup: £250 launch (founding cohort) / £850 standard — 70% off launch pricing

The multi-platform tier. Full content engine + advanced automation + strategy.

Features:
- Custom AI voice agent trained on your business
- 3,000 minutes/month calls
- WhatsApp, SMS, or email confirmations and reminders
- Integration with your existing booking system
- 8-10 original social posts per week across 3 platforms (Instagram + Facebook + TikTok) — 3-4 per platform
- Reels, carousels, and stories produced for you
- Click Desk AI dashboard
- Basic Google Business Profile setup
- Review request automation and response management
- Lapsed client win-back sequences
- Multi-language support
- Monthly strategy call (30 min)
- 14-day trial from go-live, no monthly fee during trial

==============================================
CLICK ELITE — £1,990/month
Setup: £350 launch (founding cohort) / £1,200 standard — 70% off launch pricing

The full system. Calls, content, marketing, website, SEO. Dedicated account manager.

Features:
- Custom AI voice agent trained on your business
- Up to 10,000 minutes/month + fair-use clause beyond
- WhatsApp, SMS, or email confirmations and reminders
- Integration with your existing booking system
- 10-12 original social posts per week across 3 platforms (Instagram + Facebook + TikTok)
- Daily stories (2 per day, 7 days a week, ≈60 stories per month)
- Reels, carousels, and stories produced for you
- Click Desk AI dashboard
- Advanced Google Business Profile setup
- Review request automation and response management
- Lapsed client win-back sequences
- CRM integration
- Influencer outreach
- Multi-language support
- Professional website design
- Professional SEO/GEO
- Dedicated account manager
- Monthly strategy call (60 min)
- 14-day trial from go-live, no monthly fee during trial

==============================================

THINGS TO REMOVE WHEREVER THEY APPEAR (no longer in any standard tier):

- "Full WhatsApp automation" — retired. WhatsApp is transactional only (confirmations + reminders).
- "Community management on DMs and comments" — retired.
- "Click" tier at £497/month — retired entirely. Remove from pricing tables, comparison tables, and any package displays.

PAGE-BY-PAGE NOTES:

Homepage (/):
- Package section currently has 4 cards. Update each to match new spec above. Click Voice stays as the large featured card at the top. Click+/Pro/Elite remain in the 3-card grid below.
- The "MOST POPULAR" badge stays on Click+ as it has been.

/ai-phone-answering-and-booking-automation-uk-restaurants-cafes:
- Two-tier comparison shows Click Voice + Click+. Update both with new spec.
- Click Voice retains "founding cohort £100 setup" line.
- Click+ minutes line was "1,000 minutes/month combined voice + WhatsApp" — update to "1,500 minutes/month calls".
- The "30 to 50% no-show reduction" body copy that referenced WhatsApp automation should be softened to "30 to 50% no-show reduction from confirmation/reminder messages" since full WhatsApp automation is no longer a standard inclusion.

/ai-receptionist-for-uk-dental-practices:
- Pricing comparison shows Click+ vs Click Pro. Update both with new spec.
- Note: Click+ no longer has "review request automation" — moved to Pro. The dental page already recommends Click Pro for most practices, so review automation lives in the Pro column where most dental clinics will be.

/ai-receptionist-for-uk-aesthetic-clinics:
- Pricing comparison shows Click+ vs Click Pro vs Click Elite. Update all three.
- Elite section now includes "CRM integration" (not "HubSpot, GoHighLevel, or equivalent" — just "CRM integration").
- Elite includes "Up to 10,000 minutes/month + fair-use" (not "Unlimited").
- Add "Influencer outreach" to Elite features.

/ai-receptionist-uk-gyms-fitness-studios:
- Pricing comparison shows Click+ vs Click Pro. Update both with new spec.
- Note: Click+ "review management" line was incorrect, should be removed (review automation is Pro+).

PRESERVE:
- All existing design tokens (colours, fonts, spacing)
- All existing imagery
- All existing component behaviour (FAQ accordions, CTA buttons, mobile responsive layouts)
- All existing internal links to other pages
- All existing meta tags, canonical URLs, sitemap entries
- The "MOST POPULAR" badge on Click+ where it exists
- The "Recommended for [segment]" badge on whichever tier is recommended per page
```

---

## Pre-publish checklist (after Lovable update)

- [ ] All 5 pages render with new monthly prices: £290 / £790 / £1,290 / £1,990
- [ ] All 5 pages render with new launch setup fees: £100 / £150 / £250 / £350
- [ ] Standard setup fees show £350 / £500 / £850 / £1,200 with "70% off launch pricing" or equivalent framing
- [ ] Setup fees appear UNDER package name + monthly price (not in feature lists)
- [ ] Click+ shows 1,500 minutes (not 1,000)
- [ ] Click Pro shows 3,000 minutes (not 2,500)
- [ ] Click Elite shows "Up to 10,000 minutes + fair-use" (not "Unlimited", not "5,000")
- [ ] "Full WhatsApp automation" is gone from every page
- [ ] "Community management" is gone from every page
- [ ] "Click" tier at £497 is gone (no Core/Click in any pricing table)
- [ ] "Multi-language support" appears in Click+, Pro, and Elite
- [ ] "CRM integration" appears in Click Elite (without naming HubSpot/GHL/etc.)
- [ ] "Influencer outreach" appears in Click Elite
- [ ] Click Elite includes website + SEO/GEO
- [ ] No visual regressions vs the existing brand

---

## Why these changes matter

- Setup fee placement under price (not in items) makes pricing tables read cleaner and matches Stripe / Notion / industry-standard pricing card design.
- Removing the retired "Click" tier eliminates confusion for buyers seeing five tiers when we sell four.
- Moving full WhatsApp automation to bespoke quoting prevents underdelivery — it's genuinely a custom build per business type.
- Removing community management aligns the offer with what we can actually deliver consistently in a standard tier.
- Click Elite's "10,000 minutes + fair-use" replaces "unlimited" which was a unit-economics risk (Vapi + Twilio cost could exceed monthly revenue on high-volume clients).

## What changes for existing clients

Haleh Cake's existing Click+ contract is HONOURED AS SIGNED. Her contract includes full WhatsApp automation and review management at the original Click+ terms. She is grandfathered. Apply new spec to new signings only.
