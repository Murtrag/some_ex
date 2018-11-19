def fib(n):
	if n <= 1:		
		return 0 if n==0 else 1

	else:
		return sum([fib(n-2),fib(n-1)])


#print(fib(5))
