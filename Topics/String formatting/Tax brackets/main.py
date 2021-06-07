income = int(input())
if income <= 15527:
    percent = int(0)
elif 15528 <= income <= 42707:
    percent = int(15)
elif 42708 <= income <= 132406:
    percent = int(25)
elif income >= 132407:
    percent = int(28)
else:
    percent = int(0)
tax_amt = int(round(income * (percent / 100), 0))
print(f'The tax for {income} is {percent}%. That is {tax_amt} dollars!')
