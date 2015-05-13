__author__ = 'Rashmi'

import queue
from flask import Flask
from flask import request
from flask import jsonify
import time
app = Flask(__name__)
import logging
logging.getLogger("requests").setLevel(logging.WARNING)

q = queue.Queue()
class Customer:

    #Attributes
    global nextNumber
    global customerName
    global arrivalTime
    global waitingTime
    global transactionTime
    global customers
    customers = []



    def __init__(self,customerName,custId,order,arrivalTime):
        self.customerName = customerName
        self.custId = custId
        self.order = order
        #time the customer showed up
        self.arrivalTime = arrivalTime
        #Order Waiting time
        self.orderTime = 0



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
    start=time.time()
    if request.method == 'POST':
        cust=Customer(request.json['customerName'], request.json['custId'], request.json['order'], start)
        print(cust.customerName + "added to Queue")
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
            c = q.get(block=False)
            custId = c.custId
            start = c.arrivalTime
            endtime=round(time.time()-start,2)
            print("Customer waited {} in the queue".format(endtime))
            return jsonify({"status": "customer deleted successfully", "custId": custId}), 200


# Cashier will call this to ask for Customer Order
@app.route('/customer/getCustomer/<int:custId>', methods=['GET'])
def getCustomer(custId):
    cust=findCustomer(customers, custId)
    cust.orderTime = time.time()
    if cust is not None:
        print("{}: Hello, I would like to have {} ".format(cust.customerName, cust.order))
        return jsonify({'customerName': cust.customerName, 'custId': cust.custId, 'order': cust.order, "orderTime": cust.orderTime}), 200
    else:
        return jsonify({"status": "customer not found"}), 200

#Utility function to find customer from Customers List
def findCustomer(list, custId):
    for i in list:
        if i.custId ==custId:
            return i
    return None

# Coordinator will call this function when entire order is ready to deliver order
@app.route('/customer/deliverOrder', methods=['POST'])
def deliverCustomer():
    print("Thank you")
    orderTime = request.json['orderTime']
    endtime=round(time.time()-orderTime,2)
    print("Customer had to wait for {} to receive order".format(endtime))
    return jsonify({"status": "Order Delivered to Customer"}), 200

if __name__ == '__main__':
    host = 'localhost'
    port = 5001
    app.run(host=host, port=port)
