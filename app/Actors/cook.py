import queue
from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
import time
import sys
import logging
#from httpie.output.formatters
import json
import requests
from random import randint


app = Flask(__name__)
host = None
port = None


from queue import Queue

#orderQueue= queue.Queue


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


# def get_time():
#     wallClockURL = 'http://localhost:10001/wallclock'
#     queueResponse = requests.get(wallClockURL).json()
#     # print("Printing time %s" %queueResponse['time'])
#     return queueResponse['time']


while(True):
    req_custQueueUrl = "http://localhost:3000/queue/readQueue"
    response = requests.delete(req_custQueueUrl)
    if response.status_code == 200:
        res = response.json()
        customerId = res['custId']
        customerName = res['customerName']
        order = res['order']

        time.sleep(randint(3, 10))
        print("{} Cook: Hey {}, your {} is ready..".format(customerName, order))
        Queue_Url = "http://localhost:5001/customer/removeCustomer"
        #cust_header = {'Content-Type': 'application/json'}
        requests.delete(Queue_Url)
    elif response.status_code == 204:
        # print("Waiting for next order..")
        time.sleep(randint(3, 6))






if __name__ == '__main__':
 app.run(debug=True)

if __name__ == '__main__':
 app.debug = True
host = 'localhost'
port = 5000
app.run(host=host, port=port)