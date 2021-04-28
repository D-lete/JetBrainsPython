class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(name):
        return str("Hello, I am {}!".format(name))


print(Person.greet(name=input()))
