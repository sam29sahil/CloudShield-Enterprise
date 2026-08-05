"""
CloudShield Enterprise
Security Scan Model
"""

from datetime import datetime

from app.extensions import db


class SecurityScan(db.Model):

    __tablename__ = "security_scans"

<<<<<<< HEAD
    id = db.Column(db.Integer, primary_key=True)

    tool = db.Column(db.String(50), nullable=False)

    target = db.Column(db.String(255), nullable=False)

    status = db.Column(db.String(30), default="Completed")

    execution_time = db.Column(db.Float, default=0)

    raw_output = db.Column(db.Text)

    parsed_output = db.Column(db.JSON)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
=======
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    tool = db.Column(
        db.String(50),
        nullable=False
    )

    target = db.Column(
        db.String(255),
        nullable=False
    )

    status = db.Column(
        db.String(30),
        default="Completed"
    )

    execution_time = db.Column(
        db.Float,
        default=0
    )

    raw_output = db.Column(
        db.Text
    )

    parsed_output = db.Column(
        db.JSON
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def to_dict(self):

        return {
<<<<<<< HEAD
            "id": self.id,
            "tool": self.tool,
            "target": self.target,
            "status": self.status,
            "execution_time": self.execution_time,
            "raw_output": self.raw_output,
            "parsed_output": self.parsed_output,
            "created_at": self.created_at.isoformat(),
=======

            "id": self.id,

            "tool": self.tool,

            "target": self.target,

            "status": self.status,

            "execution_time": self.execution_time,

            "raw_output": self.raw_output,

            "parsed_output": self.parsed_output,

            "created_at": self.created_at.isoformat()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    def __repr__(self):

<<<<<<< HEAD
        return f"<SecurityScan " f"{self.tool} " f"{self.target}>"
=======
        return (

            f"<SecurityScan "

            f"{self.tool} "

            f"{self.target}>"

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
