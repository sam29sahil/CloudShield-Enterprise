"""
CloudShield Enterprise
Enterprise Report Builder
"""

import json


class ReportBuilder:

    def __init__(self, scan):

        self.scan = scan

        try:
            parsed = getattr(scan, "parsed_output", None)

            if parsed:
                self.data = json.loads(parsed)
            else:
                self.data = {}

        except Exception:
            self.data = {}

        if not isinstance(self.data, dict):
            self.data = {}

    # ----------------------------------------------------
    # Main Report
    # ----------------------------------------------------

    def build(self):

        report = {
            "summary": self.summary(),

            "website": self.website(),

            "headers": self.headers(),

            "ssl": self.ssl(),

            "dns": self.dns(),

            "whois": self.whois(),

            "technology": self.technology(),

            "ports": self.ports(),

            "findings": self.findings(),

            "recommendations": self.recommendations(),

            "raw": self.raw(),
        }

        # ------------------------------------------------
        # Cloud / Azure
        # ------------------------------------------------

        cloud = self.cloud()

        if cloud:
            report["cloud"] = cloud

        return report

    # ----------------------------------------------------
    # Summary
    # ----------------------------------------------------

    def summary(self):

        return {
            "target": getattr(self.scan, "target", ""),
            "tool": getattr(self.scan, "tool", ""),
            "category": getattr(self.scan, "category", ""),
            "status": getattr(self.scan, "status", ""),
            "score": getattr(self.scan, "score", 0),
            "risk": getattr(self.scan, "risk", ""),
            "duration": getattr(self.scan, "duration", 0),
            "started": getattr(self.scan, "started_at", None),
            "completed": getattr(self.scan, "completed_at", None),
        }

    # ----------------------------------------------------
    # Website
    # ----------------------------------------------------

    def website(self):

        return self.data.get(
            "website",
            {},
        )

    # ----------------------------------------------------
    # Headers
    # ----------------------------------------------------

    def headers(self):

        headers = self.data.get(
            "headers",
            {},
        )

        if isinstance(headers, dict):

            return headers.get(
                "analysis",
                [],
            )

        return headers

    # ----------------------------------------------------
    # SSL
    # ----------------------------------------------------

    def ssl(self):

        return self.data.get(
            "ssl",
            {},
        )

    # ----------------------------------------------------
    # DNS
    # ----------------------------------------------------

    def dns(self):

        return self.data.get(
            "dns",
            {},
        )

    # ----------------------------------------------------
    # WHOIS
    # ----------------------------------------------------

    def whois(self):

        return self.data.get(
            "whois",
            {},
        )

    # ----------------------------------------------------
    # Technology
    # ----------------------------------------------------

    def technology(self):

        tech = self.data.get(
            "technology",
            {},
        )

        if isinstance(tech, dict):

            return tech.get(
                "technologies",
                [],
            )

        return tech

    # ----------------------------------------------------
    # Ports
    # ----------------------------------------------------

    def ports(self):

        ports = self.data.get(
            "ports",
            [],
        )

        if ports is None:
            return []

        return ports

    # ----------------------------------------------------
    # Findings
    # ----------------------------------------------------

    def findings(self):

        items = []

        if not hasattr(self.scan, "findings"):
            return items

        for finding in self.scan.findings:

            items.append(
                {
                    "id": getattr(
                        finding,
                        "id",
                        None,
                    ),

                    "title": getattr(
                        finding,
                        "title",
                        "",
                    ),

                    "severity": getattr(
                        finding,
                        "severity",
                        "",
                    ),

                    "description": getattr(
                        finding,
                        "description",
                        "",
                    ),

                    "recommendation": getattr(
                        finding,
                        "recommendation",
                        "",
                    ),

                    "evidence": getattr(
                        finding,
                        "evidence",
                        "",
                    ),

                    "cvss": getattr(
                        finding,
                        "cvss",
                        "",
                    ),

                    "cwe": getattr(
                        finding,
                        "cwe",
                        "",
                    ),

                    "owasp": getattr(
                        finding,
                        "owasp",
                        "",
                    ),

                    "reference": getattr(
                        finding,
                        "reference",
                        "",
                    ),

                    "status": getattr(
                        finding,
                        "status",
                        "",
                    ),

                    "asset_id": getattr(
                        finding,
                        "asset_id",
                        "",
                    ),

                    "scan_id": getattr(
                        finding,
                        "scan_id",
                        "",
                    ),
                }
            )

        return items

    # ----------------------------------------------------
    # Recommendations
    # ----------------------------------------------------

    def recommendations(self):

        # Azure scanner already provides recommendations
        # directly in parsed_output.

        cloud_recommendations = self.data.get(
            "recommendations"
        )

        if isinstance(
            cloud_recommendations,
            list,
        ):
            return cloud_recommendations

        items = []

        if not hasattr(self.scan, "findings"):
            return items

        for finding in self.scan.findings:

            items.append(
                {
                    "title": getattr(
                        finding,
                        "title",
                        "",
                    ),

                    "severity": getattr(
                        finding,
                        "severity",
                        "",
                    ),

                    "recommendation": getattr(
                        finding,
                        "recommendation",
                        "",
                    ),

                    "evidence": getattr(
                        finding,
                        "evidence",
                        "",
                    ),

                    "reference": getattr(
                        finding,
                        "reference",
                        "",
                    ),
                }
            )

        return items

    # ----------------------------------------------------
    # Cloud / Azure
    # ----------------------------------------------------

    def cloud(self):

        # Only create the Cloud section when this is
        # actually a cloud/Azure scan.

        category = str(
            getattr(
                self.scan,
                "category",
                "",
            )
        ).lower()

        tool = str(
            getattr(
                self.scan,
                "tool",
                "",
            )
        ).lower()

        is_cloud = (
            category == "cloud"
            or "azure" in tool
            or "azure" in str(
                self.data.get(
                    "provider",
                    ""
                )
            ).lower()
            or "azure" in str(
                self.data.get(
                    "scanner",
                    ""
                )
            ).lower()
        )

        if not is_cloud:
            return {}

        # -----------------------------------------------
        # Score
        # -----------------------------------------------

        score_data = self.data.get(
            "score",
            {},
        )

        if not isinstance(
            score_data,
            dict,
        ):
            score_data = {}

        security_score = score_data.get(
            "security_score",
            getattr(
                self.scan,
                "score",
                0,
            ),
        )

        # -----------------------------------------------
        # Risk
        # -----------------------------------------------

        risk_data = self.data.get(
            "risk",
            {},
        )

        if not isinstance(
            risk_data,
            dict,
        ):
            risk_data = {}

        risk_level = risk_data.get(
            "risk_level",
            getattr(
                self.scan,
                "risk",
                "Unknown",
            ),
        )

        # -----------------------------------------------
        # Inventory
        # -----------------------------------------------

        inventory = self.data.get(
            "inventory",
            {},
        )

        if not isinstance(
            inventory,
            dict,
        ):
            inventory = {}

        # -----------------------------------------------
        # Resource Groups
        # -----------------------------------------------

        resource_groups = inventory.get(
            "resource_groups",
            [],
        )

        if not isinstance(
            resource_groups,
            list,
        ):
            resource_groups = []

        # -----------------------------------------------
        # Virtual Machines
        # -----------------------------------------------

        virtual_machines = inventory.get(
            "virtual_machines",
            [],
        )

        if not isinstance(
            virtual_machines,
            list,
        ):
            virtual_machines = []

        # -----------------------------------------------
        # Network
        # -----------------------------------------------

        network = inventory.get(
            "network",
            {},
        )

        if not isinstance(
            network,
            dict,
        ):
            network = {}

        virtual_networks = network.get(
            "virtual_networks",
            [],
        )

        subnets = network.get(
            "subnets",
            [],
        )

        network_security_groups = network.get(
            "network_security_groups",
            [],
        )

        network_interfaces = network.get(
            "network_interfaces",
            [],
        )

        if not isinstance(
            virtual_networks,
            list,
        ):
            virtual_networks = []

        if not isinstance(
            subnets,
            list,
        ):
            subnets = []

        if not isinstance(
            network_security_groups,
            list,
        ):
            network_security_groups = []

        if not isinstance(
            network_interfaces,
            list,
        ):
            network_interfaces = []

        # -----------------------------------------------
        # Key Vault
        # -----------------------------------------------

        keyvault = inventory.get(
            "keyvault",
            [],
        )

        if not isinstance(
            keyvault,
            list,
        ):
            keyvault = []

        # -----------------------------------------------
        # Defender
        # -----------------------------------------------

        defender = inventory.get(
            "defender",
            {},
        )

        if not isinstance(
            defender,
            dict,
        ):
            defender = {}

        # -----------------------------------------------
        # Findings
        # -----------------------------------------------

        findings = self.data.get(
            "findings",
            [],
        )

        if not isinstance(
            findings,
            list,
        ):
            findings = []

        # -----------------------------------------------
        # Recommendations
        # -----------------------------------------------

        recommendations = self.data.get(
            "recommendations",
            [],
        )

        if not isinstance(
            recommendations,
            list,
        ):
            recommendations = []

        # -----------------------------------------------
        # Summary
        # -----------------------------------------------

        summary = self.data.get(
            "summary",
            {},
        )

        if not isinstance(
            summary,
            dict,
        ):
            summary = {}

        # -----------------------------------------------
        # Return normalized Cloud report
        # -----------------------------------------------

        return {
            "provider": self.data.get(
                "provider",
                "Microsoft Azure",
            ),

            "report_type": self.data.get(
                "report_type",
                "Azure Basic Security Assessment",
            ),

            "scanner": self.data.get(
                "scanner",
                getattr(
                    self.scan,
                    "tool",
                    "azure_basic_security_scan",
                ),
            ),

            "security_score": security_score,

            "score": security_score,

            "risk_level": risk_level,

            "risk": risk_level,

            "status": getattr(
                self.scan,
                "status",
                "Completed",
            ),

            "summary": summary,

            "inventory": inventory,

            "inventory_summary": {
                "resource_groups": len(
                    resource_groups
                ),

                "virtual_machines": len(
                    virtual_machines
                ),

                "virtual_networks": len(
                    virtual_networks
                ),

                "subnets": len(
                    subnets
                ),

                "network_security_groups": len(
                    network_security_groups
                ),

                "network_interfaces": len(
                    network_interfaces
                ),

                "key_vaults": len(
                    keyvault
                ),

                "defender": defender,
            },

            "resource_groups": resource_groups,

            "virtual_machines": virtual_machines,

            "virtual_networks": virtual_networks,

            "subnets": subnets,

            "network_security_groups": network_security_groups,

            "network_interfaces": network_interfaces,

            "keyvault": keyvault,

            "key_vaults": keyvault,

            "defender": defender,

            "findings": findings,

            "total_findings": len(
                findings
            ),

            "recommendations": recommendations,

            "recommendation_count": len(
                recommendations
            ),
        }

    # ----------------------------------------------------
    # Raw Output
    # ----------------------------------------------------

    def raw(self):

        return self.data