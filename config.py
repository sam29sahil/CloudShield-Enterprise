"""
CloudShield Enterprise
Configuration
"""

import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))




BASE_DIR = os.path.abspath(os.path.dirname(__file__))



class Config:

    # ==========================================
    # Flask
    # ==========================================

    SECRET_KEY = os.getenv("SECRET_KEY")

    SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "dev-secret-key-change-me"
)


    # ==========================================
    # Database
    # ==========================================


    SQLALCHEMY_DATABASE_URI = "sqlite:///cloudshield.db"
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