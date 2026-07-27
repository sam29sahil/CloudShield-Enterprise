"""
CloudShield Enterprise
Evidence Model
"""

from datetime import datetime

from app.extensions import db


class Evidence(db.Model):

    __tablename__ = "evidence"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    finding_id = db.Column(
        db.Integer,
        db.ForeignKey("findings.id"),   # <-- FIXED
        nullable=False
    )

    filename = db.Column(
        db.String(255),
        nullable=False
    )

    filepath = db.Column(
        db.String(500),
        nullable=False
    )

    filetype = db.Column(
        db.String(50)
    )

    uploaded_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    finding = db.relationship(
        "Finding",
        back_populates="evidence_files"
    )