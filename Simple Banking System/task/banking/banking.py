# Write your code here
import random


class ATM:

    card_number = None
    pin_code = None
    balance = None

    @staticmethod
    def menu():
        print('1. Create an account \n2. Log into account \n0. Exit')
        user_input = input('> ')
        if user_input == '1':
            ATM.generator()
        elif user_input == '2':
            ATM.login()
        elif user_input == '0':
            ATM.exit()

    @staticmethod
    def generator():
        base_card = '400000' + str(random.randrange(100000000, 999999999) + random.randrange(1, 9))
        ATM.card_number = base_card
        ATM.pin_code = str(random.randrange(1000, 9999))
        ATM.balance = round(0, 2)
        print(f'Your card has been created \nYour card number: \n{ATM.card_number}\nYour card PIN: \n{ATM.pin_code}')
        ATM.menu()

    @staticmethod
    def login():
        print('Enter your card number:')
        user_card_number = input('> ')
        print('Enter your PIN:')
        user_pin_code = input('> ')
        if user_card_number == ATM.card_number and user_pin_code == ATM.pin_code:
            print('You have successfully logged in!')
            ATM.nav()
        elif user_card_number != ATM.card_number or user_pin_code != ATM.pin_code:
            print('Wrong card number or PIN!')
            ATM.menu()

    @staticmethod
    def nav():
        print('1. Balance \n2. Log out \n0. Exit')
        user_input = input('> ')
        if user_input == '1':
            print(f'Balance: 0')
            ATM.nav()
        elif user_input == '2':
            print('You have successfully logged out!')
            ATM.menu()
        elif user_input == '0':
            ATM.exit()

    @staticmethod
    def exit():
        print('Bye!')


ATM.menu()
