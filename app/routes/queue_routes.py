from ..data import data
from flask import jsonify, request, Blueprint, abort
from queue import Queue

queue = Blueprint('queue', __name__)


@queue.route('/queues', methods=['POST'])
def post():
    r = request.json
    id = str(r['id'])
    name = r['name']
    if not id or not name:
        abort(400)

    for queue in data['queues']:
        if queue['id'] == id:
            abort(400)

    queue = {
        "id": id,
        "name": name,
        "data": Queue(10)
    }
    data['queues'].append(queue)
    response = jsonify(r)
    response.status_code = 201
    return response


@queue.route('/queues/<string:id>', methods=['DELETE'])
def delete(id):
    queues = [x for x in data['queues'] if x['id'] == id]
    if not len(queues):
        print(id)
        print(data['queues'])
        abort(400)
    data['queues'] = [x for x in data['queues'] if not x['id'] == id]
    response = {
        "id": queues[0]['id'],
        "name": queues[0]['name']
    }
    return jsonify(response), 200
