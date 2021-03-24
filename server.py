from flask import Flask
from flask import request

# import DSI library here

app = Flask(__name__)


@app.route("/", methods=["POST"])
def gen_loans():
    # get business data points using request.get_json()
    # pass to DSI library
    # return DSI library response as JSON
    pass