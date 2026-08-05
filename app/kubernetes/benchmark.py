"""
CloudShield Enterprise
Kubernetes Security Benchmark
"""


class KubernetesBenchmark:

    def evaluate(self, findings):

        summary = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0, "Info": 0}

        score = 100

        for finding in findings:

            severity = finding.get("severity", "Info")

            if severity in summary:

                summary[severity] += 1

            if severity == "Critical":

                score -= 25

            elif severity == "High":

                score -= 15

            elif severity == "Medium":

                score -= 8

            elif severity == "Low":

                score -= 3

        score = max(score, 0)

        return {
            "score": score,
            "critical": summary["Critical"],
            "high": summary["High"],
            "medium": summary["Medium"],
            "low": summary["Low"],
            "info": summary["Info"],
            "findings": findings,
        }
