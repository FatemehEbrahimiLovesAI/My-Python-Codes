 class Pizza:
    def __init__(self,name: str,size: str,price: int, ingredients):
        self.name= name
        self.size= size
        self.price= price
        self.ingredients= ingredients
    
    def get_price(self):
        return self.price
        
    def description(self):
        print(f"Pizza name: {self.name}\nPizza price:{self.price}\nthe list of ingredients:{self.ingredients}")
        
        
class Customer:
    def __init__(self,name,phone_number, address,orders):
        self.name= name
        self.phone_number= phone_number
        self.address= address
        self.orders= []
        
    def add_order(self,order):
        self.orders.append(order)
        
    def get_order_history(self):
        for i,order in enumerate(self.orders,start=1):
            print(f"order number{i}= {order.name}")
        
class Order:
    def __init__(self,order_ID, customer,pizzas,status):
        self.order_ID = order_ID
        self.customer= customer
        self.pizzas= []
        self.status= "not paid"
        
    def add_pizza(self,pizza):
        self.pizzas.append(pizza)
        
    def calculate_total(self):
        total = 0
        for pizza in self.pizzas:
            total+= pizza.price
        return total
        
    def update_status(self,status):
        self.status= status
    
            
class Menu:
    pizzas = []
    
    def add_pizza(self,pizza,price):
        self.pizza= pizza
        
    def remove_pizza(self,pizza):
        for i in pizzas:
            if pizzas[i]== pizza:
                del pizzas[i]
        else:
            print("pizza's name not found ")
            
    def display_menu(self):
        for i,pizza in enumerate(pizzas):
            print(f"{i}= {pizza.name}\t :{pizza.price}")
    

class PizzaShop:
    customers= []
    orders= []
    manu= Menu()
    
    def add_customer(self):
        pass
        
    def create_order(self):
        pass
        
    def add_pizza_to_order(self):
        pass
    
    def view_oder(self):
        pass
    
    def update_order_state(self):
        pass
    
    def show_all_orders(self):
        pass
