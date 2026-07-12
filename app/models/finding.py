"""
CloudShield Enterprise
Finding Model
"""

from datetime import datetime

from app.extensions import db


class Finding(db.Model):

    __tablename__ = "findings"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    project_id = db.Column(
        db.Integer,
        db.ForeignKey("projects.id"),
        nullable=False
    )

    asset_id = db.Column(
        db.Integer,
        db.ForeignKey("assets.id"),
        nullable=False
    )

    scan_id = db.Column(
        db.Integer,
        db.ForeignKey("security_scans.id"),
        nullable=False
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    severity = db.Column(
        db.String(20),
        default="Low"
    )

    cvss = db.Column(
        db.Float,
        default=0.0
    )

    recommendation = db.Column(
        db.Text
    )

    evidence = db.Column(
        db.Text
    )

    status = db.Column(
        db.String(20),
        default="Open"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    project = db.relationship(

        "Project",

        back_populates="findings"

    )

    asset = db.relationship(

        "Asset",

        back_populates="findings"

    )

    scan = db.relationship(

        "SecurityScan",

        back_populates="findings"

    )