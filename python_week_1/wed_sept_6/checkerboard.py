def checkerboard():
	count = 0
	while count < 8:
		if count % 2 == 0:
			print "* * * * "
			count +=1
		else:
			print " * * * *"
			count +=1

checkerboard() 