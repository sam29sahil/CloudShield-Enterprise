"""
CloudShield Enterprise
Professional Tool Manager
"""

import shutil


class ToolManager:

    def __init__(self):

        self.tools = {
            "nmap": "nmap",
            "nuclei": "nuclei",
            "nikto": "nikto",
            "whatweb": "whatweb",
            "wafw00f": "wafw00f",
            "testssl": "testssl.sh",
            "subfinder": "subfinder",
            "dnsrecon": "dnsrecon",
        }

    def is_installed(self, tool):

        command = self.tools.get(tool)

        if command is None:

            return False

        return shutil.which(command) is not None

    def installed_tools(self):

        result = {}

        for tool in self.tools:

            result[tool] = self.is_installed(tool)

        return result
