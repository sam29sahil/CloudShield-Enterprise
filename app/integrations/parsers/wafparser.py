"""
CloudShield Enterprise
WAF Parser
"""


class WAFParser:

    def parse(self, output):

        vendor = "Unknown"

        detected = False

        for line in output.splitlines():

            lower = line.lower()

            if "cloudflare" in lower:

                vendor = "Cloudflare"

                detected = True

            elif "aws" in lower:

                vendor = "AWS WAF"

                detected = True

            elif "akamai" in lower:

                vendor = "Akamai"

                detected = True

            elif "imperva" in lower:

                vendor = "Imperva"

                detected = True

            elif "f5" in lower:

                vendor = "F5 BIG-IP"

                detected = True

        return {

            "detected": detected,

            "vendor": vendor

        }