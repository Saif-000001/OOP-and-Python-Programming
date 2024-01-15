class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer
    
    def add_to_cart(self, item):
        self.cart.append(item)

mehzaa = Shop('mehzaa')
mehzaa.add_to_cart('shoes')
mehzaa.add_to_cart('cap')
print(mehzaa.cart)

apur = Shop('apur')
apur.add_to_cart('pant')
apur.add_to_cart('shart')
print(apur.cart)