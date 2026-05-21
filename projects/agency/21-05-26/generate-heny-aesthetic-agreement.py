from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
)
import os

OUTPUT = "/Users/hadi/Developer/Jodie-AI/projects/agency/21-05-26/heny-aesthetic-clinic-agreement.pdf"
LOGO_PATHS = [
    "/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI/brand-assets/Click AI Logos/click-logo.png",
    "/Users/hadi/Developer/Jodie-AI/brand-assets/Click AI Logos/click-logo.png",
]
LOGO = next((p for p in LOGO_PATHS if os.path.exists(p)), None)

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
    title="Click AI Agency - Service Agreement - Heny Aesthetic Clinic",
    author="Click AI Agency"
)

def s(name, **kw):
    return ParagraphStyle(name, **kw)

title_style = s("Title", fontName="Helvetica-Bold", fontSize=18, textColor=BLACK, leading=24, spaceAfter=2)
subtitle_style = s("Subtitle", fontName="Helvetica", fontSize=10, textColor=GREY, leading=14, spaceAfter=12)
h2 = s("H2", fontName="Helvetica-Bold", fontSize=11, textColor=BLACK, leading=16, spaceBefore=10, spaceAfter=4)
body = s("Body", fontName="Helvetica", fontSize=9.5, textColor=BLACK, leading=14, spaceAfter=4)
body_bold = s("BodyBold", fontName="Helvetica-Bold", fontSize=9.5, textColor=BLACK, leading=14, spaceAfter=4)
body_bold_white = s("BodyBoldWhite", fontName="Helvetica-Bold", fontSize=9.5, textColor=WHITE, leading=14, spaceAfter=4)
body_small = s("BodySmall", fontName="Helvetica", fontSize=8.5, textColor=GREY, leading=12, spaceAfter=3)
note_style = s("Note", fontName="Helvetica-Oblique", fontSize=8.5, textColor=ACCENT, leading=12, spaceAfter=3)

def rule():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=6, spaceBefore=6)

story = []

if LOGO:
    logo = Image(LOGO, width=30*mm, height=30*mm)
    logo.hAlign = 'LEFT'
    story.append(logo)
    story.append(Spacer(1, 2*mm))

story.append(Paragraph("SERVICE AGREEMENT", title_style))
story.append(Paragraph("Click AI Agency Ltd | clickaiagency.com | hello@clickaiagency.com", subtitle_style))
story.append(rule())

# PARTIES
parties_data = [
    [Paragraph("<b>Client business name:</b>", body), Paragraph("Heny Aesthetic Clinic", body)],
    [Paragraph("<b>Legal entity name (if different):</b>", body), Paragraph("_______________________________________________", body)],
    [Paragraph("<b>Contact name:</b>", body), Paragraph("Heny _______________________________________", body)],
    [Paragraph("<b>Email:</b>", body), Paragraph("_______________________________________________", body)],
    [Paragraph("<b>Phone:</b>", body), Paragraph("_______________________________________________", body)],
    [Paragraph("<b>Clinic address:</b>", body), Paragraph("_______________________________________________", body)],
]
pt = Table(parties_data, colWidths=[55*mm, W - 2*MARGIN - 55*mm])
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
    [Paragraph("<b>Package</b>", body_bold_white), Paragraph("<b>Monthly fee (months 1-3)</b>", body_bold_white), Paragraph("<b>Monthly fee (month 4 onwards)</b>", body_bold_white), Paragraph("<b>Setup fee</b>", body_bold_white)],
    [Paragraph("Click Voice<br/>(Aesthetics Launch Tier)", body), Paragraph("£190.00 / month", body), Paragraph("£290.00 / month", body), Paragraph("£100.00 (one-off)", body)],
]
pkg_table = Table(pkg_data, colWidths=[40*mm, 38*mm, 40*mm, W - 2*MARGIN - 118*mm])
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
story.append(Spacer(1, 2*mm))
story.append(Paragraph("Launch offer pricing. The £190/month rate applies for the Client's first three months of service. From month four onwards, the standard rate of £290/month applies. This launch offer is available to UK aesthetic clinics signing this Agreement on or before 31 July 2026.", body_small))
story.append(Spacer(1, 3*mm))

# WHAT'S INCLUDED
story.append(Paragraph("<b>What is included</b>", h2))
included_items = [
    "AI voice receptionist available 24 hours a day, 7 days a week, trained on the Client's treatments, opening hours, and booking rules",
    "Treatments knowledge base loaded into the voice agent (the agent answers caller questions about treatments offered, indicative pricing, durations, aftercare, and books appropriate consultations or sessions)",
    "Click Desk AI dashboard access (call logs, bookings made, recovered bookings, monthly performance summary)",
    "Up to 500 voice minutes per month included in the monthly fee",
    "Calendar booking integration for a single practitioner (the Client herself)",
    "Voice agent name and persona configured to the Client's preference",
    "Monthly performance summary delivered on day 1 of the following month",
]
for item in included_items:
    story.append(Paragraph("  +  " + item, body))
story.append(Spacer(1, 3*mm))

# WHAT IS NOT INCLUDED
story.append(Paragraph("<b>What is not included in this tier</b>", h2))
excluded_items = [
    "Multi-practitioner support (treatment-to-practitioner mapping is available in a higher tier from month 2 or 3 onwards by mutual agreement)",
    "WhatsApp automation (booking confirmations, reminders, follow-ups via WhatsApp)",
    "Social media management or content creation",
    "Google Business Profile setup or optimisation",
    "SEO services",
    "Website design or maintenance",
    "Payment processing or transactional payment confirmations",
]
for item in excluded_items:
    story.append(Paragraph("  -  " + item, body))
story.append(Spacer(1, 1*mm))
story.append(Paragraph("Any services not listed under \"What is included\" are out of scope and are not delivered under this Agreement. The Client may upgrade to a higher tier at any time, subject to a separate agreement and pricing.", body_small))
story.append(Spacer(1, 3*mm))

# PAYMENT SCHEDULE
story.append(Paragraph("<b>Payment schedule</b>", h2))
payment_data = [
    [Paragraph("<b>When</b>", body_bold_white), Paragraph("<b>What</b>", body_bold_white)],
    [Paragraph("On signature", body), Paragraph("Setup fee of £100.00 payable within 3 business days of signing this Agreement. Setup work begins on receipt of the setup fee.", body)],
    [Paragraph("Go-live (day 0)", body), Paragraph("System activated by the Service Provider. The Service Provider will confirm the go-live date in writing at least 24 hours in advance.", body)],
    [Paragraph("Day 1 to Day 30", body), Paragraph("First month of service. £190.00 monthly fee invoiced on go-live date, payable within 7 days of invoice.", body)],
    [Paragraph("Months 2 and 3", body), Paragraph("£190.00 per month, invoiced on the same day of each month, payable within 7 days of invoice.", body)],
    [Paragraph("Month 4 onwards", body), Paragraph("£290.00 per month (standard rate), invoiced on the same day of each month, payable within 7 days of invoice.", body)],
]
pay_table = Table(payment_data, colWidths=[40*mm, W - 2*MARGIN - 40*mm])
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
    "<b>Contract:</b> Monthly rolling from the go-live date. No minimum commitment. Either party may cancel with 30 days written notice.",
    "<b>Setup fee:</b> Non-refundable once setup work has begun. Setup work includes configuring the voice agent, loading the treatments knowledge base, setting up calendar integration, and testing the system before go-live.",
    "<b>Launch offer rate:</b> The £190/month rate is a launch offer available to UK aesthetic clinics signing on or before 31 July 2026. The £190 rate applies to the Client's first three months of service. From month four onwards, the standard rate of £290/month applies automatically without further notice.",
    "<b>No trial period:</b> This Agreement does not include a free trial. Monthly billing begins from the go-live date as set out in the payment schedule.",
    "<b>No performance guarantee:</b> This tier does not include the booking recovery performance guarantee offered to restaurants. The Service Provider commits to deliver the services described in \"What is included\" and to address any service issues promptly.",
    "<b>Voice minutes:</b> Up to 500 voice minutes per month are included. Voice usage over 500 minutes per month is charged at £0.20 per minute, billed monthly in arrears.",
    "<b>Upgrade path:</b> The Client may upgrade to a higher tier at any time (for example, to gain multi-practitioner support, WhatsApp automation, or social media management). The Service Provider will share a separate agreement and pricing for any upgrade.",
    "<b>Additional charges:</b> Any expense over £100 outside the scope of this Agreement requires the Client's written approval before the Service Provider proceeds.",
    "<b>Your data:</b> The Client owns all data held in the Click Desk AI dashboard and the voice agent's call records. The Service Provider complies with UK GDPR. On termination, all data will be exported and returned to the Client within 14 days.",
    "<b>Service availability:</b> The Service Provider commits to a target uptime of 99% per calendar month, excluding scheduled maintenance windows notified in advance.",
    "<b>Confidentiality:</b> The Service Provider will not disclose customer data, financial information, pricing arrangements, or any information designated by the Client as confidential.",
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
    [Paragraph("<b>For Click AI Agency Ltd</b>", body_bold), Paragraph("<b>For the Client: Heny Aesthetic Clinic</b>", body_bold)],
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

doc.build(story)
print(f"Heny Aesthetic Clinic agreement generated at: {OUTPUT}")
