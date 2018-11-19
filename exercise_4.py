#def dogs_age(ages):
#	dog_age = 0	
#	for x in range(ages):
#		if x<2:
#			dog_age+=10.5
#		else:
#			dog_age+=4
#	else:
#		return dog_age


def dogs_age(ages):
	fist_years = 2*10.5 if ages>2 else ages*10.5
	if ages > 2:
		return (ages-2)*4 + fist_years
	return fist_years


#azor = dogs_age(1.5)  # spodziewany wynik: 1.5 * 10.5 = 15.75
#
#burek = dogs_age(5)  # spodziewany wynik: 2 * 10.5 + 3 * 4 = 33
#
#print(azor)
#print(burek)
