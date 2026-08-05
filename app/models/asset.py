"""
CloudShield Enterprise
Asset Model
"""

from app.extensions import db
from datetime import datetime


class Asset(db.Model):

    __tablename__ = "assets"

<<<<<<< HEAD
    id = db.Column(db.Integer, primary_key=True)

    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)

    name = db.Column(db.String(120), nullable=False)

    target = db.Column(db.String(255), nullable=False)

    asset_type = db.Column(db.String(50))

    score = db.Column(db.Integer, default=0)

    risk = db.Column(db.String(20), default="Unknown")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    scans = db.relationship(
        "SecurityScan", back_populates="asset", lazy=True, cascade="all, delete-orphan"
    )

    findings = db.relationship(
        "Finding", back_populates="asset", lazy=True, cascade="all, delete-orphan"
    )
=======
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    project_id = db.Column(

        db.Integer,

        db.ForeignKey("projects.id"),

        nullable=False

    )

    name = db.Column(

        db.String(120),

        nullable=False

    )

    target = db.Column(

        db.String(255),

        nullable=False

    )

    asset_type = db.Column(

        db.String(50)

    )

    score = db.Column(

        db.Integer,

        default=0

    )

    risk = db.Column(

        db.String(20),

        default="Unknown"

    )

    created_at = db.Column(

        db.DateTime,

        default=datetime.utcnow

    )

    scans = db.relationship(

        "SecurityScan",

        back_populates="asset",

        lazy=True,

        cascade="all, delete-orphan"


    )

    findings = db.relationship(

        "Finding",

        back_populates="asset",

        lazy=True,

        cascade="all, delete-orphan"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
