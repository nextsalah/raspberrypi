from bs4 import Tag
from flask import Flask
from flask_socketio import SocketIO
import werkzeug
import flask.scaffold
werkzeug.cached_property = werkzeug.utils.cached_property
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restplus import Api
from src.config import Config 
from flask_sqlalchemy import SQLAlchemy
from src.routes.main import main
from src.routes.api.routes_api import HelloWorld

# Initialize the app
app = Flask(__name__)

# Initialize socketio
socketio = SocketIO()

# Initialize API
api = Api(app, prefix=Config.API_PREFIX,
          title='API',
          description='Handels API requests',
          license='MIT License',
          contact='Ismail Sacic',
          contact_url='https://github.com/nextsalah',
          version='1.0',
          doc=f"{Config.API_PREFIX}/docs/"
        )

#initialize database
db = SQLAlchemy()

def create_app(config_class=Config):    
    #App configuration
    app.config.from_object(Config)
    
    #Initialize database
    db.init_app(app)

    # Configure main routes
    app.register_blueprint( main , url_prefix='/')

    # Configure socketio
    socketio.init_app(app)

    return app