class Order:
    def __init__(self):
        self.products = []
        self.id = ""
        self.total_order = 0.00
    
    def get_subtotal(self, products):
        sum = 0
        i = 0
        while i < len(self.products):
            sum += self.products[i].total
            i += 1
        return sum
  

    def get_tax(self, sum):
        tax = sum * .065
        return tax
    

    def get_total(self, sum, tax):
        total = sum + tax
        return total
    

    def add_product(self, pro_fill):
        self.products.append(pro_fill)
    
    def display_receipt(self): 
        print("Order: {}".format(self.id))
        i = 0
        while i < len(self.products):
            self.products[i].display()
            i += 1
        sub_total = self.get_subtotal(self.products)
        print("Subtotal: ${0:.2f}".format(sub_total))
        tax = self.get_tax(sub_total)
        print("Tax: ${0:.2f}".format(tax))
        self.total_order = self.get_total(sub_total, tax)
        print("Total: ${0:.2f}".format(self.total_order))