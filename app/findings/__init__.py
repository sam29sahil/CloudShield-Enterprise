"""
CloudShield Enterprise
Findings Module
"""

from app.findings.severity import SeverityEngine
from app.findings.aggregator import FindingAggregator
from app.findings.deduplicator import Deduplicator
from app.findings.report_builder import ReportBuilder

# New Backend
from app.findings.services import FindingService
from app.findings.statistics import FindingStatistics
from app.findings.filters import FindingFilters
from app.findings.exporter import FindingExporter

__all__ = [

    # Existing
    "SeverityEngine",

    "FindingAggregator",

    "Deduplicator",

    "ReportBuilder",

    # New
    "FindingService",

    "FindingStatistics",

    "FindingFilters",

    "FindingExporter"

]

