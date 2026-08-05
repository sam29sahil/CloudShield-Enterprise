"""
CloudShield Enterprise
Scan Service
"""

from datetime import datetime

from app.extensions import db
from app.models.security_scan import SecurityScan


class ScanService:

    def create(self, asset_id, score, risk, scan_type="Website"):

        scan = Scan(
            asset_id=asset_id,
            score=score,
            risk=risk,
            scan_type=scan_type,
            completed_at=datetime.utcnow(),
        )

        db.session.add(scan)

        db.session.commit()

        return scan

    def get(self, scan_id):

        return SecurityScan.query.get(scan_id)

    def all(self):

        return SecurityScan.query.order_by(Scan.started_at.desc()).all()

    def asset_scans(self, asset_id):

        return SecurityScan.query.filter_by(asset_id=asset_id).all()
