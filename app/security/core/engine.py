"""
CloudShield Enterprise
Universal Scanner Engine
"""

from app.security.core.manager import SecurityManager
from app.security.core.validator import TargetValidator
from app.security.core.profiles import SCAN_PROFILES
from app.security.core.findings import FindingsEngine
from app.security.core.risk_engine import RiskEngine


class UniversalScannerEngine:
    """
    Main orchestration engine for CloudShield Enterprise.
    """

    def __init__(self):

        self.manager = SecurityManager()

    # ==========================================================
    # Single Tool Scan
    # ==========================================================

    def scan(self, target, tool, arguments=None):
        """
        Validate target and execute a single tool.
        """

        valid, target_type = TargetValidator.validate(target)

        if not valid:
            return {"success": False, "error": target_type}

        result = self.manager.run_tool(tool=tool, target=target, arguments=arguments)

        result["target"] = target
        result["target_type"] = target_type
        result["tool"] = tool

        return result

    # ==========================================================
    # Profile Scan
    # ==========================================================

    def scan_profile(self, target, profile, arguments=None):
        """
        Execute all tools registered in a scan profile.
        """

        valid, target_type = TargetValidator.validate(target)

        if not valid:
            return {"success": False, "error": target_type}

        tools = SCAN_PROFILES.get(profile)

        if not tools:
            return {"success": False, "error": "Unknown scan profile."}

        findings = []
        results = []

        for tool in tools:

            result = self.manager.run_tool(
                tool=tool, target=target, arguments=arguments
            )

            results.append(result)

            severity = "Info"

            if not result.get("success"):
                severity = "Low"

            findings.append(
                FindingsEngine.create(
                    tool=tool,
                    category=profile,
                    target=target,
                    severity=severity,
                    title=f"{tool} scan completed",
                    description=(
                        result.get("error")
                        if not result.get("success")
                        else f"{tool} scan completed successfully."
                    ),
                    raw=result,
                )
            )

        risk = RiskEngine.calculate(findings)

        return {
            "success": True,
            "profile": profile,
            "target": target,
            "target_type": target_type,
            "results": results,
            "findings": findings,
            "risk": risk,
        }

    # ==========================================================
    # Metadata
    # ==========================================================

    def available_tools(self):
        """
        Return all available tools.
        """

        return self.manager.tools()

    def categories(self):
        """
        Return tool categories.
        """

        return self.manager.categories()
