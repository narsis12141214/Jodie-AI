# Lovable Prompt — Restaurants and Cafes Page

**Use this as a single paste into Lovable's chat. Short, direct, scoped.**

---

## The prompt

```
Update the existing page at /ai-voice-receptionist-restaurants-cafes.

REPLACE THE COPY ONLY. Do not change design, fonts, colours, layout, components, spacing, imagery style, or any visual element. The visual brand stays exactly as it is today.

Use the HTML file I'm attaching as the new content source. Map the sections one-to-one onto the existing page structure: hero → hero, problem → problem, pricing → pricing, FAQ → FAQ, and so on. If the existing page has a section that the new HTML does not cover, keep the existing section. If the new HTML has a section the existing page does not have, add it using the existing design language.

URL change required:
- New URL slug: /ai-phone-answering-and-booking-automation-uk-restaurants-cafes
- Set a 301 redirect from /ai-voice-receptionist-restaurants-cafes to the new URL
- Update the canonical link in the page head to match the new URL
- Update sitemap.xml automatically

Meta tags to update exactly as in the HTML head:
- Page title: AI Phone Answering for UK Restaurants & Cafes | Click AI
- Meta description: AI phone agent that answers every booking call for UK restaurants and cafes. Capture every reservation, fill every table. From £290/month. See a live demo.
- Open Graph + Twitter card meta tags
- JSON-LD schema markup (Service type)

Internal links inside the page should point to:
- /ai-receptionist-for-uk-dental-practices (dental page)
- /ai-receptionist-uk-gyms-fitness-studios (fitness page when live)
- /ai-receptionist-for-uk-aesthetic-clinics (aesthetic clinics page)
- /contact or /demo (CTA destinations, use existing)

External citation links should open in a new tab (target="_blank" rel="noopener").

Preserve all existing component behaviour: pricing toggles if any, FAQ accordions, CTA button hover states, mobile menu, footer. Visual style must match the rest of clickaiagency.com exactly.
```

---

## How to use this prompt

1. Open Lovable for clickaiagency.com
2. Paste the prompt above into the chat
3. Attach `landing-page-restaurants-cafes.html` from this folder as the content source
4. Review the output before publishing — confirm Lovable preserved the existing design tokens (colours, fonts, spacing)
5. Test the 301 redirect: load `/ai-voice-receptionist-restaurants-cafes` in an incognito tab and confirm it lands on the new URL
6. Submit URL change in Google Search Console after publishing

## What NOT to do in Lovable

- Do not let Lovable redesign the page
- Do not let Lovable swap fonts (Click brand fonts must remain)
- Do not let Lovable change the colour palette
- Do not let Lovable replace imagery with stock photography
- Do not let Lovable rename existing components

If Lovable produces something that looks visually different from the rest of clickaiagency.com, reject the build and re-prompt with "match the visual style of the existing /ai-voice-receptionist-restaurants-cafes page exactly".

## Pre-publish checklist (after Lovable build)

- [ ] H1 matches: "AI Phone Answering and Booking Automation for UK Restaurants and Cafes"
- [ ] Page title matches
- [ ] Meta description matches
- [ ] Canonical URL matches new slug
- [ ] 301 redirect from old slug confirmed working
- [ ] Pricing table renders correctly on desktop and mobile
- [ ] FAQ accordion functions
- [ ] All citation links open in new tab
- [ ] No visual regressions vs other site pages
- [ ] Sitemap.xml includes new URL
- [ ] Old URL removed from sitemap.xml (or both kept temporarily during redirect window)
- [ ] Submit URL change in Google Search Console
- [ ] Internal links to dental, fitness, aesthetic clinics pages point to new canonical URLs
