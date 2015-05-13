__author__ = 'Ankit'

import json
import time
import random
import logging
from flask import Flask
import requests


app = Flask(__name__)
log = logging.getLogger('werkzeug')


def addOrdertoCookQueue(custID, custName, custOrder):
    cookQueueUrl = 'http://localhost:3001/cook/orderqueue'
    header = {'Content-Type': 'application/json'}
    addOrder = requests.post(cookQueueUrl,
                             data=json.dumps({"custId": custID, "customerName": custName, "orderName": custOrder}),
                             headers=header)


def get_customer_order(custID):
    print("In cust order")
    getOrderUrl = "http://localhost:5001/customer/getCustomer/" + str(custID)
    custDetails = requests.get(getOrderUrl).json()
    customerID = custDetails['custId']
    customerName = custDetails['customerName']
    customerOrder = custDetails['order']
    print(len(customerOrder))
    orderArray = []
    for i in range(len(customerOrder)):
        print(i, customerOrder[i])

    if len(customerOrder) > 0:
        print("Cashier: {} {} will be provided in a while ".format(customerName, customerOrder))
        for i, v in enumerate(customerOrder):
            addOrdertoCookQueue(customerID, customerName, v)
    else:
        print("{} Cashier: Have a good day! Bye".format(get_time()))

def getCustomer():
    custURL = 'http://localhost:5001/customer/removeCustomer'
    custResponse = requests.delete(custURL)
    if custResponse.status_code == requests.codes.ok:
        custQueueResponse = custResponse.json()
        custID = custQueueResponse['custId']
        waitTime = random.randrange(2, 10)
        time.sleep(waitTime)
        print("Cashier: Hello, What would you like to order??")
        get_customer_order(custID)
    elif custResponse.status_code == 204:
        time.sleep(random.randrange(2, 6))


def get_time():
    wallClockURL = 'http://localhost:10001/wallclock'
    queueResponse = requests.get(wallClockURL).json()
    return queueResponse['time']

print("Cashier Waiting for Customer")
while(True):
    getCustomer()
    #get_time()