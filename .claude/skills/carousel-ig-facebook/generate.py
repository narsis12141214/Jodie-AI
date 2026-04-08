#!/usr/bin/env python3
"""
Carousel Slide Generator — Click AI Agency
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
FONT_BASE = "brand-assets/fonts"

BRAND_INSTAGRAM = {
    "handle": "@clickaiagency",
    "display_name": "Click AI Agency",
    "background_color": "#0A0D14",
    "text_color": "#FFFFFF",
    "subtext_color": "#8A8F9E",
    "accent_color": "#6C63FF",
    "font_headline": f"{FONT_BASE}/inter-bold.ttf",
    "font_mono": f"{FONT_BASE}/JetBrainsMono-Regular.ttf",
    "font_mono_bold": f"{FONT_BASE}/JetBrainsMono-Bold.ttf",
    "logo_path": "brand-assets/Click AI Logos/click-logo-white.png",
}

BRAND_LINKEDIN = {
    "handle": "@clickaiagency",
    "display_name": "Click AI Agency",
    "background_color": "#FFFFFF",
    "text_color": "#0A0A0A",
    "subtext_color": "#6B7280",
    "accent_color": "#6C63FF",
    "font_headline": f"{FONT_BASE}/inter-bold.ttf",
    "font_body": f"{FONT_BASE}/inter-regular.ttf",
    "logo_path": LOGO_PATH,
}

# —— Canvas ————————————————————————————————————————————————————————————————————

W, H = 1080, 1350
MARGIN_X = 80
SAFE_W = W - MARGIN_X * 2

# —— Helpers ————————————————————————————————————————————————————————————————————

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def resolve_path(base_dir, path):
    if os.path.isabs(path):
        return path
    return os.path.join(base_dir, path)

def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        print(f"⚠  Font not found: {path} — using default")
        return ImageFont.load_default()

def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines, current = [], []
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

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    return re.sub(r'\s+', '-', text.strip())

def circle_crop(img, size):
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new('L', (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size, size), fill=255)
    result = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    result.paste(img.convert('RGBA'), (0, 0), mask)
    return result

def paste_logo(img, logo_path, top, size=72):
    draw = ImageDraw.Draw(img)
    if not os.path.exists(logo_path):
        return img, draw, MARGIN_X
    try:
        logo = Image.open(logo_path).convert("RGBA")
        ratio = size / logo.height
        logo = logo.resize((int(logo.width * ratio), size), Image.LANCZOS)
        logo_circle = circle_crop(logo, size)
        img.paste(logo_circle, (MARGIN_X, top), logo_circle)
        draw = ImageDraw.Draw(img)
        return img, draw, MARGIN_X + size + 18
    except Exception as e:
        print(f"⚠  Logo: {e}")
        return img, draw, MARGIN_X

def draw_highlighted_text(draw, x, y, text, highlight_word, font, base_color, highlight_color):
    words = text.split()
    cursor_x = x
    for word in words:
        clean = re.sub(r'[^\w]', '', word)
        suffix = word[len(clean):]
        color = highlight_color if clean.upper() == highlight_word.upper() else base_color
        draw.text((cursor_x, y), clean + suffix, font=font, fill=color)
        cursor_x += draw.textlength(word + ' ', font=font)

# —— INSTAGRAM renderer ————————————————————————————————————————————————————————

def draw_verified_badge(draw, x, y, size, acc_color):
    """Draw a filled blue circle with a white tick."""
    draw.ellipse([(x, y), (x + size, y + size)], fill=acc_color)
    tick_pts = [
        (x + int(size * 0.22), y + int(size * 0.52)),
        (x + int(size * 0.42), y + int(size * 0.72)),
        (x + int(size * 0.78), y + int(size * 0.28)),
    ]
    draw.line([tick_pts[0], tick_pts[1]], fill=(255, 255, 255), width=max(2, size // 10))
    draw.line([tick_pts[1], tick_pts[2]], fill=(255, 255, 255), width=max(2, size // 10))

def draw_instagram_header(img, draw, cfg, base_dir, header_y, acc):
    """Draw logo + name + verified badge + handle. Returns updated img, draw."""
    font_name   = load_font(resolve_path(base_dir, cfg["font_mono_bold"]), 38)
    font_handle = load_font(resolve_path(base_dir, cfg["font_mono"]), 32)

    logo_path = resolve_path(base_dir, cfg["logo_path"])
    img, draw, logo_right = paste_logo(img, logo_path, header_y, size=100)

    name_x = logo_right
    name_y = header_y + 14
    draw.text((name_x, name_y), cfg["display_name"], font=font_name, fill=(255, 255, 255))

    name_w = int(draw.textlength(cfg["display_name"], font=font_name))
    badge_size = 28
    badge_x = name_x + name_w + 10
    badge_y = name_y + 6
    draw_verified_badge(draw, badge_x, badge_y, badge_size, acc)

    draw.text((name_x, name_y + 50), cfg["handle"], font=font_handle,
              fill=hex_to_rgb(cfg["subtext_color"]))

    return img, draw

def draw_instagram_slide(slide, index, total, cfg, base_dir):
    bg  = hex_to_rgb(cfg["background_color"])
    fg  = hex_to_rgb(cfg["text_color"])
    sub = hex_to_rgb(cfg["subtext_color"])
    acc = hex_to_rgb(cfg["accent_color"])
    swipe_col = (100, 100, 100)

    img  = Image.new('RGB', (W, H), bg)
    draw = ImageDraw.Draw(img)

    font_bold    = load_font(resolve_path(base_dir, cfg["font_headline"]), 72)
    font_mono    = load_font(resolve_path(base_dir, cfg["font_mono"]), 40)
    font_mono_bd = load_font(resolve_path(base_dir, cfg["font_mono_bold"]), 44)
    font_mono_sm = load_font(resolve_path(base_dir, cfg["font_mono"]), 28)

    slide_type = slide.get("type", "content")
    title      = slide.get("title", "").upper()
    body       = slide.get("body", "")
    cta_word   = slide.get("cta_word", "")
    is_last    = (index == total)

    header_y = int(H * 0.22)
    img, draw = draw_instagram_header(img, draw, cfg, base_dir, header_y, acc)
    content_start = header_y + 100 + 70

    if not is_last:
        sw = "----->"
        sw_w = draw.textlength(sw, font=font_mono_sm)
        draw.text((W - MARGIN_X - sw_w, H - 90), sw, font=font_mono_sm, fill=swipe_col)

    # —— INTRO ————————————————————————————————————————————————————————————————
    if slide_type == "intro":
        headline_y = content_start
        lines = wrap_text(draw, title, font_bold, SAFE_W)
        for line in lines[:4]:
            draw.text((MARGIN_X, headline_y), line, font=font_bold, fill=fg)
            headline_y += 90
        if body:
            body_y = headline_y + 44
            for line in wrap_text(draw, body, font_mono, SAFE_W):
                draw.text((MARGIN_X, body_y), line, font=font_mono, fill=fg)
                body_y += 60

    # —— CONTENT ——————————————————————————————————————————————————————————————
    elif slide_type == "content":
        content_y = content_start
        numbered = f"{index - 1} | {title}"
        lines = wrap_text(draw, numbered, font_mono_bd, SAFE_W)
        for line in lines[:3]:
            draw.text((MARGIN_X, content_y), line, font=font_mono_bd, fill=fg)
            content_y += 62
        if body:
            body_y = content_y + 44
            for line in wrap_text(draw, body, font_mono, SAFE_W):
                draw.text((MARGIN_X, body_y), line, font=font_mono, fill=sub)
                body_y += 58

    # —— OUTRO ————————————————————————————————————————————————————————————————
    elif slide_type == "outro":
        title_lines = wrap_text(draw, title, font_bold, SAFE_W)
        body_lines  = wrap_text(draw, body, font_mono, SAFE_W) if body else []
        start_y = content_start + 40
        for line in title_lines:
            draw.text((MARGIN_X, start_y), line, font=font_bold, fill=fg)
            start_y += 90
        if body_lines:
            start_y += 36
            for line in body_lines:
                if cta_word:
                    draw_highlighted_text(draw, MARGIN_X, start_y, line,
                                          cta_word, font_mono, fg, acc)
                else:
                    draw.text((MARGIN_X, start_y), line, font=font_mono, fill=fg)
                start_y += 60

    return img

# —— LINKEDIN renderer —————————————————————————————————————————————————————————

def draw_linkedin_slide(slide, index, total, cfg, base_dir):
    bg  = hex_to_rgb(cfg["background_color"])
    fg  = hex_to_rgb(cfg["text_color"])
    sub = hex_to_rgb(cfg["subtext_color"])
    acc = hex_to_rgb(cfg["accent_color"])
    swipe_col = tuple(int(bg[c] * 0.4) for c in range(3))

    img  = Image.new('RGB', (W, H), bg)
    draw = ImageDraw.Draw(img)

    font_bold_lg = load_font(resolve_path(base_dir, cfg["font_headline"]), 108)
    font_bold_md = load_font(resolve_path(base_dir, cfg["font_headline"]), 76)
    font_body    = load_font(resolve_path(base_dir, cfg["font_body"]), 42)
    font_name    = load_font(resolve_path(base_dir, cfg["font_headline"]), 32)
    font_handle  = load_font(resolve_path(base_dir, cfg["font_body"]), 28)
    font_small   = load_font(resolve_path(base_dir, cfg["font_body"]), 26)

    slide_type = slide.get("type", "content")
    title      = slide.get("title", "")
    body       = slide.get("body", "")
    is_last    = (index == total)

    draw.text((MARGIN_X, H - 90), cfg["handle"], font=font_small, fill=sub)
    if not is_last:
        sw = "Swipe ->"
        sw_w = draw.textlength(sw, font=font_small)
        draw.text((W - MARGIN_X - sw_w, H - 90), sw, font=font_small, fill=swipe_col)

    if slide_type == "intro":
        headline_y = int(H * 0.28)
        lines = wrap_text(draw, title, font_bold_lg, SAFE_W)
        for line in lines[:4]:
            draw.text((MARGIN_X, headline_y), line, font=font_bold_lg, fill=fg)
            headline_y += 122
        accent_y = headline_y + 20
        draw.rectangle([(MARGIN_X, accent_y), (MARGIN_X + 100, accent_y + 5)], fill=acc)
        brand_y = accent_y + 30
        logo_path = resolve_path(base_dir, cfg["logo_path"])
        img, draw, logo_right = paste_logo(img, logo_path, brand_y, size=72)
        draw.text((logo_right, brand_y + 8),  cfg["display_name"], font=font_name,   fill=fg)
        draw.text((logo_right, brand_y + 44), cfg["handle"],       font=font_handle, fill=sub)

    elif slide_type == "content":
        header_y = int(H * 0.22)
        logo_path = resolve_path(base_dir, cfg["logo_path"])
        img, draw, logo_right = paste_logo(img, logo_path, header_y, size=64)
        draw.text((logo_right, header_y + 10), cfg["display_name"], font=font_handle, fill=fg)
        draw.text((logo_right, header_y + 40), cfg["handle"],       font=font_small,  fill=sub)
        headline_y = int(H * 0.38)
        for line in wrap_text(draw, title, font_bold_md, SAFE_W)[:3]:
            draw.text((MARGIN_X, headline_y), line, font=font_bold_md, fill=fg)
            headline_y += 94
        if body:
            body_y = headline_y + 36
            for line in wrap_text(draw, body, font_body, SAFE_W):
                draw.text((MARGIN_X, body_y), line, font=font_body, fill=fg)
                body_y += 60

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
        platform = sys.argv[sys.argv.index("--platform") + 1].lower()

    with open(input_path, 'r') as f:
        data = json.load(f)

    topic    = data.get("topic", "carousel")
    slides   = data.get("slides", [])
    override = data.get("brand_config", {})

    cfg = BRAND_INSTAGRAM.copy() if platform == "instagram" else BRAND_LINKEDIN.copy()
    cfg.update(override)

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    date_str = datetime.now().strftime('%Y-%m-%d')
    out_dir  = os.path.join(base_dir, 'projects', 'carousels',
                            f"{date_str}-{slugify(topic)}-{platform}")
    os.makedirs(out_dir, exist_ok=True)

    total = len(slides)
    for i, slide in enumerate(slides, 1):
        img = draw_instagram_slide(slide, i, total, cfg, base_dir) \
              if platform == "instagram" \
              else draw_linkedin_slide(slide, i, total, cfg, base_dir)

        if i == 1:
            filename = "slide-1-intro.png"
        elif i == total:
            filename = f"slide-{i}-outro.png"
        else:
            filename = f"slide-{i}.png"

        img.save(os.path.join(out_dir, filename), 'PNG')
        print(f"✓ {filename}")

    print(f"\n🎯 Slides saved to: {out_dir}")

if __name__ == "__main__":
    main()
