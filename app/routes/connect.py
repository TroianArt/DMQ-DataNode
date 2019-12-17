from flask import Blueprint, request, abort


connect = Blueprint("connect", __name__)

SECRET = '\xb5\xdee\xe2gA\t\xaf&\xde\x8a\xdd'
CONNECTED = False


@connect.route('/ping')
def ping():
    return 'pong'


@connect.route('/connect', methods=['POST'])
def handle_connect():
    global CONNECTED
    global SECRET
    if not request.json['secret'] or CONNECTED:
        abort(404)

    SECRET = request.json['secret']
    CONNECTED = True
    return 200


@connect.route('/disconnect')
def disconnect():
    global CONNECTED
    global SECRET
    CONNECTED = False
    SECRET = None
    return 200