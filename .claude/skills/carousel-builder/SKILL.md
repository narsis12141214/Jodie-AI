# carousel-builder

**Trigger:** Use when the user asks to create a carousel, generate slides, make a social media carousel, or build slide graphics.

---

## Agent hierarchy for carousel creation

Jodie handles carousel generation autonomously. No live Strategist or Closer involvement is needed per post. Instead:

- **Strategist input is pre-baked** into this SKILL.md as standing brand rules. Read them every time before writing copy.
- **Campaign Builder gets involved** only if the carousel is part of a named campaign — check with Hadi first.
- **Closer does not touch carousels.** Carousels are top-of-funnel content, not conversion moments.

Flow: **Jodie reads brand rules → decides slide count → writes copy → builds JSON → runs generator.**

---

## How to invoke

```bash
python .claude/skills/carousel-builder/generate.py input.json --platform linkedin
python .claude/skills/carousel-builder/generate.py input.json --platform instagram
```

Platform defaults to `linkedin` if omitted.

---

## Slide count — how to decide

There is no fixed slide count. Decide based on the topic:

- **Intro:** always exactly 1
- **Outro:** always exactly 1
- **Content slides:** however many points the topic genuinely needs — typically 3-7
- **Minimum total:** 4 slides. **Maximum:** 9 slides.
- Do not pad with weak points to hit a number.
- Do not cut a strong point to stay short.
- Each content slide must earn its place — one clear idea, expressed simply.

---

## Input contract

Create a JSON file with this structure:

```json
{
  "topic": "your topic here",
  "slides": [
    {"type": "intro", "title": "Your big hook headline"},
    {"type": "content", "title": "Point one", "body": "Supporting detail for this point."},
    {"type": "content", "title": "Point two", "body": "Supporting detail for this point."},
    {"type": "outro", "title": "Call to action", "body": "Secondary CTA line."}
  ]
}
```

### Slide types
- `intro` — Large headline + accent line. No body text. Hook must stop the scroll.
- `content` — Medium headline + body paragraph. One idea per slide.
- `outro` — Large CTA headline + body. No swipe indicator. End with a clear action.

### Optional brand override
Add a `brand_config` object to override any default. Keys: `handle`, `display_name`, `background_color`, `text_color`, `accent_color`, `logo_path`, `headshot_path`.

---

## Standing brand rules (Strategist brief — read every time)

### Click AI Agency — brand voice
- **Positioning:** AI automation for small businesses in London. We make them faster, leaner, and more competitive without hiring more staff.
- **Tone:** Direct, confident, no fluff. Speak like a founder who knows their stuff, not a marketer trying to sound clever.
- **Never say:** "game-changing", "revolutionary", "cutting-edge", "leverage", "unlock", "empower", or anything that sounds like a press release.
- **Always say:** Concrete outcomes. Specific problems. Real numbers where possible.
- **Target audience:** Restaurant owners, beauty clinic owners, estate agents, tradespeople, wholesalers, barber shops — London-based small business owners who are time-poor and skeptical of tech promises.
- **What they fear:** Wasting money on things that don't work. Looking stupid in front of their team. Being left behind by competitors.
- **What they want:** More customers, less admin, someone they can trust to handle the tech.

### Content rules for carousels
- Intro headline must create tension or curiosity — a problem, a contrast, or a surprising fact.
- Content slides must feel like genuine insight, not bullet points dressed up as slides.
- Outro CTA must be low-friction — comment, DM, or link. Never ask for a call on the first touch.
- Write for someone scrolling fast. If it takes more than 2 seconds to understand a slide, rewrite it.
- LinkedIn tone: slightly more professional, still direct. No slang.
- Instagram tone: punchier, shorter sentences, can use one emoji per slide maximum.

### What carousels are for
- Top-of-funnel awareness and trust-building.
- Demonstrating expertise without pitching.
- Carousels do not close deals — they earn the right to start a conversation.

---

## Output contract

Slides land in: `projects/carousels/YYYY-MM-DD-{slug}-{platform}/`

Filenames: `slide-1-intro.png`, `slide-2.png`, `slide-3.png`, ..., `slide-N-outro.png`

Size: 1080 x 1350px PNG (Instagram 4:5, works on LinkedIn)

---

## Brand configs (built in)

### LinkedIn (white)
- Background: `#FFFFFF`, Text: `#0A0A0A`, Accent: `#6C63FF`
- Clean Nate Herk-style layout

### Instagram (dark)
- Background: `#0A0D14`, Text: `#FFFFFF`, Accent: `#6C63FF`
- Click AI Agency dark brand

---

## Brand assets expected at
- `brand-assets/fonts/inter-bold.ttf`
- `brand-assets/fonts/inter-regular.ttf`
- `/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI/brand-assets/Click AI Logos/click-logo.png` — used for both logo and headshot

All assets are optional — skill runs gracefully without them.
