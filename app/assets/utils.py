"""
CloudShield Enterprise
Asset Utilities
"""

from datetime import datetime


def current_time():

    return datetime.utcnow()


def risk_color(risk):

    colors = {
<<<<<<< HEAD
        "Critical": "danger",
        "High": "warning",
        "Medium": "info",
        "Low": "primary",
        "Info": "success",
    }

    return colors.get(risk, "secondary")
=======

        "Critical": "danger",

        "High": "warning",

        "Medium": "info",

        "Low": "primary",

        "Info": "success"

    }

    return colors.get(

        risk,

        "secondary"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


def asset_summary(asset):

    return {
<<<<<<< HEAD
        "name": asset.name,
        "target": asset.target,
        "score": asset.score,
        "risk": asset.risk,
        "findings": asset.findings,
    }
=======

        "name": asset.name,

        "target": asset.target,

        "score": asset.score,

        "risk": asset.risk,

        "findings": asset.findings

    }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
