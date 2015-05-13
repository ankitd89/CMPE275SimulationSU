__author__ = 'Ankit'

from flask import Flask
import time
import requests
from random import randint
import json
import logging
logging.getLogger("requests").setLevel(logging.WARNING)

app = Flask(__name__)
host = None
port = None

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

while(True):
    req_custQueueUrl = "http://localhost:3001/queue/readQueue"
    response = requests.delete(req_custQueueUrl)
    if response.status_code == 200:
        start=time.time()
        res = response.json()
        customerId = res['custId']
        customerName = res['customerName']
        orderName = res['orderName']
        time.sleep(randint(3, 10))
        endtime=round(time.time()-start,2)
        print("Cook: Hey {}, for {} is ready..".format(orderName,customerName))
        print("Cook took {} to prepare ".format(endtime))
        coordinatorProcessedQueueUrl = 'http://localhost:6001/coordinator/processedorder'
        header = {'Content-Type': 'application/json'}
        addOrder = requests.post(coordinatorProcessedQueueUrl,
                                 data=json.dumps({"custId": customerId, "customerName": customerName, "orderName": orderName}),
                                 headers=header)
    elif response.status_code == 204:
        # print("Waiting for next order..")
        time.sleep(randint(3, 6))

if __name__ == '__main__':
    host = 'localhost'
    port = 4001
    app.run(host=host, port=port)