"""
CloudShield Enterprise
Docker Security Analyzer
"""

from app.docker.benchmark import DockerBenchmark


class DockerAnalyzer:
    """
    Analyze Docker security posture.
    """

    def __init__(self):

        self.benchmark = DockerBenchmark()

    # ----------------------------------
    # Analyze
    # ----------------------------------

    def analyze(self):

        benchmark = self.benchmark.run()

        score = benchmark["score"]

        if score >= 90:

            risk = "Low"

        elif score >= 70:

            risk = "Medium"

        elif score >= 50:

            risk = "High"

        else:

            risk = "Critical"

        return {
<<<<<<< HEAD
            "score": score,
            "risk": risk,
            "summary": benchmark,
            "recommendation": self.recommendations(benchmark["findings"]),
=======

            "score": score,

            "risk": risk,

            "summary": benchmark,

            "recommendation": self.recommendations(

                benchmark["findings"]

            )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # ----------------------------------
    # Recommendations
    # ----------------------------------

    def recommendations(self, findings):

        recommendations = []

        for finding in findings:

            title = finding.get("title", "")

            if title == "Privileged Container":

<<<<<<< HEAD
                recommendations.append("Disable privileged mode.")

            elif title == "Running as Root":

                recommendations.append("Run containers using a non-root user.")

            elif title == "Docker Socket Mounted":

                recommendations.append("Do not mount docker.sock into containers.")
=======
                recommendations.append(

                    "Disable privileged mode."

                )

            elif title == "Running as Root":

                recommendations.append(

                    "Run containers using a non-root user."

                )

            elif title == "Docker Socket Mounted":

                recommendations.append(

                    "Do not mount docker.sock into containers."

                )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            elif title == "Host Network":

                recommendations.append(
<<<<<<< HEAD
                    "Use bridge networking instead of host networking."
                )

        return list(set(recommendations))
=======

                    "Use bridge networking instead of host networking."

                )

        return list(set(recommendations))
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
