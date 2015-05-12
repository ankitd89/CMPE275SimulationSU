__author__ = 'rashmi'


import json
import sys
import time
from random import randint
import requests

order = [["Burger", "Taco","Coke"], ["Noodles", "Rice"]]

def main():
    count =1
    while True:
        createUrl = 'http://localhost:5001/customer'
        customerName = "Customer %d" %count
        custheader = {'Content-Type': 'application/json'}
        addCustomer = requests.post(createUrl, data=json.dumps({"custId": count, "customerName": customerName, "order": order[randint(0, 2)]}), headers=custheader)
        count += 1
        time.sleep(0.05)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("User interrupted")
        sys.exit(0)