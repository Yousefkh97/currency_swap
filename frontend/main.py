import flask
from flask import Flask, render_template, request, jsonify, url_for
import requests
from datetime import datetime

# url to get the data of currncy from it
api_key = "85aa5a4fb3533fbae7223f74ccb1befb"
url = "http://data.fixer.io/api/latest?access_key=" + api_key


app = Flask(__name__)
info_list =[] # the list that save the history
when_get = dict() # a dict that save the data that get from the backend
@app.route("/", methods=["POST", "GET"])
def index():
    # get the aws ec2 public ip
    ip_address = (requests.get("http://169.254.169.254/latest/meta-data/public-ipv4").content).decode('utf-8')

    # make a urls to conect to them
    ur1 = "http://" + ip_address + ":5000"
    ur2 = "http://" + ip_address + ":5000/Auti/"

    #when get a post req from the back end update the data and the web page
    if request.method == "POST":
        # get the data from the backend
        input_json = request.get_json(force=True)
        global when_get
        when_get = input_json
    return render_template("index2.html", info=when_get, val = ur1, val2 = ur2)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)
