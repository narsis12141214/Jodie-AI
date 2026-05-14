# Lovable Prompt — Homepage Rewrite

**Use this as a single paste into Lovable's chat. Short, direct, scoped.**

---

## The prompt

```
Update the homepage at clickaiagency.com (route: /).

REPLACE THE COPY ONLY. Do not change design, fonts, colours, layout, components, spacing, imagery style, or any visual element. The visual brand stays exactly as it is today.

Use the HTML file I'm attaching as the new content source. Map sections one-to-one onto the existing homepage structure: hero → hero, industries → industries, pain section → pain section, services → services, differentiators → differentiators, how it works → how it works, packages → packages, social proof → social proof, final CTA → final CTA.

Critical structural changes (priority order):

1. Hero structure: KEEP the existing rotating-word animation "Branding that makes you more Growth / Sales / Clicks" exactly as it currently renders. It is a brand element we are preserving. Move it to position above the new H1 as a hero eyebrow / pre-headline. ADD a new H1 directly below it:
   "Never Miss Another Booking. Done-for-you AI for UK Service Businesses."

   The rotating animation stays in its current visual treatment. The new H1 is a separate element underneath. The rotating element is NOT the H1; it stays as a styled paragraph or eyebrow.

2. Package section must be restructured:
   - REMOVE the current "Core" tier entirely (do not display on homepage)
   - The retired tier names (Core, Drive, Turbo, Nitro) are dead. Replace with Click Voice, Click+, Click Pro, Click Elite.
   - Click Voice is the new entry tier, displayed as a LARGE, FEATURED card at the TOP of the package section
   - Click+, Click Pro, Click Elite displayed as a 3-card grid BELOW Click Voice
   - Click+ retains the "Most Popular" badge

3. Industry section must be restructured:
   - The current "TRUSTED BY UK..." section lists 7 industries as text only (Restaurants, Salons, Clinics, Coaches, Photography, Electricians, Plumbers)
   - Replace with 4 clickable cards linking to dedicated segment landing pages:
     * "AI for Restaurants and Cafes" → /ai-phone-answering-and-booking-automation-uk-restaurants-cafes
     * "AI for Dental Practices" → /ai-receptionist-for-uk-dental-practices
     * "AI for Aesthetic Clinics" → /ai-receptionist-for-uk-aesthetic-clinics
     * "AI for Gyms and Fitness Studios" → /ai-receptionist-uk-gyms-fitness-studios

4. Setup fees must align with the new package structure:
   - Click Voice: £100 launch (standard £350)
   - Click+: £750 (waived for founding cohort)
   - Click Pro: £1,000 (waived for founding cohort)
   - Click Elite: £1,500 (waived for founding cohort)

   The current homepage shows £290/£290/£790/£990 which is wrong. These are retired.

Meta tags to update exactly as in the HTML head:
- Page title: Click AI Agency: Done-for-you AI for UK Service Businesses (58 chars)
- Meta description: We build AI receptionists, follow-up systems and content engines for UK restaurants, clinics and salons. Never miss another booking. (138 chars)
- Open Graph + Twitter card meta tags
- JSON-LD schema markup (Organization type)

External citation links should open in a new tab (target="_blank" rel="noopener").

Preserve all existing component behaviour: pricing card hover states, CTA button hover states, mobile menu, footer. Visual style must match the rest of clickaiagency.com exactly.
```

---

## How to use this prompt

1. Open Lovable for clickaiagency.com
2. Paste the prompt above into the chat
3. Attach `homepage.html` from this folder as the content source
4. Review the output before publishing — confirm Lovable preserved the existing design tokens
5. **Critical visual check:** open the new homepage preview side-by-side with the restaurants/cafes page (once built). The visual style must match.

## What NOT to do in Lovable

- Do not let Lovable redesign the page
- Do not let Lovable swap fonts
- Do not let Lovable change the colour palette
- Do not let Lovable replace imagery with stock photography
- Do not let Lovable shorten the package section to "save space" — Click Voice MUST be visually featured at the top
- Do not let Lovable leave the old Core tier as a 5th package

If Lovable produces something visually different from the rest of clickaiagency.com, reject the build and re-prompt with "match the visual style of the existing site exactly".

## Pre-publish checklist (after Lovable build)

- [ ] H1 matches: "Never Miss Another Booking. Done-for-you AI for UK Service Businesses."
- [ ] Rotating-word brand animation ("Branding that makes you more Growth / Sales / Clicks") is PRESERVED above the H1 as a hero eyebrow
- [ ] Rotating animation is tagged as a styled paragraph (not as the H1)
- [ ] Package section: Click Voice on top (large/featured), 3 bundles below (Click+, Click Pro, Click Elite)
- [ ] Core tier is NOT on the page
- [ ] Setup fees match canonical: £100/£750/£1,000/£1,500
- [ ] All 4 industry cards link to correct segment page URLs
- [ ] Page title matches (58 chars)
- [ ] Meta description matches (138 chars)
- [ ] Canonical URL is `https://clickaiagency.com/`
- [ ] JSON-LD schema markup present in head
- [ ] All citation links open in new tab
- [ ] Pricing cards render correctly on desktop and mobile
- [ ] No visual regressions vs other site pages
- [ ] Sitemap.xml includes homepage URL
- [ ] Submit homepage for re-indexing in Google Search Console

## Why these changes matter

- The current homepage has a rotating-word brand element ("Branding that makes you more Growth / Sales / Clicks") that stays. The page is missing a real H1 underneath it for SEO. Adding the new H1 below the rotating element gives the page proper search structure.
- The current package names (Core/Drive/Turbo/Nitro) were retired 17 April. Anyone seeing the homepage sees package names that don't exist anywhere else in the business. Major credibility issue.
- The current setup fees don't match the canonical packages file. Anyone who converts on those fees will be confused when they receive a contract with different numbers.
- The current industry section doesn't link anywhere. Visitors see "Restaurants" as a text label with no path forward. The new cards do the conversion job they were always meant to do.

This is not a polish job. This is fixing 4+ weeks of brand erosion.
