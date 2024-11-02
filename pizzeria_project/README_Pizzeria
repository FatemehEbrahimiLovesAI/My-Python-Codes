Pizza Shop System

A Python project to manage a pizza shop, handling operations for pizzas, customers, orders, and menu management. This system allows users to add and view pizzas, manage customers, create and track orders, and display the menu. Ideal for small businesses or for learning OOP in Python.

Project Structure

The project is organized with the following main classes:

Classes

1. Pizza

Represents a pizza item with attributes:

name: Name of the pizza.

size: Size of the pizza (Big, Medium, Small).

price: Price of the pizza.

ingredients: List of ingredients.


Methods:

get_price(): Returns the price of the pizza.

description(): Prints a detailed description of the pizza.




2. Customer

Holds customer details:

name: Customer's name.

phone_number: Contact phone number.

address: Delivery address (optional).

orders: A list of the customer's orders.


Methods:

add_order(order): Adds an order to the customer's history.

get_order_history(): Displays the customer's order history.




3. Order

Manages an individual order:

order_ID: Unique identifier for the order.

customer: The customer who placed the order.

pizzas: List of pizzas in the order.

status: Current status of the order ("not paid", "paid", "canceled").


Methods:

add_pizza(pizza): Adds a pizza to the order.

calculate_total(): Calculates the total cost of the order.

update_status(status): Updates the order status.




4. Menu

Represents the pizza shop's menu.

pizzas: A list of available pizzas in the menu.


Methods:

add_pizza(pizza): Adds a pizza to the menu.

remove_pizza(pizza): Removes a pizza from the menu.

display_menu(): Displays the menu with pizza names and prices.




5. Pizzeria

Central class to manage the pizza shop's operations.

customers: List of customers.

orders: List of all orders.

menu: Instance of the Menu class, managing available pizzas.


Methods:

display_menu(): Displays the menu.

add_customer(name, phone_number, address): Adds a new customer.

create_order(order_ID, customer): Creates an order for a customer.

view_order(): Allows viewing of a specific order by ID.

update_order_state(order, status): Updates the status of an order.

show_all_orders(): Displays all orders with their status.

delete_order(order): Removes an order from the system.





How to Use

1. Clone this repository to your local machine.


2. Ensure Python 3.x is installed on your machine.


3. Run the system:

Interact with the console interface to manage pizzas, customers, and orders.

Choose options to add customers, create and manage orders, and update statuses as needed.




Future Improvements

Enhance User Interface: Implement a graphical user interface (GUI) for easier order management.

Expand Validations and Error Handling: Add more checks to handle user input errors.

Order Status Tracking: Add timestamps or history tracking for status updates.

Advanced Customer Management: Add features for editing customer details or searching by name.
