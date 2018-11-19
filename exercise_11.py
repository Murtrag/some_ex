#!/usr/bin/python3

for num in range(1,102):
	if not num%3:
		print("Fizz", end="")
	if not num%5:
		print("Buzz", end="")
	if num%3 and num%5:
		print(num, end="")
	print("\n")

