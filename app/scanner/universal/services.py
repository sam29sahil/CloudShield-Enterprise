"""
CloudShield Enterprise
Universal Scan Service
"""
import json
from datetime import datetime

from app.extensions import db
from app.models import SecurityScan, Report
from app.scanner.live import ScanTracker

from app.security.core.manager import SecurityManager
from app.assets.services import AssetManager


class ScanService:
    """
    Universal Scan Service
    """

    def __init__(self):

        self.manager = SecurityManager()

    def execute(

        self,

        user_id,

        asset_id,

        category,

        tool,

        target,

        arguments=None

    ):

        started = datetime.utcnow()

        findings = FindingGenerator.generate(
        scan,
        esult
    )

        print("=" * 60)
        print("SCAN RESULT")
        print(result)
        print("=" * 60)

        completed = datetime.utcnow()

        duration = (

            completed - started

        ).total_seconds()

        scan = SecurityScan(

            user_id=user_id,

            asset_id=asset_id,

            category=category,

            tool=tool,

            target=target,

            arguments=" ".join(arguments)
            if arguments else "",

            status=result["summary"]["status"],

            score=result["summary"].get("score", 0),

            risk=result["summary"].get("risk", "Unknown"),

            raw_output=result["raw_output"],

            parsed_output=json.dumps(result, indent=2),

            started_at=started,

            completed_at=completed,

            duration=duration

        )

        db.session.add(scan)

        db.session.commit()

        tracker = ScanTracker(scan)

        tracker.start()

        tracker.validating()

        tracker.initializing()

        tracker.running(tool)

        print("=" * 60)
        print("SCAN ID :", scan.id)
        print("ASSET ID:", scan.asset_id)
        print("SCORE   :", scan.score)
        print("RISK    :", scan.risk)
        print("=" * 60)

        from app.findings.generator import FindingGenerator

        import inspect

        print("=" * 60)
        print("GENERATOR CLASS :", FindingGenerator)
        print("GENERATOR FILE  :", inspect.getfile(FindingGenerator))
        print("SIGNATURE       :", inspect.signature(FindingGenerator.generate))
        print("=" * 60)

        import traceback

        try:

            tracker.parsing()

            findings = FindingGenerator.generate(

                scan,

                report

            )

            tracker.findings()

            print("=" * 60)
            print(f"FINDINGS CREATED : {findings}")
            print("=" * 60)

        except Exception as e:

            tracker.failed(e)

            print("=" * 60)
            print("FINDING GENERATOR ERROR")
            traceback.print_exc()
            print("=" * 60)

        # --------------------------
        # Update Asset
        # --------------------------

        if asset_id:

            from app.models.finding import Finding

            count = Finding.query.filter_by(

                asset_id=asset_id

            ).count()

            AssetManager().update_scan(

                asset_id=asset_id,

                score=result["summary"].get("score", 0),

                risk=result["summary"].get("risk", "Unknown"),

                findings=count

            )

        # --------------------------
        # Live Scanner
        # --------------------------

        tracker.reporting()

        tracker.complete()

        return {

            "scan": scan,

            "result": result

        }

    def tools(self):

        return self.manager.tools()

    def categories(self):

        return self.manager.categories()