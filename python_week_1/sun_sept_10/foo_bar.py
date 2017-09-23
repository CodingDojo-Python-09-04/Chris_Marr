def foo_bar():	
	for num in range(100, 10001):	
		while num <= 100000:
			for i in range(2,num):
				if num % i == 0:
					print "Foo"
					# break 
				else:
					print "FooBar"
			low = 0
			high = num // 2
			root = high
			while root * root != num:
				root = (low + high) // 2
				if low + 1 >= high:
					print "FooBar"
				if root * root > num:
					high = root
				else:
					low = root
			print "Bar"

foo_bar()