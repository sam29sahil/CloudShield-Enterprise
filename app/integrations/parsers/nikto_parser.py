"""
CloudShield Enterprise
Nikto Parser
"""


class NiktoParser:

    def parse(self, output):

        findings = []

        for line in output.splitlines():

            if line.startswith("+"):

<<<<<<< HEAD
                findings.append(line.replace("+ ", ""))

        return {"count": len(findings), "findings": findings}
=======
                findings.append(

                    line.replace("+ ", "")

                )

        return {

            "count": len(findings),

            "findings": findings

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
