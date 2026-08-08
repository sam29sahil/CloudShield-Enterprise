"""
CloudShield Enterprise
Professional PDF Report Generator
"""

import io
import json
import html

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)

from app.scanner.services.report_builder import ReportBuilder


class PDFReport:
    """
    Enterprise PDF Report Generator
    """

    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._create_styles()

    # --------------------------------------------------
    # Styles
    # --------------------------------------------------

    def _create_styles(self):

        self.title_style = ParagraphStyle(
            "ReportTitle",
            parent=self.styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=24,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#2563eb"),
            spaceAfter=20,
        )

        self.subtitle_style = ParagraphStyle(
            "Subtitle",
            parent=self.styles["Heading2"],
            alignment=TA_CENTER,
            textColor=colors.HexColor("#64748b"),
            fontSize=14,
            spaceAfter=25,
        )

        self.heading = ParagraphStyle(
            "Heading",
            parent=self.styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=16,
            textColor=colors.HexColor("#2563eb"),
            spaceAfter=10,
            spaceBefore=15,
        )

        self.label = ParagraphStyle(
            "Label",
            parent=self.styles["BodyText"],
            fontName="Helvetica-Bold",
            textColor=colors.HexColor("#111827"),
        )

        self.value = ParagraphStyle(
            "Value",
            parent=self.styles["BodyText"],
            fontSize=10,
            leading=15,
        )

        self.footer = ParagraphStyle(
            "Footer",
            parent=self.styles["BodyText"],
            alignment=TA_CENTER,
            textColor=colors.grey,
            fontSize=8,
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
                value = json.dumps(value, indent=2, default=str)
            except Exception:
                value = str(value)

        value = html.escape(str(value))
        value = value.replace("\n", "<br/>")

        return value

    def heading_block(self, story, title):

        story.append(Paragraph(title, self.heading))
        story.append(Spacer(1, 8))

    def table(self, rows, widths=None):

        if widths is None:
            widths = [2.2 * inch, 4.1 * inch]

        table = Table(rows, colWidths=widths)

        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563eb")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 8),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ]
            )
        )

        return table

        # --------------------------------------------------

    # Cover Page
    # --------------------------------------------------

    def draw_cover(self, story, report):

        summary = report["summary"]

        story.append(
            Paragraph(
                "CloudShield Enterprise",
                self.title_style,
            )
        )

        story.append(
            Paragraph(
                "Professional Security Assessment Report",
                self.subtitle_style,
            )
        )

        story.append(Spacer(1, 25))

        rows = [
            ["Property", "Value"],
            ["Target", self.clean(summary.get("target"))],
            ["Scanner", self.clean(summary.get("tool"))],
            ["Category", self.clean(summary.get("category"))],
            ["Status", self.clean(summary.get("status"))],
            ["Risk", self.clean(summary.get("risk"))],
            ["Security Score", f"{summary.get('score', 0)}/100"],
            ["Started", self.clean(summary.get("started"))],
            ["Completed", self.clean(summary.get("completed"))],
            [
                "Duration",
                f"{float(summary.get('duration', 0)):.2f} seconds",
            ],
        ]

        story.append(self.table(rows))

        story.append(Spacer(1, 25))

        story.append(
            Paragraph(
                "Confidential — Generated by CloudShield Enterprise",
                self.footer,
            )
        )

        story.append(PageBreak())

    # --------------------------------------------------
    # Executive Summary
    # --------------------------------------------------

    def draw_summary(self, story, report):

        summary = report["summary"]

        self.heading_block(
            story,
            "Executive Summary",
        )

        rows = [
            ["Metric", "Value"],
            ["Security Score", f"{summary.get('score', 0)}/100"],
            ["Risk Level", self.clean(summary.get("risk"))],
            ["Status", self.clean(summary.get("status"))],
            ["Scanner", self.clean(summary.get("tool"))],
            ["Category", self.clean(summary.get("category"))],
            [
                "Duration",
                f"{float(summary.get('duration', 0)):.2f} sec",
            ],
            ["Target", self.clean(summary.get("target"))],
        ]

        story.append(self.table(rows))

        story.append(Spacer(1, 20))

    # --------------------------------------------------
    # Website
    # --------------------------------------------------

    def draw_website(self, story, report):

        website = report.get("website", {})

        self.heading_block(
            story,
            "Website Analysis",
        )

        rows = [
            ["Property", "Value"],
            ["Target URL", self.clean(website.get("url"))],
            ["HTTP Status", self.clean(website.get("status_code"))],
            [
                "HTTPS",
                "Enabled" if website.get("https") else "Disabled",
            ],
            [
                "Response Time",
                self.clean(website.get("response_time")),
            ],
            [
                "Redirects",
                self.clean(website.get("redirects")),
            ],
            [
                "Server",
                self.clean(website.get("server")),
            ],
            [
                "Powered By",
                self.clean(website.get("powered_by")),
            ],
        ]

        story.append(self.table(rows))

        story.append(Spacer(1, 20))

    # --------------------------------------------------
    # HTTP Headers
    # --------------------------------------------------

    def draw_headers(self, story, report):

        headers = report.get("headers", [])

        self.heading_block(
            story,
            "Security Headers",
        )

        rows = [
            [
                "Header",
                "Status",
                "Severity",
            ]
        ]

        if headers:

            for header in headers:

                rows.append(
                    [
                        self.clean(header.get("header")),
                        self.clean(header.get("status")),
                        self.clean(header.get("severity")),
                    ]
                )

        else:

            rows.append(
                [
                    "No Headers",
                    "-",
                    "-",
                ]
            )

        table = Table(
            rows,
            colWidths=[
                3 * inch,
                1.4 * inch,
                1.4 * inch,
            ],
        )

        table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#2563eb"),
                    ),
                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        colors.white,
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.4,
                        colors.grey,
                    ),
                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        8,
                    ),
                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        8,
                    ),
                ]
            )
        )

        story.append(table)

        story.append(Spacer(1, 20))

    # --------------------------------------------------
    # SSL
    # --------------------------------------------------

    def draw_ssl(self, story, report):

        ssl = report.get("ssl", {})

        self.heading_block(
            story,
            "SSL Certificate",
        )

        rows = [
            ["Property", "Value"],
            ["Issuer", self.clean(ssl.get("issuer"))],
            ["Issued To", self.clean(ssl.get("issued_to"))],
            [
                "Certificate Valid",
                "Yes" if ssl.get("valid") else "No",
            ],
            ["Expires", self.clean(ssl.get("expires"))],
            [
                "Days Remaining",
                self.clean(ssl.get("days_left")),
            ],
        ]

        story.append(self.table(rows))

        story.append(Spacer(1, 20))

    # --------------------------------------------------
    # DNS
    # --------------------------------------------------

    def draw_dns(self, story, report):

        dns = report.get("dns", {})

        self.heading_block(
            story,
            "DNS Records",
        )

        if not dns:

            story.append(
                Paragraph(
                    "No DNS information available.",
                    self.value,
                )
            )

            story.append(Spacer(1, 20))

            return

        for record, values in dns.items():

            story.append(
                Paragraph(
                    f"<b>{record} Records</b>",
                    self.label,
                )
            )

            if isinstance(values, list):

                if values:

                    for value in values:

                        story.append(
                            Paragraph(
                                f"• {self.clean(value)}",
                                self.value,
                            )
                        )

                else:

                    story.append(
                        Paragraph(
                            "No Records",
                            self.value,
                        )
                    )

            else:

                story.append(
                    Paragraph(
                        self.clean(values),
                        self.value,
                    )
                )

            story.append(Spacer(1, 8))

        story.append(Spacer(1, 20))

        # --------------------------------------------------

    # WHOIS
    # --------------------------------------------------

    def draw_whois(self, story, report):

        whois = report.get("whois", {})

        self.heading_block(story, "WHOIS Information")

        if not whois:
            story.append(
                Paragraph(
                    "WHOIS information unavailable.",
                    self.value,
                )
            )
            story.append(Spacer(1, 20))
            return

        rows = [["Property", "Value"]]

        for key, value in whois.items():
            rows.append(
                [
                    key.replace("_", " ").title(),
                    self.clean(value),
                ]
            )

        story.append(self.table(rows))
        story.append(Spacer(1, 20))

    # --------------------------------------------------
    # Technology
    # --------------------------------------------------

    def draw_technology(self, story, report):

        technologies = report.get("technology", [])

        self.heading_block(
            story,
            "Technology Detection",
        )

        if not technologies:

            story.append(
                Paragraph(
                    "No technologies detected.",
                    self.value,
                )
            )

        else:

            for tech in technologies:

                story.append(
                    Paragraph(
                        f"• {self.clean(tech)}",
                        self.value,
                    )
                )

        story.append(Spacer(1, 20))

    # --------------------------------------------------
    # Ports
    # --------------------------------------------------

    def draw_ports(self, story, report):

        ports = report.get("ports", [])

        self.heading_block(
            story,
            "Open Ports",
        )

        rows = [
            [
                "Port",
                "Protocol",
                "Service",
                "State",
            ]
        ]

        if not ports:

            rows.append(
                [
                    "No Open Ports",
                    "-",
                    "-",
                    "-",
                ]
            )

        else:

            for port in ports:

                rows.append(
                    [
                        self.clean(port.get("port")),
                        self.clean(port.get("protocol")),
                        self.clean(port.get("service")),
                        self.clean(port.get("status")),
                    ]
                )

        table = Table(
            rows,
            colWidths=[
                1 * inch,
                1.4 * inch,
                2.2 * inch,
                1.3 * inch,
            ],
        )

        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563eb")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 8),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ]
            )
        )

        story.append(table)
        story.append(Spacer(1, 20))

    # --------------------------------------------------
    # Findings
    # --------------------------------------------------

    def draw_findings(self, story, report):

        findings = report.get("findings", [])

        self.heading_block(
            story,
            "Security Findings",
        )

        if not findings:

            story.append(
                Paragraph(
                    "No security findings detected.",
                    self.value,
                )
            )

            story.append(Spacer(1, 20))
            return

        for finding in findings:

            rows = [
                ["Severity", self.clean(finding.get("severity"))],
                ["Title", self.clean(finding.get("title"))],
                ["Status", self.clean(finding.get("status"))],
                ["CVSS", self.clean(finding.get("cvss"))],
                ["CWE", self.clean(finding.get("cwe"))],
                ["OWASP", self.clean(finding.get("owasp"))],
                ["Description", self.clean(finding.get("description"))],
                ["Evidence", self.clean(finding.get("evidence"))],
            ]

            story.append(self.table(rows))
            story.append(Spacer(1, 15))

    # --------------------------------------------------
    # Recommendations
    # --------------------------------------------------

    def draw_recommendations(self, story, report):

        recommendations = report.get("recommendations", [])

        self.heading_block(
            story,
            "Recommendations",
        )

        if not recommendations:

            story.append(
                Paragraph(
                    "No recommendations available.",
                    self.value,
                )
            )

            story.append(Spacer(1, 20))
            return

        for item in recommendations:

            rows = [
                ["Issue", self.clean(item.get("title"))],
                ["Severity", self.clean(item.get("severity"))],
                [
                    "Recommendation",
                    self.clean(item.get("recommendation")),
                ],
                ["Evidence", self.clean(item.get("evidence"))],
            ]

            story.append(self.table(rows))
            story.append(Spacer(1, 15))

    # --------------------------------------------------
    # Appendix
    # --------------------------------------------------

    def draw_appendix(self, story, report):

        self.heading_block(
            story,
            "Appendix",
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

        story.append(self.table(rows))
        story.append(Spacer(1, 20))

    # --------------------------------------------------
    # Raw Output
    # --------------------------------------------------

    def draw_raw_output(self, story, report):

        self.heading_block(
            story,
            "Raw Scan Output",
        )

        raw = dict(report.get("raw", {}))

        for key in [
            "html",
            "body",
            "response",
            "cookies",
            "raw_html",
        ]:
            raw.pop(key, None)

        text = json.dumps(
            raw,
            indent=2,
            default=str,
        )

        if len(text) > 8000:
            text = text[:8000] + "\n\n... Output Truncated ..."

        story.append(
            Paragraph(
                "<font face='Courier'>" + self.clean(text) + "</font>",
                self.value,
            )
        )

        story.append(Spacer(1, 20))

    # --------------------------------------------------
    # Footer
    # --------------------------------------------------

    def draw_footer(self, canvas, doc):

        canvas.saveState()

        width, _ = doc.pagesize

        canvas.setFont("Helvetica", 9)
        canvas.setFillColor(colors.grey)

        canvas.drawString(
            30,
            20,
            "CloudShield Enterprise v1.0",
        )

        canvas.drawRightString(
            width - 30,
            20,
            f"Page {canvas.getPageNumber()}",
        )

        canvas.restoreState()


    # --------------------------------------------------
    # Cloud / Azure Security Report
    # --------------------------------------------------

    def draw_cloud(self, story, report):

        # Azure data can arrive from ReportBuilder in different shapes.
        # Prefer the explicit cloud/azure section, then fall back to
        # the top-level Azure fields, and finally the raw scan output.

        cloud = report.get("cloud")

        if not isinstance(cloud, dict):
            cloud = report.get("azure")

        if not isinstance(cloud, dict):
            cloud = {}

        # If ReportBuilder did not create a dedicated cloud/azure block,
        # collect the Azure Basic ReportGenerator fields from the report.
        if not cloud:

            azure_keys = {
                "provider",
                "report_type",
                "scanner",
                "summary",
                "executive_summary",
                "score",
                "security_score",
                "risk",
                "risk_level",
                "inventory",
                "inventory_summary",
                "findings",
                "total_findings",
                "severity",
                "recommendations",
                "recommendation_count",
                "status",
            }

            cloud = {
                key: report[key]
                for key in azure_keys
                if key in report
            }

        # Some ReportBuilder versions keep the original Azure scan result
        # inside raw. Extract it when the normalized fields are unavailable.
        raw = report.get("raw", {})

        if isinstance(raw, dict):

            raw_cloud = raw.get("cloud")

            if not isinstance(raw_cloud, dict):
                raw_cloud = raw.get("azure")

            if isinstance(raw_cloud, dict):

                merged = dict(raw_cloud)
                merged.update(cloud)
                cloud = merged

            else:

                # Azure Basic ReportGenerator may have returned its data
                # directly inside raw.
                raw_azure_keys = {
                    "provider",
                    "report_type",
                    "scanner",
                    "security_score",
                    "risk_level",
                    "inventory",
                    "inventory_summary",
                    "findings",
                    "recommendations",
                    "status",
                }

                for key in raw_azure_keys:
                    if key not in cloud and key in raw:
                        cloud[key] = raw[key]

        if not isinstance(cloud, dict):
            cloud = {}

        self.heading_block(
            story,
            "Cloud Security Assessment",
        )

        rows = [
            ["Property", "Value"],
            [
                "Provider",
                self.clean(
                    cloud.get(
                        "provider",
                        "Microsoft Azure",
                    )
                ),
            ],
            [
                "Security Score",
                f"{cloud.get('security_score', cloud.get('score', 0))}/100",
            ],
            [
                "Risk Level",
                self.clean(
                    cloud.get(
                        "risk_level",
                        cloud.get(
                            "risk",
                            "Unknown",
                        ),
                    )
                ),
            ],
            [
                "Status",
                self.clean(
                    cloud.get(
                        "status",
                        "Completed",
                    )
                ),
            ],
        ]

        story.append(self.table(rows))
        story.append(Spacer(1, 20))

        # ------------------------------------------
        # Azure Resource Inventory
        # ------------------------------------------

        self.heading_block(
            story,
            "Azure Resource Inventory",
        )

        inventory_summary = cloud.get(
            "inventory_summary",
            {},
        )

        if not isinstance(inventory_summary, dict):
            inventory_summary = {}

        # Build a basic inventory summary if the scanner supplied only
        # the full inventory.
        if not inventory_summary:

            inventory = cloud.get(
                "inventory",
                {},
            )

            if isinstance(inventory, dict):

                def count_items(value):
                    if isinstance(value, list):
                        return len(value)

                    if isinstance(value, dict):
                        data = value.get("data")

                        if isinstance(data, list):
                            return len(data)

                        if isinstance(value.get("count"), int):
                            return value["count"]

                    return 0

                network = inventory.get(
                    "network",
                    {},
                )

                if not isinstance(network, dict):
                    network = {}

                inventory_summary = {
                    "resource_groups": count_items(
                        inventory.get("resource_groups")
                    ),
                    "virtual_machines": count_items(
                        inventory.get("virtual_machines")
                    ),
                    "virtual_networks": count_items(
                        network.get("virtual_networks")
                    ),
                    "subnets": count_items(
                        network.get("subnets")
                    ),
                    "network_security_groups": count_items(
                        network.get("network_security_groups")
                    ),
                    "network_interfaces": count_items(
                        network.get("network_interfaces")
                    ),
                    "keyvaults": count_items(
                        inventory.get("keyvault")
                    ),
                    "defender": inventory.get(
                        "defender",
                        {},
                    ),
                }

        rows = [
            ["Resource", "Count"],
            [
                "Resource Groups",
                self.clean(
                    inventory_summary.get(
                        "resource_groups",
                        0,
                    )
                ),
            ],
            [
                "Virtual Machines",
                self.clean(
                    inventory_summary.get(
                        "virtual_machines",
                        0,
                    )
                ),
            ],
            [
                "Virtual Networks",
                self.clean(
                    inventory_summary.get(
                        "virtual_networks",
                        0,
                    )
                ),
            ],
            [
                "Subnets",
                self.clean(
                    inventory_summary.get(
                        "subnets",
                        0,
                    )
                ),
            ],
            [
                "Network Security Groups",
                self.clean(
                    inventory_summary.get(
                        "network_security_groups",
                        0,
                    )
                ),
            ],
            [
                "Network Interfaces",
                self.clean(
                    inventory_summary.get(
                        "network_interfaces",
                        0,
                    )
                ),
            ],
            [
                "Key Vaults",
                self.clean(
                    inventory_summary.get(
                        "keyvaults",
                        0,
                    )
                ),
            ],
        ]

        story.append(self.table(rows))
        story.append(Spacer(1, 20))

        # ------------------------------------------
        # Defender
        # ------------------------------------------

        defender = inventory_summary.get(
            "defender",
            {},
        )

        if not isinstance(defender, dict):
            defender = {}

        self.heading_block(
            story,
            "Microsoft Defender",
        )

        rows = [
            ["Property", "Value"],
            [
                "Secure Score",
                self.clean(
                    defender.get(
                        "secure_score",
                        0,
                    )
                ),
            ],
            [
                "Active Alerts",
                self.clean(
                    defender.get(
                        "alerts",
                        0,
                    )
                ),
            ],
            [
                "Recommendations",
                self.clean(
                    defender.get(
                        "recommendations",
                        0,
                    )
                ),
            ],
        ]

        story.append(self.table(rows))
        story.append(Spacer(1, 20))

        # ------------------------------------------
        # Cloud Findings
        # ------------------------------------------

        self.heading_block(
            story,
            "Cloud Security Findings",
        )

        findings = cloud.get(
            "findings",
            [],
        )

        if not isinstance(findings, list):
            findings = []

        if not findings:

            story.append(
                Paragraph(
                    "No cloud security findings detected.",
                    self.value,
                )
            )

        else:

            for finding in findings:

                if not isinstance(finding, dict):
                    continue

                rows = [
                    [
                        "Severity",
                        self.clean(
                            finding.get(
                                "severity",
                                "Info",
                            )
                        ),
                    ],
                    [
                        "Rule ID",
                        self.clean(
                            finding.get(
                                "rule_id",
                                "",
                            )
                        ),
                    ],
                    [
                        "Category",
                        self.clean(
                            finding.get(
                                "category",
                                "Azure",
                            )
                        ),
                    ],
                    [
                        "Resource",
                        self.clean(
                            finding.get(
                                "resource",
                                finding.get(
                                    "resource_name",
                                    "Unknown",
                                ),
                            )
                        ),
                    ],
                    [
                        "Title",
                        self.clean(
                            finding.get(
                                "title",
                                "Azure Security Finding",
                            )
                        ),
                    ],
                    [
                        "Description",
                        self.clean(
                            finding.get(
                                "description",
                                "",
                            )
                        ),
                    ],
                    [
                        "Recommendation",
                        self.clean(
                            finding.get(
                                "recommendation",
                                "",
                            )
                        ),
                    ],
                    [
                        "Evidence",
                        self.clean(
                            finding.get(
                                "evidence",
                                finding.get(
                                    "metadata",
                                    {},
                                ),
                            )
                        ),
                    ],
                ]

                story.append(self.table(rows))
                story.append(Spacer(1, 15))

        story.append(Spacer(1, 5))

        # ------------------------------------------
        # Cloud Recommendations
        # ------------------------------------------

        self.heading_block(
            story,
            "Cloud Recommendations",
        )

        recommendations = cloud.get(
            "recommendations",
            [],
        )

        if not isinstance(recommendations, list):
            recommendations = []

        if not recommendations:

            story.append(
                Paragraph(
                    "No cloud recommendations available.",
                    self.value,
                )
            )

        else:

            for item in recommendations:

                if isinstance(item, dict):

                    title = item.get(
                        "title",
                        "Recommendation",
                    )

                    severity = item.get(
                        "severity",
                        "",
                    )

                    recommendation = item.get(
                        "recommendation",
                        item.get(
                            "description",
                            "",
                        ),
                    )

                    evidence = item.get(
                        "evidence",
                        "",
                    )

                    rows = [
                        [
                            "Issue",
                            self.clean(title),
                        ],
                        [
                            "Severity",
                            self.clean(severity),
                        ],
                        [
                            "Recommendation",
                            self.clean(
                                recommendation
                            ),
                        ],
                        [
                            "Evidence",
                            self.clean(evidence),
                        ],
                    ]

                    story.append(self.table(rows))
                    story.append(Spacer(1, 15))

                else:

                    story.append(
                        Paragraph(
                            f"• {self.clean(item)}",
                            self.value,
                        )
                    )

        story.append(Spacer(1, 20))

        # ------------------------------------------
        # Full Azure Inventory
        # ------------------------------------------

        inventory = cloud.get(
            "inventory",
            {},
        )

        if isinstance(inventory, dict) and inventory:

            self.heading_block(
                story,
                "Azure Inventory Details",
            )

            for section_name, section_data in inventory.items():

                title = str(
                    section_name
                ).replace(
                    "_",
                    " ",
                ).title()

                story.append(
                    Paragraph(
                        f"<b>{self.clean(title)}</b>",
                        self.label,
                    )
                )

                if isinstance(section_data, list):

                    if not section_data:

                        story.append(
                            Paragraph(
                                "No resources found.",
                                self.value,
                            )
                        )

                    else:

                        for item in section_data:

                            story.append(
                                Paragraph(
                                    self.clean(item),
                                    self.value,
                                )
                            )

                            story.append(
                                Spacer(1, 5)
                            )

                elif isinstance(section_data, dict):

                    rows = [
                        ["Property", "Value"]
                    ]

                    for key, value in section_data.items():

                        rows.append(
                            [
                                self.clean(
                                    str(key)
                                    .replace(
                                        "_",
                                        " ",
                                    )
                                    .title()
                                ),
                                self.clean(value),
                            ]
                        )

                    story.append(
                        self.table(rows)
                    )

                else:

                    story.append(
                        Paragraph(
                            self.clean(section_data),
                            self.value,
                        )
                    )

                story.append(
                    Spacer(1, 12)
                )

        story.append(Spacer(1, 10))

    # --------------------------------------------------
    # Generate
    # --------------------------------------------------

    def generate(self, scan):

        report = ReportBuilder(scan).build()

        buffer = io.BytesIO()

        document = SimpleDocTemplate(
            buffer,
            leftMargin=30,
            rightMargin=30,
            topMargin=30,
            bottomMargin=30,
        )

        story = []

        # ------------------------------------------
        # Common Cover
        # ------------------------------------------

        self.draw_cover(story, report)
        self.draw_summary(story, report)

        # ------------------------------------------
        # Detect Scan Type
        # ------------------------------------------

        summary = report.get(
            "summary",
            {},
        )

        if not isinstance(summary, dict):
            summary = {}

        category = str(
            summary.get(
                "category",
                "",
            )
        ).lower()

        tool = str(
            summary.get(
                "tool",
                "",
            )
        ).lower()

        target = str(
            summary.get(
                "target",
                "",
            )
        ).lower()

        is_cloud = (
            category in {
                "cloud",
                "azure",
                "aws",
                "gcp",
            }
            or "cloud" in category
            or "azure" in category
            or "azure" in tool
            or target.startswith("azure:")
            or "microsoft azure" in target
            or isinstance(
                report.get("cloud"),
                dict,
            )
            or isinstance(
                report.get("azure"),
                dict,
            )
        )

        # ------------------------------------------
        # Cloud / Azure Report
        # ------------------------------------------

        if is_cloud:

            self.draw_cloud(
                story,
                report,
            )

        # ------------------------------------------
        # Normal Basic / Website Report
        # ------------------------------------------

        else:

            self.draw_website(
                story,
                report,
            )

            self.draw_headers(
                story,
                report,
            )

            self.draw_ssl(
                story,
                report,
            )

            self.draw_dns(
                story,
                report,
            )

            self.draw_whois(
                story,
                report,
            )

            self.draw_technology(
                story,
                report,
            )

            self.draw_ports(
                story,
                report,
            )

        # ------------------------------------------
        # Common Security Sections
        # ------------------------------------------

        self.draw_findings(
            story,
            report,
        )

        self.draw_recommendations(
            story,
            report,
        )

        self.draw_appendix(
            story,
            report,
        )

        self.draw_raw_output(
            story,
            report,
        )

        # ------------------------------------------
        # Build PDF
        # ------------------------------------------

        document.build(
            story,
            onFirstPage=self.draw_footer,
            onLaterPages=self.draw_footer,
        )

        buffer.seek(0)

        return buffer
    
