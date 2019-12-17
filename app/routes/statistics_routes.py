from ..data import data
from flask import jsonify, request, Blueprint, abort
import psutil

statistics = Blueprint('statistics', __name__)


@statistics.route('/statistics', methods=['GET'])
def get_statistics():
    response = {
        'cpu_load_percent': psutil.cpu_times_percent()._asdict()["user"] / 100,
        'queues': []
    }
    for x in data['queues']:
        queue_statistic = {
            'id': x['id'],
            'name': x['name'],
            'size': x['data'].qsize()
        }
        response['queues'].append(queue_statistic)
    return jsonify(response), 200

