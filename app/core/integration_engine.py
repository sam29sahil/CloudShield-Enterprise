"""
Professional Tool Integration Engine
"""

import shutil


class IntegrationEngine:

    def tool_exists(self, tool):

        return shutil.which(tool) is not None

    def available_tools(self):

<<<<<<< HEAD
        tools = ["nmap", "nuclei", "nikto", "whatweb", "wafw00f", "testssl.sh"]
=======
        tools = [

            "nmap",

            "nuclei",

            "nikto",

            "whatweb",

            "wafw00f",

            "testssl.sh"

        ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        available = {}

        for tool in tools:

            available[tool] = self.tool_exists(tool)

<<<<<<< HEAD
        return available
=======
        return available
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
