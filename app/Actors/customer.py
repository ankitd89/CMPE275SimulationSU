__author__ = 'Rashmi'

import Queue
from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
import time
import sys
import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')

def get_time():
    wallClockURL = 'http://localhost:10001/wallclock'
    queueResponse = request.get(wallClockURL).json()
    return 	queueResponse['time']

q = Queue.Queue()
class Customer:

    #Attributes
    global nextNumber
    global customerName
    global arrivalTime
    global waitingTime
    global transactionTime
    global customers
    customers = []



    def __init__(self,customerName,custId,order):
        self.customerName = customerName
        self.custId = custId
        self.order = order
        #time the customer showed up
        self.arrivalTime = 0
        #in line waiting to be served
        self.waitingTime = 0
        #At the counter while being served
        self.transactionTime = 0



'''
    def nextNumber(self):
        self.nextNumber += 1
        return nextNumber

    def customerWaiting(self):
    	self.waitingTime += 1


    def customerTransaction(self,transactionTime):
    	self.transactionTime = transactionTime

    def depart(self):
    	return "Customer " + customerName + " has left."


    def timeArrival(self, time):
    	self.arrivalTime = time
    	return "Customer " + customerName + " arrived at time unit " + arrivalTime

'''


    # there is a customer queue
    # the customer is added to the queue
    # cashier will dequeue a customer after billing
    # cashier --> cook -->coordinator --> customer
    # the dequeued person waits for the order  and leaves the shop-- what is the wait time?
    #
#Cust_main will create customer and push it in queue
@app.route('/customer', methods=['POST'])
def create_customer():
    if request.method == 'POST':
        cust=Customer(request.json['customerName'], request.json['custId'], request.json['order'])
        print(cust)
        customers.append(cust)
        q.put(cust)
        return jsonify({'status': 'customer successfully added'}), 201

#Cashier will call this function and take the order
@app.route('/customer/removeCustomer', methods=['DELETE'])
def reomveCustomer():
    if request.method == 'DELETE':
        if q.empty():
            return jsonify({"status": "No Customer in queue"}), 204
        else:
            custId = q.get(block=False)
            return jsonify({"status": "customer deleted successfully", "id": custId}), 200


# Cashier will call this to ask for Customer Order
@app.route('/customer/getCustomer/<int:custId>', methods=['GET'])
def getCustomer(custId):
    cust=findCustomer(customers, custId)
    if cust is not None:
        print("{} {}: Hello, I would like to have {} ".format(get_time(), cust.name, cust.order))
        return jsonify({'customerName': cust.name, 'custId': cust.id, 'order': cust.order}), 200
    else:
        return jsonify({"status": "customer not found"}), 200



def findCustomer(list, custId):
    for i in list:
        if i.id==custId:
            return i
    return None



if __name__ == '__main__':
    app.debug = True
       # host = sys.argv[1]
        #port = int(sys.argv[2])
    host = 'localhost'
    port = 5001
    app.run(host=host, port=port)
