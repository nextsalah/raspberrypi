class Config:
    SECRET_KEY = 'secret'
    UPLOAD_FOLDER = './static/upload'
    API_PREFIX = '/api'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BABEL_DEFAULT_LOCALE = 'en'
    
