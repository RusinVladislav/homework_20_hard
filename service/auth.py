import calendar
import datetime

import jwt
from flask_restx import abort

from constants import SECRET, ALGO
from service.user import UserService


class AuthServices:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password):
        user = self.user_service.get_by_username(username)

        if user is None:
            raise abort(404)

        if not self.user_service.compare_passwords(user.password, password):
            abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }

        # Создаем токен основной на 30 минут
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)

        # Создаем токен обновления на 130 дней
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
