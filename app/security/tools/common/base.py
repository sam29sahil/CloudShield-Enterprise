"""
CloudShield Enterprise
Base Tool
"""

from abc import ABC

from app.security.core.tool_runner import ToolRunner


class BaseTool(ABC):
    """
    Base class for all security tools.
    """

    name = ""

    default_arguments = []

    timeout = 300

    def __init__(self):

        self.runner = ToolRunner()

    def scan(
        self,
        target,
        arguments=None
    ):
        """
        Execute the tool.
        """

        if arguments is None:

            arguments = self.default_arguments.copy()

        return self.runner.execute(

            tool=self.name,

            target=target,

            arguments=arguments

        )

    def version(self):

        return self.runner.version(

            self.name

        )

    def installed(self):

        return self.runner.is_installed(

            self.name

        )

    def info(self):

        return {

            "name": self.name,

            "installed": self.installed(),

            "version": self.version()

        }