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

    def execute(self, tool, target, arguments=None):

        started = datetime.utcnow()

        result = self.manager.run_tool(tool, target, arguments)

        finished = datetime.utcnow()

        return {
            "success": result.get("success", False),
            "tool": tool,
            "target": target,
            "started_at": started,
            "completed_at": finished,
            "duration": (finished - started).total_seconds(),
            "result": result,
        }

    def execute_multiple(self, tools, target):

        results = []

        for tool in tools:

            results.append(self.execute(tool, target))

        return results
