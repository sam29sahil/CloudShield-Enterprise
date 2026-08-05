"""
CloudShield Enterprise
Enterprise JSON Report Export
"""

import json


class JSONReport:

    def generate(self, scan, filename):

        try:
            parsed = json.loads(scan.parsed_output or "{}")
        except Exception:
            parsed = {}

        report = {
            "metadata": {
                "generated_by": "CloudShield Enterprise",
                "report_type": "Security Assessment",
<<<<<<< HEAD
                "version": "1.0",
            },
=======
                "version": "1.0"
            },

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            "summary": {
                "target": scan.target,
                "category": scan.category,
                "tool": scan.tool,
                "status": scan.status,
                "security_score": scan.score,
                "risk": scan.risk,
                "started_at": str(scan.started_at),
<<<<<<< HEAD
                "completed_at": str(scan.completed_at),
            },
            "infrastructure": {
                "ports": parsed.get("ports", []),
                "services": parsed.get("services", []),
            },
            "ssl": parsed.get("ssl", {}),
            "dns": parsed.get("dns", {}),
            "whois": parsed.get("whois", {}),
            "headers": parsed.get("headers", {}),
            "technologies": parsed.get("technologies", []),
            "findings": parsed.get("findings", []),
            "recommendations": parsed.get("recommendations", []),
=======
                "completed_at": str(scan.completed_at)
            },

            "infrastructure": {
                "ports": parsed.get("ports", []),
                "services": parsed.get("services", [])
            },

            "ssl": parsed.get("ssl", {}),

            "dns": parsed.get("dns", {}),

            "whois": parsed.get("whois", {}),

            "headers": parsed.get("headers", {}),

            "technologies": parsed.get("technologies", []),

            "findings": parsed.get("findings", []),

            "recommendations": parsed.get("recommendations", [])
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

        # Include any additional scan sections automatically
        reserved = {
            "ports",
            "services",
            "ssl",
            "dns",
            "whois",
            "headers",
            "technologies",
            "findings",
            "recommendations",
            "html",
            "body",
            "cookies",
            "raw_html",
<<<<<<< HEAD
            "response",
=======
            "response"
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

        additional = {}

        for key, value in parsed.items():
            if key.lower() not in reserved:
                additional[key] = value

        if additional:
            report["additional_data"] = additional

<<<<<<< HEAD
        with open(filename, "w", encoding="utf-8") as file:

            json.dump(report, file, indent=4, ensure_ascii=False)

        return filename
=======
        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
                ensure_ascii=False
            )

        return filename
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
