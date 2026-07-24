#!/usr/bin/env python3
"""Generate Elan Cafe proposal PDF v3 — EL&N brand palette, transformation-led."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable,
    KeepTogether
)

# --- EL&N palette (from website screenshot) ---
BLUSH      = colors.HexColor("#E5CBC0")   # header band, dusty rose
BLUSH_DARK = colors.HexColor("#D4B4A6")   # deeper blush accent
CREAM      = colors.HexColor("#FAF5F0")   # body background (warm cream)
SOFT_PINK  = colors.HexColor("#F5DDE0")   # subtle card fills
ROSE       = colors.HexColor("#C58A8A")   # section markers, deeper feminine
ROSE_MUTED = colors.HexColor("#B78585")   # secondary rose
CHARCOAL   = colors.HexColor("#2C2C2C")   # primary text
INK        = colors.HexColor("#3A3A3A")
BODY       = colors.HexColor("#454545")
GREY       = colors.HexColor("#8A857F")   # warm grey
HAIR       = colors.HexColor("#E8DED4")   # hairline dividers on cream
WHITE      = colors.white

W, H = A4
OUT = "elan-cafe-proposal.pdf"
BAND_H = 62 * mm
TOP_MARGIN = 16 * mm

S = {
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10.5,
                           textColor=BODY, leading=15, spaceAfter=6),
    "lead": ParagraphStyle("lead", fontName="Helvetica", fontSize=11,
                           textColor=INK, leading=16, spaceAfter=6),
    "emph": ParagraphStyle("emph", fontName="Helvetica-Oblique", fontSize=11,
                           textColor=CHARCOAL, leading=16, spaceAfter=8),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=10.5,
                             textColor=BODY, leading=15, spaceAfter=4,
                             leftIndent=14, bulletIndent=2),
    "num": ParagraphStyle("num", fontName="Helvetica", fontSize=10.5,
                          textColor=BODY, leading=15, spaceAfter=5, leftIndent=18),
    "sec_num": ParagraphStyle("sec_num", fontName="Helvetica-Bold", fontSize=10.5,
                              textColor=WHITE, alignment=TA_CENTER),
    "sec_title": ParagraphStyle("sec_title", fontName="Helvetica-Bold", fontSize=14,
                                textColor=CHARCOAL, leading=17),
    "card_k": ParagraphStyle("card_k", fontName="Helvetica-Bold", fontSize=7.5,
                             textColor=ROSE, spaceAfter=3),
    "card_v": ParagraphStyle("card_v", fontName="Helvetica-Bold", fontSize=10,
                             textColor=CHARCOAL, leading=13),
    "price_h_l": ParagraphStyle("price_h_l", fontName="Helvetica-Bold", fontSize=12,
                                textColor=CHARCOAL, leading=15),
    "price_h_r": ParagraphStyle("price_h_r", fontName="Helvetica-Bold", fontSize=15,
                                textColor=ROSE, leading=17, alignment=TA_RIGHT),
    "price_d": ParagraphStyle("price_d", fontName="Helvetica", fontSize=10,
                              textColor=BODY, leading=15.5),
    "price_note_h": ParagraphStyle("price_note_h", fontName="Helvetica-Bold",
                                   fontSize=9, textColor=CHARCOAL, spaceAfter=4),
    "sig_name": ParagraphStyle("sig_name", fontName="Helvetica-Bold", fontSize=11.5,
                               textColor=CHARCOAL, leading=15),
    "sig_co": ParagraphStyle("sig_co", fontName="Helvetica", fontSize=10,
                             textColor=GREY, leading=14),
    "eyebrow": ParagraphStyle("eyebrow", fontName="Helvetica-Bold", fontSize=8,
                              textColor=ROSE_MUTED, alignment=TA_LEFT),
}


def _page_bg(canvas):
    """Warm cream page background."""
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)


def first_page(canvas, doc):
    canvas.saveState()
    _page_bg(canvas)
    # Blush header band
    canvas.setFillColor(BLUSH)
    canvas.rect(0, H - BAND_H, W, BAND_H, fill=1, stroke=0)
    # Rose accent line under band
    canvas.setFillColor(ROSE)
    canvas.rect(0, H - BAND_H - 0.8 * mm, W, 0.8 * mm, fill=1, stroke=0)
    # Eyebrow: CLICK AI AGENCY (top-left)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.setFillColor(CHARCOAL)
    canvas.drawString(20 * mm, H - 14 * mm, "C L I C K   A I   A G E N C Y")
    # PROPOSAL tag (top-right)
    tag_w, tag_h = 30 * mm, 8 * mm
    canvas.setFillColor(CHARCOAL)
    canvas.roundRect(W - 20 * mm - tag_w, H - 16.5 * mm, tag_w, tag_h, 1 * mm,
                     fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawCentredString(W - 20 * mm - tag_w / 2, H - 14 * mm, "P R O P O S A L")
    # Title
    canvas.setFillColor(CHARCOAL)
    canvas.setFont("Helvetica-Bold", 26)
    canvas.drawString(20 * mm, H - 32 * mm, "A Custom Ordering System")
    canvas.setFont("Helvetica", 15)
    canvas.setFillColor(CHARCOAL)
    canvas.drawString(20 * mm, H - 43 * mm, "for the EL&N Cake Department")
    # Sub-line
    canvas.setFillColor(colors.HexColor("#7A6D63"))
    canvas.setFont("Helvetica-Oblique", 10)
    canvas.drawString(20 * mm, H - 52 * mm,
                      "Designed and built by Click AI Agency")
    footer(canvas, doc)
    canvas.restoreState()


def later_pages(canvas, doc):
    canvas.saveState()
    _page_bg(canvas)
    # Slim blush top band
    canvas.setFillColor(BLUSH)
    canvas.rect(0, H - 13 * mm, W, 13 * mm, fill=1, stroke=0)
    canvas.setFillColor(ROSE)
    canvas.rect(0, H - 13.6 * mm, W, 0.6 * mm, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.setFillColor(CHARCOAL)
    canvas.drawString(20 * mm, H - 8.5 * mm,
                      "A Custom Ordering System for EL&N")
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.setFillColor(CHARCOAL)
    canvas.drawRightString(W - 20 * mm, H - 8.5 * mm, "CLICK AI AGENCY")
    footer(canvas, doc)
    canvas.restoreState()


def footer(canvas, doc):
    canvas.setStrokeColor(ROSE)
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, 16 * mm, W - 20 * mm, 16 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY)
    canvas.drawString(20 * mm, 11 * mm, "Click AI Agency   |   clickaiagency.com")
    canvas.drawRightString(W - 20 * mm, 11 * mm, f"Page {canvas.getPageNumber()}")


def section(num, title):
    t = Table([[Paragraph(str(num), S["sec_num"]), Paragraph(title, S["sec_title"])]],
              colWidths=[9 * mm, 161 * mm], rowHeights=[9 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), ROSE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (1, 0), (1, 0), 7),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 0),
    ]))
    return [Spacer(1, 9), t,
            HRFlowable(width="100%", thickness=0.5, color=HAIR,
                       spaceBefore=3, spaceAfter=7)]


def blush_bullets(items):
    out = []
    for t in items:
        out.append(Paragraph(
            f'<bullet><font color="#C58A8A">&#9679;</font></bullet> {t}', S["bullet"]))
    return out


def card(k, v):
    inner = Table([[Paragraph(k, S["card_k"])], [Paragraph(v, S["card_v"])]],
                  colWidths=[52 * mm])
    inner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), SOFT_PINK),
        ("LINEABOVE", (0, 0), (-1, 0), 1.3, ROSE),
        ("TOPPADDING", (0, 0), (-1, 0), 6),
        ("TOPPADDING", (0, 1), (-1, 1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 0),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return inner


def price_block(title, price, includes_lines=None, note_lines=None, note_header=None):
    """Build a two-part price block: dark header row + light body detail block."""
    head = Table([[Paragraph(title, S["price_h_l"]), Paragraph(price, S["price_h_r"])]],
                 colWidths=[120 * mm, 50 * mm])
    head.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUSH),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("LINEBELOW", (0, 0), (-1, -1), 1.1, ROSE),
    ]))
    body_rows = []
    if includes_lines:
        for d in includes_lines:
            body_rows.append([Paragraph(
                f'<font color="#C58A8A">&#9679;</font>&nbsp;&nbsp;{d}', S["price_d"])])
    if note_header:
        body_rows.append([Paragraph(note_header, S["price_note_h"])])
    if note_lines:
        for d in note_lines:
            body_rows.append([Paragraph(
                f'<font color="#C58A8A">&#9679;</font>&nbsp;&nbsp;{d}', S["price_d"])])
    body_t = Table(body_rows, colWidths=[170 * mm])
    body_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FCF6F0")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("LINEBELOW", (0, -1), (-1, -1), 0.5, HAIR),
    ]))
    return KeepTogether([head, body_t, Spacer(1, 10)])


# --- Build story ---
story = []
story.append(Spacer(1, BAND_H - TOP_MARGIN + 6 * mm))

# Meta cards
meta = Table([[card("PREPARED FOR",
                    "Ali Bidarbakht<br/>Head of Pastry, EL&amp;N London"),
               card("DATE", "24 July 2026<br/>&nbsp;"),
               card("TARGET GO-LIVE", "1 August 2026<br/>&nbsp;")]],
             colWidths=[56 * mm, 56 * mm, 56 * mm])
meta.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
]))
story.append(meta)

# 1. The problem you told us about
story += section(1, "The problem you told us about")
story.append(Paragraph(
    "Today, a customer wanting a bespoke cake fills out a long form on your website, and from "
    "that moment your team is on the clock. Ten to fifteen emails to confirm the design, the "
    "flavours, the message, the collection details, the payment. Multiplied across every order, "
    "every day of the week. Weekends and evenings do not stop; the inbox does not stop.",
    S["lead"]))
story.append(Paragraph(
    "It is careful, personal work, and it is why EL&amp;N's cakes matter. It is also work that "
    "quietly caps how far the department can grow. Every new order is another manual thread. "
    "Doubling orders means doubling admin. Opening another branch means opening another admin "
    "operation from scratch. It does not scale.", S["lead"]))

# 2. The system we designed for you
story += section(2, "The system we designed for you")
story.append(Paragraph(
    "We designed a complete, custom ordering system for the EL&amp;N cake department. Not a "
    "plug-in, not an off-the-shelf tool. A system built specifically for how your customers "
    "order and how your kitchen delivers.", S["body"]))
story.append(Paragraph("It has four parts, working as one:", S["body"]))
story += blush_bullets([
    "<b>Ella</b>, a dedicated AI voice agent that answers your cake ordering line 24 hours a "
    "day, seven days a week, and takes orders end to end.",
    "<b>A bespoke cake designer page</b>, custom-built for EL&amp;N, where customers with a "
    "specific vision build and visualise their cake step by step and see it before they commit.",
    "<b>Stripe payment</b>, integrated into both flows, with funds paid out to EL&amp;N every "
    "two to three days.",
    "<b>Click Pro</b>, your order management dashboard, where every completed order arrives "
    "ready for the kitchen with an image of the cake and the full spec in one place.",
])
story.append(Paragraph(
    "Ella, the designer page, the payment layer and the dashboard were conceived, designed and "
    "built together to solve one problem: turning cake enquiries into paid, kitchen-ready orders "
    "without a single email in between.", S["body"]))

# 3. How it works in practice
story += section(3, "How it works in practice")
story.append(Paragraph("When a customer calls the cake ordering line:", S["body"]))
steps = [
    "Ella answers immediately, every time, <b>24 hours a day, seven days a week</b>. Even when "
    "two or three customers call at the same time, every call is picked up. No busy line, no "
    "waiting, no missed order.",
    "Standard cakes: Ella takes the cake selection from your current range, the customer's name "
    "and contact details, and sends a secure payment link.",
    "Custom cakes: Ella sends the customer a link to EL&amp;N's bespoke cake designer, where "
    "they build their cake step by step and watch the design come to life as they choose.",
    "Payment is taken through Stripe, with funds paid out to EL&amp;N every two to three days. "
    "Card details are handled entirely by Stripe and never touch our systems or yours.",
    "Every completed order lands in Click Pro, ready for the kitchen: an image of the order and "
    "exactly what the customer chose and agreed, all in one place. No paperwork, no notes passed "
    "back and forth.",
]
for i, s_ in enumerate(steps, 1):
    story.append(Paragraph(
        f'<font color="#C58A8A"><b>{i}.</b></font>&nbsp;&nbsp;{s_}', S["num"]))

# 4. What ends when the system goes live
story += section(4, "What ends when the system goes live")
story.append(Paragraph(
    "<i>The 10 to 15 email threads per order end. Multiplied across your daily volume, that is "
    "time returned to the work only your team can do.</i>", S["emph"]))
story += blush_bullets([
    "The complicated form that filters good customers out before they reach you.",
    "The missed enquiries that arrive out of hours or when the phone is busy.",
    "The paperwork moving between the front team and the kitchen.",
    "The evenings and weekends spent replying to order emails.",
    "The scaling ceiling. The same system that handles today's volume comfortably handles 200 "
    "orders a day. It handles the next branch the same way it handles this one.",
])

# 5. Reliability and support
story += section(5, "Reliability and support")
story.append(Paragraph(
    "A system like this is only as good as its worst day. Here is what stands behind it:",
    S["body"]))
story += blush_bullets([
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

# 6. Built once, deployed per branch
story += section(6, "Built once, deployed per branch")
story.append(Paragraph(
    "The London build is the foundation. Because the design and system already exist, every "
    "future EL&amp;N branch can be deployed in a fraction of the time London took.", S["body"]))
story.append(Paragraph(
    "Each branch runs as its own deployment: its own phone line, its own Stripe account and "
    "currency, its own menu and pricing, its own operating hours and time zone, its own "
    "monitoring and included minutes. This keeps every branch fast, accurate, and locally right.",
    S["body"]))
story.append(Paragraph(
    "The Ella platform, the cake designer page design, and the underlying systems remain the "
    "property of Click AI Agency and are licensed to EL&amp;N Cafe per site under the service "
    "agreement.", S["body"]))

# 7. Investment
story += section(7, "Investment")
story.append(price_block(
    "Implementation Investment", "£6,500",
    includes_lines=[
        "System design and ideation, tailored to EL&amp;N's cake ordering operation",
        "Ella voice agent, trained on your product range and brand voice",
        "Bespoke cake designer web page, custom-built with visual preview",
        "Stripe payment integration, with per-branch payout configuration",
        "Click Pro dashboard integration for kitchen order delivery",
        "Full-stack build, testing and go-live",
        "Launch support and staff training",
    ],
    note_header="Payment schedule",
    note_lines=[
        "£3,250 on agreement",
        "£3,250 due 30 days after go-live",
    ],
))
story.append(price_block(
    "Monthly service", "£500 / month",
    includes_lines=[
        "1,000 call minutes included",
        "Billed from go-live",
        "Rate locked for the full 12-month term",
        "Additional minutes: £0.25 per minute beyond the included 1,000",
        "Automatic usage reminder when you reach 85% of your monthly allowance",
    ],
))
story.append(Paragraph(
    "Usage is always transparent: you are reminded before you get near the limit, and nothing "
    "changes on your invoice without you seeing it coming.", S["body"]))

# 8. Partnership terms — kept together but standalone (not bound to tail,
# because the roadmap section is significant and should flow naturally)
partnership = []
partnership += section(8, "Partnership terms")
for b in blush_bullets([
    "12-month partnership agreement, service rate locked for the term.",
    "Quarterly service reviews, with the first review including the multi-branch conversation.",
    "Expansion commitment: any additional EL&amp;N branch signed within 12 months of this "
    "agreement receives the London build rate, with service billed per branch.",
]):
    partnership.append(b)
story.append(KeepTogether(partnership))

# 9. What could come next
story += section(9, "What could come next")
story.append(Paragraph(
    "The system we are building is a foundation, not a finished thing. Once London is live and "
    "the operation is proven, there are natural next chapters. None of these are part of the "
    "initial scope or fee. They are what the platform makes possible when EL&amp;N is ready.",
    S["body"]))
story += blush_bullets([
    "<b>A dedicated EL&amp;N ordering app for iOS and Android.</b> The same designer, the same "
    "checkout, the same Click Pro delivery to the kitchen, in a branded app your customers keep "
    "on their phone. One system, more surfaces.",
    "<b>A WhatsApp ordering channel.</b> For the many customers who already message brands "
    "before they call or click, the same system available inside WhatsApp. Order, pay and "
    "confirm without leaving the conversation. Every message-led order lands in Click Pro the "
    "same way a call or web order does.",
    "<b>Customer accounts and a loyalty programme.</b> Once customers create an account, "
    "everything opens up: saved designs, one-tap reorder, gift cards, discount codes, referral "
    "rewards, occasion reminders. The system already collects the data. Loyalty is what happens "
    "when you put it to work.",
    "<b>Proactive outreach for birthdays and repeat occasions.</b> With customer accounts and "
    "dates on file, an outbound agent can call a week before a birthday, an anniversary, or a "
    "saved occasion and offer to place the order right there on the phone. The same voice, the "
    "same experience, the same fulfilment path. No human intervention.",
    "<b>Delivery, integrated at checkout.</b> A partner integration with Uber Direct or Stuart, "
    "so customers can choose delivery at the moment they pay. The order still lands in Click "
    "Pro; the courier is dispatched automatically when the cake is ready. End-to-end, no phone "
    "calls.",
    "<b>Corporate and event accounts.</b> A separate account type for hotels, offices, event "
    "planners and repeat commercial buyers. Bulk ordering, saved billing details, delivery to "
    "multiple addresses, monthly invoicing. Opens a new revenue stream that does not compete "
    "with retail.",
    "<b>A marketing insights dashboard.</b> A dedicated view for the marketing team: "
    "bestselling designs, seasonal patterns, VIP customers, most-requested flavours, "
    "order-value trends by branch. The data the system already collects, turned into decisions "
    "the marketing team can act on.",
])
story.append(Paragraph(
    "We are happy to price and scope any of these separately when the time comes.", S["body"]))

# 10. Next step — bound with signature so they never split
tail = []
tail += section(10, "Next step")
tail.append(Paragraph(
    "Confirm by reply and we will issue the agreement and begin go-live preparation for "
    "<b>1 August 2026</b>.", S["lead"]))
tail.append(Spacer(1, 12))
tail.append(HRFlowable(width=50 * mm, thickness=1, color=ROSE,
                       spaceBefore=2, spaceAfter=8, hAlign="LEFT"))
tail.append(Paragraph("Hadi Yazdani", S["sig_name"]))
tail.append(Paragraph("CEO and Founder, Click AI Agency", S["sig_co"]))
tail.append(Paragraph("clickaiagency.com", S["sig_co"]))
tail.append(Spacer(1, 14))
tail.append(Paragraph(
    '<font color="#8A857F">2026</font>',
    ParagraphStyle("year", fontName="Helvetica-Bold", fontSize=8.5,
                   textColor=GREY, leading=10, spaceAfter=0, alignment=TA_LEFT)))
story.append(KeepTogether(tail))

doc = SimpleDocTemplate(OUT, pagesize=A4,
                        leftMargin=20 * mm, rightMargin=20 * mm,
                        topMargin=TOP_MARGIN, bottomMargin=22 * mm,
                        title="A Custom Ordering System for the EL&N Cake Department",
                        author="Click AI Agency",
                        subject="Proposal - EL&N London")
doc.build(story, onFirstPage=first_page, onLaterPages=later_pages)
print(f"Written: {OUT}")
