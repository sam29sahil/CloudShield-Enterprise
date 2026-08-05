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

<<<<<<< HEAD
    def save(self, tool, target, status, execution_time, raw_output, parsed_output):

        scan = SecurityScan(
            tool=tool,
            target=target,
            status=status,
            execution_time=execution_time,
            raw_output=raw_output,
            parsed_output=parsed_output,
=======
    def save(

        self,

        tool,

        target,

        status,

        execution_time,

        raw_output,

        parsed_output

    ):

        scan = SecurityScan(

            tool=tool,

            target=target,

            status=status,

            execution_time=execution_time,

            raw_output=raw_output,

            parsed_output=parsed_output

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        db.session.add(scan)

        db.session.commit()

        return scan

    def all(self):

<<<<<<< HEAD
        return SecurityScan.query.order_by(SecurityScan.created_at.desc()).all()

    def get(self, scan_id):

        return SecurityScan.query.get(scan_id)

    def delete(self, scan_id):
=======
        return (

            SecurityScan.query

            .order_by(

                SecurityScan.created_at.desc()

            )

            .all()

        )

    def get(

        self,

        scan_id

    ):

        return SecurityScan.query.get(

            scan_id

        )

    def delete(

        self,

        scan_id

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        scan = self.get(scan_id)

        if scan:

            db.session.delete(scan)

            db.session.commit()

            return True

<<<<<<< HEAD
        return False
=======
        return False
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
