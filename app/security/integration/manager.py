"""
CloudShield Enterprise
Integration Manager
"""

from app.security.core.manager import SecurityManager


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

<<<<<<< HEAD
    def execute(self, tool, target, arguments=None):

        return self.manager.run_tool(tool, target, arguments)
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
