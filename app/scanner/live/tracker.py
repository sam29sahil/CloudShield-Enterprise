"""
CloudShield Enterprise
Live Scan Tracker
"""

from app.scanner.live.manager import live_manager
from app.scanner.live.status import ScanStatus


class ScanTracker:
    """
    High-level helper for updating
    live scan progress.
    """

    def __init__(self, scan):

        self.scan = scan

    # ----------------------------------------------------------
    # Create
    # ----------------------------------------------------------

    def start(self):

        live_manager.create(
            scan_id=self.scan.id, target=self.scan.target, tool=self.scan.tool
        )

    # ----------------------------------------------------------
    # Validation
    # ----------------------------------------------------------

    def validating(self):

        live_manager.update(
            self.scan.id,
            status=ScanStatus.VALIDATING,
            progress=10,
            message="Validating target...",
        )

    # ----------------------------------------------------------
    # Initialization
    # ----------------------------------------------------------

    def initializing(self):

        live_manager.update(
            self.scan.id,
            status=ScanStatus.INITIALIZING,
            progress=20,
            message="Initializing tool...",
        )

    # ----------------------------------------------------------
    # Running
    # ----------------------------------------------------------

    def running(self, tool=None):

        live_manager.update(
            self.scan.id,
            status=ScanStatus.RUNNING,
            progress=50,
            tool=tool or self.scan.tool,
            message=f"Running {tool or self.scan.tool}...",
        )

    # ----------------------------------------------------------
    # Parsing
    # ----------------------------------------------------------

    def parsing(self):

        live_manager.update(
            self.scan.id,
            status=ScanStatus.PARSING,
            progress=70,
            message="Parsing scan results...",
        )

    # ----------------------------------------------------------
    # Findings
    # ----------------------------------------------------------

    def findings(self):

        live_manager.update(
            self.scan.id,
            status=ScanStatus.FINDINGS,
            progress=85,
            message="Generating findings...",
        )

    # ----------------------------------------------------------
    # Report
    # ----------------------------------------------------------

    def reporting(self):

        live_manager.update(
            self.scan.id,
            status=ScanStatus.REPORT,
            progress=95,
            message="Generating report...",
        )

    # ----------------------------------------------------------
    # Complete
    # ----------------------------------------------------------

    def complete(self):

        live_manager.complete(self.scan.id, message="Scan completed.")

    # ----------------------------------------------------------
    # Fail
    # ----------------------------------------------------------

    def failed(self, error):

        live_manager.fail(self.scan.id, message=str(error))

    # ----------------------------------------------------------
    # Cancel
    # ----------------------------------------------------------

    def cancelled(self):

        live_manager.cancel(self.scan.id)
