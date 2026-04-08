#!/usr/bin/env python3
"""
Carousel Slide Generator — Click AI Agency / Hadi Photography London
Generates branded PNG slides for Instagram and LinkedIn.
Usage: python generate.py input.json [--platform instagram|linkedin]
"""

import json
import os
import re
import sys
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# —— Brand configs ——————————————————————————————————————————————————————————————

LOGO_PATH = "/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI/brand-assets/Click AI Logos/click-logo.png"

BRAND_INSTAGRAM = {
    "handle": "@clickaiagency",
    "display_name": "Click AI Agency",
    "background_color": "#0A0D14",
    "text_color": "#FFFFFF",
    "subtext_color": "#8A8F9E",
    "accent_color": "#6C63FF",
    "page_indicator_color": "#8A8F9E",
    "swipe_color": "#8A8F9E",
    "font_headline": "brand-assets/fonts/inter-bold.ttf",
    "font_body": "brand-assets/fonts/inter-regular.ttf",
    "logo_path": LOGO_PATH,
    "headshot_path": LOGO_PATH,
}

BRAND_LINKEDIN = {
    "handle": "@clickaiagency",
    "display_name": "Click AI Agency",
    "background_color": "#FFFFFF",
    "text_color": "#0A0A0A",
    "subtext_color": "#6B7280",
    "accent_color": "#6C63FF",
    "page_indicator_color": "#9CA3AF",
    "swipe_color": "#6C63FF",
    "font_headline": "brand-assets/fonts/inter-bold.ttf",
    "font_body": "brand-assets/fonts/inter-regular.ttf",
    "logo_path": LOGO_PATH,
    "headshot_path": LOGO_PATH,
}

# —— Helpers ————————————————————————————————————————————————————————————————————

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        print(f"⚠  Font not found: {path} — using default")
        return ImageFont.load_default()

def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines = []
    current = []
    for word in words:
        test = ' '.join(current + [word])
        if draw.textlength(test, font=font) <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(' '.join(current))
            current = [word]
    if current:
        lines.append(' '.join(current))
    return lines

def resolve_path(base_dir, path):
    """Return path as-is if absolute, otherwise join with base_dir."""
    if os.path.isabs(path):
        return path
    return os.path.join(base_dir, path)

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text.strip())
    return text

def circle_crop(img, size):
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new('L', (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size, size), fill=255)
    result = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    result.paste(img.convert('RGBA'), (0, 0), mask)
    return result

# —— Canvas dimensions —————————————————————————————————————————————————————————

W, H = 1080, 1350
MARGIN_X = 80
MARGIN_TOP = 110
MARGIN_BOTTOM = 160
SAFE_W = W - MARGIN_X * 2

# —— Slide renderer ————————————————————————————————————————————————————————————

def draw_slide(slide, index, total, cfg, base_dir):
    bg = hex_to_rgb(cfg["background_color"])
    fg = hex_to_rgb(cfg["text_color"])
    sub = hex_to_rgb(cfg["subtext_color"])
    acc = hex_to_rgb(cfg["accent_color"])

    # Black at 60% opacity blended against background
    swipe_col = tuple(int(bg[c] * 0.4 + 0 * 0.6) for c in range(3))

    img = Image.new('RGB', (W, H), bg)
    draw = ImageDraw.Draw(img)

    font_bold_lg = load_font(resolve_path(base_dir, cfg["font_headline"]), 108)
    font_bold_md = load_font(resolve_path(base_dir, cfg["font_headline"]), 76)
    font_body    = load_font(resolve_path(base_dir, cfg["font_body"]), 42)
    font_name    = load_font(resolve_path(base_dir, cfg["font_headline"]), 32)
    font_handle  = load_font(resolve_path(base_dir, cfg["font_body"]), 28)
    font_small   = load_font(resolve_path(base_dir, cfg["font_body"]), 26)

    slide_type = slide.get("type", "content")
    title = slide.get("title", "")
    body  = slide.get("body", "")
    is_last = (index == total)

    # —— Shared bottom elements ————————————————————————————————————————————————
    bottom_y = H - 90  # baseline for swipe + handle text

    # Handle bottom-left (very small, subtext color) — Nate Herk style
    draw.text((MARGIN_X, bottom_y), cfg["handle"], font=font_small, fill=sub)

    # Swipe bottom-right (hide on last)
    if not is_last:
        swipe_text = "Swipe →"
        sw_w = draw.textlength(swipe_text, font=font_small)
        draw.text((W - MARGIN_X - sw_w, bottom_y), swipe_text, font=font_small, fill=swipe_col)

    # —— INTRO slide ———————————————————————————————————————————————————————————
    if slide_type == "intro":
        # Headline starts at ~30% down
        headline_y = int(H * 0.28)
        lines = wrap_text(draw, title, font_bold_lg, SAFE_W)
        for line in lines[:4]:
            draw.text((MARGIN_X, headline_y), line, font=font_bold_lg, fill=fg)
            headline_y += 122

        # Accent line below headline
        accent_y = headline_y + 20
        draw.rectangle([(MARGIN_X, accent_y), (MARGIN_X + 100, accent_y + 5)], fill=acc)

        # Branding: headshot + name + handle below accent line (Nate Herk position)
        brand_y = accent_y + 30
        hs_size = 72
        hs_path = resolve_path(base_dir, cfg["headshot_path"])
        hs_placed = False
        if os.path.exists(hs_path):
            try:
                hs = Image.open(hs_path)
                hs_circle = circle_crop(hs, hs_size)
                img.paste(hs_circle, (MARGIN_X, brand_y), hs_circle)
                draw = ImageDraw.Draw(img)
                hs_placed = True
            except Exception as e:
                print(f"⚠  Headshot: {e}")
        text_x = MARGIN_X + (hs_size + 18 if hs_placed else 0)
        draw.text((text_x, brand_y + 8), cfg["display_name"], font=font_name, fill=fg)
        draw.text((text_x, brand_y + 44), cfg["handle"], font=font_handle, fill=sub)

    # —— CONTENT slide —————————————————————————————————————————————————————————
    elif slide_type == "content":
        # Logo + handle header — lower than before, sits at ~12% down
        header_y = int(H * 0.22)
        logo_path = resolve_path(base_dir, cfg["logo_path"])
        logo_right = MARGIN_X
        if os.path.exists(logo_path):
            try:
                logo = Image.open(logo_path).convert("RGBA")
                max_h = 64
                ratio = max_h / logo.height
                logo = logo.resize((int(logo.width * ratio), max_h), Image.LANCZOS)
                bg_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
                bg_layer.paste(logo, (MARGIN_X, header_y), logo)
                img = Image.alpha_composite(img.convert('RGBA'), bg_layer).convert('RGB')
                draw = ImageDraw.Draw(img)
                logo_right = MARGIN_X + logo.width + 16
            except Exception as e:
                print(f"⚠  Logo: {e}")
        draw.text((logo_right, header_y + 10), cfg["display_name"], font=font_handle, fill=fg)
        draw.text((logo_right, header_y + 40), cfg["handle"], font=font_small, fill=sub)

        # Headline below header — pushed lower to match intro/outro visual weight
        headline_y = int(H * 0.38)
        lines = wrap_text(draw, title, font_bold_md, SAFE_W)
        for line in lines[:3]:
            draw.text((MARGIN_X, headline_y), line, font=font_bold_md, fill=fg)
            headline_y += 94

        # Body below headline
        if body:
            body_y = headline_y + 36
            body_lines = wrap_text(draw, body, font_body, SAFE_W)
            for line in body_lines:
                draw.text((MARGIN_X, body_y), line, font=font_body, fill=fg)
                body_y += 60

    # —— OUTRO slide ———————————————————————————————————————————————————————————
    elif slide_type == "outro":
        title_lines = wrap_text(draw, title, font_bold_lg, SAFE_W)
        body_lines  = wrap_text(draw, body, font_body, SAFE_W) if body else []
        block_h = len(title_lines) * 122 + (48 if body_lines else 0) + len(body_lines) * 60
        start_y = (H - block_h) // 2 - 40
        for line in title_lines:
            draw.text((MARGIN_X, start_y), line, font=font_bold_lg, fill=fg)
            start_y += 122
        if body_lines:
            start_y += 32
            for line in body_lines:
                draw.text((MARGIN_X, start_y), line, font=font_body, fill=sub)
                start_y += 60

    return img

# —— Main ——————————————————————————————————————————————————————————————————————

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate.py input.json [--platform instagram|linkedin]")
        sys.exit(1)

    input_path = sys.argv[1]
    platform = "linkedin"
    if "--platform" in sys.argv:
        idx = sys.argv.index("--platform")
        platform = sys.argv[idx + 1].lower()

    with open(input_path, 'r') as f:
        data = json.load(f)

    topic = data.get("topic", "carousel")
    slides = data.get("slides", [])
    brand_override = data.get("brand_config", {})

    # Pick base config
    cfg = BRAND_INSTAGRAM.copy() if platform == "instagram" else BRAND_LINKEDIN.copy()
    cfg.update(brand_override)

    # Resolve base dir (where generate.py lives — project root)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

    # Output folder
    date_str = datetime.now().strftime('%Y-%m-%d')
    slug = slugify(topic)
    out_dir = os.path.join(base_dir, 'projects', 'carousels', f"{date_str}-{slug}-{platform}")
    os.makedirs(out_dir, exist_ok=True)

    total = len(slides)
    for i, slide in enumerate(slides, 1):
        img = draw_slide(slide, i, total, cfg, base_dir)
        stype = slide.get("type", "content")
        if i == 1:
            filename = f"slide-1-intro.png"
        elif i == total:
            filename = f"slide-{i}-outro.png"
        else:
            filename = f"slide-{i}.png"
        out_path = os.path.join(out_dir, filename)
        img.save(out_path, 'PNG')
        print(f"✓ {filename}")

    print(f"\n🎯 Slides saved to: {out_dir}")

if __name__ == "__main__":
    main()
