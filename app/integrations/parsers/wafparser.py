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

<<<<<<< HEAD
        return {"detected": detected, "vendor": vendor}
=======
        return {

            "detected": detected,

            "vendor": vendor

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
