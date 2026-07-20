"""
CloudShield Enterprise
Enterprise Analytics Service
"""

from sqlalchemy import func, desc

from app.extensions import db
from app.models import (
    Asset,
    Finding,
    SecurityScan
)


class AnalyticsService:

    # ------------------------------------------
    # Dashboard Statistics
    # ------------------------------------------

    def statistics(self):

        total_assets = Asset.query.count()

        total_scans = SecurityScan.query.count()

        total_findings = Finding.query.count()

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

        success_rate = 0

        if total_scans:

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

        }

    # ------------------------------------------
    # Dashboard Summary Cards
    # ------------------------------------------

    def summary(self):

        return {

            "assets": Asset.query.count(),

            "scans": SecurityScan.query.count(),

            "findings": Finding.query.count(),

            "average_score": round(

                db.session.query(

                    func.avg(SecurityScan.score)

                ).scalar() or 0

            )

        }

    # ------------------------------------------
    # Severity Distribution
    # ------------------------------------------

    def severity(self):

        return {

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

        }

    # ------------------------------------------
    # Security Score Trend
    # ------------------------------------------

    def score_trend(self, limit=15):

        scans = (

            SecurityScan.query

            .order_by(

                desc(SecurityScan.started_at)

            )

            .limit(limit)

            .all()

        )

        scans.reverse()

        return {

            "labels": [

                scan.started_at.strftime("%d %b")

                for scan in scans

            ],

            "scores": [

                scan.score

                for scan in scans

            ]

        }

    # ------------------------------------------
    # Chart Data
    # ------------------------------------------

    def chart_data(self):

        trend = self.score_trend()

        severity = self.severity()

        return {

            "labels": trend["labels"],

            "scores": trend["scores"],

            "critical": severity["critical"],

            "high": severity["high"],

            "medium": severity["medium"],

            "low": severity["low"],

            "info": severity["info"]

        }
    
        # ------------------------------------------
    # Recent Scans
    # ------------------------------------------

    def recent_scans(self, limit=10):

        return (

            SecurityScan.query

            .order_by(

                SecurityScan.started_at.desc()

            )

            .limit(limit)

            .all()

        )

    # ------------------------------------------
    # Top Vulnerable Assets
    # ------------------------------------------

    def top_assets(self, limit=5):

        assets = (

            Asset.query

            .outerjoin(Finding)

            .group_by(Asset.id)

            .order_by(

                func.count(Finding.id).desc()

            )

            .limit(limit)

            .all()

        )

        return assets

    # ------------------------------------------
    # Scanner Usage
    # ------------------------------------------

    def scanner_usage(self):

        rows = (

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

        }

    # ------------------------------------------
    # Top Vulnerabilities
    # ------------------------------------------

    def top_vulnerabilities(self, limit=10):

        rows = (

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

    # ------------------------------------------
    # Performance Metrics
    # ------------------------------------------

    def performance(self):

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

        }

    # ------------------------------------------
    # Complete Dashboard Data
    # ------------------------------------------

    def dashboard_data(self):

        return {

            "summary": self.summary(),

            "statistics": self.statistics(),

            "severity": self.severity(),

            "charts": self.chart_data(),

            "trend": self.score_trend(),

            "recent_scans": self.recent_scans(),

            "top_assets": self.top_assets(),

            "scanner_usage": self.scanner_usage(),

            "top_vulnerabilities": self.top_vulnerabilities(),

            "performance": self.performance()

        }