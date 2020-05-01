from flask import Flask
from config import ProductionConfig
import blueprints
from importlib import import_module
import ipdb


def configure_database(app):
    pass


def configure_logger(app):
    pass


def configure_blueprints(app):
    for blueprint in blueprints.__all__:
        bp = import_module("blueprints.{}".format(blueprint))
        for route in bp.__all__:
            app.register_blueprint(getattr(bp, route))


def create_app(configuration=None):
    app = Flask(__name__)
    app.config.from_object(configuration or ProductionConfig)
    configure_blueprints(app)
    configure_database(app)
    configure_logger(app)
    return app
