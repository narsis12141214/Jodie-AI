#!/usr/bin/env python3
"""Generate Elan Cafe proposal PDF v2 — Click AI Agency. Professional layout."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable,
    KeepTogether
)

W, H = A4
CHARCOAL = colors.HexColor("#1C1C1C")
INK = colors.HexColor("#2B2B2B")
BODY = colors.HexColor("#3A3A3A")
GOLD = colors.HexColor("#B08D3E")
GOLD_SOFT = colors.HexColor("#C9A961")
LIGHT = colors.HexColor("#F6F2EA")
PALE = colors.HexColor("#FAF8F3")
GREY = colors.HexColor("#8A8A8A")
HAIR = colors.HexColor("#E3DED2")
WHITE = colors.white

OUT = "elan-cafe-proposal.pdf"
BAND_H = 58 * mm
TOP_MARGIN = 16 * mm

S = {
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10.5,
                           textColor=BODY, leading=16, spaceAfter=8),
    "lead": ParagraphStyle("lead", fontName="Helvetica", fontSize=11,
                           textColor=INK, leading=17, spaceAfter=8),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=10.5,
                             textColor=BODY, leading=16, spaceAfter=6,
                             leftIndent=14, bulletIndent=2),
    "num": ParagraphStyle("num", fontName="Helvetica", fontSize=10.5,
                          textColor=BODY, leading=16, spaceAfter=6, leftIndent=18),
    "sec_num": ParagraphStyle("sec_num", fontName="Helvetica-Bold", fontSize=11,
                              textColor=WHITE, alignment=1),
    "sec_title": ParagraphStyle("sec_title", fontName="Helvetica-Bold", fontSize=14,
                                textColor=CHARCOAL, leading=16),
    "card_k": ParagraphStyle("card_k", fontName="Helvetica-Bold", fontSize=7.5,
                             textColor=GOLD, spaceAfter=3),
    "card_v": ParagraphStyle("card_v", fontName="Helvetica-Bold", fontSize=10,
                             textColor=CHARCOAL, leading=13),
    "price_h_l": ParagraphStyle("price_h_l", fontName="Helvetica-Bold", fontSize=12,
                                textColor=WHITE, leading=15),
    "price_h_r": ParagraphStyle("price_h_r", fontName="Helvetica-Bold", fontSize=14,
                                textColor=GOLD_SOFT, leading=16, alignment=TA_RIGHT),
    "price_d": ParagraphStyle("price_d", fontName="Helvetica", fontSize=10,
                              textColor=BODY, leading=15),
    "sig_name": ParagraphStyle("sig_name", fontName="Helvetica-Bold", fontSize=11.5,
                               textColor=CHARCOAL, leading=15),
    "sig_co": ParagraphStyle("sig_co", fontName="Helvetica", fontSize=10,
                             textColor=GREY, leading=14),
}


def spaced(text):
    return "&nbsp;".join(list(text.replace(" ", "  ")))


def first_page(canvas, doc):
    canvas.saveState()
    # Header band
    canvas.setFillColor(CHARCOAL)
    canvas.rect(0, H - BAND_H, W, BAND_H, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, H - BAND_H - 1.2 * mm, W, 1.2 * mm, fill=1, stroke=0)
    # Eyebrow
    canvas.setFont("Helvetica-Bold", 9)
    canvas.setFillColor(GOLD_SOFT)
    canvas.drawString(20 * mm, H - 16 * mm, "C L I C K   A I   A G E N C Y")
    # PROPOSAL tag
    tag_w, tag_h = 30 * mm, 8 * mm
    canvas.setFillColor(GOLD)
    canvas.roundRect(W - 20 * mm - tag_w, H - 18 * mm, tag_w, tag_h, 1.5 * mm,
                     fill=1, stroke=0)
    canvas.setFillColor(CHARCOAL)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.drawCentredString(W - 20 * mm - tag_w / 2, H - 15.5 * mm, "P R O P O S A L")
    # Title
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 36)
    canvas.drawString(20 * mm, H - 32 * mm, "Ella")
    canvas.setFillColor(colors.HexColor("#CFCabc") if False else colors.HexColor("#D8D2C2"))
    canvas.setFont("Helvetica", 13)
    canvas.drawString(20 * mm, H - 41 * mm, "AI Cake Ordering for Elan Cafe London")
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 9)
    canvas.drawString(20 * mm, H - 50 * mm,
                      "A done-for-you ordering system from Click AI Agency")
    footer(canvas, doc)
    canvas.restoreState()


def later_pages(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CHARCOAL)
    canvas.rect(0, H - 12 * mm, W, 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, H - 12.8 * mm, W, 0.8 * mm, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.setFillColor(WHITE)
    canvas.drawString(20 * mm, H - 8 * mm, "Ella")
    canvas.setFont("Helvetica", 8.5)
    canvas.setFillColor(colors.HexColor("#BBB5A6"))
    canvas.drawString(29 * mm, H - 8 * mm, "|   Proposal for Elan Cafe London")
    canvas.setFillColor(GOLD_SOFT)
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.drawRightString(W - 20 * mm, H - 8 * mm, "CLICK AI AGENCY")
    footer(canvas, doc)
    canvas.restoreState()


def footer(canvas, doc):
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.6)
    canvas.line(20 * mm, 16 * mm, W - 20 * mm, 16 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY)
    canvas.drawString(20 * mm, 11 * mm, "Click AI Agency   |   clickaiagency.com")
    canvas.drawRightString(W - 20 * mm, 11 * mm, f"Page {canvas.getPageNumber()}")


def section(num, title):
    t = Table([[Paragraph(str(num), S["sec_num"]), Paragraph(title, S["sec_title"])]],
              colWidths=[9 * mm, 161 * mm], rowHeights=[9 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), GOLD),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (1, 0), (1, 0), 6),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 0),
    ]))
    return [Spacer(1, 12), t,
            HRFlowable(width="100%", thickness=0.6, color=HAIR,
                       spaceBefore=4, spaceAfter=9)]


def gbullets(items):
    out = []
    for t in items:
        out.append(Paragraph(
            f'<bullet><font color="#B08D3E">&#9632;</font></bullet> {t}', S["bullet"]))
    return out


story = []
story.append(Spacer(1, BAND_H - TOP_MARGIN + 6 * mm))

# Meta cards
def card(k, v):
    inner = Table([[Paragraph(k, S["card_k"])], [Paragraph(v, S["card_v"])]],
                  colWidths=[52 * mm])
    inner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
        ("LINEABOVE", (0, 0), (-1, 0), 1.4, GOLD),
        ("TOPPADDING", (0, 0), (-1, 0), 6),
        ("TOPPADDING", (0, 1), (-1, 1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 0),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return inner

meta = Table([[card("PREPARED FOR", "Ali Bidarbakht<br/>Head of Pastry, Elan Cafe"),
               card("DATE", "23 July 2026<br/>&nbsp;"),
               card("TARGET GO-LIVE", "1 August 2026<br/>&nbsp;")]],
             colWidths=[56 * mm, 56 * mm, 56 * mm])
meta.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
]))
story.append(meta)

# 1
story += section(1, "What this is")
story.append(Paragraph(
    "A complete, done-for-you ordering system for Elan's cake department. Ella, your dedicated "
    "AI voice agent, answers the cake ordering line, takes orders, and turns phone enquiries into "
    "paid orders without a single missed call. You have already seen the bespoke cake designer in "
    "action. This proposal covers what it costs, how we support it, and how it grows with you.",
    S["lead"]))

# 2
story += section(2, "How Ella works")
story.append(Paragraph("When a customer calls the cake ordering line:", S["body"]))
steps = [
    "Ella answers immediately, every time, <b>24 hours a day, seven days a week</b>. Even when "
    "two or three customers call at the same time, every call is picked up. No busy line, no "
    "waiting, no missed order.",
    "Standard cakes: Ella takes the cake selection from your current range, the customer's name "
    "and contact details, and sends a secure payment link.",
    "Custom cakes: Ella sends the customer a link to Elan's bespoke cake designer, where they "
    "build their cake step by step and watch the design come to life as they choose.",
    "Payment is taken through Stripe, with funds paid out to Elan every two to three days. Card "
    "details are handled entirely by Stripe and never touch our systems or yours.",
    "Every completed order lands in Click Pro, your order management dashboard, ready for the "
    "kitchen: an image of the order and exactly what the customer chose and agreed, all in one "
    "place. No paperwork, no notes passed back and forth.",
]
for i, s_ in enumerate(steps, 1):
    story.append(Paragraph(
        f'<font color="#B08D3E"><b>{i}.</b></font>&nbsp;&nbsp;{s_}', S["num"]))

# 3
story += section(3, "Reliability and support")
story.append(Paragraph(
    "A system like this is only as good as its worst day. Here is what stands behind Ella:",
    S["body"]))
story += gbullets([
    "<b>Continuous monitoring.</b> We watch the system so you never have to. If anything needs "
    "attention, we know before your customers do.",
    "<b>Monthly service report.</b> Every month you receive a thorough report: calls answered, "
    "orders processed, revenue taken through Stripe. You will always know exactly what the "
    "system is doing for you.",
    "<b>Menu and product updates.</b> Up to 10 updates each month are included, live within 48 "
    "hours of your request. New cakes, price changes, seasonal ranges.",
    "<b>A dedicated account manager at Click.</b> One person who knows your account, with a "
    "response the same business day. No ticket queues, no call centres.",
    "<b>Quarterly service reviews.</b> Every quarter we sit down together, review the numbers, "
    "and plan what comes next.",
    "<b>Trusted infrastructure.</b> Payments run on Stripe. Voice and hosting run on "
    "enterprise-grade infrastructure built for continuous availability.",
])

# 4
story += section(4, "Built once, deployed per branch")
story.append(Paragraph(
    "The London build is the foundation. Because the design and system already exist, every "
    "future Elan branch can be deployed in a fraction of the time London took.", S["body"]))
story.append(Paragraph(
    "Each branch runs as its own deployment: its own phone line, its own Stripe account and "
    "currency, its own menu and pricing, its own operating hours and time zone, its own "
    "monitoring and included minutes. This keeps every branch fast, accurate, and locally right.",
    S["body"]))
story.append(Paragraph(
    "The Ella platform, the cake designer page design, and the underlying systems remain the "
    "property of Click AI Agency and are licensed to Elan Cafe per site under the service "
    "agreement.", S["body"]))

# 5
def price_block(title, price, details):
    head = Table([[Paragraph(title, S["price_h_l"]), Paragraph(price, S["price_h_r"])]],
                 colWidths=[120 * mm, 50 * mm])
    head.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CHARCOAL),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("LINEBELOW", (0, 0), (-1, -1), 1.2, GOLD),
    ]))
    rows = [[Paragraph(
        f'<font color="#B08D3E">&#9632;</font>&nbsp;&nbsp;{d}', S["price_d"])]
        for d in details]
    body_t = Table(rows, colWidths=[170 * mm])
    body_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("LINEBELOW", (0, -1), (-1, -1), 0.6, HAIR),
    ]))
    return KeepTogether([head, body_t, Spacer(1, 8)])

story += section(5, "Investment")
story.append(price_block(
    "Implementation  (London branch)", "£5,000",
    ["£2,500 on agreement",
     "£2,500 due 30 days after go-live"]))
story.append(price_block(
    "Monthly service", "£500 / month",
    ["1,000 call minutes included",
     "Billed from go-live",
     "Rate locked for the full 12-month term",
     "Additional minutes: £0.25 per minute beyond the included 1,000",
     "Automatic usage reminder when you reach 85% of your monthly allowance"]))
story.append(Paragraph(
    "Usage is always transparent: you are reminded before you get near the limit, and nothing "
    "changes on your invoice without you seeing it coming.", S["body"]))

# 6
story += section(6, "Partnership terms")
story += gbullets([
    "12-month partnership agreement, service rate locked for the term.",
    "Quarterly service reviews, with the first review including the multi-branch conversation.",
    "Expansion commitment: any additional Elan branch signed within 12 months of this agreement "
    "receives the London implementation rate, with service billed per branch.",
])

# 7
story += section(7, "Next step")
story.append(Paragraph(
    "Confirm by reply and we will issue the agreement and begin go-live preparation for "
    "<b>1 August 2026</b>.", S["lead"]))
story.append(Spacer(1, 10))
story.append(HRFlowable(width=50 * mm, thickness=1, color=GOLD,
                        spaceBefore=2, spaceAfter=8, hAlign="LEFT"))
story.append(Paragraph("Hadi Yazdani", S["sig_name"]))
story.append(Paragraph("Click AI Agency&nbsp;&nbsp;|&nbsp;&nbsp;clickaiagency.com", S["sig_co"]))

doc = SimpleDocTemplate(OUT, pagesize=A4,
                        leftMargin=20 * mm, rightMargin=20 * mm,
                        topMargin=TOP_MARGIN, bottomMargin=22 * mm,
                        title="Ella - AI Cake Ordering for Elan Cafe London",
                        author="Click AI Agency",
                        subject="Proposal - Elan Cafe London")
doc.build(story, onFirstPage=first_page, onLaterPages=later_pages)
print(f"Written: {OUT}")
