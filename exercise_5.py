#!/usr/bin/python3
from math import sqrt

print('Równanie w postaci ax**2 + bx + c == 0')

a = int( input('podaj a: ') )
b = int( input('podaj b: ') )
c = int( input('podaj c: ') )


delta = b**2 - 4*a*c
if delta > 0:
	print( "Pierwiastek x_1: ", (-b-sqrt(delta))/(2*a) )
	print( "Pierwiastek x_2: ", (-b+sqrt(delta))/(2*a) )
elif delta == 0:
	print( "Pierwiastek x_0: ", -b/(2*a) )
else:
	print("brak pierwiastków równania")