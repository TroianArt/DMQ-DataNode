from flask import Blueprint,request,abort
from .. import CONNECTED, rsa_key

connect = Blueprint("connect", __name__)


@connect.route('/ping')
def ping():
    return 'pong'


@connect.route('/connect', methods=['GET'])
def connect():
    global CONNECTED
    global rsa_key
    if not request.headers['rsa_public_key'] or CONNECTED:
        abort(404)

    rsa_key = request.headers['rsa_public_key']
    CONNECTED = True
    return 200


@connect.route('/disconnect')
def disconnect():
    global CONNECTED
    global rsa_key
    CONNECTED = False
    rsa_key = None
    return 200