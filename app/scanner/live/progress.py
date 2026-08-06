"""
CloudShield Enterprise
Live Scan Progress
"""

from dataclasses import dataclass, field
from datetime import datetime

from app.scanner.live.status import ScanStatus


@dataclass
class ScanProgress:
    """
    Stores live scan progress.
    """

    scan_id: int | None = None

    target: str = ""

    tool: str = ""

    status: ScanStatus = ScanStatus.QUEUED

    progress: int = 0

    message: str = "Waiting..."

    started_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    completed_at: datetime | None = None

    def update(self, status=None, progress=None, message=None, tool=None):
        """
        Update scan progress.
        """

        if status is not None:
            self.status = status

        if progress is not None:
            self.progress = max(0, min(100, progress))

        if message is not None:
            self.message = message

        if tool is not None:
            self.tool = tool

        self.updated_at = datetime.utcnow()

        if self.progress >= 100:

            self.completed_at = datetime.utcnow()

    @property
    def elapsed(self):
        """
        Elapsed scan time.
        """

        end = self.completed_at or datetime.utcnow()

        return round((end - self.started_at).total_seconds(), 2)

    def to_dict(self):
        """
        Return JSON serializable object.
        """

        return {
            "scan_id": self.scan_id,
            "target": self.target,
            "tool": self.tool,
            "status": self.status.value,
            "progress": self.progress,
            "message": self.message,
            "elapsed": self.elapsed,
            "started_at": self.started_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "completed_at": (
                self.completed_at.isoformat() if self.completed_at else None
            ),
        }
