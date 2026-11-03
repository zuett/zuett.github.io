from docx import Document
from docx.enum.section import WD_SECTION_START
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


OUT = "Pierre_Mikhiel_OceanX_Cover_Letter.docx"


def set_cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def set_cell_border(cell, color="D9E2EF", size="8"):
    tc_pr = cell._tc.get_or_add_tcPr()
    borders = tc_pr.first_child_found_in("w:tcBorders")
    if borders is None:
        borders = OxmlElement("w:tcBorders")
        tc_pr.append(borders)
    for edge in ("top", "left", "bottom", "right"):
        tag = "w:{}".format(edge)
        element = borders.find(qn(tag))
        if element is None:
            element = OxmlElement(tag)
            borders.append(element)
        element.set(qn("w:val"), "single")
        element.set(qn("w:sz"), size)
        element.set(qn("w:space"), "0")
        element.set(qn("w:color"), color)


def set_paragraph_spacing(paragraph, before=0, after=6, line=1.1):
    fmt = paragraph.paragraph_format
    fmt.space_before = Pt(before)
    fmt.space_after = Pt(after)
    fmt.line_spacing = line


def add_run(paragraph, text, bold=False, size=10.5, color="202124"):
    run = paragraph.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = RGBColor.from_string(color)
    return run


def add_paragraph(doc, text="", after=6, before=0, size=10.5, color="202124"):
    paragraph = doc.add_paragraph()
    set_paragraph_spacing(paragraph, before=before, after=after, line=1.1)
    if text:
        add_run(paragraph, text, size=size, color=color)
    return paragraph


doc = Document()
section = doc.sections[0]
section.start_type = WD_SECTION_START.NEW_PAGE
section.page_width = Inches(8.5)
section.page_height = Inches(11)
section.top_margin = Inches(0.75)
section.bottom_margin = Inches(0.75)
section.left_margin = Inches(0.9)
section.right_margin = Inches(0.9)
section.header_distance = Inches(0.35)
section.footer_distance = Inches(0.35)

styles = doc.styles
normal = styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10.5)
normal.font.color.rgb = RGBColor.from_string("202124")
normal.paragraph_format.space_after = Pt(6)
normal.paragraph_format.line_spacing = 1.1

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
set_paragraph_spacing(title, after=1)
add_run(title, "Pierre Mikhiel", bold=True, size=18, color="12355B")

subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
set_paragraph_spacing(subtitle, after=8)
add_run(
    subtitle,
    "Creative Technologist | XR, AI/ML Interaction, Immersive Education",
    size=10.5,
    color="4B5563",
)

contact = doc.add_paragraph()
contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
set_paragraph_spacing(contact, after=12)
add_run(
    contact,
    "Abu Dhabi, UAE  |  pmk2057@nyu.edu  |  +971 55 984 5520  |  pierremikhiel.com",
    size=9.5,
    color="4B5563",
)

rule = doc.add_table(rows=1, cols=1)
rule.allow_autofit = False
rule.columns[0].width = Inches(6.7)
rule.cell(0, 0).width = Inches(6.7)
set_cell_shading(rule.cell(0, 0), "12355B")
set_cell_border(rule.cell(0, 0), "12355B", "4")
rule.cell(0, 0).paragraphs[0].add_run("")

date = add_paragraph(doc, "June 5, 2026", after=8, before=12)

recipient = add_paragraph(doc, after=8)
add_run(recipient, "OceanX Education Hiring Team\n", bold=True, size=10.5)
add_run(recipient, "OceanX\nSingapore", size=10.5)

subject = add_paragraph(doc, after=10)
add_run(subject, "Re: AI Immersive Technologist, OceanX Education", bold=True, size=10.5)

add_paragraph(doc, "Dear OceanX Education Hiring Team,", after=8)

add_paragraph(
    doc,
    "I am excited to apply for the AI Immersive Technologist role with OceanX Education. I am a creative technologist and Interactive Media graduate from NYU Abu Dhabi, with minors in Computer Science and Film & New Media, and my work sits at the intersection of immersive storytelling, real-time 3D systems, machine-learning interfaces, and public education. OceanX's mission to make ocean science more accessible through exploration, media, and advanced technology strongly aligns with the kind of systems I want to build: experiences that help people feel scientific and environmental complexity, not just read about it.",
)

add_paragraph(
    doc,
    "My portfolio includes room-scale VR and XR installations, browser-based AI/ML learning tools, live performance systems, and research prototypes. In Whispers from the Depth, I developed an XR performance at NYUAD's Black Box Theater using motion capture, real-time digital avatars, projection, immersive sound, and environmental storytelling to address marine pollution. In Mondrian's Mirage, exhibited at Louvre Abu Dhabi, I translated an artwork into a navigable Unity-based VR environment. My capstone installation, V!Real(ity), combined VR scenes, primed audio, and spatial experience design to investigate perception, judgment, and agency.",
)

add_paragraph(
    doc,
    "I also bring hands-on experience with AI-driven interaction and research. As an ML research assistant, I proposed and built ASL Trainer, a webcam-based fingerspelling practice tool using p5.js, ml5.js, HandPose, dataset testing, real-time feedback, and a polished learning interface. I also developed an Interactive ML Portrait Builder that helps first-time users combine Face Mesh, Body Pose, Hand Pose, Body Segmentation, and Face Texture models into exportable starter projects. These projects taught me how to turn complex technical systems into approachable, exploratory tools for learners and audiences.",
)

add_paragraph(
    doc,
    "What draws me to OceanX is the chance to apply that practice to ocean education at a much larger scale. I can contribute across concept development, Unity and real-time prototyping, creative coding, AI-assisted production workflows, interaction design, and cross-functional collaboration with science, media, education, and technology teams. I am especially interested in translating real-world ocean data, expedition narratives, and scientific concepts into interactive environments where users can investigate, ask questions, and build an emotional relationship with the ocean.",
)

add_paragraph(
    doc,
    "I would be grateful for the opportunity to discuss how my background in XR, AI/ML interaction, environmental storytelling, and immersive public experiences could support OceanX Education's next generation of exploration-driven learning platforms. Thank you for your time and consideration.",
)

closing = add_paragraph(doc, "Sincerely,", after=2, before=6)
name = add_paragraph(doc, "Pierre Mikhiel", after=0)
name.runs[0].font.bold = True
name.runs[0].font.color.rgb = RGBColor.from_string("12355B")

doc.save(OUT)
print(OUT)
