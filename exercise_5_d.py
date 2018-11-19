def chessboard(n=8):
	line = "# "*int(n/2)

	chessboard_str=""
	for count in range(n):
		if not count%2:
			chessboard_str+=line+"\n"
		else:			
			chessboard_str+=" "+line+"\n"
	else:
		return chessboard_str


#print(chessboard(10))