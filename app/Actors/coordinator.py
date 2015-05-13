__author__ = 'Ankit'


import queue
import logging
import requests
from flask import Flask
from flask import request
from flask import json
from flask import Response
from app.Actors.customer import Customer

logging.getLogger("requests").setLevel(logging.WARNING)

global processedCount
global orderCount
global orderTime
global order
orderCount = 0
processedCount = 0
order = None
orderTime = 0


app = Flask(__name__)
log = logging.getLogger('werkzeug')
combinedOrder = queue.Queue()
processedOrder = queue.Queue()

@app.route('/coordinator/combinedorder', methods=['POST'])
def addCombinedQueue():
    cust=Customer(request.json['customerName'], request.json['custId'], request.json['order'],0)
    cust.orderTime = request.json['orderTime']
    combinedOrder.put(cust)
    responsedata = {
        'status': 'Order Received'
    }
    responsedata = json.dumps(responsedata)
    resp = Response(responsedata, status=201, mimetype='application/json')
    return resp


@app.route('/coordinator/processedorder', methods=['POST'])
def addProcessedQueue():
    global orderCount
    global processedCount
    global orderTime
    global order
    if(processedCount == 0):
        c = combinedOrder.get(block=True)
        order = c.order
        orderCount = len(c.order)
        orderTime = c.orderTime

    processedCount +=1
    if(processedCount == orderCount):
        processedCount = 0
        orderCount = 0
        custid = request.json['custId']
        custname = request.json['customerName']
        print("Coordinator: Hey {}, your order is ready..".format(request.json['customerName']))
        createUrl = 'http://localhost:5001/customer/deliverOrder'
        custheader = {'Content-Type': 'application/json'}
        addCustomer = requests.post(createUrl, data=json.dumps({"custId": custid, "customerName": custname, "order": order,"orderTime": orderTime}), headers=custheader)

    responsedata = {
        'status': 'Adding Order to Basket'
    }
    responsedata = json.dumps(responsedata)
    resp = Response(responsedata, status=201, mimetype='application/json')
    return resp
if __name__ == '__main__':
    host = 'localhost'
    port = 6001
    app.run(host=host, port=port)