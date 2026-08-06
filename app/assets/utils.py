"""
CloudShield Enterprise
Asset Utilities
"""

from datetime import datetime


def current_time():

    return datetime.utcnow()


def risk_color(risk):

    colors = {
        "Critical": "danger",
        "High": "warning",
        "Medium": "info",
        "Low": "primary",
        "Info": "success",
    }

    return colors.get(risk, "secondary")


def asset_summary(asset):

    return {
        "name": asset.name,
        "target": asset.target,
        "score": asset.score,
        "risk": asset.risk,
        "findings": asset.findings,
    }
