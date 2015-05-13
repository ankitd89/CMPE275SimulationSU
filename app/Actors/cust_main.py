__author__ = 'rashmi'


import json
import sys
import time
from random import randint
import requests
import logging
logging.getLogger("requests").setLevel(logging.WARNING)


order = [["Burger", "Taco","Coke"], ["Noodles", "Rice"]]

def main():
    count =1
    while count != 2:
        createUrl = 'http://localhost:5001/customer'
        customerName = "Customer %d" %count
        custheader = {'Content-Type': 'application/json'}
        addCustomer = requests.post(createUrl, data=json.dumps({"custId": count, "customerName": customerName, "order": order[randint(0, 1)]}), headers=custheader)
        count += 1
        time.sleep(20)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("User interrupted")
        sys.exit(0)