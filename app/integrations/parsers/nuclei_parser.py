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

<<<<<<< HEAD
                findings.append({"finding": line})

        return {"total": len(findings), "findings": findings}
=======
                findings.append({

                    "finding": line

                })

        return {

            "total": len(findings),

            "findings": findings

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
