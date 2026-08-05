"""
CloudShield Enterprise
Universal Scanner Engine
"""

from app.security.core.manager import SecurityManager
from app.security.core.validator import TargetValidator
<<<<<<< HEAD
from app.security.core.profiles import SCAN_PROFILES
=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
from app.security.core.findings import FindingsEngine
from app.security.core.risk_engine import RiskEngine


class UniversalScannerEngine:
    """
<<<<<<< HEAD
    Main orchestration engine for CloudShield Enterprise.
=======
    Enterprise Scan Orchestrator

    Responsible only for:

        • Validate target
        • Execute manager
        • Build findings
        • Calculate risk
        • Return response
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    """

    def __init__(self):

        self.manager = SecurityManager()

    # ==========================================================
<<<<<<< HEAD
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
=======
    # Main Scan
    # ==========================================================

    def scan(
        self,
        target,
        category,
        mode="quick",
        tool=None,
        arguments=None
    ):

        if arguments is None:

            arguments = []

        #
        # Validate Target
        #

        valid, target_type = TargetValidator.validate(

            target

        )

        if not valid:

            return {

                "success": False,

                "error": target_type

            }

        #
        # Execute
        #

        try:

            result = self.manager.execute(

                user_id=None,

                asset_id=None,

                mode=mode,

                category=category,

                tool=tool,

                target=target,

                arguments=arguments

            )

        except Exception:

            import traceback

            traceback.print_exc()

            raise

        #
        # Multiple tool execution
        #

        if isinstance(result, list):

            results = result

        else:

            results = [

                result

            ]

        findings = []





                # ======================================================
        # Build Findings
        # ======================================================

        for item in results:

            findings.append(

                FindingsEngine.create(

                    tool=item.get(

                        "tool",

                        "unknown"

                    ),

                    category=category,

                    target=target,

                    severity=(

                        "Info"

                        if item.get("success")

                        else "Low"

                    ),

                    title=(

                        f"{item.get('tool','Tool')} "

                        "completed"

                    ),

                    description=(

                        "Execution completed successfully."

                        if item.get("success")

                        else item.get(

                            "error",

                            "Execution failed."

                        )

                    ),

                    raw=item

                )

            )

        # ======================================================
        # Calculate Risk
        # ======================================================

        risk = RiskEngine.calculate(

            findings

        )

        # ======================================================
        # Summary
        # ======================================================

        summary = {

            "total_tools": len(results),

            "successful": sum(

                1

                for r in results

                if r.get("success")

            ),

            "failed": sum(

                1

                for r in results

                if not r.get("success")

            )

        }

        # ======================================================
        # Final Response
        # ======================================================

        return {

            "success": True,

            "mode": mode,

            "category": category,

            "target": target,

            "target_type": target_type,

            "results": results,

            "findings": findings,

            "risk": risk,

            "summary": summary

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # ==========================================================
    # Metadata
    # ==========================================================

    def available_tools(self):
<<<<<<< HEAD
        """
        Return all available tools.
        """
=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return self.manager.tools()

    def categories(self):
<<<<<<< HEAD
        """
        Return tool categories.
        """

        return self.manager.categories()
=======

        return self.manager.get_categories()

    def tools(self, category):

        return self.manager.get_tools(category)

    # ==========================================================
    # Information
    # ==========================================================

    def info(self):

        return {

            "engine": "UniversalScannerEngine",

            "version": "2.0",

            "categories": self.categories(),

            "tools": len(

                self.available_tools()

            )

        }

    # ==========================================================
    # Debug
    # ==========================================================

    def __repr__(self):

        return (

            "<UniversalScannerEngine "

            f"tools={len(self.available_tools())}>"

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
