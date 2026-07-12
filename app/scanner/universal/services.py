"""
CloudShield Enterprise
Universal Scan Service
"""

from datetime import datetime

from app.extensions import db
from app.models import SecurityScan

from app.security.manager import SecurityManager
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

        result = self.manager.run_tool(

            tool,

            target,

            arguments

        )

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

            raw_output=result["raw_output"],

            parsed_output=str(result),

            started_at=started,

            completed_at=completed,

            duration=duration

        )

        db.session.add(scan)

        db.session.commit()

        if asset_id:

            AssetManager().update_scan(

                asset_id=asset_id,

                score=result["summary"].get("score", 0),

                risk=result["summary"].get("risk", "Unknown"),

                findings=0

            )

        return {

            "scan": scan,

            "result": result

        }

    def tools(self):

        return self.manager.tools()

    def categories(self):

        return self.manager.categories()