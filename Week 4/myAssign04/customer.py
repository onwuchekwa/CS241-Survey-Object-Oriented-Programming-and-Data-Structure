class Customer:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = []
        self.total_order_summary = 0.00
        
    def get_order_count(self):
        return int(len(self.orders))    
    
    def get_total(self):
        sum = 0
        i = 0
        while i < self.get_order_count():            
            sum += self.orders[i].total_order
            i += 1
        return sum

    def add_order(self, order):
        self.orders.append(order)
    
    def display_summary(self):
        print("Summary for customer '{}':\nName: {}".format(self.id, self.name))
        self.total_order_summary = self.get_total()
        print("Orders: {}".format(self.get_order_count())+"\nTotal: ${0:.2f}".format(self.total_order_summary))

    def display_receipts(self):
        print("Detailed receipts for customer '{}':\nName: {}\n".format(self.id, self.name))
        i = 0
        while i < self.get_order_count():
            self.orders[i].display_receipt()
            print()
            i += 1