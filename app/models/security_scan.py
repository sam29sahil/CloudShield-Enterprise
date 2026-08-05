"""
CloudShield Enterprise
Universal Security Scan Model
"""

from datetime import datetime

from app.extensions import db


class SecurityScan(db.Model):

    __tablename__ = "security_scans"

<<<<<<< HEAD
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    asset_id = db.Column(db.Integer, db.ForeignKey("assets.id"), nullable=True)

    category = db.Column(db.String(50), nullable=False)

    tool = db.Column(db.String(100), nullable=False)

    target = db.Column(db.String(255), nullable=False)

    arguments = db.Column(db.Text)

    status = db.Column(db.String(20), default="Pending")

    score = db.Column(db.Integer, default=0)

    risk = db.Column(db.String(20), default="Unknown")

    raw_output = db.Column(db.Text)

    parsed_output = db.Column(db.Text)

    started_at = db.Column(db.DateTime, default=datetime.utcnow)

    completed_at = db.Column(db.DateTime)

    duration = db.Column(db.Float, default=0)

    asset = db.relationship("Asset", back_populates="scans")

    findings = db.relationship(
        "Finding", back_populates="scan", lazy=True, cascade="all, delete-orphan"
    )

    def __repr__(self):

        return f"<SecurityScan " f"{self.tool} " f"{self.target}>"
=======
    id = db.Column(

        db.Integer,

        primary_key=True

    )

    user_id = db.Column(

        db.Integer,

        db.ForeignKey("users.id"),

        nullable=False

    )

    asset_id = db.Column(

        db.Integer,

        db.ForeignKey("assets.id"),

        nullable=True

    )

    category = db.Column(

        db.String(50),

        nullable=False

    )

    tool = db.Column(

        db.String(100),

        nullable=False

    )

    target = db.Column(

        db.String(255),

        nullable=False

    )

    arguments = db.Column(

        db.Text

    )

    status = db.Column(

        db.String(20),

        default="Pending"

    )

    score = db.Column(

        db.Integer,

        default=0

    )

    risk = db.Column(

        db.String(20),

        default="Unknown"

    )

    raw_output = db.Column(

        db.Text

    )

    parsed_output = db.Column(

        db.Text

    )

    started_at = db.Column(

        db.DateTime,

        default=datetime.utcnow

    )

    completed_at = db.Column(

        db.DateTime

    )

    duration = db.Column(

        db.Float,

        default=0

    )

    asset = db.relationship(

        "Asset",

        back_populates="scans"

    )

    findings = db.relationship(

        "Finding",

        back_populates="scan",

        lazy=True,

        cascade="all, delete-orphan"

    )
    def __repr__(self):

        return (

            f"<SecurityScan "

            f"{self.tool} "

            f"{self.target}>"

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
