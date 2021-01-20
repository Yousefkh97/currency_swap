from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

api_key = "85aa5a4fb3533fbae7223f74ccb1befb"
url = "http://data.fixer.io/api/latest?access_key=" + api_key
ip_address = flask.request.remote_addr

app = Flask(__name__)
info_list =[]
when_get = dict()
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        input_json = request.get_json(force=True)
        global when_get
        when_get= input_json
    return render_template("index2.html", info=when_get, val = ip_address)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)
