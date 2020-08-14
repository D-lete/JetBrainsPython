water_needed = 200
milk_needed = 50
coffee_needed = 15

cups_of_coffee = int(input("How many cups of coffee would you like?: "))

water_reserve = int(input(400))
milk_reserve = int(input(100))
coffee_reserve = int(input(30))


def coffee_water():
	cw = cups_of_coffee * water_needed
	return int()


def coffee_milk():
	cm = cups_of_coffee * milk_needed
	return int()


def coffee_coffee():
	cc = cups_of_coffee * coffee_needed
	return int()


def coffee_product():
	min(water_reserve // coffee_water(), milk_reserve // coffee_milk(), coffee_reserve // coffee_coffee())
	return int()
	

if cups_of_coffee > 0 and water_reserve > 0 and milk_reserve > 0 and coffee_reserve > 0:
	print(f"{coffee_product()} cups of coffee can be made.")
else:
	print("No cups of coffee can be made")

