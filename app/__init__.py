from flask import Flask, json
from flask_migrate import Migrate
from flask_login import current_user

from config import Config
from app.extensions import db, login_manager, bcrypt
from app.notifications.services import NotificationService
from app.notifications.utils import time_ago

# Create migrate object
migrate = Migrate()


def create_app():

    app = Flask(__name__)

    # Load Config
    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Flask Login Settings
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please login to continue."

    # Import Models
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints
    from app.routes import main
    app.register_blueprint(main)

    from app.auth import auth
    app.register_blueprint(auth)

    from app.dashboard import dashboard
    app.register_blueprint(dashboard)

    from app.scanner import scanner
    app.register_blueprint(scanner)

    from app.security import security
    app.register_blueprint(security)

    from app.reports import reports
    app.register_blueprint(reports)

    from app.analytics import analytics
    app.register_blueprint(analytics)

    from app.history import history
    app.register_blueprint(history)

    from app.settings import settings
    app.register_blueprint(settings)

    from app.admin import admin
    app.register_blueprint(admin)

    from app.cloud import cloud
    app.register_blueprint(cloud)

    from app.threat import threat
    app.register_blueprint(threat)
    
    from app.findings_ui import findings_ui
    app.register_blueprint(findings_ui)

    from app.notifications import notifications
    app.register_blueprint(notifications)

    from app.assets import assets
    app.register_blueprint(assets)

    from app.projects import projects
    app.register_blueprint(projects)

    from app.executive import executive
    app.register_blueprint(executive)
    
    from app.api import api
    app.register_blueprint(api)

    from app.docker import docker
    app.register_blueprint(docker)

    # -------------------------------
    # Jinja Filter
    # -------------------------------

    @app.template_filter("from_json")
    def from_json(value):

        try:
            return json.loads(value)
        except Exception:
            return {}
        

    @app.template_filter("timeago")
    def timeago_filter(value):
        return time_ago(value)    

    # -------------------------------
    # Global Notification Badge
    # -------------------------------

    notification_service = NotificationService()

    @app.context_processor
    def inject_notifications():

        if current_user.is_authenticated:

            unread = notification_service.unread_count(
                current_user.id
            )

        else:

            unread = 0

        return {
            "unread_notifications": unread
        }

    return app