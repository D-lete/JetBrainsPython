# Write your code here

import random


class ATM:

    def __init__(self):
        options_root = {1: ATM.__generator__(self),
                        2: ATM.__login__(self),
                        0: ATM.__exit__(self)}
        print('1. Create an account\n2. Log into account\n0. Exit')
        user_input = int(input('> '))
        options_root.get(user_input)

    def __generator__(self):
        self.card_number = str('400000') + str(random.)
        self.pin_code = str(random.randrange(1000, 9999, 1))
        self.balance = 0
        print('Your card number:\n{}\nYour card PIN:\n{}')
        ATM.__init__(self)

    def __login__(self):
        card = input('Enter your card number: \n> ')
        pin = input('Enter your PIN: \n> ')
        if card == self.card_number and pin == self.pin_code:
            print('You have successfully logged in!')
            ATM.__acct__(self)
        elif card != self.card_number or pin != self.pin_code:
            print('Wrong card number or PIN!')
            ATM.__init__(self)

    def __acct__(self):
        options_acct = {1: ATM.__balance__(self),
                        2: ATM.__logout__(self),
                        0: ATM.__exit__(self)}
        print('1. Balance\n2. Log into account\n0. Exit')
        user_input = int(input('> '))
        options_acct.get(user_input)

    def __balance__(self):
        print('Balance: ' + str(self.balance))
        ATM.__acct__(self)

    def __logout__(self):
        print('You have been successfully logged out!')
        ATM.__init__(self)

    def __exit__(self):
        print('Bye!')


ATM()
