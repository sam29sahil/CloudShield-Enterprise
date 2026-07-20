"""
CloudShield Enterprise
Security Services
"""

from app.security.manager import SecurityManager


class SecurityService:
    """
    Security Service Layer
    """

    def __init__(self):

        self.manager = SecurityManager()

    def scan(

        self,

        tool,

        target,

        arguments=None

    ):

        return self.manager.run_tool(

            tool=tool,

            target=target,

            arguments=arguments

        )

    def available_tools(self):

        return self.manager.tools()

    def tool_exists(self, tool):

        return self.manager.installed(tool)

    def categories(self):

        return self.manager.categories()