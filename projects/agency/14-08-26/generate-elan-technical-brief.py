#!/usr/bin/env python3
"""Generate EL&N Technical Brief PDF for IT team meeting.

Companion document to the 24 July Elan proposal, structured for IT
due-diligence conversation. Same EL&N brand family (blush + charcoal + gold),
denser typography for technical density, heavy on Q&A format.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable,
    KeepTogether,
)

OUTPUT = "/Users/hadi/Developer/Jodie-AI/projects/agency/14-08-26/elan-technical-brief.pdf"

# --- EL&N palette (matched to 24 July proposal) ---
BLUSH      = colors.HexColor("#E5CBC0")
BLUSH_DK   = colors.HexColor("#D4B4A6")
CREAM      = colors.HexColor("#FAF5F0")
SOFT_PINK  = colors.HexColor("#F5DDE0")
ROSE       = colors.HexColor("#C58A8A")
ROSE_MUTED = colors.HexColor("#B78585")
CHARCOAL   = colors.HexColor("#1A1613")
INK        = colors.HexColor("#2A2320")
BODY       = colors.HexColor("#3A322D")
GREY       = colors.HexColor("#8A857F")
NUDE       = colors.HexColor("#EDDDCE")
HAIR       = colors.HexColor("#E8DED4")
WHITE      = colors.HexColor("#FFFFFF")

W, H = A4
MARGIN = 20 * mm
BAND_H = 55 * mm

LOGO_PATHS = [
    "/Users/hadi/Developer/Jodie-AI/brand-assets/Click AI Logos/click-logo-white.png",
    "/Users/hadi/Developer/Jodie-AI/brand-assets/Click AI Logos/click-logo.png",
]
LOGO = next((p for p in LOGO_PATHS if os.path.exists(p)), None)


def _s(name, **kw):
    return ParagraphStyle(name, **kw)


S = {
    "eyebrow": _s("eyebrow", fontName="Helvetica-Bold", fontSize=7.5,
                  textColor=ROSE_MUTED, leading=10, spaceAfter=3),
    "sec_num": _s("sec_num", fontName="Helvetica-Bold", fontSize=8,
                  textColor=ROSE_MUTED, leading=10, spaceAfter=2),
    "sec_title": _s("sec_title", fontName="Helvetica-Bold", fontSize=12.5,
                    textColor=CHARCOAL, leading=15, spaceAfter=4),
    "body": _s("body", fontName="Helvetica", fontSize=9.5, textColor=BODY,
               leading=13.5, spaceAfter=5),
    "body_bold": _s("body_bold", fontName="Helvetica-Bold", fontSize=9.5,
                    textColor=CHARCOAL, leading=13.5, spaceAfter=4),
    "body_small": _s("body_small", fontName="Helvetica", fontSize=8.5,
                     textColor=TAUPE if False else GREY, leading=12, spaceAfter=4),
    "q_label": _s("q_label", fontName="Helvetica-Bold", fontSize=8,
                  textColor=ROSE, leading=11, spaceAfter=2),
    "q_text": _s("q_text", fontName="Helvetica-Bold", fontSize=9.5,
                 textColor=CHARCOAL, leading=13, spaceAfter=3),
    "a_text": _s("a_text", fontName="Helvetica", fontSize=9.5, textColor=BODY,
                 leading=13.5, spaceAfter=8),
    "meta_k": _s("meta_k", fontName="Helvetica-Bold", fontSize=7,
                 textColor=ROSE_MUTED, leading=10, spaceAfter=2),
    "meta_v": _s("meta_v", fontName="Helvetica-Bold", fontSize=9.5,
                 textColor=CHARCOAL, leading=12),
    "th": _s("th", fontName="Helvetica-Bold", fontSize=8.5, textColor=WHITE,
             leading=11),
    "td": _s("td", fontName="Helvetica", fontSize=9, textColor=BODY,
             leading=12.5),
    "td_bold": _s("td_bold", fontName="Helvetica-Bold", fontSize=9,
                  textColor=CHARCOAL, leading=12.5),
    "footer": _s("footer", fontName="Helvetica", fontSize=7.5, textColor=GREY,
                 leading=10, alignment=TA_CENTER),
    "confirm": _s("confirm", fontName="Helvetica-Bold", fontSize=8.5,
                  textColor=colors.HexColor("#B45C00"), leading=11,
                  spaceAfter=6),
}


def _page_bg(canvas):
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)


def first_page(canvas, doc):
    canvas.saveState()
    _page_bg(canvas)
    canvas.setFillColor(CHARCOAL)
    canvas.rect(0, H - BAND_H, W, BAND_H, fill=1, stroke=0)
    canvas.setFillColor(ROSE)
    canvas.rect(0, H - BAND_H - 0.6 * mm, W, 0.6 * mm, fill=1, stroke=0)
    if LOGO:
        try:
            canvas.drawImage(LOGO, MARGIN, H - 20 * mm, width=22 * mm,
                             height=22 * mm, preserveAspectRatio=True,
                             mask='auto')
        except Exception:
            pass
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(colors.HexColor("#D0C5B4"))
    canvas.drawRightString(W - MARGIN, H - 14 * mm,
                           "C L I C K   A I   A G E N C Y")
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(colors.HexColor("#D0C5B4"))
    canvas.drawString(MARGIN, H - 30 * mm,
                      "T E C H N I C A L   B R I E F")
    canvas.setFont("Helvetica-Bold", 23)
    canvas.setFillColor(WHITE)
    canvas.drawString(MARGIN, H - 41 * mm,
                      "Ella + Cake Ordering System")
    canvas.setFont("Helvetica", 11.5)
    canvas.setFillColor(colors.HexColor("#D0C5B4"))
    canvas.drawString(MARGIN, H - 48 * mm,
                      "For the EL&N London IT team review meeting")
    footer(canvas, doc)
    canvas.restoreState()


def later_pages(canvas, doc):
    canvas.saveState()
    _page_bg(canvas)
    canvas.setFillColor(CHARCOAL)
    canvas.rect(0, H - 12 * mm, W, 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(ROSE)
    canvas.rect(0, H - 12.5 * mm, W, 0.5 * mm, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.setFillColor(WHITE)
    canvas.drawString(MARGIN, H - 8 * mm,
                      "Technical Brief  ·  EL&N Cake Ordering System")
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.setFillColor(colors.HexColor("#D0C5B4"))
    canvas.drawRightString(W - MARGIN, H - 8 * mm, "CLICK AI AGENCY")
    footer(canvas, doc)
    canvas.restoreState()


def footer(canvas, doc):
    canvas.setStrokeColor(ROSE)
    canvas.setLineWidth(0.4)
    canvas.line(MARGIN, 16 * mm, W - MARGIN, 16 * mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(MARGIN, 11 * mm,
                      "Click AI Agency Ltd  ·  clickaiagency.com  ·  "
                      "hello@clickaiagency.com")
    canvas.drawRightString(W - MARGIN, 11 * mm,
                           f"Page {canvas.getPageNumber()}")


def section(num, title):
    return [
        Spacer(1, 10),
        Paragraph(f"SECTION {num:02d}", S["sec_num"]),
        Paragraph(title, S["sec_title"]),
        HRFlowable(width="100%", thickness=0.5, color=ROSE,
                   spaceBefore=1, spaceAfter=8),
    ]


def qa(q, a):
    return [
        Paragraph(f"Q. {q}", S["q_text"]),
        Paragraph(a, S["a_text"]),
    ]


def meta_card(k, v):
    inner = Table([[Paragraph(k, S["meta_k"])], [Paragraph(v, S["meta_v"])]],
                  colWidths=[52 * mm])
    inner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NUDE),
        ("LINEABOVE", (0, 0), (-1, 0), 1.2, ROSE),
        ("TOPPADDING", (0, 0), (-1, 0), 5),
        ("TOPPADDING", (0, 1), (-1, 1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 0),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return inner


story = []
story.append(Spacer(1, BAND_H - MARGIN + 3 * mm))

meta = Table([[
    meta_card("PREPARED FOR", "EL&amp;N London IT team"),
    meta_card("PREPARED BY", "Click AI Agency"),
    meta_card("DATE", "14 August 2026"),
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

# ============ SECTION 1: OVERVIEW ============
story += section(1, "System at a glance")
story.append(Paragraph(
    "The Ella + Cake Ordering System is a purpose-built, custom-designed "
    "software stack that turns EL&amp;N's inbound cake enquiries into paid, "
    "kitchen-ready orders without manual email back-and-forth. It has four "
    "integrated components delivered as one service:", S["body"]))

comp_data = [
    [Paragraph("COMPONENT", S["th"]),
     Paragraph("ROLE", S["th"])],
    [Paragraph("<b>Ella</b> voice agent", S["td_bold"]),
     Paragraph("Answers the cake ordering line 24/7. Handles standard cake "
               "orders end to end. For custom cakes, sends the caller a link "
               "to the bespoke designer.", S["td"])],
    [Paragraph("<b>Bespoke cake designer</b> web page", S["td_bold"]),
     Paragraph("Custom-built visual designer where customers with specific "
               "requirements build and preview their cake step by step, then "
               "confirm and pay.", S["td"])],
    [Paragraph("<b>Stripe</b> payment layer", S["td_bold"]),
     Paragraph("Handles card capture and settlement. Card data never touches "
               "Click or EL&amp;N systems; Stripe is the PCI-DSS Level 1 "
               "service of record. Payouts to EL&amp;N every 2 to 3 days.",
               S["td"])],
    [Paragraph("<b>Click Pro</b> order dashboard", S["td_bold"]),
     Paragraph("Every completed order lands here with the cake image, spec, "
               "customer contact, and pickup or delivery details, ready for "
               "the kitchen. Single pane of glass for the operation.",
               S["td"])],
]
comp_table = Table(comp_data,
                   colWidths=[50 * mm, W - 2 * MARGIN - 50 * mm])
comp_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), CHARCOAL),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1),
     [WHITE, colors.HexColor("#FBF7F0")]),
    ("LINEABOVE", (0, 0), (-1, 0), 0.5, ROSE),
    ("LINEBELOW", (0, 0), (-1, 0), 0.5, ROSE),
    ("LINEBELOW", (0, -1), (-1, -1), 0.5, ROSE),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(comp_table)

# ============ SECTION 2: STACK ============
story += section(2, "Stack and hosting")
story.append(Paragraph(
    "The system runs on established, enterprise-grade providers. No component "
    "is custom infrastructure; every provider below has published SOC 2, "
    "ISO 27001, or equivalent certifications.", S["body"]))

stack_data = [
    [Paragraph("LAYER", S["th"]),
     Paragraph("TECHNOLOGY / PROVIDER", S["th"]),
     Paragraph("PURPOSE", S["th"]),
     Paragraph("REGION", S["th"])],
    [Paragraph("<b>Voice AI</b>", S["td_bold"]),
     Paragraph("Vapi + ElevenLabs", S["td"]),
     Paragraph("Voice agent orchestration and text-to-speech", S["td"]),
     Paragraph("EU/UK [CONFIRM]", S["td"])],
    [Paragraph("<b>Telephony</b>", S["td_bold"]),
     Paragraph("Twilio", S["td"]),
     Paragraph("Inbound number, call routing, recording", S["td"]),
     Paragraph("EU/UK", S["td"])],
    [Paragraph("<b>Web application</b>", S["td_bold"]),
     Paragraph("Vercel", S["td"]),
     Paragraph("Bespoke cake designer + Click Pro dashboard hosting",
               S["td"]),
     Paragraph("EU/UK [CONFIRM]", S["td"])],
    [Paragraph("<b>Database</b>", S["td_bold"]),
     Paragraph("Supabase (Postgres)", S["td"]),
     Paragraph("Order records, tenant configuration, customer contact",
               S["td"]),
     Paragraph("EU/UK [CONFIRM]", S["td"])],
    [Paragraph("<b>Payments</b>", S["td_bold"]),
     Paragraph("Stripe", S["td"]),
     Paragraph("Card capture, settlement, payouts", S["td"]),
     Paragraph("UK", S["td"])],
    [Paragraph("<b>Messaging</b>", S["td_bold"]),
     Paragraph("WhatsApp Business API + SMS via Twilio", S["td"]),
     Paragraph("Order confirmations, status updates to customers",
               S["td"]),
     Paragraph("EU/UK", S["td"])],
    [Paragraph("<b>Automation</b>", S["td_bold"]),
     Paragraph("n8n (self-hosted)", S["td"]),
     Paragraph("Workflow orchestration between components",
               S["td"]),
     Paragraph("EU (Hostinger VPS)", S["td"])],
]
stack_table = Table(stack_data,
                    colWidths=[28 * mm, 42 * mm,
                               W - 2 * MARGIN - 28 * mm - 42 * mm - 26 * mm,
                               26 * mm])
stack_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), CHARCOAL),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1),
     [WHITE, colors.HexColor("#FBF7F0")]),
    ("LINEABOVE", (0, 0), (-1, 0), 0.5, ROSE),
    ("LINEBELOW", (0, 0), (-1, 0), 0.5, ROSE),
    ("LINEBELOW", (0, -1), (-1, -1), 0.5, ROSE),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story.append(stack_table)
story.append(Spacer(1, 4))
story.append(Paragraph(
    "<b>[CONFIRM before meeting]:</b> Regional hosting choices for Vapi, "
    "Vercel, and Supabase. All three support EU/UK regions; we will confirm "
    "the deployment region for the EL&amp;N London tenant is EU/UK before "
    "go-live.", S["confirm"]))

# ============ SECTION 3: SECURITY ============
story += section(3, "Security and data protection")
story += qa(
    "Where is EL&amp;N customer data stored?",
    "Customer contact and order metadata are stored in Supabase (Postgres), "
    "with the EL&amp;N London tenant configured to a UK or EU region. "
    "Payment card data is stored by Stripe only; it does not touch Click's "
    "systems or EL&amp;N's."
)
story += qa(
    "What encryption is in place?",
    "TLS 1.2 or higher on all data in transit. AES-256 on all data at rest "
    "(Supabase default). Stripe handles PCI DSS Level 1 encryption for card "
    "data end to end."
)
story += qa(
    "How is access controlled at Click?",
    "Only named Click personnel have production access, gated by SSO and MFA. "
    "Access is scoped by role (support, engineering, admin). Every "
    "administrative action on the EL&amp;N tenant is logged with timestamp "
    "and operator identity."
)
story += qa(
    "Are you UK GDPR compliant?",
    "Yes. Click AI Agency acts as Data Processor for EL&amp;N under UK GDPR. "
    "We will sign a Data Processing Agreement (DPA) as part of contract "
    "execution. Our sub-processors (Vapi, ElevenLabs, Twilio, Vercel, "
    "Supabase, Stripe) all have published GDPR compliance and are on our "
    "sub-processor register available to EL&amp;N on request."
)
story += qa(
    "How long is customer data retained?",
    "Order records: retained for 7 years for accounting purposes, then "
    "deleted. Call recordings: retained for 90 days for quality assurance, "
    "then deleted. Customer contact records: retained as long as the "
    "customer relationship is active; deleted on written request under "
    "GDPR right to erasure within 30 days."
)
story += qa(
    "How do you handle a data breach?",
    "24/7 monitoring on all production systems. In the event of a confirmed "
    "breach affecting EL&amp;N data, we notify EL&amp;N within 24 hours and "
    "the ICO within 72 hours per UK GDPR. Full incident report follows "
    "within 5 business days."
)

# ============ SECTION 4: INTEGRATIONS ============
story += section(4, "Integrations and data flow")
story += qa(
    "What does the end-to-end flow look like for one order?",
    "1. Customer calls the EL&amp;N cake line. 2. Twilio routes the call to "
    "Vapi. 3. Vapi runs the Ella agent script; ElevenLabs produces her voice. "
    "4. For standard orders: Ella captures order + contact and triggers a "
    "Stripe payment link via SMS/WhatsApp. For custom orders: Ella sends the "
    "designer page link. 5. On payment success, Stripe fires a webhook to "
    "our backend. 6. The order (with image and full spec) is written to "
    "Supabase and appears in Click Pro for the kitchen."
)
story += qa(
    "Does anything integrate with EL&amp;N's existing systems?",
    "For go-live day 1, no direct integration with EL&amp;N's internal "
    "systems is required. The system runs standalone. If EL&amp;N later "
    "wants integration with an existing POS, accounting system, or CRM, we "
    "can scope that separately."
)
story += qa(
    "Can the system export order data?",
    "Yes. Click Pro provides CSV export of all orders for any date range. A "
    "read-only API endpoint can also be provisioned if EL&amp;N's accounting "
    "or reporting team needs programmatic access."
)

# ============ SECTION 5: AVAILABILITY ============
story += section(5, "Availability, monitoring, and support")
story += qa(
    "What uptime do you commit to?",
    "99% target uptime on the Click Pro platform and voice agent, per "
    "calendar month, excluding scheduled maintenance windows notified in "
    "advance. Underlying provider SLAs (Vercel, Supabase, Stripe, Twilio) "
    "are all 99.9%+."
)
story += qa(
    "How is the system monitored?",
    "Continuous monitoring on all layers: uptime probes on Ella and the "
    "designer page every 60 seconds; error tracking on all backend jobs; "
    "call-quality metrics on every voice interaction. On-call rotation "
    "responds within 15 minutes to critical alerts, 24/7."
)
story += qa(
    "What happens if a component goes down?",
    "The stack is designed for graceful degradation. If Ella is unavailable, "
    "calls fall back to a recorded holding message and callback offer, so "
    "no order is silently lost. If Stripe is unavailable, the customer "
    "receives a retry link. If the designer page is unavailable, the caller "
    "is routed back to Ella for a phone-based order."
)
story += qa(
    "How are updates deployed?",
    "Changes to the EL&amp;N tenant configuration (menu, pricing, opening "
    "hours) are deployed within 48 hours of a written request, up to 10 per "
    "month. Platform-level updates are deployed on a rolling schedule with "
    "zero downtime. Major platform changes are communicated to EL&amp;N in "
    "advance."
)
story += qa(
    "What support do we get?",
    "A named dedicated account manager at Click AI Agency as the single "
    "point of contact, with same-business-day response. Emergency line for "
    "system-down issues, 24/7. Monthly service review meeting to walk "
    "through numbers, feedback, and any changes."
)

# ============ SECTION 6: MULTI-BRANCH ============
story += section(6, "Multi-branch deployment model")
story += qa(
    "How does the system scale to EL&amp;N's other branches?",
    "Each branch runs as a separate tenant instance: its own phone number, "
    "its own Stripe account and currency, its own menu and pricing, its own "
    "hours and time zone, its own included minutes and monitoring. Because "
    "the London build is the foundation, each additional branch deploys in "
    "a fraction of the time London took."
)
story += qa(
    "Is data isolated between branches?",
    "Yes. Tenant data isolation at the database level. No branch can see "
    "another branch's orders, customer records, or configuration. "
    "Administrative access is scoped per tenant."
)
story += qa(
    "Who owns the platform IP?",
    "The Ella platform, the cake designer page design, and the underlying "
    "systems remain the property of Click AI Agency and are licensed to "
    "EL&amp;N per site under the service agreement. EL&amp;N owns all its "
    "own data (orders, customer records, ad accounts, brand assets)."
)

# ============ SECTION 7: BUSINESS CONTINUITY ============
story += section(7, "Data ownership and business continuity")
story += qa(
    "What happens on termination?",
    "Per the service agreement: all EL&amp;N data (Click Pro records, "
    "customer contact database, voice agent call logs, advertising accounts) "
    "is exported and returned to EL&amp;N within 14 days. Administrator "
    "access to any ad accounts registered under EL&amp;N's name is handed "
    "over. Deletion from Click systems follows within a further 30 days."
)
story += qa(
    "What if Click AI Agency goes out of business?",
    "Contingency: (a) all EL&amp;N-owned data (orders, customers, "
    "campaigns, ad accounts) is under EL&amp;N's name where possible; "
    "(b) Stripe payouts continue directly to EL&amp;N's bank regardless of "
    "Click's status; (c) EL&amp;N holds admin credentials to its own "
    "Twilio number and can port it out; (d) source code and infrastructure "
    "documentation covering the EL&amp;N tenant would be escrowed on "
    "request at contract execution."
)

# ============ SECTION 8: WHAT WE NEED FROM YOU ============
story += section(8, "What EL&amp;N IT will need to provide")
inputs = [
    ("Domain and DNS access",
     "A subdomain of EL&amp;N (for example, cakes.elancafe.com) for the "
     "customer-facing designer page. We will provide the DNS records needed; "
     "EL&amp;N IT applies them."),
    ("Business Stripe account",
     "Either an existing EL&amp;N Stripe account for the London branch, or "
     "we can help EL&amp;N create one. Bank details for payouts remain "
     "under EL&amp;N's control at all times."),
    ("Menu and pricing input",
     "Current standard cake range with names, prices, images, and "
     "descriptions. Custom cake components (flavours, tiers, decorations, "
     "add-ons) with pricing rules."),
    ("Operating hours and lead times",
     "Cake ordering hours; earliest order lead time (for example, custom "
     "cakes 5 working days minimum); pickup or delivery slot rules."),
    ("Brand assets",
     "EL&amp;N logo files, brand fonts and colours, image library for the "
     "designer page. High-resolution product photography preferred."),
    ("Kitchen point of contact",
     "One nominated Head of Pastry or duty manager per shift, to be trained "
     "on Click Pro during onboarding."),
]
for k, v in inputs:
    story.append(Paragraph(f'<font color="#C58A8A">&#9679;</font>&nbsp;&nbsp;<b>{k}.</b> {v}', S["body"]))

# ============ SECTION 9: MEETING AGENDA SUGGESTION ============
story += section(9, "Suggested meeting agenda")
agenda = [
    "System walkthrough and demo (15 mins) — Ella on a live call, the designer page in action, an order landing in Click Pro",
    "Security and compliance Q&amp;A (15 mins) — anything not covered by this brief",
    "Integrations and data flow (10 mins) — where the boundaries sit between Click, Stripe, and EL&amp;N systems",
    "Multi-branch scaling (10 mins) — what the rollout playbook looks like once London is proven",
    "What EL&amp;N IT needs to action pre-go-live (10 mins) — DNS, Stripe account, brand assets",
    "Open questions and next steps (10 mins)",
]
for a in agenda:
    story.append(Paragraph(f'<font color="#C58A8A">&#9679;</font>&nbsp;&nbsp;{a}', S["body"]))

# ============ SECTION 10: OPEN ITEMS ============
story += section(10, "Open items to close in the meeting")
opens = [
    "Regional hosting confirmation across Vapi, Vercel, and Supabase for the EL&amp;N London tenant (EU/UK)",
    "Domain and subdomain decision for the designer page",
    "Stripe account preference (existing EL&amp;N account or new for this line)",
    "Any additional compliance certifications EL&amp;N IT requires beyond UK GDPR and Stripe PCI DSS",
    "Preferred format and cadence for the monthly service report",
    "Confirmation that the 1 September go-live target still holds",
]
for o in opens:
    story.append(Paragraph(f'<font color="#C58A8A">&#9679;</font>&nbsp;&nbsp;{o}', S["body"]))

story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=0.5, color=HAIR,
                        spaceBefore=2, spaceAfter=6))
story.append(Paragraph(
    "Prepared by Hadi Yazdani, CEO and Founder, Click AI Agency  ·  "
    "clickaiagency.com  ·  hello@clickaiagency.com",
    S["footer"]))


doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=15 * mm, bottomMargin=22 * mm,
    title="Ella + EL&N Cake Ordering System - Technical Brief",
    author="Click AI Agency",
    subject="Technical Brief for EL&N IT Team meeting",
)
doc.build(story, onFirstPage=first_page, onLaterPages=later_pages)
print(f"Elan Technical Brief generated at: {OUTPUT}")
