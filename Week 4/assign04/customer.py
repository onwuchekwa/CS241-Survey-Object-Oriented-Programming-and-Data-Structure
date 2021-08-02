'''
File: customer.py
Purpose: Write programs that correctly use classes and objects to solve problems.
All dollar amounts should be displayed to two decimals.
'''
class Customer:
    ''' init - Initializes to id="", name="", and orders to an empty list [] '''
    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = []
    
    ''' get_order_count - Returns the number of orders '''
    def get_order_count(self):
        return len(self.orders)
    
    ''' get_total - Returns the total price of all orders combined '''
    def get_total(self, product1, customer1, product2, customer2):
        return 1.065 * ((product1 * customer1) + (product2 * customer2))
    
    ''' add_order - Adds the provided order to the list of orders '''
    def add_order(self, order):
        self.orders.append(order.id)
        self.orders.append(order.products)
        
    ''' display_summary - Displays a summary as follows:
        Summary for customer 'aa32':
        Name: Gandalf
        Orders: 1
        Total: $3077.57
    '''
    def display_summary(self):
        order = self.get_order_count() / 2
        i = 1
        subtotal = 0
        
        while (i <= order):
            subtotal += ((self.orders[i][2] * self.orders[i][3]) + (self.orders[i][6] * self.orders[i][7]))
            break
        total = 1.065 * subtotal
        
        print("Summary for customer {}".format(self.id))
        print("Name: {}".format(self.name))
        print("Orders: {}".format(self.orders))
        print("Total: {}".format(total))
    
    ''' display_receipts - Displays all the orders' receipts as follows:
        Detailed receipts for customer 'aa32':
        Name: Gandalf

        Order: 1138
        Sword (10) - $18999.90
        Shield (6) - $5938.50
        Subtotal: $2889.74
        Tax: $187.83
        Total: $3077.57

        Order: 1277182
        The Ring (1) - $1000000.00
        Wizard Staff (3) - $599.97
        Subtotal: $1000199.99
        Tax: $65013.00
        Total: $1065212.99
    '''
    def display_receipts(self):
        order = self.get_order_count()
        i = 1
        print("Detailed receipts for customer {}".format(self.id))
        print("Name: {}".format(self.name))
        while (i < order):
            print()
            print("Orders: " + self.orders[1-1])
            print("{} ({}) - ${:.2f}".format(self.orders[i][1], self.orders[i][3], self.orders[i][2]))
            print("{} ({}) - ${:.2f}".format(self.orders[i][5], self.orders[i][7], self.orders[i][6]))
            print("Subtotal: ${:.2f}".format(((self.orders[i][2] * self.orders[i][3]) + (self.orders[i][6] * self.orders[i][7]))))
            print("Tax: ${:.2f}".format(((self.orders[i][2] * self.orders[i][3]) + (self.orders[i][6] * self.orders[i][7])) * 0.065))
            total = self.get_total(self.orders[i][2], self.orders[i][3], self.orders[i][6], self.orders[i][7])
            print("Total: ${:.2f}".format(total))
            i += 3