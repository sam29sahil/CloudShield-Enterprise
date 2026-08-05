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
            "generated_at": datetime.utcnow().isoformat(),
            "product": "CloudShield Enterprise",
            "module": "Docker Security",
            "score": analysis["score"],
            "risk": analysis["risk"],
            "recommendations": analysis["recommendation"],
            "findings": analysis["summary"]["findings"],
        }
