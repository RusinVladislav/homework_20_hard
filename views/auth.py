from flask import request
from flask_restx import Namespace, Resource

from implemented import auth_service

auth_services = Namespace('auth')


@auth_services.route("/")
class AuthsView(Resource):
    def post(self):
        data = request.json

        username = data.get("username", None)
        password = data.get("password", None)

        if None in [username, password]:
            return "", 400

        tokens = auth_service.generate_tokens(username, password)

        return tokens, 201
