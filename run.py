__author__ = 'Ankit'

from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
import time
import sys
import logging
import json


app = Flask(__name__)
host = None
port = None
log = logging.getLogger('werkzeug')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/v1/customers/order')
def Order():
        order = {"starter":'burger'}
        #print(json.dumps(order))
        return json.dumps(order)

def process_request(self, request):
        print("Hello!! What would you like to order!!!")
        order = request.get("http://%s:%s/api/v1/customers/order" % (request.address.host, request.address.port)) \
        .json()

if __name__ == '__main__':
    app.debug = True
    host = sys.argv[1]
    port = int(sys.argv[2])
    #host = 'localhost'
    #port = 5000
    app.run(host=host, port=port)