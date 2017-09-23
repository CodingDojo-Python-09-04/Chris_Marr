def multiplication_table():
	x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	row = "x "
	for item in x:
		row += "{} ".format(item)
	print row

	for i in range(1, 13):
		row = [y*i for y in range(1, len(x)+1)]
		sub = ""
		for item in row:
			sub += "{} ".format(item)
		print sub

multiplication_table()