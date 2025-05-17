class Coffee:
    def __init__(self,name):
        self.name = name 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffe name must be a string.")
        
        if not (3 <= len(value)):
            raise ValueError("Name must be atleast 3 characters.")
        
        self._name = value 

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        from order import Order
        return list(set(order.customer for order in Order.all if order.coffee == self))