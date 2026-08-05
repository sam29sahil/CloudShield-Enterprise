"""
CloudShield Enterprise
User Model
"""

from datetime import datetime

from flask_login import UserMixin

from app.extensions import db


class User(UserMixin, db.Model):

    __tablename__ = "users"

<<<<<<< HEAD
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(150), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    is_active_user = db.Column(db.Boolean, default=True)

    role = db.Column(db.String(30), default="User")

    def __repr__(self):

        return f"<User {self.username}>"
=======
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    is_active_user = db.Column(
        db.Boolean,
        default=True
    )

    role = db.Column(
        db.String(30),
        default="User"
    )

    def __repr__(self):

        return f"<User {self.username}>"
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
