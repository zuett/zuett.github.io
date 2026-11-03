from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUT = "Pierre_Mikhiel_Microsoft_Creative_Technologist_Resume.pdf"


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
    textColor=colors.HexColor("#0F2F57"),
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
    textColor=colors.HexColor("#0F2F57"),
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

doc = SimpleDocTemplate(
    OUT,
    pagesize=letter,
    leftMargin=0.58 * inch,
    rightMargin=0.58 * inch,
    topMargin=0.48 * inch,
    bottomMargin=0.48 * inch,
    title="Pierre Mikhiel - Microsoft Creative Technologist Resume",
    author="Pierre Mikhiel",
)

story = []

story.append(para("Pierre Mikhiel", name_style))
story.append(para("Creative Technologist / UX Engineer - AI, Real-Time 3D, Browser-Based Interactivity", headline_style))
story.append(
    para(
        "Abu Dhabi, UAE | Open to New York or Redmond relocation | +971 55 984 5520 | pmk2057@nyu.edu | pierremikhiel.com | github.com/zuett",
        contact_style,
    )
)

rule = Table([[""]], colWidths=[7.34 * inch], rowHeights=[0.025 * inch])
rule.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#0F2F57")),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]
    )
)
story.append(rule)

section("PROFILE", section_style, story)
story.append(
    para(
        "Creative technologist and UX engineer building functional prototypes, browser-based AI/ML interactions, and real-time Unity/XR experiences for research, education, and public storytelling. Strong at translating ambiguous creative concepts into high-fidelity demos, validating experience quality through user research and QA, and collaborating across design, engineering, research, production, and media teams.",
        summary_style,
    )
)

section("TECHNICAL SKILLS", section_style, story)
skills = [
    ("Creative engineering", "JavaScript, HTML/CSS, p5.js, ml5.js, TensorFlow.js, Python, C#, C++, Arduino"),
    ("Real-time / immersive", "Unity 3D, XR Interaction Toolkit, Cinemachine, Blender, VR prototyping, motion capture, projection, RGB DMX, QLC+"),
    ("AI / ML interaction", "HandPose, FaceMesh, Body Pose, Body Segmentation, dataset testing, model behavior tuning, in-browser computer vision"),
    ("UX / product storytelling", "high-fidelity prototyping, interaction design, demo scripting, visual pacing, QA testing, audience-facing installations, technical documentation"),
]
for label, text in skills:
    story.append(para(f"<b>{label}:</b> {text}", skills_style))

section("CREATIVE TECHNOLOGY EXPERIENCE", section_style, story)
story.append(para("Machine Learning Research Assistant - ml5.js, Interactive Media NYUAD", role_style))
story.append(para("Abu Dhabi, UAE | Jan. 2026 - Present", meta_style))
story.append(
    bullet(
        "Contribute to the creative application of ml5.js, an open-source browser-based machine learning library built on TensorFlow.js, by prototyping interactive demos for artists, educators, and students.",
        bullet_style,
    )
)
story.append(
    bullet(
        "Proposed and co-developed ASL Trainer, a deployed webcam-based fingerspelling practice tool using p5.js, ml5.js, HandPose, embedded neural assets, real-time feedback, and full-screen learning modes.",
        bullet_style,
    )
)
story.append(
    bullet(
        "Designed UI/UX flows for A-Z practice, word mode, reference visuals, progress feedback, and onboarding; tuned recognition behavior and in-browser performance for smoother live interaction.",
        bullet_style,
    )
)
story.append(
    bullet(
        "Built Interactive ML Portrait Builder, a browser tool that lets users compose Face Mesh, Body Pose, Hand Pose, Body Segmentation, and Face Texture models into exportable starter projects.",
        bullet_style,
    )
)

story.append(para("Research Assistant - VR Emotion Induction Toolkit, Aim Lab NYUAD", role_style))
story.append(para("Abu Dhabi, UAE | May 2025 - Sep. 2025", meta_style))
story.append(
    bullet(
        "Led design and Unity implementation for the Anger module of a modular VR toolbox studying universal emotions and stress.",
        bullet_style,
    )
)
story.append(
    bullet(
        "Engineered interactive scenarios using social unfairness, time pressure, environmental pacing, animation, and spatial cues to evoke measurable emotional responses.",
        bullet_style,
    )
)
story.append(
    bullet(
        "Supported biometric and behavioral validation workflows, connecting immersive experience design with research-grade measurement and iteration.",
        bullet_style,
    )
)

story.append(para("Co-Author - vER: Virtual Human Companionship for Preoperative Care", role_style))
story.append(para("IMX ACM 2025; EMRN Barcelona 2025", meta_style))
story.append(
    bullet(
        "Designed virtual companion agents that use social presence to reduce anxiety in simulated pre-operative hospital settings.",
        bullet_style,
    )
)
story.append(
    bullet(
        "Validated agent experience through a pilot study combining biometric tracking, qualitative surveys, and post-study analysis.",
        bullet_style,
    )
)

story.append(para("Creative Technology / Unity QA Intern, Mental.ae", role_style))
story.append(para("Abu Dhabi, UAE | Nov. 2024 - Jan. 2025", meta_style))
story.append(
    bullet(
        "Performed QA testing on interactive food-safety training modules, documenting UX issues, navigation friction, and product behavior gaps for design revisions.",
        bullet_style,
    )
)
story.append(
    bullet(
        "Used Unity Cinemachine to create dynamic camera systems and cinematic sequences for immersive training simulations and demo-ready learning content.",
        bullet_style,
    )
)

section("SELECTED PROTOTYPES, DEMOS & INSTALLATIONS", section_style, story)
projects = [
    (
        "V!Real(ity) - Capstone interactive installation + VR",
        "Designed and engineered a room-scale sensory system combining Unity VR, RGB DMX lighting, layered composite visuals, primed audio, and multi-user shadow mechanics to turn an abstract perception thesis into a filmable, audience-facing experience.",
    ),
    (
        "Mondrian's Mirage - VR installation, Louvre Abu Dhabi",
        "Translated a Mondrian composition into a navigable Unity-based VR environment with 3D spatial transitions, abstract architectural forms, and embodied museum interaction.",
    ),
    (
        "Whispers from the Depth - XR performance, NYUAD Black Box Theater",
        "Built an environmental XR performance about marine pollution using motion capture, real-time avatar projection, immersive sound, and visual storytelling for a live audience.",
    ),
    (
        "Beat-Hoven - Interactive music game, p5.js + Arduino",
        "Created a physical-digital music interface with Arduino buttons, serial communication, synchronized p5.js visuals, and layered beatboxing loops for public showcase interaction.",
    ),
    (
        "Alien Meta Rave / Are You There? - live-digital performances, New York",
        "Combined VR worlds, projection, DJing, machine-learning interaction, and performer silhouettes to explore virtual presence and hybrid storytelling.",
    ),
]
for title, text in projects:
    story.append(bullet(f"<b>{title}:</b> {text}", bullet_style))

section("EDUCATION", section_style, story)
story.append(para("<b>New York University Abu Dhabi</b> - B.A. in Interactive Media; Minors in Computer Science and Film & New Media", body_style))
story.append(para("Abu Dhabi, UAE | Cum Laude | Graduated May 2026 | Global semesters: New York City and Shanghai", meta_style))
story.append(
    para(
        "<b>Relevant coursework:</b> UX Design, Data Structures, Algorithms, VR Research and Applications, Designing Virtual Worlds, Virtual Body Performance, Sound Technology.",
        skills_style,
    )
)

section("PUBLIC WORK & RECOGNITION", section_style, story)
recognition = [
    "Presented virtual companion research at IMX ACM 2025 and EMRN Barcelona 2025.",
    "Exhibited Unity-based VR work at Louvre Abu Dhabi and hybrid performance work at La MaMa Studio, New York.",
    "ArtsIT 2024 organizer/media lead; documented conference programming across photography and digital media.",
    "Top 10 globally in Swissnex sustainability diplomacy competition for Future of Rights of Nature.",
    "Residential Assistant, NYU Abu Dhabi; coordinated social and educational programming for inclusive student communities.",
]
for item in recognition:
    story.append(bullet(item, bullet_style))

section("DEMO / PORTFOLIO LINKS", section_style, story)
links = [
    "Portfolio and project demos: pierremikhiel.com",
    "GitHub: github.com/zuett",
    "ASL Trainer source: github.com/zuett/ASL",
    "Interactive ML Portrait Builder source: github.com/zuett/Interactive-ML-Portrait-Builder",
    "V!Real(ity) capstone site: thelieyoubelieved.framer.website",
]
for item in links:
    story.append(bullet(item, bullet_style))

doc.build(story, onFirstPage=draw_background, onLaterPages=draw_background)
print(OUT)
