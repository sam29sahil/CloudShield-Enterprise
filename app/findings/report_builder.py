"""
CloudShield Enterprise
Executive Report Builder
"""


class ReportBuilder:

    def build(self, findings):

        summary = {

            "Critical": 0,

            "High": 0,

            "Medium": 0,

            "Low": 0,

            "Info": 0

        }

        for finding in findings:

            summary[finding.severity] += 1

        return {

            "summary": summary,

            "total": len(findings),

            "findings": findings

        }