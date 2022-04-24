import imp
from flask import Flask
from flask_socketio import SocketIO
from flask_restful import Api
from src.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_scss import Scss

# Initialize the full app
app = Flask( __name__)
socketio = SocketIO()
api = Api(prefix=Config.API_PREFIX )
db = SQLAlchemy( )
migrate = Migrate(app, db)
Scss(app, static_dir='static',  asset_dir='assets')
   

def create_app():    
    """Create an application."""
    
    #App configurations
    app.config.from_object(Config)
    
    # Initialize the database
    db.init_app(app)
    db.create_all(app=app)
    
    # Import the models
    import src.models

    # Register main routes
    from .routes.main import main_routes
    app.register_blueprint( main_routes, url_prefix='/')

    # Register the API & SocketIO routes
    socketio.init_app(app)
    api.init_app(app)

    return app

