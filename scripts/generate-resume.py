#!/usr/bin/env python3
"""Generate assets/resume/deepak-vishwakarma-resume.pdf from on-site facts only.

Do not add employers, dates, metrics, phone numbers, or education that are
not already published on the portfolio. Requires reportlab and DejaVu Sans.

    python3 -m venv .venv && .venv/bin/pip install reportlab
    .venv/bin/python scripts/generate-resume.py
"""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "resume" / "deepak-vishwakarma-resume.pdf"

BLUE = colors.HexColor("#0078ff")
DARK = colors.HexColor("#1e1e1e")
MUTED = colors.HexColor("#4e4e4e")
RULE = colors.HexColor("#cde1f8")

FONT = "DejaVu"
FONT_BOLD = "DejaVu-Bold"


def _register_fonts() -> None:
    pdfmetrics.registerFont(TTFont(FONT, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont(FONT_BOLD, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))


def _styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Title"],
            fontName=FONT_BOLD,
            fontSize=18,
            leading=21,
            textColor=DARK,
            alignment=TA_CENTER,
            spaceAfter=2,
        ),
        "title": ParagraphStyle(
            "Role",
            parent=base["Normal"],
            fontName=FONT,
            fontSize=11,
            leading=14,
            textColor=BLUE,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName=FONT,
            fontSize=8,
            leading=11,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceAfter=2,
        ),
        "h": ParagraphStyle(
            "Section",
            parent=base["Heading2"],
            fontName=FONT_BOLD,
            fontSize=10,
            leading=13,
            textColor=BLUE,
            spaceBefore=8,
            spaceAfter=3,
            alignment=TA_LEFT,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName=FONT,
            fontSize=8.5,
            leading=11,
            textColor=DARK,
            alignment=TA_JUSTIFY,
            spaceAfter=2,
        ),
        "job": ParagraphStyle(
            "Job",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=9,
            leading=12,
            textColor=DARK,
            spaceBefore=3,
            spaceAfter=0,
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=base["Normal"],
            fontName=FONT,
            fontSize=8,
            leading=10,
            textColor=MUTED,
            spaceAfter=1,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName=FONT,
            fontSize=8.5,
            leading=11,
            textColor=DARK,
            leftIndent=0,
        ),
        "skill_label": ParagraphStyle(
            "SkillLabel",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=8,
            leading=11,
            textColor=DARK,
        ),
        "skill_body": ParagraphStyle(
            "SkillBody",
            parent=base["Normal"],
            fontName=FONT,
            fontSize=8,
            leading=11,
            textColor=DARK,
        ),
    }


def _bullets(items: list[str], style: ParagraphStyle) -> ListFlowable:
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=12, bulletColor=BLUE) for item in items],
        bulletType="bullet",
        start="•",
        leftIndent=14,
        bulletFontName=FONT,
        bulletFontSize=8,
        spaceBefore=0,
        spaceAfter=2,
    )


def build() -> None:
    _register_fonts()
    styles = _styles()
    OUT.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch,
        title="Deepak Vishwakarma — Resume",
        author="Deepak Vishwakarma",
        subject="DevOps / Platform Engineer resume (facts from https://deepakv30.github.io/)",
    )

    story: list = [
        Paragraph("Deepak Vishwakarma", styles["name"]),
        Paragraph("DevOps / Platform Engineer", styles["title"]),
        Paragraph(
            "Bengaluru, Karnataka, India · "
            '<link href="mailto:deepakv.knit@gmail.com">deepakv.knit@gmail.com</link>',
            styles["contact"],
        ),
        Paragraph(
            '<link href="https://deepakv30.github.io/">deepakv30.github.io</link> · '
            '<link href="https://www.linkedin.com/in/deepakv30/">linkedin.com/in/deepakv30</link> · '
            '<link href="https://github.com/deepakv30">github.com/deepakv30</link> · '
            '<link href="https://medium.com/@deepakv30">medium.com/@deepakv30</link>',
            styles["contact"],
        ),
        HRFlowable(width="100%", thickness=1.5, color=BLUE, spaceBefore=6, spaceAfter=2),
        Paragraph("Summary", styles["h"]),
        Paragraph(
            "DevOps / Platform Engineer at Dell Technologies. I help teams ship faster by "
            "turning fragile infra into reliable delivery paths — CI/CD, automation, and "
            "platforms developers actually want to use. Reduced system failures 50% through "
            "better platform practices. GitLab, CI/CD, Kubernetes. Based in Bengaluru.",
            styles["body"],
        ),
        Paragraph("Experience", styles["h"]),
        Paragraph("DevOps / Platform Engineer", styles["job"]),
        Paragraph("Software Engineer 2 - DevOps · Dell Technologies · Bengaluru · Jun 2019 – Present", styles["meta"]),
        _bullets(
            [
                "Administered GitLab for 200+ engineers; optimized 50+ CI/CD pipelines reducing deployment time by 65%.",
                "Implemented ArgoCD GitOps + Kubernetes (EKS) for 15+ microservices with zero-downtime releases.",
                "Embedded DevSecOps: Trivy, SonarQube &amp; OWASP scanning in pipelines; remediated 200+ critical vulnerabilities.",
                "Built Terraform IaC modules for multi-account AWS infrastructure &amp; monitoring (Prometheus/Grafana/ELK).",
                "Reduced system failures 50% through better platform practices.",
            ],
            styles["bullet"],
        ),
        Paragraph("Key Achievements", styles["h"]),
        _bullets(
            [
                "Internal award for DevOps automation excellence &amp; infrastructure optimization (2024).",
                "Reduced system failures 50%; cut CI/CD deployment time by 65% and reduced failed deploys by 80% via GitLab + ArgoCD GitOps.",
                "Embedded automated scanning (Trivy/Sonar) achieving 95%+ vulnerability remediation SLA.",
                "Active technical blogger (Medium) plus internal workshops on DevOps, Linux &amp; Kubernetes best practices.",
                "Architected GitOps platform and Terraform modules adopted across multiple teams.",
            ],
            styles["bullet"],
        ),
        Paragraph("Skills", styles["h"]),
    ]

    skill_rows = [
        ["DevOps &amp; CI/CD", "GitLab CI/CD, Jenkins, GitHub Actions, ArgoCD, Ansible, Terraform, Helm, Maven, Gradle"],
        ["Cloud &amp; Container", "AWS (EC2, S3, ECS, Lambda), Docker, Kubernetes, container orchestration, microservices"],
        ["Security &amp; Monitoring", "DevSecOps, SonarQube, Trivy, OWASP, Prometheus, Grafana, ELK Stack, APM tools"],
        ["Systems", "Linux (RHEL, Ubuntu, CentOS), shell scripting, Python, system automation, performance tuning"],
        ["Version Control", "Git, GitLab administration, GitHub, branch strategies, code review workflows"],
        ["Practices", "MLOps, AIOps, Infrastructure as Code, GitOps, observability, SRE practices"],
    ]
    skill_table = Table(
        [
            [Paragraph(label, styles["skill_label"]), Paragraph(body, styles["skill_body"])]
            for label, body in skill_rows
        ],
        colWidths=[1.45 * inch, 5.85 * inch],
    )
    skill_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ]
        )
    )
    story.append(skill_table)

    story.extend(
        [
            Paragraph("Education", styles["h"]),
            Paragraph("Bachelor’s, Electronics", styles["job"]),
            Paragraph("Kamla Nehru Institute of Technology (KNIT) · 2011 – 2015 · Grade: A+", styles["meta"]),
            Paragraph("Certifications", styles["h"]),
            _bullets(
                [
                    '<link href="https://rhtapps.redhat.com/verify?certId=240-144-576"><b>Red Hat Certified System Administrator (RHCSA)</b></link> · Red Hat · Aug 2024 – Aug 2027',
                    '<link href="https://www.credly.com/badges/1e8632c5-4215-4f98-b767-4c8fbbe5ede3"><b>Associate - Information Storage and Management v5.0</b></link> · Dell Technologies · Dec 2023',
                    '<link href="https://www.credly.com/badges/12a25f05-a244-4824-a695-18f07b0fe4b7"><b>Associate - PowerEdge v2.0</b></link> · Dell Technologies · Sep 2023',
                    '<link href="https://pwskills.com/learn/certificate/44658404-29a8-4316-a8b7-a13690e47d07"><b>Be A DevOps Pro</b></link> · iNeuron.ai · Jul 2023',
                ],
                styles["bullet"],
            ),
            Paragraph("Selected public work", styles["h"]),
            _bullets(
                [
                    '<link href="https://deepakv30.github.io/devops-mastery-guide/"><b>DevOps Mastery Guide</b></link> — hands-on path from Linux to Docker, Kubernetes, Terraform, GitHub Actions, Prometheus, and Grafana.',
                    '<link href="https://apna-hisab.ai.studio/"><b>Apna Hisab</b></link> — split trip, dinner, and flatmate expenses; settle up with UPI.',
                    "Additional demos: JS Calculator, Todo Application, Alien Invasion, Hangman — see github.com/deepakv30.",
                ],
                styles["bullet"],
            ),
        ]
    )

    def _footer(canvas, doc_):
        canvas.saveState()
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.4)
        y = 0.32 * inch
        canvas.line(doc_.leftMargin, y + 10, letter[0] - doc_.rightMargin, y + 10)
        canvas.setFont(FONT, 7)
        canvas.setFillColor(MUTED)
        canvas.drawString(
            doc_.leftMargin,
            y,
            "https://deepakv30.github.io/  ·  deepakv.knit@gmail.com",
        )
        canvas.drawRightString(letter[0] - doc_.rightMargin, y, "Page %d" % doc_.page)
        canvas.restoreState()

    doc.build(story, onFirstPage=_footer, onLaterPages=_footer)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
