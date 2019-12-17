from flask import Flask
from flask_restful import Api
from .routes.message_resource import Message

app = Flask(__name__)
app.config.from_object('config.default.Config')

api = Api(app)
api.add_resource(Message, '/queues/<string:queue_id>/messages/')
