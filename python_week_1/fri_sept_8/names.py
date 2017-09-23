print "---Part I---"
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names():
	for dicts in students:
		print dicts['first_name'] + ' ' + dicts['last_name']
names()
print "---Part II---"
#-----------------------------------------------
# Part II:
users = {
	'Students': [
    	{'first_name':  'Michael', 'last_name' : 'Jordan'},
    	{'first_name' : 'John', 'last_name' : 'Rosales'},
    	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
    	{'first_name' : 'KB', 'last_name' : 'Tonel'}
	],
	'Instructors': [
    	{'first_name' : 'Michael', 'last_name' : 'Choi'},
    	{'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}

def names_part_2(dictionary):
	for lists in dictionary:
		print lists
		count = 0
		for people in dictionary[lists]:
			count +=1
			temp = people['first_name'] + ' ' + people['last_name']
			temp = temp + ' ' + str(len(temp)-1)
			print str(count) + ' - ' + temp

names_part_2(users)



