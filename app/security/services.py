"""
CloudShield Enterprise
Security Service
"""

from app.models import SecurityScan
from app.models.finding import Finding
from app.models.report import Report
from app.notifications.models import Notification

from app.security.core.engine import UniversalScannerEngine


class SecurityService:
    """
    Enterprise Security Service

    Acts as the bridge between:

        Scanner
            ↓
        Security Engine
            ↓
        Database
    """

    def __init__(self):

        self.engine = UniversalScannerEngine()

    # =====================================================
    # Scanner
    # =====================================================

    def execute(
        self,
        user_id,
        asset_id,
        mode,
        category,
        tool,
        target,
        arguments=None
    ):

        if arguments is None:

            arguments = []

        if mode == "basic":

            return self.engine.scan_profile(

                target=target,

                profile="quick",

                arguments=arguments

            )

        return self.engine.scan(

            target=target,

            tool=tool,

            arguments=arguments

        )

    # =====================================================
    # Dashboard
    # =====================================================

    def dashboard(self):

        scans = SecurityScan.query.count()

        findings = Finding.query.count()

        reports = Report.query.count()

        critical = Finding.query.filter_by(

            severity="Critical"

        ).count()

        high = Finding.query.filter_by(

            severity="High"

        ).count()

        medium = Finding.query.filter_by(

            severity="Medium"

        ).count()

        low = Finding.query.filter_by(

            severity="Low"

        ).count()

        latest = SecurityScan.query.order_by(

            SecurityScan.started_at.desc()

        ).first()

        score = 100

        if latest:

            score = latest.score

        return {

            "score": score,

            "risk_level": (

                latest.risk

                if latest

                else "Unknown"

            ),

            "total_scans": scans,

            "findings": findings,

            "reports": reports,

            "critical": critical,

            "high": high,

            "medium": medium,

            "low": low

        }

    # =====================================================
    # Findings
    # =====================================================

    def findings(self):

        return Finding.query.order_by(

            Finding.created_at.desc()

        ).all()

    # =====================================================
    # Reports
    # =====================================================

    def reports(self):

        return Report.query.order_by(

            Report.created_at.desc()

        ).all()

    # =====================================================
    # Threats
    # =====================================================

    def threats(self):

        return Finding.query.filter(

            Finding.severity.in_(

                [

                    "Critical",

                    "High"

                ]

            )

        ).all()

    # =====================================================
    # Statistics
    # =====================================================

    def statistics(self):

        dashboard = self.dashboard()

        return {

            "dashboard": dashboard,

            "notifications": Notification.query.count()

        }

    # =====================================================
    # Metadata
    # =====================================================

    def available_categories(self):

        return self.engine.categories()

    def available_tools(self, category):

        return self.engine.tools(category)