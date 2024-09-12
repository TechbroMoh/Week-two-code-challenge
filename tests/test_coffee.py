import pytest
from coffee import Coffee
from customer import Customer  
from order import Order  


def test_coffee_creation():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_invalid_coffee_name():
    with pytest.raises(ValueError):
        Coffee("AE")

def test_coffee_orders():
    coffee = Coffee("Latte")
    customer = Customer("Felix")
    order = customer.create_order(coffee, 5.0)
    assert coffee.orders() == [order]

def test_coffee_customers():
    coffee = Coffee("Latte")
    customer = Customer("Felix")
    customer.create_order(coffee, 5.0)
    assert coffee.customers() == [customer]

def test_coffee_num_orders():
    coffee = Coffee("Latte")
    customer = Customer("Felix")
    customer.create_order(coffee, 5.0)
    assert coffee.num_orders() == 1

def test_coffee_average_price():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 6.0)
    assert coffee.average_price() == 5.5
