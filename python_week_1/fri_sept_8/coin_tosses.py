import random
def coin_tosses():
	print "Starting the program..."
	count = 1
	heads = 0
	tails = 0
	while count <= 5000:	
		random_num = random.randint(1, 2)
		if random_num == 1:
			heads +=1
			print "Attempt #" + str(count) + ": Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far."
		else:
			tails +=1
			print "Attempt #" + str(count) + ": Throwing a coin... It's a tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far."
		count +=1
	print "Ending the program, thank you!"

coin_tosses()