class Compounder:

    def __init__(self, balance):
        self.balance = balance
        self.interest = 0.071 * self.balance
        self.balance += self.interest
        self.years = 0
        while self.balance < 700000:
            self.years += 1

    def deposit(self, balance):
        balance += self.deposit
        return self.years

    deposit(balance=())
