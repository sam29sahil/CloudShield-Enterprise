"""
CloudShield Enterprise
Nikto Parser
"""


class NiktoParser:

    def parse(self, output):

        findings = []

        for line in output.splitlines():

            if line.startswith("+"):

                findings.append(line.replace("+ ", ""))

        return {"count": len(findings), "findings": findings}
