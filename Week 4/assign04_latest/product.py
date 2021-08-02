'''
File: product.py
Use classes in Python to model an e-commerce system
Write programs that correctly use classes and objects to solve problems

All dollar amounts should be displayed to two decimals.

@author: Sunday Ogbonnaya Onwuchekwa

@class: CS 241 - 05
'''
class Product:
    ''' init - Initializes to the values that were passed '''
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
     
    ''' get_total_price - Returns the price multiplied by the quantity '''
    def get_total_price(self):
        total = self.quantity * self.price
        return total
    
    ''' display - Displays the products name, quantity, and total price '''
    def display(self):
        total_price = self.get_total_price()
        print("{} ({}) - ${:.2f}".format(self.name, self.quantity, total_price))
