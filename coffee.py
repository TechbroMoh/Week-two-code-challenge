#coffee.py

from order import Order  # Import Order to access orders in methods


class Coffee:
    all_coffees = []  

    def __init__(self, name):
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = name
        Coffee.all_coffees.append(self)  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)
