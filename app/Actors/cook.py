import queue
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


from queue import Queue


class Orders:
    """Base class for order object"""
    def __init__(self, customerid, customername, itemname):
        self.customerid = customerid
        self.customername = customername
        self.itemname = itemname

    def displayOrder(self):
        print("Order => {}...{}...{}".format(self.customerid, self.customername, self.itemname))


o=Orders(123,'Nupoor',1)

q=queue.Queue()

q.put(o)
o=Orders(123,'Nupoor',1)
q.put(o)
o=Orders(123,'Nupoor',1)
q.put(o)
o=Orders(123,'Nupoor',1)
q.put(o)

@app.route('/queue/readQueue', methods=['DELETE'])
def read_queue():
    if q.empty():
        result_JSON = {
            'response': 'Empty Order'
        }

        json_data = jsonify(result_JSON)
        json_data.status_code = 204

    else:
        order = q.get(block=False)

        result_JSON = {
            'custId': order.customerid,
            'customerName': order.customername,
            'itemName': order.itemname
        }

        json_data = jsonify(result_JSON)
        json_data.status_code = 200

    return json_data


if __name__ == '__main__':
 app.run(debug=True)

if __name__ == '__main__':
 app.debug = True
#host = sys.argv[1]
#port = int(sys.argv[2])
host = 'localhost'
port = 5000
app.run(host=host, port=port)