"""
CloudShield Enterprise
Report Service
"""

from app.models import SecurityScan


class ReportService:

    def get_scan(self, scan_id):
        """
        Get scan by ID.
        """

        return SecurityScan.query.get_or_404(scan_id)

    def report_data(self, scan_id):

        scan = self.get_scan(scan_id)

        return {
<<<<<<< HEAD
            "id": scan.id,
            "target": scan.target,
            "category": scan.category,
            "tool": scan.tool,
            "status": scan.status,
            "score": scan.score,
            "risk": scan.risk,
            "started_at": scan.started_at,
            "completed_at": scan.completed_at,
        }
=======

            "id": scan.id,

            "target": scan.target,

            "category": scan.category,

            "tool": scan.tool,

            "status": scan.status,

            "score": scan.score,

            "risk": scan.risk,

            "started_at": scan.started_at,

            "completed_at": scan.completed_at

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
