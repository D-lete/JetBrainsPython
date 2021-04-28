money = int(input())

chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

if money >= sheep and money // sheep >= 1:
    print(f"{money // sheep} sheep")
elif money >= cow < sheep and money // cow > 1:
    print(f"{money // cow} cows")
elif money >= cow < sheep and money // cow == 1:
    print(f"{money // cow} cow")  # Cow
elif money >= pig < cow and money // pig > 1:
    print(f"{money // pig} pigs")
elif money >= pig < cow and money // pig == 1:
    print(f"{money // pig} pig")  # Pig
elif money >= goat < pig and money // goat > 1:
    print(f"{money // goat} goats")
elif money >= goat < pig and money // goat == 1:
    print(f"{money // goat} goat")  # goat
elif money < goat >= chicken and money // chicken > 1:
    print(f"{money // chicken} chickens")
elif money < goat >= chicken and money // chicken == 1:
    print(f"{money // chicken} chicken")  # Chickens
elif money < chicken:
    print("None")
