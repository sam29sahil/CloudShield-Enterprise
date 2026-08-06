"""
CloudShield Enterprise
Notification Model
"""

from datetime import datetime

from app.extensions import db


class Notification(db.Model):

    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    title = db.Column(db.String(150), nullable=False)

    message = db.Column(db.Text, nullable=False)

    severity = db.Column(db.String(20), default="Info")

    is_read = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    source = db.Column(db.String(50), default="System")

    icon = db.Column(db.String(50), default="bi-bell-fill")

    url = db.Column(db.String(255))

    def __repr__(self):

        return f"<Notification {self.title}>"
