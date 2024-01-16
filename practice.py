class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class Shop:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f'product name {product.name} added to the shop.')
    
product1 = Product('pen', 5)
product2 = Product('kyboard', 500)

my_shop = Shop()

my_shop.add_product(product1)
my_shop.add_product(product2)

for product in my_shop.products:
    print(f'{product.name} - ${product.price}')

