from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
)
import os

OUTPUT = "/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI/projects/agency/09-05-26/kish-restaurant-agreement.pdf"
LOGO = "/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI/brand-assets/Click AI Logos/click-logo.png"

BLACK = colors.HexColor("#0D0D0D")
WHITE = colors.HexColor("#FFFFFF")
ACCENT = colors.HexColor("#6C63FF")
GREY = colors.HexColor("#666666")
LIGHT_GREY = colors.HexColor("#F5F5F5")
BORDER = colors.HexColor("#DDDDDD")

W, H = A4
MARGIN = 18 * mm

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=MARGIN, bottomMargin=MARGIN,
    title="Click AI Agency - Service Agreement - Kish Restaurant",
    author="Click AI Agency"
)

def s(name, **kw):
    return ParagraphStyle(name, **kw)

title_style = s("Title", fontName="Helvetica-Bold", fontSize=18, textColor=BLACK, leading=24, spaceAfter=2)
subtitle_style = s("Subtitle", fontName="Helvetica", fontSize=10, textColor=GREY, leading=14, spaceAfter=12)
h2 = s("H2", fontName="Helvetica-Bold", fontSize=11, textColor=BLACK, leading=16, spaceBefore=10, spaceAfter=4)
body = s("Body", fontName="Helvetica", fontSize=9.5, textColor=BLACK, leading=14, spaceAfter=4)
body_bold = s("BodyBold", fontName="Helvetica-Bold", fontSize=9.5, textColor=BLACK, leading=14, spaceAfter=4)
body_small = s("BodySmall", fontName="Helvetica", fontSize=8.5, textColor=GREY, leading=12, spaceAfter=3)

def rule():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=6, spaceBefore=6)

story = []

# LOGO
if os.path.exists(LOGO):
    logo = Image(LOGO, width=30*mm, height=30*mm)
    logo.hAlign = 'LEFT'
    story.append(logo)
    story.append(Spacer(1, 2*mm))

# HEADER
story.append(Paragraph("SERVICE AGREEMENT", title_style))
story.append(Paragraph("Click AI Agency Ltd | clickaiagency.com | hello@clickaiagency.com", subtitle_style))
story.append(rule())

# PARTIES
parties_data = [
    [Paragraph("<b>Client business name:</b>", body), Paragraph("Kish Restaurant", body)],
    [Paragraph("<b>Contact name:</b>", body), Paragraph("_______________________________________________", body)],
    [Paragraph("<b>Email:</b>", body), Paragraph("_______________________________________________", body)],
    [Paragraph("<b>Phone:</b>", body), Paragraph("_______________________________________________", body)],
]
pt = Table(parties_data, colWidths=[45*mm, W - 2*MARGIN - 45*mm])
pt.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING", (0,0), (-1,-1), 3),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3),
]))
story.append(pt)
story.append(Spacer(1, 3*mm))

# SELECTED PACKAGE
story.append(Paragraph("<b>Selected package</b>", h2))

pkg_data = [
    [Paragraph("<b>Package</b>", body_bold), Paragraph("<b>Monthly fee</b>", body_bold), Paragraph("<b>Setup fee</b>", body_bold), Paragraph("<b>Included minutes</b>", body_bold)],
    [Paragraph("Click+", body), Paragraph("797.00/month", body), Paragraph("Waived (case study)", body), Paragraph("1,400 (1,000 standard + 400 bonus)", body)],
]
pkg_table = Table(pkg_data, colWidths=[30*mm, 35*mm, 40*mm, W - 2*MARGIN - 105*mm])
pkg_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#0D0D0D")),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE]),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(pkg_table)
story.append(Spacer(1, 1*mm))
story.append(Paragraph("The Click+ package includes: AI voice receptionist (24/7), WhatsApp automation, social media management, content creation, and automation workflows. An additional 400 bonus minutes per month have been added as a special arrangement for Kish Restaurant, bringing the total included minutes to 1,400 per month.", body_small))
story.append(Spacer(1, 3*mm))

# WHAT'S INCLUDED
story.append(Paragraph("<b>What you get</b>", h2))
included_items = [
    "AI voice receptionist answering calls 24/7, trained on your menu, hours, and booking rules",
    "WhatsApp automation: booking confirmations, reminders, follow-ups",
    "1,400 included minutes per month (voice + WhatsApp combined)",
    "Social media content: 12 posts per month including 2 reels",
    "Google review management and automated review requests",
    "Monthly performance reporting",
    "7-day free trial before billing starts",
]
for item in included_items:
    story.append(Paragraph("  +  " + item, body))
story.append(Spacer(1, 3*mm))

# PAYMENT SCHEDULE
story.append(Paragraph("<b>Payment schedule</b>", h2))
payment_data = [
    [Paragraph("<b>When</b>", body_bold), Paragraph("<b>What</b>", body_bold)],
    [Paragraph("Setup fee", body), Paragraph("Waived (case study exchange)", body)],
    [Paragraph("Days 1 to 7", body), Paragraph("Free trial. No charge.", body)],
    [Paragraph("Day 8", body), Paragraph("First monthly invoice issued (797.00)", body)],
    [Paragraph("Day 10", body), Paragraph("Payment due (within 2 days of invoice)", body)],
    [Paragraph("Monthly thereafter", body), Paragraph("797.00 per month, payable within 2 days of invoice", body)],
]
pay_table = Table(payment_data, colWidths=[45*mm, W - 2*MARGIN - 45*mm])
pay_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#0D0D0D")),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(pay_table)
story.append(Spacer(1, 3*mm))

# KEY TERMS
story.append(Paragraph("<b>Key terms</b>", h2))
terms = [
    "<b>Contract:</b> Monthly rolling. No minimum commitment. Cancel with 30 days written notice.",
    "<b>Trial:</b> 7 days from go-live. Cancel during the trial and no monthly fees apply.",
    "<b>Price guarantee:</b> The monthly fee of 797.00 will not increase for the first 24 months. After 24 months, any price adjustment will be limited to a maximum of 3.5% per year, with 30 days written notice.",
    "<b>Setup fee:</b> Waived in exchange for the Client's agreement to be featured as a case study on the Service Provider's website and marketing materials. No sensitive business information will be published without the Client's written approval.",
    "<b>Social media content:</b> 12 posts per month including 2 reels. All content requires Client approval within 3 business days before publishing.",
    "<b>Additional charges:</b> Any expense over 100 requires your written approval before we proceed.",
    "<b>Your data:</b> You own your data. We comply with UK GDPR. All data returned to you on termination.",
    "<b>Overage:</b> Voice minutes over 1,400/month: 0.20/min. WhatsApp messages over plan: 0.05/msg.",
]
for term in terms:
    story.append(Paragraph(term, body))
story.append(Spacer(1, 3*mm))

# FULL TERMS REFERENCE
story.append(Paragraph("This summary is governed by the full Terms and Conditions available at clickaiagency.com/terms. By signing below, the Client agrees to both this summary and the full Terms and Conditions.", body_small))
story.append(Spacer(1, 4*mm))

# SIGNATURES
story.append(rule())

sig_data = [
    [Paragraph("<b>For Click AI Agency Ltd</b>", body_bold), Paragraph("<b>For the Client: Kish Restaurant</b>", body_bold)],
    [Paragraph("Name: Hadi Yazdani", body), Paragraph("Name: _________________________", body)],
    [Paragraph("Title: Director", body), Paragraph("Title: _________________________", body)],
    [Paragraph("Signature: _________________", body), Paragraph("Signature: _________________", body)],
    [Paragraph("Date: _____________________", body), Paragraph("Date: _______________________", body)],
]
sig_table = Table(sig_data, colWidths=[(W - 2*MARGIN) / 2, (W - 2*MARGIN) / 2])
sig_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LINEBELOW", (0,0), (-1,0), 0.5, BORDER),
]))
story.append(sig_table)

story.append(Spacer(1, 4*mm))
story.append(Paragraph("Click AI Agency Ltd | Companies House registered | hello@clickaiagency.com | clickaiagency.com", body_small))

# BUILD
doc.build(story)
print("Kish Restaurant agreement generated successfully.")
