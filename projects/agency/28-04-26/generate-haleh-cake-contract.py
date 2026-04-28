from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak, Image
)
import os

OUTPUT = "/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI/projects/agency/28-04-26/haleh-cake-service-agreement.pdf"
LOGO = "/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI/brand-assets/Click AI Logos/click-logo.png"

BLACK = colors.HexColor("#0D0D0D")
WHITE = colors.HexColor("#FFFFFF")
ACCENT = colors.HexColor("#6C63FF")
GREY = colors.HexColor("#666666")
LIGHT_GREY = colors.HexColor("#F5F5F5")
BORDER = colors.HexColor("#DDDDDD")

W, H = A4
MARGIN = 20 * mm

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=MARGIN, bottomMargin=MARGIN,
    title="Click AI Agency - Service Agreement - Haleh Cake",
    author="Click AI Agency"
)

def s(name, **kw):
    return ParagraphStyle(name, **kw)

title_style = s("Title", fontName="Helvetica-Bold", fontSize=22, textColor=BLACK, leading=28, spaceAfter=4)
subtitle_style = s("Subtitle", fontName="Helvetica", fontSize=11, textColor=GREY, leading=16, spaceAfter=20)
h1 = s("H1", fontName="Helvetica-Bold", fontSize=14, textColor=BLACK, leading=20, spaceBefore=20, spaceAfter=8)
h2 = s("H2", fontName="Helvetica-Bold", fontSize=11, textColor=BLACK, leading=16, spaceBefore=14, spaceAfter=6)
body = s("Body", fontName="Helvetica", fontSize=10, textColor=BLACK, leading=16, spaceAfter=6)
body_bold = s("BodyBold", fontName="Helvetica-Bold", fontSize=10, textColor=BLACK, leading=16, spaceAfter=6)
body_indent = s("BodyIndent", fontName="Helvetica", fontSize=10, textColor=BLACK, leading=16, spaceAfter=4, leftIndent=16)
body_small = s("BodySmall", fontName="Helvetica", fontSize=9, textColor=GREY, leading=14, spaceAfter=4)

def rule():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=8, spaceBefore=8)

story = []

# LOGO HEADER
if os.path.exists(LOGO):
    logo = Image(LOGO, width=40*mm, height=40*mm)
    logo.hAlign = 'LEFT'
    story.append(logo)
    story.append(Spacer(1, 4*mm))

# HEADER
story.append(Paragraph("SERVICE AGREEMENT", title_style))
story.append(Paragraph("Click AI Agency Ltd", subtitle_style))
story.append(rule())
story.append(Spacer(1, 4*mm))

# PARTIES
story.append(Paragraph("1. PARTIES", h1))
story.append(Paragraph("This Service Agreement (the \"Agreement\") is entered into on the date of last signature below, between:", body))
story.append(Spacer(1, 2*mm))

parties = [
    [Paragraph("<b>Service Provider:</b>", body), Paragraph("Click AI Agency Ltd", body)],
    [Paragraph("", body), Paragraph("Companies House registered", body_small)],
    [Paragraph("", body), Paragraph("Email: hello@clickaiagency.com", body_small)],
    [Paragraph("", body), Paragraph("Website: clickaiagency.com", body_small)],
    [Paragraph("", body), Paragraph(""), ],
    [Paragraph("<b>Client:</b>", body), Paragraph("Haleh Cake", body)],
    [Paragraph("", body), Paragraph("[Client Address]", body_small)],
    [Paragraph("", body), Paragraph("[Client Email]", body_small)],
    [Paragraph("", body), Paragraph("[Client Contact Name]", body_small)],
]
pt = Table(parties, colWidths=[45*mm, W - 2*MARGIN - 45*mm])
pt.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING", (0,0), (-1,-1), 2),
    ("BOTTOMPADDING", (0,0), (-1,-1), 2),
]))
story.append(pt)
story.append(Spacer(1, 4*mm))

# SERVICES
story.append(Paragraph("2. SERVICES", h1))
story.append(Paragraph("The Service Provider agrees to deliver the following services to the Client:", body))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>2.1 AI Voice Receptionist</b>", h2))
story.append(Paragraph("Design, build, and deploy a custom AI voice receptionist configured specifically for the Client's business. The voice agent will:", body))
story.append(Paragraph("a) Answer inbound phone calls 24 hours a day, 7 days a week", body_indent))
story.append(Paragraph("b) Handle enquiries based on the Client's products, opening hours, and ordering process", body_indent))
story.append(Paragraph("c) Take orders and booking requests automatically", body_indent))
story.append(Paragraph("d) Send order confirmations and reminders via WhatsApp or SMS", body_indent))
story.append(Paragraph("e) Capture lead information and forward to the Client", body_indent))
story.append(Paragraph("f) Provide call transcripts and analytics reporting", body_indent))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>2.2 WhatsApp Business Automation</b>", h2))
story.append(Paragraph("Setup and management of automated WhatsApp communication for the Client's business, including:", body))
story.append(Paragraph("a) Automated responses to customer enquiries via WhatsApp", body_indent))
story.append(Paragraph("b) Order confirmations and status updates", body_indent))
story.append(Paragraph("c) Follow-up messages after purchases or orders", body_indent))
story.append(Paragraph("d) Review request automation", body_indent))
story.append(Paragraph("e) FAQ handling trained on the Client's products and services", body_indent))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>2.3 Social Media Content Creation and Management</b>", h2))
story.append(Paragraph("Creation and management of the Client's social media presence across the following platforms:", body))
story.append(Spacer(1, 1*mm))

platforms = [
    [Paragraph("<b>Platform</b>", body_bold), Paragraph("<b>Included</b>", body_bold)],
    [Paragraph("Instagram", body), Paragraph("Yes", body)],
    [Paragraph("Facebook", body), Paragraph("Yes", body)],
    [Paragraph("TikTok", body), Paragraph("Yes", body)],
]
plt_table = Table(platforms, colWidths=[60*mm, W - 2*MARGIN - 60*mm])
plt_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#0D0D0D")),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(plt_table)
story.append(Spacer(1, 2*mm))

story.append(Paragraph("Services include:", body))
story.append(Paragraph("a) Content creation: graphics, photography direction, captions, and scheduling", body_indent))
story.append(Paragraph("b) Original content production: carousels, reels, stories, and static posts", body_indent))
story.append(Paragraph("c) Monthly content calendar with Client approval before publishing", body_indent))
story.append(Paragraph("d) Community management: responding to comments and direct messages", body_indent))
story.append(Paragraph("e) Google review management: response drafting and review request automation", body_indent))
story.append(Paragraph("f) Hashtag research and content strategy aligned to business goals", body_indent))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>2.4 Content Approval</b>", h2))
story.append(Paragraph("All content, text, images, design changes, and updates published to the Client's social media accounts must be reviewed and approved by the Client (or their designated representative) before going live. This includes:", body))
story.append(Paragraph("a) Social media posts, captions, reels, and scheduled content", body_indent))
story.append(Paragraph("b) Responses to customer reviews", body_indent))
story.append(Paragraph("c) Any promotional or campaign content", body_indent))
story.append(Spacer(1, 1*mm))
story.append(Paragraph("The Service Provider will provide content for review via email or an agreed approval workflow. The Client agrees to respond to approval requests within 5 business days. Content not approved or rejected within this period may be deferred to the next scheduled update cycle.", body_small))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>2.5 Case Study Permission</b>", h2))
story.append(Paragraph("In consideration of the waived setup fee (see Section 3.1), the Client grants the Service Provider permission to:", body))
story.append(Paragraph("a) Use the Client's business name, logo, and a description of the services delivered as a case study on the Service Provider's website, social media, and marketing materials", body_indent))
story.append(Paragraph("b) Reference the Client's business in proposals, presentations, and sales conversations with prospective clients", body_indent))
story.append(Paragraph("c) Share anonymised performance metrics (e.g., calls answered, engagement growth) as part of the case study", body_indent))
story.append(Spacer(1, 1*mm))
story.append(Paragraph("The Service Provider will share the case study content with the Client for approval before publishing. The Client may request removal of the case study at any time by providing written notice.", body_small))

story.append(PageBreak())

# PRICING
story.append(Paragraph("3. PRICING AND PAYMENT", h1))

story.append(Paragraph("<b>3.1 Setup Fee</b>", h2))
story.append(Paragraph("The standard one-time setup fee for the Click+ package is 750. <b>This fee has been waived in full</b> in consideration of the Client's agreement to participate as a case study (see Section 2.5).", body))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>3.2 Monthly Service Fee</b>", h2))
story.append(Paragraph("The standard monthly fee for the Click+ package is 797 per month. The following introductory discount structure applies:", body))
story.append(Spacer(1, 2*mm))

discount_data = [
    [Paragraph("<b>Period</b>", body_bold), Paragraph("<b>Discount</b>", body_bold), Paragraph("<b>Monthly fee</b>", body_bold)],
    [Paragraph("Month 1", body), Paragraph("50% off", body), Paragraph("398.50", body)],
    [Paragraph("Months 2 and 3", body), Paragraph("20% off", body), Paragraph("637.60", body)],
    [Paragraph("Month 4 onwards", body), Paragraph("10% loyalty discount", body), Paragraph("717.30", body)],
]
dt = Table(discount_data, colWidths=[55*mm, 45*mm, W - 2*MARGIN - 100*mm])
dt.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#0D0D0D")),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story.append(dt)
story.append(Spacer(1, 2*mm))

story.append(Paragraph("a) The 10% loyalty discount applies for the duration of the first 24 months of this Agreement", body_indent))
story.append(Paragraph("b) After 24 months, the monthly fee will be reviewed. The Service Provider will provide 30 days written notice of any pricing changes.", body_indent))
story.append(Paragraph("c) The monthly fee includes up to 1,000 minutes of AI voice and WhatsApp usage per month", body_indent))
story.append(Paragraph("d) Usage exceeding the included minutes will be charged at the overage rates specified in Schedule A", body_indent))
story.append(Paragraph("e) Monthly billing begins after the 7-day trial period (see Section 4)", body_indent))
story.append(Paragraph("f) Payment is due within 7 days of invoice date", body_indent))
story.append(Paragraph("g) All prices are exclusive of VAT where applicable", body_indent))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>3.3 Additional Services</b>", h2))
add_on_data = [
    [Paragraph("<b>Service</b>", body_bold), Paragraph("<b>Fee</b>", body_bold), Paragraph("<b>Notes</b>", body_bold)],
    [Paragraph("Google Workspace (Gmail)", body), Paragraph("7.00/month", body), Paragraph("Optional. Client may pay directly or through the Service Provider.", body)],
    [Paragraph("Blog/WordPress integration", body), Paragraph("Included (Year 1)", body), Paragraph("Review at 12 months.", body)],
]
at = Table(add_on_data, colWidths=[50*mm, 40*mm, W - 2*MARGIN - 90*mm])
at.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#0D0D0D")),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story.append(at)
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>3.4 Payment Method</b>", h2))
story.append(Paragraph("Payments may be made by bank transfer, direct debit, or any other method agreed in writing between the parties.", body))

# TRIAL
story.append(Paragraph("4. TRIAL PERIOD", h1))
story.append(Paragraph("The Client is entitled to a 7-day trial period beginning on the go-live date of the system. During this period:", body))
story.append(Paragraph("a) The Client may use all services as described in Section 2", body_indent))
story.append(Paragraph("b) No monthly fee is charged during the trial period", body_indent))
story.append(Paragraph("c) If the Client wishes to cancel during the trial period, they must notify the Service Provider in writing before the trial expires", body_indent))
story.append(Paragraph("d) If the Client cancels during the trial period, no monthly fees will be charged", body_indent))
story.append(Paragraph("e) If the Client does not cancel during the trial period, monthly billing begins automatically on the day following the trial expiry", body_indent))

# TERM
story.append(Paragraph("5. TERM AND TERMINATION", h1))

story.append(Paragraph("<b>5.1 Contract Term</b>", h2))
story.append(Paragraph("This Agreement operates on a monthly rolling basis. There is no minimum contract length beyond the current billing month.", body))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>5.2 Termination by Client</b>", h2))
story.append(Paragraph("The Client may terminate this Agreement at any time by providing 30 days written notice to the Service Provider. Upon termination:", body))
story.append(Paragraph("a) The Client is responsible for payment of all fees incurred up to the termination date", body_indent))
story.append(Paragraph("b) The Service Provider will deliver any outstanding work completed up to the termination date", body_indent))
story.append(Paragraph("c) The AI voice agent will be deactivated at the end of the notice period", body_indent))
story.append(Paragraph("d) All social media content created for the Client (graphics, captions, templates) will be delivered to the Client at no extra charge", body_indent))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>5.3 Termination by Service Provider</b>", h2))
story.append(Paragraph("The Service Provider may terminate this Agreement with 30 days written notice, or immediately if:", body))
story.append(Paragraph("a) The Client fails to make payment within 14 days of the due date after a written reminder", body_indent))
story.append(Paragraph("b) The Client breaches any material term of this Agreement and fails to remedy the breach within 14 days of written notice", body_indent))

story.append(PageBreak())

# IP
story.append(Paragraph("6. INTELLECTUAL PROPERTY", h1))
story.append(Paragraph("a) Social media content created by the Service Provider for the Client (graphics, captions, templates, reels) is the property of the Client from the date of creation.", body_indent))
story.append(Paragraph("b) The AI voice agent system, underlying technology, workflows, and automation logic remain the intellectual property of the Service Provider at all times. The Client is granted a licence to use the system for the duration of this Agreement.", body_indent))
story.append(Paragraph("c) Upon termination, the Service Provider will deliver all social media content, templates, and assets to the Client at no charge within 14 days of the termination date.", body_indent))

# CONFIDENTIALITY
story.append(Paragraph("7. CONFIDENTIALITY", h1))
story.append(Paragraph("Both parties agree to keep confidential any proprietary or sensitive information shared during the course of this Agreement. This includes, but is not limited to:", body))
story.append(Paragraph("a) Business strategies, pricing, and financial information", body_indent))
story.append(Paragraph("b) Customer data and contact information", body_indent))
story.append(Paragraph("c) Technical specifications and system configurations", body_indent))
story.append(Paragraph("d) Any information marked as confidential by either party", body_indent))
story.append(Spacer(1, 1*mm))
story.append(Paragraph("This obligation survives termination of this Agreement for a period of 2 years.", body))

# DATA PROTECTION
story.append(Paragraph("8. DATA PROTECTION AND GDPR", h1))
story.append(Paragraph("a) The Service Provider will process personal data only as necessary to deliver the services described in this Agreement and in compliance with the UK General Data Protection Regulation (UK GDPR) and the Data Protection Act 2018.", body_indent))
story.append(Paragraph("b) The Client remains the data controller for any customer data processed through the AI voice agent or social media channels. The Service Provider acts as a data processor.", body_indent))
story.append(Paragraph("c) The Service Provider will implement appropriate technical and organisational measures to protect personal data against unauthorised access, loss, or destruction.", body_indent))
story.append(Paragraph("d) In the event of a data breach, the Service Provider will notify the Client within 72 hours of becoming aware of the breach.", body_indent))
story.append(Paragraph("e) Upon termination of this Agreement, the Service Provider will delete or return all personal data held on behalf of the Client within 30 days, unless retention is required by law.", body_indent))

# LIABILITY
story.append(Paragraph("9. LIABILITY", h1))
story.append(Paragraph("a) The Service Provider's total liability under this Agreement shall not exceed the total fees paid by the Client in the 12 months preceding the claim.", body_indent))
story.append(Paragraph("b) The Service Provider shall not be liable for any indirect, consequential, or incidental damages, including loss of revenue, loss of data, or loss of business opportunity.", body_indent))
story.append(Paragraph("c) The Service Provider does not guarantee uninterrupted service. The AI voice agent operates at 99.5% target uptime. In the event of system downtime, calls are automatically diverted to the Client's main phone line.", body_indent))
story.append(Paragraph("d) The Service Provider is not liable for any losses arising from information provided by the Client that is inaccurate, incomplete, or out of date.", body_indent))

# FORCE MAJEURE
story.append(Paragraph("10. FORCE MAJEURE", h1))
story.append(Paragraph("Neither party shall be liable for any failure or delay in performing their obligations under this Agreement where such failure or delay results from circumstances beyond the reasonable control of that party, including but not limited to natural disasters, pandemics, government actions, internet outages, or third-party service failures.", body))

# GENERAL
story.append(Paragraph("11. GENERAL PROVISIONS", h1))
story.append(Paragraph("a) This Agreement constitutes the entire agreement between the parties and supersedes all prior discussions, negotiations, and agreements.", body_indent))
story.append(Paragraph("b) Any amendments to this Agreement must be made in writing and signed by both parties.", body_indent))
story.append(Paragraph("c) This Agreement shall be governed by and construed in accordance with the laws of England and Wales.", body_indent))
story.append(Paragraph("d) Any disputes arising from this Agreement shall be subject to the exclusive jurisdiction of the courts of England and Wales.", body_indent))
story.append(Paragraph("e) If any provision of this Agreement is found to be invalid or unenforceable, the remaining provisions shall continue in full force and effect.", body_indent))

story.append(PageBreak())

# SCHEDULE A
story.append(Paragraph("SCHEDULE A: PRICING SUMMARY", h1))
story.append(rule())
story.append(Spacer(1, 4*mm))

pricing_data = [
    [Paragraph("<b>Item</b>", body_bold), Paragraph("<b>Amount</b>", body_bold)],
    [Paragraph("Package", body), Paragraph("Click+", body)],
    [Paragraph("Setup fee", body), Paragraph("Waived (case study exchange)", body)],
    [Paragraph("Standard monthly fee", body), Paragraph("797.00 per month", body)],
    [Paragraph("Month 1 (50% discount)", body), Paragraph("398.50", body)],
    [Paragraph("Months 2 and 3 (20% discount)", body), Paragraph("637.60 per month", body)],
    [Paragraph("Month 4 onwards (10% loyalty discount)", body), Paragraph("717.30 per month", body)],
    [Paragraph("Included minutes", body), Paragraph("1,000 minutes/month (voice + WhatsApp)", body)],
    [Paragraph("Social media platforms", body), Paragraph("Instagram, Facebook, TikTok", body)],
    [Paragraph("Blog/WordPress integration (Year 1)", body), Paragraph("Included", body)],
    [Paragraph("Google Workspace (optional)", body), Paragraph("7.00 per month", body)],
    [Paragraph("Trial period", body), Paragraph("7 days from go-live date", body)],
    [Paragraph("Billing start date", body), Paragraph("Day after trial period ends", body)],
    [Paragraph("Loyalty discount term", body), Paragraph("24 months, then review with 30 days notice", body)],
    [Paragraph("Notice period", body), Paragraph("30 days written notice", body)],
]
pt2 = Table(pricing_data, colWidths=[75*mm, W - 2*MARGIN - 75*mm])
pt2.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#0D0D0D")),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story.append(pt2)
story.append(Spacer(1, 4*mm))

story.append(Paragraph("<b>Overage Rates</b>", h2))
overage_data = [
    [Paragraph("<b>Item</b>", body_bold), Paragraph("<b>Rate</b>", body_bold)],
    [Paragraph("Voice minutes (over 1,000/month)", body), Paragraph("0.20 per minute", body)],
    [Paragraph("WhatsApp messages (over plan)", body), Paragraph("0.05 per message", body)],
    [Paragraph("Additional phone number", body), Paragraph("10.00 per month", body)],
    [Paragraph("Additional social platform", body), Paragraph("150.00 per month", body)],
]
ot = Table(overage_data, colWidths=[75*mm, W - 2*MARGIN - 75*mm])
ot.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#0D0D0D")),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story.append(ot)

story.append(Spacer(1, 8*mm))

# SIGNATURES
story.append(Paragraph("SIGNATURES", h1))
story.append(rule())
story.append(Spacer(1, 6*mm))

story.append(Paragraph("<b>For the Service Provider: Click AI Agency Ltd</b>", body_bold))
story.append(Spacer(1, 2*mm))

sig_provider = [
    [Paragraph("Name:", body), Paragraph("Hadi Yazdani", body)],
    [Paragraph("Title:", body), Paragraph("Director", body)],
    [Paragraph("Signature:", body), Paragraph("_________________________________", body)],
    [Paragraph("Date:", body), Paragraph("_________________________________", body)],
]
sp = Table(sig_provider, colWidths=[30*mm, 80*mm])
sp.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(sp)

story.append(Spacer(1, 8*mm))

story.append(Paragraph("<b>For the Client: Haleh Cake</b>", body_bold))
story.append(Spacer(1, 2*mm))

sig_client = [
    [Paragraph("Name:", body), Paragraph("_________________________________", body)],
    [Paragraph("Title:", body), Paragraph("_________________________________", body)],
    [Paragraph("Signature:", body), Paragraph("_________________________________", body)],
    [Paragraph("Date:", body), Paragraph("_________________________________", body)],
]
sc = Table(sig_client, colWidths=[30*mm, 80*mm])
sc.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(sc)

story.append(Spacer(1, 10*mm))
story.append(rule())
story.append(Paragraph("Click AI Agency Ltd | hello@clickaiagency.com | clickaiagency.com", body_small))

# BUILD
doc.build(story)
print("Haleh Cake contract PDF generated successfully.")
