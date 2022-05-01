from .. import socketio
from ..utils.nextsalah_api import NextSalahAPI


@socketio.on('connect', namespace='/dd')
def ws_conn():
    socketio.emit('msg', {'count': 1}, namespace='/dd')

@socketio.on('disconnect', namespace='/dd')
def ws_disconn():
    print('Disconnected')
    
@socketio.on('get_new_prayertimes')
def get_new_prayertimes(json):
    source, data = json['source'], json['data']
    print('Getting new prayertimes ', source, data)
    new_prayertimes = NextSalahAPI.get_prayertimes(source, data)
    print(new_prayertimes)
    print('New prayertimes: ', "Done")