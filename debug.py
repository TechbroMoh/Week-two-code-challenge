# debug.py

from customer import Customer
from coffee import Coffee
from order import Order

def main():
    print("Welcome to the Coffee Shop Debugging Console")
    while True:
        print("\nAvailable commands:")
        print("1. Create a new customer")
        print("2. Create a new coffee")
        print("3. Create a new order")
        print("4. List all orders")
        print("5. Show customer orders")
        print("6. Show coffee orders")
        print("7. Exit")

        choice = input("Enter a command number: ").strip()

        if choice == '1':
            name = input("Enter customer name (1-15 characters): ").strip()
            try:
                customer = Customer(name)
                print(f"Created customer: {customer.name}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            name = input("Enter coffee name (at least 3 characters): ").strip()
            try:
                coffee = Coffee(name)
                print(f"Created coffee: {coffee.name}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            customer_name = input("Enter customer name: ").strip()
            coffee_name = input("Enter coffee name: ").strip()
            price = float(input("Enter price (1.0 - 100.0): ").strip())
            
            # Find or create customer and coffee instances
            customer = next((c for c in Customer.all_customers if c.name == customer_name), None)
            if not customer:
                print("Customer not found.")
                continue

            coffee = next((c for c in Coffee.all_coffees if c.name == coffee_name), None)
            if not coffee:
                print("Coffee not found.")
                continue

            try:
                order = Order(customer, coffee, price)
                print(f"Created order: {order.customer.name} ordered {order.coffee.name} for ${order.price}")
            except ValueError as e:
                print(e)

        elif choice == '4':
            print("\nAll Orders:")
            for order in Order.all_orders:
                print(f"{order.customer.name} ordered {order.coffee.name} for ${order.price}")

        elif choice == '5':
            customer_name = input("Enter customer name to view orders: ").strip()
            customer = next((c for c in Customer.all_customers if c.name == customer_name), None)
            if customer:
                print(f"\nOrders for {customer.name}:")
                for order in customer.orders():
                    print(f"Ordered {order.coffee.name} for ${order.price}")
            else:
                print("Customer not found.")

        elif choice == '6':
            coffee_name = input("Enter coffee name to view orders: ").strip()
            coffee = next((c for c in Coffee.all_coffees if c.name == coffee_name), None)
            if coffee:
                print(f"\nOrders for {coffee.name}:")
                for order in coffee.orders():
                    print(f"Ordered by {order.customer.name} for ${order.price}")
            else:
                print("Coffee not found.")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid command. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
