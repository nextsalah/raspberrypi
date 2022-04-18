from flask import Blueprint
from src.config import Config

UPLOAD_FILE_SRC = Config.UPLOAD_FOLDER
api = Blueprint('api', __name__)

@api.route( '/' )
def index():
    return {'message': 'Hello, World!'}
