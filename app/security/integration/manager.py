"""
CloudShield Enterprise
Integration Manager
"""

from app.security.manager import SecurityManager


class IntegrationManager:
    """
    Main integration manager.
    """

    def __init__(self):

        self.manager = SecurityManager()

    def tools(self):

        return self.manager.tools()

    def exists(self, tool):

        return self.manager.installed(tool)

    def execute(

        self,

        tool,

        target,

        arguments=None

    ):

        return self.manager.run_tool(

            tool,

            target,

            arguments

        )