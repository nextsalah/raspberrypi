from flask_restful import Resource
from .. import api
from ..models import Setting
from .. import db

class Todo(Resource):
    def get(self, todo_id):
        setting = Setting.query.filter_by(id=todo_id).one_or_none()
        print(Setting.query.all())
        if Setting.query.all() == []:
            db.session.add(Setting())
            db.session.commit()
        
        return setting.json()

api.add_resource(Todo, '/todo/<todo_id>')