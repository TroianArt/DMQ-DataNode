from app.data import data
from flask import jsonify, request, abort
from flask_restful import Resource


class Message(Resource):
    def get(self, queue_id):
        queue = [x for x in data['queues'] if x['id'] == queue_id][0]
        if not queue:
            abort(400)

        message = queue['data'].get()
        response = jsonify(message)
        response.status_code = 200
        return response

    def post(self, queue_id):
        queue = [x for x in data['queues'] if x['id'] == queue_id][0]
        if not queue:
            abort(400)

        message = request.get_json()
        if not message.get('key') or not message.get('value') or not queue:
            abort(400)

        queue['data'].put(message)
        queue['data'].task_done()

        response = jsonify(message)
        response.status_code = 201
        return response
