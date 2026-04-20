# Briefing: No-Website Dental Clinic Outreach Sequence

**From:** Hadi
**Date:** 20 April 2026
**For:** Campaign Builder (via Marketing Strategist approval)
**Owner once live:** Outreach (cold first touch), Closer (warm follow-up)
**Status:** AWAITING CAMPAIGN BUILDER EXECUTION, THEN OPERATOR APPROVAL

---

## What's new

There's a new lead segment in the pipeline. Hadi has built a scraper (lead-engine repo, separate from this one) that pulls London dental clinics from Google Maps via RapidAPI and identifies which ones don't have a website. The first export landed 21 clinics with no website: 3 genuine hot prospects, 1 solid warm, the rest too low-quality or wrong-fit to pitch.

This is a different prospect profile from the clinics we've been going after with the voice receptionist pitch. These clinics don't have a website at all, their Google listing is doing 100% of their discovery work. The pitch here is different and the angle is cleaner.

The spreadsheet Zizi will work is at exports/no_website_leads_[timestamp].csv in the lead-engine repo. Sales tier column sorts best-to-worst.

## The ICP for this segment

Independent London dental practice. Owner-operator or small partnership. Claimed and verified Google Maps listing. 50+ reviews. 4.0+ stars. No dedicated website. Phone as the only currently-working contact channel.

Read that last line carefully: this is a prospect who has already proven they value being findable (they claimed Google, they reply to reviews, they've accumulated volume) but hasn't bought a website yet. That gap is the entire story.

## Why the existing voice-receptionist pitch won't work here

Our current Step 2 diagnostic for clinics is built around the problem of missed calls on an existing site that converts. These prospects don't have a site, there's nothing to convert from. If we ask them about missed calls first, we're solving the wrong problem in sequence. Walking into a conversation with "we'll answer your phones" when the prospect doesn't even have a place for people to find them first is getting the order wrong.

The hook needs to lead with the visibility gap, then expand to the full system.

## What Campaign Builder must design

A 3-step cold outreach sequence for the no-website dental segment, via email (primary channel since these prospects aren't particularly active on social).

**Step 1: Opener.** Names a specific pain, not a category. The Dr Noura benchmark applies: something as concrete as "patients who say I'll check your website first never book." Ends with a diagnostic question, not a pitch. Does NOT mention the word "website" or "agency" in the first message.

**Step 2: Diagnostic.** If they engage at all, this is where we learn whether they've tried a website before (bad experience with a previous agency? Built one themselves that broke?) or never prioritised it. Different diagnostic paths depending on which answer surfaces. Still no pitch at this stage.

**Step 3: Handoff to Hadi.** Once we have a direct contact name and email confirmed (not gatekeeper, not practice@), they come to Hadi for the actual sales conversation. The Closer takes over from here if they go quiet between Hadi's touch and closing.

## Constraints: Campaign Builder read carefully

- No "no problem at all," "just checking in," "totally understand if you've been busy," or any variant of permission-seeking soft language. Closer's forbidden-phrases list applies across all steps.
- No generic-consultant pain statements ("you're leaving money on the table," "in today's digital landscape"). Specificity or silence.
- Don't describe a solution category. Don't say "we build websites" or "we're a digital agency." Name a specific outcome the prospect would recognise as their problem.
- The sequence uses the full Presence-Method-style hierarchy the Strategist maintains for photography: Elevation (lead), Guidance (method), Relief (proof), adapted for agency context. The emotional arc is: their current state is invisible growth ceiling, we see it, we've already solved it for clinics like them.
- Frame the offer as website + AI receptionist as a single combined system, not two products. The positioning is "we handle the whole front door." Nobody else is selling the combined package, that's the wedge.

## Hot prospects to write toward

Campaign Builder should write the sequence for these specific prospects in mind, not a generic avatar:

- Puresmile Bethnal Green (E2, 139 reviews, no site)
- E2 Dental Practice (E2, 126 reviews, no site)
- 18A Charing Cross Dental Surgery (WC2H, 38 reviews, no site)

Every line should be something Zizi could send to one of these three and not have it feel weird. If it could land in Puresmile's inbox and make the owner go "yeah that's us," it's right. If it reads like it was written for a template folder, kill it.

## Deliverables

1. Step 1 email (cold opener, 3 variants for A/B)
2. Step 2 email (diagnostic follow-up, 2 variants depending on Step 1 response)
3. Step 3 handoff template (warm handover note Zizi sends when booking the call with Hadi)
4. Response protocol for common objections:
   - "We have a Facebook page, we don't need a website"
   - "We tried this before, didn't work"
   - "Too expensive / can't afford it"
   - "We're too busy for new patients anyway"

Save output to: projects/agency/outreach-system/sequences/no-website-clinics.md

## Approval gate

Strategist reviews positioning before Campaign Builder ships. Operator approves the sequence before it goes to Outreach. Then Zizi works the list, tracks in the Outreach Tracker using the existing Step/Diagnostic/Direct Contact columns, 48hr nudge rule applies.

---

*Briefing filed 20 April 2026. Campaign Builder: execute when assigned. Operator: approve before shipping to Outreach.*
