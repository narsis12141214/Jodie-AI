# Lovable Prompt — Aesthetic Clinics Page

**Use this as a single paste into Lovable's chat. Short, direct, scoped.**

---

## The prompt

```
Update the existing page at /ai-voice-receptionist-beauty-aesthetics-clinics.

REPLACE THE COPY ONLY. Do not change design, fonts, colours, layout, components, spacing, imagery style, or any visual element. The visual brand stays exactly as it is today and must match the other Click landing pages.

Use the HTML file I'm attaching as the new content source. Map the sections one-to-one onto the existing page structure: hero → hero, problem → problem, pricing → pricing, FAQ → FAQ, and so on. Add a new "Regulatory framing" section if the existing page doesn't have one (it's important for this segment).

URL change required:
- New URL slug: /ai-receptionist-for-uk-aesthetic-clinics
- Set a 301 redirect from /ai-voice-receptionist-beauty-aesthetics-clinics to the new URL
- Update the canonical link in the page head to match the new URL
- Update sitemap.xml automatically

Meta tags to update exactly as in the HTML head:
- Page title: AI Receptionist for Aesthetic Clinics UK | Click AI Agency
- Meta description: AI receptionist for UK aesthetic clinics. Answer every Botox, filler, and skin enquiry 24/7. Books into Pabau and Phorest. See a live demo today.
- Open Graph + Twitter card meta tags
- JSON-LD schema markup (Service type)

Internal links inside the page should point to:
- /ai-phone-answering-and-booking-automation-uk-restaurants-cafes (restaurants page)
- /ai-receptionist-for-uk-dental-practices (dental page)
- /ai-receptionist-uk-gyms-fitness-studios (fitness page)
- / (homepage)
- /contact or /demo (CTA destinations, use existing)

External citation links should open in a new tab (target="_blank" rel="noopener").

Design specifics for aesthetic clinics:
- Clinical, premium visual tone (not generic beauty stock)
- Stat callouts (30-42%, 85%, £150-£350, £2,950+) prominent in problem section
- "Click Pro Recommended for aesthetics" badge subtle but visible on pricing comparison
- The "Regulatory framing" section (What the AI does. And what it does not.) must be visually prominent — this builds trust and removes objections
- Integration logo strip (Pabau, Phorest Medical, ANS, Consentz, Clinicminds) prominent on page
- GDPR / data protection mentions throughout, especially in FAQ

Preserve all existing component behaviour: pricing toggles, FAQ accordions, CTA button hover states, mobile menu, footer. Visual style must match clickaiagency.com exactly.
```

---

## How to use this prompt

1. Open Lovable for clickaiagency.com
2. Paste the prompt above into the chat
3. Attach `landing-page-aesthetic-clinics.html` from this folder as the content source
4. Review the output before publishing — confirm Lovable preserved the existing design tokens
5. Test the 301 redirect: load `/ai-voice-receptionist-beauty-aesthetics-clinics` in an incognito tab and confirm it lands on the new URL
6. **Critical check:** the "Regulatory framing" section (What the AI does / does not) must be visible. This is the trust signal that converts hesitant clinic owners.

## What NOT to do in Lovable

- Do not let Lovable redesign the page
- Do not let Lovable swap fonts or colours
- Do not let Lovable use generic beauty stock photography (smiling women, syringes-in-faces close-ups, etc.)
- Do not let Lovable strip the regulatory / GDPR mentions
- Do not let Lovable insert clinical claims the AI is not allowed to make
- Do not let Lovable downgrade the integration logo strip to a single icon row

## Pre-publish checklist (after Lovable build)

- [ ] H1 matches: "AI Receptionist for UK Aesthetic Clinics"
- [ ] Page title matches (57 chars)
- [ ] Meta description matches (143 chars, includes "Pabau" and "Phorest")
- [ ] Canonical URL matches new slug
- [ ] 301 redirect from old URL confirmed working
- [ ] Click Pro as recommended tier badge visible
- [ ] "Regulatory framing" section (does / does not) visually prominent
- [ ] All 5 integration names (Pabau, Phorest Medical, ANS, Consentz, Clinicminds) visible
- [ ] All stat callouts (30-42%, 85%, £150-£350, £2,950+) render correctly
- [ ] All citation links open in new tab
- [ ] JSON-LD schema present in head
- [ ] No visual regressions vs other site pages
- [ ] Sitemap.xml includes new URL
- [ ] Old URL removed from sitemap.xml (or both kept during redirect window)
- [ ] Submit URL change in Google Search Console
- [ ] Internal links to homepage and other segment pages updated

## Specific aesthetics considerations

This page is the highest-stakes from a regulatory and trust perspective. Three things MUST land:

1. **The regulatory framing section** (What the AI does / What the AI does not) removes the buyer's biggest objection before it's raised. This is the difference between converting and not converting.
2. **The integration story** (Pabau, Phorest Medical, ANS, Consentz, Clinicminds named on page) is the trust signal that beats every US competitor. They don't name UK-specific systems. We do.
3. **The data points are all sourced** with citation URLs. Aesthetic clinic owners read carefully. Unsourced claims kill credibility immediately.

These elements are all in the HTML. Lovable should preserve them exactly.
