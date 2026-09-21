class Product:

    def __init__(self, name, price, quantity=1):
        self.name = name
        if price > 0:
            self.price = price
        self.quantity = quantity
