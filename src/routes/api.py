from webargs.flaskparser import use_kwargs, parser
from ..utils.nextsalah_api import NextSalahAPI
from ..models import PrayerTimes, Settings
from flask_restful import Resource, abort
from ..utils.theme import Theme
from webargs import fields
from ..utils.error_handling import catch_api_errors
from .. import api

class SettingsAPI(Resource):
    def get(self):
        settings = Settings.query.filter_by( id = 1 ).one_or_none()
        if settings:
            return settings.json()
        return {}, 404

class PrayerTimesAPI(Resource):
    args = {'source': fields.Str(required=True),'data': fields.Dict(required=True)}
    @use_kwargs(args)
    def post(self, source, data):
        new_prayertimes = NextSalahAPI.get_prayertimes(source, data)
        return {"status": PrayerTimes.save_prayertimes(new_prayertimes)}, 200
    
    def get(self):
        prayertimes = PrayerTimes.query.all()
        if prayertimes != []:
            return [prayertime.json() for prayertime in prayertimes], 200
        else:
            abort(404, message="No prayer times found.")
            
                        

class ThemeAPI:
    class Config(Resource):
        @catch_api_errors
        def get(self):
            return Theme().config

    class Variables(Resource):
        @catch_api_errors
        def get(self):
            return Theme().variables

# This error handler is necessary for usage with Flask-RESTful.
@parser.error_handler
def handle_request_parsing_error(err):
    abort(404, errors=err.messages)

    
api.add_resource(SettingsAPI, '/settings')
api.add_resource(PrayerTimesAPI, '/prayertimes')
api.add_resource(ThemeAPI.Config, '/theme/config')
api.add_resource(ThemeAPI.Variables, '/theme/variables')