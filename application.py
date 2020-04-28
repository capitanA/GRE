from flask import Flask
from config import ProductionConfig
from flask import blueprints,abort


def configure_database(app):
    pass


def configure_logger(app):
    pass


def configure_blueprints(app):
    pass


def create_app(configuration=None):
    app = Flask(__name__)
    app.config.from_object(configuration or ProductionConfig)
    configure_blueprints(app)
    configure_database(app)
    configure_logger(app)
    return app
