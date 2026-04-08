# Jodie Briefing — Carousel IG/Facebook Skill
## Deployed: 8 April 2026

---

## What this skill does

Generates branded PNG carousel slides (1080x1350px) for @clickaiagency on Instagram and Facebook. Dark background, ALL CAPS headlines, JetBrains Mono body font, verified badge, numbered content slides, and a `cta_word` highlight on the outro. Completely different visual output from the LinkedIn carousel-builder skill.

---

## Files

| File | Purpose |
|------|---------|
| `generate.py` | Python renderer — handles both instagram and linkedin platform paths |
| `SKILL.md` | Brand rules, platform differences, input contract, output contract — read every time |
| `jodie-briefing_carousel-ig-facebook_2026-04-08.md` | This file |

---

## How to use

1. Write slide copy in ALL CAPS headline style, monospace body feel
2. Save as a `.json` file (e.g. `projects/carousels/input-topic-name.json`)
3. Run: `python .claude/skills/carousel-ig-facebook/generate.py input.json --platform instagram`
4. Slides output to: `projects/carousels/YYYY-MM-DD-{slug}-instagram/`

---

## Key differences from carousel-builder (LinkedIn skill)

| Feature | carousel-builder | carousel-ig-facebook |
|---------|-----------------|---------------------|
| Skill folder | `.claude/skills/carousel-builder/` | `.claude/skills/carousel-ig-facebook/` |
| Primary platform | LinkedIn | Instagram + Facebook |
| Background | White `#FFFFFF` | Dark `#0A0D14` |
| Headlines | Sentence case | ALL CAPS |
| Body font | Inter Regular | JetBrains Mono |
| Content labels | None | `N | TITLE` numbered |
| Verified badge | No | Yes |
| CTA highlight | No | Yes — `cta_word` required on outro |

**Never mix up these two skills.** The outputs are visually distinct and serve different platforms.

---

## The `cta_word` field

Outro slide only. The single word highlighted in accent purple `#6C63FF`. This is the comment trigger:

```json
{"type": "outro", "title": "Want to see it in action?", "body": "Comment DEMO and I'll send you a link.", "cta_word": "DEMO"}
```

Changes per post. Match the word exactly. Common options: `DEMO`, `MENU`, `YES`, `GUIDE`, `FREE`.

---

## Dependencies

```bash
pip install Pillow
```

Fonts expected at:
- `brand-assets/fonts/inter-bold.ttf`
- `brand-assets/fonts/JetBrainsMono-Regular.ttf` — download from jetbrains.com/lp/mono
- `brand-assets/fonts/JetBrainsMono-Bold.ttf`

Logo expected at: `brand-assets/Click AI Logos/click-logo-white.png` (white version for dark background)

All assets optional — skill runs with PIL defaults if missing.

---

## Workflow when asked for an Instagram or Facebook carousel

1. Read SKILL.md
2. Decide slide count (4-9 total, 1 intro, 1 outro, rest content)
3. Write copy — ALL CAPS headlines, punchy direct body
4. Choose `cta_word` for outro
5. Build JSON
6. Run: `python .claude/skills/carousel-ig-facebook/generate.py input.json --platform instagram`
7. Report folder path and slide count to Hadi
