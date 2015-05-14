__author__ = 'rashmi'


import json
import sys
import time
from random import randint
import requests
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


order = [["Burger", "Taco","Coke"], ["Noodles", "Rice"], ["Sandwich","Pepsi"], ["Pizza"], ["Smoothies", "Fries"], ["Spicy Red-Wine Spaghetti"]]

def main():
    count =1
    while count != 5:
        createUrl = 'http://localhost:5001/customer'
        customerName = "Customer %d" %count
        custheader = {'Content-Type': 'application/json'}
        addCustomer = requests.post(createUrl, data=json.dumps({"custId": count, "customerName": customerName, "order": order[randint(0, 5)]}), headers=custheader)
        count += 1
        time.sleep(20)
        
    time.sleep(50)
    print("Calling")
    meanUrl = 'http://localhost:5001/customer/displayWaitTime/' + str(count)
    addCustomer = requests.get(meanUrl)
    print(addCustomer)


print("Customer created")
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("User interrupted")
        sys.exit(0)