# read animals.txt
# and write animals_new.txt

with open('animals.txt', 'rt', encoding='UTF-8') as animals:
    content = animals.readlines()
animals_new = open('animals_new.txt', 'wt', encoding='UTF-8')
for animal in content:
    staging = str.rstrip(str(animal), '\n')
    animals_new.write(staging + ' ')

animals.close()
animals_new.close()
