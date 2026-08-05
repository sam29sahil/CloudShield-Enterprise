"""
CloudShield Enterprise
Nuclei Parser
"""


class NucleiParser:

    def parse(self, output):

        findings = []

        for line in output.splitlines():

            line = line.strip()

            if line:

                findings.append({"finding": line})

        return {"total": len(findings), "findings": findings}
