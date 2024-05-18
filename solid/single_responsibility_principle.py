class Invoice:
    def __init__(self, number, customer, items):
        self.number = number
        self.customer = customer
        self.items = items

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

    def print_invoice(self):
        print("Invoice Number:", self.number)
        print("Customer:", self.customer)
        print("Items:")
        for item in self.items:
            print(item.name, "-", item.price, "x", item.quantity)
        print("Total:", self.calculate_total())

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity