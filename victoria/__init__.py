from flask import Flask

from victoria.commands.commands import create_db, drop_db, recreate_db

from victoria.database import db

from victoria.user import user


def register_errorhandlers(app):
    """Register error handlers with the Flask application."""
    pass


def register_commands(app):
    """Register custom commands for the Flask CLI."""
    for command in [create_db, drop_db, recreate_db]:
        app.cli.command()(command)


def register_blueprints(app):
    """Register blueprints with the Flask application."""
    app.register_blueprint(user, url_prefix='/victoria/users')


def register_extensions(app):
    """Register extensions with the Flask application."""
    db.init_app(app)


def create_app(config):
    """Returns an initialized Flask application."""
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    @app.route('/', methods=['GET'])
    def index():
        """Returns the applications index page."""
        return 'Welcome to victoria'

    return app