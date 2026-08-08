"""
CloudShield Enterprise
Docker Benchmark
"""

from app.docker.scanner import DockerScanner


class DockerBenchmark:
    """
    CIS Docker Benchmark
    """

    def __init__(self):

        self.scanner = DockerScanner()

    # ----------------------------------
    # Run Benchmark
    # ----------------------------------

    def run(self):

        findings = self.scanner.security_findings()

        critical = 0

        high = 0

        medium = 0

        low = 0

        info = 0

        for finding in findings:

            severity = finding["severity"]

            if severity == "Critical":

                critical += 1

            elif severity == "High":

                high += 1

            elif severity == "Medium":

                medium += 1

            elif severity == "Low":

                low += 1

            else:

                info += 1

        score = max(100 - critical * 20 - high * 10, 0)

        return {
            "score": score,
            "critical": critical,
            "high": high,
            "medium": medium,
            "low": low,
            "info": info,
            "findings": findings,
        }
