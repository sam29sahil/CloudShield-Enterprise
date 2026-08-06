"""
CloudShield Enterprise
Scan Monitor
"""

from datetime import datetime


class ScanMonitor:
    """
    Monitor running scans.
    """

    def __init__(self):

        self.active_scans = {}

    def start(self, scan_id, tool, target):

        self.active_scans[scan_id] = {
            "tool": tool,
            "target": target,
            "status": "Running",
            "started_at": datetime.utcnow(),
        }

    def finish(self, scan_id):

        if scan_id in self.active_scans:

            self.active_scans[scan_id]["status"] = "Completed"

            self.active_scans[scan_id]["completed_at"] = datetime.utcnow()

    def status(self, scan_id):

        return self.active_scans.get(scan_id)

    def all(self):

        return self.active_scans
