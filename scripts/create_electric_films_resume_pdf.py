from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUT = "Pierre_Mikhiel_Electric_Films_Junior_Assistant_Producer_Resume.pdf"


def para(text, style):
    return Paragraph(text, style)


def bullet(text, style):
    return Paragraph(text, style, bulletText="-")


def section(title, style, story):
    story.append(Spacer(1, 4))
    story.append(para(title, style))


def draw_background(canvas, _doc):
    canvas.saveState()
    canvas.setFillColor(colors.white)
    canvas.rect(0, 0, letter[0], letter[1], stroke=0, fill=1)
    canvas.restoreState()


styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=18,
    leading=20,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#111827"),
    spaceAfter=1,
)

headline_style = ParagraphStyle(
    "Headline",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9.8,
    leading=11.5,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#374151"),
    spaceAfter=2,
)

contact_style = ParagraphStyle(
    "Contact",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.9,
    leading=10.5,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#374151"),
    spaceAfter=5,
)

section_style = ParagraphStyle(
    "Section",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=10.2,
    leading=11.5,
    textColor=colors.HexColor("#111827"),
    spaceBefore=2,
    spaceAfter=3,
)

body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.75,
    leading=10.2,
    alignment=TA_LEFT,
    textColor=colors.HexColor("#111827"),
    spaceAfter=3,
)

summary_style = ParagraphStyle(
    "Summary",
    parent=body_style,
    fontSize=9.0,
    leading=10.8,
    spaceAfter=5,
)

role_style = ParagraphStyle(
    "Role",
    parent=body_style,
    fontName="Helvetica-Bold",
    fontSize=9.1,
    leading=10.3,
    textColor=colors.HexColor("#111827"),
    spaceBefore=3,
    spaceAfter=1,
)

meta_style = ParagraphStyle(
    "Meta",
    parent=body_style,
    fontName="Helvetica-Oblique",
    fontSize=8.5,
    leading=9.6,
    textColor=colors.HexColor("#4B5563"),
    spaceAfter=2,
)

bullet_style = ParagraphStyle(
    "Bullet",
    parent=body_style,
    leftIndent=12,
    firstLineIndent=-7,
    bulletIndent=3,
    spaceAfter=1.8,
)

skills_style = ParagraphStyle(
    "Skills",
    parent=body_style,
    fontSize=8.55,
    leading=10,
    spaceAfter=2,
)

project_style = ParagraphStyle(
    "Project",
    parent=body_style,
    fontSize=8.65,
    leading=10.1,
    spaceAfter=2.2,
)

doc = SimpleDocTemplate(
    OUT,
    pagesize=letter,
    leftMargin=0.58 * inch,
    rightMargin=0.58 * inch,
    topMargin=0.48 * inch,
    bottomMargin=0.48 * inch,
    title="Pierre Mikhiel - Electric Films Junior Assistant Producer Resume",
    author="Pierre Mikhiel",
)

story = []

story.append(para("Pierre Mikhiel", name_style))
story.append(para("Junior Producer / Production Coordinator / Media Assistant", headline_style))
story.append(
    para(
        "Abu Dhabi, UAE | Available in Dubai | +971 55 984 5520 | pmk2057@nyu.edu | pierremikhiel.com",
        contact_style,
    )
)

rule = Table([[""]], colWidths=[7.34 * inch], rowHeights=[0.025 * inch])
rule.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#111827")),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]
    )
)
story.append(rule)

section("PROFESSIONAL SUMMARY", section_style, story)
story.append(
    para(
        "Organised, client-facing media graduate (Cum Laude, NYU Abu Dhabi) with hands-on experience supporting live productions, event logistics, and social content delivery across the UAE. Proven liaison between stakeholders, crew, and administration; comfortable managing schedules, feedback, and day-of shoot coordination. Bilingual in English and Arabic, with a genuine interest in film, branded content, and fast-moving creative production environments.",
        summary_style,
    )
)

section("CORE STRENGTHS", section_style, story)
strengths = [
    "<b>Client & stakeholder communication</b> - primary point of contact across events, exhibitions, and university programming",
    "<b>Production logistics</b> - scheduling, run-of-show planning, crew coordination, and on-set support",
    "<b>Social & content delivery</b> - Instagram, LinkedIn, and TikTok-ready photography, video, captions, and behind-the-scenes posts",
    "<b>Documentation & research</b> - production notes, media pipelines, casting/sourcing support, and rapid turnaround deliverables",
]
for item in strengths:
    story.append(bullet(item, bullet_style))

section("PRODUCTION & CLIENT-FACING EXPERIENCE", section_style, story)

story.append(para("Freelance Production & Event Media Coordinator", role_style))
story.append(para("Independent | Abu Dhabi & Dubai, UAE | 2022 - Present", meta_style))
for item in [
    "Act as on-site production contact for conferences, exhibitions, performances, and institutional events; manage schedules, shot lists, and client approvals.",
    "Deliver edited photography, short-form video, and platform-ready social assets with same-day turnaround for stakeholders and organisers.",
    "Plan and publish event coverage across Instagram and LinkedIn, including captions, cropping, and behind-the-scenes content aligned to client tone.",
    "Coordinate logistics end-to-end: equipment prep, vendor communication, file delivery, and structured feedback rounds.",
]:
    story.append(bullet(item, bullet_style))

story.append(para("ArtsIT Conference - Organizer & Media Lead", role_style))
story.append(para("Abu Dhabi, UAE | 2024 - 2025", meta_style))
for item in [
    "Led media planning and day-of production for an international arts conference; scheduled coverage, assigned shooters, and published daily social highlights.",
    "Coordinated speakers, volunteers, and venue teams to keep parallel sessions on time and communication clear across departments.",
]:
    story.append(bullet(item, bullet_style))

story.append(para("NYU Abu Dhabi Housing - Residential Assistant", role_style))
story.append(para("Abu Dhabi, UAE | 2023 - 2026", meta_style))
for item in [
    "Served as primary liaison between residents and university administration; handled inquiries, scheduling, and escalations with professionalism.",
    "Planned and executed community events including logistics, vendor booking, and post-event documentation for 200+ residents.",
]:
    story.append(bullet(item, bullet_style))

story.append(para("Mental.ae - Creative Production Intern", role_style))
story.append(para("Abu Dhabi, UAE | Nov 2024 - Jan 2025", meta_style))
for item in [
    "Supported QA and documentation for training media content; tracked issues and communicated actionable feedback across design and production teams.",
    "Assisted cinematic sequence production using Unity and Cinemachine for client-facing demo and training deliverables.",
]:
    story.append(bullet(item, bullet_style))

section("SELECTED PRODUCTIONS", section_style, story)
projects = [
    (
        "V!Real(ity) - Capstone exhibition",
        "Produced immersive installation; coordinated technical rehearsals, crew scheduling, and live audience flow from prep through show.",
    ),
    (
        "Mondrian's Mirage - Louvre Abu Dhabi",
        "Delivered public VR installation; liaised with museum staff on install timelines, visitor coordination, and exhibition requirements.",
    ),
    (
        "Whispers from the Depth - NYUAD Black Box",
        "Supported live XR performance production including run-of-show, motion-capture crew, and audience-facing delivery.",
    ),
    (
        "Alien Meta Rave - New York",
        "Coordinated live VR music event integrating projection, talent, and audience engagement across a compressed production schedule.",
    ),
    (
        "Are You There? - La MaMa Studio, NYC",
        "Co-produced hybrid performance; managed projection, music, and live talent coordination during show week.",
    ),
]
for title, text in projects:
    story.append(para(f"<b>{title}:</b> {text}", project_style))

section("EDUCATION", section_style, story)
story.append(para("<b>New York University Abu Dhabi</b> - B.A. in Interactive Media, Cum Laude", body_style))
story.append(para("Abu Dhabi, UAE | May 2026 | Minors: Film & New Media, Computer Science", meta_style))
story.append(
    para(
        "<b>Relevant coursework:</b> Film production, virtual worlds, sound technology, UX design, performance systems.",
        skills_style,
    )
)

section("SKILLS", section_style, story)
skills = [
    ("Production", "Scheduling & call sheets, client liaison, crew & talent coordination, location & logistics support, casting & sourcing research, production documentation"),
    ("Social & content", "Instagram, LinkedIn, TikTok, caption writing, behind-the-scenes content, photography & videography, rapid asset turnaround"),
    ("Tools & languages", "DaVinci Resolve, Adobe Creative Suite, OBS Studio, Blender, English (fluent), Arabic (fluent)"),
]
for label, text in skills:
    story.append(para(f"<b>{label}:</b> {text}", skills_style))

doc.build(story, onFirstPage=draw_background, onLaterPages=draw_background)
print(OUT)
