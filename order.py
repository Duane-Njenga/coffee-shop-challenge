from customer import Customer
from coffee import Coffee

class Order:
    all = []
    def __init__(self, customer,coffee, price):
        if isinstance(customer, Customer):
            self.customer = customer
            customer._orders.append(self)

        if isinstance(coffee, Coffee):
            self.coffee = coffee

        Order.all.append(self)
        self.price = price

    @property
    def price(self):
        return self._price 
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("Price must be a float")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = value
    

customer_1 = Customer("Dim")
customer_2 =Customer("Szoboslai")
Mocha = Coffee("Mocha")
Latte = Coffee("Latte")

Order_1 =Order(customer_1, Mocha, 8.0)
Order_2 =Order(customer_1, Mocha, 8.0)
Order_3 =Order(customer_1, Latte, 8.0)
Order_4 =Order(customer_2, Mocha, 8.0)


# print(customer_1.orders())
# print(Mocha.orders())
print(Mocha.customers())
# print(customer_1.orders())


