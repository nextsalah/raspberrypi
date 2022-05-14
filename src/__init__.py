from flask import Flask
from flask_socketio import SocketIO
from flask_restful import Api
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_assets import Environment, Bundle
from alembic import command


# Initialize the full app
app = Flask( __name__)
socketio = SocketIO()
api = Api(prefix=Config.API_PREFIX )
db = SQLAlchemy( )
migrate = Migrate(app, db, render_as_batch=True)
assets = Environment(app)

def create_app():    
    """Create an application."""
    
    #App configurations
    app.config.from_object(Config)
    
    # Import the models
    import src.models
    
    # Initialize the database
    db.init_app(app)
    db.create_all(app=app)
    migrate.init_app(app, db, render_as_batch=True)
    with app.app_context():
        print("Upgrading the database")
        command.upgrade(migrate.get_config(), revision='head', sql=False, tag=None)
    


    # Initialize SCSS for the assets
    scss = Bundle('scss/style.scss', filters='pyscss', output='css/style.css', depends=('scss/*.scss'))
    assets.register('scss_all', scss)

    # Register main routes
    from .routes.main import main_routes
    app.register_blueprint( main_routes, url_prefix='/')

    # Register the API & SocketIO routes
    socketio.init_app(app)
    api.init_app(app)

    return app

