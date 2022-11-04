import json

first_family = json.loads(input())
second_family = json.loads(input())

new_fam = {**first_family, **second_family}
print(new_fam)
