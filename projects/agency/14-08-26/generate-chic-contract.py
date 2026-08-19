#!/usr/bin/env python3
"""Generate Chic Salon & Clinic (Willesden) Service Agreement PDF.

Deal structure (as confirmed 14 August 2026):
- Website: £400 one-off, ALREADY PAID (delivered / in progress)
- Monthly social media management (IG + FB): £400/mo
- Monthly AI voice receptionist + Click Desk Pro: £290/mo (500 mins, £0.30/min overage)
- Standard monthly total: £690
- Term: monthly rolling with 30 days notice from day one (default — Hadi may override)

Same premium editorial template as LaMure (charcoal + gold + cream).
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

OUTPUT = "/Users/hadi/Developer/Jodie-AI/projects/agency/14-08-26/chic-salon-clinic-agreement.pdf"

# Same palette family as LaMure
CREAM       = colors.HexColor("#FBF6EE")
CREAM_DK    = colors.HexColor("#F3EBDD")
CHARCOAL    = colors.HexColor("#1A1613")
INK         = colors.HexColor("#2A2320")
BODY        = colors.HexColor("#3A322D")
GOLD        = colors.HexColor("#B8945A")
GOLD_DK     = colors.HexColor("#8F6E3A")
GOLD_SOFT   = colors.HexColor("#D9BC85")
TAUPE       = colors.HexColor("#8A7A6D")
NUDE        = colors.HexColor("#EDDDCE")
HAIR        = colors.HexColor("#E4D8C6")
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
    "amount_taupe": _s("amount_taupe", fontName="Helvetica", fontSize=9.5,
                       textColor=TAUPE, leading=14, alignment=TA_RIGHT),
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
    canvas.setFillColor(CHARCOAL)
    canvas.rect(0, H - BAND_H, W, BAND_H, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, H - BAND_H - 0.6 * mm, W, 0.6 * mm, fill=1, stroke=0)
    if LOGO:
        try:
            canvas.drawImage(LOGO, MARGIN, H - 20 * mm, width=22 * mm,
                             height=22 * mm, preserveAspectRatio=True,
                             mask='auto')
        except Exception:
            pass
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(GOLD_SOFT)
    canvas.drawRightString(W - MARGIN, H - 14 * mm,
                           "C L I C K   A I   A G E N C Y")
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.setFillColor(GOLD_SOFT)
    canvas.drawString(MARGIN, H - 30 * mm, "S E R V I C E   A G R E E M E N T")
    canvas.setFont("Helvetica-Bold", 27)
    canvas.setFillColor(WHITE)
    canvas.drawString(MARGIN, H - 42 * mm, "Chic Salon & Clinic")
    canvas.setFont("Helvetica", 11.5)
    canvas.setFillColor(colors.HexColor("#D0C5B4"))
    canvas.drawString(MARGIN, H - 49 * mm,
                      "In partnership with Click AI Agency  ·  Willesden, London")
    footer(canvas, doc)
    canvas.restoreState()


def later_pages(canvas, doc):
    canvas.saveState()
    _page_bg(canvas)
    canvas.setFillColor(CHARCOAL)
    canvas.rect(0, H - 12 * mm, W, 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, H - 12.5 * mm, W, 0.5 * mm, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.setFillColor(WHITE)
    canvas.drawString(MARGIN, H - 8 * mm,
                      "Service Agreement  ·  Chic Salon & Clinic")
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
story.append(Spacer(1, BAND_H - MARGIN + 6 * mm))

meta = Table([[
    meta_card("PREPARED FOR", "Chic Salon &amp; Clinic<br/>Willesden, London"),
    meta_card("DATE", "14 August 2026<br/>&nbsp;"),
    meta_card("CONTRACT REF.", "CLK-CHIC-2026-08<br/>&nbsp;"),
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
     Paragraph("Chic Salon &amp; Clinic (Willesden)", S["td"])],
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
    "This Agreement provides three service lines: a one-off website build "
    "(already delivered and paid), and two monthly services delivered "
    "together as an ongoing package.", S["body"]))
story.append(Spacer(1, 4))

svc_data = [
    [Paragraph("SERVICE LINE", S["th_dark"]),
     Paragraph("WHAT IS DELIVERED", S["th_dark"]),
     Paragraph("FEE", S["th_dark"])],

    [Paragraph("<b>01</b><br/><b>Website build</b><br/>(one-off, paid)",
               S["td_bold"]),
     Paragraph("Custom-designed and built salon website, mobile-responsive, "
               "with service pages, booking touchpoints, contact form, and "
               "brand-aligned visual identity. Delivered and hosted for the "
               "term of this Agreement.", S["td"]),
     Paragraph("£400.00<br/><i>received</i>", S["amount_taupe"])],

    [Paragraph("<b>02</b><br/><b>Social media management</b>",
               S["td_bold"]),
     Paragraph("Instagram and Facebook management for Chic Salon &amp; "
               "Clinic: content planning, creative production (feed posts, "
               "reels, stories), scheduling and posting, community "
               "management, monthly performance summary.", S["td"]),
     Paragraph("£400.00 / month", S["amount"])],

    [Paragraph("<b>03</b><br/><b>AI voice receptionist &amp; Click Desk Pro</b>",
               S["td_bold"]),
     Paragraph("24/7 AI voice agent trained on Chic Salon's services, "
               "opening hours, and booking rules. 500 voice minutes per "
               "month included; unlimited SMS and WhatsApp messages from the "
               "agent. Full access to Click Desk Pro: client management, "
               "appointments, loyalty programme, reviews, payments.",
               S["td"]),
     Paragraph("£290.00 / month", S["amount"])],

    [Paragraph("<b>Standard monthly total</b>", S["td_bold"]),
     Paragraph("", S["td"]),
     Paragraph("<b>£690.00 / month</b>", S["amount_gold"])],
]
svc_table = Table(svc_data,
                  colWidths=[42 * mm, W - 2 * MARGIN - 42 * mm - 30 * mm, 30 * mm])
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

# ---------- 3. COMMERCIAL SUMMARY ----------
story += section("Section 03", "Commercial summary")

cs_data = [
    [Paragraph("ITEM", S["th_dark"]),
     Paragraph("AMOUNT", S["th_dark"])],
    [Paragraph("Website build (one-off)", S["td"]),
     Paragraph("<b>£400.00</b> &nbsp;<i>received</i>", S["amount_taupe"])],
    [Paragraph("Standard monthly total (from month 1)", S["td"]),
     Paragraph("<b>£690.00 / month</b>", S["amount_gold"])],
    [Paragraph("Voice usage over 500 minutes per calendar month", S["td"]),
     Paragraph("£0.30 per minute", S["amount"])],
]
cs_table = Table(cs_data, colWidths=[W - 2 * MARGIN - 60 * mm, 60 * mm])
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
    [Paragraph("<b>Website build</b>", S["td_bold"]),
     Paragraph("£400.00 one-off fee, <b>received</b>. No further action "
               "required on the Client's side for the website build.",
               S["td"])],
    [Paragraph("<b>Go-live (day 0)</b>", S["td_bold"]),
     Paragraph("The Service Provider activates the ongoing monthly package. "
               "The go-live date will be confirmed in writing to the Client "
               "at least 24 hours in advance.", S["td"])],
    [Paragraph("<b>Month 1 onwards</b>", S["td_bold"]),
     Paragraph("<b>£690.00</b> per calendar month for the combined social "
               "media management and voice receptionist services. Invoiced "
               "on the same day of each month from go-live, payable within "
               "7 days of invoice.", S["td"])],
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
     "This Agreement runs from the go-live date on a monthly rolling basis. "
     "Either party may terminate this Agreement by giving 30 days written "
     "notice at any time."),
    ("Cancellation",
     "Termination requires 30 days written notice from either party. "
     "Termination for material breach is available at any time in "
     "accordance with the full Terms and Conditions."),
    ("Website",
     "The website build has been delivered and paid for as a one-off. "
     "During the term of this Agreement, the Service Provider will host "
     "and maintain the website. Ongoing hosting after termination can be "
     "arranged separately or handed over to the Client to self-host."),
    ("Voice minutes",
     "500 voice minutes per calendar month are included in the £290.00 AI "
     "voice receptionist and Click Desk Pro line. Voice usage above 500 "
     "minutes is charged at £0.30 per minute per the payment schedule "
     "above."),
    ("Content approvals",
     "The Client will nominate one point of contact empowered to approve "
     "content. Content is delivered on a rolling schedule and treated as "
     "approved unless the nominated contact objects in writing within 2 "
     "business days of receipt."),
    ("Advertising compliance",
     "All content and voice-agent scripts produced by the Service Provider "
     "will follow the UK Advertising Standards Authority (ASA) rules and "
     "Committee of Advertising Practice (CAP) code, including the specific "
     "restrictions that apply to beauty and aesthetic services. The Client "
     "is responsible for the accuracy of any service claims requested."),
    ("Performance standard",
     "The Service Provider commits to deliver the services described in "
     "this Agreement to a high professional standard, with continuous "
     "content optimisation and monthly performance reporting to the Client. "
     "Content and voice-agent outcomes are influenced by factors including "
     "market conditions, competition, seasonality, service mix, and price "
     "positioning; specific booking or engagement figures are reviewed "
     "with the Client month by month rather than fixed in this Agreement."),
    ("Additional charges",
     "Any expense over £100 outside the scope of this Agreement (for "
     "example, paid third-party tools, influencer fees, printed materials, "
     "additional voice minute allowance) requires the Client's written "
     "approval before the Service Provider proceeds."),
    ("Your data",
     "The Client owns all data held in the Click Desk Pro platform, all "
     "customer records, all voice agent call records, and all social media "
     "accounts. The Service Provider complies with UK GDPR. On termination, "
     "all data will be exported and returned to the Client within 14 days, "
     "and administrator access to any accounts registered under the "
     "Client's name will be handed over."),
    ("Intellectual property",
     "The Client owns all final creative assets delivered under this "
     "Agreement (posts, reels, stories, website content). The Service "
     "Provider retains the right to use anonymised performance metrics and "
     "creative examples in its own portfolio."),
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
    title="Service Agreement - Chic Salon & Clinic",
    author="Click AI Agency",
    subject="Service Agreement - Chic Salon & Clinic Willesden",
)
doc.build(story, onFirstPage=first_page, onLaterPages=later_pages)
print(f"Chic Salon & Clinic agreement generated at: {OUTPUT}")
