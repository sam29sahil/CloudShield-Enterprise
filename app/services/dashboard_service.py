"""
CloudShield Enterprise
Dashboard Service
"""

from app.models.asset import Asset
from app.models.security_scan import SecurityScan
from app.models.finding import Finding


class DashboardService:

    def statistics(self):

        total_assets = Asset.query.count()

        total_scans = SecurityScan.query.count()

        total_findings = Finding.query.count()

<<<<<<< HEAD
        critical = Finding.query.filter_by(severity="Critical").count()

        high = Finding.query.filter_by(severity="High").count()

        medium = Finding.query.filter_by(severity="Medium").count()

        low = Finding.query.filter_by(severity="Low").count()

        return {
            "assets": total_assets,
            "scans": total_scans,
            "findings": total_findings,
            "critical": critical,
            "high": high,
            "medium": medium,
            "low": low,
=======
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

        return {

            "assets": total_assets,

            "scans": total_scans,

            "findings": total_findings,

            "critical": critical,

            "high": high,

            "medium": medium,

            "low": low

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    def latest_Securityscans(self, limit=10):

<<<<<<< HEAD
        return SecurityScan.query.order_by(Scan.started_at.desc()).limit(limit).all()
=======
        return SecurityScan.query.order_by(

            Scan.started_at.desc()

        ).limit(limit).all()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
