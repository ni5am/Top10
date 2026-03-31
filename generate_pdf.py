#!/usr/bin/env python3
"""Generate a PDF of all OWASP Top 10 2025 files."""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

DOCS_DIR = "/home/user/Top10/2025/docs/en"
OUTPUT_PDF = "/home/user/Top10/OWASP_Top10_2025.pdf"

FILES = [
    "0x00_2025-Introduction.md",
    "0x01_2025-About_OWASP.md",
    "0x02_2025-What_are_Application_Security_Risks.md",
    "0x03_2025-Establishing_a_Modern_Application_Security_Program.md",
    "A01_2025-Broken_Access_Control.md",
    "A02_2025-Security_Misconfiguration.md",
    "A03_2025-Software_Supply_Chain_Failures.md",
    "A04_2025-Cryptographic_Failures.md",
    "A05_2025-Injection.md",
    "A06_2025-Insecure_Design.md",
    "A07_2025-Authentication_Failures.md",
    "A08_2025-Software_or_Data_Integrity_Failures.md",
    "A09_2025-Security_Logging_and_Alerting_Failures.md",
    "A10_2025-Mishandling_of_Exceptional_Conditions.md",
]

def build_styles():
    styles = getSampleStyleSheet()
    custom = {
        "h1": ParagraphStyle("h1", parent=styles["Heading1"], fontSize=20, textColor=colors.HexColor("#003366"), spaceAfter=12),
        "h2": ParagraphStyle("h2", parent=styles["Heading2"], fontSize=14, textColor=colors.HexColor("#005a9e"), spaceAfter=8, spaceBefore=12),
        "h3": ParagraphStyle("h3", parent=styles["Heading3"], fontSize=12, textColor=colors.HexColor("#336699"), spaceAfter=6, spaceBefore=8),
        "body": ParagraphStyle("body", parent=styles["Normal"], fontSize=10, spaceAfter=6, leading=14),
        "bullet": ParagraphStyle("bullet", parent=styles["Normal"], fontSize=10, leftIndent=20, spaceAfter=4, leading=14, bulletIndent=10),
        "code": ParagraphStyle("code", parent=styles["Code"], fontSize=8, backColor=colors.HexColor("#f4f4f4"), leftIndent=20, rightIndent=20, spaceAfter=8, spaceBefore=4),
        "title": ParagraphStyle("title", parent=styles["Title"], fontSize=28, textColor=colors.HexColor("#003366"), alignment=TA_CENTER, spaceAfter=20),
        "subtitle": ParagraphStyle("subtitle", parent=styles["Normal"], fontSize=14, textColor=colors.HexColor("#555555"), alignment=TA_CENTER, spaceAfter=40),
    }
    return custom

def escape_xml(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text

def parse_md_to_flowables(md_text, styles):
    flowables = []
    lines = md_text.split("\n")
    i = 0
    in_code_block = False
    code_lines = []

    while i < len(lines):
        line = lines[i]

        # Code block
        if line.strip().startswith("```"):
            if in_code_block:
                code = "\n".join(code_lines)
                flowables.append(Preformatted(code, styles["code"]))
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Strip image markdown
        line = re.sub(r"!\[.*?\]\(.*?\)\{.*?\}", "", line).strip()
        line = re.sub(r"!\[.*?\]\(.*?\)", "", line).strip()

        # Headings
        if line.startswith("### "):
            text = escape_xml(line[4:].strip())
            flowables.append(Paragraph(text, styles["h3"]))
        elif line.startswith("## "):
            text = escape_xml(line[3:].strip())
            flowables.append(Paragraph(text, styles["h2"]))
        elif line.startswith("# "):
            text = escape_xml(line[2:].strip())
            flowables.append(Spacer(1, 6))
            flowables.append(Paragraph(text, styles["h1"]))
            flowables.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#003366"), spaceAfter=8))

        # Bullet points
        elif line.startswith("* ") or line.startswith("- "):
            text = line[2:].strip()
            # Convert inline code
            text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', escape_xml(text))
            # Convert bold
            text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
            # Convert links
            text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
            flowables.append(Paragraph(f"• {text}", styles["bullet"]))

        # Horizontal rule
        elif line.strip() in ("---", "***", "___"):
            flowables.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceAfter=6))

        # Table rows - simplified rendering
        elif line.strip().startswith("|") and "|" in line:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            row_text = " | ".join(escape_xml(c) for c in cells if c and not re.match(r"^[-:]+$", c))
            if row_text:
                flowables.append(Paragraph(row_text, styles["body"]))

        # Normal paragraph
        elif line.strip():
            text = line.strip()
            text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', escape_xml(text))
            text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
            text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
            text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
            flowables.append(Paragraph(text, styles["body"]))

        else:
            if flowables and not isinstance(flowables[-1], Spacer):
                flowables.append(Spacer(1, 4))

        i += 1

    return flowables

def main():
    styles = build_styles()
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=inch,
        bottomMargin=inch,
    )

    story = []

    # Cover page
    story.append(Spacer(1, 2 * inch))
    story.append(Paragraph("OWASP Top 10", styles["title"]))
    story.append(Paragraph("2025 Edition", styles["subtitle"]))
    story.append(HRFlowable(width="80%", thickness=2, color=colors.HexColor("#003366"), spaceAfter=20))
    story.append(Paragraph("Open Web Application Security Project", styles["subtitle"]))
    story.append(PageBreak())

    for filename in FILES:
        filepath = os.path.join(DOCS_DIR, filename)
        if not os.path.exists(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        flowables = parse_md_to_flowables(content, styles)
        story.extend(flowables)
        story.append(PageBreak())

    doc.build(story)
    print(f"PDF created: {OUTPUT_PDF}")

if __name__ == "__main__":
    main()
