from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
)
import os

OUTPUT = "/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI/projects/agency/01-05-26/click-ai-agency-1page-agreement.pdf"
LOGO = "/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI/brand-assets/Click AI Logos/click-logo.png"

BLACK = colors.HexColor("#0D0D0D")
WHITE = colors.HexColor("#FFFFFF")
ACCENT = colors.HexColor("#6C63FF")
GREY = colors.HexColor("#666666")
LIGHT_GREY = colors.HexColor("#F5F5F5")
BORDER = colors.HexColor("#DDDDDD")
GREEN = colors.HexColor("#38A169")

W, H = A4
MARGIN = 18 * mm

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=MARGIN, bottomMargin=MARGIN,
    title="Click AI Agency - Service Agreement (Summary)",
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
check_style = s("Check", fontName="Helvetica", fontSize=9.5, textColor=BLACK, leading=14, spaceAfter=2)

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

# PARTIES (compact)
parties_data = [
    [Paragraph("<b>Client business name:</b>", body), Paragraph("_______________________________________________", body)],
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

# PACKAGE SELECTION
story.append(Paragraph("<b>Select your package</b> (tick one):", h2))

pkg_data = [
    [Paragraph("<b>Package</b>", body_bold), Paragraph("<b>Monthly</b>", body_bold), Paragraph("<b>Setup</b>", body_bold), Paragraph("<b>Minutes</b>", body_bold), Paragraph("<b>Select</b>", body_bold)],
    [Paragraph("Click", body), Paragraph("497/mo", body), Paragraph("290", body), Paragraph("500", body), Paragraph("[    ]", body)],
    [Paragraph("Click+", body), Paragraph("797/mo", body), Paragraph("290", body), Paragraph("1,000", body), Paragraph("[    ]", body)],
    [Paragraph("Click Pro", body), Paragraph("1,297/mo", body), Paragraph("490", body), Paragraph("2,500", body), Paragraph("[    ]", body)],
    [Paragraph("Click Elite", body), Paragraph("1,997/mo", body), Paragraph("790", body), Paragraph("5,000", body), Paragraph("[    ]", body)],
]
pkg_table = Table(pkg_data, colWidths=[32*mm, 30*mm, 25*mm, 28*mm, W - 2*MARGIN - 115*mm])
pkg_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#0D0D0D")),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("ALIGN", (4,1), (4,-1), "CENTER"),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(pkg_table)
story.append(Spacer(1, 1*mm))
story.append(Paragraph("All packages include: AI voice receptionist (24/7), WhatsApp automation, social media management, content creation, and automation workflows. Minutes are combined voice and WhatsApp usage per month.", body_small))
story.append(Spacer(1, 3*mm))

# WHAT'S INCLUDED
story.append(Paragraph("<b>What you get</b>", h2))
included_items = [
    "AI voice receptionist answering calls 24/7, trained on your business",
    "WhatsApp automation: confirmations, reminders, follow-ups",
    "Social media content creation and scheduling",
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
    [Paragraph("On signing", body), Paragraph("Setup fee (50% deposit)", body)],
    [Paragraph("On delivery (go-live)", body), Paragraph("Setup fee (remaining 50%)", body)],
    [Paragraph("Days 1 to 7", body), Paragraph("Free trial. No charge.", body)],
    [Paragraph("Day 8", body), Paragraph("First monthly invoice issued", body)],
    [Paragraph("Day 10", body), Paragraph("Payment due (within 2 days of invoice)", body)],
    [Paragraph("Monthly thereafter", body), Paragraph("Invoice issued, payable within 2 days", body)],
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

# KEY TERMS (compact)
story.append(Paragraph("<b>Key terms</b>", h2))
terms = [
    "<b>Contract:</b> Monthly rolling. No minimum commitment. Cancel with 30 days written notice.",
    "<b>Trial:</b> 7 days from go-live. Cancel during the trial and no monthly fees apply.",
    "<b>Content approval:</b> All content published on your behalf requires your approval within 3 business days.",
    "<b>Additional charges:</b> Any expense over 100 requires your written approval before we proceed.",
    "<b>Your data:</b> You own your data. We comply with UK GDPR. All data returned to you on termination.",
    "<b>Overage:</b> Voice minutes over your plan: 0.20/min. WhatsApp over plan: 0.05/msg.",
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
    [Paragraph("<b>For Click AI Agency Ltd</b>", body_bold), Paragraph("<b>For the Client</b>", body_bold)],
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
print("1-page agreement template generated successfully.")
