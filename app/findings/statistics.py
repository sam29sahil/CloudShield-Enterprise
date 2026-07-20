"""
CloudShield Enterprise
Finding Statistics Engine
"""

from sqlalchemy import func

from app.extensions import db
from app.models.finding import Finding


class FindingStatistics:

    """
    Enterprise Statistics Engine
    """

    # =====================================================
    # TOTAL
    # =====================================================

    @staticmethod
    def total():

        return Finding.query.count()

    # =====================================================
    # BY SEVERITY
    # =====================================================

    @staticmethod
    def severity():

        return {

            "Critical": Finding.query.filter_by(
                severity="Critical"
            ).count(),

            "High": Finding.query.filter_by(
                severity="High"
            ).count(),

            "Medium": Finding.query.filter_by(
                severity="Medium"
            ).count(),

            "Low": Finding.query.filter_by(
                severity="Low"
            ).count(),

            "Info": Finding.query.filter_by(
                severity="Info"
            ).count()

        }

    # =====================================================
    # BY STATUS
    # =====================================================

    @staticmethod
    def status():

        return {

            "Open": Finding.query.filter_by(
                status="Open"
            ).count(),

            "Resolved": Finding.query.filter_by(
                status="Resolved"
            ).count(),

            "False Positive": Finding.query.filter_by(
                false_positive=True
            ).count()

        }

    # =====================================================
    # SUMMARY
    # =====================================================

    @staticmethod
    def summary():

        return {

            "total": FindingStatistics.total(),

            "severity": FindingStatistics.severity(),

            "status": FindingStatistics.status()

        }
    
        # =====================================================
    # CATEGORY DISTRIBUTION
    # =====================================================

    @staticmethod
    def categories():

        rows = db.session.query(

            Finding.category,

            func.count(Finding.id)

        ).group_by(

            Finding.category

        ).all()

        return {

            category or "Unknown": count

            for category, count in rows

        }

    # =====================================================
    # TOP ASSETS
    # =====================================================

    @staticmethod
    def top_assets(limit=10):

        return db.session.query(

            Finding.asset_id,

            func.count(Finding.id).label("count")

        ).group_by(

            Finding.asset_id

        ).order_by(

            func.count(Finding.id).desc()

        ).limit(limit).all()

    # =====================================================
    # TOP PROJECTS
    # =====================================================

    @staticmethod
    def top_projects(limit=10):

        return db.session.query(

            Finding.project_id,

            func.count(Finding.id).label("count")

        ).group_by(

            Finding.project_id

        ).order_by(

            func.count(Finding.id).desc()

        ).limit(limit).all()

    # =====================================================
    # AVERAGE CVSS
    # =====================================================

    @staticmethod
    def average_cvss():

        value = db.session.query(

            func.avg(Finding.cvss)

        ).scalar()

        return round(value or 0, 2)

    # =====================================================
    # MAX CVSS
    # =====================================================

    @staticmethod
    def max_cvss():

        value = db.session.query(

            func.max(Finding.cvss)

        ).scalar()

        return round(value or 0, 2)

    # =====================================================
    # RISK SCORE
    # =====================================================

    @staticmethod
    def risk_score():

        weights = {

            "Critical": 10,

            "High": 7,

            "Medium": 5,

            "Low": 2,

            "Info": 0

        }

        findings = Finding.query.filter_by(

            status="Open"

        ).all()

        score = 0

        for finding in findings:

            score += weights.get(

                finding.severity,

                0

            )

        return score

    # =====================================================
    # DASHBOARD METRICS
    # =====================================================

    @staticmethod
    def dashboard():

        return {

            "summary": FindingStatistics.summary(),

            "categories": FindingStatistics.categories(),

            "top_assets": FindingStatistics.top_assets(),

            "top_projects": FindingStatistics.top_projects(),

            "average_cvss": FindingStatistics.average_cvss(),

            "max_cvss": FindingStatistics.max_cvss(),

            "risk_score": FindingStatistics.risk_score()

        }
    
        # =====================================================
    # FINDINGS BY TOOL
    # =====================================================

    @staticmethod
    def by_tool():

        rows = db.session.query(

            Finding.scan_id,

            func.count(Finding.id)

        ).group_by(

            Finding.scan_id

        ).all()

        return [

            {

                "scan": scan,

                "count": count

            }

            for scan, count in rows

        ]

    # =====================================================
    # FINDINGS BY DATE
    # =====================================================

    @staticmethod
    def by_date():

        rows = db.session.query(

            func.date(Finding.created_at),

            func.count(Finding.id)

        ).group_by(

            func.date(Finding.created_at)

        ).order_by(

            func.date(Finding.created_at)

        ).all()

        return [

            {

                "date": str(date),

                "count": count

            }

            for date, count in rows

        ]

    # =====================================================
    # MONTHLY TREND
    # =====================================================

    @staticmethod
    def monthly():

        rows = db.session.query(

            func.strftime(

                "%Y-%m",

                Finding.created_at

            ),

            func.count(Finding.id)

        ).group_by(

            func.strftime(

                "%Y-%m",

                Finding.created_at

            )

        ).all()

        return [

            {

                "month": month,

                "count": count

            }

            for month, count in rows

        ]

    # =====================================================
    # MEAN TIME TO RESOLVE
    # =====================================================

    @staticmethod
    def mttr():

        findings = Finding.query.filter(

            Finding.resolved_at.isnot(None)

        ).all()

        if not findings:

            return 0

        total = 0

        for finding in findings:

            total += (

                finding.resolved_at -

                finding.created_at

            ).total_seconds()

        return round(

            total /

            len(findings) /

            3600,

            2

        )

    # =====================================================
    # RECENTLY RESOLVED
    # =====================================================

    @staticmethod
    def recently_resolved(limit=10):

        return Finding.query.filter_by(

            status="Resolved"

        ).order_by(

            Finding.resolved_at.desc()

        ).limit(limit).all()

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    @staticmethod
    def executive_summary():

        return {

            "summary": FindingStatistics.summary(),

            "risk_score": FindingStatistics.risk_score(),

            "average_cvss": FindingStatistics.average_cvss(),

            "max_cvss": FindingStatistics.max_cvss(),

            "categories": FindingStatistics.categories(),

            "top_assets": FindingStatistics.top_assets(5),

            "top_projects": FindingStatistics.top_projects(5),

            "monthly": FindingStatistics.monthly(),

            "mttr": FindingStatistics.mttr()

        }