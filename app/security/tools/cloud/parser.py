"""
CloudShield Enterprise
Cloud Parser
"""


class CloudParser:
    """
    Parse cloud security tool output.
    """

<<<<<<< HEAD
    def parse(self, tool, target, result):
=======
    def parse(

        self,

        tool,

        target,

        result

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        output = result.get("stdout", "")

        return {
<<<<<<< HEAD
            "success": result.get("success", False),
            "tool": tool,
            "target": target,
            "findings": self.findings(output),
            "raw_output": output,
            "error": result.get("stderr", ""),
=======

            "success": result.get("success", False),

            "tool": tool,

            "target": target,

            "findings": self.findings(output),

            "raw_output": output,

            "error": result.get("stderr", "")

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    def findings(self, output):

<<<<<<< HEAD
        return [line.strip() for line in output.splitlines() if line.strip()]
=======
        return [

            line.strip()

            for line in output.splitlines()

            if line.strip()

        ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
