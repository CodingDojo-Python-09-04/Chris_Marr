# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
words_list = words.split()
words_index = words_list.index("day.")
print words_index
words_list[words_index] = "month."
print " ".join(words_list)
#--------------------
# Min and Max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)
#--------------------
# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[-1]
y = []
y.append(x[0])
y.append(x[-1])
print y
#---------------------
# New List
x_2 = [19,2,54,-2,7,12,98,32,10,-3,6]
x_2.sort()
y_first_half = []
y_second_half = []
count = 0
half_list_index = len(x_2)/2
for item in x_2:	
	if count < half_list_index:
		y_first_half.append(item)
		count +=1
	else:
		y_second_half.append(item)
		count +=1	
y_first_half.append(y_second_half)
print y_first_half