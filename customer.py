#customer.py

from order import Order  # Import Order for the create_order method


class Customer:
    all_customers = []  

    def __init__(self, name):
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = name
        Customer.all_customers.append(self)  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = value

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})
