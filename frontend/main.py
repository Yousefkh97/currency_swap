import flask
from flask import Flask, render_template, request, jsonify, url_for
import requests
from datetime import datetime

from pip._internal import req
from werkzeug.utils import redirect
import urllib, json
import urllib.request
import socket


urllib.request.urlopen("http://169.254.169.254/latest/meta-data/public-ipv4").read()
api_key = "85aa5a4fb3533fbae7223f74ccb1befb"
url = "http://data.fixer.io/api/latest?access_key=" + api_key


app = Flask(__name__)
info_list =[]
when_get = dict()
@app.route("/", methods=["POST", "GET"])
def index():
    ip_address = (requests.get("http://169.254.169.254/latest/meta-data/local-ipv4").content).decode('utf-8')
    #ip_address = '0.0.0.0'
    ur1 = "http://" + ip_address + ":5000"
    ur2 = "http://" + ip_address + ":5000/Auti/"
    if request.method == "POST":
        input_json = request.get_json(force=True)
        global when_get
        when_get = input_json
    return render_template("index2.html", info=when_get, val=ur1, val2=ur2)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)
