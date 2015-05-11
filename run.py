__author__ = 'Ankit'


from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
import time
import sys
import logging

app = Flask(__name__)
host = None
port = None
log = logging.getLogger('werkzeug')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.debug = True
    host = sys.argv[1]
    port = int(sys.argv[2])
    #host = 'localhost'
    #port = 5000
    app.run(host=host, port=port)
