# Importing flask and the config
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
    migrate.init_app(app, db, render_as_batch=True)
    with app.app_context():
        print('Creating the database tables if they do not exist...')
        db.create_all(app=app)
        command.upgrade(migrate.get_config(), revision='head', sql=False, tag=None)

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

