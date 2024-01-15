class Pen:
    # constructors 
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

my_pen = Pen('My', 'i-team', '15')
print(my_pen.owner, my_pen.brand, my_pen.price)

her_pen = Pen('she', 'matador', '10')
print(her_pen.owner, her_pen.brand, her_pen.price)

they_pen = Pen('They', 'matador all-time', '5')
print(they_pen.owner, they_pen.brand, they_pen.price)