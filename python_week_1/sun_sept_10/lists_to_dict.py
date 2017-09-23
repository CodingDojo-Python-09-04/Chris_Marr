def make_dict(arr1, arr2):
	new_dict = {}
	count = 0
	while count < len(arr1):
		new_dict[arr1[count]] = arr2[count]
		count +=1
	print new_dict
	return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

make_dict(name, favorite_animal)