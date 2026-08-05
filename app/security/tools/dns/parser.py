"""
CloudShield Enterprise
DNS Parser
"""

import re


class DNSParser:
    """
    Parse DNS enumeration results.
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
            "subdomains": self.subdomains(output),
            "records": self.records(output),
            "findings": self.findings(output),
            "raw_output": output,
            "error": result.get("stderr", ""),
=======

            "success": result.get("success", False),

            "tool": tool,

            "target": target,

            "subdomains": self.subdomains(output),

            "records": self.records(output),

            "findings": self.findings(output),

            "raw_output": output,

            "error": result.get("stderr", "")

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    def subdomains(self, output):

        domains = []

        pattern = r"[A-Za-z0-9._-]+\.[A-Za-z]{2,}"

        for match in re.findall(pattern, output):

            if match not in domains:

                domains.append(match)

        return domains

    def records(self, output):

        records = []

        for line in output.splitlines():

            line = line.strip()

            if line:

                records.append(line)

        return records

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
