# the following line reads the list from the input; do not modify it, please
my_numbers = [int(x) for x in input().split(" ")]
evens = [x for x in my_numbers if x % 2 == 0]
print(evens)

# work with the variable 'my_numbers'