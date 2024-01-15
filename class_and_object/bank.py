class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 1000

    def get_balance(self):
        return self.balance
    
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdaw(self, amount):
        if amount < self.min_withdraw:
            print(f'poor, you can withdraw value {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'restriction , you can not more than{self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is our present monay {self.get_balance()}')
        
brac = Bank(150000)

brac.withdaw(10)
brac.withdaw(10000)
brac.withdaw(1000)

brac.deposite(5000)
brac.withdaw(1000)