"""
CloudShield Enterprise
Live Scan Manager
"""

from threading import Lock

from app.scanner.live.progress import ScanProgress
from app.scanner.live.status import ScanStatus


class LiveScanManager:
    """
    Manage active scan progress.
    """

    def __init__(self):

        self._scans = {}

        self._lock = Lock()

    # ==========================================================
    # Create
    # ==========================================================

    def create(self, scan_id, target, tool):
        """
        Create a new live scan.
        """

        progress = ScanProgress(
            scan_id=scan_id,
            target=target,
            tool=tool,
            status=ScanStatus.QUEUED,
            progress=0,
            message="Waiting to start...",
        )

        with self._lock:

            self._scans[scan_id] = progress

        return progress

    # ==========================================================
    # Get
    # ==========================================================

    def get(self, scan_id):
        """
        Return scan progress.
        """

        return self._scans.get(scan_id)

    # ==========================================================
    # Update
    # ==========================================================

    def update(self, scan_id, **kwargs):
        """
        Update a running scan.
        """

        progress = self.get(scan_id)

        if progress is None:

            return None

        progress.update(**kwargs)

        return progress

    # ==========================================================
    # Complete
    # ==========================================================

    def complete(self, scan_id, message="Scan completed."):
        """
        Mark scan as completed.
        """

        return self.update(
            scan_id, status=ScanStatus.COMPLETED, progress=100, message=message
        )

    # ==========================================================
    # Fail
    # ==========================================================

    def fail(self, scan_id, message):
        """
        Mark scan as failed.
        """

        return self.update(scan_id, status=ScanStatus.FAILED, message=message)

    # ==========================================================
    # Cancel
    # ==========================================================

    def cancel(self, scan_id):
        """
        Cancel a scan.
        """

        return self.update(
            scan_id, status=ScanStatus.CANCELLED, message="Scan cancelled."
        )

    # ==========================================================
    # Remove
    # ==========================================================

    def remove(self, scan_id):
        """
        Remove completed scan.
        """

        with self._lock:

            self._scans.pop(scan_id, None)

    # ==========================================================
    # List
    # ==========================================================

    def all(self):
        """
        Return all scans.
        """

        return self._scans


live_manager = LiveScanManager()
