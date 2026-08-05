"""
CloudShield Enterprise
Finding Statistics Engine
"""

from sqlalchemy import func

from app.extensions import db
from app.models.finding import Finding


class FindingStatistics:
<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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
<<<<<<< HEAD
            "Critical": Finding.query.filter_by(severity="Critical").count(),
            "High": Finding.query.filter_by(severity="High").count(),
            "Medium": Finding.query.filter_by(severity="Medium").count(),
            "Low": Finding.query.filter_by(severity="Low").count(),
            "Info": Finding.query.filter_by(severity="Info").count(),
=======

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

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # BY STATUS
    # =====================================================

    @staticmethod
    def status():

        return {
<<<<<<< HEAD
            "Open": Finding.query.filter_by(status="Open").count(),
            "Resolved": Finding.query.filter_by(status="Resolved").count(),
            "False Positive": Finding.query.filter_by(false_positive=True).count(),
=======

            "Open": Finding.query.filter_by(
                status="Open"
            ).count(),

            "Resolved": Finding.query.filter_by(
                status="Resolved"
            ).count(),

            "False Positive": Finding.query.filter_by(
                false_positive=True
            ).count()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # SUMMARY
    # =====================================================

    @staticmethod
    def summary():

        return {
<<<<<<< HEAD
            "total": FindingStatistics.total(),
            "severity": FindingStatistics.severity(),
            "status": FindingStatistics.status(),
        }

        # =====================================================

=======

            "total": FindingStatistics.total(),

            "severity": FindingStatistics.severity(),

            "status": FindingStatistics.status()

        }
    
        # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # CATEGORY DISTRIBUTION
    # =====================================================

    @staticmethod
    def categories():

<<<<<<< HEAD
        rows = (
            db.session.query(Finding.category, func.count(Finding.id))
            .group_by(Finding.category)
            .all()
        )

        return {category or "Unknown": count for category, count in rows}
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # TOP ASSETS
    # =====================================================

    @staticmethod
    def top_assets(limit=10):

<<<<<<< HEAD
        return (
            db.session.query(Finding.asset_id, func.count(Finding.id).label("count"))
            .group_by(Finding.asset_id)
            .order_by(func.count(Finding.id).desc())
            .limit(limit)
            .all()
        )
=======
        return db.session.query(

            Finding.asset_id,

            func.count(Finding.id).label("count")

        ).group_by(

            Finding.asset_id

        ).order_by(

            func.count(Finding.id).desc()

        ).limit(limit).all()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # TOP PROJECTS
    # =====================================================

    @staticmethod
    def top_projects(limit=10):

<<<<<<< HEAD
        return (
            db.session.query(Finding.project_id, func.count(Finding.id).label("count"))
            .group_by(Finding.project_id)
            .order_by(func.count(Finding.id).desc())
            .limit(limit)
            .all()
        )
=======
        return db.session.query(

            Finding.project_id,

            func.count(Finding.id).label("count")

        ).group_by(

            Finding.project_id

        ).order_by(

            func.count(Finding.id).desc()

        ).limit(limit).all()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # AVERAGE CVSS
    # =====================================================

    @staticmethod
    def average_cvss():

<<<<<<< HEAD
        value = db.session.query(func.avg(Finding.cvss)).scalar()
=======
        value = db.session.query(

            func.avg(Finding.cvss)

        ).scalar()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return round(value or 0, 2)

    # =====================================================
    # MAX CVSS
    # =====================================================

    @staticmethod
    def max_cvss():

<<<<<<< HEAD
        value = db.session.query(func.max(Finding.cvss)).scalar()
=======
        value = db.session.query(

            func.max(Finding.cvss)

        ).scalar()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return round(value or 0, 2)

    # =====================================================
    # RISK SCORE
    # =====================================================

    @staticmethod
    def risk_score():

<<<<<<< HEAD
        weights = {"Critical": 10, "High": 7, "Medium": 5, "Low": 2, "Info": 0}

        findings = Finding.query.filter_by(status="Open").all()
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        score = 0

        for finding in findings:

<<<<<<< HEAD
            score += weights.get(finding.severity, 0)
=======
            score += weights.get(

                finding.severity,

                0

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return score

    # =====================================================
    # DASHBOARD METRICS
    # =====================================================

    @staticmethod
    def dashboard():

        return {
<<<<<<< HEAD
            "summary": FindingStatistics.summary(),
            "categories": FindingStatistics.categories(),
            "top_assets": FindingStatistics.top_assets(),
            "top_projects": FindingStatistics.top_projects(),
            "average_cvss": FindingStatistics.average_cvss(),
            "max_cvss": FindingStatistics.max_cvss(),
            "risk_score": FindingStatistics.risk_score(),
        }

        # =====================================================

=======

            "summary": FindingStatistics.summary(),

            "categories": FindingStatistics.categories(),

            "top_assets": FindingStatistics.top_assets(),

            "top_projects": FindingStatistics.top_projects(),

            "average_cvss": FindingStatistics.average_cvss(),

            "max_cvss": FindingStatistics.max_cvss(),

            "risk_score": FindingStatistics.risk_score()

        }
    
        # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # FINDINGS BY TOOL
    # =====================================================

    @staticmethod
    def by_tool():

<<<<<<< HEAD
        rows = (
            db.session.query(Finding.scan_id, func.count(Finding.id))
            .group_by(Finding.scan_id)
            .all()
        )

        return [{"scan": scan, "count": count} for scan, count in rows]
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # FINDINGS BY DATE
    # =====================================================

    @staticmethod
    def by_date():

<<<<<<< HEAD
        rows = (
            db.session.query(func.date(Finding.created_at), func.count(Finding.id))
            .group_by(func.date(Finding.created_at))
            .order_by(func.date(Finding.created_at))
            .all()
        )

        return [{"date": str(date), "count": count} for date, count in rows]
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # MONTHLY TREND
    # =====================================================

    @staticmethod
    def monthly():

<<<<<<< HEAD
        rows = (
            db.session.query(
                func.strftime("%Y-%m", Finding.created_at), func.count(Finding.id)
            )
            .group_by(func.strftime("%Y-%m", Finding.created_at))
            .all()
        )

        return [{"month": month, "count": count} for month, count in rows]
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # MEAN TIME TO RESOLVE
    # =====================================================

    @staticmethod
    def mttr():

<<<<<<< HEAD
        findings = Finding.query.filter(Finding.resolved_at.isnot(None)).all()
=======
        findings = Finding.query.filter(

            Finding.resolved_at.isnot(None)

        ).all()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        if not findings:

            return 0

        total = 0

        for finding in findings:

<<<<<<< HEAD
            total += (finding.resolved_at - finding.created_at).total_seconds()

        return round(total / len(findings) / 3600, 2)
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # RECENTLY RESOLVED
    # =====================================================

    @staticmethod
    def recently_resolved(limit=10):

<<<<<<< HEAD
        return (
            Finding.query.filter_by(status="Resolved")
            .order_by(Finding.resolved_at.desc())
            .limit(limit)
            .all()
        )
=======
        return Finding.query.filter_by(

            status="Resolved"

        ).order_by(

            Finding.resolved_at.desc()

        ).limit(limit).all()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    @staticmethod
    def executive_summary():

        return {
<<<<<<< HEAD
            "summary": FindingStatistics.summary(),
            "risk_score": FindingStatistics.risk_score(),
            "average_cvss": FindingStatistics.average_cvss(),
            "max_cvss": FindingStatistics.max_cvss(),
            "categories": FindingStatistics.categories(),
            "top_assets": FindingStatistics.top_assets(5),
            "top_projects": FindingStatistics.top_projects(5),
            "monthly": FindingStatistics.monthly(),
            "mttr": FindingStatistics.mttr(),
        }
=======

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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
