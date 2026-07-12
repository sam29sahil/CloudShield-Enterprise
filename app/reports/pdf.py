"""
CloudShield Enterprise
Professional PDF Report Generator v2
"""

import io
import json
import html

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)


class PDFReport:

    @staticmethod
    def clean(value):

        if value is None:
            return "-"

        if isinstance(value, (dict, list)):
            try:
                value = json.dumps(value, indent=2)
            except Exception:
                value = str(value)

        value = str(value)

        value = html.escape(value)

        value = value.replace("\n", "<br/>")

        if len(value) > 1500:
            value = value[:1500] + "..."

        return value

    @staticmethod
    def section_title(story, styles, title):

        story.append(
            Paragraph(
                f"<font color='#2563eb'><b>{title}</b></font>",
                styles["Heading2"]
            )
        )

        story.append(Spacer(1, 10))

    @staticmethod
    def build_table(rows):

        table = Table(
            rows,
            colWidths=[2.2 * inch, 4.1 * inch]
        )

        table.setStyle(TableStyle([

            ("GRID", (0,0), (-1,-1), 0.4, colors.grey),

            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#2563eb")),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("BOTTOMPADDING", (0,0), (-1,-1), 7),

            ("TOPPADDING", (0,0), (-1,-1), 7),

            ("VALIGN", (0,0), (-1,-1), "TOP"),

        ]))

        return table

    @staticmethod
    def generate(scan):

        buffer = io.BytesIO()

        document = SimpleDocTemplate(
            buffer,
            leftMargin=30,
            rightMargin=30,
            topMargin=30,
            bottomMargin=30
        )

        styles = getSampleStyleSheet()

        story = []

        # ======================================
        # COVER
        # ======================================

        story.append(
            Paragraph(
                "<font size='24'><b>CloudShield Enterprise</b></font>",
                styles["Title"]
            )
        )

        story.append(
            Paragraph(
                "<font size='16'>Professional Security Assessment Report</font>",
                styles["Heading2"]
            )
        )

        story.append(Spacer(1, 25))

        cover = [
            ["Target", PDFReport.clean(scan.target)],
            ["Category", PDFReport.clean(scan.category)],
            ["Tool", PDFReport.clean(scan.tool)],
            ["Status", PDFReport.clean(scan.status)],
            ["Risk Level", PDFReport.clean(scan.risk)],
            ["Security Score", f"{scan.score}%"],
            ["Started", PDFReport.clean(scan.started_at)],
            ["Completed", PDFReport.clean(scan.completed_at)],
        ]

        story.append(PDFReport.build_table(cover))

        story.append(PageBreak())
                # ======================================
        # EXECUTIVE SUMMARY
        # ======================================

        PDFReport.section_title(
            story,
            styles,
            "Executive Summary"
        )

        summary = [
            ["Property", "Value"],
            ["Security Score", f"{scan.score}%"],
            ["Risk Level", PDFReport.clean(scan.risk)],
            ["Status", PDFReport.clean(scan.status)],
            ["Target", PDFReport.clean(scan.target)],
            ["Category", PDFReport.clean(scan.category)],
            ["Tool", PDFReport.clean(scan.tool)],
            ["Started", PDFReport.clean(scan.started_at)],
            ["Completed", PDFReport.clean(scan.completed_at)],
        ]

        story.append(
            PDFReport.build_table(summary)
        )

        story.append(Spacer(1, 20))

        # ======================================
        # LOAD PARSED DATA
        # ======================================

        try:
            parsed = json.loads(
                scan.parsed_output or "{}"
            )
        except Exception:
            parsed = {}

        if not parsed:

            story.append(
                Paragraph(
                    "No parsed scan data available.",
                    styles["BodyText"]
                )
            )

            document.build(story)

            buffer.seek(0)

            return buffer

        SKIP = {
            "html",
            "body",
            "response",
            "cookies",
            "raw_html"
        }

        SECTION_NAMES = {
            "ports": "Open Ports",
            "ssl": "SSL Information",
            "dns": "DNS Information",
            "whois": "WHOIS Information",
            "headers": "Security Headers",
            "technologies": "Technology Detection",
            "findings": "Security Findings",
            "recommendations": "Recommendations",
        }
                # ======================================
        # PARSED SECTIONS
        # ======================================

        for key, value in parsed.items():

            if key.lower() in SKIP:
                continue

            title = SECTION_NAMES.get(
                key.lower(),
                key.replace("_", " ").title()
            )

            PDFReport.section_title(
                story,
                styles,
                title
            )

            # ----------------------------
            # Dictionary
            # ----------------------------

            if isinstance(value, dict):

                rows = [["Property", "Value"]]

                for k, v in value.items():

                    rows.append([
                        PDFReport.clean(k),
                        PDFReport.clean(v)
                    ])

                story.append(
                    PDFReport.build_table(rows)
                )

            # ----------------------------
            # List
            # ----------------------------

            elif isinstance(value, list):

                rows = [["Value"]]

                if len(value) == 0:

                    rows.append([
                        "No Results"
                    ])

                else:

                    for item in value:

                        if isinstance(item, dict):

                            rows.append([
                                PDFReport.clean(
                                    json.dumps(
                                        item,
                                        indent=2
                                    )
                                )
                            ])

                        else:

                            rows.append([
                                PDFReport.clean(item)
                            ])

                table = Table(
                    rows,
                    colWidths=[6.3 * inch]
                )

                table.setStyle(TableStyle([

                    ("GRID", (0,0), (-1,-1), 0.4, colors.grey),

                    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#2563eb")),

                    ("TEXTCOLOR", (0,0), (-1,0), colors.white),

                    ("BOTTOMPADDING", (0,0), (-1,-1), 7),

                    ("TOPPADDING", (0,0), (-1,-1), 7),

                ]))

                story.append(table)

            # ----------------------------
            # Single Value
            # ----------------------------

            else:

                story.append(

                    Paragraph(

                        PDFReport.clean(value),

                        styles["BodyText"]

                    )

                )

            story.append(

                Spacer(1, 15)

            )
                    # ======================================
        # FOOTER
        # ======================================

        story.append(Spacer(1, 25))

        footer = Table(
            [
                ["CloudShield Enterprise v1.0"],
                ["Professional Security Assessment Report"],
                ["Generated Automatically"],
                ["For authorized security assessment purposes only."]
            ],
            colWidths=[6.3 * inch]
        )

        footer.setStyle(TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1f2937")),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), 0.4, colors.grey),

            ("BOTTOMPADDING", (0,0), (-1,-1), 8),

            ("TOPPADDING", (0,0), (-1,-1), 8),

            ("ALIGN", (0,0), (-1,-1), "CENTER"),

            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

        ]))

        story.append(footer)

        document.build(story)

        buffer.seek(0)

        return buffer