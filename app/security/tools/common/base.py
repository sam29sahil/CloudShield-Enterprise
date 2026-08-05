"""
CloudShield Enterprise
<<<<<<< HEAD
Base Tool
=======
Base Security Tool
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
"""

from abc import ABC

<<<<<<< HEAD
from app.security.core.tool_runner import ToolRunner


class BaseTool(ABC):
    """
    Base class for all security tools.
    """

=======

class BaseTool(ABC):
    """
    Base class for every security tool.
    """

    # ======================================================
    # Metadata
    # ======================================================

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    name = ""

    display_name = ""

<<<<<<< HEAD
    default_arguments = []

    timeout = 300

    def __init__(self):

        self.runner = ToolRunner()

    # ==========================================================
    # Execute
    # ==========================================================

    def scan(self, target, arguments=None):
        """
        Execute the security tool.
        """

        if arguments is None:

            arguments = self.default_arguments.copy()

        elif isinstance(arguments, str):

            arguments = arguments.split()

        result = self.runner.execute(tool=self.name, target=target, arguments=arguments)

        return result

    # ==========================================================
    # Tool Information
    # ==========================================================

    def version(self):
        """
        Return installed tool version.
        """

        return self.runner.version(self.name)

    def installed(self):
        """
        Check whether the tool exists.
        """

        return self.runner.is_installed(self.name)

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
            "default_arguments": self.default_arguments,
        }

    # ==========================================================
    # Helpers
    # ==========================================================

    def command(self):
        """
        Return executable name.
        """

        return self.name
=======
    category = ""

    description = ""

    version = "1.0"

    author = "CloudShield Enterprise"

    # ======================================================
    # Execution
    # ======================================================

    enabled = True

    always = False

    priority = 100

    timeout = 300

    passive = False

    requires_https = False

    # ======================================================
    # Scan Modes
    # ======================================================

    modes = [

        "quick",

        "standard",

        "deep",

        "enterprise"

    ]

    # ======================================================
    # Tool Information
    # ======================================================

    def metadata(self):

        return {

            "name": self.name,

            "display_name": self.display_name,

            "category": self.category,

            "description": self.description,

            "version": self.version,

            "author": self.author,

            "enabled": self.enabled,

            "always": self.always,

            "priority": self.priority,

            "timeout": self.timeout,

            "passive": self.passive,

            "requires_https": self.requires_https,

            "modes": self.modes

        }

    # ======================================================
    # Validation
    # ======================================================

    def supports_mode(self, mode):

        return mode.lower() in self.modes

    # ======================================================
    # Execution
    # =================================================

    def run(
        self,
        target,
        arguments=None
    ):
        """
        Default compatibility method.

        Existing tools may implement
        execute(), scan(), check(), etc.
        Manager will detect the correct
        execution method.
        """

        raise NotImplementedError(
            f"{self.__class__.__name__} "
            "does not implement run()."
        )

    # ======================================================
    # Optional Hooks
    # ======================================================

    def before_scan(self, target):
        """
        Called before execution.
        """

        pass

    def after_scan(self, result):
        """
        Called after execution.
        """

        return result

    # ======================================================
    # String Representation
    # ======================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def __repr__(self):

        return (
<<<<<<< HEAD
            f"<{self.__class__.__name__}"
            f" name='{self.name}'"
            f" installed={self.installed()}>"
        )
=======

            f"<SecurityTool "

            f"{self.name}>"

        )
# ======================================================
# Backward Compatibility
# ======================================================

SecurityTool = BaseTool        
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
