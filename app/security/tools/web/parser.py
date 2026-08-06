"""
CloudShield Enterprise
Web Tools Parser
"""


class WebParser:
    """
    Standard parser for web security tools.
    """

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

        findings = []

        for line in output.splitlines():

            line = line.strip()

            if line:

                findings.append(line)

        return findings