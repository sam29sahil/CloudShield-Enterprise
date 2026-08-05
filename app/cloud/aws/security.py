"""
CloudShield Enterprise
AWS Security Assessment
"""


class SecurityAssessment:

    def __init__(self):

        self.findings = []

<<<<<<< HEAD
    def add(self, service, severity, title, description, recommendation):

        self.findings.append(
            {
                "service": service,
                "severity": severity,
                "title": title,
                "description": description,
                "recommendation": recommendation,
            }
        )
=======
    def add(

        self,

        service,

        severity,

        title,

        description,

        recommendation

    ):

        self.findings.append({

            "service": service,

            "severity": severity,

            "title": title,

            "description": description,

            "recommendation": recommendation

        })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def summary(self):

        critical = 0
        high = 0
        medium = 0
        low = 0

        for finding in self.findings:

            severity = finding["severity"]

            if severity == "Critical":
                critical += 1

            elif severity == "High":
                high += 1

            elif severity == "Medium":
                medium += 1

            else:
                low += 1

        return {
<<<<<<< HEAD
            "total": len(self.findings),
            "critical": critical,
            "high": high,
            "medium": medium,
            "low": low,
            "findings": self.findings,
        }
=======

            "total": len(self.findings),

            "critical": critical,

            "high": high,

            "medium": medium,

            "low": low,

            "findings": self.findings

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
