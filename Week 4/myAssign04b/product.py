class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = 0.00
    
    def get_total_price(self):
        self.price = self.price * self.quantity
        return self.price
    
    def display(self):
        self.total = self.get_total_price()
        print("{} ({}) - ${:.2f}".format(self.name, self.quantity, self.total))