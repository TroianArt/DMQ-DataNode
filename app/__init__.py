from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)

app.config.from_object('config.default.Config')

api = Api(app)
