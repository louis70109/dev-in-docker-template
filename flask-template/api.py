import os
import traceback
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

if os.getenv('FLASK_ENV') != 'production':
    from dotenv import load_dotenv
    load_dotenv()

from controller.item_controller import ItemController

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(ItemController, '/items')


@app.errorhandler(500)
def internal_error(e):
    error_trace = str(traceback.format_exc())[-300:]
    msg = 'P+ bot: url: ' + str(request.url) + " inbound: " + str(request.remote_addr) + " log: " + error_trace
    lotify = Client()
    lotify.send_message(access_token=os.getenv('LINE_NOTIFY_TOKEN'), message=msg)
    return "500"


@app.route("/healthz", methods=['GET'])
def health_check():
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
