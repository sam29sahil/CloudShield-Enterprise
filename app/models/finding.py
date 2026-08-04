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
        nullable=True
    )

    asset_id = db.Column(
        db.Integer,
        db.ForeignKey("assets.id"),
        nullable=True
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

    cwe = db.Column(

        db.String(30)

    )

    owasp = db.Column(

        db.String(30)

    )

    reference = db.Column(
        db.String(500)
    )

    mitre = db.Column(
        db.String(100)
    )

    vulnerability_type = db.Column(
        db.String(100)
    )

    category = db.Column(

        db.String(100)

    )

    recommendation = db.Column(
        db.Text
    )

    remediation = db.Column(
        db.Text
    )

    impact = db.Column(
        db.Text
    )

    affected_component = db.Column(
        db.String(255)
    )

    evidence = db.Column(
        db.Text
    )

    status = db.Column(
        db.String(20),
        default="Open"
    )

    verified = db.Column(
        db.Boolean,
        default=False
    )

    verified_by = db.Column(
        db.String(100)
    )

    verified_at = db.Column(
        db.DateTime
    )

    false_positive = db.Column(

        db.Boolean,

        default=False

    )

    resolved_at = db.Column(

        db.DateTime

    )

    updated_at = db.Column(

        db.DateTime,

        default=datetime.utcnow,

        onupdate=datetime.utcnow

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

    evidence_files = db.relationship(
        "Evidence",
        back_populates="finding",
        cascade="all, delete-orphan"
    )

    def __repr__(self):

        return (

            f"<Finding "

            f"{self.title} "

            f"({self.severity})>"

        )