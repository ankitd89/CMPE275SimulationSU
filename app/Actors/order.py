__author__ = 'rashmi'

class Order:
    def __init__(self, customerid, customername, orderName):
        self.customerid = customerid
        self.customername = customername
        self.orderName = orderName

    def displayOrder(self):
        print("Order => {}...{}...{}".format(self.customerid, self.customername, self.orderName))