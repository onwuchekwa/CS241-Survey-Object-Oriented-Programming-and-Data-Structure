class Order:
    def __init__(self):
        self.id = str()
        self.products = []
        
    def get_subtotal(self, p1, p2):
        return p1 +p2
    
    def get_tax(self, sub):
        return sub * .065
    
    def get_total(self, sub, tax):
        return sub + tax
    
    def add_product(self, product):
        self.products.append(product.id)
        self.products.append(product.name)
        self.products.append(product.price)
        self.products.append(product.quantity)
        
    def display_receipt(self):
        i = 0
        subtotal = self.get_subtotal(self.products[2], self.products[6])
        tax = self.get_tax(subtotal)
        total = self.get_total(subtotal, tax)
        print("Order: {}".format(self.id))
        print("{} ({}) - ${:.2f}".format(self.products[1], self.products[3], self.products[2]))
        print("{} ({}) - ${:.2f}".format(self.products[5], self.products[7], self.products[6]))
        print("Subtotal: {:.2f}".format(subtotal))
        print("Tax: {:.2f}".format(tax))
        print("Total: {:.2f}".format(total))