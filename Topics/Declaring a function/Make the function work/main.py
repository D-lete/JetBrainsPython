def closest_higher_mod_5(x):
	if x % 5 == 0:
		return x
	else:
		while x % 5 != 0:
			x += 1 % 5
		return x

