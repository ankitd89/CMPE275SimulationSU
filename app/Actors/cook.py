
from flask import Flask
import time
import logging
import requests
from random import randint

app = Flask(__name__)
host = None
port = None

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

while(True):
    req_custQueueUrl = "http://localhost:3000/queue/readQueue"
    response = requests.delete(req_custQueueUrl)
    if response.status_code == 200:
        res = response.json()
        customerId = res['custId']
        customerName = res['customerName']
        orderName = res['orderName']
        time.sleep(randint(3, 10))
        print("Cook: Hey {}, for {} is ready..".format(orderName,customerName))
        Queue_Url = "http://localhost:5001/customer/removeCustomer"
        requests.delete(Queue_Url)
    elif response.status_code == 204:
        # print("Waiting for next order..")
        time.sleep(randint(3, 6))


if __name__ == '__main__':
 app.debug = True
host = 'localhost'
port = 4001
app.run(host=host, port=port)