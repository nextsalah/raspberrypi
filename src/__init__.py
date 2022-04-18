
from flask import Flask, send_from_directory
from flask.helpers import url_for
from flask_socketio import SocketIO, emit
from src.config import Config 
from flask_sqlalchemy import SQLAlchemy
import os


# Initialize socketio
socketio = SocketIO()

#initialize database
db = SQLAlchemy()

def create_app(config_class=Config):

    #Create and configure the app    
    app = Flask(__name__, static_folder="./build_react")
    app.config.from_object(Config)
    db.init_app(app)
    
    # Configure main routes
    from src.routes.main import main
    app.register_blueprint(main, url_prefix='/')
    
    # Configure routes (/api)
    from src.routes.api.routes_api import api
    app.register_blueprint(api, url_prefix='/api/v1')
    
    # Configure socketio
    socketio.init_app(app)

    return app