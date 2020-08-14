water_needed = int(200)
milk_needed = int(50)
coffee_needed = int(15)

cups_of_coffee = int(input("How many cups of coffee would you like?: "))

water_reserve = int(400)
milk_reserve = int(100)
coffee_reserve = int(30)


def coffee_water():
	cw = cups_of_coffee * water_needed
	return cw


def coffee_milk():
	cm = cups_of_coffee * milk_needed
	return cm


def coffee_coffee():
	cc = cups_of_coffee * coffee_needed
	return cc


def coffee_product():
	cups = min(water_reserve // coffee_water(), milk_reserve // coffee_milk(),
												coffee_reserve // coffee_coffee())
	return cups


if cups_of_coffee > 0 and water_reserve > 0 and milk_reserve > 0 and coffee_reserve > 0:
	print(f"{coffee_product()} cups of coffee can be made.")
else:
	print("No cups of coffee can be made")

