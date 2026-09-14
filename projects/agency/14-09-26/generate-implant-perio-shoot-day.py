#!/usr/bin/env python3
"""Implant + Perio Clinic — Photography & Film Shoot Day, one-page outline. Same palette as the proposal."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

W, H = A4
OUT = "/Users/hadi/Developer/Jodie-AI/projects/agency/14-09-26/implant-perio-shoot-day.pdf"
NAVY=colors.HexColor("#232737"); SAGE=colors.HexColor("#606c68"); SAGE_L=colors.HexColor("#8a938f")
MIST=colors.HexColor("#e9ece9"); CREAM=colors.HexColor("#f7f6f2"); INK=colors.HexColor("#1f2230")
BODY=colors.HexColor("#3d4048"); GREY=colors.HexColor("#7c8088"); HAIR=colors.HexColor("#d9dcd8"); WHITE=colors.white
BAND=44*mm

S={
 "lead":ParagraphStyle("lead",fontName="Helvetica",fontSize=11.2,leading=16.5,textColor=INK,spaceAfter=8),
 "body":ParagraphStyle("body",fontName="Helvetica",fontSize=9.8,leading=14.5,textColor=BODY,spaceAfter=5),
 "h":ParagraphStyle("h",fontName="Helvetica-Bold",fontSize=11.5,textColor=NAVY,leading=14,spaceBefore=9,spaceAfter=4),
 "b":ParagraphStyle("b",fontName="Helvetica",fontSize=9.6,leading=13.6,textColor=BODY,leftIndent=10,spaceAfter=2.5),
 "k":ParagraphStyle("k",fontName="Helvetica-Bold",fontSize=9.6,textColor=INK,leading=13),
 "v":ParagraphStyle("v",fontName="Helvetica",fontSize=9.6,textColor=BODY,leading=13.5),
 "price":ParagraphStyle("price",fontName="Helvetica-Bold",fontSize=22,textColor=NAVY,leading=25),
 "per":ParagraphStyle("per",fontName="Helvetica",fontSize=9.2,textColor=GREY,leading=12),
 "pull":ParagraphStyle("pull",fontName="Helvetica-Bold",fontSize=10.6,leading=15,textColor=NAVY,spaceBefore=4,spaceAfter=6),
 "small":ParagraphStyle("small",fontName="Helvetica",fontSize=8.6,leading=12.5,textColor=GREY),
 "sig":ParagraphStyle("sig",fontName="Helvetica-Bold",fontSize=10.5,textColor=INK,leading=14),
 "sigc":ParagraphStyle("sigc",fontName="Helvetica",fontSize=9,textColor=GREY,leading=12.5),
}
def P(t,s="body"): return Paragraph(t,S[s])
def B(items): return [Paragraph(f'<bullet><font color="#606c68">&#9679;</font></bullet> {t}',S["b"]) for t in items]

def page(c,doc):
    c.saveState()
    c.setFillColor(CREAM); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(NAVY); c.rect(0,H-BAND,W,BAND,fill=1,stroke=0)
    c.setFillColor(SAGE); c.rect(0,H-BAND-1.2*mm,W,1.2*mm,fill=1,stroke=0)
    c.setFont("Helvetica-Bold",8.5); c.setFillColor(MIST); c.drawString(20*mm,H-13*mm,"C L I C K   A I   A G E N C Y")
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold",21); c.drawString(20*mm,H-27*mm,"A Shoot Day at the Clinic")
    c.setFont("Helvetica",11.5); c.setFillColor(MIST); c.drawString(20*mm,H-35.5*mm,"Photography and film for Implant + Perio Clinic   |   Prepared for Dr Sanaz Tehrani")
    c.setStrokeColor(SAGE); c.setLineWidth(0.5); c.line(20*mm,14*mm,W-20*mm,14*mm)
    c.setFont("Helvetica",8); c.setFillColor(GREY)
    c.drawString(20*mm,9.5*mm,"Click AI Agency   |   clickaiagency.com")
    c.drawRightString(W-20*mm,9.5*mm,"September 2026")
    c.restoreState()

doc=SimpleDocTemplate(OUT,pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,topMargin=BAND+9*mm,bottomMargin=20*mm,
                      title="A Shoot Day at the Clinic — Implant + Perio Clinic",author="Click AI Agency")
E=[]
E+=[P("Real photographs and real footage of the clinic and the people in it, made by a professional team on a single day, then edited and distributed for you. Nothing to film yourselves. Nothing that becomes a second job.","lead")]

E+=[P("What happens on the day","h")]
E+=B(["<b>Photography</b> of the clinic, the treatment rooms, the team at work and the details that make the place what it is",
      "<b>Film</b>: genuine footage of the clinic and team, shot for short pieces rather than long ones",
      "<b>Clinician pieces</b>, when you feel like it: a short real answer to a real patient question, in your own words. Optional, every time",
      "We work alongside you and around the diary. Patients and treatments come first; we fit into the gaps"])

E+=[P("What you receive from each day","h")]
E+=B(["A library of edited photographs for the website, social media, print and anything else you need",
      "One short film of the clinic, and a set of short clips cut from the day",
      "Any clinician pieces recorded, edited and captioned",
      "<b>Distribution across the month</b>, handled by us, so the content works without anyone at the clinic touching it. Or the full library handed over for your team to use as they wish"])

E+=[P("Cadence","h"),
    P("Once a month, or once every two months. Your choice, and it can change. Each day stands on its own, so you book the next one when you want it.")]

price=Table([[Paragraph("Per shoot day",S["k"]),Paragraph("£1,400",S["price"]),Paragraph("Photography, film, editing and distribution for the month. That is the whole price.",S["per"])]],
            colWidths=[36*mm,40*mm,94*mm])
price.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),MIST),("LINEABOVE",(0,0),(-1,0),1.3,SAGE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                           ("TOPPADDING",(0,0),(-1,-1),10),("BOTTOMPADDING",(0,0),(-1,-1),10),("LEFTPADDING",(0,0),(-1,-1),10)]))
E+=[Spacer(1,6),price,Spacer(1,4),
    P("Invoiced per day, after the shoot. One price, one day at a time.","small")]

E+=[P("Who is behind the camera","h"),
    P("Hadi has spent twenty years behind a camera, first as a photojournalist and then photographing people and places for a living. This is the work he knows best, and he will be at the clinic on every shoot day.")]

E+=[P("The next step","h"),
    P("Pick a cadence, and we put the first day in the diary. Everything else follows from that.","pull"),
    Spacer(1,6),HRFlowable(width=55*mm,thickness=0.6,color=SAGE,hAlign="LEFT",spaceAfter=5),
    Paragraph("Hadi Yazdani",S["sig"]),Paragraph("Founder, Click AI Agency  |  clickaiagency.com",S["sigc"])]

doc.build(E,onFirstPage=page,onLaterPages=page)
print("written:",OUT)
