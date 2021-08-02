'''
File: product.py
Purpose: Write programs that correctly use classes and objects to solve problems.
'''
class Product:
    ''' init - Initializes to the values that were passed '''
    def __init__(self, ID, Name, Price, Quantity):
        self.id = ID
        self.name = Name
        self.price = Price
        self.quantity = Quantity
     
    ''' get_total_price - Returns the price multiplied by the quantity '''
    def get_total_price(self):
        total_price = self.price * self.quantity
        return total_price
    
    ''' display - Displays the products name, quantity, and total price in the following format: Pencil (10) - $12.90 '''
    def display(self):
        print("{} ({}) - ${:.2f}".format(self.name, self.quantity, self.get_total_price()))