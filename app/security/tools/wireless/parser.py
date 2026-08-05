"""
CloudShield Enterprise
Wireless Result Parser
"""

import re


class WirelessParser:
    """
    Wireless Tool Parser
    """

<<<<<<< HEAD
    def parse(self, tool, target, result):

        output = result.get("stdout", "")

        return {
            "success": result.get("success", False),
            "tool": tool,
            "target": target,
            "networks": self.networks(output),
            "clients": self.clients(output),
            "handshakes": self.handshakes(output),
            "findings": self.findings(output),
            "raw_output": output,
            "error": result.get("stderr", ""),
=======
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

            "networks": self.networks(output),

            "clients": self.clients(output),

            "handshakes": self.handshakes(output),

            "findings": self.findings(output),

            "raw_output": output,

            "error": result.get(

                "stderr",

                ""

            )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    def networks(self, output):

        networks = []

        for line in output.splitlines():

            if "WPA" in line or "WEP" in line or "OPN" in line:

<<<<<<< HEAD
                networks.append(line.strip())
=======
                networks.append(

                    line.strip()

                )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return networks

    def clients(self, output):

        clients = []

        mac_regex = r"(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}"

<<<<<<< HEAD
        for match in re.findall(mac_regex, output):
=======
        for match in re.findall(

            mac_regex,

            output

        ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            if match not in clients:

                clients.append(match)

        return clients

    def handshakes(self, output):

        handshakes = []

        for line in output.splitlines():

            if "handshake" in line.lower():

<<<<<<< HEAD
                handshakes.append(line.strip())
=======
                handshakes.append(

                    line.strip()

                )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return handshakes

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
