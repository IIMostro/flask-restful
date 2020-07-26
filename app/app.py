from flask import Flask


def registry_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.secure')
    # noinspection PyTypeChecker
    registry_blueprints(app)
    return app
