# Odd/Even:
def odd_even():
	for x in range(1, 2001):
		if x % 2 != 0:
			print "Number is " + str(x) + ". This is an odd number."
		else:
			print "Number is " + str(x) + ". This is an even number."

odd_even()
#-------------------------
# Multiply:
a = [2,4,10,16]

def multiply(l, num):
	new_list = []
	for x in l:
		new_list.append(x * num)
	return new_list

print multiply(a, 5)
#-------------------------
# Hacker Challenge:
def layered_multiples(arr):
	new_array = []
	for y in arr:
		new_array2 = []
		count = 0
		while count < y:	
			new_array2.append(1)
			count +=1
		new_array.append(new_array2)
	return new_array

test = layered_multiples(multiply([2,4,5],3))
print test