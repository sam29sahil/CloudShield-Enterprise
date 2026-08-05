"""
CloudShield Enterprise
Web Tools Parser
"""


class WebParser:
    """
    Standard parser for web security tools.
    """

<<<<<<< HEAD
    def parse(self, tool, target, result):

        return {
            "success": result.get("success", False),
            "tool": tool,
            "target": target,
            "raw_output": result.get("stdout", ""),
            "error": result.get("stderr", ""),
            "findings": self.findings(result.get("stdout", "")),
        }

    def findings(self, output):
=======
    def parse(
        self,
        tool,
        target,
        result
    ):

        return {

            "success": result.get("success", False),

            "tool": tool,

            "target": target,

            "raw_output": result.get("stdout", ""),

            "error": result.get("stderr", ""),

            "findings": self.findings(
                result.get("stdout", "")
            )

        }

    def findings(
        self,
        output
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        findings = []

        for line in output.splitlines():

            line = line.strip()

            if line:

                findings.append(line)

<<<<<<< HEAD
        return findings
=======
        return findings
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
