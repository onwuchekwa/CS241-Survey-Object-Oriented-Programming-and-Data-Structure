from product import Product
from order import Order

class Customer:
    def __init__(self):
        self.id = str()
        self.name = ""
        self.order = []
        
    def get_order_count(self):
        return len(self.order)
    
    def get_total(self, pc1, c1, pc2, c2):
        return 1.065 * ((pc1 * c1) + (pc2 * c2))
    
    def add_order(self, order):
        self.order.append(order.id)
        self.order.append(order.products)
        
    def display_summary(self):
        orders = self.get_order_count() / 2
        i = 1
        sub = 0
        
        while (i <= orders):
            sub += ((self.order[i][2] * self.order[i][3]) + (self.order[i][6] * self.order[i][7]))
            break
        total = 1.065 * sub
        
        print("Summary for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print("Orders: {}".format(orders))
        print("Total: {:.2f}".format(total))
        
    def display_receipts(self):
        i = 1
        orders = self.get_order_count()
        
        print("Detailed receipts for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        while (i < orders):
            print()
            print("Order: " + self.order[i-1])
            print("{} ({}) - ${:.2f}".format(self.order[i][1], self.order[i][3], self.order[i][2]))
            print("{} ({}) - ${:.2f}".format(self.order[i][5], self.order[i][7], self.order[i][6]))
            print("Subtotal: {:.2f}".format(((self.order[i][2] * self.order[i][3]) + (self.order[i][6] * self.order[i][7]))))
            print("Tax: {:.2f}".format(((self.order[i][2] * self.order[i][3]) + (self.order[i][6] * self.order[i][7])) * 0.065))
            total = self.get_total(self.order[i][2], self.order[i][3], self.order[i][6], self.order[i][7])
            print("Total: {:.2f}".format(total))
            i += 3
