"""
CloudShield Enterprise
Base Security Tool
"""

from abc import ABC


class BaseTool(ABC):
    """
    Base class for every security tool.
    """

    # ======================================================
    # Metadata
    # ======================================================

    name = ""

    display_name = ""

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

    def __repr__(self):

        return (

            f"<SecurityTool "

            f"{self.name}>"

        )
# ======================================================
# Backward Compatibility
# ======================================================

SecurityTool = BaseTool        