from product import Product


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product, quantity: int):
        contains = False
        for item in self.products:
            if item.name == product.name:
                contains = True
        if contains:
            self.products.append(product)

    def remove_product(self, product_name: str):
        self.products = list(filter(lambda x: x.name != product_name, self.products))

    def calculate_total(self):
        total = 0
        if len(self.products):
            for product in self.products:
                total += product.price
        return total


product1 = Product("Laptop", 50000)
product2 = Product("Mouse", 1000)

cart = Cart()

cart.add_product(product1, 2)
cart.add_product(product2, 1)

print(cart.calculate_total())

cart.remove_product("Mouse")

print(cart.calculate_total())
