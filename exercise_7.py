#!/usr/bin/python3

how_many = int( input("ile liczb zamierzasz wprowadzić?\n>> ") )

numbers_container = []
for count in range(1,how_many+1):
	numbers_container.append( int(input("Wprowadź liczbę nr {}: ".format(count))))
else:
	sum_ = sum(numbers_container)
	print( "Podałeś liczby ", *[x for x in numbers_container] )
	print("suma:",sum_, end=", ")
	print("średnia:",sum_ / how_many, end=", ")

	if sum_ > sum_ / how_many:
		print("suma jest większa!")
	elif sum_ == sum_ / how_many:
		print("suma równa średniej ;o")
	else:
		print("suma mniejsza od średniej")

