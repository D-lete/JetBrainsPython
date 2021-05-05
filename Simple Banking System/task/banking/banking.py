# Write your code here
import random


class ATM:

    def __init__(self, card_number, pin_code, balance):
        self.card_number = card_number
        self.pin_code = pin_code
        self.balance = balance
        self.menu()

    def menu(self):
        print("1. Create an account \n2. Log into account \n0. Exit")
        user_input = str(input('> '))
        if user_input == 1:
            self.gen_cc(card_number=None, pin_code=None, balance=None)
        elif user_input == 2:
            self.login()
        elif user_input == 0:
            self.exit()

    @staticmethod
    def gen_cc(card_number, pin_code, balance):
        card_number = '400000' + str(random.randrange(1000000000, 9999999999, 1))
        pin_code = str(random.randrange(1000, 9999, 1))
        balance = 0
        print(f'Your card has been created \nYour card number:\n{card_number} \nYour card PIN:\n{pin_code}')

    def acct_options(self):
        print("1. Balance \n2. Log out \n0. Exit")
        user_input = str(input('> '))
        if user_input == 1:
            print('Balance: {}'.format(self.balance))
        elif user_input == 2:
            print('You have successfully logged out!')

            self.menu()
        elif user_input == 0:
            exit()

    def login(self, card_number, pin_code):
        print('Enter your card number:')
        user_card_entry = input('> ')
        print('Enter your PIN:')
        user_pin_entry = input('> ')
        if user_card_entry != card_number or user_pin_entry != pin_code:
            print('Wrong card number or PIN!')
            self.menu()
        elif user_card_entry == card_number and user_pin_entry == pin_code:
            print('You have successfully logged in!')
            self.acct_options()

    def exit(self=None):
        print('Bye!')
        breakpoint()


ATM(card_number=None, pin_code=None, balance=None)
