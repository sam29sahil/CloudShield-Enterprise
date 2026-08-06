"""
CloudShield Enterprise
SSL Parser
"""

import re


class SSLParser:
    """
    SSL Result Parser
    """

    def parse(

        self,

        tool,

        target,

        result

    ):

        output = result.get(

            "stdout",

            ""

        )

        return {

            "success": result.get("success", False),

            "tool": tool,

            "target": target,

            "certificate": self.certificate(output),

            "tls_versions": self.protocols(output),

            "vulnerabilities": self.vulnerabilities(output),

            "findings": self.findings(output),

            "raw_output": output,

            "error": result.get("stderr", "")

        }

    def certificate(self, output):

        cert = {}

        for line in output.splitlines():

            if "Issuer" in line:

                cert["issuer"] = line.strip()

            elif "Subject" in line:

                cert["subject"] = line.strip()

            elif "Not After" in line:

                cert["expiry"] = line.strip()

        return cert

    def protocols(self, output):

        versions = []

        for version in [

            "SSLv2",

            "SSLv3",

            "TLS1.0",

            "TLS1.1",

            "TLS1.2",

            "TLS1.3"

        ]:

            if version in output:

                versions.append(version)

        return versions

    def vulnerabilities(self, output):

        findings = []

        checks = [

            "Heartbleed",

            "POODLE",

            "BEAST",

            "FREAK",

            "LOGJAM",

            "ROBOT",

            "DROWN"

        ]

        for check in checks:

            if re.search(

                check,

                output,

                re.IGNORECASE

            ):

                findings.append(check)

        return findings

    def findings(self, output):

        return [

            line.strip()

            for line in output.splitlines()

            if line.strip()

        ]