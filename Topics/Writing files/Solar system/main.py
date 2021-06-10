# create the planets.txt
sol = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets = open('planets.txt', 'wt', encoding='utf-8')
for planet in sol:
    planets.writelines(planet + '\n')
planets.close()
