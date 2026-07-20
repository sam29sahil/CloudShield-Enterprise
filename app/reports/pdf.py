"""
CloudShield Enterprise
Professional PDF Report Generator v3
"""

import io
import json
import html

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    KeepTogether
)

from app.scanner.services.report_builder import ReportBuilder


class PDFReport:

    def __init__(self):

        self.styles = getSampleStyleSheet()

        self._create_styles()

    # --------------------------------------------------
    # Enterprise Styles
    # --------------------------------------------------

    def _create_styles(self):

        self.title_style = ParagraphStyle(

            "ReportTitle",

            parent=self.styles["Title"],

            fontName="Helvetica-Bold",

            fontSize=26,

            alignment=TA_CENTER,

            textColor=colors.HexColor("#1d4ed8"),

            spaceAfter=20

        )

        self.subtitle_style = ParagraphStyle(

            "Subtitle",

            parent=self.styles["Heading2"],

            alignment=TA_CENTER,

            textColor=colors.HexColor("#475569"),

            fontSize=14,

            spaceAfter=25

        )

        self.heading = ParagraphStyle(

            "Heading",

            parent=self.styles["Heading2"],

            fontName="Helvetica-Bold",

            textColor=colors.HexColor("#2563eb"),

            fontSize=17,

            spaceAfter=12,

            spaceBefore=20

        )

        self.label = ParagraphStyle(

            "Label",

            parent=self.styles["BodyText"],

            fontName="Helvetica-Bold",

            textColor=colors.HexColor("#111827")

        )

        self.value = ParagraphStyle(

            "Value",

            parent=self.styles["BodyText"],

            fontSize=10,

            leading=16

        )

        self.footer = ParagraphStyle(

            "Footer",

            parent=self.styles["BodyText"],

            alignment=TA_CENTER,

            textColor=colors.grey,

            fontSize=9

        )

    # --------------------------------------------------
    # Utilities
    # --------------------------------------------------

    @staticmethod
    def clean(value):

        if value is None:

            return "Not Available"

        if value == "":

            return "Not Available"

        if isinstance(value, (dict, list)):

            try:

                value = json.dumps(

                    value,

                    indent=2,

                    default=str

                )

            except Exception:

                value = str(value)

        value = html.escape(str(value))

        value = value.replace("\n", "<br/>")

        return value

    # --------------------------------------------------

    def heading_block(self, story, title):

        story.append(

            Paragraph(

                title,

                self.heading

            )

        )

        story.append(

            Spacer(

                1,

                8

            )

        )

    # --------------------------------------------------

    def table(self, rows, widths=None):

        if widths is None:

            widths = [

                2.2 * inch,

                4.1 * inch

            ]

        table = Table(

            rows,

            colWidths=widths

        )

        table.setStyle(TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#2563eb")),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), .4, colors.grey),

            ("BOTTOMPADDING", (0,0), (-1,-1), 8),

            ("TOPPADDING", (0,0), (-1,-1), 8),

            ("VALIGN", (0,0), (-1,-1), "TOP"),

            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

        ]))

        return table

    # --------------------------------------------------
    # Cover Page
    # --------------------------------------------------

    def draw_cover(

        self,

        story,

        report

    ):

        summary = report["summary"]

        story.append(

            Paragraph(

                "CloudShield Enterprise",

                self.title_style

            )

        )

        story.append(

            Paragraph(

                "Professional Security Assessment Report",

                self.subtitle_style

            )

        )

        story.append(

            Spacer(

                1,

                30

            )

        )

        rows = [

            [

                "Property",

                "Value"

            ],

            [

                "Target",

                self.clean(summary["target"])

            ],

            [

                "Scanner",

                self.clean(summary["tool"])

            ],

            [

                "Category",

                self.clean(summary["category"])

            ],

            [

                "Status",

                self.clean(summary["status"])

            ],

            [

                "Risk",

                self.clean(summary["risk"])

            ],

            [

                "Security Score",

                f'{summary["score"]}/100'

            ],

            [

                "Started",

                self.clean(summary["started"])

            ],

            [

                "Completed",

                self.clean(summary["completed"])

            ],

            [

                "Duration",

                 f'{float(summary.get("duration", 0)):.2f} seconds'
            ]

        ]

        story.append(

            self.table(rows)

        )

        story.append(

            Spacer(

                1,

                25

            )

        )

        story.append(

            Paragraph(

                "Confidential - Generated by CloudShield Enterprise",

                self.footer

            )

        )

        story.append(

            PageBreak()

        )
    def draw_summary(self, story, report):

        summary = report["summary"]

        self.heading_block(
            story,
            "Executive Summary"
        )

        rows = [

            ["Metric", "Value"],

            ["Security Score", f'{summary["score"]}/100'],

            ["Risk Level", self.clean(summary["risk"])],

            ["Scan Status", self.clean(summary["status"])],

            ["Scanner", self.clean(summary["tool"])],

            ["Category", self.clean(summary["category"])],

            ["Duration", f'{float(summary.get("duration",0)):.2f} sec'],

            ["Target", self.clean(summary["target"])]

        ]

        story.append(self.table(rows))

        story.append(Spacer(1,20))    

    def draw_website(self, story, report):

        website = report.get("website", {})

        self.heading_block(
            story,
            "Website Analysis"
        )

        rows = [

            ["Property","Value"],

            ["Target URL", self.clean(website.get("url"))],

            ["HTTP Status", self.clean(website.get("status_code"))],

            ["HTTPS", "Enabled" if website.get("https") else "Disabled"],

            ["Response Time", self.clean(website.get("response_time"))],

            ["Redirects", self.clean(website.get("redirects"))],

            ["Server", self.clean(website.get("server"))],

            ["Powered By", self.clean(website.get("powered_by"))],

        ]

        story.append(self.table(rows))

        story.append(Spacer(1,20))

    def draw_headers(self, story, report):

        headers = report.get("headers", [])

        self.heading_block(
            story,
            "Security Headers"
        )

        rows = [

            ["Header","Status","Risk"]

        ]

        rows = [["Header", "Status", "Severity"]]

        if headers:

            for h in headers:

                rows.append([

                    self.clean(h.get("header")),

                self.clean(h.get("status")),

                    self.clean(h.get("severity"))

                ])

        else:

            rows.append([

                "No Headers",

                "-",

                "-"

            ])
        

        table = Table(

            rows,

            colWidths=[3*inch,1.4*inch,1.4*inch]

        )

        table.setStyle(TableStyle([

            ("GRID",(0,0),(-1,-1),0.4,colors.grey),

            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#2563eb")),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8),

        ]))

        story.append(table)

        story.append(Spacer(1,20))

    def draw_ssl(self, story, report):

        ssl = report.get("ssl", {})

        self.heading_block(
            story,
            "SSL Certificate"
        )

        rows = [

            ["Property", "Value"],

            ["Issuer", self.clean(ssl.get("issuer"))],

            ["Issued To", self.clean(ssl.get("issued_to"))],

            ["Certificate Valid", "Yes" if ssl.get("valid") else "No"],

            ["Expires", self.clean(ssl.get("expires"))],

            ["Days Remaining", self.clean(ssl.get("days_left"))],

        ]

        story.append(self.table(rows))

        story.append(Spacer(1,20))

    def draw_dns(self, story, report):

        dns = report.get("dns", {})

        self.heading_block(
            story,
            "DNS Records"
        )

        if not dns:

            story.append(
                Paragraph(
                    "No DNS information available.",
                    self.value
                )
            )

            story.append(Spacer(1, 15))

            return

        for record, values in dns.items():

            story.append(

                Paragraph(

                    f"<b>{record} Records</b>",

                    self.label

                )

            )

            if isinstance(values, list):

                if values:

                    for value in values:

                        story.append(

                            Paragraph(

                                f"• {self.clean(value)}",

                                self.value

                            )

                        )

                else:

                    story.append(

                        Paragraph(

                            "No Records",

                            self.value

                        )

                    )

            else:

                story.append(

                    Paragraph(

                        self.clean(values),

                        self.value

                    )

                )

            story.append(Spacer(1,8))

        story.append(Spacer(1,20))

    def draw_whois(self, story, report):

        whois = report.get("whois", {})

        self.heading_block(
            story,
            "WHOIS Information"
        )

        if not whois:

            story.append(

                Paragraph(

                    "WHOIS information unavailable.",

                    self.value

                )

            )

            story.append(Spacer(1,20))

            return

        rows = [

            ["Property","Value"]

        ]

        for key, value in whois.items():

            rows.append([

                key.replace("_"," ").title(),

                self.clean(value)

            ])

        story.append(

            self.table(rows)

        )

        story.append(

            Spacer(1,20)

        )

    def draw_technology(self, story, report):

        technologies = report.get(

            "technology",

            []

        )

        self.heading_block(

            story,

            "Technology Detection"

        )

        if not technologies:

            story.append(

                Paragraph(

                    "No technologies detected.",

                    self.value

                )

            )

        else:

            for tech in technologies:

                story.append(

                    Paragraph(

                        f"• {self.clean(tech)}",

                        self.value

                    )

                )

        story.append(

            Spacer(

                1,

                20

            )

        )

    def draw_ports(self, story, report):

        ports = report.get(

            "ports",

            []

        )

        self.heading_block(

            story,

            "Open Ports"

        )

        rows = [

            [

                "Port",

                "Protocol",

                "Service",

                "State"

            ]

        ]

        if not ports:

            rows.append(

                [

                    "No Open Ports",

                    "-",

                    "-",

                    "-"

                ]

            )

        else:

            for port in ports:

                rows.append([

                    self.clean(port.get("port")),

                    self.clean(port.get("protocol")),

                    self.clean(port.get("service")),

                    self.clean(port.get("status"))

                ])

        table = Table(

            rows,

            colWidths=[

                1*inch,

                1.4*inch,

                2.2*inch,

                1.3*inch

            ]

        )

        table.setStyle(TableStyle([

            ("GRID",(0,0),(-1,-1),0.4,colors.grey),

            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#2563eb")),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ]))

        story.append(

            table

        )

        story.append(

            Spacer(

                1,

                20

            )

        )

    def draw_findings(self, story, report):

        findings = report.get("findings", [])

        self.heading_block(
            story,
            "Security Findings"
        )

        if not findings:

            story.append(
                Paragraph(
                    "No security findings detected.",
                    self.value
                )
            )

            story.append(Spacer(1, 20))
    
            return

        for finding in findings:

            severity = self.clean(
                finding.get("severity", "Unknown")
            )

            title = self.clean(
                finding.get("title", "")
            )

            description = self.clean(
                finding.get("description", "")
            )

            evidence = self.clean(
                finding.get("evidence", "")
            )

            cvss = self.clean(
                finding.get("cvss", "")
            )

            cwe = self.clean(
                finding.get("cwe", "")
            )

            owasp = self.clean(
                finding.get("owasp", "")
            )

            status = self.clean(
                finding.get("status", "")
            )

            data = [

                ["Severity", severity],

                ["Title", title],

                ["Status", status],

                ["CVSS", cvss],

                ["CWE", cwe],

                ["OWASP", owasp],

                ["Description", description],

                ["Evidence", evidence]

            ]

            story.append(
                self.table(data)
            )

            story.append(
                Spacer(1, 15)
            )

    def draw_recommendations(self, story, report):

        recommendations = report.get("recommendations", [])

        self.heading_block(
            story,
            "Recommendations"
        )

        if not recommendations:

            story.append(
                Paragraph(
                    "No recommendations available.",
                    self.value
                )
            )

            story.append(Spacer(1, 20))
            return

        for item in recommendations:

            rows = [

                ["Issue", self.clean(item.get("title"))],

                ["Severity", self.clean(item.get("severity"))],

                ["Recommendation", self.clean(item.get("recommendation"))],

                ["Evidence", self.clean(item.get("evidence"))]

            ]

            story.append(
                self.table(rows)
            )

            story.append(
                Spacer(1, 15)
            )

    def draw_appendix(self, story, report):

        self.heading_block(
            story,
            "Appendix"
        )

        summary = report.get("summary", {})

        rows = [

            ["Field", "Value"],

            ["Generated By", "CloudShield Enterprise"],

            ["Report Version", "3.0"],

            ["Scanner", self.clean(summary.get("tool"))],

            ["Category", self.clean(summary.get("category"))],

            ["Target", self.clean(summary.get("target"))],

            ["Generated On", self.clean(summary.get("completed"))],

        ]

        story.append(
            self.table(rows)
        )

        story.append(
            Spacer(1,20)
        )    

    def draw_raw_output(self, story, report):

        self.heading_block(
            story,
            "Raw Scan Output"
        )

        raw = dict(report.get("raw", {}))

        for key in [
            "html",
            "body",
            "response",
            "cookies",
            "raw_html"
        ]:
            raw.pop(key, None)

        text = json.dumps(

            raw,

            indent=2,

            default=str

        )

        if len(text) > 8000:

            text = text[:8000] + "\n\n... Output Truncated ..."

        story.append(

            Paragraph(

                "<font face='Courier'>"

                + self.clean(text)

                + "</font>",

                self.value

            )

        )

        story.append(

            Spacer(

                1,

                20

            )

        )

    def draw_footer(self, canvas, doc):

        canvas.saveState()

        width, height = doc.pagesize    

        canvas.setFont(

            "Helvetica",

            9

        )

        canvas.setFillColor(

            colors.grey

        )

        canvas.drawString(

            30,

            20,

            "CloudShield Enterprise v1.0"

        )

        canvas.drawRightString(

           width - 30,

            20,

            f"Page {canvas.getPageNumber()}"

        )

        canvas.restoreState()


    def generate(self, scan):

        report = ReportBuilder(scan).build()

        buffer = io.BytesIO()

        document = SimpleDocTemplate(

            buffer,

            leftMargin=30,

            rightMargin=30,

            topMargin=30,

            bottomMargin=30

        )

        story = []

        self.draw_cover(

            story,

            report

        )

        self.draw_summary(

            story,

            report

        )

        self.draw_website(

            story,

            report

    )

        self.draw_headers(

            story,

            report

        )

        self.draw_ssl(

            story,

            report

        )

        self.draw_dns(

            story,

            report

    )

        self.draw_whois(

            story,

            report

        )

        self.draw_technology(

            story,

            report

        )

        self.draw_ports(

            story,

            report

        )

        self.draw_findings(

            story,

            report

        )

        self.draw_recommendations(

            story,

            report

        )

        self.draw_appendix(

            story,

            report

        )

        self.draw_raw_output(

            story,

            report

        )

        document.build(

            story,

            onFirstPage=self.draw_footer,

            onLaterPages=self.draw_footer

        )

        buffer.seek(0)

        return buffer