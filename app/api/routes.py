"""
CloudShield Enterprise
API Route Registration
"""

from flask import jsonify

from app.api import api

# Register API Modules
from app.api import auth
from app.api import users
from app.api import projects
from app.api import assets
from app.api import scans
from app.api import findings
from app.api import reports
from app.api import dashboard
from app.api import cloud

# Future Modules
# from app.api import notifications
# from app.api import analytics


@api.route("/", methods=["GET"])
def api_home():
    """
    CloudShield API Root
    """

    return jsonify({

        "name": "CloudShield Enterprise API",

        "version": "1.0.0",

        "status": "running",

        "architecture": "Enterprise",

        "developer": "CloudShield",

        "documentation": "/api/docs",

        "health": "/api/health",

        "modules": {

            "authentication": "/api/auth",

            "users": "/api/users",

            "projects": "/api/projects",

            "assets": "/api/assets",

            "scans": "/api/scans",

            "findings": "/api/findings",

            "reports": "/api/reports",

            "dashboard": "/api/dashboard",

            "cloud": "/api/cloud"

        }

    })


@api.route("/health", methods=["GET"])
def health_check():
    """
    API Health Check
    """

    return jsonify({

        "success": True,

        "service": "CloudShield Enterprise API",

        "status": "healthy",

        "version": "1.0.0"

    })


@api.route("/version", methods=["GET"])
def version():
    """
    API Version
    """

    return jsonify({

        "name": "CloudShield Enterprise",

        "api_version": "1.0.0",

        "python": "3.x",

        "framework": "Flask"

    })


@api.route("/endpoints", methods=["GET"])
def endpoints():
    """
    List Available API Endpoints
    """

    return jsonify({

        "authentication": {

            "login": "/api/auth/login",

            "register": "/api/auth/register",

            "logout": "/api/auth/logout"

        },

        "users": {

            "list": "/api/users",

            "details": "/api/users/<id>"

        },

        "projects": {

            "list": "/api/projects",

            "details": "/api/projects/<id>"

        },

        "assets": {

            "list": "/api/assets",

            "details": "/api/assets/<id>"

        },

        "scans": {

            "list": "/api/scans",

            "details": "/api/scans/<id>",

            "start": "/api/scans/start"

        },

        "findings": {

            "list": "/api/findings",

            "details": "/api/findings/<id>"

        },

        "reports": {

            "list": "/api/reports",

            "download": "/api/reports/<id>"

        },

        "dashboard": {

            "stats": "/api/dashboard"

        },

        "cloud": {

            "aws": "/api/cloud"

        }

    })


@api.route("/ping", methods=["GET"])
def ping():
    """
    Ping Endpoint
    """

    return jsonify({

        "message": "pong"

    })