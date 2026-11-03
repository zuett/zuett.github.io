from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUT = "Pierre_Mikhiel_OceanX_Cover_Letter.pdf"


def p(text, style):
    return Paragraph(text, style)


styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=18,
    leading=21,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#12355B"),
    spaceAfter=2,
)

subtitle_style = ParagraphStyle(
    "Subtitle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=10,
    leading=12,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#4B5563"),
    spaceAfter=3,
)

contact_style = ParagraphStyle(
    "Contact",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9,
    leading=11,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#4B5563"),
    spaceAfter=10,
)

body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=10,
    leading=13.15,
    textColor=colors.HexColor("#202124"),
    spaceAfter=7,
)

body_tight = ParagraphStyle(
    "BodyTight",
    parent=body_style,
    spaceAfter=4,
)

subject_style = ParagraphStyle(
    "Subject",
    parent=body_style,
    fontName="Helvetica-Bold",
    spaceAfter=8,
)

doc = SimpleDocTemplate(
    OUT,
    pagesize=letter,
    rightMargin=0.85 * inch,
    leftMargin=0.85 * inch,
    topMargin=0.62 * inch,
    bottomMargin=0.62 * inch,
    title="Pierre Mikhiel - OceanX Cover Letter",
    author="Pierre Mikhiel",
)

story = []

story.append(p("Pierre Mikhiel", name_style))
story.append(p("Creative Technologist | XR, AI/ML Interaction, Immersive Education", subtitle_style))
story.append(p("Abu Dhabi, UAE | pmk2057@nyu.edu | +971 55 984 5520 | pierremikhiel.com", contact_style))

rule = Table([[""]], colWidths=[6.8 * inch], rowHeights=[0.035 * inch])
rule.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#12355B")),
            ("LINEABOVE", (0, 0), (-1, -1), 0, colors.HexColor("#12355B")),
            ("LINEBELOW", (0, 0), (-1, -1), 0, colors.HexColor("#12355B")),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]
    )
)
story.append(rule)
story.append(Spacer(1, 0.12 * inch))

story.append(p("June 5, 2026", body_tight))
story.append(p("<b>OceanX Education Hiring Team</b><br/>OceanX<br/>Singapore", body_tight))
story.append(Spacer(1, 0.04 * inch))
story.append(p("Re: AI Immersive Technologist, OceanX Education", subject_style))
story.append(p("Dear OceanX Education Hiring Team,", body_tight))

paragraphs = [
    "I am excited to apply for the AI Immersive Technologist role with OceanX Education. I am a creative technologist and Interactive Media graduate from NYU Abu Dhabi, with minors in Computer Science and Film & New Media, and my work sits at the intersection of immersive storytelling, real-time 3D systems, machine-learning interfaces, and public education. OceanX's mission to make ocean science more accessible through exploration, media, and advanced technology strongly aligns with the kind of systems I want to build: experiences that help people feel scientific and environmental complexity, not just read about it.",
    "My portfolio includes room-scale VR and XR installations, browser-based AI/ML learning tools, live performance systems, and research prototypes. In <i>Whispers from the Depth</i>, I developed an XR performance at NYUAD's Black Box Theater using motion capture, real-time digital avatars, projection, immersive sound, and environmental storytelling to address marine pollution. In <i>Mondrian's Mirage</i>, exhibited at Louvre Abu Dhabi, I translated an artwork into a navigable Unity-based VR environment. My capstone installation, <i>V!Real(ity)</i>, combined VR scenes, primed audio, and spatial experience design to investigate perception, judgment, and agency.",
    "I also bring hands-on experience with AI-driven interaction and research. As an ML research assistant, I proposed and built <i>ASL Trainer</i>, a webcam-based fingerspelling practice tool using p5.js, ml5.js, HandPose, dataset testing, real-time feedback, and a polished learning interface. I also developed an <i>Interactive ML Portrait Builder</i> that helps first-time users combine Face Mesh, Body Pose, Hand Pose, Body Segmentation, and Face Texture models into exportable starter projects. These projects taught me how to turn complex technical systems into approachable, exploratory tools for learners and audiences.",
    "What draws me to OceanX is the chance to apply that practice to ocean education at a much larger scale. I can contribute across concept development, Unity and real-time prototyping, creative coding, AI-assisted production workflows, interaction design, and cross-functional collaboration with science, media, education, and technology teams. I am especially interested in translating real-world ocean data, expedition narratives, and scientific concepts into interactive environments where users can investigate, ask questions, and build an emotional relationship with the ocean.",
    "I would be grateful for the opportunity to discuss how my background in XR, AI/ML interaction, environmental storytelling, and immersive public experiences could support OceanX Education's next generation of exploration-driven learning platforms. Thank you for your time and consideration.",
]

for paragraph in paragraphs:
    story.append(p(paragraph, body_style))

story.append(Spacer(1, 0.02 * inch))
story.append(p("Sincerely,", body_tight))
story.append(p("<b><font color='#12355B'>Pierre Mikhiel</font></b>", body_tight))

doc.build(story)
print(OUT)
