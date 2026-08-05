"""
CloudShield Enterprise
Docker Report
"""

from datetime import datetime

from app.docker.analyzer import DockerAnalyzer


class DockerReport:

    def __init__(self):

        self.analyzer = DockerAnalyzer()

    # ----------------------------------
    # Generate Report
    # ----------------------------------

    def generate(self):

        analysis = self.analyzer.analyze()

        return {
<<<<<<< HEAD
            "generated_at": datetime.utcnow().isoformat(),
            "product": "CloudShield Enterprise",
            "module": "Docker Security",
            "score": analysis["score"],
            "risk": analysis["risk"],
            "recommendations": analysis["recommendation"],
            "findings": analysis["summary"]["findings"],
        }
=======

            "generated_at": datetime.utcnow().isoformat(),

            "product": "CloudShield Enterprise",

            "module": "Docker Security",

            "score": analysis["score"],

            "risk": analysis["risk"],

            "recommendations": analysis["recommendation"],

            "findings": analysis["summary"]["findings"]

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
