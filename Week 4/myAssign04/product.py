
"""
Product class, needs no imports but is imported everywhere else
for inputting items that will be stored in order


"""


class Product:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.price = 0.00
        self.quantity = 0
        self.total = 0.00
    
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_total_price(self):
        total = self.price * self.quantity
        return total
    
    def display(self):
        self.total = self.get_total_price()
        print("{} ({}) -".format(self.name, self.quantity, ),"${0:.2f}".format(self.total))

    