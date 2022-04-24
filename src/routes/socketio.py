from flask_socketio import emit, join_room, leave_room
from .. import socketio

@socketio.on('connect', namespace='/dd')
def ws_conn():
    socketio.emit('msg', {'count': 1}, namespace='/dd')

@socketio.on('disconnect', namespace='/dd')
def ws_disconn():
    print('Disconnected')
    
@socketio.on('test')
def test(json):
    return json

