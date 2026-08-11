#!/usr/bin/env python3
"""Generate LaMure Aesthetic Clinic (Chelsea) Service Agreement PDF.

Premium editorial design for a high-end Chelsea aesthetic clinic client.
Palette: cream + charcoal + muted gold. Wide margins, small-caps eyebrows,
gold accents, elegant table treatments.

Bundle: Meta+WhatsApp ads (£400) + Google ads (£400) + Content (£400)
        + Voice + Click Desk Pro (£490) = £1,690/mo standard.
First month promo: £200 credit on the voice line = £1,490 first month.
Setup: £350 one-off, payable on signing.
Term: 12 months initial, then monthly rolling with 30-day notice.
Voice: 500 mins/mo included, unlimited messages, £0.30/min overage.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image,
    KeepTogether,
)

OUTPUT = "/Users/hadi/Developer/Jodie-AI/projects/agency/28-07-26/lamure-aesthetic-clinic-agreement.pdf"

# --- Premium aesthetics palette ---
CREAM       = colors.HexColor("#FBF6EE")   # body background
CREAM_DK    = colors.HexColor("#F3EBDD")   # subtle card fill
CHARCOAL    = colors.HexColor("#1A1613")   # primary text, header block
INK         = colors.HexColor("#2A2320")   # secondary text
BODY        = colors.HexColor("#3A322D")   # body text
GOLD        = colors.HexColor("#B8945A")   # primary accent
GOLD_DK     = colors.HexColor("#8F6E3A")   # darker gold for hover-like states
GOLD_SOFT   = colors.HexColor("#D9BC85")   # softer gold for tables
TAUPE       = colors.HexColor("#8A7A6D")   # secondary text
NUDE        = colors.HexColor("#EDDDCE")   # very subtle fill
HAIR        = colors.HexColor("#E4D8C6")   # hairline dividers
WHITE       = colors.HexColor("#FFFFFF")

W, H = A4
MARGIN = 22 * mm
BAND_H = 55 * mm

LOGO_PATHS = [
    "/Users/hadi/Developer/Jodie-AI/brand-assets/Click AI Logos/click-logo-white.png",
    "/Users/hadi/Developer/Jodie-AI/brand-assets/Click AI Logos/click-logo.png",
]
LOGO = next((p for p in LOGO_PATHS if os.path.exists(p)), None)


def _s(name, **kw):
    return ParagraphStyle(name, **kw)


S = {
    "hero_eyebrow": _s("hero_eyebrow", fontName="Helvetica-Bold", fontSize=8.5,
                       textColor=GOLD_SOFT, leading=11),
    "hero_title": _s("hero_title", fontName="Helvetica-Bold", fontSize=28,
                     textColor=WHITE, leading=32, spaceAfter=4),
    "hero_sub": _s("hero_sub", fontName="Helvetica", fontSize=12,
                   textColor=colors.HexColor("#D0C5B4"), leading=16),
    "eyebrow": _s("eyebrow", fontName="Helvetica-Bold", fontSize=8,
                  textColor=GOLD_DK, leading=11, spaceAfter=4),
    "sec_title": _s("sec_title", fontName="Helvetica-Bold", fontSize=13,
                    textColor=CHARCOAL, leading=17, spaceAfter=6),
    "body": _s("body", fontName="Helvetica", fontSize=9.5, textColor=BODY,
               leading=14.5, spaceAfter=5),
    "body_bold": _s("body_bold", fontName="Helvetica-Bold", fontSize=9.5,
                    textColor=CHARCOAL, leading=14.5, spaceAfter=5),
    "body_small": _s("body_small", fontName="Helvetica", fontSize=8.5,
                     textColor=TAUPE, leading=12, spaceAfter=4),
    "meta_k": _s("meta_k", fontName="Helvetica-Bold", fontSize=7.5,
                 textColor=GOLD_DK, leading=10, spaceAfter=3),
    "meta_v": _s("meta_v", fontName="Helvetica", fontSize=9.5,
                 textColor=CHARCOAL, leading=13),
    "th_dark": _s("th_dark", fontName="Helvetica-Bold", fontSize=9,
                  textColor=WHITE, leading=12),
    "td": _s("td", fontName="Helvetica", fontSize=9.5, textColor=BODY,
             leading=14, spaceAfter=0),
    "td_bold": _s("td_bold", fontName="Helvetica-Bold", fontSize=9.5,
                  textColor=CHARCOAL, leading=14),
    "amount": _s("amount", fontName="Helvetica-Bold", fontSize=10.5,
                 textColor=CHARCOAL, leading=14, alignment=TA_RIGHT),
    "amount_gold": _s("amount_gold", fontName="Helvetica-Bold", fontSize=11,
                      textColor=GOLD_DK, leading=14, alignment=TA_RIGHT),
    "term_label": _s("term_label", fontName="Helvetica-Bold", fontSize=8.5,
                     textColor=GOLD_DK, leading=11, spaceAfter=2),
    "term_body": _s("term_body", fontName="Helvetica", fontSize=9.5,
                    textColor=BODY, leading=14.5, spaceAfter=8),
    "sig_label": _s("sig_label", fontName="Helvetica-Bold", fontSize=8,
                    textColor=GOLD_DK, leading=11, spaceAfter=6),
    "sig_party": _s("sig_party", fontName="Helvetica-Bold", fontSize=10,
                    textColor=CHARCOAL, leading=14, spaceAfter=8),
    "sig_line": _s("sig_line", fontName="Helvetica", fontSize=9,
                   textColor=BODY, leading=22),
    "footer": _s("footer", fontName="Helvetica", fontSize=7.5, textColor=TAUPE,
                 leading=10, alignment=TA_CENTER),
}


def _page_bg(canvas):
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)


def first_page(canvas, doc):
    canvas.saveState()
    _page_bg(canvas)
    # Charcoal hero band
    canvas.setFillColor(CHARCOAL)
    canvas.rect(0, H - BAND_H, W, BAND_H, fill=1, stroke=0)
    # Gold accent line
    canvas.setFillColor(GOLD)
    canvas.rect(0, H - BAND_H - 0.6 * mm, W, 0.6 * mm, fill=1, stroke=0)
    # Logo (white) top-left
    if LOGO:
        try:
            canvas.drawImage(LOGO, MARGIN, H - 20 * mm, width=22 * mm,
                             height=22 * mm, preserveAspectRatio=True,
                             mask='auto')
        except Exception:
            pass
    # Eyebrow top right
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(GOLD_SOFT)
    canvas.drawRightString(W - MARGIN, H - 14 * mm,
                           "C L I C K   A I   A G E N C Y")
    # Hero eyebrow
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.setFillColor(GOLD_SOFT)
    canvas.drawString(MARGIN, H - 30 * mm, "S E R V I C E   A G R E E M E N T")
    # Hero title
    canvas.setFont("Helvetica-Bold", 27)
    canvas.setFillColor(WHITE)
    canvas.drawString(MARGIN, H - 42 * mm, "LaMure Aesthetic Clinic")
    # Sub-line
    canvas.setFont("Helvetica", 11.5)
    canvas.setFillColor(colors.HexColor("#D0C5B4"))
    canvas.drawString(MARGIN, H - 49 * mm,
                      "In partnership with Click AI Agency  ·  Chelsea, London")
    footer(canvas, doc)
    canvas.restoreState()


def later_pages(canvas, doc):
    canvas.saveState()
    _page_bg(canvas)
    # Slim charcoal top band
    canvas.setFillColor(CHARCOAL)
    canvas.rect(0, H - 12 * mm, W, 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, H - 12.5 * mm, W, 0.5 * mm, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.setFillColor(WHITE)
    canvas.drawString(MARGIN, H - 8 * mm,
                      "Service Agreement  ·  LaMure Aesthetic Clinic")
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.setFillColor(GOLD_SOFT)
    canvas.drawRightString(W - MARGIN, H - 8 * mm, "CLICK AI AGENCY")
    footer(canvas, doc)
    canvas.restoreState()


def footer(canvas, doc):
    canvas.setStrokeColor(GOLD_SOFT)
    canvas.setLineWidth(0.4)
    canvas.line(MARGIN, 16 * mm, W - MARGIN, 16 * mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(TAUPE)
    canvas.drawString(MARGIN, 11 * mm,
                      "Click AI Agency Ltd  ·  clickaiagency.com  "
                      "·  hello@clickaiagency.com")
    canvas.drawRightString(W - MARGIN, 11 * mm,
                           f"Page {canvas.getPageNumber()}")


def section(eyebrow, title):
    return [
        Spacer(1, 10),
        Paragraph(eyebrow.upper(), S["eyebrow"]),
        Paragraph(title, S["sec_title"]),
        HRFlowable(width="100%", thickness=0.5, color=GOLD,
                   spaceBefore=2, spaceAfter=10),
    ]


def meta_card(k, v):
    inner = Table([[Paragraph(k, S["meta_k"])], [Paragraph(v, S["meta_v"])]],
                  colWidths=[52 * mm])
    inner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NUDE),
        ("LINEABOVE", (0, 0), (-1, 0), 1.2, GOLD),
        ("TOPPADDING", (0, 0), (-1, 0), 7),
        ("TOPPADDING", (0, 1), (-1, 1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 0),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 9),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return inner


story = []
# Push content below the hero band on page 1
story.append(Spacer(1, BAND_H - MARGIN + 6 * mm))

# Meta cards row
meta = Table([[
    meta_card("PREPARED FOR", "LaMure Aesthetic Clinic<br/>Chelsea, London"),
    meta_card("DATE", "28 July 2026<br/>&nbsp;"),
    meta_card("CONTRACT REF.", "CLK-LAM-2026-07<br/>&nbsp;"),
]], colWidths=[
    (W - 2 * MARGIN - 8 * mm) / 3,
    (W - 2 * MARGIN - 8 * mm) / 3,
    (W - 2 * MARGIN - 8 * mm) / 3,
])
meta.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
]))
story.append(meta)

# ---------- 1. PARTIES ----------
story += section("Section 01", "Parties")
parties_data = [
    [Paragraph("<b>Service Provider</b>", S["td_bold"]),
     Paragraph("Click AI Agency Ltd", S["td"])],
    [Paragraph("<b>Client business name</b>", S["td_bold"]),
     Paragraph("LaMure Aesthetic Clinic (Chelsea)", S["td"])],
    [Paragraph("<b>Legal entity name (if different)</b>", S["td_bold"]),
     Paragraph("_______________________________________________", S["td"])],
    [Paragraph("<b>Company registration number</b>", S["td_bold"]),
     Paragraph("_______________________________________________", S["td"])],
    [Paragraph("<b>Registered address</b>", S["td_bold"]),
     Paragraph("_______________________________________________", S["td"])],
    [Paragraph("<b>Contact name</b>", S["td_bold"]),
     Paragraph("_______________________________________________", S["td"])],
    [Paragraph("<b>Contact email</b>", S["td_bold"]),
     Paragraph("_______________________________________________", S["td"])],
    [Paragraph("<b>Contact phone</b>", S["td_bold"]),
     Paragraph("_______________________________________________", S["td"])],
]
pt = Table(parties_data, colWidths=[60 * mm, W - 2 * MARGIN - 60 * mm])
pt.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
story.append(pt)

# ---------- 2. SERVICES ----------
story += section("Section 02", "Services included")
story.append(Paragraph(
    "This Agreement provides four service lines, delivered together as a "
    "single monthly package.", S["body"]))
story.append(Spacer(1, 4))

svc_data = [
    [Paragraph("SERVICE LINE", S["th_dark"]),
     Paragraph("WHAT IS DELIVERED", S["th_dark"]),
     Paragraph("MONTHLY FEE", S["th_dark"])],

    [Paragraph("<b>01</b><br/><b>Meta &amp; WhatsApp campaign</b>", S["td_bold"]),
     Paragraph("End-to-end campaign management across Instagram, Facebook, "
               "and WhatsApp: strategy, audience targeting, creative "
               "direction, campaign build, day-to-day optimisation, monthly "
               "performance report. <b>Includes ad spend.</b>", S["td"]),
     Paragraph("£400.00", S["amount"])],

    [Paragraph("<b>02</b><br/><b>Google campaign</b>", S["td_bold"]),
     Paragraph("End-to-end campaign management across Google Ads (Search), "
               "Google Maps local ads, and YouTube: keyword strategy, "
               "geo-targeting, ad build, day-to-day optimisation, monthly "
               "performance report. <b>Includes ad spend.</b>", S["td"]),
     Paragraph("£400.00", S["amount"])],

    [Paragraph("<b>03</b><br/><b>Content creation</b>", S["td_bold"]),
     Paragraph("Daily social content for Instagram (auto-shared to "
               "Facebook): a mix of feed posts, reels, and stories. Planning, "
               "creative production, scheduling, and posting under LaMure's "
               "brand identity.", S["td"]),
     Paragraph("£400.00", S["amount"])],

    [Paragraph("<b>04</b><br/><b>AI voice receptionist &amp; Click Desk Pro</b>",
               S["td_bold"]),
     Paragraph("24/7 AI voice agent trained on LaMure's treatments, opening "
               "hours, and booking rules. 500 voice minutes per month "
               "included; unlimited SMS and WhatsApp messages from the "
               "agent. Full access to Click Desk Pro: loyalty programme, "
               "advanced feedback and review system, client management, "
               "appointments, consents, payments.", S["td"]),
     Paragraph("£490.00", S["amount"])],

    [Paragraph("<b>Standard monthly total</b>", S["td_bold"]),
     Paragraph("", S["td"]),
     Paragraph("<b>£1,690.00</b>", S["amount_gold"])],
]
svc_table = Table(svc_data,
                  colWidths=[42 * mm, W - 2 * MARGIN - 42 * mm - 28 * mm, 28 * mm])
svc_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), CHARCOAL),
    ("BACKGROUND", (0, -1), (-1, -1), CREAM_DK),
    ("ROWBACKGROUNDS", (0, 1), (-1, -2), [WHITE, colors.HexColor("#FBF7F0")]),
    ("LINEABOVE", (0, 0), (-1, 0), 0.5, GOLD),
    ("LINEBELOW", (0, 0), (-1, 0), 0.5, GOLD),
    ("LINEBELOW", (0, -1), (-1, -1), 0.6, GOLD),
    ("LINEBEFORE", (0, 0), (0, -1), 0.3, HAIR),
    ("LINEAFTER", (-1, 0), (-1, -1), 0.3, HAIR),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 9),
    ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
]))
story.append(svc_table)
story.append(Spacer(1, 5))
story.append(Paragraph(
    "The £400.00 per campaign line covers all-in delivery: creative production, "
    "campaign build, day-to-day optimisation, monthly performance reporting, "
    "and the actual advertising budget spent on the respective platforms. "
    "Total monthly advertising budget across both campaigns is £800.00, "
    "split £400.00 to Google and £400.00 to Meta &amp; WhatsApp. The Client "
    "will not receive separate invoices from Meta, Google, or any other "
    "advertising platform under this Agreement.", S["body_small"]))

# ---------- 3. COMMERCIAL SUMMARY ----------
story += section("Section 03", "Commercial summary")

cs_data = [
    [Paragraph("ITEM", S["th_dark"]),
     Paragraph("AMOUNT", S["th_dark"])],
    [Paragraph("One-off setup fee, payable on signing", S["td"]),
     Paragraph("<b>£350.00</b>", S["amount_gold"])],
    [Paragraph("First month total (with £200.00 welcome credit against the "
               "AI voice receptionist and Click Desk Pro line)", S["td"]),
     Paragraph("<b>£1,490.00</b>", S["amount_gold"])],
    [Paragraph("Standard monthly total (month 2 onwards)", S["td"]),
     Paragraph("<b>£1,690.00</b>", S["amount_gold"])],
    [Paragraph("Voice usage over 500 minutes per calendar month", S["td"]),
     Paragraph("£0.30 per minute", S["amount"])],
]
cs_table = Table(cs_data, colWidths=[W - 2 * MARGIN - 55 * mm, 55 * mm])
cs_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), CHARCOAL),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1),
     [WHITE, colors.HexColor("#FBF7F0")]),
    ("LINEABOVE", (0, 0), (-1, 0), 0.5, GOLD),
    ("LINEBELOW", (0, 0), (-1, 0), 0.5, GOLD),
    ("LINEBELOW", (0, -1), (-1, -1), 0.5, GOLD),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
]))
story.append(cs_table)

# ---------- 4. PAYMENT SCHEDULE ----------
story += section("Section 04", "Payment schedule")

pay_data = [
    [Paragraph("WHEN", S["th_dark"]),
     Paragraph("WHAT", S["th_dark"])],
    [Paragraph("<b>On signature</b>", S["td_bold"]),
     Paragraph("Setup fee of £350.00 payable within 3 business days of "
               "signing this Agreement. Setup work begins on receipt of the "
               "setup fee.", S["td"])],
    [Paragraph("<b>Go-live (day 0)</b>", S["td_bold"]),
     Paragraph("The Service Provider activates the full package. The go-live "
               "date will be confirmed in writing to the Client at least 24 "
               "hours in advance.", S["td"])],
    [Paragraph("<b>Month 1</b>", S["td_bold"]),
     Paragraph("First month fee of <b>£1,490.00</b> (standard £1,690.00 "
               "less the £200.00 welcome credit against the AI voice "
               "receptionist and Click Desk Pro line). Invoiced on the "
               "go-live date, payable within 7 days.", S["td"])],
    [Paragraph("<b>Month 2 onwards</b>", S["td_bold"]),
     Paragraph("<b>£1,690.00</b> per calendar month. Invoiced on the same "
               "day of each month, payable within 7 days of invoice.",
               S["td"])],
    [Paragraph("<b>Overage</b>", S["td_bold"]),
     Paragraph("Voice usage above 500 minutes in a calendar month is charged "
               "at £0.30 per minute, billed in arrears alongside the next "
               "monthly invoice. An automatic usage reminder is issued when "
               "the Client reaches 85% of the monthly voice allowance.",
               S["td"])],
]
pay_table = Table(pay_data, colWidths=[42 * mm, W - 2 * MARGIN - 42 * mm])
pay_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), CHARCOAL),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1),
     [WHITE, colors.HexColor("#FBF7F0")]),
    ("LINEABOVE", (0, 0), (-1, 0), 0.5, GOLD),
    ("LINEBELOW", (0, 0), (-1, 0), 0.5, GOLD),
    ("LINEBELOW", (0, -1), (-1, -1), 0.5, GOLD),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
]))
story.append(pay_table)

# ---------- 5. KEY TERMS ----------
story += section("Section 05", "Key terms")

terms = [
    ("Term",
     "This Agreement runs for an initial term of 12 months from the go-live "
     "date. Following the initial 12-month term, the Agreement continues on "
     "a monthly rolling basis until either party gives 30 days written "
     "notice to terminate. Any notice given during the initial term takes "
     "effect no earlier than the last day of the initial 12-month term."),
    ("Cancellation",
     "After the initial 12-month term, either party may terminate this "
     "Agreement by giving 30 days written notice. Termination for material "
     "breach by either party is available at any time in accordance with the "
     "full Terms and Conditions."),
    ("Welcome credit",
     "The £200.00 first-month credit is a one-off welcome benefit against "
     "the AI voice receptionist and Click Desk Pro line. It applies to the "
     "Client's first invoice under this Agreement."),
    ("Setup fee",
     "The £350.00 setup fee is non-refundable once setup work has begun. "
     "Setup includes configuring the voice agent, loading the treatments "
     "knowledge base, activating Click Desk Pro, integrating calendars and "
     "payments, building the ad accounts, and testing the system before "
     "go-live."),
    ("Voice minutes",
     "500 voice minutes per calendar month are included in the £490.00 AI "
     "voice receptionist and Click Desk Pro line. Voice usage above 500 "
     "minutes is charged at £0.30 per minute per the payment schedule "
     "above."),
    ("Advertising spend",
     "The total monthly advertising budget is £800.00, split evenly between "
     "the two campaigns: £400.00 to the Google campaign (Google Ads, Google "
     "Maps, YouTube) and £400.00 to the Meta &amp; WhatsApp campaign "
     "(Instagram, Facebook, WhatsApp). The Service Provider will allocate "
     "spend across the platforms within each campaign in a way that best "
     "serves the Client's stated business objectives (bookings, enquiries, "
     "foot traffic, brand awareness)."),
    ("Content approvals",
     "The Client will nominate one point of contact empowered to approve "
     "content. Content is delivered on a rolling schedule and treated as "
     "approved unless the nominated contact objects in writing within 2 "
     "business days of receipt."),
    ("Advertising compliance",
     "All content, ads, and voice-agent scripts produced by the Service "
     "Provider will follow the UK Advertising Standards Authority (ASA) "
     "rules and Committee of Advertising Practice (CAP) code, including the "
     "specific restrictions that apply to aesthetic and cosmetic treatments. "
     "Prescription-only medicines will not be advertised by brand name. The "
     "Client is responsible for the medical accuracy of any clinical claims "
     "requested."),
    ("Performance standard",
     "The Service Provider commits to deliver the services described in "
     "this Agreement to a high professional standard, with continuous "
     "campaign optimisation and monthly performance reporting to the Client. "
     "Advertising and content outcomes are influenced by factors including "
     "market conditions, competition, seasonality, treatment mix, and price "
     "positioning; specific booking, revenue, or return-on-ad-spend figures "
     "are set and reviewed with the Client campaign by campaign rather than "
     "fixed in this Agreement."),
    ("Additional charges",
     "Any expense over £100 outside the scope of this Agreement (for "
     "example, paid third-party tools, influencer fees, printed materials, "
     "additional voice minute allowance) requires the Client's written "
     "approval before the Service Provider proceeds."),
    ("Your data",
     "The Client owns all data held in the Click Desk Pro platform, all "
     "customer records, all voice agent call records, and all advertising "
     "accounts created on the Client's behalf. The Service Provider "
     "complies with UK GDPR. On termination, all data will be exported and "
     "returned to the Client within 14 days, and administrator access to "
     "any ad accounts registered under the Client's name will be handed "
     "over."),
    ("Intellectual property",
     "The Client owns all final creative assets delivered under this "
     "Agreement (posts, reels, stories, ad creative). The Service Provider "
     "retains the right to use anonymised performance metrics and creative "
     "examples in its own portfolio."),
    ("Confidentiality",
     "The Service Provider will not disclose customer data, financial "
     "information, pricing arrangements, treatment protocols, or any "
     "information designated by the Client as confidential."),
    ("Service availability",
     "The Service Provider targets 99% uptime per calendar month on the "
     "Click Desk Pro platform and the voice agent, excluding scheduled "
     "maintenance windows notified in advance."),
]

for label, text in terms:
    story.append(Paragraph(label.upper(), S["term_label"]))
    story.append(Paragraph(text, S["term_body"]))

# ---------- Full T&Cs reference ----------
story.append(Spacer(1, 4))
story.append(Paragraph(
    "This summary agreement is governed by the full Terms and Conditions "
    "available at clickaiagency.com/terms. By signing below, the Client "
    "agrees to both this summary and the full Terms and Conditions.",
    S["body_small"]))

# ---------- 6. SIGNATURES ----------
signature_block = []
signature_block += section("Section 06", "Signatures")

sig_data = [
    [Paragraph("FOR THE SERVICE PROVIDER", S["sig_label"]),
     Paragraph("FOR THE CLIENT", S["sig_label"])],
    [Paragraph("Click AI Agency Ltd", S["sig_party"]),
     Paragraph("Company:&nbsp;&nbsp;__________________________", S["sig_line"])],
    [Paragraph("Name:&nbsp;&nbsp;Hadi Yazdani", S["sig_line"]),
     Paragraph("Name:&nbsp;&nbsp;__________________________", S["sig_line"])],
    [Paragraph("Title:&nbsp;&nbsp;CEO and Founder", S["sig_line"]),
     Paragraph("Title:&nbsp;&nbsp;__________________________", S["sig_line"])],
    [Paragraph("Signature:&nbsp;&nbsp;__________________", S["sig_line"]),
     Paragraph("Signature:&nbsp;&nbsp;__________________", S["sig_line"])],
    [Paragraph("Date:&nbsp;&nbsp;____________________", S["sig_line"]),
     Paragraph("Date:&nbsp;&nbsp;______________________", S["sig_line"])],
]
sig_table = Table(sig_data,
                  colWidths=[(W - 2 * MARGIN - 10 * mm) / 2,
                             (W - 2 * MARGIN - 10 * mm) / 2])
sig_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ("LINEBELOW", (0, 0), (-1, 0), 0.5, GOLD),
]))
signature_block.append(sig_table)

story.append(KeepTogether(signature_block))
story.append(Spacer(1, 8))
story.append(Paragraph(
    "Click AI Agency Ltd  ·  Companies House registered  ·  "
    "hello@clickaiagency.com  ·  clickaiagency.com",
    S["footer"]))


doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=15 * mm, bottomMargin=22 * mm,
    title="Service Agreement - LaMure Aesthetic Clinic",
    author="Click AI Agency",
    subject="Service Agreement - LaMure Chelsea",
)
doc.build(story, onFirstPage=first_page, onLaterPages=later_pages)
print(f"LaMure Aesthetic Clinic agreement generated at: {OUTPUT}")
