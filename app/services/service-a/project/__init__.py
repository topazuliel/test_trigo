# services/scores/project/__init__.py


import os

from flask import Flask
from flask_cors import CORS
from flask import Flask, current_app
from flask_pymongo import PyMongo
# instantiate the extensions




def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    mongo = PyMongo(app, tz_aware=True)
    app.__setattr__('mongo', mongo)

    # set up extensions
    mongo.init_app(app)

    # register blueprints
    from project.api.service_a_routes import service_a_blueprint
    app.register_blueprint(service_a_blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app})

    return app
