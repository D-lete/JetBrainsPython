# Write your code here

import random


class ATM:

    def __init__(self, card_number, pin_code, balance):
        self.card_number = card_number
        self.pin_code = pin_code
        self.balance = balance
        options_root = {1: ATM.generator(self, card_number, pin_code, balance),
                        2: ATM.login(self),
                        0: ATM.exit(self)}

        print('1. Create an account\n2. Log into account\n0. Exit')
        user_input = int(input('> '))
        options_root.get(user_input)

    def generator(self, card_number, pin_code, balance):
        if card_number == 0:
            self.card_number = str('400000') + str(random.randint(1000000000, 9999999999))
        if pin_code == 0:
            self.pin_code = str(random.randrange(1000, 9999, 1))
        if balance == 0:
            self.balance = 0
        print('Your card number:\n %s Your card PIN:\n %s' % (self.card_number, self.pin_code))
        ATM.__init__(self, card_number=self.card_number, pin_code=self.pin_code, balance=self.balance)

    def login(self):
        card = input('Enter your card number: \n> ')
        pin = input('Enter your PIN: \n> ')
        if card == self.card_number and pin == self.pin_code:
            print('You have successfully logged in!')
            ATM.acct(self)
        elif card != self.card_number or pin != self.pin_code:
            print('Wrong card number or PIN!')
            ATM.__init__(self, card_number=self.card_number, pin_code=self.pin_code, balance=self.balance)

    def acct(self):
        options_acct = {1: ATM.balance(self),
                        2: ATM.logout(self),
                        0: ATM.exit(self)}
        print('1. Balance\n2. Log into account\n0. Exit')
        user_input = int(input('> '))
        options_acct.get(user_input)

    def balance(self):
        print('Balance: ' + str(self.balance))
        ATM.acct(self)

    def logout(self):
        print('You have been successfully logged out!')
        ATM.__init__(self, card_number=self.card_number, pin_code=self.pin_code, balance=self.balance)

    def exit(self):
        print('Bye!')
        exit()


ATM.__init__(self, card_number=0, pin_code=0, balance=0)
