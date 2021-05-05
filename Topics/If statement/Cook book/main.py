pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

recipes = {'pasta': list(pasta.split(', ')), 'apple pie': list(apple_pie.split(', ')),
           'ratatouille': list(ratatouille.split(', ')), 'chocolate cake': list(chocolate_cake.split(', ')),
           'omelette': list(omelette.split(', '))}
ingredient = str(input())
print(list(recipes.keys())[list(recipes.values()).index(ingredient)])
