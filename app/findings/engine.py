"""
CloudShield Enterprise
Finding Engine
"""

from app.extensions import db

from app.models.asset import Asset
from app.models.finding import Finding
from app.models.project import Project


class FindingEngine:
    """
    Universal Finding Engine

    All modules create findings through this class.

    Website Scanner
    Cloud Security
    Threat Intelligence
    Manual Findings
    """

    @staticmethod
    def create(
<<<<<<< HEAD
        scan,
        title,
        severity="Low",
        description="",
        recommendation="",
        category="General",
        cvss=0.0,
        evidence="",
        cwe=None,
        owasp=None,
=======

        scan,

        title,

        severity="Low",

        description="",

        recommendation="",

        category="General",

        cvss=0.0,

        evidence="",

        cwe=None,

        owasp=None

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    ):

        # ------------------------------------------
        # Get Asset
        # ------------------------------------------

        asset = None

        if scan.asset_id:

            asset = Asset.query.get(scan.asset_id)

        # ------------------------------------------
        # Determine Project
        # ------------------------------------------

        project_id = None

        if asset:

            project_id = asset.project_id

        else:

            project = Project.query.first()

            if project:

                project_id = project.id

        # ------------------------------------------
        # Safety Check
        # ------------------------------------------

        if project_id is None:

            print("FindingEngine: No project found.")

            return None

        # ------------------------------------------
        # Create Finding
        # ------------------------------------------

        finding = Finding(
<<<<<<< HEAD
            project_id=project_id,
            asset_id=scan.asset_id,
            scan_id=scan.id,
            title=title,
            description=description,
            severity=severity,
            cvss=cvss,
            cwe=cwe,
            owasp=owasp,
            category=category,
            recommendation=recommendation,
            evidence=evidence,
            status="Open",
=======

            project_id=project_id,

            asset_id=scan.asset_id,

            scan_id=scan.id,

            title=title,

            description=description,

            severity=severity,

            cvss=cvss,

            cwe=cwe,

            owasp=owasp,

            category=category,

            recommendation=recommendation,

            evidence=evidence,

            status="Open"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        db.session.add(finding)

        db.session.commit()

        print("=" * 60)
        print("FINDING CREATED")
        print("ID       :", finding.id)
        print("TITLE    :", finding.title)
        print("SEVERITY :", finding.severity)
        print("=" * 60)

<<<<<<< HEAD
        return finding
=======
        return finding
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
