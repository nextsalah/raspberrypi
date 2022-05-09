from flask_restful import Resource
from src.routes.main import prayertimes
from .. import api
from ..models import PrayerTimes, Settings
from .. import db

class SettingsAPI(Resource):
    def get(self):
        settings = Settings.query.filter_by( id = 1 ).one_or_none()
        if settings:
            return settings.json()
        return {}, 404

class PrayerTimesAPI(Resource):
    def post(self, source, data):
        return {"source": source, "data":data}
    def get(self):
        prayertimes = PrayerTimes.query()
        return [pt.json() for pt in prayertimes ]

api.add_resource(SettingsAPI, '/settings')
api.add_resource(PrayerTimesAPI, '/prayertimes')