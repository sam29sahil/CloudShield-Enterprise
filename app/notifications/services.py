"""
CloudShield Enterprise
Enterprise Notification Service
"""

from app.extensions import db
from app.notifications.models import Notification


class NotificationService:

    # ----------------------------------------
    # Create Notification
    # ----------------------------------------

    def create(
<<<<<<< HEAD
        self,
        user_id,
        title,
        message,
        severity="Info",
        source="System",
        icon="bi-bell-fill",
        url=None,
    ):

        notification = Notification(
            user_id=user_id,
            title=title,
            message=message,
            severity=severity,
            source=source,
            icon=icon,
            url=url,
=======

        self,

        user_id,

        title,

        message,

        severity="Info",

        source="System",

        icon="bi-bell-fill",

        url=None

    ):

        notification = Notification(

            user_id=user_id,

            title=title,

            message=message,

            severity=severity,

            source=source,

            icon=icon,

            url=url

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        db.session.add(notification)

        db.session.commit()

        return notification

    # ----------------------------------------
    # Scanner Notification
    # ----------------------------------------

<<<<<<< HEAD
    def scan_completed(self, user_id, target):

        return self.create(
            user_id=user_id,
            title="Scan Completed",
            message=f"Security scan completed for {target}.",
            severity="Info",
            source="Scanner",
            icon="bi-search",
=======
    def scan_completed(

        self,

        user_id,

        target

    ):

        return self.create(

            user_id=user_id,

            title="Scan Completed",

            message=f"Security scan completed for {target}.",

            severity="Info",

            source="Scanner",

            icon="bi-search"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

    # ----------------------------------------
    # High Risk Finding
    # ----------------------------------------

<<<<<<< HEAD
    def high_risk(self, user_id, finding):

        return self.create(
            user_id=user_id,
            title="High Risk Finding",
            message=f"{finding} detected.",
            severity="High",
            source="Scanner",
            icon="bi-exclamation-triangle-fill",
=======
    def high_risk(

        self,

        user_id,

        finding

    ):

        return self.create(

            user_id=user_id,

            title="High Risk Finding",

            message=f"{finding} detected.",

            severity="High",

            source="Scanner",

            icon="bi-exclamation-triangle-fill"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

    # ----------------------------------------
    # Report Generated
    # ----------------------------------------

<<<<<<< HEAD
    def report_generated(self, user_id, report):

        return self.create(
            user_id=user_id,
            title="Report Generated",
            message=f"{report} is ready.",
            severity="Info",
            source="Reports",
            icon="bi-file-earmark-pdf",
=======
    def report_generated(

        self,

        user_id,

        report

    ):

        return self.create(

            user_id=user_id,

            title="Report Generated",

            message=f"{report} is ready.",

            severity="Info",

            source="Reports",

            icon="bi-file-earmark-pdf"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

    # ----------------------------------------
    # Asset Added
    # ----------------------------------------

<<<<<<< HEAD
    def asset_added(self, user_id, asset):

        return self.create(
            user_id=user_id,
            title="New Asset Added",
            message=f"{asset} added successfully.",
            severity="Info",
            source="Assets",
            icon="bi-hdd-network",
=======
    def asset_added(

        self,

        user_id,

        asset

    ):

        return self.create(

            user_id=user_id,

            title="New Asset Added",

            message=f"{asset} added successfully.",

            severity="Info",

            source="Assets",

            icon="bi-hdd-network"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

    # ----------------------------------------
    # Get All
    # ----------------------------------------

<<<<<<< HEAD
    def all(self, user_id):

        return (
            Notification.query.filter_by(user_id=user_id)
            .order_by(Notification.created_at.desc())
            .all()
=======
    def all(

        self,

        user_id

    ):

        return (

            Notification.query

            .filter_by(

                user_id=user_id

            )

            .order_by(

                Notification.created_at.desc()

            )

            .all()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

    # ----------------------------------------
    # Recent
    # ----------------------------------------

<<<<<<< HEAD
    def recent(self, user_id, limit=5):

        return (
            Notification.query.filter_by(user_id=user_id)
            .order_by(Notification.created_at.desc())
            .limit(limit)
            .all()
=======
    def recent(

        self,

        user_id,

        limit=5

    ):

        return (

            Notification.query

            .filter_by(

                user_id=user_id

            )

            .order_by(

                Notification.created_at.desc()

            )

            .limit(limit)

            .all()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

    # ----------------------------------------
    # Unread
    # ----------------------------------------

<<<<<<< HEAD
    def unread(self, user_id):

        return (
            Notification.query.filter_by(user_id=user_id, is_read=False)
            .order_by(Notification.created_at.desc())
            .all()
=======
    def unread(

        self,

        user_id

    ):

        return (

            Notification.query

            .filter_by(

                user_id=user_id,

                is_read=False

            )

            .order_by(

                Notification.created_at.desc()

            )

            .all()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

    # ----------------------------------------
    # Count
    # ----------------------------------------

<<<<<<< HEAD
    def unread_count(self, user_id):

        return Notification.query.filter_by(user_id=user_id, is_read=False).count()
=======
    def unread_count(

        self,

        user_id

    ):

        return (

            Notification.query

            .filter_by(

                user_id=user_id,

                is_read=False

            )

            .count()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # ----------------------------------------
    # Mark Read
    # ----------------------------------------

<<<<<<< HEAD
    def mark_read(self, notification_id, user_id):

        notification = Notification.query.filter_by(
            id=notification_id, user_id=user_id
        ).first()
=======
    def mark_read(

        self,

        notification_id,

        user_id

    ):

        notification = (

            Notification.query

            .filter_by(

                id=notification_id,

                user_id=user_id

            )

            .first()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        if notification:

            notification.is_read = True

            db.session.commit()

        return notification

    # ----------------------------------------
    # Mark All
    # ----------------------------------------

<<<<<<< HEAD
    def mark_all_read(self, user_id):

        (
            Notification.query.filter_by(user_id=user_id, is_read=False).update(
                {"is_read": True}
            )
=======
    def mark_all_read(

        self,

        user_id

    ):

        (

            Notification.query

            .filter_by(

                user_id=user_id,

                is_read=False

            )

            .update(

                {

                    "is_read": True

                }

            )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        db.session.commit()

    # ----------------------------------------
    # Delete One
    # ----------------------------------------

<<<<<<< HEAD
    def delete(self, notification_id, user_id):

        notification = Notification.query.filter_by(
            id=notification_id, user_id=user_id
        ).first()
=======
    def delete(

        self,

        notification_id,

        user_id

    ):

        notification = (

            Notification.query

            .filter_by(

                id=notification_id,

                user_id=user_id

            )

            .first()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        if notification:

            db.session.delete(notification)

            db.session.commit()

    # ----------------------------------------
    # Delete All
    # ----------------------------------------

<<<<<<< HEAD
    def delete_all(self, user_id):

        (Notification.query.filter_by(user_id=user_id).delete())
=======
    def delete_all(

        self,

        user_id

    ):

        (

            Notification.query

            .filter_by(

                user_id=user_id

            )

            .delete()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        db.session.commit()

    # ----------------------------------------
    # Filter by Severity
    # ----------------------------------------

<<<<<<< HEAD
    def severity(self, user_id, severity):

        return (
            Notification.query.filter_by(user_id=user_id, severity=severity)
            .order_by(Notification.created_at.desc())
            .all()
        )
=======
    def severity(

        self,

        user_id,

        severity

    ):

        return (

            Notification.query

            .filter_by(

                user_id=user_id,

                severity=severity

            )

            .order_by(

                Notification.created_at.desc()

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
