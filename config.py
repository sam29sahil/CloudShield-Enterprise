"""
CloudShield Enterprise
Configuration
"""

import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    # ==========================================
    # Flask
    # ==========================================

    SECRET_KEY = e371ed3e8da2b5c0c6e953762e1e1f7c90f812d602c020cf2f6e5656da697611

    # ==========================================
    # Database
    # ==========================================

    SQLALCHEMY_DATABASE_URI =  os.getenv(
    "DATABASE_URL",
    "sqlite:///cloudshield.db"
)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ==========================================
    # File Upload
    # ==========================================

    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "static",
        "uploads",
        "findings"
    )

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024   # 16 MB

    ALLOWED_EVIDENCE_EXTENSIONS = {
        "png",
        "jpg",
        "jpeg",
        "pdf",
        "json",
        "txt",
        "log",
        "zip"
    }