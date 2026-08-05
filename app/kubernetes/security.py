"""
CloudShield Enterprise
Kubernetes Security
"""

from app.kubernetes.report import KubernetesReport


class KubernetesSecurity:

    def __init__(self):

        self.report = KubernetesReport()

    def dashboard(self):

        report = self.report.generate()

        security = report["security"]

        return {
<<<<<<< HEAD
            "score": security["score"],
            "critical": security["critical"],
            "high": security["high"],
            "medium": security["medium"],
            "low": security["low"],
            "info": security["info"],
            "findings": security["findings"],
            "recommendations": report["recommendations"],
        }
=======

            "score": security["score"],

            "critical": security["critical"],

            "high": security["high"],

            "medium": security["medium"],

            "low": security["low"],

            "info": security["info"],

            "findings": security["findings"],

            "recommendations": report["recommendations"]

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
