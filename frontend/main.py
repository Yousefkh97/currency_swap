import flask
from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

api_key = "85aa5a4fb3533fbae7223f74ccb1befb"
url = "http://data.fixer.io/api/latest?access_key=" + api_key


app = Flask(__name__)
info_list =[]
when_get = dict()
@app.route("/", methods=["POST", "GET"])
def index():
    ip_address = flask.request.remote_addr
    ur1 = "http://" + ip_address + ":5000"
    ur2 = "http://" + ip_address + ":5000/Auti/"
    if request.method == "POST":
        input_json = request.get_json(force=True)
        global when_get
        when_get = input_json
    return render_template("index2.html", info=when_get, val=ur1, val2=ur2)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)
