def calculate(amount, interest_rate, time):
    total_amount = amount + (amount * interest_rate * time) / 100
    interest = (amount * interest_rate * time) / 100
    return interest, total_amount


def print_result(interest, total_amount):
    print(f'The interest is: {interest}\nThe total amount is: {total_amount}')
