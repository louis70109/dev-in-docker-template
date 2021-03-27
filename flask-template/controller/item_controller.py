from flask import request
import json
from flask_restful import Resource


class ItemController(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        return 'OK'
    def post(self):
        payload = request.get_json(force=True)
        response = {
            "statusCode": 200,
            "body": json.dumps(payload)
        }

        return response
