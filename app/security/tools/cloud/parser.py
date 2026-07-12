"""
CloudShield Enterprise
Cloud Parser
"""


class CloudParser:
    """
    Parse cloud security tool output.
    """

    def parse(

        self,

        tool,

        target,

        result

    ):

        output = result.get("stdout", "")

        return {

            "success": result.get("success", False),

            "tool": tool,

            "target": target,

            "findings": self.findings(output),

            "raw_output": output,

            "error": result.get("stderr", "")

        }

    def findings(self, output):

        return [

            line.strip()

            for line in output.splitlines()

            if line.strip()

        ]