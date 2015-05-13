__author__ = 'rashmi'

import queue
import logging

from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from flask import Response


app = Flask(__name__)
log = logging.getLogger('werkzeug')
orderQueue = queue.Queue()

class Order:
    def __init__(self, customerid, customername, orderName):
        self.customerid = customerid
        self.customername = customername
        self.orderName = orderName

    def displayOrder(self):
        print("Order => {}...{}...{}".format(self.customerid, self.customername, self.orderName))






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


@app.route('/queue/readQueue', methods=['DELETE'])
def read_queue():
    if orderQueue.empty():
        result_JSON = {
            'response': 'Empty Order'
        }
        json_data = jsonify(result_JSON)
        json_data.status_code = 204
    else:
        order = orderQueue.get(block=False)
        result_JSON = {
            'custId': order.customerid,
            'customerName': order.customername,
            'orderName': order.orderName
        }

        json_data = jsonify(result_JSON)
        json_data.status_code = 200

    return json_data


if __name__ == '__main__':
    app.run(port=3001)