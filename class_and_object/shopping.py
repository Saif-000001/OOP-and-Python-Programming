class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item':item, 'price':price, 'quantity':quantity}
        self.cart.append(product)

    def remove(self, item):
        self.cart.pop(item)

    def check_out(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print('total price', total)

        if amount < total:
            print(f'please provide {total - amount} more')
        else:
            extra = amount - total
            print(f'Here is your iteam and extra manoy: {extra}')
    
swapan = Shopping('Alan swapan')
swapan.add_to_cart('alu', 25, 2)
swapan.add_to_cart('pen', 5, 6)

print(swapan.cart)

swapan.check_out(1000)

swapan.remove(1)

print(swapan.cart)
