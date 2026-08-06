"""
CloudShield Enterprise
Wireless Result Parser
"""

import re


class WirelessParser:
    """
    Wireless Tool Parser
    """

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
        }

    def networks(self, output):

        networks = []

        for line in output.splitlines():

            if "WPA" in line or "WEP" in line or "OPN" in line:

                networks.append(line.strip())

        return networks

    def clients(self, output):

        clients = []

        mac_regex = r"(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}"

        for match in re.findall(mac_regex, output):

            if match not in clients:

                clients.append(match)

        return clients

    def handshakes(self, output):

        handshakes = []

        for line in output.splitlines():

            if "handshake" in line.lower():

                handshakes.append(line.strip())

        return handshakes

    def findings(self, output):

        return [line.strip() for line in output.splitlines() if line.strip()]
