from datetime import datetime

from flask_login import UserMixin

from app.extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

<<<<<<< HEAD
    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    is_active = db.Column(db.Boolean, default=True)

    is_admin = db.Column(db.Boolean, default=False)

    # Relationship
    scans = db.relationship(
        "ScanHistory", backref="user", lazy=True, cascade="all, delete-orphan"
=======
    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    is_admin = db.Column(
        db.Boolean,
        default=False
    )

    # Relationship
    scans = db.relationship(
        "ScanHistory",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )

    def __repr__(self):
        return f"<User {self.username}>"


class ScanHistory(db.Model):
    __tablename__ = "scan_history"

<<<<<<< HEAD
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    website = db.Column(db.String(255), nullable=False)

    status_code = db.Column(db.Integer)

    server = db.Column(db.String(255))

    https = db.Column(db.Boolean)

    response_time = db.Column(db.Float)

    security_score = db.Column(db.Integer)

    risk_level = db.Column(db.String(30))

    scanned_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ScanHistory {self.website}>"
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

    website = db.Column(
        db.String(255),
        nullable=False
    )

    status_code = db.Column(
        db.Integer
    )

    server = db.Column(
        db.String(255)
    )

    https = db.Column(
        db.Boolean
    )

    response_time = db.Column(
        db.Float
    )

    security_score = db.Column(
        db.Integer
    )

    risk_level = db.Column(
        db.String(30)
    )

    scanned_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<ScanHistory {self.website}>"
    
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
