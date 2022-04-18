class Config:
    SECRET_KEY = 'Secret key'
    UPLOAD_FOLDER = './static/upload'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///src/db/database.db'
    API_PREFIX = '/api/v1'