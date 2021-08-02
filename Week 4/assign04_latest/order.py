'''
File: order.py
Use classes in Python to model an e-commerce system
Write programs that correctly use classes and objects to solve problems

All dollar amounts should be displayed to two decimals.

@author: Sunday Ogbonnaya Onwuchekwa

@class: CS 241 - 05
'''
class Order:
    ''' init - Initializes to id="", and products to an empty list [] '''
    def __init__(self):
        self.id = ""
        self.products = []

    ''' get_subtotal - Sums the price of each product and returns it '''
    def get_subtotal(self):
        sum = 0
        i = 0
        while i < len(self.products):
            sum += self.products[i].get_total_price()
            i += 1
        return sum
    
    ''' get_tax - Returns 6.5% times the subtotal '''
    def get_tax(self):
        subtotal = self.get_subtotal()
        tax = subtotal * .065
        return tax
    
    ''' get_total - Returns the subtotal plus the tax '''
    def get_total(self):
        total = self.get_subtotal() + self.get_tax()
        return total
    
    ''' add_product - Adds the provided product to the list '''
    def add_product(self, product):
        self.products.append(product)
    
    ''' display_receipt - Displays a receipt '''
    def display_receipt(self):
        print("Order: {}".format(self.id))
        i = 0
        while i < len(self.products):
            self.products[i].display()
            i += 1
            
        sub_total = self.get_subtotal()
        tax = self.get_tax()
        self.total_order = self.get_total()
        
        print("Subtotal: ${0:.2f}".format(sub_total))
        print("Tax: ${:.2f}".format(tax))
        print("Total: ${:.2f}".format(self.total_order))
        

        