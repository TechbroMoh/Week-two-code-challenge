import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture(autouse=True)
def clear_orders():
    """Fixture to clear Order.all_orders before each test."""
    Order.all_orders = []

def test_order_creation():
    customer = Customer("Felix")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_invalid_order_price():
    customer = Customer("Felix")
    coffee = Coffee("Espresso")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  

def test_order_all_orders():
    customer = Customer("Felix")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)
    assert Order.all_orders == [order]
