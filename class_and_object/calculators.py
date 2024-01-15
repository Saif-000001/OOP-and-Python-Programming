class Calculator:
    brand = 'casio MS990'
    def add(self, n1, n2):
        return n1 + n2
    def deduct(self, n1, n2):
        return n1 - n2
    def multiple(self, n1, n2):
        return n1 * n2
    def divide(self, n1, n2):
        return n1/n2
    
my_calculator = Calculator()

add = my_calculator.add(7,5)
print(add)

sub = my_calculator.deduct(7,5)
print(sub)

multi = my_calculator.multiple(7,5)
print(multi)

div = my_calculator.divide(7,5)
print(div)