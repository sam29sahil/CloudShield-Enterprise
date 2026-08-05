"""
CloudShield Enterprise
DNS Parser
"""

import re


class DNSParser:
    """
    Parse DNS enumeration results.
    """

    def parse(self, tool, target, result):

        output = result.get("stdout", "")

        return {
            "success": result.get("success", False),
            "tool": tool,
            "target": target,
            "subdomains": self.subdomains(output),
            "records": self.records(output),
            "findings": self.findings(output),
            "raw_output": output,
            "error": result.get("stderr", ""),
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

        return [line.strip() for line in output.splitlines() if line.strip()]
