import os

class Config:
    SECRET_KEY = "cloudshield-secret-key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///cloudshield.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False