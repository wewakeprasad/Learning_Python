planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#for planent in planents:
	#print(planent,' ')

#short_planets=[planet for planet in planents if len(planet)<6]
#short_planets

loud_short_planents=[planet.upper()+' ! ' for planet in planets if len(planet)<6 ]
loud_short_planents