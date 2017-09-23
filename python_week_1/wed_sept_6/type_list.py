l = ['magical unicorns',19,'hello',98.98,'world']

def type_list(lst):
	running_sum = 0
	running_string = ""
	for x in lst:
		if isinstance(x, str):
			running_string += x
			running_string += " "
		elif isinstance(x, int):
			running_sum += x
		elif isinstance(x, float):
			running_sum += x
	print "Sum: " + str(running_sum)
	print "Your complete string is: " + running_string

type_list(l)
