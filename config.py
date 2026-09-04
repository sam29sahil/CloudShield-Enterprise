"""
CloudShield Enterprise
Configuration
"""

import os

from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASE_DIR, ".env"))

APP_ENV = os.getenv("APP_ENV", os.getenv("FLASK_ENV", "development")).lower()


def database_url():
    url = os.getenv("DATABASE_URL", "sqlite:///cloudshield.db")

    if url.startswith("postgres://"):
        return "postgresql://" + url[len("postgres://") :]

    return url




BASE_DIR = os.path.abspath(os.path.dirname(__file__))



class Config:

    # ==========================================
    # Flask
    # ==========================================

    SECRET_KEY = os.getenv("SECRET_KEY") or (
        None if APP_ENV == "production" else "dev-secret-key-change-me"
    )

    if APP_ENV == "production" and not SECRET_KEY:
        raise RuntimeError("SECRET_KEY must be configured in production.")


    # ==========================================
    # Database
    # ==========================================


    SQLALCHEMY_DATABASE_URI = database_url()


    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = APP_ENV == "production"
    WTF_CSRF_ENABLED = True

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