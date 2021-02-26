# Write your code here
class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def state(self):
        print("The coffee machine has: \n%s of water\n%s of milk\n%s of coffee beans" % (self.water, self.milk,
                                                                                         self.beans))
        print("%s of disposable cups\n%s of money" % (self.cups, self.money))

    def stock(self, water, milk, beans, cups):
        if self.water < water or self.milk < milk or self.beans < beans or self.cups < cups:
            return False
        else:
            return True

    def buy(self):
        drink = ""
        while drink != "1" or drink != "2" or drink != "3":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            drink = input()
            # print(drink)
            if drink == "1":
                if self.water < 250 or self.milk < 0 or self.beans < 16 or self.cups < 1:
                    print("Sorry, but the coffee machine does not have enough ingredients for your drink")
                else:
                    self.water -= 250
                    self.beans -= 16
                    self.cups -= 1
                    self.money += 4
                break
            if drink == "2":
                if self.water < 350 or self.milk < 75 or self.beans < 20 or self.cups < 1:
                    print("Sorry, but the coffee machine does not have enough ingredients for your drink")
                else:
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.cups -= 1
                    self.money += 7
                break
            if drink == "3":
                if self.water < 200 or self.milk < 100 or self.beans < 12 or self.cups < 1:
                    print("Sorry, but the coffee machine does not have enough ingredients for your drink")
                else:
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.cups -= 1
                    self.money += 6
                break
            if drink == "back":
                break

    def fill(self):
        water = ""
        while not water.isdigit():
            print("Write how many ml of water do you want to add:")
            water = input()
        milk = ""
        while not milk.isdigit():
            print("Write how many ml of milk do you want to add:")
            milk = input()
        beans = ""
        while not beans.isdigit():
            print("Write how many grams of beans do you want to add:")
            beans = input()
        cups = ""
        while not cups.isdigit():
            print("Write how many disposable cups do you want to add:")
            cups = input()
        self.water += int(water)
        self.milk += int(milk)
        self.beans += int(beans)
        self.cups += int(cups)

    def take(self):
        print("I gave you %s" % self.money)
        self.money = 0

    def remaining(self):
        return self.state()


act = ""
coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while act != "exit":
    print()
    print("Write action (buy, fill, take, remaining, exit):")
    act = input()
    if act == "buy":
        coffee_machine.buy()
    elif act == "fill":
        coffee_machine.fill()
    elif act == "take":
        coffee_machine.take()
    elif act == "remaining":
        coffee_machine.remaining()
    elif act == "exit":
        break
    else:
        print("Command Unknown")
