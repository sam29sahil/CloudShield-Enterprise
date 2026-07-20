"""
CloudShield Enterprise
Report Model
"""

from app.extensions import db
from datetime import datetime


class Report(db.Model):

    __tablename__ = "reports"

    id = db.Column(

        db.Integer,

        primary_key=True

    )

    scan_id = db.Column(

        db.Integer,

        db.ForeignKey("security_scans.id"),

        nullable=False

    )

    report_type = db.Column(

        db.String(50)

    )

    file_name = db.Column(

        db.String(255)

    )

    created_at = db.Column(

        db.DateTime,

        default=datetime.utcnow

    )

    scan = db.relationship(

        "SecurityScan",

        backref="reports",

        lazy=True

    )