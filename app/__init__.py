from flask import Flask
from flask_restful import Api
from .routes.queue_routes import queue
from .routes.statistics_routes import statistics
from .routes.message_resource import Message
from .routes.connect import connect

app = Flask(__name__)
app.config.from_object('config.default.Config')
app.register_blueprint(queue)
app.register_blueprint(statistics)
app.register_blueprint(connect)

#CONNECTED = False
#rsa_key = None

api = Api(app)
api.add_resource(Message, '/queues/<string:queue_id>/messages/')
