from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

OUTPUT = "/Users/hadi/Library/Mobile Documents/com~apple~CloudDocs/EA AI/projects/agency/outreach-system/email-outreach-setup-guide.pdf"

# Colours
BLACK       = colors.HexColor("#0D0D0D")
WHITE       = colors.HexColor("#FFFFFF")
ACCENT      = colors.HexColor("#6C63FF")
LIGHT_BG    = colors.HexColor("#F5F4FF")
BORDER      = colors.HexColor("#E0DEF7")
GREY        = colors.HexColor("#666666")
LIGHT_GREY  = colors.HexColor("#F8F8F8")
STEP_BG     = colors.HexColor("#0D0D0D")
GREEN       = colors.HexColor("#2D9E6B")
AMBER       = colors.HexColor("#D97706")

W, H = A4
MARGIN = 18 * mm

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=MARGIN,
    rightMargin=MARGIN,
    topMargin=MARGIN,
    bottomMargin=MARGIN,
    title="Email Outreach Setup Guide — Click AI Agency",
    author="Jodie / Click AI Agency"
)

styles = getSampleStyleSheet()

def style(name, **kw):
    return ParagraphStyle(name, **kw)

cover_title = style("CoverTitle",
    fontName="Helvetica-Bold", fontSize=28, textColor=WHITE,
    leading=36, spaceAfter=8)

cover_sub = style("CoverSub",
    fontName="Helvetica", fontSize=13, textColor=colors.HexColor("#B8B4F0"),
    leading=20, spaceAfter=4)

cover_meta = style("CoverMeta",
    fontName="Helvetica", fontSize=10, textColor=colors.HexColor("#888888"),
    leading=14)

h1 = style("H1",
    fontName="Helvetica-Bold", fontSize=18, textColor=BLACK,
    leading=24, spaceBefore=16, spaceAfter=6)

h2 = style("H2",
    fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT,
    leading=18, spaceBefore=12, spaceAfter=4)

h3 = style("H3",
    fontName="Helvetica-Bold", fontSize=11, textColor=BLACK,
    leading=15, spaceBefore=8, spaceAfter=3)

body = style("Body",
    fontName="Helvetica", fontSize=10, textColor=BLACK,
    leading=16, spaceAfter=6)

body_grey = style("BodyGrey",
    fontName="Helvetica", fontSize=9.5, textColor=GREY,
    leading=15, spaceAfter=4)

bullet = style("Bullet",
    fontName="Helvetica", fontSize=10, textColor=BLACK,
    leading=16, spaceAfter=4, leftIndent=14, firstLineIndent=-14)

bullet_sub = style("BulletSub",
    fontName="Helvetica", fontSize=9.5, textColor=GREY,
    leading=15, spaceAfter=3, leftIndent=28, firstLineIndent=-14)

code = style("Code",
    fontName="Courier", fontSize=9, textColor=colors.HexColor("#2D2D2D"),
    leading=14, spaceAfter=2, leftIndent=8)

note_style = style("Note",
    fontName="Helvetica-Oblique", fontSize=9.5, textColor=colors.HexColor("#555555"),
    leading=14, spaceAfter=4)

warn_style = style("Warn",
    fontName="Helvetica-Bold", fontSize=9.5, textColor=AMBER,
    leading=14, spaceAfter=4)

label_style = style("Label",
    fontName="Helvetica-Bold", fontSize=9, textColor=WHITE,
    leading=12)

toc_item = style("TOCItem",
    fontName="Helvetica", fontSize=10.5, textColor=BLACK,
    leading=18, leftIndent=20)

toc_num = style("TOCNum",
    fontName="Helvetica-Bold", fontSize=10.5, textColor=ACCENT,
    leading=18)

page_label = style("PageLabel",
    fontName="Helvetica-Bold", fontSize=8, textColor=GREY,
    leading=10)

def rule(color=BORDER, thickness=0.5):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=6, spaceBefore=6)

def step_header(number, title):
    data = [[
        Paragraph(str(number), style("SN", fontName="Helvetica-Bold", fontSize=16,
                                      textColor=WHITE, leading=20)),
        Paragraph(title, style("ST", fontName="Helvetica-Bold", fontSize=13,
                                textColor=WHITE, leading=18))
    ]]
    t = Table(data, colWidths=[32, W - 2*MARGIN - 40])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), STEP_BG),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING",(0,0), (0,0), 10),
        ("RIGHTPADDING",(0,0),(-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING",(0,0),(-1,-1), 10),
        ("ROUNDEDCORNERS", [4,4,4,4]),
    ]))
    return t

def info_box(text, bg=LIGHT_BG, border=BORDER):
    data = [[Paragraph(text, body)]]
    t = Table(data, colWidths=[W - 2*MARGIN])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX",        (0,0), (-1,-1), 0.5, border),
        ("LEFTPADDING",(0,0), (-1,-1), 12),
        ("RIGHTPADDING",(0,0),(-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING",(0,0),(-1,-1), 8),
    ]))
    return t

def warning_box(text):
    data = [[Paragraph("<b>Important:</b> " + text, body_grey)]]
    t = Table(data, colWidths=[W - 2*MARGIN])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#FFFBEA")),
        ("BOX",        (0,0), (-1,-1), 0.5, colors.HexColor("#F59E0B")),
        ("LEFTPADDING",(0,0), (-1,-1), 12),
        ("RIGHTPADDING",(0,0),(-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING",(0,0),(-1,-1), 8),
    ]))
    return t

def action_box(text):
    data = [[Paragraph("<b>Action:</b> " + text, body)]]
    t = Table(data, colWidths=[W - 2*MARGIN])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#EDFBF3")),
        ("BOX",        (0,0), (-1,-1), 0.5, colors.HexColor("#2D9E6B")),
        ("LEFTPADDING",(0,0), (-1,-1), 12),
        ("RIGHTPADDING",(0,0),(-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING",(0,0),(-1,-1), 8),
    ]))
    return t

def b(text):
    return f"<b>{text}</b>"

def make_table(headers, rows, col_widths=None):
    data = [headers] + rows
    if not col_widths:
        col_widths = [(W - 2*MARGIN) / len(headers)] * len(headers)
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,0),  STEP_BG),
        ("TEXTCOLOR",    (0,0), (-1,0),  WHITE),
        ("FONTNAME",     (0,0), (-1,0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,0),  9),
        ("FONTNAME",     (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",     (0,1), (-1,-1), 9),
        ("TEXTCOLOR",    (0,1), (-1,-1), BLACK),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, LIGHT_GREY]),
        ("GRID",         (0,0), (-1,-1), 0.3, BORDER),
        ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING",  (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING",   (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0), (-1,-1), 6),
    ]))
    return t

# -----------------------------------------------------------------------
# BUILD STORY
# -----------------------------------------------------------------------
story = []

# -----------------------------------------------------------------------
# COVER PAGE
# -----------------------------------------------------------------------
cover_data = [[
    Paragraph("CLICK AI AGENCY", style("CA", fontName="Helvetica-Bold", fontSize=9,
              textColor=ACCENT, leading=12)),
]]
cover_top = Table(cover_data, colWidths=[W - 2*MARGIN])
cover_top.setStyle(TableStyle([
    ("LEFTPADDING",(0,0),(-1,-1),0),
    ("BOTTOMPADDING",(0,0),(-1,-1),0),
    ("TOPPADDING",(0,0),(-1,-1),0),
]))
story.append(Spacer(1, 20*mm))
story.append(cover_top)
story.append(Spacer(1, 8*mm))

cover_block = [[
    Paragraph("Email Outreach\nSetup Guide", cover_title),
]]
ct = Table(cover_block, colWidths=[W - 2*MARGIN])
ct.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1), STEP_BG),
    ("LEFTPADDING",(0,0),(-1,-1),20),
    ("RIGHTPADDING",(0,0),(-1,-1),20),
    ("TOPPADDING",(0,0),(-1,-1),24),
    ("BOTTOMPADDING",(0,0),(-1,-1),24),
    ("ROUNDEDCORNERS",[6,6,6,6]),
]))
story.append(ct)
story.append(Spacer(1, 6*mm))

story.append(Paragraph("A step-by-step guide to registering your outreach domain, setting up email accounts, configuring Instantly.ai, enriching leads, and launching your first cold email campaign.", body))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("Prepared by Jodie | April 2026 | Click AI Agency", body_grey))
story.append(Spacer(1, 8*mm))
story.append(rule(ACCENT, 1))
story.append(Spacer(1, 4*mm))

# Summary stats
summary_data = [
    [Paragraph(b("Target volume"), body), Paragraph("300 to 500 emails/week", body)],
    [Paragraph(b("Monthly cost"), body), Paragraph("approx. PS40-50/month once live", body)],
    [Paragraph(b("Time to full volume"), body), Paragraph("4 to 5 weeks (warmup required)", body)],
    [Paragraph(b("Tools used"), body), Paragraph("Namecheap, Google Workspace, Instantly.ai, Apify, ZeroBounce", body)],
]
st = Table(summary_data, colWidths=[55*mm, W - 2*MARGIN - 55*mm])
st.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (0,-1), LIGHT_BG),
    ("BACKGROUND", (1,0), (1,-1), WHITE),
    ("BOX", (0,0), (-1,-1), 0.5, BORDER),
    ("INNERGRID", (0,0), (-1,-1), 0.3, BORDER),
    ("LEFTPADDING",(0,0),(-1,-1),10),
    ("RIGHTPADDING",(0,0),(-1,-1),10),
    ("TOPPADDING",(0,0),(-1,-1),7),
    ("BOTTOMPADDING",(0,0),(-1,-1),7),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
]))
story.append(st)
story.append(Spacer(1, 8*mm))

# TOC
story.append(Paragraph("Contents", h1))
story.append(rule())
toc = [
    ("1", "Register your outreach domain"),
    ("2", "Create email accounts on that domain"),
    ("3", "Set up your Instantly.ai account"),
    ("4", "Connect your email accounts to Instantly.ai"),
    ("5", "Configure warmup settings"),
    ("6", "Set up lead enrichment with Apify"),
    ("7", "Verify emails with ZeroBounce"),
    ("8", "Build your email templates"),
    ("9", "Follow the warmup timeline"),
    ("10", "Launch your first campaign"),
    ("", "Full checklist"),
]
for num, title in toc:
    if num:
        row_data = [[
            Paragraph(num, toc_num),
            Paragraph(title, toc_item)
        ]]
    else:
        row_data = [[
            Paragraph("", toc_num),
            Paragraph(title, style("TOCBold", fontName="Helvetica-Bold", fontSize=10.5,
                                   textColor=BLACK, leading=18, leftIndent=20))
        ]]
    rt = Table(row_data, colWidths=[20, W - 2*MARGIN - 20])
    rt.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("TOPPADDING",(0,0),(-1,-1),2),
        ("BOTTOMPADDING",(0,0),(-1,-1),2),
        ("LEFTPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(rt)

story.append(PageBreak())

# -----------------------------------------------------------------------
# STEP 1: DOMAIN
# -----------------------------------------------------------------------
story.append(step_header("1", "Register your outreach domain"))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("Your outreach domain must be completely separate from clickaiagency.com. If your sending domain gets flagged as spam, you do not want that to touch your main domain or your main email reputation.", body))
story.append(Spacer(1, 3*mm))
story.append(warning_box("Never send cold email from hello@clickaiagency.com or any address on your main domain. Use a dedicated outreach domain only."))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Recommended domain options"), h3))
story.append(Paragraph("Choose one that is available and feels professional. Avoid anything with 'AI' in the name since spam filters are increasingly trained on it.", body))
story.append(Spacer(1, 2*mm))

domain_data = [
    [Paragraph(b("Domain"), body), Paragraph(b("Notes"), body)],
    [Paragraph("teamclick.co", body), Paragraph("Clean, professional, short", body)],
    [Paragraph("clickhq.co", body), Paragraph("Agency feel, easy to remember", body)],
    [Paragraph("clickgrowth.co", body), Paragraph("Benefit-led, clear purpose", body)],
    [Paragraph("getclick.co", body), Paragraph("Action-oriented, short", body)],
    [Paragraph("tryclickai.com", body), Paragraph("If .co not available, .com fallback", body)],
]
story.append(make_table(
    [Paragraph(b("Domain"), label_style), Paragraph(b("Notes"), label_style)],
    [[Paragraph(r[0].text, body), Paragraph(r[1].text, body)] for r in domain_data[1:]],
    col_widths=[65*mm, W - 2*MARGIN - 65*mm]
))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Where to register"), h3))
story.append(Paragraph("Use Namecheap (namecheap.com). It is the cheapest reliable registrar.", body))
story.append(Spacer(1, 2*mm))
steps_domain = [
    "Go to namecheap.com",
    "Search for your chosen domain name",
    "Add to cart. Do not add any extras (privacy protection is included free on .com/.co)",
    "Checkout. Cost: approx. PS8 to PS12 per year",
    "Once registered, log in to your Namecheap dashboard and keep it open. You will need it in Step 2.",
]
for i, s in enumerate(steps_domain, 1):
    story.append(Paragraph(f"{i}.  {s}", bullet))
story.append(Spacer(1, 3*mm))
story.append(action_box("Register your domain before moving to Step 2. Everything else depends on it."))

story.append(Spacer(1, 6*mm))

# -----------------------------------------------------------------------
# STEP 2: GOOGLE WORKSPACE
# -----------------------------------------------------------------------
story.append(step_header("2", "Create email accounts on your outreach domain"))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("You need 2 email addresses on your outreach domain. One is your primary sender, the second is a backup. Spreading sends across 2 accounts protects deliverability.", body))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Use Google Workspace"), h3))
story.append(Paragraph("Google Workspace gives you professional Gmail accounts on your own domain. The Starter plan is PS5 per user per month.", body))
story.append(Spacer(1, 2*mm))

steps_gw = [
    ("Go to workspace.google.com and click Get Started", ""),
    ("Enter your business name (Click AI Agency) and select the number of employees: Just you", ""),
    ("When asked for your domain, choose 'Use a domain I already have' and enter your new outreach domain", ""),
    ("Complete checkout. Cost: PS5 per user per month. You need 2 users = PS10/month", ""),
    ("Google will give you DNS records to add to your domain. Go back to Namecheap.", ""),
    ("In Namecheap, go to your domain, click Manage, then Advanced DNS", ""),
    ("Add the MX records Google provides. These connect your domain to Google's email servers.", ""),
    ("Also add the SPF record Google gives you. This is a TXT record. It tells receiving servers that Google is authorised to send from your domain.", ""),
    ("Add the DKIM record. Google provides this too. It is another TXT record. It cryptographically signs your emails.", ""),
    ("Wait 10 to 30 minutes for DNS to propagate, then verify in the Google Workspace setup wizard", ""),
]
for i, (s, _) in enumerate(steps_gw, 1):
    story.append(Paragraph(f"{i}.  {s}", bullet))

story.append(Spacer(1, 3*mm))
story.append(info_box("SPF, DKIM, and DMARC are the three technical signals that tell receiving email servers your emails are legitimate. Skipping these will destroy your deliverability before you send a single email. Do not skip them."))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("DMARC record (add this last)"), h3))
story.append(Paragraph("After SPF and DKIM are set, add a DMARC record. In Namecheap Advanced DNS, add a new TXT record:", body))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("Host:  _dmarc", code))
story.append(Paragraph("Value: v=DMARC1; p=none; rua=mailto:admin@yourdomain.co", code))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("Replace yourdomain.co with your actual domain. The p=none means it monitors without blocking. This is correct for a new domain.", body_grey))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Email addresses to create"), h3))
email_data = [
    [Paragraph(b("Account"), label_style), Paragraph(b("Name"), label_style), Paragraph(b("Purpose"), label_style)],
    [Paragraph("hadi@yourdomain.co", body), Paragraph("Hadi Yazdani", body), Paragraph("Primary sender", body)],
    [Paragraph("team@yourdomain.co", body), Paragraph("Click AI Team", body), Paragraph("Backup sender / volume split", body)],
]
story.append(make_table(
    email_data[0],
    [email_data[1], email_data[2]],
    col_widths=[65*mm, 45*mm, W - 2*MARGIN - 110*mm]
))
story.append(Spacer(1, 3*mm))
story.append(action_box("Confirm all three DNS records (SPF, DKIM, DMARC) are added before moving to Step 3. Use mail-tester.com to verify: send a test email and check the score. You want 8/10 or higher."))

story.append(PageBreak())

# -----------------------------------------------------------------------
# STEP 3: INSTANTLY.AI SETUP
# -----------------------------------------------------------------------
story.append(step_header("3", "Set up your Instantly.ai account"))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("Instantly.ai handles two things: warming up your email accounts (automated, runs in the background) and sending your cold email campaigns. One tool, one subscription.", body))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Plans"), h3))
plan_data = [
    [Paragraph(b("Plan"), label_style), Paragraph(b("Price"), label_style), Paragraph(b("Sending limit"), label_style), Paragraph(b("Right for you?"), label_style)],
    [Paragraph("Growth", body), Paragraph("$37/month", body), Paragraph("5,000/month", body), Paragraph("Yes. Start here.", body)],
    [Paragraph("Hypergrowth", body), Paragraph("$97/month", body), Paragraph("100,000/month", body), Paragraph("When you exceed 5,000/month", body)],
]
story.append(make_table(plan_data[0], [plan_data[1], plan_data[2]], col_widths=[35*mm, 35*mm, 45*mm, W - 2*MARGIN - 115*mm]))
story.append(Spacer(1, 3*mm))
story.append(Paragraph("5,000 emails/month = 1,250/week. Your target is 300 to 500/week. The Growth plan covers you with headroom to grow.", body))
story.append(Spacer(1, 3*mm))

steps_inst = [
    "Go to instantly.ai and click Get Started",
    "Choose the Growth plan at $37/month",
    "Complete signup with your personal email (not the outreach domain email)",
    "You are now in the Instantly dashboard. Leave it open for Step 4.",
]
for i, s in enumerate(steps_inst, 1):
    story.append(Paragraph(f"{i}.  {s}", bullet))

story.append(Spacer(1, 6*mm))

# -----------------------------------------------------------------------
# STEP 4: CONNECT EMAIL ACCOUNTS
# -----------------------------------------------------------------------
story.append(step_header("4", "Connect your email accounts to Instantly.ai"))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("You are connecting both Google Workspace accounts (the two you created in Step 2) to Instantly.ai.", body))
story.append(Spacer(1, 3*mm))

steps_connect = [
    "In Instantly.ai, go to Email Accounts in the left sidebar",
    "Click Add Account",
    "Select Google / Gmail",
    "Click Connect with Google and authorise with your first outreach email (hadi@yourdomain.co)",
    "Repeat for your second account (team@yourdomain.co)",
    "Both accounts should now appear in your Email Accounts list with a green status",
]
for i, s in enumerate(steps_connect, 1):
    story.append(Paragraph(f"{i}.  {s}", bullet))

story.append(Spacer(1, 3*mm))
story.append(warning_box("If either account shows as disconnected or red after connecting, go back and re-authorise. A disconnected account will not warm up and will not send. Check this daily for the first week."))
story.append(Spacer(1, 6*mm))

# -----------------------------------------------------------------------
# STEP 5: WARMUP SETTINGS
# -----------------------------------------------------------------------
story.append(step_header("5", "Configure warmup settings"))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("Warmup gradually increases your sending volume so receiving email servers build trust in your domain. Skipping or rushing this is the single biggest reason new outreach domains get flagged as spam.", body))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Settings to apply to BOTH email accounts"), h3))
warmup_data = [
    [Paragraph(b("Setting"), label_style), Paragraph(b("Value"), label_style), Paragraph(b("Why"), label_style)],
    [Paragraph("Warmup enabled", body), Paragraph("Yes (toggle on)", body), Paragraph("Starts the reputation-building process", body)],
    [Paragraph("Daily warmup limit", body), Paragraph("Start at 5, increase by 2 per day", body), Paragraph("Gradual increase mimics human sending", body)],
    [Paragraph("Reply rate", body), Paragraph("30 to 40%", body), Paragraph("High reply rate signals engagement to Gmail", body)],
    [Paragraph("Mark as important", body), Paragraph("Yes", body), Paragraph("Trains inbox placement", body)],
    [Paragraph("Warmup tag", body), Paragraph("Leave default", body), Paragraph("Keeps warmup emails out of your sent view", body)],
]
story.append(make_table(
    warmup_data[0],
    warmup_data[1:],
    col_widths=[50*mm, 55*mm, W - 2*MARGIN - 105*mm]
))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Enable warmup now. Do not touch it after enabling."), h3))
story.append(Paragraph("Instantly.ai handles the warmup automatically. It sends small volumes of emails between accounts in its warmup network, and those accounts reply to each other. This builds your sender reputation. Your job is to leave it running.", body))
story.append(Spacer(1, 3*mm))
story.append(action_box("Enable warmup on both accounts today. Do not send any cold campaigns until Week 4. The warmup runs for 3 to 4 weeks before you have enough reputation to send volume safely."))

story.append(PageBreak())

# -----------------------------------------------------------------------
# STEP 6: LEAD ENRICHMENT
# -----------------------------------------------------------------------
story.append(step_header("6", "Set up lead enrichment with Apify"))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("You already have an Apify account from Workflow 1. You are going to add a second scraper: Google Maps Scraper. This pulls business name, address, website, and often the contact email directly from Google Maps listings.", body))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Why Apify over Apollo for your targets"), h3))
story.append(Paragraph("Apollo is built for mid-size B2B companies with clear corporate structure. Your targets are small local UK businesses: restaurants, dental practices, aesthetics clinics. Many of these are not in Apollo's database, or the contact data is wrong. Google Maps has accurate, real-time data for every local business with a Google listing.", body))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Setting up Google Maps Scraper in Apify"), h3))
steps_apify = [
    "Log in to apify.com",
    "Go to Store (left sidebar)",
    "Search for 'Google Maps Scraper'",
    "Click on it and click Try for free",
    "In the input settings, configure a test run:",
    [
        "Search terms: 'restaurants london', 'dental practices london', 'aesthetics clinics london'",
        "Max results: 50 (for testing)",
        "Language: en",
        "Country: GB",
    ],
    "Click Save and Run",
    "Wait for it to complete (usually 2 to 5 minutes for 50 results)",
    "Click Results and export as JSON or CSV",
    "Check the output: look for a 'email' column. Not every listing has an email, but many do.",
]
for item in steps_apify:
    if isinstance(item, list):
        for sub in item:
            story.append(Paragraph(f"      -  {sub}", bullet_sub))
    else:
        story.append(Paragraph(f"{steps_apify.index(item) + 1 if not isinstance(item, list) else ''}.  {item}", bullet))

story.append(Spacer(1, 3*mm))
story.append(Paragraph(b("Handling leads without a public email"), h3))
story.append(Paragraph("For businesses where Google Maps does not have a public email, go to their website and check the Contact page. Most small businesses list an email there. Hunter.io (free tier: 25 searches/month) can also find emails from a company domain if the website does not list one directly.", body))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Hunter.io setup"), h3))
steps_hunter = [
    "Go to hunter.io",
    "Create a free account",
    "Use Domain Search: enter the business domain (e.g. crockersbistro.co.uk)",
    "Hunter returns any email addresses found for that domain",
    "Free tier gives 25 searches/month. Upgrade to Starter ($49/month, 500 searches) when needed.",
]
for i, s in enumerate(steps_hunter, 1):
    story.append(Paragraph(f"{i}.  {s}", bullet))

story.append(Spacer(1, 6*mm))

# -----------------------------------------------------------------------
# STEP 7: ZEROB OUNCE
# -----------------------------------------------------------------------
story.append(step_header("7", "Verify emails with ZeroBounce"))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("Every email address must be verified before you send to it. Sending to invalid addresses increases your bounce rate. A bounce rate above 3% will get your sending domain flagged and eventually blacklisted.", body))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Why this step is non-negotiable"), h3))
story.append(Paragraph("Google Maps and Hunter.io data is not always current. Businesses close, staff change, email addresses get retired. Verifying before sending protects your sender reputation. At your volume (300 to 500/week), even 10 bad addresses per week adds up fast.", body))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("ZeroBounce setup"), h3))
steps_zb = [
    "Go to zerobounce.net",
    "Create a free account (100 verifications free per month)",
    "To verify a list: go to Email Validation, upload a CSV with your email addresses",
    "ZeroBounce returns a result for each address: Valid, Invalid, Catch-all, Unknown",
    "Only send to Valid results. Remove Invalid immediately. Catch-all means the domain accepts all emails regardless of whether the address exists (treat with caution).",
    "Cost once you exceed 100/month: $8 per 1,000 verifications (pay as you go, no subscription needed)",
]
for i, s in enumerate(steps_zb, 1):
    story.append(Paragraph(f"{i}.  {s}", bullet))

story.append(Spacer(1, 3*mm))
story.append(info_box("Run every batch of leads through ZeroBounce before importing to Instantly.ai. Build this into your weekly workflow: scrape on Monday, verify on Monday, import to Instantly on Tuesday, send Wednesday onwards."))

story.append(PageBreak())

# -----------------------------------------------------------------------
# STEP 8: EMAIL TEMPLATES
# -----------------------------------------------------------------------
story.append(step_header("8", "Build your email templates in Instantly.ai"))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("These are the approved templates for Click AI Agency. Copy them exactly into Instantly.ai. Personalisation variables are shown in double brackets.", body))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Subject line formula"), h3))
story.append(info_box("Formula: [Business name] + [specific pain] + question? Keep under 50 characters. End with a question mark. Never use the words 'free', 'grow', 'scale', 'AI-powered', or 'revolutionary'."))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Template 1: Restaurants and Cafes"), h2))
story.append(Paragraph(b("Subject:"), body))
story.append(Paragraph("{{business_name}} + guest follow-up?", code))
story.append(Spacer(1, 2*mm))
story.append(Paragraph(b("Body:"), body))
body_r = [
    "Hi {{first_name}},",
    "",
    "We help restaurants automatically follow up with guests after their visit, so reviews come in and tables get rebooked without anyone chasing them manually.",
    "",
    "For a place like {{business_name}}, this runs in the background. No new software to learn.",
    "",
    "Can I send you a 2-minute screen recording of how it works?",
    "",
    "Hadi",
    "Click AI Agency",
]
for line in body_r:
    story.append(Paragraph(line if line else "&nbsp;", code))
story.append(Spacer(1, 4*mm))

story.append(Paragraph(b("Template 2: Aesthetics Clinics"), h2))
story.append(Paragraph(b("Subject:"), body))
story.append(Paragraph("{{business_name}} + rebooking follow-up?", code))
story.append(Spacer(1, 2*mm))
story.append(Paragraph(b("Body:"), body))
body_a = [
    "Hi {{first_name}},",
    "",
    "We help aesthetics clinics automatically follow up with clients after their treatment, so rebooking happens without the manual chasing and revenue does not slip through.",
    "",
    "For a clinic like {{business_name}}, it connects to whatever booking system you already use.",
    "",
    "Can I send you a 2-minute screen recording of how it works?",
    "",
    "Hadi",
    "Click AI Agency",
]
for line in body_a:
    story.append(Paragraph(line if line else "&nbsp;", code))
story.append(Spacer(1, 4*mm))

story.append(Paragraph(b("Template 3: Dental Practices"), h2))
story.append(Paragraph(b("Subject:"), body))
story.append(Paragraph("{{business_name}} + appointment reminders?", code))
story.append(Spacer(1, 2*mm))
story.append(Paragraph(b("Body:"), body))
body_d = [
    "Hi {{first_name}},",
    "",
    "We help dental practices automatically remind patients before their appointments, so no-shows stop happening and the day stays full.",
    "",
    "For a practice like {{business_name}}, it runs alongside your existing booking system.",
    "",
    "Can I send you a 2-minute screen recording of how it works?",
    "",
    "Hadi",
    "Click AI Agency",
]
for line in body_d:
    story.append(Paragraph(line if line else "&nbsp;", code))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Setting up templates in Instantly.ai"), h3))
steps_tmpl = [
    "In Instantly.ai, go to Campaigns in the left sidebar",
    "Click Create Campaign",
    "Name it by industry and date: e.g. 'Restaurants London April 2026'",
    "In the Email Sequence section, paste your subject line and body",
    "Add personalisation variables using Instantly's variable picker (matches the {{variable}} format)",
    "Set the From name to: Hadi | Click AI Agency",
    "Do not add any attachments, images, or HTML formatting. Plain text only. It gets better deliverability.",
    "Save as a draft. Do not activate until you are in Week 4 of warmup.",
]
for i, s in enumerate(steps_tmpl, 1):
    story.append(Paragraph(f"{i}.  {s}", bullet))

story.append(PageBreak())

# -----------------------------------------------------------------------
# STEP 9: WARMUP TIMELINE
# -----------------------------------------------------------------------
story.append(step_header("9", "Follow the warmup timeline"))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("Warmup takes 3 to 4 weeks. This is not optional. Sending volume before your domain has enough reputation means your emails land in spam and the domain gets flagged. Run the warmup properly once and you will not have to do it again.", body))
story.append(Spacer(1, 3*mm))

timeline_data = [
    [Paragraph(b("Week"), label_style), Paragraph(b("Warmup sends/day"), label_style), Paragraph(b("Cold campaign sends/day"), label_style), Paragraph(b("What to do"), label_style)],
    [Paragraph("Week 1", body), Paragraph("5 to 10 (auto)", body), Paragraph("0", body), Paragraph("Enable warmup. Build your lead list. Verify with ZeroBounce.", body)],
    [Paragraph("Week 2", body), Paragraph("15 to 30 (auto)", body), Paragraph("0", body), Paragraph("Continue building leads. Finalise templates. Check accounts stay connected.", body)],
    [Paragraph("Week 3", body), Paragraph("30 to 50 (auto)", body), Paragraph("0", body), Paragraph("Last preparation week. Import verified leads to Instantly. Set up campaign sequences.", body)],
    [Paragraph("Week 4", body), Paragraph("50+ (auto)", body), Paragraph("20 to 30/day", body), Paragraph("Soft launch. Send to 20 to 30/day. Monitor open rates and replies.", body)],
    [Paragraph("Week 5+", body), Paragraph("50+ (auto)", body), Paragraph("70 to 100/day", body), Paragraph("Scale to full volume (300 to 500/week). Keep warmup running permanently.", body)],
]
story.append(make_table(
    timeline_data[0],
    timeline_data[1:],
    col_widths=[20*mm, 38*mm, 42*mm, W - 2*MARGIN - 100*mm]
))
story.append(Spacer(1, 3*mm))

story.append(warning_box("Keep warmup running permanently, even after you are at full volume. Warmup does not stop at Week 4. It runs indefinitely in the background and maintains your sender reputation."))
story.append(Spacer(1, 3*mm))

story.append(Paragraph(b("Benchmarks to watch"), h3))
bench_data = [
    [Paragraph(b("Metric"), label_style), Paragraph(b("Good"), label_style), Paragraph(b("Investigate if below"), label_style)],
    [Paragraph("Open rate", body), Paragraph("20 to 35%", body), Paragraph("Below 15%", body)],
    [Paragraph("Reply rate", body), Paragraph("3 to 8%", body), Paragraph("Below 2%", body)],
    [Paragraph("Bounce rate", body), Paragraph("Below 2%", body), Paragraph("Above 3%: pause and investigate", body)],
    [Paragraph("Spam complaint rate", body), Paragraph("Below 0.1%", body), Paragraph("Above 0.3%: pause immediately", body)],
]
story.append(make_table(
    bench_data[0],
    bench_data[1:],
    col_widths=[45*mm, 35*mm, W - 2*MARGIN - 80*mm]
))
story.append(Spacer(1, 6*mm))

# -----------------------------------------------------------------------
# STEP 10: LAUNCH
# -----------------------------------------------------------------------
story.append(step_header("10", "Launch your first campaign"))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("You are in Week 4. Warmup has been running for 3 weeks. Leads are verified. Templates are built. Here is how to launch.", body))
story.append(Spacer(1, 3*mm))

steps_launch = [
    "In Instantly.ai, go to your campaign draft (e.g. 'Restaurants London April 2026')",
    "In Campaign Settings, set sending schedule: Monday to Friday, 9am to 5pm (recipient's timezone)",
    "Set daily limit per account: 25 emails to start. Increase to 50 after one week with no issues.",
    "Set delay between emails: 3 to 5 minutes minimum. This mimics human sending.",
    "Assign both email accounts to the campaign (Instantly distributes sends between them automatically)",
    "Click Activate Campaign",
    "Check results every day for the first week: open rate, reply rate, bounce rate",
    "When a lead replies, move them to a Replied status in Instantly and handle the conversation manually",
    "Do not automate replies. All responses from leads are handled by Zizi or Hadi directly.",
]
for i, s in enumerate(steps_launch, 1):
    story.append(Paragraph(f"{i}.  {s}", bullet))

story.append(Spacer(1, 3*mm))
story.append(Paragraph(b("What to do when a lead replies"), h3))
reply_data = [
    [Paragraph(b("Their reply"), label_style), Paragraph(b("Who handles it"), label_style), Paragraph(b("What to do"), label_style)],
    [Paragraph("Positive: interested, asks a question", body), Paragraph("Zizi", body), Paragraph("Send Step 2 email version. Offer screen recording.", body)],
    [Paragraph("Neutral: who are you, tell me more", body), Paragraph("Zizi", body), Paragraph("Send Step 2 email version.", body)],
    [Paragraph("Yes to demo", body), Paragraph("Hadi", body), Paragraph("Zizi flags to Hadi immediately. Hadi takes over.", body)],
    [Paragraph("Unsubscribe or not interested", body), Paragraph("Zizi", body), Paragraph("Reply: 'No problem, removed.' Mark as unsubscribed in Instantly.", body)],
    [Paragraph("Out of office", body), Paragraph("Zizi", body), Paragraph("Note the date. Follow up after they return.", body)],
]
story.append(make_table(
    reply_data[0],
    reply_data[1:],
    col_widths=[55*mm, 30*mm, W - 2*MARGIN - 85*mm]
))

story.append(PageBreak())

# -----------------------------------------------------------------------
# FULL CHECKLIST
# -----------------------------------------------------------------------
story.append(Paragraph("Full Setup Checklist", h1))
story.append(rule(ACCENT, 1))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("Work through this in order. Do not skip steps. Each depends on the one before it.", body))
story.append(Spacer(1, 4*mm))

checklist = [
    ("Domain", [
        "Chosen and registered outreach domain (not clickaiagency.com)",
        "Domain appears in Namecheap dashboard",
    ]),
    ("Google Workspace", [
        "Google Workspace Starter plan active",
        "Two email accounts created on outreach domain",
        "MX records added to Namecheap DNS",
        "SPF record (TXT) added",
        "DKIM record (TXT) added",
        "DMARC record (TXT) added",
        "mail-tester.com score is 8/10 or higher",
    ]),
    ("Instantly.ai", [
        "Account created on Growth plan ($37/month)",
        "Both email accounts connected and showing green",
        "Warmup enabled on both accounts",
        "Warmup reply rate set to 30 to 40%",
        "Mark as important toggled on",
    ]),
    ("Lead Enrichment", [
        "Google Maps Scraper test run completed in Apify",
        "Output reviewed and email column present",
        "Hunter.io free account created",
        "ZeroBounce free account created",
        "First batch of leads exported and verified",
    ]),
    ("Templates", [
        "Restaurant template created in Instantly.ai (draft)",
        "Aesthetics template created in Instantly.ai (draft)",
        "Dental template created in Instantly.ai (draft)",
        "All templates reviewed: no em dashes, no forbidden words, ends with question",
    ]),
    ("Warmup (Week 4 gate)", [
        "Warmup has been running for 3 full weeks",
        "Both accounts still connected and green in Instantly",
        "Bounce rate on warmup emails is below 2%",
        "Lead list for first campaign is verified in ZeroBounce",
    ]),
    ("Launch", [
        "Campaign activated at 20 to 30/day",
        "Sending schedule set to Mon to Fri 9am to 5pm",
        "Delay between emails set to 3 to 5 minutes",
        "Open rate and reply rate being monitored daily",
        "Zizi briefed on email reply protocol",
    ]),
]

for section, items in checklist:
    section_data = [[Paragraph(section, style("SL", fontName="Helvetica-Bold", fontSize=10,
                                               textColor=WHITE, leading=14))]]
    st_table = Table(section_data, colWidths=[W - 2*MARGIN])
    st_table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), ACCENT),
        ("LEFTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),6),
        ("BOTTOMPADDING",(0,0),(-1,-1),6),
    ]))
    story.append(st_table)
    for item in items:
        story.append(Paragraph(f"[ ]   {item}", bullet))
    story.append(Spacer(1, 3*mm))

story.append(Spacer(1, 4*mm))
story.append(rule(ACCENT, 1))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("Questions or issues during setup? Message Hadi.", body_grey))
story.append(Paragraph("This guide was prepared by Jodie for Click AI Agency. April 2026.", body_grey))

# -----------------------------------------------------------------------
# BUILD
# -----------------------------------------------------------------------
doc.build(story)
print("PDF generated successfully.")
