# Lovable Prompt — Dental Practices Page

**Use this as a single paste into Lovable's chat. Short, direct, scoped.**

---

## The prompt

```
Build the page at /ai-receptionist-for-uk-dental-practices.

IMPORTANT: The existing /dental-clinics-ai-voice-receptionist URL currently returns 404. Hadi to investigate Lovable status first. If the page was genuinely deleted, build fresh at the new URL using the HTML I'm attaching. If it was a routing issue, restore the page first, then implement these changes.

REPLACE THE COPY ONLY. Do not change design, fonts, colours, layout, components, spacing, imagery style, or any visual element. The visual brand stays exactly as it is today and must match the other Click landing pages.

Use the HTML file I'm attaching as the new content source. Map the sections one-to-one onto the existing page structure: hero → hero, problem → problem, pricing → pricing, FAQ → FAQ, and so on.

URL change required:
- New URL slug: /ai-receptionist-for-uk-dental-practices
- Set a 301 redirect from /dental-clinics-ai-voice-receptionist to the new URL
- Update the canonical link in the page head to match the new URL
- Update sitemap.xml automatically

Meta tags to update exactly as in the HTML head:
- Page title: AI Receptionist for UK Dental Practices | Click AI Agency
- Meta description: AI receptionist for UK dental practices. Answer every call, book every patient, reduce no-shows 24/7. Done-for-you setup. See a live demo today.
- Open Graph + Twitter card meta tags
- JSON-LD schema markup (Service type)

Internal links inside the page should point to:
- /ai-phone-answering-and-booking-automation-uk-restaurants-cafes (restaurants page)
- /ai-receptionist-uk-gyms-fitness-studios (fitness page)
- /ai-receptionist-for-uk-aesthetic-clinics (aesthetic clinics page)
- / (homepage)
- /contact or /demo (CTA destinations, use existing)

External citation links should open in a new tab (target="_blank" rel="noopener").

Design specifics for dental:
- More clinical/professional visual tone than the restaurants page
- Stat callouts (32%, 80%, 300, 30-50%) prominent in the problem section
- "Click+ Recommended for dental" badge subtle but visible on the pricing comparison
- GDPR / data protection mention should be visible above the fold (small print but visible)

Preserve all existing component behaviour: pricing toggles, FAQ accordions, CTA button hover states, mobile menu, footer. Visual style must match clickaiagency.com exactly.
```

---

## How to use this prompt

1. **Critical first step:** investigate the existing /dental-clinics-ai-voice-receptionist page status in Lovable. It currently returns 404. Is the page deleted, or is it a routing/publish issue?
2. Open Lovable for clickaiagency.com
3. Paste the prompt above into the chat
4. Attach `landing-page-dental-practices.html` from this folder as the content source
5. Review the output before publishing
6. Test the 301 redirect: load `/dental-clinics-ai-voice-receptionist` in an incognito tab and confirm it lands on the new URL

## What NOT to do in Lovable

- Do not let Lovable redesign the page
- Do not let Lovable swap fonts or colours
- Do not let Lovable use generic dental stock photography (people with mouths open, exaggerated smiles, etc.)
- Do not let Lovable strip the regulatory / GDPR mentions
- Do not let Lovable insert clinical claims the AI is not allowed to make

## Pre-publish checklist (after Lovable build)

- [ ] H1 matches: "AI Receptionist for UK Dental Practices"
- [ ] Page title matches (57 chars)
- [ ] Meta description matches
- [ ] Canonical URL matches new slug
- [ ] 301 redirect from /dental-clinics-ai-voice-receptionist confirmed working
- [ ] Click+ as recommended tier badge visible
- [ ] All 4 stat callouts (32%, 80%, 300, 30-50%) render correctly
- [ ] All citation links open in new tab
- [ ] JSON-LD schema present in head
- [ ] No visual regressions vs other site pages
- [ ] Sitemap.xml includes new URL
- [ ] Old URL removed from sitemap.xml (or both kept during redirect window)
- [ ] Submit URL change in Google Search Console
- [ ] Internal links to homepage and other segment pages updated

## Specific dental considerations

The dental copy carries higher trust-signal stakes than restaurants. Patients are healthcare consumers, not diners. The page must:

- Lead with sourced statistics, not estimates
- State the data security / GDPR position early
- Address the "what about clinical questions?" objection in the FAQ visibly
- Mention practice management integrations (SOE, Dentally, EXACT) by name
- Avoid any language that suggests the AI replaces clinical judgement

These elements are all in the HTML. Lovable should preserve them.
