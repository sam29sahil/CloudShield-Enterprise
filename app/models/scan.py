"""
CloudShield Enterprise
Scan Model
"""

from datetime import datetime

from app.extensions import db


class Scan(db.Model):

    __tablename__ = "scans"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    asset_id = db.Column(
        db.Integer,
        db.ForeignKey("assets.id"),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    score = db.Column(
        db.Integer,
        default=0
    )

    risk = db.Column(
        db.String(20),
        default="Low"
    )

    scan_type = db.Column(
        db.String(50),
        nullable=False
    )

    started_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    completed_at = db.Column(
        db.DateTime
    )

   
    findings = db.relationship(
        "Finding",
        backref="scan",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # -------------------------
    # Compatibility Properties
    # -------------------------

    @property
    def security_score(self):
        return self.score

    @property
    def risk_level(self):
        return self.risk

    @property
    def scanned_at(self):
        return self.started_at

    @property
    def website(self):
        from app.models.asset import Asset

        asset = Asset.query.get(self.asset_id)

        if asset:

            return asset.target


        return "Unknown"

    @property
    def status_code(self):
        return "200"

    @property
    def https(self):
        from app.models.asset import Asset

        asset = Asset.query.get(self.asset_id)

        if asset:
            return asset.target.startswith("https")
        return False

    def to_dict(self):

        return {

            "id": self.id,

            "asset_id": self.asset_id,

            "user_id": self.user_id,

            "score": self.score,

            "risk": self.risk,

            "scan_type": self.scan_type,

            "started_at": self.started_at.isoformat()
            if self.started_at else None,

            "completed_at": self.completed_at.isoformat()
            if self.completed_at else None

        }

    def __repr__(self):

        return f"<Scan {self.id}>"