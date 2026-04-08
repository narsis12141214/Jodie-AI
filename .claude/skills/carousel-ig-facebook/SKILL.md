# carousel-ig-facebook

**Trigger:** Use when the user asks to create a carousel, generate slides, or build slide graphics specifically for Instagram or Facebook.

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
# LinkedIn (white, Nate Herk style)
python .claude/skills/carousel-ig-facebook/generate.py input.json --platform linkedin

# Instagram / Facebook (dark, monospace style)
python .claude/skills/carousel-ig-facebook/generate.py input.json --platform instagram
```

Platform defaults to `linkedin` if omitted. Use `instagram` for both Instagram and Facebook — same output file works for both.

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
    {"type": "intro", "title": "Your big hook headline", "body": "Supporting hook line. What's coming"},
    {"type": "content", "title": "Point one", "body": "Supporting detail for this point."},
    {"type": "content", "title": "Point two", "body": "Supporting detail for this point."},
    {"type": "outro", "title": "Your CTA headline", "body": "Comment \"WORD\" and I'll send you the details.", "cta_word": "WORD"}
  ]
}
```

### Slide types
- `intro` — Large bold ALL CAPS headline + monospace body. Hook must stop the scroll.
- `content` — Auto-numbered `N | TITLE` format in mono bold + body in lighter mono. One idea per slide.
- `outro` — Large CTA headline + body with one highlighted CTA word. No swipe arrow.

### The `cta_word` field (outro only)
The word to highlight in accent purple `#6C63FF`. This is the comment trigger or action word — e.g. `"MENU"`, `"DEMO"`, `"YES"`. Changes per post. Required on outro for Instagram. Omit for LinkedIn.

---

## Platform differences

| | LinkedIn | Instagram / Facebook |
|---|---|---|
| Background | White `#FFFFFF` | Dark `#0A0D14` |
| Headline font | Inter Bold, sentence case | Inter Bold, ALL CAPS |
| Body font | Inter Regular | JetBrains Mono Regular |
| Content labels | None | `N \| TITLE` numbered |
| Verified badge | No | Yes (blue tick after name) |
| Swipe arrow | "Swipe ->" bottom-right | "----->" bottom-right |
| Outro swipe | No | No |
| CTA highlight | No | Yes (`cta_word` in purple) |

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
- LinkedIn tone: slightly more professional, still direct. No slang. Sentence case.
- Instagram/Facebook tone: punchier, shorter sentences, ALL CAPS headlines, can use one emoji per slide maximum.

### What carousels are for
- Top-of-funnel awareness and trust-building.
- Demonstrating expertise without pitching.
- Carousels do not close deals — they earn the right to start a conversation.

---

## Output contract

Slides land in: `projects/carousels/YYYY-MM-DD-{slug}-{platform}/`

Filenames: `slide-1-intro.png`, `slide-2.png`, `slide-3.png`, ..., `slide-N-outro.png`

Size: 1080 x 1350px PNG (4:5 ratio — works on Instagram feed, Facebook, and LinkedIn)

---

## Brand assets

### Instagram / Facebook
- Logo + headshot: `brand-assets/Click AI Logos/click-logo-white.png`
- Headline font: `brand-assets/fonts/inter-bold.ttf`
- Body font: `brand-assets/fonts/JetBrainsMono-Regular.ttf`
- Bold mono: `brand-assets/fonts/JetBrainsMono-Bold.ttf`

### LinkedIn
- Logo: `/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI/brand-assets/Click AI Logos/click-logo.png`
- Headline font: `brand-assets/fonts/inter-bold.ttf`
- Body font: `brand-assets/fonts/inter-regular.ttf`

All assets are optional — skill runs gracefully without them.

**Note:** Once JetBrains Mono is installed, body text will look sharper and more on-brand. Download from jetbrains.com/lp/mono and drop Regular and Bold TTF files into `brand-assets/fonts/`.
