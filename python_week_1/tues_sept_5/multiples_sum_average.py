# Multiples
## Part I
for number in range(1, 1001):
	print number
## Part II
for five in range(1, 1000001):
	if five % 5 == 0:
		print five
	else:
		continue
#-------------------------
# Sum List
a = [1, 2, 5, 10, 255, 3]
list_sum = sum(a)
print list_sum
#-------------------------
# Average List
list_avg = list_sum/len(a)
print list_avg