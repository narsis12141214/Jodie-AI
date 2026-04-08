# Jodie Briefing — Carousel Builder Skill
## Deployed: 8 April 2026

---

## What this skill does

Generates branded PNG carousel slides (1080x1350px) for @clickaiagency on Instagram and LinkedIn. Takes a JSON input file with slide copy, renders each slide using Python PIL, outputs PNGs to `projects/carousels/`.

---

## Files

| File | Purpose |
|------|---------|
| `generate.py` | Python renderer — runs locally, no external API calls |
| `SKILL.md` | Brand rules, input contract, output contract — read every time |
| `jodie-briefing_carousel-builder_2026-04-08.md` | This file |

---

## How to use

1. Write slide copy following the input JSON contract in SKILL.md
2. Save as a `.json` file (e.g. `projects/carousels/input-topic-name.json`)
3. Run: `python .claude/skills/carousel-builder/generate.py input.json --platform linkedin`
4. Slides output to: `projects/carousels/YYYY-MM-DD-{slug}-{platform}/`

---

## Dependencies

Install once if not already installed:
```bash
pip install Pillow
```

Fonts expected at `brand-assets/fonts/inter-bold.ttf` and `brand-assets/fonts/inter-regular.ttf`. If missing, PIL default font is used automatically.

Logo expected at `/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI/brand-assets/Click AI Logos/click-logo.png`.

---

## Bug fixed on deploy (8 April 2026)

The `slugify` function was accidentally embedded as dead code inside `resolve_path()` — both functions returned early before reaching the slugify logic. The `slugify` function was extracted as a standalone function. Script would have crashed with `NameError: name 'slugify' is not defined` at runtime without this fix.

---

## Platform configs

| Platform | Background | Text | Accent |
|----------|-----------|------|--------|
| instagram | `#0A0D14` (dark) | `#FFFFFF` | `#6C63FF` |
| linkedin | `#FFFFFF` (white) | `#0A0A0A` | `#6C63FF` |

---

## Standing rules (from Strategist brief)

- Never say: game-changing, revolutionary, cutting-edge, leverage, unlock, empower
- Always say: concrete outcomes, specific problems, real numbers
- Intro slide: tension or curiosity — problem, contrast, or surprising fact
- Outro CTA: low-friction — comment, DM, link. Never ask for a call on first touch
- Carousels earn the right to start a conversation. They do not close deals.
