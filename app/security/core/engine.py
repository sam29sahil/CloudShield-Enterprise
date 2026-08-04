"""
CloudShield Enterprise
Universal Scanner Engine
"""

from app.security.core.manager import SecurityManager
from app.security.core.validator import TargetValidator
from app.security.core.findings import FindingsEngine
from app.security.core.risk_engine import RiskEngine


class UniversalScannerEngine:
    """
    Enterprise Scan Orchestrator

    Responsible only for:

        • Validate target
        • Execute manager
        • Build findings
        • Calculate risk
        • Return response
    """

    def __init__(self):

        self.manager = SecurityManager()

    # ==========================================================
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

        result = self.manager.execute(

            user_id=None,

            asset_id=None,

            mode=mode,

            category=category,

            tool=tool,

            target=target,

            arguments=arguments

        )

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