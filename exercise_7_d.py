def histogram(list):
	#if any(not type(item) == type(1) for item in list): 
	if any(not isinstance(item, int) for item in list):  
		return None
	else:
		return "\n".join(["#"*n for n in list])

#print(histogram([1,2,0,5, "a"]))
