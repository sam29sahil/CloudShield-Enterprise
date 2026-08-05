"""
CloudShield Enterprise
Scan Executor
"""

from datetime import datetime

from app.security.core.manager import SecurityManager


class ScanExecutor:
    """
    Executes security scans.
    """

    def __init__(self):

        self.manager = SecurityManager()

<<<<<<< HEAD
    def execute(self, tool, target, arguments=None):

        started = datetime.utcnow()

        result = self.manager.run_tool(tool, target, arguments)
=======
    def execute(

        self,

        tool,

        target,

        arguments=None

    ):

        started = datetime.utcnow()

        result = self.manager.run_tool(

            tool,

            target,

            arguments

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        finished = datetime.utcnow()

        return {
<<<<<<< HEAD
            "success": result.get("success", False),
            "tool": tool,
            "target": target,
            "started_at": started,
            "completed_at": finished,
            "duration": (finished - started).total_seconds(),
            "result": result,
        }

    def execute_multiple(self, tools, target):
=======

            "success": result.get("success", False),

            "tool": tool,

            "target": target,

            "started_at": started,

            "completed_at": finished,

            "duration": (

                finished - started

            ).total_seconds(),

            "result": result

        }

    def execute_multiple(

        self,

        tools,

        target

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        results = []

        for tool in tools:

<<<<<<< HEAD
            results.append(self.execute(tool, target))

        return results
=======
            results.append(

                self.execute(

                    tool,

                    target

                )

            )

        return results
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
