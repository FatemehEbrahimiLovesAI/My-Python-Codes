class Pizza:
    """
    In this class, the pizzas in the pizzeria are
    stored and managed with different characteristics.
    
    Attributes:
        name(str) : it is pizza's name
        size(str) : Each pizza has a specific size.
        price(int) : Pizza payment price in dollars.
        ingredients(list) : A list of different ingredients used in pizza baking.
    
    Example:
    pepperoni_pizza = Pizza("pepperoni","medium",25,["Pepperoni sausage", "pizza cheese", "tomato", "red pepper", "ketchup", "thyme"])
    """
    def __init__(self, name: str, size: str, price: int, ingredients):
        self.name = name
        self.size = size
        self.price = price
        self.ingredients = ingredients
        self.ingredients_str = ", ".join(self.ingredients)

    def __str__(self):
        return f"{self.name} : \n\tsize = {self.size} , \n\tprice = {self.price} \n\t ingredients = {self.ingredients_str}"

    def __repr__(self):
        return f"Pizza('{self.name}','{self.size}',{self.price},{self.ingredients})"

    def get_price(self):
        return self.price

    def description(self):
        print(f"Pizza name: {self.name}\nPizza price: {self.price}\nIngredients: {self.ingredients_str}")


class Customer:
    def __init__(self, name: str, phone_number: str, address: str = ""):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.orders = []

    def __str__(self):
        return f"{self.name}: \nphone = {self.phone_number}\naddress = {self.address}"

    def __repr__(self):
        return f"Customer('{self.name}','{self.phone_number}','{self.address}')"

    def add_order(self, order):
        self.orders.append(order)

    def get_order_history(self):
        for i, order in enumerate(self.orders, start=1):
            print(f"Order number {i}: {order.order_ID}")


class Order:
    orders = []
    order_IDs = []

    def __init__(self, order_ID, customer):
        while order_ID in Order.order_IDs:
            print(f"Error! This ID ({order_ID}) already exists!")
            order_ID = input("order ID = ")
        self.order_ID = order_ID
        Order.order_IDs.append(order_ID)
        self.customer = customer
        self.pizzas = []
        self.status = "not paid"
        Order.orders.append(self)

    def __str__(self):
        pizza_names = ", ".join([pizza.name for pizza in self.pizzas])
        return (f"Order ID: {self.order_ID}\n"
                f"Customer: {self.customer.name}\n"
                f"Pizzas: {pizza_names if pizza_names else 'No pizzas added'}\n"
                f"Status: {self.status}")

    def __repr__(self):
        return f"Order('{self.order_ID}', Customer('{self.customer.name}', '{self.customer.phone_number}', '{self.customer.address}'))"

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calculate_total(self):
        return sum(pizza.price for pizza in self.pizzas)

    def update_status(self, status):
        self.status = status


class Menu:
    def __init__(self):
        self.pizzas = []

    def __str__(self):
        if not self.pizzas:
            return "Menu is empty."
        return "\n".join([f"{i+1}. {pizza.name} - {pizza.size} (${pizza.price})" for i, pizza in enumerate(self.pizzas)])

    def __repr__(self):
        return f"Menu({self.pizzas})"

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
        else:
            print("Pizza not found")

    def display_menu(self):
        if not self.pizzas:
            print("The menu is empty.")
        else:
            for i, pizza in enumerate(self.pizzas, start=1):
                print(f"{i}. {pizza.name}: ${pizza.price}")


class Pizzeria:
    def __init__(self):
        self.customers = []
        self.orders = []
        self.menu = Menu()

    def __str__(self):
        customer_names = ", ".join([customer.name for customer in self.customers])
        order_ids = ", ".join([order.order_ID for order in self.orders])
        return (f"Pizzeria:\n"
                f"Customers: {customer_names if customer_names else 'No customers added'}\n"
                f"Orders: {order_ids if order_ids else 'No orders created'}\n"
                f"Menu:\n{str(self.menu)}")

    def __repr__(self):
        return f"Pizzeria(customers={self.customers}, orders={self.orders}, menu={self.menu})"

    def display_menu(self):
        self.menu.display_menu()

    def add_customer(self, name, phone_number, address=""):
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

    def delete_order(self, order):
        if order in self.orders:
            self.orders.remove(order)
        else:
            print("Order not found")


pizzeria = Pizzeria()

while True:
    print("welcome to pizzeria management system")
    print("what do you want to do?\n\t1-show menu\n\t2-go to orders panel\n\t3-add new Pizza\n\t4-add new Customer")
    try:
        present_choice = int(input("your choice= "))
    except ValueError:
        print("Please enter a valid choice number.")
        continue

    if present_choice == 1:
        pizzeria.display_menu()

    elif present_choice == 2:
        print("you are in order management.")
        print("which do you need?\n\t1-add an order\n\t2-change an order status\n\t3-delete an order\n\t4-show orders")
        try:
            order_choice = int(input("please enter your choice: "))
        except ValueError:
            print("Please enter a valid choice number.")
            continue

        if order_choice == 1:
            customer_name = input("Please enter customer's name: ")
            customer = next((c for c in pizzeria.customers if c.name == customer_name), None)
            if customer is None:
                print("Customer not found. Please add the customer first.")
            else:
                order_ID = input("Please enter a new order ID: ")
                new_order = pizzeria.create_order(order_ID, customer)

        elif order_choice == 2:
            pizzeria.show_all_orders()
            try:
                choice = int(input("Please tell me which order do you want to change the status of?")) - 1
                if 0 <= choice < len(pizzeria.orders):
                    present_order = pizzeria.orders[choice]
                    new_status = input("Enter new status: ")
                    pizzeria.update_order_state(present_order, new_status)
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")

        elif order_choice == 3:
            pizzeria.show_all_orders()
            try:
                choice = int(input("Please tell me which order do you want to delete?")) - 1
                if 0 <= choice < len(pizzeria.orders):
                    present_order = pizzeria.orders[choice]
                    pizzeria.delete_order(present_order)
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")

        elif order_choice == 4:
            pizzeria.show_all_orders()

    elif present_choice == 3:
        pizza_name = input("Please enter Pizza's name: ")
        print('*' * 30)
        pizza_size = input("Please enter Pizza's size (Big/Medium/Small): ")
        print('*' * 30)
        try:
            pizza_price = int(input("Please enter Pizza's price: "))
        except ValueError:
            print("Invalid price, please enter a number.")
            continue
        print('*' * 30)
        this_pizza_ingredients = input("Please enter ingredients= (separate with ,)")
        pizza_ingredients = this_pizza_ingredients.split(",")
        pizzeria.add_pizza_to_menu(pizza_name, pizza_size, pizza_price, pizza_ingredients)

    elif present_choice == 4:
        customer_name = input("Please enter Customer's name: ")
        print('*' * 35)
        customer_phone_number = input("Please enter Customer's phone: ")
        print('*' * 35)
        customer_address = input("Please enter Customer's address if you need: ")
        print('*' * 35)
        pizzeria.add_customer(customer_name, customer_phone_number, customer_address)