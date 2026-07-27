"""
CloudShield Enterprise
Configuration
"""

import os
<<<<<<< HEAD
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

=======


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
class Config:

    # ==========================================
    # Flask
    # ==========================================

<<<<<<< HEAD
    SECRET_KEY = os.getenv("SECRET_KEY")
=======
    SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "dev-secret-key-change-me"
)
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40

    # ==========================================
    # Database
    # ==========================================

<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = "sqlite:///cloudshield.db"
=======
    SQLALCHEMY_DATABASE_URI =  os.getenv(
    "DATABASE_URL",
    "sqlite:///cloudshield.db"
)
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40

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