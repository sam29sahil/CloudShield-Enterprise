"""
CloudShield Enterprise
Security Services
"""

from app.security.core.engine import UniversalScannerEngine

# Basic Scanner
from app.security.tools.basic.services import BasicSecurityService


class SecurityService:
    """
    Central Security Service.

    Acts as the single entry point for all
    security operations inside CloudShield.

    Scanner -> SecurityService -> Security Tools
    """

    def __init__(self):

        # Enterprise Scanner Engine
        self.engine = UniversalScannerEngine()

        # Basic Scanner
        self.basic = BasicSecurityService()

    # =====================================================
    # Basic Scanner
    # =====================================================

    def run_basic_scan(
        self,
        user_id=None,
        asset_id=None,
        category="basic",
        tool="quick_scan",
        target=None,
        arguments=None,
    ):
        """
        Execute the Basic Scanner.
        """

        return self.basic.execute(
            user_id=user_id,
            asset_id=asset_id,
            category=category,
            tool=tool,
            target=target,
            arguments=arguments,
        )

    # =====================================================
    # Universal Scanner
    # =====================================================

    def run_universal_scan(
        self,
        user_id=None,
        asset_id=None,
        category=None,
        tool=None,
        target=None,
        arguments=None,
    ):
        """
        Execute a Universal Scanner tool.
        """

        return self.engine.execute(
            user_id=user_id,
            asset_id=asset_id,
            category=category,
            tool=tool,
            target=target,
            arguments=arguments,
        )

    # =====================================================
    # Legacy Compatibility
    # =====================================================

    def scan(
        self,
        target,
        tool=None,
        profile=None,
        arguments=None,
    ):
        """
        Legacy API.

        Keeps old routes working while the
        project is migrated.
        """

        if profile:

            return self.engine.scan_profile(
                target=target,
                profile=profile,
            )

        if tool:

            return self.engine.scan(
                target=target,
                tool=tool,
                arguments=arguments,
            )

        return {
            "success": False,
            "error": "No tool or profile selected.",
        }

    # =====================================================
    # Tool Management
    # =====================================================

    def available_tools(self):
        """
        Return all installed tools.
        """

        return self.engine.manager.tools()

    def tool_exists(self, tool):
        """
        Check whether a tool exists.
        """

        return self.engine.manager.installed(tool)

    def categories(self):
        """
        Return tool categories.
        """

        return self.engine.manager.categories()
