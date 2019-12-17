from flask import Flask
from .routes.queue_routes import queue

app = Flask(__name__)

app.config.from_object('config.default.Config')

app.register_blueprint(queue)
