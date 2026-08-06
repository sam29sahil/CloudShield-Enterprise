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

    display_name = ""

    default_arguments = []

    timeout = 300

    def __init__(self):

        self.runner = ToolRunner()

    # ==========================================================
    # Execute
    # ==========================================================

    def scan(
        self,
        target,
        arguments=None
    ):
        """
        Execute the security tool.
        """

        if arguments is None:

            arguments = self.default_arguments.copy()

        elif isinstance(arguments, str):

            arguments = arguments.split()

        result = self.runner.execute(

            tool=self.name,

            target=target,

            arguments=arguments

        )

        return result

    # ==========================================================
    # Tool Information
    # ==========================================================

    def version(self):
        """
        Return installed tool version.
        """

        return self.runner.version(

            self.name

        )

    def installed(self):
        """
        Check whether the tool exists.
        """

        return self.runner.is_installed(

            self.name

        )

    # ==========================================================
    # Metadata
    # ==========================================================

    def info(self):
        """
        Return metadata.
        """

        return {

            "name": self.name,

            "display_name": self.display_name or self.name.title(),

            "installed": self.installed(),

            "version": self.version(),

            "timeout": self.timeout,

            "default_arguments": self.default_arguments

        }

    # ==========================================================
    # Helpers
    # ==========================================================

    def command(self):
        """
        Return executable name.
        """

        return self.name

    def __repr__(self):

        return (

            f"<{self.__class__.__name__}"

            f" name='{self.name}'"

            f" installed={self.installed()}>"

        )