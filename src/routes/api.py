from flask_restful import Resource
from .. import api
from ..models import Settings
from .. import db

class Todo(Resource):
    def get(self, todo_id):
        setting = Settings.query.filter_by(id=todo_id).one_or_none()
        print(Settings.query.all())
        if Settings.query.all() == []:
            db.session.add(Settings())
            db.session.commit()
        
        return setting.json()

api.add_resource(Todo, '/todo/<todo_id>')