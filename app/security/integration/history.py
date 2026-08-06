"""
CloudShield Enterprise
Scan History
"""

from app.extensions import db
from app.models import SecurityScan


class ScanHistory:
    """
    Store and retrieve scan history.
    """

    def save(self, tool, target, status, execution_time, raw_output, parsed_output):

        scan = SecurityScan(
            tool=tool,
            target=target,
            status=status,
            execution_time=execution_time,
            raw_output=raw_output,
            parsed_output=parsed_output,
        )

        db.session.add(scan)

        db.session.commit()

        return scan

    def all(self):

        return SecurityScan.query.order_by(SecurityScan.created_at.desc()).all()

    def get(self, scan_id):

        return SecurityScan.query.get(scan_id)

    def delete(self, scan_id):

        scan = self.get(scan_id)

        if scan:

            db.session.delete(scan)

            db.session.commit()

            return True

        return False
