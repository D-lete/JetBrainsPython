# Write your code here
# Write your code here

import random


class ATM:

    def menu(self, user_input):
        print("1. Create an account \n 2. Log into account \n 0. Exit")
        self.user_input = user_input = input('>: ')
        if user_input == 1:
            ATM.gen_cc()
        elif user_input == 2:
            ATM.login()
        elif user_input == 0:
            ATM.exit()

    def gen_cc(self):

    def login(self):

    def exit(self):