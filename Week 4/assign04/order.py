'''
File: order.py
Purpose: Write programs that correctly use classes and objects to solve problems.
'''
class Order:
    ''' init - Initializes to id="", and products to an empty list [] '''
    def __init__(self):
        self.id = ""
        self.products = []
    
    ''' get_subtotal - Sums the price of each product and returns it '''
    def get_subtotal(self):
        self.subtotal = self.products[2] + self.products[6]
        return self.subtotal

    ''' get_tax - Returns 6.5% times the subtotal '''
    def get_tax(self):
        self.tax = self.get_subtotal() * (6.5 / 100)
        return self.tax
    
    ''' get_total - Returns the subtotal plus the tax '''
    def get_total(self):
        self.total = self.get_subtotal() + self.get_tax()
        return self.total
    
    '''add_product - Adds the provided product to the list '''
    def add_product(self, product):
        self.products.append(product.id)
        self.products.append(product.name)
        self.products.append(product.price)
        self.products.append(product.quantity)
    
    ''' display_receipt - Displays a receipt in the format:
        Order: 1138
        Sword (10) - $18999.90
        Shield (6) - $5938.50
        Subtotal: $2889.74
        Tax: $187.83
        Total: $3077.57
    '''
    def display_receipt(self):
        print("Order: {}".format(self.id))
        print("{} ({}) - ${:.2f}".format(self.products[1], self.products[3], self.products[2]))
        print("{} ({}) - ${:.2f}".format(self.products[5], self.products[7], self.products[6]))
        print("Subtotal: ${:.2f}".format(self.get_subtotal()))
        print("Tax: ${:.2f}".format(self.get_tax()))
        print("Total: ${:.2f}".format(self.get_total()))