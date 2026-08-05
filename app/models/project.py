"""
CloudShield Enterprise
Project Model
"""

from app.extensions import db
from datetime import datetime


class Project(db.Model):

    __tablename__ = "projects"

<<<<<<< HEAD
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120), nullable=False)

    description = db.Column(db.Text)

    owner = db.Column(db.String(120))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    assets = db.relationship("Asset", backref="project", lazy=True)

    findings = db.relationship(
        "Finding", back_populates="project", lazy=True, cascade="all, delete-orphan"
    )
=======
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(120),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    owner = db.Column(
        db.String(120)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    assets = db.relationship(

        "Asset",

        backref="project",

        lazy=True

    )

    findings = db.relationship(

        "Finding",

        back_populates="project",
       
        lazy=True,

        cascade="all, delete-orphan"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
