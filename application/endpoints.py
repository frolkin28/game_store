from flask_restful import Resource


class UserApi(Resource):
    def get(self):
        return "hello", 200
