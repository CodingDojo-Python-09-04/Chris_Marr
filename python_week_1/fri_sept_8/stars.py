# Part I
# def draw_stars(num_list):
# 	for number in num_list:
# 		count = 0
# 		empty_str = ""
# 		while count < number:
# 			empty_str += "*"
# 			count +=1
# 		print empty_str

y = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(x)

# ------------------------------
# Part II
def draw_stars(the_list):
	for item in the_list:
		if isinstance(item, int):
			count = 0
			empty_str = ""
			while count < item:
				empty_str += "*"
				count +=1
			print empty_str
		elif isinstance(item, str):
			count = 0
			empty_str = ""
			while count < len(item):
				empty_str += item[:1].lower()
				count +=1
			print empty_str

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(y)
draw_stars(x)