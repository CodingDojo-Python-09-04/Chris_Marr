# Make dictionary containing my:
## Name
## Age
## Country of birth
## Favorite language

about_me = {
	'name': 'chris',
	'age': '22',
	'country of origin': 'USA',
	'favorite language': 'Python'
}
# print about_me['name']
def reading_dictionaries():
	for key, value in about_me.iteritems():
		print "My " + key + " is " + value + "."

reading_dictionaries()











