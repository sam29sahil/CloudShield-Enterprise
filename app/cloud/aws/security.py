"""
CloudShield Enterprise
AWS Security Assessment
"""


class SecurityAssessment:

    def __init__(self):

        self.findings = []

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

            "total": len(self.findings),

            "critical": critical,

            "high": high,

            "medium": medium,

            "low": low,

            "findings": self.findings

        }