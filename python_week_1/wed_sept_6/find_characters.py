def find_characters(list, character):
	new_list = []
	for x in list:
		if character in x:
			new_list.append(x)
		else:
			continue
	print new_list

word_list = ['hello','world','my','name','is','Anna']

find_characters(word_list, "o")