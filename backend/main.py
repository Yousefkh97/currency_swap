import flask
from flask import Flask, render_template, request, jsonify, url_for
import requests
from datetime import datetime
import urllib, json
import urllib.request
import socket
from pip._internal import req
from werkzeug.utils import redirect

api_key = "85aa5a4fb3533fbae7223f74ccb1befb"
url = "http://data.fixer.io/api/latest?access_key=" + api_key

app = Flask(__name__)
info_list =[]

@app.route("/", methods=["POST", "GET"])
def index():
    #ip_address = (requests.get("http://169.254.169.254/latest/meta-data/local-ipv4").content).decode('utf-8')
    #ip_address = '0.0.0.0'
    #fd = 'http://' + ip_address + ':8000/'
    if request.method == "POST":
        fistCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")
        amount = request.form.get("amount")
        response = requests.get(url)
        app.logger.info(response)
        infos = response.json()
        firstValue = infos["rates"][fistCurrency]
        secondValue = infos["rates"][secondCurrency]
        result = (secondValue / firstValue) * float(amount)
        currencyInfo = dict()
        currencyInfo["firstCurrency"] = fistCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        l = [current_time, amount, fistCurrency, secondCurrency, secondValue, result]
        info_list.append(l)
        res = requests.post('http://0.0.0.0:8000/', json=currencyInfo)
        return redirect('http://0.0.0.0:8000/', code=302)
    else:
        return redirect('http://0.0.0.0:8000/', code=302)

@app.route("/Auti/", methods=["POST", "GET"])
def Auti():
    #ip_address2 = (requests.get("http://169.254.169.254/latest/meta-data/local-ipv4").content).decode('utf-8')
    #ip_address2 = '0.0.0.0'
    #fd2 = 'http://' + ip_address2 + ':7000/'
    info_dict = dict()
    info_dict["info"] = info_list
    res = requests.post("http://0.0.0.0:7000/", json=info_dict)
    return redirect("http://0.0.0.0:7000/", code=302)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)

