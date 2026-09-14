#!/usr/bin/env python3
"""Implant + Perio Clinic — Content Partnership Proposal (Click AI Agency).
Premium editorial template in the clinic's own palette (sage #606c68, navy #232737)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, PageBreak, KeepTogether)

W, H = A4
OUT = "/Users/hadi/Developer/Jodie-AI/projects/agency/14-09-26/implant-perio-proposal.pdf"

# ---- palette: theirs ---------------------------------------------------------
NAVY   = colors.HexColor("#232737")
SAGE   = colors.HexColor("#606c68")
SAGE_L = colors.HexColor("#8a938f")
MIST   = colors.HexColor("#e9ece9")   # card fill
CREAM  = colors.HexColor("#f7f6f2")   # page
INK    = colors.HexColor("#1f2230")
BODY   = colors.HexColor("#3d4048")
GREY   = colors.HexColor("#7c8088")
HAIR   = colors.HexColor("#d9dcd8")
WHITE  = colors.white

BAND_H = 62 * mm

S = {
 "body":   ParagraphStyle("body", fontName="Helvetica", fontSize=10.2, leading=15.5, textColor=BODY, spaceAfter=7),
 "lead":   ParagraphStyle("lead", fontName="Helvetica", fontSize=11.6, leading=17.5, textColor=INK, spaceAfter=9),
 "pull":   ParagraphStyle("pull", fontName="Helvetica-Bold", fontSize=11.2, leading=16, textColor=NAVY, spaceBefore=4, spaceAfter=9),
 "sec_num":ParagraphStyle("sec_num", fontName="Helvetica-Bold", fontSize=9.5, textColor=WHITE, alignment=TA_CENTER),
 "sec_title":ParagraphStyle("sec_title", fontName="Helvetica-Bold", fontSize=15, textColor=NAVY, leading=18),
 "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=10, leading=14.5, textColor=BODY, leftIndent=11, bulletIndent=0, spaceAfter=3.5),
 "opt_name":ParagraphStyle("opt_name", fontName="Helvetica-Bold", fontSize=8.2, textColor=SAGE_L, leading=11),
 "opt_title":ParagraphStyle("opt_title", fontName="Helvetica-Bold", fontSize=15, textColor=WHITE, leading=18),
 "opt_sub": ParagraphStyle("opt_sub", fontName="Helvetica-Oblique", fontSize=9.4, textColor=MIST, leading=13),
 "opt_b":   ParagraphStyle("opt_b", fontName="Helvetica", fontSize=9.4, leading=13.6, textColor=BODY, leftIndent=9, spaceAfter=3),
 "opt_price":ParagraphStyle("opt_price", fontName="Helvetica-Bold", fontSize=19, textColor=NAVY, leading=22),
 "opt_per": ParagraphStyle("opt_per", fontName="Helvetica", fontSize=9, textColor=GREY, leading=12),
 "tbl_h":   ParagraphStyle("tbl_h", fontName="Helvetica-Bold", fontSize=9, textColor=WHITE, leading=12),
 "tbl_k":   ParagraphStyle("tbl_k", fontName="Helvetica-Bold", fontSize=9.6, textColor=INK, leading=13),
 "tbl_v":   ParagraphStyle("tbl_v", fontName="Helvetica", fontSize=9.6, textColor=BODY, leading=13.5),
 "tbl_big": ParagraphStyle("tbl_big", fontName="Helvetica-Bold", fontSize=12, textColor=NAVY, leading=15),
 "small":   ParagraphStyle("small", fontName="Helvetica", fontSize=8.8, leading=13, textColor=GREY, spaceAfter=6),
 "sig_name":ParagraphStyle("sig_name", fontName="Helvetica-Bold", fontSize=11.5, textColor=INK, leading=15),
 "sig_co":  ParagraphStyle("sig_co", fontName="Helvetica", fontSize=9.6, textColor=GREY, leading=13.5),
}

# ---- page furniture ----------------------------------------------------------
def _bg(c):
    c.setFillColor(CREAM); c.rect(0, 0, W, H, fill=1, stroke=0)

def footer(c, doc):
    c.setStrokeColor(SAGE); c.setLineWidth(0.5)
    c.line(20*mm, 16*mm, W-20*mm, 16*mm)
    c.setFont("Helvetica", 8); c.setFillColor(GREY)
    c.drawString(20*mm, 11*mm, "Click AI Agency   |   clickaiagency.com   |   Prepared for Implant + Perio Clinic")
    c.drawRightString(W-20*mm, 11*mm, f"Page {c.getPageNumber()}")

def first_page(c, doc):
    c.saveState(); _bg(c)
    c.setFillColor(NAVY); c.rect(0, H-BAND_H, W, BAND_H, fill=1, stroke=0)
    c.setFillColor(SAGE); c.rect(0, H-BAND_H-1.2*mm, W, 1.2*mm, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 8.5); c.setFillColor(MIST)
    c.drawString(20*mm, H-14*mm, "C L I C K   A I   A G E N C Y")
    tw, th = 30*mm, 8*mm
    c.setFillColor(SAGE); c.roundRect(W-20*mm-tw, H-16.5*mm, tw, th, 1*mm, fill=1, stroke=0)
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(W-20*mm-tw/2, H-14*mm, "P R O P O S A L")
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 25)
    c.drawString(20*mm, H-32*mm, "Found Directly.")
    c.setFont("Helvetica", 14.5); c.setFillColor(MIST)
    c.drawString(20*mm, H-42.5*mm, "A content partnership for Implant + Perio Clinic")
    c.setFont("Helvetica-Oblique", 9.8); c.setFillColor(SAGE_L)
    c.drawString(20*mm, H-51.5*mm, "Prepared for Dr Sanaz Tehrani   |   September 2026")
    footer(c, doc); c.restoreState()

def later_pages(c, doc):
    c.saveState(); _bg(c)
    c.setFillColor(NAVY); c.rect(0, H-13*mm, W, 13*mm, fill=1, stroke=0)
    c.setFillColor(SAGE); c.rect(0, H-13.7*mm, W, 0.7*mm, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 8.5); c.setFillColor(MIST)
    c.drawString(20*mm, H-8.5*mm, "Implant + Perio Clinic   |   Content Partnership")
    c.setFont("Helvetica-Bold", 7.5); c.setFillColor(WHITE)
    c.drawRightString(W-20*mm, H-8.5*mm, "CLICK AI AGENCY")
    footer(c, doc); c.restoreState()

# ---- components --------------------------------------------------------------
def section(n, title):
    t = Table([[Paragraph(str(n), S["sec_num"]), Paragraph(title, S["sec_title"])]],
              colWidths=[9*mm, 161*mm], rowHeights=[9*mm])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(0,0),SAGE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                           ("LEFTPADDING",(1,0),(1,0),7),("LEFTPADDING",(0,0),(0,0),0),("RIGHTPADDING",(0,0),(0,0),0)]))
    return [Spacer(1,10), t, HRFlowable(width="100%", thickness=0.5, color=HAIR, spaceBefore=3, spaceAfter=8)]

def bullets(items, style="bullet"):
    return [Paragraph(f'<bullet><font color="#606c68">&#9679;</font></bullet> {t}', S[style]) for t in items]

def P(t, s="body"): return Paragraph(t, S[s])

def option_card(name, title, sub, items, price, width):
    head = Table([[Paragraph(name, S["opt_name"])],[Paragraph(title, S["opt_title"])],[Paragraph(sub, S["opt_sub"])]], colWidths=[width])
    head.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),NAVY),("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
                              ("TOPPADDING",(0,0),(-1,0),9),("BOTTOMPADDING",(0,0),(-1,0),1),("TOPPADDING",(0,1),(-1,1),0),
                              ("BOTTOMPADDING",(0,1),(-1,1),2),("TOPPADDING",(0,2),(-1,2),0),("BOTTOMPADDING",(0,2),(-1,2),10)]))
    body_rows = [[b] for b in bullets(items, "opt_b")]
    body = Table(body_rows, colWidths=[width])
    body.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),WHITE),("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
                              ("TOPPADDING",(0,0),(-1,0),9),("BOTTOMPADDING",(0,-1),(-1,-1),6)]))
    foot = Table([[Paragraph(price, S["opt_price"]), Paragraph("per month", S["opt_per"])]], colWidths=[width*0.55, width*0.45])
    foot.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),MIST),("LINEABOVE",(0,0),(-1,0),1.2,SAGE),("VALIGN",(0,0),(-1,-1),"BOTTOM"),
                              ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),9)]))
    card = Table([[head],[body],[foot]], colWidths=[width])
    card.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
                              ("BOX",(0,0),(-1,-1),0.6,HAIR)]))
    return card

def kv_table(rows, kw=42*mm, vw=128*mm):
    data = [[Paragraph(k, S["tbl_k"]), Paragraph(v, S["tbl_v"])] for k, v in rows]
    t = Table(data, colWidths=[kw, vw])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LINEBELOW",(0,0),(-1,-2),0.5,HAIR),
                           ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),("LEFTPADDING",(0,0),(-1,-1),4)]))
    return t

# ---- document ----------------------------------------------------------------
doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=24*mm, bottomMargin=24*mm,
                        title="Implant + Perio Clinic — Content Partnership Proposal", author="Click AI Agency")
E = [Spacer(1, BAND_H + 10*mm - 24*mm)]

# 1
E += section(1, "Where you are, and where you want to be")
E += [P("You told us something most clinics never say out loud: you are happy with the patients you have. The work is complex, the standards are high, and the people who find you are the right people.", "lead"),
      P("What you want to change is how they find you."),
      P("Today a meaningful share of your most valuable cases arrive through referral, and referral carries a cost that has nothing to do with the quality of the treatment. Your priority for 2027 is to be found directly, so that the patients who need what you do come to you first."),
      P("That is a visibility problem, and it has a specific shape. Implant + Perio Clinic is an established specialist practice on Portland Place, trading for nearly two decades, with 150 five-star reviews and a team that has been together for over ten years. Online, the practice is close to invisible. The Instagram account has 213 followers. The website does not link to it."),
      P("The gap between how good the clinic is and how findable it is, is the whole opportunity.", "pull")]

# 2
E += section(2, "The camera problem, solved")
E += [P("The obstacle is a familiar one. The people who should be on camera, the clinicians, would rather not be. That is entirely reasonable, and it has stopped a great many excellent practices from ever starting."),
      P("We build a realistic AI avatar of each principal: your likeness and your voice, created in a single studio session at the clinic. From then on, every reel, every explainer, every short piece of patient education is presented by you, in your voice, without you standing in front of a camera again."),
      P("We write and produce everything. You approve every word.", "pull")]

# 3
sec3 = section(3, "How each week works")
E += [KeepTogether(sec3 + [kv_table([("Monday", "We draft the week's scripts from the editorial plan, in your voice, on your treatments."),
                ("Tuesday", "You approve, amend or decline each one. Every piece is produced only after your written sign-off."),
                ("Wednesday to Thursday", "We produce the reels, captions and stills, matched to the clinic's visual identity."),
                ("Friday to Sunday", "Content publishes on schedule. We handle comments and enquiries, and escalate anything clinical to your team.")]),
      Spacer(1,6), P("You see it before your patients do. Every time.", "pull")])]

# 4
sec4 = section(4, "Two ways to work together")
cw = 82*mm
c1 = option_card("OPTION ONE", "Core", "The clinic present every week, consistently, in its own voice.",
    ["<b>2 AI avatar reels per week</b> (8 per month)",
     "<b>1 further post per week</b>: carousel, photograph or educational still, making <b>12 posts per month</b>",
     "3 stories per week",
     "Instagram managed end to end: captions, scheduling, comment and enquiry triage",
     "<b>Quarterly photography session</b> at the clinic (half day)",
     "Monthly performance report",
     "Named account manager, same-business-day response"], "£1,490", cw)
c2 = option_card("OPTION TWO", "Complete", "The full engine: enough volume to lead the specialist conversation in London, with website assets to match.",
    ["<b>4 AI avatar reels per week</b> (16 per month)",
     "<b>2 further posts per week</b>, making <b>24 posts per month</b>",
     "Daily stories",
     "Instagram and Facebook managed end to end",
     "<b>Monthly photography session</b> at the clinic (half day), including consented patient-journey work",
     "<b>One avatar-led explainer video per month for the website</b>: implants, periodontics, Invisalign, rotating through your treatments",
     "Monthly strategy call and report, quarterly review",
     "<b>Dedicated account manager</b>"], "£2,490", cw)
pair = Table([[c1, c2]], colWidths=[cw, cw], hAlign="LEFT")
pair.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(0,0),6*mm),("RIGHTPADDING",(1,0),(1,0),0)]))
E += [KeepTogether(sec4 + [pair]), Spacer(1,8), P("Both options run month to month, with 30 days' notice either way.", "small")]

# 5
E += section(5, "Avatar Studio Setup")
E += [P("Before the first reel, we build the foundation. This is a one-off piece of work, priced separately from the monthly service.")]
E += bullets(["<b>Studio session at the clinic</b>: avatar capture and voice capture for Dr Tehrani and Dr Negahban",
              "<b>Likeness and voice agreement</b>, so you hold full control over how your avatar is used",
              "<b>Visual identity for video</b>: lower-thirds, end cards, caption style, colour grade matched to the clinic's palette",
              "<b>Content pillars and a 90-day editorial plan</b> across implants, periodontics, Invisalign, whitening, patient journey, team and clinic",
              "<b>Foundation photography session</b>: clinic, team, treatment rooms and hero images for the website",
              "<b>Instagram profile rebuild</b>: bio, highlights, link and grid strategy"])
setup = Table([[Paragraph("Avatar Studio Setup", S["tbl_k"]), Paragraph("£1,950", S["tbl_big"])],
               [Paragraph("Third clinician avatar (Dr Tinti)", S["tbl_v"]), Paragraph("£450", S["tbl_v"])]], colWidths=[120*mm, 50*mm])
setup.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),MIST),("LINEABOVE",(0,0),(-1,0),1.2,SAGE),("LINEBELOW",(0,0),(-1,0),0.5,HAIR),
                           ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7),("LEFTPADDING",(0,0),(-1,-1),10),("ALIGN",(1,0),(1,-1),"RIGHT")]))
E += [Spacer(1,6), setup]

# 6
sec6 = section(6, "Investment")
inv = Table([[Paragraph("", S["tbl_h"]), Paragraph("Option One · Core", S["tbl_h"]), Paragraph("Option Two · Complete", S["tbl_h"])],
             [Paragraph("Monthly", S["tbl_k"]), Paragraph("£1,490", S["tbl_big"]), Paragraph("£2,490", S["tbl_big"])],
             [Paragraph("Avatar Studio Setup (one-off)", S["tbl_k"]), Paragraph("£1,950", S["tbl_v"]), Paragraph("£1,950", S["tbl_v"])],
             [Paragraph("Term", S["tbl_k"]), Paragraph("Month to month, 30 days' notice", S["tbl_v"]), Paragraph("Month to month, 30 days' notice", S["tbl_v"])]],
            colWidths=[58*mm, 56*mm, 56*mm])
inv.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("BACKGROUND",(0,1),(-1,-1),WHITE),("LINEBELOW",(0,1),(-1,-2),0.5,HAIR),
                         ("BOX",(0,0),(-1,-1),0.6,HAIR),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                         ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8),("LEFTPADDING",(0,0),(-1,-1),9)]))
E += [KeepTogether(sec6 + [inv]), Spacer(1,8),
      P("Studio Setup is invoiced on agreement and secures your January start. The first monthly invoice falls on 1 January 2027.", "small")]

# 7
E += [KeepTogether(section(7, "Timeline to January") + [P("You told us January is when you want to begin. Working back from that:"),
      kv_table([("On agreement", "Studio Setup confirmed. January secured."),
                ("November", "Studio session at the clinic. Avatars built. Photography session. Editorial plan agreed."),
                ("December", "Instagram profile rebuilt. First month of content produced and approved ahead of time."),
                ("1 January 2027", "Live, at full pace from week one.")])])]

# 8
E += [KeepTogether(section(8, "Standards") + [P("Dental advertising in the UK sits under GDC guidance and the CAP Code, and content carrying a clinician's likeness deserves particular care. Every script is approved in writing by the named clinician before production. Every claim is accurate and specific to your practice. Patient imagery is used only with documented consent. Content is AI-produced and human-reviewed, always.")])]

# 9
E += [KeepTogether(section(9, "The next step") + [P("Choose the option that fits. We send the agreement the same day, confirm the November studio date, and January opens with the clinic present, in its own voice, every week.", "lead"),
      Spacer(1,14),
      HRFlowable(width=60*mm, thickness=0.6, color=SAGE, hAlign="LEFT", spaceAfter=6),
      Paragraph("Hadi Yazdani", S["sig_name"]),
      Paragraph("Founder, Click AI Agency", S["sig_co"]),
      Paragraph("clickaiagency.com", S["sig_co"])])]

doc.build(E, onFirstPage=first_page, onLaterPages=later_pages)
print("PDF written:", OUT)
