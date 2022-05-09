from flask_restful import Resource, abort
from .. import api
from ..models import PrayerTimes, Settings
from webargs import fields
from webargs.flaskparser import use_kwargs, parser, abort

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
        return {"source": source, "data": data}, 200
    
    def get(self):
        prayertimes = PrayerTimes.query.all()
        if prayertimes != []:
            return [prayertime.json() for prayertime in prayertimes], 200
        else:
            abort(404, message="No prayer times found.")
            
# This error handler is necessary for usage with Flask-RESTful.
@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    abort(404, errors=err.messages)
    
api.add_resource(SettingsAPI, '/settings')
api.add_resource(PrayerTimesAPI, '/prayertimes')