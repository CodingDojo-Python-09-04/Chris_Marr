import random
def scores_and_grades():
	print "Scores and Grades:"
	count = 1
	while count <= 10:
		random_num = random.randint(60, 100)
		if random_num <= 69:
			print "Score: " + str(random_num) + "; Your grade is a D."
		elif random_num <= 79:
			print "Score: " + str(random_num) + "; Your grade is a C."
		elif random_num <= 89:
			print "Score: " + str(random_num) + "; Your grade is a B."
		elif random_num <= 100:
			print "Score: " + str(random_num) + "; Your grade is an A."
		count +=1
	print "End of the program. Bye!"
scores_and_grades()