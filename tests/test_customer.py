import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_creation():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_invalid_customer_name():
    with pytest.raises(ValueError):
        Customer("A" * 16)

def test_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 5.0)
    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_customer_orders():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 5.0)
    assert customer.orders() == [order]

def test_customer_coffees():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    customer.create_order(coffee, 5.0)
    assert customer.coffees() == [coffee]
