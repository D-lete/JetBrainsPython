# our class Ship

class Ship:
    def __init__(self, name, capacity, destination):
        self.name = name
        self.destination = destination
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self):
        return "The {} has sailed for {}!".format(self.name, self.destination)


black_pearl = Ship("Black Pearl", 800, input())

print(Ship.sail(self=black_pearl))
