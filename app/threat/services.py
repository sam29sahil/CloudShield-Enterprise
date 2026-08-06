"""
CloudShield Enterprise
Threat Intelligence Services
"""

from app.threat.cve import CVEService
from app.threat.mitre import MITREService
from app.threat.ioc import IOCService
from app.threat.threat_feed import ThreatFeedService


class ThreatService:
    """
    Threat Intelligence Service
    """

    def __init__(self):

        self.cve = CVEService()
        self.mitre_service = MITREService()
        self.ioc_service = IOCService()
        self.feed_service = ThreatFeedService()

    # ---------------------------------------
    # Dashboard
    # ---------------------------------------

    def dashboard(self):

        summary = self.cve.summary()

        return {
            "critical_cves": summary["critical"],
            "high_cves": summary["high"],
            "medium_cves": summary["medium"],
            "low_cves": summary["low"],
            "ioc_count": self.ioc_service.count(),
            "feeds": self.feed_service.count(),
            "mitre_techniques": self.mitre_service.count(),
            "score": self.calculate_score(summary),
            "latest_cves": self.cve.latest(5),
        }

    # ---------------------------------------
    # CVE Functions
    # ---------------------------------------

    def all_cves(self):

        return self.cve.all()

    def latest_cves(self):

        return self.cve.latest()

    def search_cves(self, keyword):

        return self.cve.search(keyword)

    def critical_cves(self):

        return self.cve.by_severity("Critical")

    def high_cves(self):

        return self.cve.by_severity("High")

    def medium_cves(self):

        return self.cve.by_severity("Medium")

    def low_cves(self):

        return self.cve.by_severity("Low")
    def mitre(self):

        return self.mitre_service.all()

    def search_mitre(self, keyword):

        return self.mitre_service.search(keyword)
    def iocs(self):

        return self.ioc_service.all()

    def search_iocs(self, keyword):

        return self.ioc_service.search(keyword)

    def feeds(self):

        return self.feed_service.all()

    def latest_feeds(self):

        return self.feed_service.latest()

    # ---------------------------------------
    # Threat Score
    # ---------------------------------------

    def calculate_score(self, summary):

        score = 100

        score -= summary["critical"] * 15

        score -= summary["high"] * 8

        score -= summary["medium"] * 3

        score -= summary["low"]

        if score < 0:

            score = 0

        return score
