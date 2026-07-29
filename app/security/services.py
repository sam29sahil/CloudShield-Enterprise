"""
CloudShield Enterprise
Security Services
"""

from app.security.core.engine import UniversalScannerEngine


class SecurityService:
    """
    Security Service Layer
    """

    def __init__(self):

        self.manager =  UniversalScannerEngine()

    def scan(
        self,
        target,
        tool=None,
        profile=None,
        arguments=None
    ):
        """
        Run either a single tool or a scan profile.
        """

        if profile:
            return self.engine.scan_profile(
                target=target,
                profile=profile
            )

        if tool:
            return self.engine.scan(
                target=target,
                tool=tool,
                arguments=arguments
            )

        return {
            "success": False,
            "error": "No tool or profile selected."
        }

    def available_tools(self):

        return self.engine.manager.tools()

    def tool_exists(self, tool):

        return self.engine.manager.installed(tool)

    def categories(self):

        return self.engine.manager.categories()