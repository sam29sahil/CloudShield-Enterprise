"""
CloudShield Enterprise
Enterprise Analytics Service
"""

from sqlalchemy import func, desc
from app.cloud.azure.services import AzureService

from app.extensions import db
<<<<<<< HEAD
from app.models import Asset, Finding, SecurityScan
=======
from app.models import (
    Asset,
    Finding,
    SecurityScan
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


class AnalyticsService:

    def __init__(self):

        self.azure = AzureService()

<<<<<<< HEAD
    # ------------------------------------------
=======
     # ------------------------------------------
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # Cloud Analytics
    # ------------------------------------------

    def cloud(self):

<<<<<<< HEAD
        return self.azure.summary()
=======
        return self.azure.summary()   
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # ------------------------------------------
    # Dashboard Statistics
    # ------------------------------------------

    def statistics(self):

        total_assets = Asset.query.count()

        total_scans = SecurityScan.query.count()

        total_findings = Finding.query.count()

<<<<<<< HEAD
        average_score = db.session.query(func.avg(SecurityScan.score)).scalar() or 0

        average_duration = (
            db.session.query(func.avg(SecurityScan.duration)).scalar() or 0
        )

        completed = SecurityScan.query.filter_by(status="Completed").count()

        failed = SecurityScan.query.filter_by(status="Failed").count()
=======
        average_score = db.session.query(
            func.avg(SecurityScan.score)
        ).scalar() or 0

        average_duration = db.session.query(
            func.avg(SecurityScan.duration)
        ).scalar() or 0

        completed = SecurityScan.query.filter_by(
            status="Completed"
        ).count()

        failed = SecurityScan.query.filter_by(
            status="Failed"
        ).count()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        success_rate = 0

        if total_scans:

<<<<<<< HEAD
            success_rate = round(completed * 100 / total_scans, 1)

        return {
            "total_assets": total_assets,
            "total_scans": total_scans,
            "total_findings": total_findings,
            "average_score": round(average_score),
            "average_duration": round(average_duration, 2),
            "completed": completed,
            "failed": failed,
            "success_rate": success_rate,
=======
            success_rate = round(
                completed * 100 / total_scans,
                1
            )

        return {

            "total_assets": total_assets,

            "total_scans": total_scans,

            "total_findings": total_findings,

            "average_score": round(average_score),

            "average_duration": round(
                average_duration,
                2
            ),

            "completed": completed,

            "failed": failed,

            "success_rate": success_rate

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # ------------------------------------------
    # Dashboard Summary Cards
    # ------------------------------------------

    def summary(self):

        return {
<<<<<<< HEAD
            "assets": Asset.query.count(),
            "scans": SecurityScan.query.count(),
            "findings": Finding.query.count(),
            "average_score": round(
                db.session.query(func.avg(SecurityScan.score)).scalar() or 0
            ),
            "security_score": self.security_score(),
=======

            "assets": Asset.query.count(),

            "scans": SecurityScan.query.count(),

            "findings": Finding.query.count(),

            "average_score": round(

                db.session.query(

                    func.avg(SecurityScan.score)

                ).scalar() or 0

            ),

            "security_score": self.security_score(),

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # ------------------------------------------
    # Severity Distribution
    # ------------------------------------------

    def severity(self):

        return {
<<<<<<< HEAD
            "critical": Finding.query.filter_by(severity="Critical").count(),
            "high": Finding.query.filter_by(severity="High").count(),
            "medium": Finding.query.filter_by(severity="Medium").count(),
            "low": Finding.query.filter_by(severity="Low").count(),
            "info": Finding.query.filter_by(severity="Info").count(),
=======

            "critical": Finding.query.filter_by(
                severity="Critical"
            ).count(),

            "high": Finding.query.filter_by(
                severity="High"
            ).count(),

            "medium": Finding.query.filter_by(
                severity="Medium"
            ).count(),

            "low": Finding.query.filter_by(
                severity="Low"
            ).count(),

            "info": Finding.query.filter_by(
                severity="Info"
            ).count()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # ------------------------------------------
    # Security Score Trend
    # ------------------------------------------

    def score_trend(self, limit=15):

        scans = (
<<<<<<< HEAD
            SecurityScan.query.order_by(desc(SecurityScan.started_at))
            .limit(limit)
            .all()
=======

            SecurityScan.query

            .order_by(

                desc(SecurityScan.started_at)

            )

            .limit(limit)

            .all()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        scans.reverse()

        return {
<<<<<<< HEAD
            "labels": [scan.started_at.strftime("%d %b") for scan in scans],
            "scores": [scan.score for scan in scans],
=======

            "labels": [

                scan.started_at.strftime("%d %b")

                for scan in scans

            ],

            "scores": [

                scan.score

                for scan in scans

            ]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # ------------------------------------------
    # Chart Data
    # ------------------------------------------

    def chart_data(self):

        trend = self.score_trend()

        severity = self.severity()

        return {
<<<<<<< HEAD
            "labels": trend["labels"],
            "scores": trend["scores"],
            "critical": severity["critical"],
            "high": severity["high"],
            "medium": severity["medium"],
            "low": severity["low"],
            "info": severity["info"],
        }

        # ------------------------------------------

=======

            "labels": trend["labels"],

            "scores": trend["scores"],

            "critical": severity["critical"],

            "high": severity["high"],

            "medium": severity["medium"],

            "low": severity["low"],

            "info": severity["info"]

        }
    
        # ------------------------------------------
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # Recent Scans
    # ------------------------------------------

    def recent_scans(self, limit=10):

        return (
<<<<<<< HEAD
            SecurityScan.query.order_by(SecurityScan.started_at.desc())
            .limit(limit)
            .all()
=======

            SecurityScan.query

            .order_by(

                SecurityScan.started_at.desc()

            )

            .limit(limit)

            .all()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

    # ------------------------------------------
    # Top Vulnerable Assets
    # ------------------------------------------

    def top_assets(self, limit=5):

        assets = (
<<<<<<< HEAD
            Asset.query.outerjoin(Finding)
            .group_by(Asset.id)
            .order_by(func.count(Finding.id).desc())
            .limit(limit)
            .all()
=======

            Asset.query

            .outerjoin(Finding)

            .group_by(Asset.id)

            .order_by(

                func.count(Finding.id).desc()

            )

            .limit(limit)

            .all()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        return assets

    # ------------------------------------------
    # Scanner Usage
    # ------------------------------------------

    def scanner_usage(self):

        rows = (
<<<<<<< HEAD
            db.session.query(SecurityScan.tool, func.count(SecurityScan.id))
            .group_by(SecurityScan.tool)
            .all()
        )

        return {
            "labels": [row[0] or "Unknown" for row in rows],
            "values": [row[1] for row in rows],
=======

            db.session.query(

                SecurityScan.tool,

                func.count(SecurityScan.id)

            )

            .group_by(

                SecurityScan.tool

            )

            .all()

        )

        return {

            "labels": [

                row[0] or "Unknown"

                for row in rows

            ],

            "values": [

                row[1]

                for row in rows

            ]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # ------------------------------------------
    # Top Vulnerabilities
    # ------------------------------------------

    def top_vulnerabilities(self, limit=10):

        rows = (
<<<<<<< HEAD
            db.session.query(Finding.title, func.count(Finding.id))
            .group_by(Finding.title)
            .order_by(func.count(Finding.id).desc())
            .limit(limit)
            .all()
        )

        return [{"title": row[0], "count": row[1]} for row in rows]
=======

            db.session.query(

                Finding.title,

                func.count(Finding.id)

            )

            .group_by(

                Finding.title

            )

            .order_by(

                func.count(Finding.id).desc()

            )

            .limit(limit)

            .all()

        )

        return [

            {

                "title": row[0],

                "count": row[1]

            }

            for row in rows

        ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # ------------------------------------------
    # Performance Metrics
    # ------------------------------------------

    def performance(self):

<<<<<<< HEAD
        avg_duration = db.session.query(func.avg(SecurityScan.duration)).scalar() or 0

        max_duration = db.session.query(func.max(SecurityScan.duration)).scalar() or 0

        min_duration = db.session.query(func.min(SecurityScan.duration)).scalar() or 0

        return {
            "average": round(avg_duration, 2),
            "maximum": round(max_duration, 2),
            "minimum": round(min_duration, 2),
=======
        avg_duration = db.session.query(

            func.avg(SecurityScan.duration)

        ).scalar() or 0

        max_duration = db.session.query(

            func.max(SecurityScan.duration)

        ).scalar() or 0

        min_duration = db.session.query(

            func.min(SecurityScan.duration)

        ).scalar() or 0

        return {

            "average": round(avg_duration, 2),

            "maximum": round(max_duration, 2),

            "minimum": round(min_duration, 2)

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # ------------------------------------------
    # Complete Dashboard Data
    # ------------------------------------------

    def dashboard_data(self):

        return {
<<<<<<< HEAD
            "summary": self.summary(),
            "statistics": self.statistics(),
            "severity": self.severity(),
            "charts": self.chart_data(),
            "trend": self.score_trend(),
            "recent_scans": self.recent_scans(),
            "top_assets": self.top_assets(),
            "scanner_usage": self.scanner_usage(),
            "top_vulnerabilities": self.top_vulnerabilities(),
            "performance": self.performance(),
            "cloud": self.cloud(),
        }
=======

        "summary": self.summary(),

        "statistics": self.statistics(),

        "severity": self.severity(),

        "charts": self.chart_data(),

        "trend": self.score_trend(),

        "recent_scans": self.recent_scans(),

        "top_assets": self.top_assets(),

        "scanner_usage": self.scanner_usage(),

        "top_vulnerabilities": self.top_vulnerabilities(),

        "performance": self.performance(),

        "cloud": self.cloud()

    }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # ------------------------------------------
    # Overall Security Score
    # ------------------------------------------

    def security_score(self):

<<<<<<< HEAD
        average = db.session.query(func.avg(SecurityScan.score)).scalar() or 0
=======
        average = db.session.query(

            func.avg(SecurityScan.score)

        ).scalar() or 0
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        cloud = self.azure.summary()

        azure_score = cloud.get("secure_score", average)

<<<<<<< HEAD
        return round((average + azure_score) / 2)
=======
        return round(

            (average + azure_score) / 2

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
