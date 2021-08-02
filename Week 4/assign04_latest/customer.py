'''
File: customer.py
Use classes in Python to model an e-commerce system
Write programs that correctly use classes and objects to solve problems

All dollar amounts should be displayed to two decimals.

@author: Sunday Ogbonnaya Onwuchekwa

@class: CS 241 - 05
'''
class Customer:
    ''' init - Initializes to id="", name="", and orders to an empty list '''
    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = []
    
    ''' get_order_count - Returns the number of orders '''
    def get_order_count(self):
        quantity_ordered = len(self.orders)
        return quantity_ordered
    
    ''' get_total - Returns the total price of all orders combined '''
    def get_total(self):
        sum = 0
        i = 0
        while i < self.get_order_count():            
            sum += self.orders[i].get_total()
            i += 1
        return sum
    
    ''' add_order - Adds the provided order to the list of orders '''
    def add_order(self, order):
        self.orders.append(order)
    
    ''' display_summary - Displays a summary '''
    def display_summary(self):     
        self.total_order = self.get_total()        
        print("Summary for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print("Orders: {}".format(self.get_order_count()))
        print("Total: ${:.2f}".format(self.total_order))
    
    ''' display_receipts - Displays all the orders' receipts '''
    def display_receipts(self):
        print("Detailed receipts for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print()
        i = 0
        while i < self.get_order_count():
            self.orders[i].display_receipt()
            i += 1
            if(i < self.get_order_count()):
                print()