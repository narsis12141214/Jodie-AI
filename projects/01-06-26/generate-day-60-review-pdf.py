from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
)

OUTPUT = "/Users/hadi/Developer/Jodie-AI/projects/01-06-26/day-60-review.pdf"

BLACK = colors.HexColor("#0D0D0D")
WHITE = colors.HexColor("#FFFFFF")
ACCENT = colors.HexColor("#6C63FF")
GREEN = colors.HexColor("#2A7F4F")
RED = colors.HexColor("#A8324A")
GREY = colors.HexColor("#666666")
LIGHT_GREY = colors.HexColor("#F5F5F5")
BORDER = colors.HexColor("#DDDDDD")

W, H = A4
MARGIN = 18 * mm

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=MARGIN, bottomMargin=MARGIN,
    title="Day 60 Review — Hadi Yazdani — 60-day window 1 Apr to 30 May 2026",
    author="Hadi Yazdani"
)

def s(name, **kw):
    return ParagraphStyle(name, **kw)

title_style = s("Title", fontName="Helvetica-Bold", fontSize=22, textColor=BLACK, leading=28, spaceAfter=4)
subtitle_style = s("Subtitle", fontName="Helvetica", fontSize=10, textColor=GREY, leading=14, spaceAfter=14)
h1 = s("H1", fontName="Helvetica-Bold", fontSize=15, textColor=BLACK, leading=20, spaceBefore=14, spaceAfter=6)
h2 = s("H2", fontName="Helvetica-Bold", fontSize=11.5, textColor=BLACK, leading=16, spaceBefore=10, spaceAfter=4)
body = s("Body", fontName="Helvetica", fontSize=9.5, textColor=BLACK, leading=14, spaceAfter=4)
body_bold = s("BodyBold", fontName="Helvetica-Bold", fontSize=9.5, textColor=BLACK, leading=14, spaceAfter=4)
body_bold_white = s("BodyBoldWhite", fontName="Helvetica-Bold", fontSize=9.5, textColor=WHITE, leading=14, spaceAfter=4)
body_small = s("BodySmall", fontName="Helvetica", fontSize=8.5, textColor=GREY, leading=12, spaceAfter=3)
quote_style = s("Quote", fontName="Helvetica-Bold", fontSize=12, textColor=BLACK, leading=18, spaceBefore=8, spaceAfter=8, leftIndent=8, rightIndent=8)
verdict_style = s("Verdict", fontName="Helvetica-BoldOblique", fontSize=13, textColor=BLACK, leading=18, spaceBefore=10, spaceAfter=4, leftIndent=8, rightIndent=8)

def rule():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=6, spaceBefore=6)

def bullet(text):
    return Paragraph("  •  " + text, body)

story = []

# ─── HEADER ─────────────────────────────────────────────
story.append(Paragraph("DAY 60 REVIEW", title_style))
story.append(Paragraph("60-day window: 1 April to 30 May 2026 | Owner: Hadi Yazdani | Date: 1 June 2026", subtitle_style))
story.append(rule())

# ─── HEADLINE ───────────────────────────────────────────
story.append(Paragraph("Headline assessment", h1))
story.append(Paragraph("<b>The numbers missed. The mechanism landed.</b>", quote_style))
story.append(Paragraph(
    "Revenue, follower, and ranking targets all under-hit. But the 60-day window produced something more valuable than the revenue would have: a working agency product with proof-of-concept, a sales framework with a validated performance anchor, and a positioning rebuild already underway for photography. The next 60 days inherit a workable system, not a blank page.",
    body
))

# ─── AGENCY TABLE ───────────────────────────────────────
story.append(Paragraph("Agency &mdash; Goals vs Actuals", h1))
agency_data = [
    [Paragraph("<b>Metric</b>", body_bold_white), Paragraph("<b>Day 60 Target</b>", body_bold_white), Paragraph("<b>Actual</b>", body_bold_white), Paragraph("<b>Delta</b>", body_bold_white)],
    [Paragraph("Clients closed", body), Paragraph("10", body), Paragraph("1 paid (Haleh) + 2 verbal (Kish LIVE, Heny pending)", body), Paragraph("-7 vs target", body)],
    [Paragraph("MRR at Day 60", body), Paragraph("&pound;5,000", body), Paragraph("~&pound;717 (Haleh discounted M1)", body), Paragraph("-86%", body)],
    [Paragraph("Outreach / day", body), Paragraph("100", body), Paragraph("~20-30 DMs + 424-queue cold email automation built", body), Paragraph("Behind, infra in place", body)],
    [Paragraph("@clickaiagency followers", body), Paragraph("3,000 floor / 10,000 stretch", body), Paragraph("Status unknown", body), Paragraph("Likely behind", body)],
    [Paragraph("LinkedIn followers", body), Paragraph("1,000", body), Paragraph("Partial; intermittent posts", body), Paragraph("Behind", body)],
    [Paragraph("YouTube subscribers", body), Paragraph("1,000", body), Paragraph("Channel not launched", body), Paragraph("Did not start", body)],
    [Paragraph("Inbound DMs / day from content", body), Paragraph("2-5 / day", body), Paragraph("Sporadic, no consistent inbound", body), Paragraph("Behind", body)],
]
t = Table(agency_data, colWidths=[45*mm, 30*mm, 60*mm, W - 2*MARGIN - 135*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), BLACK),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(t)
story.append(Spacer(1, 4*mm))

# ─── PHOTOGRAPHY TABLE ──────────────────────────────────
story.append(Paragraph("Photography &mdash; Goals vs Actuals", h1))
photo_data = [
    [Paragraph("<b>Metric</b>", body_bold_white), Paragraph("<b>Day 60 Target</b>", body_bold_white), Paragraph("<b>Actual</b>", body_bold_white), Paragraph("<b>Delta</b>", body_bold_white)],
    [Paragraph("Tier 1 keyword rankings", body), Paragraph("Top 3-5", body), Paragraph("Mixed: some Page 1 entries; homepage primary dropped 35 to 52", body), Paragraph("Mixed, deteriorating", body)],
    [Paragraph("london wedding photographer", body), Paragraph("Page 1 (top 10)", body), Paragraph("Position 52.2", body), Paragraph("Way off", body)],
    [Paragraph("Enquiries / month", body), Paragraph("50 / month pace", body), Paragraph("Mozhgan booked (repeat); broader inbound low", body), Paragraph("Way off", body)],
    [Paragraph("Bookings / month", body), Paragraph("5 minimum", body), Paragraph("1 (Mozhgan, repeat)", body), Paragraph("-4", body)],
    [Paragraph("Photography revenue", body), Paragraph("&pound;9,000 / month", body), Paragraph("Mozhgan cash on day, modest", body), Paragraph("Way off", body)],
    [Paragraph("@hadyyazdani followers", body), Paragraph("20,000 floor / 25,000 stretch", body), Paragraph("~13,500, no posts in ~2 weeks", body), Paragraph("Below floor", body)],
    [Paragraph("New blog posts", body), Paragraph("9 in 60 days", body), Paragraph("7 published, none since 7 May", body), Paragraph("Behind", body)],
]
t2 = Table(photo_data, colWidths=[45*mm, 30*mm, 60*mm, W - 2*MARGIN - 135*mm])
t2.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), BLACK),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(t2)
story.append(PageBreak())

# ─── WHAT WORKED ────────────────────────────────────────
story.append(Paragraph("What Worked", h1))
worked = [
    "<b>First paid client closed (Haleh, 11 May).</b> Agency model is now real, not theoretical.",
    "<b>Kish recovery deal LIVE + 10+ bookings captured in 2-3 days.</b> Most important signal of the entire window. Two of the 10+ are unambiguously recovered (outside business hours); the rest came in during operating hours. Kish runs AI-first routing (no human-attempt-first), so the inclusive recovery definition does not apply to this client &mdash; only the outside-hours subset counts as anchor-eligible. Strictly extrapolated, 2 outside-hours recoveries in 2-3 days projects to ~20 per month, comfortably above the 10-per-month anchor on the strict definition alone. The product works in production; the anchor is not yet &ldquo;hit&rdquo; by mechanism but is easily hit by extrapolation.",
    "<b>Heny aesthetic clinic verbally closed (21 May) + meeting Thursday this week.</b> Second segment opened beyond restaurants.",
    "<b>The strategic framework rebuild itself.</b> Cross-segment pricing rule, performance anchor mechanism, off-ramp logic, complete cold email rebuild (12 templates &times; 4 segments), Mon-Thu cadence, Click Voice tier extension to all service segments, contract signing protocol, three contract clause revisions, the Arman dev brief for Click Desk, Heny contract template, 5 Lovable landing pages live, and a complete photography brand rebuild framework using Maddie Mae methodology. <i>This framework is the asset that makes the next 60 days different.</i>",
    "<b>Photography SEO &mdash; corrected diagnosis.</b> N8N v2 pipeline fix revealed the real picture: 10 clicks, 2,489 impressions, 533 ranking keywords, 0.40% sitewide CTR. The problem is CTR, not rankings &mdash; a fixable problem.",
    "<b>Mozhgan booking.</b> Repeat client signal that the photography brand strength is still real; the lapse is in marketing, not in the work.",
]
for item in worked:
    story.append(bullet(item))

# ─── WHAT DID NOT WORK ──────────────────────────────────
story.append(Paragraph("What Did Not Work &mdash; and Why", h1))
not_worked = [
    "<b>Pipeline volume vs realistic close rate.</b> The 60-day target of 10 clients was always wrong math: even at 100% close rate, a pipeline of ~15 active conversations was always going to fall short.",
    "<b>Cold email automation took 6+ weeks to build.</b> Live by week 7, leaving 17 days. Infrastructure pays off in Window 2, not this one.",
    "<b>Verbal yes to signed contract leak.</b> Four deals stalled after verbal yes (Randeszvous, Maria, Kish initially, Ace). Root cause: time gap between verbal yes and signature. Sign-in-the-room protocol adopted 12 May but only Heny was reached during this window.",
    "<b>Photography content paused ~2 weeks.</b> Click Desk dev consumed Hadi&apos;s bandwidth. Acceptable trade-off given onboarding pressure, but directly explains the SEO position drops on competitive terms.",
    "<b>&ldquo;We call them back&rdquo; objection (restaurants).</b> Four-of-four in-person restaurant meetings raised price as the obstacle. Real diagnosis: value perception. Three reframes captured. Full objection-handling document not yet built.",
    "<b>Some leads should have been killed earlier.</b> Maria reviewed for 6+ weeks. Ace silent for 12+ days post-verbal-yes before being de facto written off. Earlier kill conditions would have freed bandwidth.",
    "<b>@hadyyazdani pause cost compounding follower growth.</b> Floor of 20K never approached. Pause was strategic but the cost compounded over weeks.",
    "<b>Maddie Mae methodology not adopted until Day 58.</b> The photography brand rebuild framework that should have been the foundation arrived as the window was closing. Phase 1 will lock in Window 2.",
]
for item in not_worked:
    story.append(bullet(item))

# ─── STRATEGIC INSIGHTS ─────────────────────────────────
story.append(Paragraph("Strategic Insights From the Window", h1))
insights = [
    "<b>The window measured the wrong things.</b> The real Day 60 question should have been: &ldquo;Do we have a model that produces clients repeatably?&rdquo; Answer: yes, just barely, and we have working product proof.",
    "<b>The performance anchor is the sales lever, carefully framed.</b> Kish&apos;s 2 confirmed outside-hours recoveries in 2-3 days extrapolate to ~20 per month &mdash; comfortably above the 10-per-month anchor on the strict definition. The honest pitch line: &ldquo;Our first restaurant client is capturing 2+ outside-hours bookings every 2-3 days through the AI &mdash; that projects to 20+ per month, well above our 10-booking guarantee.&rdquo; Honest, defensible, still strong.",
    "<b>The Persian / Iranian community is a defined go-to-market segment.</b> Heny + Kish + Mozhgan + Hadi&apos;s own roots. A coherent channel, not yet operationalised.",
    "<b>Trust &gt; Value &gt; Price.</b> Kish stated it explicitly. Confirmed across the window. Implications for sales script, voice, signing protocol, all of it.",
    "<b>Bandwidth is the binding constraint, not pipeline.</b> Half of the misses are sequencing problems inside one working week, not pipeline misses.",
    "<b>Photography is recoverable with focus.</b> Brand foundation in flight. CTR is the high-leverage fix. Content cadence has to restart. If those three things land in the next 60 days, photography returns. Otherwise it continues to decay.",
]
for item in insights:
    story.append(bullet(item))

story.append(PageBreak())

# ─── WINDOW 2 ───────────────────────────────────────────
story.append(Paragraph("Next 60-day Window &mdash; 1 June to 30 July 2026", h1))
story.append(Paragraph("Day 60 target reset &mdash; honest version", subtitle_style))

story.append(Paragraph("Agency (Primary)", h2))
agency2 = [
    [Paragraph("<b>Metric</b>", body_bold_white), Paragraph("<b>Window 2 Target</b>", body_bold_white), Paragraph("<b>Why</b>", body_bold_white)],
    [Paragraph("Total paid clients", body), Paragraph("<b>10</b> (Haleh + Kish converts + Heny converts + 7 net-new)", body), Paragraph("Pipeline math: ~2,760 cold-email sends &times; 4% reply &times; 25% to meeting &times; 25% close = 7 net-new. Conditional on cold email reply rate holding &ge;4%", body)],
    [Paragraph("MRR at Day 120", body), Paragraph("&pound;2,000 to &pound;3,000", body), Paragraph("Most new clients on Click Voice intro pricing (&pound;190 m1-3). Volume doesn&apos;t translate to proportional MRR until month 4 roll-up. If targeting &pound;5K, mix must include Click+ tier closes", body)],
    [Paragraph("Cold email volume", body), Paragraph("~46 / day campaign sends", body), Paragraph("Infrastructure already true; needs sustained execution", body)],
    [Paragraph("Performance anchor in pitches", body), Paragraph("Every restaurant pitch uses Kish case data", body), Paragraph("Lever is now real, with evidence", body)],
    [Paragraph("@clickaiagency", body), Paragraph("3,000 followers", body), Paragraph("Maintain bare-minimum cadence", body)],
    [Paragraph("Cold email reply rate", body), Paragraph("4%+ across 200+ sends", body), Paragraph("Kill condition if below", body)],
]
t3 = Table(agency2, colWidths=[55*mm, 50*mm, W - 2*MARGIN - 105*mm])
t3.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), BLACK),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(t3)
story.append(Spacer(1, 4*mm))

story.append(Paragraph("Photography (Secondary, Recovery mode)", h2))
photo2 = [
    [Paragraph("<b>Metric</b>", body_bold_white), Paragraph("<b>Window 2 Target</b>", body_bold_white), Paragraph("<b>Why</b>", body_bold_white)],
    [Paragraph("Brand foundation Phase 1 LOCKED", body), Paragraph("By 7 June", body), Paragraph("Sections 4-11 of foundation completed", body)],
    [Paragraph("Phase 2 website rebuild STARTED", body), Paragraph("By 14 June", body), Paragraph("Homepage rewrite + meta description fixes", body)],
    [Paragraph("Site CTR", body), Paragraph("0.7%+ by end of window", body), Paragraph("First measurable lever post-foundation", body)],
    [Paragraph("Blog cadence", body), Paragraph("1 post per 2 weeks minimum", body), Paragraph("Realistic given Click Desk and Heny onboarding load", body)],
    [Paragraph("Enquiries", body), Paragraph("5-8 per month", body), Paragraph("Floor, not full pace", body)],
    [Paragraph("@hadyyazdani", body), Paragraph("Maintain (no growth target)", body), Paragraph("Keep alive while rebuild ships", body)],
]
t4 = Table(photo2, colWidths=[55*mm, 50*mm, W - 2*MARGIN - 105*mm])
t4.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), BLACK),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(t4)
story.append(Spacer(1, 4*mm))

story.append(Paragraph("Cross-cutting principles", h2))
cross = [
    "<b>Operational discipline:</b> sequence weeks deliberately. Two days agency, one day photography, two days dev / onboarding, two days off. Stop alternating reactively.",
    "<b>Kill conditions, not optimism:</b> if a lead goes silent 7 days post-verbal-yes, escalate or accept loss. No more 12-day waits.",
    "<b>Reviews monthly, not quarterly:</b> lock 30 June and 30 July as smaller checkpoints.",
]
for item in cross:
    story.append(bullet(item))

# ─── VERDICT ────────────────────────────────────────────
story.append(Spacer(1, 6*mm))
story.append(rule())
story.append(Paragraph("Day 60 Verdict &mdash; one sentence", h1))
story.append(Paragraph(
    "&ldquo;The window did not produce the revenue. It produced the machine. The next 60 days will measure whether the machine works at volume.&rdquo;",
    verdict_style
))
story.append(rule())

# ─── FOOTER ─────────────────────────────────────────────
story.append(Spacer(1, 4*mm))
story.append(Paragraph("Click AI Agency &amp; Hadi Photography London | Day 60 Review | Generated 1 June 2026", body_small))

# BUILD
doc.build(story)
print(f"Day 60 Review PDF generated at: {OUTPUT}")
