__author__ = 'rashmi'

import Queue
import logging

from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from flask import Response
from order import Order

app = Flask(__name__)
log = logging.getLogger('werkzeug')
orderQueue = Queue.Queue()

@app.route('/cook/orderqueue', methods=['POST'])
def addOrderQueue():
    custid = request.json['custId']
    custname = request.json['customerName']
    orderName = request.json['orderName']
    neworder = Order(customerid=custid, customername=custname, orderName=orderName)
    orderQueue.put(neworder)

    responsedata = {
        'status': 'Order Queued'
    }
    responsedata = json.dumps(responsedata)
    resp = Response(responsedata, status=201, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(port=3000)