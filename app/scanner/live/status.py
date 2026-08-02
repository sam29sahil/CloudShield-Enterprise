"""
CloudShield Enterprise
Live Scanner Status
"""

from enum import Enum


class ScanStatus(str, Enum):
    """
    Scan lifecycle states.
    """

    QUEUED = "Queued"

    VALIDATING = "Validating Target"

    INITIALIZING = "Initializing Tool"

    RUNNING = "Running"

    PARSING = "Parsing Results"

    FINDINGS = "Generating Findings"

    REPORT = "Generating Report"

    COMPLETED = "Completed"

    FAILED = "Failed"

    CANCELLED = "Cancelled"


ACTIVE_STATES = {
    ScanStatus.QUEUED,
    ScanStatus.VALIDATING,
    ScanStatus.INITIALIZING,
    ScanStatus.RUNNING,
    ScanStatus.PARSING,
    ScanStatus.FINDINGS,
    ScanStatus.REPORT,
}


FINISHED_STATES = {
    ScanStatus.COMPLETED,
    ScanStatus.FAILED,
    ScanStatus.CANCELLED,
}