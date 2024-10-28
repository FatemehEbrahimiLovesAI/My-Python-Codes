class Pizza:
    def __init__(self, name: str, size: str, price: int, ingredients):
        self.name = name
        self.size = size
        self.price = price
        self.ingredients = ingredients

    def get_price(self):
        return self.price

    def description(self):
        print(f"Pizza name: {self.name}\nPizza price: {self.price}\nIngredients: {self.ingredients}")

        
class Customer:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_order_history(self):
        for i, order in enumerate(self.orders, start=1):
            print(f"Order number {i}: {order.order_ID}")


class Order:
    def __init__(self, order_ID, customer):
        self.order_ID = order_ID
        self.customer = customer
        self.pizzas = []
        self.status = "not paid"

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calculate_total(self):
        return sum(pizza.price for pizza in self.pizzas)

    def update_status(self, status):
        self.status = status


class Menu:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
        else:
            print("Pizza not found")

    def display_menu(self):
        for i, pizza in enumerate(self.pizzas, start=1):
            print(f"{i}. {pizza.name}: ${pizza.price}")


class Pizzeria:
    def __init__(self):
        self.customers = []
        self.orders = []
        self.menu = Menu()

    def add_customer(self, name, phone_number, address):
        customer = Customer(name, phone_number, address)
        self.customers.append(customer)

    def create_order(self, order_ID, customer):
        order = Order(order_ID, customer)
        self.orders.append(order)
        customer.add_order(order)
        return order

    def add_pizza_to_menu(self, name, size, price, ingredients):
        pizza = Pizza(name, size, price, ingredients)
        self.menu.add_pizza(pizza)

    def view_order(self):
        print("Please choose an order from the list:")
        for i, order in enumerate(self.orders, start=1):
            print(f"{i}. Order ID: {order.order_ID}")
        choice = int(input("Your choice: ")) - 1
        return self.orders[choice] if 0 <= choice < len(self.orders) else None

    def update_order_state(self, order, status):
        if order in self.orders:
            order.update_status(status)
        else:
            print("Order not found")

    def show_all_orders(self):
        for i, order in enumerate(self.orders, start=1):
            print(f"{i}. Order ID: {order.order_ID}, Status: {order.status}")