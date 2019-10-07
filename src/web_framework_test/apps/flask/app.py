from flask import Flask, request

from web_framework_test import routines

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    count = request.json['count']
    return {"result": routines.calculate(count)}


@app.route('/read-network')
def read_network():
    count = request.json['count']
    return {"result": routines.read_network(count)}


@app.route('/read-disk')
def read_disk():
    count = request.json['count']
    return {"result": routines.read_disk(count)}


@app.route('/deserialize')
def deserialize():
    count = request.json['count']
    return {"result": routines.deserialize(count)}

@app.route('/sleep')
def sleep():
    count = request.json['count']
    return {"result": routines.sleep(count)}

wsgi_app = app.wsgi_app
