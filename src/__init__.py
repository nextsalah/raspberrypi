# Importing flask and the config
from importlib.resources import path
from operator import imod
from flask import Flask
from .config import Config

# Importing the libraries that we will be using in our app.
from flask_socketio import SocketIO
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_assets import Environment, Bundle
from flask_babel import Babel
from flask_compress import Compress

from alembic import command
import os, glob

# Initialize the app and libraries
app = Flask( __name__)
socketio = SocketIO()
api = Api(prefix=Config.API_PREFIX )
db = SQLAlchemy( )
migrate = Migrate(app, db, render_as_batch=True)
assets = Environment(app)
babel = Babel(app)
compress = Compress()

def create_app():    
    """Create an application."""
    
    #App configurations
    app.config.from_object(Config)
    
    # Import the models and register them with the app
    import src.models
    
    # Initialize the database and register the models
    db.init_app(app)
    with app.app_context():
        print('Creating the database tables if they do not exist...')
        db.create_all(app=app)
        
        # Try to migrate the database to the latest version
        try:
            migrate.init_app(app, db, render_as_batch=True)
            command.upgrade(migrate.get_config(), revision='head', sql=False, tag=None)
        except Exception:            
            # Delete the database if it already exists
            if os.path.exists(os.path.join(app.root_path, 'db/database.db')):
                os.remove(os.path.join(app.root_path, 'db/database.db'))
                
            # Remove the migration files
            path = app.root_path[:-4] + '/migrations/versions/*.py'
            files = glob.glob(path)
            for f in files:
                os.remove(f)
                
                

    # Initialize SCSS for the assets
    scss = Bundle('scss/style.scss', filters='pyscss', output='css/style.css', depends=('scss/*.scss'))
    assets.register('scss_all', scss)
    compress.init_app(app)
    
    # Register main routes
    from .routes.main import main_routes
    app.register_blueprint( main_routes, url_prefix='/')

    # Register the API & SocketIO routes
    socketio.init_app(app)
    api.init_app(app)

    return app

