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

    def scan(
        self,
        target,
        tool,
        arguments=None
    ):
        """
        Execute a single security tool.
        """

        valid, target_type = TargetValidator.validate(target)

        if not valid:

            return {

                "success": False,

                "error": target_type

            }

        result = self.manager.execute(

            user_id=None,

            asset_id=None,

            mode="universal",

            category="custom",

            tool=tool,

            target=target,

            arguments=arguments or []

        )

        result["target"] = target
        result["target_type"] = target_type

        return result

    # ==========================================================
    # Profile Scan
    # ==========================================================
    
    def scan_profile(
        self,
        target,
        profile,
        arguments=None
    ):
        """
        Execute every tool inside a profile.
        """

        valid, target_type = TargetValidator.validate(target)

        if not valid:

            return {
                "success": False,
                "error": target_type
            }

        tools = SCAN_PROFILES.get(profile)

        if not tools:

            return {
                "success": False,
                "error": "Unknown profile."
            }

        results = []
        findings = []

        for tool in tools:

            result = self.manager.run_tool(
                tool=tool,
                target=target,
                arguments=arguments
            )

            results.append(result)

            findings.append(
                FindingsEngine.create(
                    tool=tool,
                    category=profile,
                    target=target,
                    severity="Info" if result.get("success") else "Low",
                    title=f"{tool} completed",
                    description=(
                        "Execution completed successfully."
                        if result.get("success")
                        else result.get("error")
                    ),
                    raw=result
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
            "summary": {
                "tools": len(tools),
                "successful": sum(
                    1 for r in results if r.get("success")
                ),
                "failed": sum(
                    1 for r in results if not r.get("success")
                )
            }
        }
    # ==========================================================
    # Metadata
    # ==========================================================

    def available_tools(self):

        return self.manager.tools()

    def categories(self):

        return self.manager.get_categories()

    def tools(self, category):

        return self.manager.get_tools(category)