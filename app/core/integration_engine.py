"""
Professional Tool Integration Engine
"""

import shutil


class IntegrationEngine:

    def tool_exists(self, tool):

        return shutil.which(tool) is not None

    def available_tools(self):

        tools = [

            "nmap",

            "nuclei",

            "nikto",

            "whatweb",

            "wafw00f",

            "testssl.sh"

        ]

        available = {}

        for tool in tools:

            available[tool] = self.tool_exists(tool)

        return available