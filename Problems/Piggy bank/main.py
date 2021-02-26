class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        pool = self.dollars * 100 + deposit_dollars * 100 + self.cents + deposit_cents
        self.dollars = int(round(pool / 100, 1))
        self.cents = pool % 100
